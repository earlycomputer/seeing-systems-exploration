"""Check experiment 1d's tests both ways, before any model run. No model calls.

    python -m harder.selftest

- every hand-written world (1c's five, 1d's two) passes its own test;
- every broken world fails its own test, on the check its break is meant to trip;
- failing variants of the two new worlds fail;
- the picture's residue runs for the whole swing of a door and a pendulum (1c's blind spot).
Exits non-zero on any failure.
"""

from __future__ import annotations

import sys

from harder import breaks, tests
from harder.settings import BREAKS, BRIEFS, FIXTURES_1C, FIXTURES_DIR
from worlds import draw

# The check each break must trip (its other checks may also fail; this one must).
BREAK_TRIPS = {"shot": "drops through the hoop", "cup": "ball ends in the cup",
               "door": "door starts within its hinge's range",
               "stack": "stack topples (top block ends two block-heights lower)", "catapult": "ball ends in the bucket"}


def fixture(b: str) -> str:
    return ((FIXTURES_DIR if BRIEFS[b]["kind"] == "new" else FIXTURES_1C) / f"{b}.xml").read_text()


def leaning() -> str:
    """The dominoes with the first starting tipped 20 degrees and released, instead of spun: a fair reading of the brief."""
    return fixture("dominoes").replace('qpos="0.00 0 0.08 1 0 0 0 ', 'qpos="0.02 0 0.08 0.9848 0 0.1736 0 ').replace(
        'qvel="0 0 0 0 4 0 ', 'qvel="0 0 0 0 0 0 ')


def variants():
    """(brief, what it is, edited xml, the check that must fail)."""
    d, p = fixture("dominoes"), fixture("pendulum")
    gap = d.replace('<body name="domino6" pos="0.50', '<body name="domino6" pos="0.80')
    for i in range(7, 11):
        gap = gap.replace(f'<body name="domino{i}" pos="{0.1 * (i - 1):.2f}', f'<body name="domino{i}" pos="{0.1 * (i - 1) + 0.3:.2f}')
    gap = gap.replace(" ".join(f"{0.1 * (i - 1):.2f} 0 0.08 1 0 0 0" for i in range(6, 11)),
                      " ".join(f"{0.1 * (i - 1) + 0.3:.2f} 0 0.08 1 0 0 0" for i in range(6, 11)))
    pushed = d.replace('qvel="0 0 0 0 4 0 0 0 0 0 0 0 ', 'qvel="0 0 0 0 4 0 0 0 0 0 4 0 ')
    second_leaning = d.replace('0.10 0 0.08 1 0 0 0 ', '0.12 0 0.08 0.9848 0 0.1736 0 ')
    return [
        ("dominoes", "a gap after the fifth domino", gap, "every domino ends tilted at least 15 degrees"),
        ("dominoes", "the second domino also set moving", pushed, "only the first domino is set moving"),
        ("dominoes", "the second domino starts leaning 20 degrees", second_leaning,
         "ten dominoes on the floor at the start, the other nine upright"),
        ("pendulum", "released too low", p.replace('qpos="1.1 0.1', 'qpos="0.5 0.1'), "ball ends in the cup"),
        ("pendulum", "the cup 1.4 m away", p.replace('<body name="cup" pos="1.1 0 0">', '<body name="cup" pos="1.5 0 0">'),
         "cup's centre 1 m from where the ball starts (0.9 to 1.1 m)"),
        ("pendulum", "the ball launched instead of struck", p.replace('qpos="1.1 0.1 0 0.05 1 0 0 0"/>',
                                                                        'qpos="1.1 0.1 0 0.05 1 0 0 0" qvel="0 3 0 0 0 0 0"/>'),
         "ball starts at rest on the floor"),
    ]


def main() -> int:
    bad = []

    def check(ok: bool, what: str):
        print(("ok    " if ok else "FAIL  ") + what)
        if not ok:
            bad.append(what)

    for b in BRIEFS:
        j = tests.judge(BRIEFS[b]["test"], fixture(b))
        check(bool(j.get("passed")), f"hand-written {b} passes its test")
    for b in BREAKS:
        j = tests.judge(BRIEFS[b]["test"], breaks.broken(b))
        fails = [k for k, v in (j.get("checks") or {}).items() if not v]
        check(not j.get("passed") and BREAK_TRIPS[b] in fails, f"broken {b} fails, tripping '{BREAK_TRIPS[b]}' ({fails})")
    ramp = '      <geom name="cup_entry_ramp" type="box" pos="-0.35 0 0.006" euler="0 2 0" size="0.2 0.15 0.004"/>\n'
    with_ramp = fixture("pendulum").replace('    </body>\n  </worldbody>', ramp + '    </body>\n  </worldbody>')
    j = tests.judge("pendulum", with_ramp)
    check(abs(j["values"]["cup_distance_m"] - 1.0) < 1e-6,
          f"pendulum, a cup with an entry ramp: centre measured at the cup, {j['values']['cup_distance_m']} m")
    offset = fixture("pendulum").replace('<body name="cup" pos="1.1 0 0">', '<body name="cup" pos="0 0 0">').replace(
        'name="cup_base" type="box" pos="0 0 0.005"', 'name="cup_base" type="box" pos="1.1 0 0.005"').replace(
        'name="cup_lip" type="box" pos="-0.15', 'name="cup_lip" type="box" pos="0.95').replace(
        'name="cup_far" type="box" pos="0.15', 'name="cup_far" type="box" pos="1.25').replace(
        'name="cup_left" type="box" pos="0 0.15', 'name="cup_left" type="box" pos="1.1 0.15').replace(
        'name="cup_right" type="box" pos="0 -0.15', 'name="cup_right" type="box" pos="1.1 -0.15')
    j = tests.judge("pendulum", offset)
    check(bool(j.get("passed")) and abs(j["values"]["cup_distance_m"] - 1.0) < 1e-6,
          f"pendulum, the cup's body at the world origin with its geoms offset: passes, {j['values']['cup_distance_m']} m")
    j = tests.judge("dominoes", leaning())
    check(bool(j.get("passed")), f"dominoes, the first starting tipped 20 degrees and released: passes ({[k for k, v in j['checks'].items() if not v]})")
    for b, what, xml, must in variants():
        j = tests.judge(b, xml)
        fails = [k for k, v in (j.get("checks") or {}).items() if not v]
        check(not j.get("passed") and must in fails, f"{b}, {what}: fails '{must}' ({fails})")
    for b, joint, shut in (("door", "hinge", True), ("pendulum", "pivot", False)):
        r = tests.run(fixture(b))
        m = r.model
        q = r.qvel[:, m.jnt_dofadr[m.joint(joint).id]]
        still = [i for i in range(len(r.times)) if abs(q[i]) > 0.05]
        last_turn = float(r.times[still[-1]]) if still else 0.0
        until = draw.active_until(r, draw.moving_bodies(r))
        check(until >= min(last_turn, float(r.times[-1])) - 0.05,
              f"{b}: residue runs to {until:.2f} s, past its last turn at {last_turn:.2f} s")
    print(f"{len(bad)} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
