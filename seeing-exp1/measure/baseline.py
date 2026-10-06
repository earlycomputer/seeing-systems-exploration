"""Baselines for the five 100x targets, read from runs already logged (1d, 1e, 1f). No model calls.

    python measure/baseline.py <seeing-exp1 dir holding harder/, history/, langrun/>

Every number is computed from each run's world.json; nothing is typed by hand.
"""

import glob
import json
import os
import statistics
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCES = [  # (experiment label, runs glob, keep only these kinds)
    ("1d", "harder/results/runs/*/*/world.json", {"broken"}),
    ("1e", "history/results/runs/*/*/world.json", {"broken"}),
    ("1f", "langrun/results/runs/*/*/world.json", None),
]


def final_description_chars(w):
    """Size of the last world file the model wrote (language .world or XML)."""
    run_dir = os.path.join(ROOT, w["run_dir"])
    files = sorted(glob.glob(os.path.join(run_dir, "*.world")) + glob.glob(os.path.join(run_dir, "*.xml")),
                   key=os.path.getmtime)
    return os.path.getsize(files[-1]) if files else None


def row(label, arm, ws):
    worked = [w for w in ws if w["passes_final"]]
    wrong_claims = [w for w in ws if w.get("claims_works") and not w["passes_final"]]
    tokens = sum(w["tokens"]["total"] for w in ws)
    secs = sum(w["seconds"] for w in ws)
    out_tokens = sum(w["tokens"]["output"] for w in ws)
    sizes = [s for s in (final_description_chars(w) for w in ws) if s]
    per = lambda x: f"{x / len(worked):,.0f}" if worked else "n/a"
    return (f"| {label} | {arm} | {len(worked)}/{len(ws)} | {len(wrong_claims)} | {per(tokens)} | {per(out_tokens)} "
            f"| {per(secs)} | {statistics.mean(w['rounds'] for w in ws):.2f} "
            f"| {f'{statistics.median(sizes):,.0f}' if sizes else 'n/a'} |")


print("| Exp | Arm | Worked | Said it worked, didn't | Tokens per working world | Of which output, reasoning included "
      "| Seconds per working world | Runs per world | Final description, median chars |")
print("|---|---|---|---|---|---|---|---|---|")
for label, pattern, kinds in SOURCES:
    worlds = [json.load(open(p)) for p in glob.glob(os.path.join(ROOT, pattern))]
    worlds = [w for w in worlds if not w.get("dry_run") and (kinds is None or w["kind"] in kinds)]
    for arm in sorted({w["arm"] for w in worlds}):
        print(row(label, arm, [w for w in worlds if w["arm"] == arm]))
