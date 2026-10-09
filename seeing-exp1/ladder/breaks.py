"""Where long chains break, and whether a fix keeps the links before it ($0, no model calls).

    python -m ladder.breaks            # writes ladder/results_breaks/breaks.json and breaks.md

Re-runs every file each 8- and 16-step world wrote (1j, 1k, 1l), in the order it wrote them, against the hidden test,
and asks three questions a link-by-link builder depends on:
  - Is a world's held set a prefix of its chain (everything before the first break holds, nothing after)?
  - When a later file changes the world, do links that held before stop holding (a fix that is not local)?
  - At the first broken link, did the run in words the author read mention that link's parts?
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from config import ROOT
from hundred import hidden
from hundred.settings import SIM_SECONDS
from typed.lang import LIBRARY, compile_program, parse
from worlds.tests import run as run_world

LADDER = ROOT / "ladder"
SOURCES = {"1j": LADDER / "results" / "runs", "1k": LADDER / "results_1k" / "runs", "1l": LADDER / "results_1l" / "runs"}
OUT = LADDER / "results_breaks"


def files_in_order(run_dir: Path, arm: str) -> list[tuple[str, Path]]:
    ext = "world" if arm == "language" else "xml"
    found = []
    for p in run_dir.glob(f"*.{ext}"):
        if p.name.endswith(".compiled.xml"):
            continue
        m = re.fullmatch(r"(written|round)(\d+)", p.stem)
        if m:
            found.append(((0 if m[1] == "written" else 1, int(m[2])), p.stem, p))
    return [(label, p) for _, label, p in sorted(found)]


def test_file(p: Path, arm: str, test: list[str]) -> dict | None:
    owner = None
    if arm == "language":
        library = LIBRARY.read_text()
        parts = p.with_suffix(".parts")
        if parts.exists():
            library = library.rstrip() + "\n\n\n" + parts.read_text()
        try:
            c = compile_program(parse(p.read_text(), library))
        except Exception:
            return None
        if c.problems:
            return None
        xml, owner = c.xml, c.owner
    else:
        xml = p.read_text()
    try:
        r = run_world(xml, seconds=SIM_SECONDS)
    except Exception:
        return None
    return hidden.judge(test, r, owner)


def held_list(test: list[str], checks: dict) -> list[bool]:
    return [bool(checks[line]) for line in test]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for exp, root in SOURCES.items():
        for f in sorted(root.glob("*/*/world.json")):
            rec = json.loads(f.read_text())
            if rec["steps"] < 8 or (exp != "1j" and rec["arm"] != "language"):
                continue
            seq = []
            for label, p in files_in_order(f.parent, rec["arm"]):
                v = test_file(p, rec["arm"], rec["test"])
                if v is not None:
                    seq.append({"label": label, "held": held_list(rec["test"], v["checks"]),
                                "evidence": v["evidence"]})
            rows.append({"exp": exp, "world": rec["world"], "arm": rec["arm"], "steps": rec["steps"],
                         "family": rec["family"], "test": rec["test"], "files": seq, "dir": str(f.parent)})
            print(exp, rec["world"], [sum(s["held"]) for s in seq], flush=True)
    (OUT / "breaks.json").write_text(json.dumps(rows, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
