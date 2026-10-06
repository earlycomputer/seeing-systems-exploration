"""The language's two after-parse checks, run on raw MJCF so the xml arm gets the same help in the same words.

The world language refuses a file whose hinge starts outside its own range (the 1d door) and one whose parts start
inside each other (typed/compiler.py, check_meaning and check_overlaps). Those checks read the language's own
structures; these read the compiled MuJoCo model instead, and report with the same Problem and wording.
"""

from __future__ import annotations

import math

import mujoco

from typed.compiler import OVERLAP, Problem, render
from worlds.tests import load

J = mujoco.mjtJoint


def problems(xml: str) -> list[Problem]:
    s = load(xml)  # resets to the keyframe named start, as the run does
    m, d = s.model, s.data
    out = []
    for j in range(m.njnt):
        if not m.jnt_limited[j] or int(m.jnt_type[j]) not in (int(J.mjJNT_HINGE), int(J.mjJNT_SLIDE)):
            continue
        hinge = int(m.jnt_type[j]) == int(J.mjJNT_HINGE)
        q, (lo, hi) = float(d.qpos[m.jnt_qposadr[j]]), m.jnt_range[j]
        if lo - 1e-9 <= q <= hi + 1e-9:
            continue
        f = (lambda x: f"{math.degrees(x):.4g}°") if hinge else (lambda x: f"{x:g} m")
        name = m.joint(j).name or m.body(m.jnt_bodyid[j]).name
        out.append(Problem(
            "STARTS OUTSIDE ITS OWN RANGE", f"joint {name}", f"starts at {f(q)}, range {f(lo)} to {f(hi)} as MuJoCo applies it",
            f"a starting {'angle' if hinge else 'position'} between {f(lo)} and {f(hi)}",
            "MuJoCo would push it back inside its limit in the first few steps: whatever it was meant to do from there, "
            "it would not." + (" MuJoCo reads joint ranges in degrees unless <compiler angle=\"radian\"/> is set, but "
                               "keyframe angles always in radians." if hinge else ""),
            "widen the range or change where it starts"))
    seen = set()
    for con in d.contact[: d.ncon]:
        if con.dist >= -OVERLAP:
            continue
        pair = tuple(sorted(m.geom(g).name or f"geom{g}" for g in (con.geom1, con.geom2)))
        if pair in seen:
            continue
        seen.add(pair)
        out.append(Problem(
            "PARTS START INSIDE EACH OTHER", f"{pair[0]} / {pair[1]}", f"{-con.dist * 1000:.0f} mm of overlap at t = 0",
            "parts that at most touch when the world starts",
            "MuJoCo pushes overlapping parts apart in the first steps, so the world starts with a kick nobody wrote.",
            "move one of them, or check the sizes"))
    return out


def report(xml: str) -> str | None:
    ps = problems(xml)
    return render(ps).replace("in this world. Nothing was built.", "in this file. Nothing was run.") if ps else None
