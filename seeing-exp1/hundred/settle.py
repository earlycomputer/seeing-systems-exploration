"""The settle check: what is already touching or overlapping when a run starts, said in words before the run's history.

    found = settle.problems(xml)       # [] when the start is clean
    text = settle.say(found)           # "" when clean, else a short section that goes before the run's history

In 1h, 3 worlds failed because two things in the chain were touching from the start, so their touch never "happened",
and 2 started in their end state. The run in words did say "starts touching" at 0.00 s, among dozens of lines, and no
model acted on it. This puts it first, as a problem. Only two moving things touching, or any two things overlapping
by more than OVERLAP, are reported: a ball resting on its ramp is a normal start.

The `blind` arm never sees it; it is run information.
"""

from __future__ import annotations

import mujoco

from worlds.tests import load

OVERLAP = 0.002  # m: deeper than this at the start is an overlap, and the solver pushes the two apart at once
TOUCH = 0.001  # m: closer than this counts as touching


def problems(xml: str) -> list[str]:
    s = load(xml)
    m, d = s.model, s.data
    mujoco.mj_forward(m, d)

    def name(g: int) -> str:
        b = int(m.geom_bodyid[g])
        return m.body(b).name or m.geom(g).name or f"geom{g}"

    def moves(g: int) -> bool:
        return int(m.body_weldid[m.geom_bodyid[g]]) != 0

    seen, out = set(), []
    for c in d.contact[: d.ncon]:
        g1, g2 = int(c.geom1), int(c.geom2)
        if m.geom_bodyid[g1] == m.geom_bodyid[g2] or not (moves(g1) or moves(g2)):
            continue
        a, b = sorted((name(g1), name(g2)))
        if (a, b) in seen:
            continue
        if c.dist < -OVERLAP:
            seen.add((a, b))
            out.append(f"{a} and {b} overlap by {-c.dist * 1000:.0f} mm at the start, so the solver shoves them apart "
                       "in the first steps")
        elif c.dist < TOUCH and moves(g1) and moves(g2):
            seen.add((a, b))
            out.append(f"{a} already touches {b} at the start, so their touch is not something that happens in the run")
    return out


def say(p: list[str] | None) -> str:
    if not p:
        return ""
    return "Before the run, at the start:\n" + "\n".join(f"- {x}" for x in p) + "\n\n"
