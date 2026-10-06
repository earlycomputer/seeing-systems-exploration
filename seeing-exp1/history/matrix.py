"""Experiment 1e: run every world, skipping worlds already done.

    python -m history.matrix --plan                     # list the worlds and a rough cost; no calls
    python -m history.matrix --first                    # seed 0 of every brief, both models (10 worlds)
    python -m history.matrix                            # all 40: 5 broken briefs x 4 seeds x 2 models
    python -m history.matrix --models dry-run --jobs 8  # plumbing test

Every call checks the joint ceiling for 1e and 1f and the program cap (history/budget.py).
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from loop.models import MODELS
from harder.settings import MODELS as MATRIX_MODELS, SEEDS
from history import budget
from history import run as run_world
from history.settings import BRIEFS, DRYRUN_DIR, RUNS_DIR

# Rough, for --plan only: 1d's measured cost per broken world with a picture (Opus 5.5 $0.22, GPT-6.1 Sol $0.05).
EST_USD = {"opus-5.5": 0.22, "gpt-6.1": 0.05}


def worlds(first: bool) -> list[tuple[str, int]]:
    return [(b, s) for b in BRIEFS for s in ((0,) if first else SEEDS)]


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
        b, sd = w
        return run_world.main(["--model", m, "--brief", b, "--seed", str(sd), "--effort", args.effort])

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
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; 1e spent ${budget.spent()['exp1e']:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
