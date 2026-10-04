"""Load a world, run it, and test it against its brief. MuJoCo state only: never the text, never by eye.

Each test returns every check it made and the numbers behind it, so a failure shows exactly what was missing.
The tests were written before any model run (journal, 2026-10-04) and are never shown to the models.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import mujoco
import numpy as np

from scene import sim
from worlds.settings import REST_SPEED, SIM_SECONDS, START_KEY

G = mujoco.mjtGeom


class MissingName(ValueError):
    pass


@dataclass
class Run:
    loaded: sim.Loaded
    times: np.ndarray  # (T,)
    xpos: np.ndarray  # (T, nbody, 3)
    xquat: np.ndarray  # (T, nbody, 4)
    qpos: np.ndarray  # (T, nq)
    qvel: np.ndarray  # (T, nv)
    contacts: list = field(default_factory=list)  # per step: set of (geom, geom) pairs, low id first
    diverged: str | None = None

    @property
    def model(self):
        return self.loaded.model


def load(xml: str) -> sim.Loaded:
    s = sim.load(xml)
    key = mujoco.mj_name2id(s.model, mujoco.mjtObj.mjOBJ_KEY, START_KEY)
    if key >= 0:
        mujoco.mj_resetDataKeyframe(s.model, s.data, key)
        mujoco.mj_forward(s.model, s.data)
        s.log.append(f"reset to keyframe '{START_KEY}'")
    return s


def run(xml: str, seconds: float = SIM_SECONDS) -> Run:
    s = load(xml)
    m, d = s.model, s.data
    steps = round(seconds / m.opt.timestep)
    T = steps + 1
    out = Run(s, np.zeros(T), np.zeros((T, m.nbody, 3)), np.zeros((T, m.nbody, 4)), np.zeros((T, m.nq)),
              np.zeros((T, m.nv)))

    def record(i):
        out.times[i] = d.time
        out.xpos[i], out.xquat[i], out.qpos[i], out.qvel[i] = d.xpos, d.xquat, d.qpos, d.qvel
        out.contacts.append({(min(c.geom1, c.geom2), max(c.geom1, c.geom2)) for c in d.contact[: d.ncon]})

    record(0)
    for i in range(1, T):
        mujoco.mj_step(m, d)
        if not np.all(np.isfinite(d.qpos)):
            out.diverged = f"the simulation blew up at t = {d.time:.3f} s"
            for name in ("times", "xpos", "xquat", "qpos", "qvel"):
                setattr(out, name, getattr(out, name)[:i])
            break
        record(i)
    return out


# ---- names and geometry -------------------------------------------------------------------------------

def body(m, name: str) -> int:
    b = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, name)
    if b < 0:
        raise MissingName(f'no body named "{name}"')
    return b


def geom(m, name: str) -> int:
    g = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_GEOM, name)
    if g < 0:
        raise MissingName(f'no geom named "{name}"')
    return g


def geoms_named(m, prefix: str) -> list[int]:
    gs = [g for g in range(m.ngeom) if (m.geom(g).name or "").startswith(prefix)]
    if not gs:
        raise MissingName(f'no geom named with the prefix "{prefix}"')
    return gs


def geoms_of(m, b: int) -> list[int]:
    gs = [g for g in range(m.ngeom) if m.geom_bodyid[g] == b]
    if not gs:
        raise MissingName(f'body "{m.body(b).name}" has no geoms')
    return gs


def free_joint(m, b: int) -> int:
    for j in range(m.njnt):
        if m.jnt_bodyid[j] == b and m.jnt_type[j] == mujoco.mjtJoint.mjJNT_FREE:
            return j
    raise MissingName(f'body "{m.body(b).name}" has no <freejoint/>')


def half_extents(m, g: int) -> np.ndarray:
    t, s = int(m.geom_type[g]), m.geom_size[g]
    if t == G.mjGEOM_SPHERE:
        return np.array([s[0]] * 3)
    if t == G.mjGEOM_CAPSULE:
        return np.array([s[0], s[0], s[1] + s[0]])
    if t == G.mjGEOM_CYLINDER:
        return np.array([s[0], s[0], s[1]])
    if t in (G.mjGEOM_BOX, G.mjGEOM_ELLIPSOID):
        return s[:3].copy()
    return np.zeros(3)  # planes and anything unbounded add nothing


def aabb(run: Run, gs: list[int], i: int) -> tuple[np.ndarray, np.ndarray]:
    """World bounding box of geoms at step i, from body pose + each geom's local pose and extents."""
    m = run.model
    lo, hi = np.full(3, np.inf), np.full(3, -np.inf)
    for g in gs:
        b = m.geom_bodyid[g]
        Rb = quat_mat(run.xquat[i, b])
        p = run.xpos[i, b] + Rb @ m.geom_pos[g]
        R = Rb @ quat_mat(m.geom_quat[g])
        e = np.abs(R) @ half_extents(m, g)
        lo, hi = np.minimum(lo, p - e), np.maximum(hi, p + e)
    return lo, hi


def quat_mat(q) -> np.ndarray:
    out = np.zeros(9)
    mujoco.mju_quat2Mat(out, np.asarray(q, dtype=float))
    return out.reshape(3, 3)


def speed_at_end(run: Run, b: int, window: float = 0.1) -> float:
    k = max(1, round(window / run.model.opt.timestep))
    return float(np.linalg.norm(run.xpos[-1, b] - run.xpos[-1 - k, b]) / (run.times[-1] - run.times[-1 - k]))


def touched(run: Run, g: int, others: set[int], steps=None) -> bool:
    rng = range(len(run.contacts)) if steps is None else steps
    return any(any((a == g and c in others) or (c == g and a in others) for a, c in run.contacts[i]) for i in rng)


def inside_footprint(p, lo, hi) -> bool:
    return bool(lo[0] <= p[0] <= hi[0] and lo[1] <= p[1] <= hi[1])


def result(checks: dict, values: dict) -> dict:
    checks = {k: bool(v) for k, v in checks.items()}
    return {"passed": all(checks.values()), "checks": checks, "values": values}


# ---- the five tests -----------------------------------------------------------------------------------

def test_shot(run: Run) -> dict:
    m = run.model
    b, g, rims = body(m, "ball"), geom(m, "ball"), geoms_named(m, "rim")
    body(m, "hoop")
    r = float(m.geom_size[g][0])
    rim_pts = np.array([run.xpos[0, m.geom_bodyid[k]] + quat_mat(run.xquat[0, m.geom_bodyid[k]]) @ m.geom_pos[k]
                        for k in rims])
    rim = rim_pts.mean(axis=0)
    inner = float(np.hypot(*(rim_pts[:, :2] - rim[:2]).T).min() - m.geom_size[rims, 0].max())
    start = run.xpos[0, b]
    p = run.xpos[:, b]
    made = False
    for i in np.nonzero((p[:-1, 2] >= rim[2]) & (p[1:, 2] < rim[2]))[0]:
        f = (p[i, 2] - rim[2]) / (p[i, 2] - p[i + 1, 2])
        c = p[i] + f * (p[i + 1] - p[i])
        made = made or float(np.hypot(*(c[:2] - rim[:2]))) < inner
    dist = float(np.hypot(*(rim[:2] - start[:2])))
    checks = {
        "rim at 3.05 m (within 5%)": abs(rim[2] - 3.05) / 3.05 <= 0.05,
        "hoop 4 m away (within 5%)": abs(dist - 4.0) / 4.0 <= 0.05,
        "regulation ball (radius 0.12 m within 5%)": abs(r - 0.12) / 0.12 <= 0.05,
        "launched from the floor": start[2] - r < 0.05,
        "drops through the hoop": made,
    }
    return result(checks, {"rim_z": round(float(rim[2]), 4), "distance": round(dist, 4), "ball_radius": r,
                           "start_height_above_floor": round(float(start[2] - r), 4), "rim_inner_radius": round(inner, 4)})


def test_cup(run: Run) -> dict:
    m = run.model
    b, g, ramps, cup = body(m, "ball"), geom(m, "ball"), geoms_named(m, "ramp"), body(m, "cup")
    cup_gs = geoms_of(m, cup)
    lo0, hi0 = aabb(run, cup_gs, 0)
    lo1, hi1 = aabb(run, cup_gs, -1)
    start, end = run.xpos[0, b], run.xpos[-1, b]
    v = speed_at_end(run, b)
    checks = {
        "ball starts above the cup's rim": start[2] > hi0[2],
        "ball starts outside the cup": not inside_footprint(start, lo0, hi0),
        "ball rolls on the ramp": touched(run, g, set(ramps)),
        "ball at rest at the end": v < REST_SPEED,
        "ball ends in the cup": inside_footprint(end, lo1, hi1) and end[2] < hi1[2],
    }
    return result(checks, {"ball_start": start.round(3).tolist(), "ball_end": end.round(3).tolist(),
                           "end_speed": round(v, 4), "cup_box_end": [lo1.round(3).tolist(), hi1.round(3).tolist()]})


def test_door(run: Run) -> dict:
    m = run.model
    door = body(m, "door")
    j = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, "hinge")
    if j < 0:
        raise MissingName('no joint named "hinge"')
    if m.jnt_type[j] != mujoco.mjtJoint.mjJNT_HINGE or m.jnt_bodyid[j] != door:
        raise MissingName('"hinge" must be a hinge joint on the body "door"')
    q, qd = run.qpos[:, m.jnt_qposadr[j]], run.qvel[:, m.jnt_dofadr[j]]
    last = run.times >= run.times[-1] - 1.0
    lo, hi = m.jnt_range[j] if m.jnt_limited[j] else (-np.inf, np.inf)
    checks = {
        "door starts within its hinge's range": lo - 1e-6 <= q[0] <= hi + 1e-6,
        "door starts open (at least 20 degrees)": abs(q[0]) >= math.radians(20),
        "door shut for the last second (within 2 degrees)": float(np.abs(q[last]).max()) <= math.radians(2),
        "door still at the end": abs(qd[-1]) <= 0.05,
    }
    return result(checks, {"start_deg": round(math.degrees(q[0]), 2),
                           "hinge_range_deg": [round(math.degrees(v), 2) for v in (lo, hi)] if m.jnt_limited[j] else None,
                           "last_second_max_deg": round(math.degrees(float(np.abs(q[last]).max())), 2),
                           "end_rate_rad_s": round(float(qd[-1]), 4)})


def test_stack(run: Run) -> dict:
    m = run.model
    blocks = [body(m, f"block{i}") for i in range(1, 6)]
    boxes = []
    for b in blocks:
        free_joint(m, b)
        bx = [g for g in geoms_of(m, b) if m.geom_type[g] == G.mjGEOM_BOX]
        if not bx:
            raise MissingName(f'body "{m.body(b).name}" has no box geom')
        boxes.append(bx[0])
    z0 = [float(run.xpos[0, b][2]) for b in blocks]
    stacked = all(z0[i] < z0[i + 1] for i in range(4)) and all(
        float(np.hypot(*(run.xpos[0, blocks[i + 1]][:2] - run.xpos[0, blocks[i]][:2]))) <= float(m.geom_size[boxes[i]][:2].min())
        for i in range(4))
    moved = np.stack([np.linalg.norm(run.xpos[:, b] - run.xpos[0, b], axis=1) for b in blocks])  # (5, T)
    pushed = np.nonzero(moved[0] > 0.01)[0]
    t_push = float(run.times[pushed[0]]) if len(pushed) else None
    stood = t_push is not None and t_push >= 0.2 and bool((moved[:, : pushed[0]] < 0.01).all())
    h = 2 * float(m.geom_size[boxes[4]][2])
    drop = z0[4] - float(run.xpos[-1, blocks[4]][2])
    checks = {
        "five blocks stacked at the start": stacked,
        "stack stands until the bottom block is pushed (at least 0.2 s)": stood,
        "stack topples (top block ends two block-heights lower)": drop >= 2 * h,
    }
    return result(checks, {"push_time_s": t_push, "top_block_drop_m": round(drop, 4), "block_height_m": round(h, 4)})


def test_catapult(run: Run) -> dict:
    m = run.model
    b, g, cat, bucket = body(m, "ball"), geom(m, "ball"), geoms_named(m, "catapult"), body(m, "bucket")
    j = free_joint(m, b)
    v0 = float(np.linalg.norm(run.qvel[0, m.jnt_dofadr[j]: m.jnt_dofadr[j] + 3]))
    bucket_gs = geoms_of(m, bucket)
    lo0, hi0 = aabb(run, bucket_gs, 0)
    lo1, hi1 = aabb(run, bucket_gs, -1)
    start, end = run.xpos[0, b], run.xpos[-1, b]
    dist = float(np.hypot(*((lo0[:2] + hi0[:2]) / 2 - start[:2])))
    free = [not any(g in pair for pair in run.contacts[i]) for i in range(len(run.contacts))]
    longest, cur = 0, 0
    for f in free:
        cur = cur + 1 if f else 0
        longest = max(longest, cur)
    airborne = longest * float(m.opt.timestep)
    v = speed_at_end(run, b)
    checks = {
        "ball starts at rest": v0 < 0.01,
        "ball starts in the catapult": touched(run, g, set(cat), steps=range(min(5, len(run.contacts)))),
        "bucket 3 m away (2.5 to 3.5 m)": 2.5 <= dist <= 3.5,
        "ball is thrown (in the air at least 0.2 s)": airborne >= 0.2,
        "ball at rest at the end": v < REST_SPEED,
        "ball ends in the bucket": inside_footprint(end, lo1, hi1) and end[2] < hi1[2],
    }
    return result(checks, {"distance_m": round(dist, 3), "airborne_s": round(airborne, 3), "end_speed": round(v, 4),
                           "ball_end": end.round(3).tolist(), "bucket_box_end": [lo1.round(3).tolist(), hi1.round(3).tolist()]})


TESTS = {"shot": test_shot, "cup": test_cup, "door": test_door, "stack": test_stack, "catapult": test_catapult}


def judge(brief: str, xml: str) -> dict:
    """Load, run and test one world. A world that will not load, or lacks a name, returns the problem instead."""
    try:
        r = run(xml)
    except Exception as e:  # MuJoCo raises ValueError with the parser's message
        return {"loaded": False, "problem": f"MuJoCo could not load the file: {e}"}
    try:
        res = TESTS[brief](r)
    except MissingName as e:
        return {"loaded": True, "problem": f"The scene is missing a name the brief needs: {e}.", "run": r}
    res.update(loaded=True, problem=None, diverged=r.diverged, run=r, load_log=r.loaded.log)
    if r.diverged:
        res["passed"] = False
    return res


def public(j: dict) -> dict:
    return {k: v for k, v in j.items() if k != "run"}
