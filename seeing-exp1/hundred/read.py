"""Foresight and shared understanding: both models read a world's final file, before any run is shown, and say which
of its brief's hidden-test statements will hold.

    python -m hundred.read                      # every finished world not yet read, by both readers
    python -m hundred.read --dry                # plumbing test, no calls

Scored against the hidden test's own verdicts on that file. Two readers on one file give agreement with each other
(shared understanding) and with the run (foresight). Reads go to hundred/results/reads/<world>__<reader>.json.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from loop.models import extract_block, open_chat, text
from typed.lang import LIBRARY
from hundred import budget
from hundred.settings import DRYRUN_DIR, MODELS, PROMPTS, READS_DIR, RUNS_DIR, SIM_SECONDS, SPEND_LEDGER

ABOUT = {"world": "It is in the world language; its parts library is below.\n\n<library>\n{library}\n</library>\n\n",
         "xml": ""}


def final_file(rec: dict, run_dir: Path) -> tuple[str, str] | None:
    label = rec.get("final_label")
    if not label or rec.get("final_problem") or not rec.get("final_test"):
        return None
    for fmt, suffix in (("world", ".world"), ("xml", ".xml")):
        p = run_dir / f"{label}{suffix}"
        if p.exists():
            parts = run_dir / f"{label}.parts"
            return fmt, p.read_text() + (f"\n```\n\n```parts\n{parts.read_text()}" if parts.exists() else "")
    return None


def read_one(rec: dict, run_dir: Path, reader: str, out_dir: Path, dry: bool, full: bool = False) -> dict | None:
    got = final_file(rec, run_dir)
    if got is None:
        return None
    fmt, src = got
    lines = rec["test"]
    about = ABOUT[fmt].replace("{library}", LIBRARY.read_text().strip())
    p = ((PROMPTS / "read.md").read_text().replace("{brief}", rec["brief_text"]).replace("{fmt}", fmt)
         .replace("{world}", src.rstrip()).replace("{about}", about).replace("{seconds}", f"{SIM_SECONDS:g}")
         .replace("{statements}", "\n".join(f"{i + 1}. {s}" for i, s in enumerate(lines))))
    script = ["```json\n" + json.dumps([True] * len(lines)) + "\n```"] if dry else None
    chat = open_chat("dry-run" if dry else reader, "You predict what physics simulations will do.", "high",
                     tag=f"1h/read/{rec['world']}/{reader}", script=script, ledger=None if dry else SPEND_LEDGER)
    if not dry:
        budget.check(pilot=not full)
    r = chat.send([text(p)])
    try:
        said = [bool(x) for x in json.loads(extract_block(r.text, "json") or "null")]
    except (json.JSONDecodeError, TypeError):
        said = None
    truth = [rec["final_test"]["checks"][s] for s in lines]
    res = {"world": rec["world"], "reader": reader, "author": rec["model"], "arm": rec["arm"], "format": fmt,
           "brief": rec["brief"], "statements": lines, "said": said, "truth": truth,
           "correct": None if said is None or len(said) != len(truth) else sum(a == b for a, b in zip(said, truth)),
           "tokens": {"input": r.input_tokens, "output": r.output_tokens}, "cost_usd": r.cost_usd, "reply": r.text}
    (out_dir / f"{rec['world']}__{reader}.json").write_text(json.dumps(res, indent=2) + "\n")
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--readers", nargs="+", default=list(MODELS), choices=list(MODELS))
    ap.add_argument("--full", action="store_true", help="past the pilot: 1h's own ceiling, not the pilot's")
    args = ap.parse_args(argv)
    runs = (DRYRUN_DIR / "runs") if args.dry else RUNS_DIR
    out_dir = (DRYRUN_DIR / "reads") if args.dry else READS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    todo = []
    for f in sorted(glob.glob(str(runs / "*" / "*" / "world.json"))):
        rec = json.loads(Path(f).read_text())
        if rec.get("dry_run") != args.dry:
            continue
        for reader in args.readers:
            if not (out_dir / f"{rec['world']}__{reader}.json").exists():
                todo.append((rec, Path(f).parent, reader))
    print(f"{len(todo)} reads to do")
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        done = list(pool.map(lambda t: read_one(*t, out_dir, args.dry, args.full), todo))
    print(f"{sum(d is not None for d in done)} read; {sum(d is None for d in done)} had no built final file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
