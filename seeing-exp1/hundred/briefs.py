"""Write 1h's briefs and hidden tests once, with a model that writes no worlds. Committed before any world is run.

    python -m hundred.briefs            # one call to the brief writer; writes hundred/briefs.json
    python -m hundred.briefs --check    # validate briefs.json (forms, names, counts); no calls

The writer is asked for N_BRIEFS + 4 and the first N_BRIEFS that pass validation are kept, so nobody picks among
them. Validation is mechanical: test lines in the expectation forms, names given, 5 to 15 things, 3 to 6 lines.
"""

from __future__ import annotations

import argparse
import json
import sys

from loop.models import extract_block, open_chat, text
from hundred import hidden
from hundred.settings import BRIEF_WRITER, BRIEFS_FILE, N_BRIEFS, PROMPTS, RESULTS_DIR, SIM_SECONDS, SPEND_LEDGER

KIND_XML = {"loose": "a body with a `<freejoint/>`", "hinged": "a body on a hinge joint",
            "sliding": "a body on a slide joint", "fixed": "fixed in place; all its geoms belong to one body"}
KIND_LANGUAGE = {"loose": "moves freely", "hinged": "turns on a hinge", "sliding": "slides", "fixed": "fixed"}


def problems(b: dict) -> list[str]:
    out = []
    names = {t["name"] for t in b.get("things", [])}
    if not 5 <= len(names) <= 15:
        out.append(f"{len(names)} things")
    if not 3 <= len(b.get("test", [])) <= 6:
        out.append(f"{len(b.get('test', []))} test lines")
    for line in b.get("test", []):
        if not hidden.forms_ok(line):
            out.append(f"not a form: {line}")
        elif not hidden.names_in(line) <= names:
            out.append(f"unknown name in: {line}")
        elif "floor" in hidden.names_in(line):
            out.append(f"touches the floor: {line}")
    if any(t.get("kind") not in KIND_XML for t in b.get("things", [])):
        out.append("unknown kind")
    return out


def names_xml(b: dict) -> str:
    """The naming sentence for the XML arms, as 1f's `names` were."""
    parts = [f"`{t['name']}` ({t['what']}: {KIND_XML[t['kind']]})" for t in b["things"]]
    return ("Name each thing's body exactly: " + "; ".join(parts) + ". Its geoms may be named with the body's name as a "
            "prefix (`" + b["things"][0]["name"] + "_...`).")


def names_language(b: dict) -> str:
    parts = [f"`{t['name']}` ({t['what']}, {KIND_LANGUAGE[t['kind']]})" for t in b["things"]]
    return "Name the things exactly: " + "; ".join(parts) + "."


def load(path=BRIEFS_FILE) -> dict:
    return {b["id"]: b for b in json.loads(path.read_text())}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    if args.check:
        bs = json.loads(BRIEFS_FILE.read_text())
        bad = {b["id"]: problems(b) for b in bs if problems(b)}
        print(f"{len(bs)} briefs, {len(bad)} with problems: {bad}")
        return 1 if bad or len(bs) != N_BRIEFS else 0
    if BRIEFS_FILE.exists():
        raise SystemExit(f"{BRIEFS_FILE} exists; briefs are written once")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    n = N_BRIEFS + 4
    p = (PROMPTS / "write_briefs.md").read_text().replace("{n}", str(n)).replace("{seconds}", f"{SIM_SECONDS:g}")
    chat = open_chat(BRIEF_WRITER, "You write clear, testable physics briefs.", "high", tag="1h/briefs", ledger=SPEND_LEDGER)
    r = chat.send([text(p)])
    (RESULTS_DIR / "briefs_reply.md").write_text(r.text)
    (RESULTS_DIR / "briefs_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
    got = json.loads(extract_block(r.text, "json"))
    kept, dropped, seen = [], [], set()
    for b in got:
        why = problems(b) + (["duplicate id"] if b.get("id") in seen else [])
        seen.add(b.get("id"))
        (dropped if why or len(kept) == N_BRIEFS else kept).append(b if not why else dict(b, dropped=why))
    BRIEFS_FILE.write_text(json.dumps(kept, indent=2) + "\n")
    (RESULTS_DIR / "briefs_dropped.json").write_text(json.dumps(dropped, indent=2) + "\n")
    print(f"kept {len(kept)} of {len(got)}; ${r.cost_usd:.4f}")
    return 0 if len(kept) == N_BRIEFS else 1


if __name__ == "__main__":
    sys.exit(main())
