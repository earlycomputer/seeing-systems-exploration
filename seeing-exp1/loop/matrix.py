"""Step 5: run every cell of the measurement matrix, plus the controls, skipping cells already done.

    python -m loop.matrix --plan                          # list the cells and a rough cost; no calls
    python -m loop.matrix                                 # Opus 5.5 and Gemini 3.1 Pro, 4 at a time
    python -m loop.matrix --models dry-run --jobs 8       # plumbing test

Per model: 3 errors x 3 resolutions x 3 seeds = 27 cells, plus the two controls from the handoff:
  A. unmodified scene at every resolution (seed 0): the model should report nothing wrong
  B. the embarrassment cell with the scene text withheld: hoop_low at 64 px, image only (seed 0)
--image-only-arm adds the full 27-cell image-only arm per model. It is a change to the design, so it is
off until a human says otherwise.
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import DRYRUN_DIR, RESOLUTIONS, RUNS_DIR, SEEDS, SPEND_CAP_USD
from loop import run as run_cell
from loop.models import MODELS, spent_usd
from scene.sim import ERRORS

# Rough, for --plan only: two calls per run, ~4k tokens in and ~4k out (mostly reasoning) per call.
EST_TOKENS_IN, EST_TOKENS_OUT = 8_000, 8_000


def cells(model: str, image_only_arm: bool) -> list[tuple[int, str, int, bool]]:
    out = [(res, err, seed, False) for err in ERRORS for res in RESOLUTIONS for seed in SEEDS]
    out += [(res, "none", 0, False) for res in RESOLUTIONS]  # control A
    out += [(64, "hoop_low", 0, True)]  # control B
    if image_only_arm:
        out += [(res, err, seed, True) for err in ERRORS for res in RESOLUTIONS for seed in SEEDS
                if (res, err, seed) != (64, "hoop_low", 0)]
    return out


def done(model: str, cell: tuple) -> bool:
    root = DRYRUN_DIR / "runs" if MODELS[model].provider == "dry" else RUNS_DIR
    return any((root / run_cell.cell_id(model, *cell)).glob("*/run.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=["opus-5.5", "gemini-3.1-pro"], choices=sorted(MODELS))
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--image-only-arm", action="store_true")
    ap.add_argument("--rerun", action="store_true", help="run cells that already have a result")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()

    todo = [(m, c) for m in args.models for c in cells(m, args.image_only_arm) if args.rerun or not done(m, c)]
    est = sum(EST_TOKENS_IN * MODELS[m].usd_per_mtok_in / 1e6 + EST_TOKENS_OUT * MODELS[m].usd_per_mtok_out / 1e6
              for m, _ in todo)
    print(f"{len(todo)} cells to run; rough cost ${est:.2f}; spent so far ${spent_usd():.2f} of ${SPEND_CAP_USD:.0f}")
    if args.plan:
        for m, (res, err, seed, img) in todo:
            print("  ", run_cell.cell_id(m, res, err, seed, img))
        return 0

    def one(m, cell):
        res, err, seed, img = cell
        argv = ["--model", m, "--res", str(res), "--error", err, "--seed", str(seed), "--effort", args.effort]
        return run_cell.main(argv + (["--image-only"] if img else []))

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
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; spent ${spent_usd():.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
