"""Readbacks of a shot: the flight drawn as residue in two views, or the flight as numbers.

Residue (design entry): a copy of the ball every 0.1 s from launch to first landing, older copies lighter.
The copies are the ball's own dots carried by its real pose at each moment (law 2: the dot belongs to the
object), so spin shows as the dots turning. Everything else is drawn once; it does not move.

Two views, both 512x512 before the box-filter downsample experiment 1 uses:
- camera: experiment 1's fixed perspective camera, unchanged;
- drafting: a side elevation (looking along +y) stacked over a plan (looking down), sharing one x scale,
  so x lines up between the two views as in an engineering drawing.
Same dots, shading, back-face culling and depth test as experiment 1's renderer.
"""

from __future__ import annotations

import mujoco
import numpy as np

from config import RENDER_SIZE
from outcome.settings import (DRAFT_PLAN_Y, DRAFT_RULE_GRAY, DRAFT_SIDE_Z, DRAFT_X, NUMBERS_EVERY_S,
                              RESIDUE_EVERY_S, RESIDUE_OLDEST_WEIGHT)
from outcome.shot import Flight, Shot
from render import dots
from scene import sim

# Drafting layout: one scale for both views, chosen so the two bands fill the square exactly.
DRAFT_SCALE = RENDER_SIZE / (DRAFT_X[1] - DRAFT_X[0])  # px per m
DRAFT_SIDE_H = round((DRAFT_SIDE_Z[1] - DRAFT_SIDE_Z[0]) * DRAFT_SCALE)
DRAFT_PLAN_H = RENDER_SIZE - DRAFT_SIDE_H
assert abs(DRAFT_PLAN_H - (DRAFT_PLAN_Y[1] - DRAFT_PLAN_Y[0]) * DRAFT_SCALE) < 1.0, "drafting ranges do not tile"


def residue_times(flight: Flight) -> list[float]:
    end = flight.landed_at if flight.landed_at is not None else float(flight.times[-1])
    ts = list(np.round(np.arange(0.0, end, RESIDUE_EVERY_S), 4))
    if end - ts[-1] > 1e-6:
        ts.append(round(end, 4))  # the landing itself, newest and darkest
    return ts


def _quat_mat(q: np.ndarray) -> np.ndarray:
    m = np.zeros(9)
    mujoco.mju_quat2Mat(m, q)
    return m.reshape(3, 3)


def _ball_copies(field: dots.DotField, shot: Shot, flight: Flight, ts: list[float]):
    """World points and normals of the ball's dots at each residue time, and each dot's ink weight."""
    model = shot.loaded.model
    g = sim.ball_geom_id(shot.loaded)
    on = field.geom == g
    local, normal = field.local[on], field.normal[on]
    geom_pos, geom_rot = model.geom_pos[g], _quat_mat(model.geom_quat[g])
    pts, nrm, wts = [], [], []
    for k, t in enumerate(ts):
        body_pos, body_quat = flight.at(t)
        R = _quat_mat(body_quat) @ geom_rot
        pts.append(local @ R.T + body_pos + _quat_mat(body_quat) @ geom_pos)
        nrm.append(normal @ R.T)
        w = 1.0 if len(ts) == 1 else RESIDUE_OLDEST_WEIGHT + (1 - RESIDUE_OLDEST_WEIGHT) * k / (len(ts) - 1)
        wts.append(np.full(on.sum(), w))
    return np.concatenate(pts), np.concatenate(nrm), np.concatenate(wts)


def scene_points(field: dots.DotField, shot: Shot, flight: Flight):
    """Every dot to draw: the still scene once, the ball once per residue time. Leaves data at the keyframe."""
    m, d = shot.loaded.model, shot.loaded.data
    mujoco.mj_resetDataKeyframe(m, d, shot.key_id)
    mujoco.mj_forward(m, d)
    p, n = field.world(d)
    still = field.geom != sim.ball_geom_id(shot.loaded)
    bp, bn, bw = _ball_copies(field, shot, flight, residue_times(flight))
    return (np.concatenate([p[still], bp]), np.concatenate([n[still], bn]),
            np.concatenate([np.ones(still.sum()), bw]))


def _splat(xi, yi, z, ink, w, h):
    """Experiment 1's rasterizer: splatted depth test, far first, 2 px opaque marks on white."""
    keep = (xi >= 0) & (yi >= 0) & (xi < w - 1) & (yi < h - 1) & np.isfinite(z)
    xi, yi, z, ink = xi[keep], yi[keep], z[keep], ink[keep]
    depth = np.full((h, w), np.inf)
    s = dots.DEPTH_SPLAT_PX
    for dy in range(-s, s + 1):
        for dx in range(-s, s + 1):
            np.minimum.at(depth, (np.clip(yi + dy, 0, h - 1), np.clip(xi + dx, 0, w - 1)), z)
    visible = z <= depth[yi, xi] + dots.DEPTH_TOLERANCE
    order = np.argsort(-z[visible])
    xs, ys, vs = xi[visible][order], yi[visible][order], ink[visible][order]
    img = np.ones((h, w))
    for dy in range(dots.DOT_PX):
        for dx in range(dots.DOT_PX):
            img[ys + dy, xs + dx] = vs
    return img


def _ink(n: np.ndarray, weight: np.ndarray) -> np.ndarray:
    lambert = np.clip(n @ dots.LIGHT_DIR, 0, 1)
    ink = dots.INK_UNLIT + (dots.INK_LIT - dots.INK_UNLIT) * lambert
    return 1 - (1 - ink) * weight  # an older copy is the same dot, lighter


def camera_image(p, n, w) -> np.ndarray:
    x, y, z = dots.project(p, RENDER_SIZE)
    facing = np.einsum("ni,ni->n", n, dots.CAMERA_EYE - p) > 0
    keep = facing & (z > 0.1)
    return _splat(np.floor(x[keep]).astype(int), np.floor(y[keep]).astype(int), z[keep], _ink(n[keep], w[keep]),
                  RENDER_SIZE, RENDER_SIZE)


def drafting_image(p, n, w) -> np.ndarray:
    side = n[:, 1] < 0  # faces the viewer, who stands at -y looking along +y
    xs = np.floor((p[side, 0] - DRAFT_X[0]) * DRAFT_SCALE).astype(int)
    ys = np.floor((DRAFT_SIDE_Z[1] - p[side, 2]) * DRAFT_SCALE).astype(int)
    top = _splat(xs, ys, p[side, 1], _ink(n[side], w[side]), RENDER_SIZE, DRAFT_SIDE_H)
    plan = n[:, 2] > 0  # faces the viewer above, looking down
    xp = np.floor((p[plan, 0] - DRAFT_X[0]) * DRAFT_SCALE).astype(int)
    yp = np.floor((DRAFT_PLAN_Y[1] - p[plan, 1]) * DRAFT_SCALE).astype(int)
    bottom = _splat(xp, yp, -p[plan, 2], _ink(n[plan], w[plan]), RENDER_SIZE, DRAFT_PLAN_H)
    bottom[0, :] = DRAFT_RULE_GRAY  # the rule between the two views
    return np.vstack([top, bottom])


def render(view: str, field: dots.DotField, shot: Shot, flight: Flight) -> np.ndarray:
    p, n, w = scene_points(field, shot, flight)
    return {"camera": camera_image, "drafting": drafting_image}[view](p, n, w)


def numbers(flight: Flight) -> list[tuple[float, float, float, float]]:
    """The ball's center every 0.05 s from launch to first landing (and the landing itself)."""
    end = flight.landed_at if flight.landed_at is not None else float(flight.times[-1])
    ts = list(np.round(np.arange(0.0, end, NUMBERS_EVERY_S), 4))
    if end - ts[-1] > 1e-6:
        ts.append(round(end, 4))
    return [(t, *(round(float(v), 3) for v in flight.at(t)[0])) for t in ts]


def numbers_table(rows) -> str:
    lines = ["| t (s) | x (m) | y (m) | z (m) |", "|---|---|---|---|"]
    lines += [f"| {t:.2f} | {x:.3f} | {y:.3f} | {z:.3f} |" for t, x, y, z in rows]
    return "\n".join(lines)
