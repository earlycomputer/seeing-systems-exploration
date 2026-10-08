"""A brief's hidden test: expectation lines that must all hold, each for something that happens during the run, in order.

    verdict = judge(lines, run, owner)   # {"passed", "checks": {line: bool}, "evidence": {line: str}}

The forms are langrun/expect.py's. Stricter than an author's own expectations, so a world cannot pass by starting in
its end state: a touch must begin after the start, a thing that comes to rest in another must start outside it, and
each line's moment (first touch, first stop, falling through, the end for rest) must come no earlier than the line
before it, give or take ORDER_SLACK.

Fixed after 1h (2026-10-08, Jono: "Go for it!" on the fixes in hundred/results/failures.md):

- A hinge stop is either end of its range. 1h's briefs said "lower stop" in the everyday sense, while the test read it
  as the joint's lower limit, the most negative angle: 9 of 12 hinge failures reached the other end instead. Reading
  "lower" as physically lower was tried and fails too: in working worlds the stop that releases the ball is often
  the higher one by height (hundred/results/failures.md). Which way it swings is carried by the lines around it (what
  it releases, what drops through), so `<thing> swings to a stop` is the form, and the old lower and upper lines are
  read the same way.
- Lines in order within ORDER_SLACK count as in order. 6 of 16 order failures in 1h were closer than 0.1 s, below what
  a brief's "then" can mean when contacts chatter at 500 Hz.

`strict=True` gives 1h's original reading, for reproducing its results.
"""

from __future__ import annotations

import re

from langrun import expect
from hundred.settings import ORDER_SLACK
from worlds.tests import Run, aabb

STOP_FORM = re.compile(r"(.+?) (?:reaches its (?:lower|upper) stop|swings to a stop)")


def _touch_start(run: Run, a: str, b: str, owner) -> tuple[float | None, str]:
    A, B = set(expect.geoms(run, a, owner)), set(expect.geoms(run, b, owner))
    if not A or not B:
        return None, f"there is no thing named {a if not A else b}"
    on = [any((x in A and y in B) or (x in B and y in A) for x, y in pairs) for pairs in run.contacts]
    if not any(on):
        return None, "they never touch"
    for i in range(1, len(on)):
        if on[i] and not on[i - 1]:
            return float(run.times[i]), f"first touch after the start at {run.times[i]:.2f} s"
    return None, "touching from the start and never apart, so it is not something that happens"


def _inside(run: Run, x: int, b: list[int], i: int) -> bool:
    p = run.xpos[i, x]
    lo, hi = aabb(run, b, i)
    return bool(lo[0] <= p[0] <= hi[0] and lo[1] <= p[1] <= hi[1] and p[2] < hi[2])


def _either_stop(name: str, run: Run, owner, after: float) -> tuple[bool, float | None, str]:
    got = []
    for end in ("lower", "upper"):
        ok, why = expect.one(f"{name} reaches its {end} stop", run, owner)
        found = re.search(r"at (\d+\.\d+) s", why)
        got.append((ok, float(found[1]) if ok and found else None, why))
    hits = [g for g in got if g[0]]
    if hits:  # the first stop reached in order with the line above, if either is
        timed = [g for g in hits if g[1] is not None]
        in_order = [g for g in timed if g[1] >= after]
        return min(in_order or timed, key=lambda g: g[1]) if timed else hits[0]
    return False, None, f"{got[0][2]}; and {got[1][2]}"


def one(line: str, run: Run, owner, strict: bool = False, after: float = 0.0) -> tuple[bool, float | None, str]:
    low = line.strip().rstrip(".").lower()
    if not strict and (m := STOP_FORM.fullmatch(low)):
        return _either_stop(m[1], run, owner, after)
    if m := re.fullmatch(r"(.+?) touches (.+)", low):
        t, why = _touch_start(run, m[1], m[2], owner)
        return t is not None, t, why
    ok, why = expect.one(line, run, owner)
    if not ok:
        return False, None, why
    if m := re.fullmatch(r"(.+?) comes to rest in (.+)", low):
        a, b = expect.geoms(run, m[1], owner), expect.geoms(run, m[2], owner)
        x = [y for y in expect.bodies(run, a) if expect.free_joint_or_none(run, y) is not None][0]
        if _inside(run, x, b, 0):
            return False, None, f"{m[1]} starts inside {m[2]}, so coming to rest there is not something that happens"
        return True, float(run.times[-1]), why
    found = re.search(r"at (\d+\.\d+) s", why)
    return True, float(found[1]) if found else None, why


def judge(lines: list[str], run: Run, owner: dict | None = None, strict: bool = False) -> dict:
    checks, evidence, last = {}, {}, 0.0
    slack = 1e-9 if strict else ORDER_SLACK
    for line in lines:
        ok, t, why = one(line, run, owner, strict, last - slack)
        if ok and t is not None and t + slack < last:
            ok, why = False, f"{why}, which is before the line above it ({last:.2f} s)"
        if ok and t is not None:
            last = max(last, t)
        checks[line], evidence[line] = ok, why
    if run.diverged:
        checks["the simulation stays finite"], evidence["the simulation stays finite"] = False, run.diverged
    return {"passed": all(checks.values()), "checks": checks, "evidence": evidence}


def forms_ok(line: str) -> bool:
    low = line.strip().rstrip(".").lower()
    return bool(re.fullmatch(r"(.+?) (touches|comes to rest in|drops through) (.+)", low) or
                STOP_FORM.fullmatch(low))


def names_in(line: str) -> set[str]:
    low = line.strip().rstrip(".").lower()
    if m := re.fullmatch(r"(.+?) (?:touches|comes to rest in|drops through) (.+)", low):
        return {m[1], m[2]}
    if m := STOP_FORM.fullmatch(low):
        return {m[1]}
    return set()

