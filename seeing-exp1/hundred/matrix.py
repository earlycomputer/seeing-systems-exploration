"""Experiment 1h: run every world, skipping worlds already done.

    python -m hundred.matrix --plan                          # list the worlds; no calls
    python -m hundred.matrix --pilot                         # Jono's pilot: the first 5 briefs, 60 worlds
    python -m hundred.matrix --full                          # all 20 briefs, 240 worlds (needs Jono)
    python -m hundred.matrix --models dry-run --dry-briefs   # plumbing test

Every call checks 1h's ceiling and the program cap (hundred/budget.py).
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from loop.models import MODELS as ALL_MODELS
from hundred import briefs as briefs_mod, budget, run as run_world
from hundred.settings import ARMS, BRIEFS_FILE, DRY_BRIEFS_FILE, DRYRUN_DIR, MODELS, RUNS_DIR, SEEDS

PILOT_BRIEFS = 5


def done(model: str, w: tuple) -> bool:
    root = DRYRUN_DIR / "runs" if ALL_MODELS[model].provider == "dry" else RUNS_DIR
    return any((root / run_world.world_id(model, *w)).glob("*/world.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", default=list(MODELS), choices=sorted(ALL_MODELS))
    ap.add_argument("--arms", nargs="+", default=list(ARMS), choices=ARMS)
    ap.add_argument("--seeds", nargs="+", type=int, default=list(SEEDS))
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--dry-briefs", action="store_true")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()
    if not (args.pilot or args.full or args.dry_briefs):
        ap.error("say --pilot, --full or --dry-briefs")

    briefs = list(briefs_mod.load(DRY_BRIEFS_FILE if args.dry_briefs else BRIEFS_FILE))
    if args.pilot:
        briefs = briefs[:PILOT_BRIEFS]
    todo = [(m, (b, a, s)) for m in args.models for s in args.seeds for b in briefs for a in args.arms
            if not done(m, (b, a, s))]
    s = budget.spent()
    print(f"{len(todo)} worlds to run; spent so far: 1h ${s['exp1h']:.2f}, all ${sum(s.values()):.2f}")
    if args.plan:
        for m, w in todo:
            print("  ", run_world.world_id(m, *w))
        return 0

    def one(m, w):
        b, a, sd = w
        return run_world.main(["--model", m, "--brief", b, "--arm", a, "--seed", str(sd)]
                              + (["--dry-briefs"] if args.dry_briefs else []) + (["--full"] if args.full else []))

    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(one, m, w): (m, w) for m, w in todo}
        for f in as_completed(futures):
            m, w = futures[f]
            try:
                if f.result() != 0:
                    failures.append((m, w))
            except BaseException as e:
                failures.append((m, w))
                print(f"FAILED {run_world.world_id(m, *w)}: {e!r}", file=sys.stderr)
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; 1h spent ${budget.spent()['exp1h']:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
