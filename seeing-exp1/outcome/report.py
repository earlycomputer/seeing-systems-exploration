"""Build outcome/results/results.md and failures.md from the run JSON. Never edit those files by hand.

    python -m outcome.report
    python -m outcome.report --runs .dryrun/outcome/runs --out .dryrun/outcome     # against dry runs

Uses the latest run per cell. A summary written after reading the tables goes in results/summary.md and is
copied in verbatim.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from loop.models import MODELS
from outcome import budget
from outcome.settings import BASE_RECORD, CONDITIONS, MISSES, RESULTS_DIR, RUNS_DIR, SHOT_SCENE

LABEL = {"text": "Text only", "numbers": "Numbers", "camera_128": "Camera, 128 px", "camera_64": "Camera, 64 px",
         "drafting_128": "Drafting, 128 px", "drafting_64": "Drafting, 64 px"}


def load_runs(runs_dir: Path) -> list[dict]:
    latest = {}
    for path in sorted(runs_dir.glob("*/*/run.json")):  # timestamps sort, so the last one wins
        run = json.loads(path.read_text())
        latest[run["cell"]] = run
    return list(latest.values())


def count(rs: list[dict], key: str) -> str:
    vals = [r.get(key) for r in rs if r.get(key) is not None]
    return f"{sum(bool(v) for v in vals)} of {len(vals)}" if vals else "n/a"


def order(runs):
    models = sorted({r["model"] for r in runs}, key=lambda m: list(MODELS).index(m))
    return models


def by_condition(runs: list[dict]) -> list[str]:
    by = defaultdict(list)
    for r in runs:
        by[(r["model"], r["condition"])].append(r)
    lines = ["| Model | Readback | Direction named | Made after one correction | Made after two | "
             "Tokens per run | Cost per run |", "|---|---|---|---|---|---|---|"]
    for m in order(runs):
        for c in CONDITIONS:
            rs = by.get((m, c), [])
            if not rs:
                continue
            tokens = round(sum(r["tokens"]["total"] for r in rs) / len(rs))
            cost = sum(r["cost_usd"] for r in rs) / len(rs)
            lines.append(f"| {MODELS[m].label} | {LABEL[c]} | {count(rs, 'named_correctly')} | "
                         f"{count(rs, 'made_after_one')} | {count(rs, 'made_after_two')} | {tokens:,} | ${cost:.3f} |")
    return lines


def by_miss(runs: list[dict]) -> list[str]:
    by = defaultdict(list)
    for r in runs:
        by[(r["model"], r["condition"], r["miss"])].append(r)
    lines = ["| Model | Readback | Miss | Named | What it named | Made after one | Made after two |",
             "|---|---|---|---|---|---|---|"]
    for m in order(runs):
        for c in CONDITIONS:
            for miss in MISSES:
                rs = by.get((m, c, miss), [])
                if not rs:
                    continue
                named = ", ".join(str(r.get("named")) for r in sorted(rs, key=lambda r: r["seed"]))
                lines.append(f"| {MODELS[m].label} | {LABEL[c]} | {miss} | {count(rs, 'named_correctly')} | {named} | "
                             f"{count(rs, 'made_after_one')} | {count(rs, 'made_after_two')} |")
    return lines


def embarrassment(runs: list[dict]) -> list[str]:
    lines = []
    for m in order(runs):
        cam = [r for r in runs if r["model"] == m and r["condition"] == "camera_64" and r["miss"] in ("short", "long")]
        if cam:
            lines.append(f"- {MODELS[m].label}, camera at 64 px, short and long: named correctly "
                         f"{count(cam, 'named_correctly')}.")
        for res in (128, 64):
            pair = {v: [r for r in runs if r["model"] == m and r["condition"] == f"{v}_{res}"] for v in ("camera", "drafting")}
            if pair["camera"] and pair["drafting"]:
                lines.append(f"- {MODELS[m].label} at {res} px: direction named, drafting "
                             f"{count(pair['drafting'], 'named_correctly')} vs camera {count(pair['camera'], 'named_correctly')}; "
                             f"made after two, drafting {count(pair['drafting'], 'made_after_two')} vs camera "
                             f"{count(pair['camera'], 'made_after_two')}.")
    return lines


def base_section(scene_dir: Path) -> list[str]:
    rec_path = scene_dir / BASE_RECORD.name
    if not rec_path.exists():
        return []
    rec = json.loads(rec_path.read_text())
    a, b = rec["as_written"], rec["base"]
    lines = [f"Opus's shot as written: **{a['outcome']}** ({a['launch_speed']} m/s at {a['launch_elevation_deg']} deg, "
             f"apex {a['apex_z']} m). Base: {rec['made_by']}.", "",
             "| Miss | Step | Outcome in MuJoCo | Path crosses the rim plane (along, across) | Touched |",
             "|---|---|---|---|---|"]
    for miss, m in rec["misses"].items():
        for t in m["tried"]:
            j = t["judged"]
            unit = "deg" if MISSES[miss]["kind"] == "aim" else "of launch speed"
            step = f"{t['step']:+g} {unit}" if miss != "none" else "none"
            used = "" if t["clear_cut"] else " (not clear-cut; not used)"
            lines.append(f"| {miss} | {step}{used} | {j['outcome']} | {j['along']}, {j['across']} m | "
                         f"{', '.join(dict.fromkeys(j['touched'])) or 'nothing'} |")
    return lines


def failures(runs: list[dict]) -> list[str]:
    out = ["# What the models said when wrong", "",
           "Every run whose first verdict named the wrong direction, with its own words. Generated.", ""]
    for r in sorted(runs, key=lambda r: r["cell"]):
        if r.get("named_correctly"):
            continue
        v = r["turns"][0]["verdict"]
        out += [f"## {r['cell']}", "",
                f"Truth: {r['truth_label']}. Named: {r.get('named')}. Evidence: {v.get('evidence')}. "
                f"Made after one: {r['made_after_one']}; after two: {r['made_after_two']}.", "",
                f"> {v.get('description', v.get('parse_error', ''))}", "", f"Run: `{r['run_dir']}`", ""]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=RUNS_DIR)
    ap.add_argument("--out", type=Path, default=RESULTS_DIR)
    args = ap.parse_args()
    runs = load_runs(args.runs)
    scene_dir = SHOT_SCENE.parent if args.out == RESULTS_DIR else args.out / "scene"
    s = budget.spent()
    md = ["# Experiment 1b results: see the outcome", "",
          "Generated by `python -m outcome.report` from the run JSON; never edited by hand. "
          f"{len(runs)} runs; 1b spend ${s['exp1b']:.2f} (experiment 1: ${s['exp1']:.2f}).", "",
          "## The base shot and the deliberate misses", "", *base_section(scene_dir), "",
          "## By readback", "", *by_condition(runs), "",
          "## Embarrassment tests", "", *(embarrassment(runs) or ["Not run yet."]), "",
          "## By readback and miss", "", *by_miss(runs), ""]
    summary = args.out / "summary.md"
    if summary.exists():
        md += ["## Summary", "", summary.read_text().strip(), ""]
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "results.md").write_text("\n".join(md))
    (args.out / "failures.md").write_text("\n".join(failures(runs)))
    print(f"{len(runs)} runs -> {args.out / 'results.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
