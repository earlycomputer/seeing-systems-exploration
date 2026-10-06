"""The picture readback for any world: everything that moves, drawn as residue, framed so the whole run fits.

Experiment 1b's renderer, generalised. The same dots, shading, back-face culling and depth test. A body that
moves is drawn at RESIDUE_COPIES evenly spaced moments from the start to when everything has come to rest
(or the run ends), older copies lighter. Everything else is drawn once.

Two views, both framed from the run itself so nothing is cut off:
- drafting: side elevation (looking along +y) over plan (looking down), one shared scale;
- camera: a perspective view from a raised three-quarter position, like experiment 1's, aimed at the run.
"""

from __future__ import annotations

import numpy as np

from config import RENDER_SIZE
from outcome.draw import _ink, _splat
from render import dots
from worlds.settings import REST_SPEED, RESIDUE_COPIES
from worlds.tests import Run, half_extents, quat_mat

CAMERA_DIR = np.array([-0.4, -1.0, 0.3]) / np.linalg.norm([-0.4, -1.0, 0.3])  # from the target toward the eye
CAMERA_FOVY_DEG = 40.0
RULE_GRAY = 0.5


def moving_bodies(run: Run) -> list[int]:
    out = []
    for b in range(1, run.model.nbody):
        moved = np.linalg.norm(run.xpos[:, b] - run.xpos[0, b], axis=1).max()
        turned = np.abs(np.abs(run.xquat[:, b] @ run.xquat[0, b]) - 1).max()  # 0 when the orientation never changes
        if moved > 0.01 or turned > 1e-4:
            out.append(b)
    return out


def _reach(m, b: int) -> float:
    """How far the body's geoms reach from its origin: a turn of theta radians moves them up to theta * reach."""
    gs = [g for g in range(m.ngeom) if m.geom_bodyid[g] == b]
    return max((float(np.linalg.norm(m.geom_pos[g])) + float(m.geom_rbound[g]) for g in gs), default=0.0)


def active_until(run: Run, bodies: list[int]) -> float:
    """When the last moving body comes to rest (speed over 0.05 s windows), or the run's end.

    A body's speed is its origin's speed plus its turning rate times its reach, so a door or pendulum turning
    about its own origin counts as moving (experiment 1d; 1c measured the origin only).
    """
    k = max(1, round(0.05 / run.model.opt.timestep))
    if not bodies or len(run.times) <= k:
        return float(run.times[-1])
    dt = k * run.model.opt.timestep
    lin = np.linalg.norm(run.xpos[k:, bodies] - run.xpos[:-k, bodies], axis=2) / dt  # (T-k, nb)
    dots_ = np.abs(np.einsum("tbi,tbi->tb", run.xquat[k:, bodies], run.xquat[:-k, bodies]))
    ang = 2 * np.arccos(np.clip(dots_, 0.0, 1.0)) / dt
    reach = np.array([_reach(run.model, b) for b in bodies])
    v = (lin + ang * reach).max(axis=1)
    busy = np.nonzero(v > REST_SPEED)[0]
    end = float(run.times[busy[-1] + k]) if len(busy) else 0.5
    return float(min(run.times[-1], max(0.5, end + 0.1)))


def copy_times(run: Run, bodies: list[int]) -> list[float]:
    return list(np.round(np.linspace(0.0, active_until(run, bodies), RESIDUE_COPIES), 3))


def _step(run: Run, t: float) -> int:
    return int(np.argmin(np.abs(run.times - t)))


def points(field: dots.DotField, run: Run):
    """World points, normals and ink weights: still geoms once, each moving body at every copy time."""
    m = run.model
    moving = moving_bodies(run)
    ts = copy_times(run, moving)
    on_moving = np.isin(m.geom_bodyid[field.geom], moving)
    P, N, W = [], [], []

    def place(mask, i, w):
        g = field.geom[mask]
        b = m.geom_bodyid[g]
        Rb = np.stack([quat_mat(q) for q in run.xquat[i, b]])
        Rg = np.stack([quat_mat(q) for q in m.geom_quat[g]])
        R = Rb @ Rg
        P.append(np.einsum("nij,nj->ni", R, field.local[mask]) + run.xpos[i, b] + np.einsum("nij,nj->ni", Rb, m.geom_pos[g]))
        N.append(np.einsum("nij,nj->ni", R, field.normal[mask]))
        W.append(np.full(mask.sum(), w))

    place(~on_moving, 0, 1.0)
    for k, t in enumerate(ts):
        w = 1.0 if len(ts) == 1 else 0.3 + 0.7 * k / (len(ts) - 1)
        if on_moving.any():
            place(on_moving, _step(run, t), w)
    return np.concatenate(P), np.concatenate(N), np.concatenate(W), {"moving": [m.body(b).name for b in moving],
                                                                    "times": ts}


def extent(run: Run, ts: list[float]) -> tuple[np.ndarray, np.ndarray]:
    """Bounding box of every non-plane geom over the copy times, padded."""
    m = run.model
    lo, hi = np.full(3, np.inf), np.full(3, -np.inf)
    for t in ts:
        i = _step(run, t)
        for g in range(m.ngeom):
            e0 = half_extents(m, g)
            if not e0.any():
                continue
            b = m.geom_bodyid[g]
            Rb = quat_mat(run.xquat[i, b])
            p = run.xpos[i, b] + Rb @ m.geom_pos[g]
            e = np.abs(Rb @ quat_mat(m.geom_quat[g])) @ e0
            lo, hi = np.minimum(lo, p - e), np.maximum(hi, p + e)
    lo[2] = min(lo[2], 0.0)  # always show the floor line
    pad = 0.08 * (hi - lo).max() + 0.1
    return lo - pad, hi + pad


def drafting(field: dots.DotField, run: Run):
    p, n, w, info = points(field, run)
    lo, hi = extent(run, info["times"])
    xr, yr, zr = hi - lo
    s = min(RENDER_SIZE / xr, RENDER_SIZE / (zr + yr))  # px per m, shared by both views
    side_h = int(round(zr * s))
    plan_h = RENDER_SIZE - side_h
    x0 = lo[0] - (RENDER_SIZE / s - xr) / 2  # centre the content across the width
    y_mid = (lo[1] + hi[1]) / 2
    side = n[:, 1] < 0
    top = _splat(np.floor((p[side, 0] - x0) * s).astype(int), np.floor((hi[2] - p[side, 2]) * s).astype(int),
                 p[side, 1], _ink(n[side], w[side]), RENDER_SIZE, side_h)
    plan = n[:, 2] > 0
    yp_top = y_mid + plan_h / s / 2
    bottom = _splat(np.floor((p[plan, 0] - x0) * s).astype(int), np.floor((yp_top - p[plan, 1]) * s).astype(int),
                    -p[plan, 2], _ink(n[plan], w[plan]), RENDER_SIZE, plan_h)
    bottom[0, :] = RULE_GRAY
    info.update(view="drafting", scale_px_per_m=s, x=(round(x0, 2), round(x0 + RENDER_SIZE / s, 2)),
                z=(round(hi[2] - side_h / s, 2), round(hi[2], 2)), y=(round(yp_top - plan_h / s, 2), round(yp_top, 2)))
    return np.vstack([top, bottom]), info


def camera(field: dots.DotField, run: Run):
    p, n, w, info = points(field, run)
    lo, hi = extent(run, info["times"])
    target = (lo + hi) / 2
    radius = np.linalg.norm(hi - lo) / 2
    dist = radius / np.sin(np.radians(CAMERA_FOVY_DEG) / 2) * 1.05
    eye = target + dist * CAMERA_DIR
    f = (target - eye) / np.linalg.norm(target - eye)
    r = np.cross(f, [0.0, 0.0, 1.0]); r /= np.linalg.norm(r)
    u = np.cross(r, f)
    d = p - eye
    xc, yc, zc = d @ r, d @ u, d @ f
    focal = (RENDER_SIZE / 2) / np.tan(np.radians(CAMERA_FOVY_DEG) / 2)
    facing = np.einsum("ni,ni->n", n, eye - p) > 0
    keep = facing & (zc > 0.1)
    img = _splat(np.floor(RENDER_SIZE / 2 + focal * xc[keep] / zc[keep]).astype(int),
                 np.floor(RENDER_SIZE / 2 - focal * yc[keep] / zc[keep]).astype(int),
                 zc[keep], _ink(n[keep], w[keep]), RENDER_SIZE, RENDER_SIZE)
    info.update(view="camera", eye=eye.round(2).tolist(), target=target.round(2).tolist(), fovy=CAMERA_FOVY_DEG)
    return img, info


def render(view: str, field: dots.DotField, run: Run):
    return {"drafting": drafting, "camera": camera}[view](field, run)
