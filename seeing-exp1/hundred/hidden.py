"""A brief's hidden test: expectation lines that must all hold, each for something that happens during the run, in order.

    verdict = judge(lines, run, owner)   # {"passed", "checks": {line: bool}, "evidence": {line: str}}

The forms are langrun/expect.py's. Stricter than an author's own expectations, so a world cannot pass by starting in
its end state: a touch must begin after the start, a thing that comes to rest in another must start outside it, and
each line's moment (first touch, first stop, falling through, the end for rest) must come no earlier than the line
before it.
"""

from __future__ import annotations

import re

from langrun import expect
from worlds.tests import Run, aabb


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


def one(line: str, run: Run, owner) -> tuple[bool, float | None, str]:
    low = line.strip().rstrip(".").lower()
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


def judge(lines: list[str], run: Run, owner: dict | None = None) -> dict:
    checks, evidence, last = {}, {}, 0.0
    for line in lines:
        ok, t, why = one(line, run, owner)
        if ok and t is not None and t + 1e-9 < last:
            ok, why = False, f"{why}, which is before the line above it ({last:.2f} s)"
        if ok and t is not None:
            last = t
        checks[line], evidence[line] = ok, why
    if run.diverged:
        checks["the simulation stays finite"], evidence["the simulation stays finite"] = False, run.diverged
    return {"passed": all(checks.values()), "checks": checks, "evidence": evidence}


def forms_ok(line: str) -> bool:
    low = line.strip().rstrip(".").lower()
    return bool(re.fullmatch(r"(.+?) (touches|comes to rest in|drops through) (.+)", low) or
                re.fullmatch(r"(.+?) reaches its (lower|upper) stop", low))


def names_in(line: str) -> set[str]:
    low = line.strip().rstrip(".").lower()
    if m := re.fullmatch(r"(.+?) (?:touches|comes to rest in|drops through) (.+)", low):
        return {m[1], m[2]}
    if m := re.fullmatch(r"(.+?) reaches its (?:lower|upper) stop", low):
        return {m[1]}
    return set()

