"""Trust: an independent judge reads the brief and the run in words and says whether the world works.

    python -m hundred.judge                     # every 1h world with a built final file, judged by GPT-6.1
    python -m hundred.judge --dry               # plumbing test, no calls
    python -m hundred.judge --words openings    # the run in words with openings and stops by height (words.py)
    python -m hundred.judge --retest            # no calls: re-score saved verdicts against the current hidden test

1h's authors said "it works" about 17 to 25 of 50 broken worlds in the XML arms (hundred/results/results.md). The
judge never sees the hidden test or the author's claim; it gets the brief, its thing names, the settle check and the
run's history in words (history/narrate.py), the same words the run-in-words arms saw. Scored against the hidden test
(hidden.py, fixed reading). Verdicts go to hundred/results/judge/<world>__<judge>.json, or judge/openings/ for
`--words openings`; report: judge_report.py.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from history.narrate import history as plain_history
from hundred import budget, hidden, settle, words
from hundred.failures import final_xml
from hundred.settings import BRIEFS_FILE, DRYRUN_DIR, JUDGE_DIR, JUDGE_LEDGER, MODELS, PROMPTS, RUNS_DIR, SIM_SECONDS
from loop.models import extract_block, open_chat, text
from worlds.tests import run as run_world


THINGS = {b["id"]: b["things"] for b in json.loads(BRIEFS_FILE.read_text())}


def prompt(rec: dict, xml: str, kind: str = "plain"):
    r = run_world(xml, seconds=SIM_SECONDS)
    things = ", ".join(f"{t['name']} ({t['kind']}, {t['what']})" for t in THINGS[rec["brief"]])
    p = ((PROMPTS / "judge.md").read_text().replace("{brief}", rec["brief_text"]).replace("{things}", things)
         .replace("{seconds}", f"{SIM_SECONDS:g}").replace("{settle}", settle.say(settle.problems(xml)))
         .replace("{history}", (words.history if kind == "openings" else plain_history)(r)))
    return p, r


def judge_one(rec: dict, run_dir: Path, judge: str, out_dir: Path, dry: bool, kind: str = "plain") -> dict:
    xml = final_xml(rec, run_dir)
    p, r = prompt(rec, xml, kind)
    script = ['```json\n{"works": true, "first_failure": ""}\n```'] if dry else None
    chat = open_chat("dry-run" if dry else judge, "You judge whether physics simulations do what was asked.", "high",
                     tag=f"1h/judge/{rec['world']}/{judge}", script=script, ledger=None if dry else JUDGE_LEDGER)
    if not dry:
        budget.check_judge()
    reply = chat.send([text(p)])
    try:
        v = json.loads(extract_block(reply.text, "json") or "null")
        works = bool(v["works"])
        why = str(v.get("first_failure", ""))
    except (json.JSONDecodeError, TypeError, KeyError):
        works, why = None, None
    truth = hidden.judge(rec["test"], r)
    res = {"world": rec["world"], "judge": judge, "words": kind, "author": rec["model"], "arm": rec["arm"], "brief": rec["brief"],
           "works": works, "first_failure": why, "test_passed": truth["passed"], "test_passed_strict": rec["passes_final"],
           "author_claims_works": bool(rec.get("claims_works")), "test_checks": truth["checks"],
           "test_evidence": truth["evidence"],
           "tokens": {"input": reply.input_tokens, "output": reply.output_tokens}, "cost_usd": reply.cost_usd,
           "prompt_chars": len(p), "reply": reply.text}
    (out_dir / f"{rec['world']}__{judge}.json").write_text(json.dumps(res, indent=2) + "\n")
    return res


def retest() -> int:
    """Re-score every saved verdict against hidden.py as it is now, without asking the judge again."""
    runs = {json.loads(Path(f).read_text())["world"]: Path(f).parent for f in glob.glob(str(RUNS_DIR / "*/*/world.json"))}
    changed = 0
    for f in sorted(glob.glob(str(JUDGE_DIR / "**" / "*__*.json"), recursive=True)):
        res = json.loads(Path(f).read_text())
        rec = json.loads((runs[res["world"]] / "world.json").read_text())
        truth = hidden.judge(rec["test"], run_world(final_xml(rec, runs[res["world"]]), seconds=SIM_SECONDS))
        changed += truth["passed"] != res["test_passed"]
        res |= {"test_passed": truth["passed"], "test_checks": truth["checks"], "test_evidence": truth["evidence"]}
        Path(f).write_text(json.dumps(res, indent=2) + "\n")
    print(f"{changed} verdicts' truth changed")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--judge", default="gpt-6.1", choices=list(MODELS))
    ap.add_argument("--words", default="plain", choices=("plain", "openings"))
    ap.add_argument("--limit", type=int, default=None, help="judge only the first N worlds (for a cost check)")
    ap.add_argument("--retest", action="store_true")
    args = ap.parse_args(argv)
    if args.retest:
        return retest()
    out_dir = ((DRYRUN_DIR / "judge") if args.dry else JUDGE_DIR) / ("openings" if args.words == "openings" else "")
    out_dir.mkdir(parents=True, exist_ok=True)
    todo = []
    for f in sorted(glob.glob(str(RUNS_DIR / "*" / "*" / "world.json"))):
        rec = json.loads(Path(f).read_text())
        if rec.get("final_test") and not (out_dir / f"{rec['world']}__{args.judge}.json").exists():
            todo.append((rec, Path(f).parent))
    todo = todo[: args.limit] if args.limit else todo
    print(f"{len(todo)} worlds to judge")
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        done = list(pool.map(lambda t: judge_one(*t, args.judge, out_dir, args.dry, args.words), todo))
    print(f"{len(done)} judged, ${sum(d['cost_usd'] for d in done):.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
