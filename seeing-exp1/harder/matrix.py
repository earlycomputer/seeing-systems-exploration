"""Experiment 1d: run every world, skipping worlds already done.

    python -m harder.matrix --plan                    # list the worlds and a rough cost; no calls
    python -m harder.matrix --first                   # seed 0 of every brief and arm, both models (28 worlds)
    python -m harder.matrix                           # all 112: 7 briefs x 2 arms x 4 seeds x 2 models
    python -m harder.matrix --models dry-run --jobs 8 # plumbing test

Every call checks 1d's approved ceiling and the program cap (harder/budget.py); past either, worlds fail before calling.
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from loop.models import MODELS
from harder import budget
from harder import run as run_world
from harder.settings import ARMS, BRIEFS, DRYRUN_DIR, MODELS as MATRIX_MODELS, RUNS_DIR, SEEDS

# Rough, for --plan only: 1c's measured cost per world (Opus 5.5 $0.34, GPT-6.1 Sol $0.08).
EST_USD = {"opus-5.5": 0.34, "gpt-6.1": 0.08}


def worlds(first: bool) -> list[tuple[str, str, int]]:
    if first:
        return [(b, a, 0) for b in BRIEFS for a in ARMS]
    return [(b, a, s) for b in BRIEFS for a in ARMS for s in SEEDS]


def done(model: str, w: tuple) -> bool:
    root = DRYRUN_DIR / "runs" if MODELS[model].provider == "dry" else RUNS_DIR
    return any((root / run_world.world_id(model, *w)).glob("*/world.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=list(MATRIX_MODELS), choices=sorted(MODELS))
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--first", action="store_true")
    ap.add_argument("--rerun", action="store_true")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()

    todo = [(m, w) for m in args.models for w in worlds(args.first) if args.rerun or not done(m, w)]
    est = sum(EST_USD.get(m, 0.0) for m, _ in todo)
    s = budget.spent()
    print(f"{len(todo)} worlds to run; rough cost ${est:.2f}; spent so far: " +
          ", ".join(f"{k} ${v:.2f}" for k, v in s.items()) + f" (total ${sum(s.values()):.2f} of $100)")
    if args.plan:
        for m, w in todo:
            print("  ", run_world.world_id(m, *w))
        return 0

    def one(m, w):
        b, a, sd = w
        return run_world.main(["--model", m, "--brief", b, "--arm", a, "--seed", str(sd), "--effort", args.effort])

    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(one, m, w): (m, w) for m, w in todo}
        for f in as_completed(futures):
            m, w = futures[f]
            try:
                if f.result() != 0:
                    failures.append((m, w, "nonzero exit"))
            except BaseException as e:  # keep going; a failed call is reported, not fatal
                failures.append((m, w, repr(e)))
                print(f"FAILED {run_world.world_id(m, *w)}: {e!r}", file=sys.stderr)
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; 1d spent ${budget.spent()['exp1d']:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
