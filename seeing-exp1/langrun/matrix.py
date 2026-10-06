"""Experiment 1f: run every world, skipping worlds already done.

    python -m langrun.matrix --plan                     # list the worlds and a rough cost; no calls
    python -m langrun.matrix --seeds 0                  # seed 0 of every brief and arm, both models (40 worlds)
    python -m langrun.matrix                            # all: 10 briefs x 2 arms x 2 seeds x 2 models (80 worlds)
    python -m langrun.matrix --models dry-run --jobs 8  # plumbing test

Every call checks the joint ceiling for 1e and 1f and the program cap (history/budget.py).
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from loop.models import MODELS
from history import budget
from langrun import run as run_world
from langrun.settings import ARMS, BRIEFS, DRYRUN_DIR, MODELS as MATRIX_MODELS, RUNS_DIR, SEEDS

# Rough, for --plan only: 1d's cost per new world, raised for the language's longer prompt.
EST_USD = {("opus-5.5", "xml"): 0.30, ("opus-5.5", "language"): 0.45, ("gpt-6.1", "xml"): 0.08, ("gpt-6.1", "language"): 0.12}


def done(model: str, w: tuple) -> bool:
    root = DRYRUN_DIR / "runs" if MODELS[model].provider == "dry" else RUNS_DIR
    return any((root / run_world.world_id(model, *w)).glob("*/world.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=list(MATRIX_MODELS), choices=sorted(MODELS))
    ap.add_argument("--briefs", nargs="+", default=list(BRIEFS), choices=list(BRIEFS))
    ap.add_argument("--arms", nargs="+", default=list(ARMS), choices=ARMS)
    ap.add_argument("--seeds", nargs="+", type=int, default=list(SEEDS))
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--rerun", action="store_true")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()

    todo = [(m, (b, a, s)) for m in args.models for s in args.seeds for b in args.briefs for a in args.arms
            if args.rerun or not done(m, (b, a, s))]
    est = sum(EST_USD.get((m, w[1]), 0.0) for m, w in todo)
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
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; 1f spent ${budget.spent()['exp1f']:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
