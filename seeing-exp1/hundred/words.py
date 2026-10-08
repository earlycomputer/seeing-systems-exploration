"""The run in words for 1h's ladder: history/narrate.py's history plus what it was blind to.

    text = words.history(run)              # narrate.history, with stops named by height and an Openings section
    text = words.see(run, "your")          # wrapped as history/prompts/see_history.md wraps it

Two additions, after the judge on 1h's runs (2026-10-08; Jono: "yes do it!"):

- Openings. The narrator never said whether something went through a hoop or by how much it missed, yet missing the
  opening was the largest real failure (12 of 40 broken worlds). An opening is a fixed thing made of three or more
  geoms set around the centre of its bounding box on all four sides, with nothing on the vertical line through that
  centre (a hoop, a ring, a frame with guides; not a cup or a box, which have a floor, nor a ramp). Each loose body that comes down through an opening's height is reported
  with its distance from the centre and the opening's half-width, the measure hidden.py's "drops through" uses.
- Hinge stops by height. The narrator said "lower stop" for a joint's lower limit, the most negative angle, which
  authors and the judge read as the end where the part hangs lower. Each "lower/upper stop" is now named by its angle
  and by where the hinged part's centre of mass sits there: "its -45° stop (the end where it sits lower)".

history/narrate.py itself is unchanged, so 1e, 1f, 1g and 1h reproduce as they ran.
"""

from __future__ import annotations

import re

import mujoco
import numpy as np

from history import narrate
from history.settings import PROMPTS as HISTORY_PROMPTS
from hundred.settings import SIM_SECONDS
from worlds.tests import Run, aabb, quat_mat

LEVEL = 0.01  # m: centres of mass closer than this at the two ends: neither end is lower
G = mujoco.mjtGeom


def _inside_geom(m, d, g: int, p: np.ndarray) -> bool:
    local = d.geom_xmat[g].reshape(3, 3).T @ (p - d.geom_xpos[g])
    t, s = int(m.geom_type[g]), m.geom_size[g]
    if t == G.mjGEOM_BOX:
        return bool(np.all(np.abs(local) <= s[:3]))
    if t == G.mjGEOM_SPHERE:
        return bool(np.linalg.norm(local) <= s[0])
    if t == G.mjGEOM_CAPSULE:
        return bool(np.linalg.norm([local[0], local[1], max(0.0, abs(local[2]) - s[1])]) <= s[0])
    if t == G.mjGEOM_CYLINDER:
        return bool(np.hypot(local[0], local[1]) <= s[0] and abs(local[2]) <= s[1])
    if t == G.mjGEOM_ELLIPSOID:
        return bool(np.sum((local / s[:3]) ** 2) <= 1)
    if t == G.mjGEOM_MESH:
        return bool(np.all(np.abs(local - m.geom_aabb[g][:3]) <= m.geom_aabb[g][3:]))
    return False


def openings(run: Run) -> list[tuple[str, list[int]]]:
    """Fixed things that are rings: (name, geoms)."""
    m = run.model
    d = mujoco.MjData(m)
    d.qpos[:] = run.qpos[0]
    mujoco.mj_kinematics(m, d)
    groups: dict[str, list[int]] = {}
    for g in range(m.ngeom):
        b = int(m.geom_bodyid[g])
        if m.geom_type[g] == G.mjGEOM_PLANE or int(m.body_weldid[b]) != 0:
            continue
        name = m.body(b).name if b else (m.geom(g).name or "").split("_")[0]
        if name:
            groups.setdefault(name, []).append(g)
    out = []
    for name, gs in groups.items():
        if len(gs) < 3:
            continue
        lo, hi = aabb(run, gs, 0)
        c = (lo + hi) / 2
        xy = np.array([d.geom_xpos[g][:2] for g in gs]) - c[:2]
        eps = 1e-3
        if not ((xy[:, 0] > eps).any() and (xy[:, 0] < -eps).any() and (xy[:, 1] > eps).any() and (xy[:, 1] < -eps).any()):
            continue  # not around its centre on all four sides: a ramp, a wall, a row of posts
        column = [np.array([c[0], c[1], z]) for z in np.linspace(lo[2], hi[2], 12)]
        if any(_inside_geom(m, d, g, p) for g in gs for p in column):
            continue  # something at the middle, at some height: a cup's floor, a post
        out.append((name, gs))
    return out


def opening_lines(run: Run) -> list[str]:
    n = narrate.Narrator(run)
    free = [mv for mv in n.movers if mv["kind"] == narrate.J.mjJNT_FREE]
    out = []
    for name, gs in openings(run):
        lo, hi = aabb(run, gs, 0)
        c, cz = (lo[:2] + hi[:2]) / 2, (lo[2] + hi[2]) / 2
        r = min(hi[0] - lo[0], hi[1] - lo[1]) / 2
        out.append(f"{name}: an opening {2 * r:.2f} m across, centre ({c[0]:.2f}, {c[1]:.2f}, {cz:.2f}) m")
        said = False
        for mv in free:
            z = run.xpos[:, mv["body"], 2]
            downs = [i for i in range(len(z) - 1) if z[i] >= cz > z[i + 1]]
            if not downs:
                continue
            said = True
            off, i = min((float(np.linalg.norm(run.xpos[i, mv["body"], :2] - c)), i) for i in downs)
            more = f" (down through that height {len(downs)} times; this is the closest)" if len(downs) > 1 else ""
            out.append(f"- {mv['name']} comes down through {name}'s height at {run.times[i]:.2f} s, {off:.2f} m from "
                       f"its centre: {'through it' if off < r else 'outside it, missing by ' + f'{off - r:.2f} m'}{more}")
        if not said:
            out.append(f"- nothing loose comes down through {name}'s height")
    return out


def stop_ends(run: Run) -> dict[tuple[str, str], str]:
    """(mover name, "lower"|"upper") -> how that end sits, by the hinged part's centre of mass."""
    m, n = run.model, narrate.Narrator(run)
    out = {}
    for mv in n.movers:
        j = mv["joint"]
        if mv["kind"] != narrate.J.mjJNT_HINGE or not m.jnt_limited[j]:
            continue
        zs = []
        for q in m.jnt_range[j]:
            d = mujoco.MjData(m)
            d.qpos[:] = run.qpos[0]
            d.qpos[mv["adr"]] = q
            mujoco.mj_kinematics(m, d)
            mujoco.mj_comPos(m, d)
            zs.append(float(d.subtree_com[mv["body"]][2]))
        dz = zs[0] - zs[1]
        if abs(dz) < LEVEL:
            out[(mv["name"], "lower")] = out[(mv["name"], "upper")] = "neither end sits lower"
        else:
            out[(mv["name"], "lower")] = f"the end where it sits {'lower' if dz < 0 else 'higher'}"
            out[(mv["name"], "upper")] = f"the end where it sits {'higher' if dz < 0 else 'lower'}"
    return out


def history(run: Run) -> str:
    text = narrate.history(run)
    ends = stop_ends(run)
    for (name, which), how in ends.items():
        text = re.sub(rf"(?m)^(.*\b{re.escape(name)}\b.*?)its {which} stop \(([^)]+)\)",
                      lambda mt: f"{mt[1]}its {mt[2]} stop ({how})", text)
    lines = opening_lines(run)
    if lines:
        text += ("\n\nOpenings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down "
                 "through one's height:\n" + "\n".join(lines))
    return text


def see(run: Run, whose: str) -> str:
    s = (HISTORY_PROMPTS / "see_history.md").read_text()
    return s.replace("{whose}", whose).replace("{seconds}", f"{SIM_SECONDS:g}").replace("{history}", history(run))
