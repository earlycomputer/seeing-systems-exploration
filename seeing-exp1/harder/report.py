"""Build harder/results/results.md from the world JSON. Never edit it by hand.

    python -m harder.report
    python -m harder.report --runs .dryrun/harder/runs --out .dryrun/harder     # against dry runs

Uses the latest run per world. A summary written after reading the tables goes in results/summary.md and is
copied in verbatim.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from loop.models import MODELS
from harder import budget
from harder.settings import ARMS, BREAKS, BRIEFS, MAX_ROUNDS, RESULTS_DIR, RUNS_DIR


def load(runs_dir: Path) -> list[dict]:
    latest = {}
    for p in sorted(runs_dir.glob("*/*/world.json")):
        w = json.loads(p.read_text())
        latest[w["world"]] = w
    return list(latest.values())


def n_of(ws, key) -> str:
    vals = [w.get(key) for w in ws if w.get(key) is not None]
    return f"{sum(bool(v) for v in vals)} of {len(vals)}" if vals else "n/a"


def models(ws):
    return sorted({w["model"] for w in ws}, key=lambda m: list(MODELS).index(m))



def broken_table(ws) -> list[str]:
    lines = ["| Model | Readback | Fixed in the end | Tried a fix | Model's last claim right | Said it works while broken | "
             "Rounds used | Cost per world |", "|---|---|---|---|---|---|---|---|"]
    for m in models(ws):
        for a in ARMS:
            rs = [w for w in ws if w["model"] == m and w["arm"] == a and w["kind"] == "broken"]
            if not rs:
                continue
            wrong_ok = sum(1 for w in rs if not w["passes_final"] and w.get("claims_works"))
            lines.append(f"| {MODELS[m].label} | {a} | {n_of(rs, 'passes_final')} | {n_of(rs, 'tried_fix')} | "
                         f"{n_of(rs, 'claim_correct')} | {wrong_ok} of {sum(1 for w in rs if not w['passes_final'])} | "
                         f"{sum(w['rounds'] for w in rs) / len(rs):.1f} | ${sum(w['cost_usd'] for w in rs) / len(rs):.3f} |")
    return lines


def new_table(ws) -> list[str]:
    lines = ["| Model | Readback | Loads | Works as first written | Works in the end | Fixed of those failing first | "
             "Model's last claim right | Rounds used | Cost per world |", "|---|---|---|---|---|---|---|---|---|"]
    for m in models(ws):
        for a in ARMS:
            rs = [w for w in ws if w["model"] == m and w["arm"] == a and w["kind"] == "new"]
            if not rs:
                continue
            ff = [w for w in rs if not w["passes_first"]]
            lines.append(f"| {MODELS[m].label} | {a} | {n_of(rs, 'loads')} | {n_of(rs, 'passes_first')} | "
                         f"{n_of(rs, 'passes_final')} | {sum(w['passes_final'] for w in ff)} of {len(ff)} | "
                         f"{n_of(rs, 'claim_correct')} | {sum(w['rounds'] for w in rs) / len(rs):.1f} | "
                         f"${sum(w['cost_usd'] for w in rs) / len(rs):.3f} |")
    return lines


def by_brief(ws) -> list[str]:
    by = defaultdict(list)
    for w in ws:
        by[(w["model"], w["brief"], w["arm"])].append(w)
    lines = ["| Model | Brief | Kind | Readback | First file works | Works in the end | Failing checks at the end |",
             "|---|---|---|---|---|---|---|"]
    for m in models(ws):
        for b in BRIEFS:
            for a in ARMS:
                rs = by.get((m, b, a), [])
                if not rs:
                    continue
                fails = sorted({k for w in rs for k, v in (w.get("final_checks") or {}).items() if not v})
                lines.append(f"| {MODELS[m].label} | {b} | {BRIEFS[b]['kind']} | {a} | {n_of(rs, 'passes_first')} | "
                             f"{n_of(rs, 'passes_final')} | "
                             f"{'; '.join(fails) or ('did not load' if not all(w['loads'] for w in rs) else '')} |")
    return lines


def embarrassment(ws) -> list[str]:
    out = []
    br = [w for w in ws if w["kind"] == "broken"]
    if not br:
        return out
    p = [w for w in br if w["arm"] == "picture"]
    t = [w for w in br if w["arm"] == "text"]
    out.append(f"- Broken worlds fixed, both models: picture {n_of(p, 'passes_final')}, text only {n_of(t, 'passes_final')}.")
    for m in models(ws):
        pm = [w for w in p if w["model"] == m]
        tm = [w for w in t if w["model"] == m]
        out.append(f"- {MODELS[m].label}: picture fixed {n_of(pm, 'passes_final')} broken worlds within {MAX_ROUNDS} rounds, "
                   f"text only {n_of(tm, 'passes_final')}.")
    return out


def breaks_section() -> list[str]:
    return ["| World | The break |", "|---|---|"] + [f"| {b} | {BREAKS[b][2]} |" for b in BREAKS]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=RUNS_DIR)
    ap.add_argument("--out", type=Path, default=RESULTS_DIR)
    args = ap.parse_args()
    ws = load(args.runs)
    s = budget.spent()
    md = ["# Experiment 1d results: harder worlds", "",
          f"Generated by `python -m harder.report` from the world JSON; never edited by hand. {len(ws)} worlds; "
          f"1d spend ${s['exp1d']:.2f}; all experiments ${sum(s.values()):.2f} of $100.", "",
          "## The breaks", "", *breaks_section(), "",
          "## Broken worlds: checked and fixed from the brief", "", *broken_table(ws), "",
          "## New worlds: written from the brief", "", *new_table(ws), "",
          "## Embarrassment tests", "", *(embarrassment(ws) or ["Not run yet."]), "",
          "## By brief", "", *by_brief(ws), ""]
    summary = args.out / "summary.md"
    if summary.exists():
        md += ["## Summary", "", summary.read_text().strip(), ""]
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "results.md").write_text("\n".join(md))
    print(f"{len(ws)} worlds -> {args.out / 'results.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
