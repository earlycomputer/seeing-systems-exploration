"""Re-judge saved corrections with the current checks, from the files each run saved. No model calls.

    python -m outcome.rescore                     # every run in outcome/results/runs
    python -m outcome.rescore --runs .dryrun/outcome/runs

Each run.json keeps what it said before under `superseded`, with the reason, so a changed verdict shows
its origin. Added 2026-10-04: the first batch's check counted an XML comment placed just after the
keyframe element as a change to the scene, which marked made corrections invalid.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from outcome.run import judge_correction
from outcome.settings import RUNS_DIR

REASON = "XML comments outside the keyframe no longer count as changes to the scene (2026-10-04)"


def rescore(run_dir: Path) -> tuple[dict, dict] | None:
    path = run_dir / "run.json"
    run = json.loads(path.read_text())
    miss_xml = (run_dir / "scene_miss.xml").read_text()
    files = {n: run_dir / f"scene_corrected_{n}.xml" for n in (1, 2)}
    read = lambda n: files[n].read_text() if files[n].exists() else None  # noqa: E731
    before = {k: run.get(k) for k in ("made_after_one", "made_after_two")}
    turns = {t["turn"]: t for t in run["turns"]}
    c1, _ = judge_correction(miss_xml, read(1))
    turns[2]["correction"] = c1
    run["made_after_one"] = bool(c1.get("made_valid"))
    if 3 in turns:
        if read(2) is not None:
            c2, _ = judge_correction(miss_xml, read(2))
            turns[3]["correction"] = c2
            run["made_after_two"] = bool(c2.get("made_valid"))
        else:
            run["made_after_two"] = run["made_after_one"]
    after = {k: run.get(k) for k in before}
    if after != before:
        run.setdefault("superseded", []).append({"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                                 "reason": REASON, "was": before})
        path.write_text(json.dumps(run, indent=2) + "\n")
        return before, after
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=RUNS_DIR)
    args = ap.parse_args()
    paths = sorted(args.runs.glob("*/*/run.json"))
    changed = 0
    for p in paths:
        r = rescore(p.parent)
        if r:
            changed += 1
            print(f"{p.parent.parent.name}: {r[0]} -> {r[1]}")
    print(f"{len(paths)} runs re-judged; {changed} changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
