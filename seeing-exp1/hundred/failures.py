"""Where 1h's failures come from, and 1h again under the fixed hidden test. No model calls.

    python -m hundred.failures        # writes hundred/results/failures.md

Each failed world is counted once, by its first failing hidden-test line, under 1h's original (strict) reading and
under the fixed one (hidden.py: either hinge stop, order within ORDER_SLACK). Also: whether "lower stop" could have
meant physically lower (the hinged part's centre of mass lower at that end), and what the settle check (settle.py)
finds in each final file.
"""

from __future__ import annotations

import collections
import glob
import json
import re
from pathlib import Path

import mujoco

from hundred import hidden, settle
from hundred.settings import ARMS, ORDER_SLACK, RESULTS_DIR, RUNS_DIR
from langrun import expect
from langrun.report import fisher
from worlds.tests import run as run_world

CAUSES = [("no thing named", "a name the brief needs is missing"),
          ("never touch", "the chain breaks: two things never touch"),
          ("touching from the start", "touching from the start"),
          ("before the line above", "events happen out of order"),
          ("still moving", "not at rest at the end"),
          ("outside", "comes to rest outside the target"),
          ("starts", "starts in its end state"),
          ("never reaches", "a hinge never reaches the named stop"),
          ("height", "misses the opening")]
TIE = 0.01  # m: centres of mass closer than this at the two ends: neither end is lower


def cause(evidence: str) -> str:
    return next((c for k, c in CAUSES if k in evidence), "other")


def final_xml(w: dict, d: Path) -> str:
    for name in (f"{w['final_label']}.compiled.xml", f"{w['final_label']}.xml"):
        if (d / name).exists():
            return (d / name).read_text()
    raise FileNotFoundError(d)


def stop_heights(name: str, r) -> tuple[float, float] | None:
    """Height of the hinged part's centre of mass at its lower and upper range ends, everything else as at the start."""
    m = r.model
    js = [j for j in range(m.njnt) if m.jnt_type[j] == mujoco.mjtJoint.mjJNT_HINGE and m.jnt_limited[j] and
          (expect.key(m.joint(j).name) == expect.key(name) or m.jnt_bodyid[j] in expect.bodies(r, expect.geoms(r, name)))]
    if not js:
        return None
    j, out = js[0], []
    b = int(m.jnt_bodyid[j])
    for q in m.jnt_range[j]:
        d = mujoco.MjData(m)
        d.qpos[:] = r.qpos[0]
        d.qpos[m.jnt_qposadr[j]] = q
        mujoco.mj_kinematics(m, d)
        mujoco.mj_comPos(m, d)
        out.append(float(d.subtree_com[b][2]))
    return out[0], out[1]


def table(by: collections.Counter) -> list[str]:
    causes = sorted({c for c, _ in by}, key=lambda c: -sum(by[(c, a)] for a in ARMS))
    out = ["| Cause | " + " | ".join(ARMS) + " | All |", "|---|" + "---|" * (len(ARMS) + 1)]
    for c in causes:
        out.append(f"| {c} | " + " | ".join(str(by[(c, a)]) for a in ARMS) + f" | {sum(by[(c, a)] for a in ARMS)} |")
    return out


def main() -> int:
    ws = [(json.loads(Path(f).read_text()), Path(f).parent) for f in sorted(glob.glob(str(RUNS_DIR / "*/*/world.json")))]
    n = collections.Counter(w["arm"] for w, _ in ws)
    by_strict, by_fixed, gaps = collections.Counter(), collections.Counter(), collections.Counter()
    strict, fixed, wrong_strict, wrong_fixed = (collections.Counter() for _ in range(4))
    flagged, flagged_pass, clean_pass = collections.Counter(), collections.Counter(), collections.Counter()
    height = collections.Counter()  # how "lower stop" by joint range compares with lower by height, in working worlds
    for w, d in ws:
        arm = w["arm"]
        t = w.get("final_test")
        if not t:
            by_strict[("never built", arm)] += 1
            by_fixed[("never built", arm)] += 1
            wrong_strict[arm] += bool(w.get("claims_works"))
            wrong_fixed[arm] += bool(w.get("claims_works"))
            continue
        xml = final_xml(w, d)
        r = run_world(xml)
        f = hidden.judge(w["test"], r)
        assert hidden.judge(w["test"], r, strict=True)["passed"] == w["passes_final"], w["world"]
        strict[arm] += w["passes_final"]
        fixed[arm] += f["passed"]
        wrong_strict[arm] += bool(w.get("claims_works")) and not w["passes_final"]
        wrong_fixed[arm] += bool(w.get("claims_works")) and not f["passed"]
        found = settle.problems(xml)
        flagged[arm] += bool(found)
        (flagged_pass if found else clean_pass)[arm] += f["passed"]
        for verdict, by in ((t, by_strict), (f, by_fixed)):
            if not verdict["passed"]:
                first = next(line for line, ok in verdict["checks"].items() if not ok)
                by[(cause(verdict["evidence"][first]), arm)] += 1
        if not w["passes_final"]:
            first = next(line for line, ok in t["checks"].items() if not ok)
            if m := re.search(r"at (\d+\.\d+) s.*\((\d+\.\d+) s\)", t["evidence"][first]):
                gaps[f"within {ORDER_SLACK:g} s" if float(m[2]) - float(m[1]) <= ORDER_SLACK else
                     f"more than {ORDER_SLACK:g} s"] += 1
        if f["passed"]:
            for line in w["test"]:
                if (m := hidden.STOP_FORM.fullmatch(line.strip().rstrip(".").lower())) and (h := stop_heights(m[1], r)):
                    reached = 0 if "lower stop" in f["evidence"][line] else 1
                    dz = h[reached] - h[1 - reached]
                    height["neither end lower" if abs(dz) < TIE else
                           "the end it swings to is lower" if dz < 0 else "the end it swings to is higher"] += 1

    out = ["# Where 1h's failures come from, and 1h under the fixed test", "",
           "Generated by `python -m hundred.failures`; never edited by hand. No model calls.", "",
           "## Under 1h's original test", "",
           "Each failed world counted once, by its first failing hidden-test line.", ""]
    out += table(by_strict)
    out += ["", f"Out-of-order failures by gap: {dict(gaps)}.", "",
            "## Could \"lower stop\" have meant physically lower?", "",
            "In worlds that work under the fixed test, each stop line's hinge: the end it actually swings to, against the "
            "other end, by the height of the hinged part's centre of mass with everything else as at the start "
            f"(closer than {TIE * 100:.0f} cm counts as neither):", ""]
    out += [f"- {k}: {v}" for k, v in sorted(height.items())]
    out += ["", "If some working worlds swing to the higher end, \"lower\" by height would fail working worlds too; the fixed "
            "test takes either end and leaves direction to the lines around it.", "",
            "## Under the fixed test (either hinge stop, order within "
            f"{ORDER_SLACK:g} s)", "",
            "| Arm | Worlds | Worked, original | Worked, fixed | Wrong \"it works\", original | Wrong \"it works\", fixed |",
            "|---|---|---|---|---|---|"]
    out += [f"| {a} | {n[a]} | {strict[a]} | {fixed[a]} | {wrong_strict[a]} | {wrong_fixed[a]} |" for a in ARMS]
    la, bl, xm = "language", "blind", "xml"
    out += ["", f"Fixed test, Fisher exact: language vs blind p = {fisher(fixed[la], n[la], fixed[bl], n[bl]):.3f}; "
            f"language vs xml p = {fisher(fixed[la], n[la], fixed[xm], n[xm]):.3f}; "
            f"xml vs blind p = {fisher(fixed[xm], n[xm], fixed[bl], n[bl]):.3f}.", "",
            "Failures under the fixed test, by first failing line:", ""]
    out += table(by_fixed)
    out += ["", "## What the settle check finds in 1h's final files", "",
            "Final files where two moving things touch, or any two things overlap by more than "
            f"{settle.OVERLAP * 1000:.0f} mm, at the start (settle.py). 1h's authors never saw this check.", "",
            "| Arm | Final files flagged | Worked when flagged | Worked when clean |", "|---|---|---|---|"]
    out += [f"| {a} | {flagged[a]} | {flagged_pass[a]} of {flagged[a]} | {clean_pass[a]} of "
            f"{n[a] - flagged[a] - by_fixed[('never built', a)]} |" for a in ARMS]
    text = "\n".join(out) + "\n"
    (RESULTS_DIR / "failures.md").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
