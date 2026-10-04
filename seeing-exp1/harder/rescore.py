"""Re-judge every saved world file with the current tests, from the files each world saved. No model calls.

    python -m harder.rescore                      # every world in harder/results/runs
    python -m harder.rescore --runs .dryrun/harder/runs

The tests never reach the models and never steer the loop, so re-judging the saved files gives exactly the
verdicts the current tests would have given live. Each world.json keeps what it said before under
`superseded`, with the reason. Added 2026-10-04: the dominoes test required the first domino to start upright,
but "the first is tipped over" fairly allows it to start leaning; three first-run worlds were failed for it.
Then, after the full run: the pendulum test took the cup's centre from the box around all its geoms, so a cup
with an entry ramp (which the naming convention puts in the cup body) measured short of where the cup is.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from harder import tests
from harder.settings import RUNS_DIR

REASONS = ["the dominoes test lets the first domino start tipped; only the other nine must start upright (2026-10-04)",
           "the pendulum test takes the cup's centre from its body's origin when that lies within the cup, so an entry "
           "ramp no longer moves it (2026-10-04)"]
REASON = REASONS[-1]
KEYS = ("passes_first", "passes_final", "passed_at_round", "claim_correct", "final_checks")


def rescore(run_dir: Path) -> bool:
    path = run_dir / "world.json"
    w = json.loads(path.read_text())
    before = {k: w.get(k) for k in KEYS}
    files_before = [{k: f.get(k) for k in ("label", "passed", "checks")} for f in w["files"]]
    current, passed_at = None, None
    for f in w["files"]:
        xml = run_dir / f"{f['label']}.xml"
        if not f.get("loaded") or not xml.exists():
            continue
        j = tests.public(tests.judge(w["test"], xml.read_text()))
        f.update({k: j.get(k) for k in ("passed", "checks", "values", "problem", "diverged")})
        current = f
        if f.get("passed") and passed_at is None and not f["label"].startswith(("written", "given")):
            passed_at = int(f["label"].removeprefix("round"))
    if current is not None:
        loaded = [f for f in w["files"] if f.get("loaded")]
        first = loaded[0] if loaded else None
        w["passes_first"] = bool(first and first.get("passed") and first["label"].startswith(("written", "given")))
        if w["passes_first"]:
            passed_at = 0
        w["passes_final"] = bool(current.get("passed"))
        w["passed_at_round"] = passed_at
        w["claim_correct"] = None if w.get("claims_works") is None else w["claims_works"] == w["passes_final"]
        w["final_checks"] = current.get("checks")
    after = {k: w.get(k) for k in KEYS}
    changed = after != before or files_before != [{k: f.get(k) for k in ("label", "passed", "checks")} for f in w["files"]]
    if changed:
        w.setdefault("superseded", []).append({"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                              "reason": REASON, "before": before, "files_before": files_before})
        path.write_text(json.dumps(w, indent=2, default=str) + "\n")
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=RUNS_DIR)
    args = ap.parse_args()
    dirs = sorted(p.parent for p in args.runs.glob("*/*/world.json"))
    changed = [d for d in dirs if rescore(d)]
    for d in changed:
        print("changed:", d.parent.name)
    print(f"{len(dirs)} worlds re-judged; {len(changed)} changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
