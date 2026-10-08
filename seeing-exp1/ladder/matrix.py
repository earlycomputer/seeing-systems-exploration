"""Experiment 1j: run every ladder world, skipping worlds already done, then judge each finished world.

    python -m ladder.matrix --plan                        # list the worlds; no calls
    python -m ladder.matrix --steps 16 --seeds 0 --families cascade   # a cost check on one family's longest chain
    python -m ladder.matrix                               # everything
    python -m ladder.matrix --dry                         # plumbing test, no calls
    python -m ladder.matrix --1k --arms language --steps 8 16   # 1k: the fixed language, into ladder/results_1k/

Every call checks 1j's ceiling and the program cap (ladder/budget.py). Judging uses hundred/judge.py with the run in
words with openings (hundred/words.py); verdicts go to ladder/results/judge/.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from hundred import judge as judge_mod, run as run_world
from ladder import briefs as briefs_mod, budget
from ladder import settings
from ladder.settings import ARMS, DRYRUN_DIR, JUDGE, LEVELS, MODEL, SEEDS

# 1j by default; --1k points these at ladder/results_1k/ and 1k's ceiling
RUNS_DIR, JUDGE_DIR, SPEND_LEDGER, CHECK, EXP, RUN_FLAG = (settings.RUNS_DIR, settings.JUDGE_DIR, settings.SPEND_LEDGER,
                                                           budget.check, "exp1j", "--ladder")


def runs_root(dry: bool) -> Path:
    return DRYRUN_DIR / ("runs_1k" if EXP == "exp1k" else "runs") if dry else RUNS_DIR


def done(model: str, w: tuple, dry: bool) -> bool:
    return any((runs_root(dry) / run_world.world_id(model, *w)).glob("*/world.json"))


def judge_all(dry: bool, jobs: int) -> None:
    out_dir = (DRYRUN_DIR / "judge") if dry else JUDGE_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    things = {k: b["things"] for k, b in briefs_mod.load().items()}
    todo = []
    for f in sorted(glob.glob(str(runs_root(dry) / "*" / "*" / "world.json"))):
        rec = json.loads(Path(f).read_text())
        if rec.get("final_test") and not (out_dir / f"{rec['world']}__{JUDGE}.json").exists():
            todo.append((rec, Path(f).parent))
    print(f"{len(todo)} worlds to judge")
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        list(pool.map(lambda t: judge_mod.judge_one(*t, "dry-run" if dry else JUDGE, out_dir, dry, "openings",
                                                    SPEND_LEDGER, CHECK, things), todo))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--arms", nargs="+", default=list(ARMS), choices=ARMS)
    ap.add_argument("--seeds", nargs="+", type=int, default=list(SEEDS))
    ap.add_argument("--steps", nargs="+", type=int, default=list(LEVELS), choices=LEVELS)
    ap.add_argument("--families", nargs="+", default=None)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--1k", dest="k", action="store_true", help="1k: the fixed language, ladder/results_1k/")
    args = ap.parse_args()
    global RUNS_DIR, JUDGE_DIR, SPEND_LEDGER, CHECK, EXP, RUN_FLAG
    if args.k:
        RUNS_DIR, JUDGE_DIR, SPEND_LEDGER, CHECK, EXP, RUN_FLAG = (settings.RUNS_1K_DIR, settings.JUDGE_1K_DIR,
                                                                   settings.SPEND_LEDGER_1K, budget.check_1k, "exp1k",
                                                                   "--ladder-1k")
    model = "dry-run-echo" if args.dry else MODEL
    briefs = [b for b in briefs_mod.load().values()
              if b["steps"] in args.steps and (args.families is None or b["family"] in args.families)]
    todo = [(b["id"], a, s) for s in args.seeds for b in sorted(briefs, key=lambda b: -b["steps"]) for a in args.arms
            if not done(model, (b["id"], a, s), args.dry)]
    s = budget.spent()
    print(f"{len(todo)} worlds to run; spent so far: {EXP[3:]} ${s[EXP]:.2f}, all ${sum(s.values()):.2f}")
    if args.plan:
        for w in todo:
            print("  ", run_world.world_id(model, *w))
        return 0
    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(run_world.main, ["--model", model, "--brief", b, "--arm", a, "--seed", str(sd),
                                                RUN_FLAG]): (b, a, sd) for b, a, sd in todo}
        for f in as_completed(futures):
            try:
                if f.result() != 0:
                    failures.append(futures[f])
            except BaseException as e:
                failures.append(futures[f])
                print(f"FAILED {run_world.world_id(model, *futures[f])}: {e!r}", file=sys.stderr)
    if not args.no_judge:
        judge_all(args.dry, args.jobs)
    s = budget.spent()
    print(f"done: {len(todo) - len(failures)} ok, {len(failures)} failed; {EXP[3:]} ${s[EXP]:.2f}, all ${sum(s.values()):.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
