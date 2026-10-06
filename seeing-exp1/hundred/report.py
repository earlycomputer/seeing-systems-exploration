"""1h's results, by arm, on the five-plus-two targets. Every number from the logged runs, reads and quizzes.

    python -m hundred.report            # writes hundred/results/results.md
    python -m hundred.report --dry      # from the dry-run folders, printed only
"""

from __future__ import annotations

import argparse
import glob
import json
import statistics
import sys
from pathlib import Path

from hundred.settings import ARMS, DRYRUN_DIR, QUIZ_DIR, READS_DIR, RESULTS_DIR, RUNS_DIR


def load(pattern: str) -> list[dict]:
    return [json.loads(Path(f).read_text()) for f in sorted(glob.glob(pattern))]


def ratio(a: float | None, b: float | None) -> str:
    return "n/a" if not a or not b else f"{a / b:.1f}x"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args(argv)
    base = DRYRUN_DIR if args.dry else RESULTS_DIR
    worlds = load(str((DRYRUN_DIR / "runs" if args.dry else RUNS_DIR) / "*" / "*" / "world.json"))
    reads = load(str((DRYRUN_DIR / "reads" if args.dry else READS_DIR) / "*.json"))
    quiz = load(str((DRYRUN_DIR / "quiz" if args.dry else QUIZ_DIR) / "*.json"))
    out = [f"# Experiment 1h: {len(worlds)} worlds, {len(reads)} reads, {len(quiz)} quizzes, "
           f"${sum(w['cost_usd'] for w in worlds) + sum(r['cost_usd'] for r in reads) + sum(q['cost_usd'] for q in quiz):.2f}", ""]

    out += ["## Building worlds", "",
            "| Arm | Worked | Right first write | Said it worked, didn't | Tokens per working world | Output tokens per "
            "working world | Seconds per working world | Final description, median chars |",
            "|---|---|---|---|---|---|---|---|"]
    per = {}
    for arm in ARMS:
        ws = [w for w in worlds if w["arm"] == arm]
        if not ws:
            continue
        ok = [w for w in ws if w["passes_final"]]
        wrong = sum(1 for w in ws if w.get("claims_works") and not w["passes_final"])
        tok = sum(w["tokens"]["total"] for w in ws) / len(ok) if ok else None
        outt = sum(w["tokens"]["output"] for w in ws) / len(ok) if ok else None
        secs = sum(w["seconds"] for w in ws) / len(ok) if ok else None
        chars = [w["final_chars"] for w in ws if w.get("final_chars")]
        per[arm] = {"tok": tok, "wrong": wrong / len(ws), "secs": secs}
        out.append(f"| {arm} | {len(ok)}/{len(ws)} | {sum(w['passes_first'] for w in ws)}/{len(ws)} | {wrong}/{len(ws)} "
                   f"| {tok or 0:,.0f} | {outt or 0:,.0f} | {secs or 0:,.0f} | "
                   f"{statistics.median(chars) if chars else 0:,.0f} |")
    if "blind" in per and "language" in per:
        out += ["", f"Language against blind XML: tokens per working world {ratio(per['blind']['tok'], per['language']['tok'])} "
                f"fewer, seconds {ratio(per['blind']['secs'], per['language']['secs'])} fewer, wrong claims "
                f"{ratio(per['blind']['wrong'], per['language']['wrong'])} fewer."]

    out += ["", "## Reading a world before it runs (foresight, shared understanding)", "",
            "| Format read | Reads | Statements judged right | Both readers agree | Agreeing and right | Tokens read per "
            "statement |", "|---|---|---|---|---|---|"]
    for fmt in ("xml", "world"):
        rs = [r for r in reads if r["format"] == fmt and r["correct"] is not None]
        if not rs:
            continue
        n = sum(len(r["truth"]) for r in rs)
        pairs = {}
        for r in rs:
            pairs.setdefault(r["world"], []).append(r)
        agree = agree_right = total = 0
        for both in pairs.values():
            if len(both) == 2:
                for a, b, t in zip(both[0]["said"], both[1]["said"], both[0]["truth"]):
                    total += 1
                    agree += a == b
                    agree_right += a == b == t
        tokens = sum(r["tokens"]["input"] + r["tokens"]["output"] for r in rs)
        out.append(f"| {'language' if fmt == 'world' else 'XML'} | {len(rs)} | {sum(r['correct'] for r in rs)}/{n} | "
                   f"{agree}/{total} | {agree_right}/{total} | {tokens / n:,.0f} |")

    out += ["", "## Questions about a run (understanding)", "",
            "| Form | Quizzes | Answers right | Evidence, mean chars | Tokens read per right answer |", "|---|---|---|---|---|"]
    for form in ("raw", "words"):
        qs = [q for q in quiz if q["form"] == form]
        if not qs:
            continue
        rightn = sum(q["right"] for q in qs)
        tokens = sum(q["tokens"]["input"] + q["tokens"]["output"] for q in qs)
        out.append(f"| {form} | {len(qs)} | {rightn}/{sum(q['asked'] for q in qs)} | "
                   f"{statistics.mean(q['evidence_chars'] for q in qs):,.0f} | {tokens / rightn if rightn else 0:,.0f} |")
    text = "\n".join(out) + "\n"
    if not args.dry:
        (base / "results.md").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
