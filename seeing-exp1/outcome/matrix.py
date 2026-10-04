"""Experiment 1b: run every cell, skipping cells already done.

    python -m outcome.matrix --plan                    # list the cells and a rough cost; no calls
    python -m outcome.matrix --first                   # the first real runs, shown to a human before the rest
    python -m outcome.matrix                           # all 144: 4 misses x 6 conditions x 3 seeds x 2 models
    python -m outcome.matrix --models dry-run --jobs 8 # plumbing test
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from loop.models import MODELS
from outcome import budget
from outcome import run as run_cell
from outcome.settings import CONDITIONS, DRYRUN_DIR, MISSES, MODELS as MATRIX_MODELS, RUNS_DIR, SEEDS

# Rough, for --plan only: about 3 calls per run, ~6k tokens in and ~6k out (mostly reasoning) per call.
EST_TOKENS_IN, EST_TOKENS_OUT = 18_000, 18_000

# Seed 0 of eight cells per model: every condition, every miss, and both embarrassment tests' cells.
FIRST = [("text", "short"), ("numbers", "long"), ("camera_128", "left"), ("camera_64", "short"),
         ("camera_64", "long"), ("drafting_128", "none"), ("drafting_64", "short"), ("drafting_64", "long")]


def cells(first: bool) -> list[tuple[str, str, int]]:
    if first:
        return [(c, m, 0) for c, m in FIRST]
    return [(c, m, s) for m in MISSES for c in CONDITIONS for s in SEEDS]


def done(model: str, cell: tuple) -> bool:
    root = DRYRUN_DIR / "runs" if MODELS[model].provider == "dry" else RUNS_DIR
    return any((root / run_cell.cell_id(model, *cell)).glob("*/run.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=list(MATRIX_MODELS), choices=sorted(MODELS))
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--first", action="store_true")
    ap.add_argument("--rerun", action="store_true", help="run cells that already have a result")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()

    todo = [(m, c) for m in args.models for c in cells(args.first) if args.rerun or not done(m, c)]
    est = sum(EST_TOKENS_IN * MODELS[m].usd_per_mtok_in / 1e6 + EST_TOKENS_OUT * MODELS[m].usd_per_mtok_out / 1e6
              for m, _ in todo)
    s = budget.spent()
    print(f"{len(todo)} cells to run; rough cost ${est:.2f}; spent so far: experiment 1 ${s['exp1']:.2f}, "
          f"1b ${s['exp1b']:.2f}")
    if args.plan:
        for m, c in todo:
            print("  ", run_cell.cell_id(m, *c))
        return 0

    def one(m, cell):
        condition, miss, seed = cell
        return run_cell.main(["--model", m, "--condition", condition, "--miss", miss, "--seed", str(seed),
                              "--effort", args.effort])

    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(one, m, c): (m, c) for m, c in todo}
        for f in as_completed(futures):
            m, c = futures[f]
            try:
                if f.result() != 0:
                    failures.append((m, c, "nonzero exit"))
            except BaseException as e:  # keep going; a failed call is reported, not fatal
                failures.append((m, c, repr(e)))
                print(f"FAILED {run_cell.cell_id(m, *c)}: {e!r}", file=sys.stderr)
    s = budget.spent()
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; 1b spent ${s['exp1b']:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
