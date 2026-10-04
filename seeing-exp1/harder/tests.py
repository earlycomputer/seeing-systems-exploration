"""Tests for experiment 1d. MuJoCo state only, written before any model run and never shown to the models.

The five broken worlds use 1c's tests unchanged (worlds/tests.py). The two new briefs, dominoes and pendulum,
are tested here, with 1c's loader, runner and helpers.
"""

from __future__ import annotations

import math

import mujoco
import numpy as np

from worlds import tests as t1c
from worlds.tests import (G, MissingName, Run, aabb, body, free_joint, geom, geoms_named, geoms_of, half_extents,
                          inside_footprint, quat_mat, result, run, speed_at_end, touched)
from harder.settings import REST_SPEED


def _box(m, b: int) -> int:
    bx = [g for g in geoms_of(m, b) if m.geom_type[g] == G.mjGEOM_BOX]
    if not bx:
        raise MissingName(f'body "{m.body(b).name}" has no box geom')
    return bx[0]


def _tilt(run: Run, b: int, g: int, i: int) -> float:
    """Degrees between the box's longest side and vertical at step i."""
    R = quat_mat(run.xquat[i, b]) @ quat_mat(run.model.geom_quat[g])
    axis = R[:, int(np.argmax(half_extents(run.model, g)))]
    return math.degrees(math.acos(min(1.0, abs(float(axis[2])))))


def test_dominoes(run: Run) -> dict:
    m = run.model
    ds = [body(m, f"domino{i}") for i in range(1, 11)]
    gs = []
    for b in ds:
        free_joint(m, b)
        gs.append(_box(m, b))
    tilt0 = [_tilt(run, b, g, 0) for b, g in zip(ds, gs)]
    tilt1 = [_tilt(run, b, g, -1) for b, g in zip(ds, gs)]
    bottoms = [float(aabb(run, [g], 0)[0][2]) for g in gs]
    v0 = [float(np.abs(run.qvel[0, m.jnt_dofadr[free_joint(m, b)]: m.jnt_dofadr[free_joint(m, b)] + 6]).max())
          for b in ds]
    tilts = np.array([[_tilt(run, b, g, i) for b, g in zip(ds, gs)] for i in range(len(run.times))])  # (T, 10)
    moved = [int(np.argmax(tilts[:, k] - tilt0[k] > 2.0)) if (tilts[:, k] - tilt0[k] > 2.0).any() else None
             for k in range(10)]
    t_move = [None if s is None else round(float(run.times[s]), 3) for s in moved]
    in_order = all(t_move[k] is not None for k in range(10)) and all(t_move[k] < t_move[k + 1] for k in range(1, 9)) \
        and t_move[0] <= t_move[1]
    checks = {
        # The first may start already tipped ("the first is tipped over"); the other nine must stand upright.
        "ten dominoes on the floor at the start, the other nine upright": all(a <= 10 for a in tilt0[1:]) and all(z < 0.01 for z in bottoms),
        "only the first domino is set moving": all(v < 1e-6 for v in v0[1:]),
        "they fall in order, each after the one before": in_order,
        "every domino ends tilted at least 15 degrees": all(a >= 15 for a in tilt1),
    }
    return result(checks, {"tilt_start_deg": [round(a, 1) for a in tilt0], "tilt_end_deg": [round(a, 1) for a in tilt1],
                           "first_moves_s": t_move})


def test_pendulum(run: Run) -> dict:
    m = run.model
    pend = body(m, "pendulum")
    if not any(m.jnt_bodyid[j] == pend and m.jnt_type[j] == mujoco.mjtJoint.mjJNT_HINGE for j in range(m.njnt)):
        raise MissingName('the body "pendulum" has no hinge joint')
    pg = set(geoms_named(m, "pendulum"))
    b, g, cup = body(m, "ball"), geom(m, "ball"), body(m, "cup")
    j = free_joint(m, b)
    r = float(m.geom_size[g][0])
    v0 = float(np.linalg.norm(run.qvel[0, m.jnt_dofadr[j]: m.jnt_dofadr[j] + 6]))
    cup_gs = geoms_of(m, cup)
    lo0, hi0 = aabb(run, cup_gs, 0)
    lo1, hi1 = aabb(run, cup_gs, -1)
    start, end = run.xpos[0, b], run.xpos[-1, b]
    dist = float(np.hypot(*((lo0[:2] + hi0[:2]) / 2 - start[:2])))
    hit = [i for i in range(len(run.contacts)) if touched(run, g, pg, steps=[i])]
    moved = np.nonzero(np.linalg.norm(run.xpos[:, b] - start, axis=1) > 0.01)[0]
    struck = bool(hit) and (not len(moved) or moved[0] >= hit[0])
    v = speed_at_end(run, b)
    checks = {
        "ball starts at rest on the floor": v0 < 0.01 and start[2] - r < 0.01,
        "cup's centre 1 m from where the ball starts (0.9 to 1.1 m)": 0.9 <= dist <= 1.1,
        "the pendulum strikes the ball and sets it moving": struck,
        "ball at rest at the end": v < REST_SPEED,
        "ball ends in the cup": inside_footprint(end, lo1, hi1) and end[2] < hi1[2],
    }
    return result(checks, {"cup_distance_m": round(dist, 3), "first_hit_s": round(float(run.times[hit[0]]), 3) if hit else None,
                           "ball_end": end.round(3).tolist(), "end_speed": round(v, 4),
                           "cup_box_end": [lo1.round(3).tolist(), hi1.round(3).tolist()]})


TESTS = dict(t1c.TESTS, dominoes=test_dominoes, pendulum=test_pendulum)


def judge(test: str, xml: str) -> dict:
    """Load, run and test one world, as 1c's judge does, with 1d's two extra tests."""
    try:
        r = run(xml)
    except Exception as e:  # MuJoCo raises ValueError with the parser's message
        return {"loaded": False, "problem": f"MuJoCo could not load the file: {e}"}
    try:
        res = TESTS[test](r)
    except MissingName as e:
        return {"loaded": True, "problem": f"The scene is missing a name the brief needs: {e}.", "run": r}
    res.update(loaded=True, problem=None, diverged=r.diverged, run=r, load_log=r.loaded.log)
    if r.diverged:
        res["passed"] = False
    return res


public = t1c.public
