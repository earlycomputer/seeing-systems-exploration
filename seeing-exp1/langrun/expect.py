"""Expectations in words, checked against a run: the language's `expect` block, for either format.

    results = check(lines, run, owner)     # [(line, held, evidence), ...]

The same four forms as the language (typed/lang.py), judged on the MuJoCo run itself rather than on the replay's
event list, so a raw MJCF file can carry them too. Two faults of the language's own checker are fixed here: a
touch that is already happening at the start counts (a ball resting on a table touches it), and names may have
spaces or a part's piece (`catapult.scoop base`, `cup ramp`), matched to MuJoCo names as `catapult_scoop_base`.

A name matches a geom when it is the geom's name, the start of it (`bucket` matches `bucket_base`), its body's name,
or, for the language, the label the compiler gave it (`hoop.rim`).
"""

from __future__ import annotations

import math
import re

import mujoco
import numpy as np

from worlds.tests import Run, aabb, free_joint

REST = 0.05  # m/s, as the tests and the replay
STOP = math.radians(0.5)  # within this of a range end counts as at the stop
FORMS = ("<thing> touches <thing>", "<thing> comes to rest in <thing>", "<thing> drops through <thing>",
         "<thing> reaches its lower stop", "<thing> reaches its upper stop")


def key(name: str) -> str:
    return re.sub(r"[\s.]+", "_", name.strip().lower())


def geoms(run: Run, name: str, owner: dict | None = None) -> list[int]:
    m, k, out = run.model, key(name), []
    for g in range(m.ngeom):
        gname = key(m.geom(g).name)
        bname = key(m.body(m.geom_bodyid[g]).name)
        label = key((owner or {}).get(m.geom(g).name, ""))
        if k in (gname, bname, label) or gname.startswith(k + "_") or (label and label.startswith(k + "_")):
            out.append(g)
    return out


def bodies(run: Run, gs: list[int]) -> list[int]:
    return sorted({int(run.model.geom_bodyid[g]) for g in gs} - {0})


def speed(run: Run, b: int) -> np.ndarray:
    m = run.model
    j = free_joint(m, b)
    return np.linalg.norm(run.qvel[:, m.jnt_dofadr[j]: m.jnt_dofadr[j] + 3], axis=1)


def one(line: str, run: Run, owner: dict | None) -> tuple[bool, str]:
    s = line.strip().rstrip(".")
    low = s.lower()
    if m := re.fullmatch(r"(.+?) touches (.+)", low):
        a, b = geoms(run, m[1], owner), geoms(run, m[2], owner)
        if not a or not b:
            return False, f"there is no thing named {m[1] if not a else m[2]}"
        A, B = set(a), set(b)
        for i, pairs in enumerate(run.contacts):
            if any((x in A and y in B) or (x in B and y in A) for x, y in pairs):
                return True, ("touching from the start" if i == 0 else f"first touch at {run.times[i]:.2f} s")
        return False, "they never touch"
    if m := re.fullmatch(r"(.+?) comes to rest in (.+)", low):
        a, b = geoms(run, m[1], owner), geoms(run, m[2], owner)
        if not a or not b:
            return False, f"there is no thing named {m[1] if not a else m[2]}"
        mover = [x for x in bodies(run, a) if free_joint_or_none(run, x) is not None]
        if not mover:
            return False, f"{m[1]} is not a loose thing"
        x = mover[0]
        v = speed(run, x)
        tail = v[run.times >= run.times[-1] - 0.1]
        p = run.xpos[-1, x]
        lo, hi = aabb(run, b, -1)
        inside = lo[0] <= p[0] <= hi[0] and lo[1] <= p[1] <= hi[1] and p[2] < hi[2]
        if tail.max() >= REST:
            return False, f"{m[1]} is still moving at the end ({v[-1]:.2f} m/s), {'inside' if inside else 'outside'} {m[2]}"
        if not inside:
            return False, f"{m[1]} comes to rest at ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f}) m, outside {m[2]}"
        return True, f"{m[1]} at rest inside {m[2]} at the end"
    if m := re.fullmatch(r"(.+?) drops through (.+)", low):
        a, b = geoms(run, m[1], owner), geoms(run, m[2], owner)
        if not a or not b:
            return False, f"there is no thing named {m[1] if not a else m[2]}"
        x = bodies(run, a)[0]
        z = run.xpos[:, x, 2]
        nearest = None
        for i in range(len(z) - 1):
            lo, hi = aabb(run, b, i)
            cz = (lo[2] + hi[2]) / 2
            if z[i] >= cz > z[i + 1]:
                c = (lo[:2] + hi[:2]) / 2
                r = min(hi[0] - lo[0], hi[1] - lo[1]) / 2
                off = float(np.linalg.norm(run.xpos[i, x, :2] - c))
                if off < r:
                    return True, f"through at {run.times[i]:.2f} s, {off * 100:.0f} cm from its centre"
                nearest = off if nearest is None else min(nearest, off)
        if nearest is None:
            return False, f"{m[1]} never comes down through {m[2]}'s height"
        return False, f"{m[1]} comes down through {m[2]}'s height {nearest:.2f} m from its centre, outside it"
    if m := re.fullmatch(r"(.+?) reaches its (lower|upper) stop", low):
        mm, k = run.model, key(m[1])
        js = [j for j in range(mm.njnt) if mm.jnt_type[j] == mujoco.mjtJoint.mjJNT_HINGE and
              (key(mm.joint(j).name) == k or mm.jnt_bodyid[j] in bodies(run, geoms(run, m[1], owner)))]
        js = [j for j in js if mm.jnt_limited[j]]
        if not js:
            return False, f"{m[1]} has no hinge with a range"
        j = js[0]
        q = run.qpos[:, mm.jnt_qposadr[j]]
        end = mm.jnt_range[j][0 if m[2] == "lower" else 1]
        at = np.abs(q - end) < STOP
        hits = np.nonzero(at)[0]
        away = np.nonzero(~at)[0]
        if len(hits) and len(away) and hits[-1] > away[0]:
            first = next(i for i in hits if i > away[0])
            return True, f"at its {m[2]} stop ({math.degrees(end):.0f}°) at {run.times[first]:.2f} s"
        if len(hits) and not len(away):
            return False, f"it starts at its {m[2]} stop ({math.degrees(end):.0f}°) and never leaves it"
        return False, (f"it never reaches its {m[2]} stop ({math.degrees(end):.0f}°); it gets within "
                       f"{math.degrees(np.abs(q - end).min()):.0f}°")
    return False, "I can't read this; the forms are: " + "; ".join(FORMS)


def free_joint_or_none(run: Run, b: int) -> int | None:
    try:
        return free_joint(run.model, b)
    except Exception:
        return None


def check(lines: list[str], run: Run, owner: dict | None = None) -> list[tuple[str, bool, str]]:
    return [(line, *one(line, run, owner)) for line in lines if line.strip() and not line.strip().startswith("--")]


def block(text: str | None) -> list[str]:
    """The lines of an ```expect block (every line)."""
    return [s.strip() for s in (text or "").splitlines() if s.strip()]


def section(text: str | None) -> list[str]:
    """The lines of a .world file's `expect` section; none when it has no such section."""
    if not text:
        return []
    lines, on = [], False
    for raw in text.splitlines():
        if raw.strip() == "expect" and not raw.startswith(" "):
            on = True
            continue
        if on:
            if raw and not raw.startswith((" ", "\t")):
                break
            lines.append(raw.strip())
    return [s for s in lines if s]


def words(results: list[tuple[str, bool, str]]) -> str:
    if not results:
        return ""
    held = sum(ok for _, ok, _ in results)
    out = [f"Your expectations, checked against the run ({held} of {len(results)} hold):", ""]
    out += [f"- {'holds' if ok else 'DOES NOT HOLD'}: {line} ({evidence})" for line, ok, evidence in results]
    return "\n".join(out)
