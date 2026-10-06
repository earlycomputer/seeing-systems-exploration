"""Tests for 1f's three held-out briefs. MuJoCo state only, written before any model run, never shown to the models.

The world language and its library were shaped on 1d's seven briefs. These three were written after, by a session
that did not change the language: a seesaw, a ball off a table's edge, and a chain of three balls. Their tests use
1c's loader, runner and helpers, as 1d's did.
"""

from __future__ import annotations

import mujoco
import numpy as np

from worlds.tests import (MissingName, Run, aabb, body, free_joint, geom, geoms_named, geoms_of, inside_footprint, result,
                          speed_at_end, touched)
from harder.settings import REST_SPEED

J = mujoco.mjtJoint


def _v0(run: Run, b: int) -> float:
    m = run.model
    j = free_joint(m, b)
    return float(np.linalg.norm(run.qvel[0, m.jnt_dofadr[j]: m.jnt_dofadr[j] + 3]))


def _first_touch(run: Run, gs: set[int], others: set[int]) -> int | None:
    for i, pairs in enumerate(run.contacts):
        if any((a in gs and c in others) or (c in gs and a in others) for a, c in pairs):
            return i
    return None


def _first_move(run: Run, b: int, tol: float = 0.01) -> int | None:
    moved = np.nonzero(np.linalg.norm(run.xpos[:, b] - run.xpos[0, b], axis=1) > tol)[0]
    return int(moved[0]) if len(moved) else None


def test_seesaw(run: Run) -> dict:
    m = run.model
    saw = body(m, "seesaw")
    if not any(m.jnt_bodyid[j] == saw and m.jnt_type[j] == J.mjJNT_HINGE for j in range(m.njnt)):
        raise MissingName('the body "seesaw" has no hinge joint')
    saw_gs = set(geoms_of(m, saw))
    wb, bb = body(m, "weight"), body(m, "ball")
    wg, bg = set(geoms_of(m, wb)), set(geoms_of(m, bb))
    w_mass, b_mass = float(m.body_subtreemass[wb]), float(m.body_subtreemass[bb])
    z0 = float(run.xpos[0, bb, 2])
    rise = float(run.xpos[:, bb, 2].max() - z0)
    hit = _first_touch(run, wg, saw_gs)
    start_on = touched(run, next(iter(bg)), saw_gs, steps=range(min(5, len(run.contacts))))
    w_free = [i for i in range(min(5, len(run.contacts))) if not any(g in p for g in wg for p in run.contacts[i])]
    # the ball must rise after the weight lands: its highest point comes after the first hit
    top = int(np.argmax(run.xpos[:, bb, 2]))
    checks = {
        "weight about 1 kg (0.8 to 1.2 kg), ball about 100 g (80 to 120 g)": 0.8 <= w_mass <= 1.2 and 0.08 <= b_mass <= 0.12,
        "ball starts at rest on the seesaw": _v0(run, bb) < 0.01 and start_on,
        "weight starts in the air, clear of the seesaw": len(w_free) == min(5, len(run.contacts)) and _v0(run, wb) < 0.01,
        "weight lands on the seesaw": hit is not None,
        "ball thrown at least 50 cm above where it started, after the weight lands": rise >= 0.5 and hit is not None and top > hit,
    }
    return result(checks, {"weight_kg": round(w_mass, 3), "ball_kg": round(b_mass, 3), "rise_m": round(rise, 3),
                           "weight_lands_s": None if hit is None else round(float(run.times[hit]), 3)})


def test_ledge(run: Run) -> dict:
    m = run.model
    b, g = body(m, "ball"), geom(m, "ball")
    table_gs = geoms_named(m, "table")
    if not table_gs:
        raise MissingName('no geom is named with the prefix "table"')
    bucket = body(m, "bucket")
    bucket_gs = geoms_of(m, bucket)
    start, end = run.xpos[0, b], run.xpos[-1, b]
    tlo, thi = aabb(run, table_gs, 0)
    lo0, hi0 = aabb(run, bucket_gs, 0)
    lo1, hi1 = aabb(run, bucket_gs, -1)
    centre = (lo0[:2] + hi0[:2]) / 2
    # horizontal distance from the bucket's centre to the table's footprint: how far beyond its edge
    dx = max(tlo[0] - centre[0], 0.0, centre[0] - thi[0])
    dy = max(tlo[1] - centre[1], 0.0, centre[1] - thi[1])
    beyond = float(np.hypot(dx, dy))
    on_table = touched(run, g, set(table_gs), steps=range(min(5, len(run.contacts))))
    left = _first_touch(run, {g}, set(bucket_gs) | {i for i in range(m.ngeom) if m.geom(i).name == "floor"})
    v = speed_at_end(run, b)
    checks = {
        "ball starts on the table": on_table and start[2] > 0.3,
        "bucket's centre 60 cm beyond the table's edge (50 to 70 cm)": 0.5 <= beyond <= 0.7,
        "bucket stands on the floor": lo0[2] < 0.01,
        "ball leaves the table and comes down": left is not None,
        "ball at rest at the end": v < REST_SPEED,
        "ball ends in the bucket": inside_footprint(end, lo1, hi1) and end[2] < hi1[2],
    }
    return result(checks, {"beyond_edge_m": round(beyond, 3), "table_top_z": round(float(thi[2]), 3),
                           "ball_end": end.round(3).tolist(), "end_speed": round(v, 4)})


def test_chain(run: Run) -> dict:
    m = run.model
    bs = [body(m, f"ball{i}") for i in (1, 2, 3)]
    gs = [set(geoms_of(m, b)) for b in bs]
    cup = body(m, "cup")
    cup_gs = geoms_of(m, cup)
    lo1, hi1 = aabb(run, cup_gs, -1)
    floor = {i for i in range(m.ngeom) if m.geom(i).name == "floor"}
    on_floor = all(_first_touch(run, g, floor) == 0 for g in gs)
    hit12, hit23 = _first_touch(run, gs[0], gs[1]), _first_touch(run, gs[1], gs[2])
    mv2, mv3 = _first_move(run, bs[1]), _first_move(run, bs[2])
    end = run.xpos[-1, bs[2]]
    v = speed_at_end(run, bs[2])
    checks = {
        "three balls on the floor at the start": on_floor,
        "only ball1 is set moving": _v0(run, bs[1]) < 0.01 and _v0(run, bs[2]) < 0.01,
        "ball1 hits ball2 before ball2 moves": hit12 is not None and mv2 is not None and hit12 <= mv2,
        "ball2 hits ball3 before ball3 moves": hit23 is not None and mv3 is not None and hit23 <= mv3,
        "ball3 at rest at the end": v < REST_SPEED,
        "ball3 ends in the cup": inside_footprint(end, lo1, hi1) and end[2] < hi1[2],
    }
    return result(checks, {"hit12_s": None if hit12 is None else round(float(run.times[hit12]), 3),
                           "hit23_s": None if hit23 is None else round(float(run.times[hit23]), 3),
                           "ball3_end": end.round(3).tolist(), "end_speed": round(v, 4)})


TESTS = {"seesaw": test_seesaw, "ledge": test_ledge, "chain": test_chain}
