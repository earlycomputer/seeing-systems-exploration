"""Write 1j's briefs and hidden tests once, with a model that writes no worlds. Committed before any world is run.

    python -m ladder.briefs            # one call to the brief writer; writes ladder/briefs.json
    python -m ladder.briefs --check    # validate briefs.json; no calls

The writer is asked for N_FAMILIES + 2 families and the first N_FAMILIES that pass validation are kept, so nobody
picks among them. Validation is mechanical: one test line per step in the forms, names given, and each shorter
version's test the first lines of the 16-step test (a closing "comes to rest in" aside).
"""

from __future__ import annotations

import argparse
import json
import sys

from hundred import hidden
from ladder import budget
from ladder.settings import BRIEF_WRITER, BRIEFS_FILE, LEVELS, N_FAMILIES, PROMPTS, RESULTS_DIR, SECONDS, SPEND_LEDGER
from loop.models import extract_block, open_chat, text

KINDS = ("loose", "hinged", "sliding", "fixed")


def problems(f: dict) -> list[str]:
    out = []
    vs = f.get("versions", {})
    if sorted(vs, key=int) != [str(n) for n in LEVELS]:
        return [f"versions {sorted(vs)}"]
    full = vs[str(LEVELS[-1])]["test"]
    for n in LEVELS:
        v = vs[str(n)]
        names = {t["name"] for t in v.get("things", [])}
        if len(v.get("test", [])) != n:
            out.append(f"{n} steps but {len(v.get('test', []))} test lines")
        for line in v.get("test", []):
            if not hidden.forms_ok(line):
                out.append(f"{n}: not a form: {line}")
            elif not hidden.names_in(line) <= names:
                out.append(f"{n}: unknown name in: {line}")
            elif "floor" in hidden.names_in(line):
                out.append(f"{n}: touches the floor: {line}")
        if any(t.get("kind") not in KINDS for t in v.get("things", [])):
            out.append(f"{n}: unknown kind")
        if any(a != b and b.startswith(a + "_") for a in names for b in names):
            out.append(f"{n}: a name starts with another's")
        head = v.get("test", [])[:-1] if v.get("test") and " comes to rest in " in v["test"][-1] else v.get("test", [])
        if head != full[: len(head)]:
            out.append(f"{n}: test is not the start of the 16-step test")
        if any(" comes to rest in " in line for line in v.get("test", [])[:-1]):
            out.append(f"{n}: comes to rest before the last line")
    return out


def load(path=BRIEFS_FILE) -> dict:
    """{"<family>-<n>": brief}, each brief with id, family, steps, seconds, brief, things, test."""
    out = {}
    for f in json.loads(path.read_text()):
        for n in LEVELS:
            v = f["versions"][str(n)]
            bid = f"{f['family']}{n}"
            out[bid] = {"id": bid, "family": f["family"], "steps": n, "seconds": SECONDS[n], **v}
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    if args.check:
        fs = json.loads(BRIEFS_FILE.read_text())
        bad = {f["family"]: problems(f) for f in fs if problems(f)}
        print(f"{len(fs)} families, {len(bad)} with problems: {bad}")
        return 1 if bad or len(fs) != N_FAMILIES else 0
    if BRIEFS_FILE.exists():
        raise SystemExit(f"{BRIEFS_FILE} exists; briefs are written once")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    n = N_FAMILIES + 2
    p = (PROMPTS / "write_briefs.md").read_text().replace("{n}", str(n))
    for k, s in SECONDS.items():
        p = p.replace(f"{{seconds_{k}}}", f"{s:g}")
    budget.check()
    chat = open_chat(BRIEF_WRITER, "You write clear, testable physics briefs.", "high", tag="1j/briefs", ledger=SPEND_LEDGER)
    r = chat.send([text(p)])
    (RESULTS_DIR / "briefs_reply.md").write_text(r.text)
    (RESULTS_DIR / "briefs_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
    got = json.loads(extract_block(r.text, "json"))
    kept, dropped, seen = [], [], set()
    for f in got:
        why = problems(f) + (["duplicate family"] if f.get("family") in seen else [])
        seen.add(f.get("family"))
        (dropped if why or len(kept) == N_FAMILIES else kept).append(f if not why else dict(f, dropped=why))
    BRIEFS_FILE.write_text(json.dumps(kept, indent=2) + "\n")
    (RESULTS_DIR / "briefs_dropped.json").write_text(json.dumps(dropped, indent=2) + "\n")
    print(f"kept {len(kept)} of {len(got)}; ${r.cost_usd:.4f}")
    return 0 if len(kept) == N_FAMILIES else 1


if __name__ == "__main__":
    sys.exit(main())
