"""Body state -> dot field -> 512x512 grayscale image.

Law 2, the dot belongs to the object: points are sampled once on each geom's surface in that geom's own
frame, then moved by the geom's pose from mjData every frame. Nothing is re-sampled when things move.

Law 3, material is information: the only variation is shading by surface normal against one fixed key
light, plus perspective. Dots are dark marks on a white ground, opaque, no blending; the nearest dot wins.
Back faces are dropped and a splatted depth test hides dots behind other objects.
"""

from __future__ import annotations

from dataclasses import dataclass

import mujoco
import numpy as np

from config import RENDER_SIZE

G = mujoco.mjtGeom
PLANE, SPHERE, CAPSULE, ELLIPSOID, CYLINDER, BOX = (int(G.mjGEOM_PLANE), int(G.mjGEOM_SPHERE), int(G.mjGEOM_CAPSULE),
                                                  int(G.mjGEOM_ELLIPSOID), int(G.mjGEOM_CYLINDER), int(G.mjGEOM_BOX))

# Fixed pinhole camera: a raised three-quarter view from the ball's side of the court, so the ball->hoop
# line runs left to right and slightly away, the rim reads as an ellipse, and the backboard's face shows.
CAMERA_TARGET = np.array([2.6, 0.0, 1.7])
CAMERA_EYE = CAMERA_TARGET + 9.5 * np.array([-0.4, -1.0, 0.3]) / np.linalg.norm([-0.4, -1.0, 0.3])
CAMERA_FOVY_DEG = 40.0

LIGHT_DIR = np.array([-0.3, -0.6, 1.0]) / np.linalg.norm([-0.3, -0.6, 1.0])  # one key, from above
INK_UNLIT, INK_LIT = 0.08, 0.68  # gray level of a dot facing away from / straight at the light; ground is 1.0

N_DOTS = 20_000
FLOOR_SHARE = 0.25  # of N_DOTS, spread over the floor window below
FLOOR_WINDOW = ((-3.0, 7.0), (-4.0, 4.0))  # plane-local x and y ranges that the camera can see
MIN_DOTS_PER_BODY = 400  # every other surface gets the same density; this only lifts small bodies (the ball)
DOT_PX = 2
DEPTH_SPLAT_PX = 1  # each dot claims depth over a (2*1+1)^2 neighbourhood
DEPTH_TOLERANCE = 0.15  # m


def _unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v, axis=-1, keepdims=True)


def _sphere_dirs(rng, n):
    return _unit(rng.normal(size=(n, 3)))


def _sample_sphere(rng, n, size):
    d = _sphere_dirs(rng, n)
    return d * size[0], d


def _sample_ellipsoid(rng, n, size):
    # Not exactly area-uniform; close enough for a legibility renderer.
    d = _sphere_dirs(rng, n)
    p = d * size[:3]
    return p, _unit(d / size[:3])


def _sample_cylinder(rng, n, size):
    r, h = size[0], size[1]
    side, cap = 2 * np.pi * r * 2 * h, np.pi * r * r
    k = rng.choice(3, size=n, p=np.array([side, cap, cap]) / (side + 2 * cap))
    th = rng.uniform(0, 2 * np.pi, n)
    p, nrm = np.zeros((n, 3)), np.zeros((n, 3))
    s = k == 0
    p[s] = np.c_[r * np.cos(th[s]), r * np.sin(th[s]), rng.uniform(-h, h, s.sum())]
    nrm[s] = np.c_[np.cos(th[s]), np.sin(th[s]), np.zeros(s.sum())]
    for cap_k, z in ((1, h), (2, -h)):
        c = k == cap_k
        rr = r * np.sqrt(rng.uniform(0, 1, c.sum()))
        p[c] = np.c_[rr * np.cos(th[c]), rr * np.sin(th[c]), np.full(c.sum(), z)]
        nrm[c] = [0, 0, np.sign(z)]
    return p, nrm


def _sample_capsule(rng, n, size):
    r, h = size[0], size[1]
    side, ends = 2 * np.pi * r * 2 * h, 4 * np.pi * r * r
    on_side = rng.uniform(0, side + ends, n) < side
    p, nrm = np.zeros((n, 3)), np.zeros((n, 3))
    th = rng.uniform(0, 2 * np.pi, on_side.sum())
    p[on_side] = np.c_[r * np.cos(th), r * np.sin(th), rng.uniform(-h, h, on_side.sum())]
    nrm[on_side] = np.c_[np.cos(th), np.sin(th), np.zeros(on_side.sum())]
    d = _sphere_dirs(rng, (~on_side).sum())
    p[~on_side] = d * r + np.c_[np.zeros(len(d)), np.zeros(len(d)), np.sign(d[:, 2]) * h]
    nrm[~on_side] = d
    return p, nrm


def _sample_box(rng, n, size):
    a, b, c = size[:3]
    areas = np.array([b * c, b * c, a * c, a * c, a * b, a * b])
    face = rng.choice(6, size=n, p=areas / areas.sum())
    u = rng.uniform(-1, 1, (n, 3)) * size[:3]
    axis, sign = face // 2, np.where(face % 2 == 0, 1.0, -1.0)
    u[np.arange(n), axis] = sign * size[axis]
    nrm = np.zeros((n, 3))
    nrm[np.arange(n), axis] = sign
    return u, nrm


def _sample_plane(rng, n, size):
    (x0, x1), (y0, y1) = FLOOR_WINDOW
    if size[0] > 0:
        x0, x1 = max(x0, -size[0]), min(x1, size[0])
    if size[1] > 0:
        y0, y1 = max(y0, -size[1]), min(y1, size[1])
    p = np.c_[rng.uniform(x0, x1, n), rng.uniform(y0, y1, n), np.zeros(n)]
    return p, np.tile([0.0, 0.0, 1.0], (n, 1))


SAMPLERS = {SPHERE: _sample_sphere, ELLIPSOID: _sample_ellipsoid, CYLINDER: _sample_cylinder,
            CAPSULE: _sample_capsule, BOX: _sample_box, PLANE: _sample_plane}


def _area(gtype, size) -> float:
    gtype = int(gtype)
    r, h = size[0], size[1]
    if gtype == SPHERE:
        return 4 * np.pi * r * r
    if gtype == ELLIPSOID:
        a, b, c = size[:3]
        return 4 * np.pi * ((a * b) ** 1.6 + (a * c) ** 1.6 + (b * c) ** 1.6) ** (1 / 1.6) / 3 ** (1 / 1.6)
    if gtype == CYLINDER:
        return 2 * np.pi * r * 2 * h + 2 * np.pi * r * r
    if gtype == CAPSULE:
        return 2 * np.pi * r * 2 * h + 4 * np.pi * r * r
    if gtype == BOX:
        a, b, c = size[:3]
        return 8 * (a * b + b * c + a * c)
    raise ValueError(gtype)


@dataclass
class DotField:
    geom: np.ndarray  # (N,) geom id each dot belongs to
    local: np.ndarray  # (N, 3) position in that geom's frame, fixed for the life of the field
    normal: np.ndarray  # (N, 3) outward normal in that geom's frame
    skipped: list[str]  # geoms not drawn, and why

    @classmethod
    def sample(cls, model: mujoco.MjModel, seed: int, n_dots: int = N_DOTS) -> "DotField":
        rng = np.random.default_rng(seed)
        planes, solids, skipped = [], [], []
        for g in range(model.ngeom):
            name = model.geom(g).name or f"geom{g}"
            if model.geom_rgba[g][3] == 0:
                skipped.append(f"{name}: invisible (alpha 0)")
            elif int(model.geom_type[g]) == PLANE:
                planes.append(g)
            elif int(model.geom_type[g]) in SAMPLERS:
                solids.append(g)
            else:
                skipped.append(f"{name}: geom type {mujoco.mjtGeom(model.geom_type[g]).name} not drawn")
        counts = {}
        if planes:
            for g in planes:
                counts[g] = int(n_dots * FLOOR_SHARE / len(planes))
        budget = n_dots - sum(counts.values())
        if solids:
            # One density for every solid surface, then lift any body below the minimum as a whole, so a
            # segmented rim is not denser than a one-piece one.
            areas = np.array([_area(model.geom_type[g], model.geom_size[g]) for g in solids])
            share = budget * areas / areas.sum()
            bodies = model.geom_bodyid[solids]
            for b in np.unique(bodies):
                on = bodies == b
                if share[on].sum() < MIN_DOTS_PER_BODY:
                    share[on] *= MIN_DOTS_PER_BODY / share[on].sum()
            counts.update({g: max(1, int(round(c))) for g, c in zip(solids, share)})
        geom, local, normal = [], [], []
        for g, k in counts.items():
            p, nrm = SAMPLERS[int(model.geom_type[g])](rng, k, model.geom_size[g])
            geom.append(np.full(k, g)), local.append(p), normal.append(nrm)
        return cls(np.concatenate(geom), np.concatenate(local), np.concatenate(normal), skipped)

    def world(self, data: mujoco.MjData) -> tuple[np.ndarray, np.ndarray]:
        R = data.geom_xmat[self.geom].reshape(-1, 3, 3)
        p = np.einsum("nij,nj->ni", R, self.local) + data.geom_xpos[self.geom]
        return p, np.einsum("nij,nj->ni", R, self.normal)


def camera_basis():
    f = _unit(CAMERA_TARGET - CAMERA_EYE)
    r = _unit(np.cross(f, [0.0, 0.0, 1.0]))
    return r, np.cross(r, f), f


def project(points: np.ndarray, size: int = RENDER_SIZE):
    """World points -> (x px, y px, depth m). Pixel (0, 0) is top left."""
    r, u, f = camera_basis()
    d = points - CAMERA_EYE
    xc, yc, zc = d @ r, d @ u, d @ f
    focal = (size / 2) / np.tan(np.radians(CAMERA_FOVY_DEG) / 2)
    with np.errstate(divide="ignore", invalid="ignore"):
        return size / 2 + focal * xc / zc, size / 2 - focal * yc / zc, zc


def draw(field: DotField, data: mujoco.MjData, size: int = RENDER_SIZE) -> np.ndarray:
    """Returns a float image in [0, 1], white ground, dark dots."""
    p, n = field.world(data)
    x, y, z = project(p, size)
    facing = np.einsum("ni,ni->n", n, CAMERA_EYE - p) > 0
    xi, yi = np.floor(x).astype(int), np.floor(y).astype(int)
    keep = facing & (z > 0.1) & (xi >= 0) & (yi >= 0) & (xi < size - 1) & (yi < size - 1)
    xi, yi, z, n = xi[keep], yi[keep], z[keep], n[keep]

    depth = np.full((size, size), np.inf)
    s = DEPTH_SPLAT_PX
    for dy in range(-s, s + 1):
        for dx in range(-s, s + 1):
            np.minimum.at(depth, (np.clip(yi + dy, 0, size - 1), np.clip(xi + dx, 0, size - 1)), z)
    visible = z <= depth[yi, xi] + DEPTH_TOLERANCE

    lambert = np.clip(n @ LIGHT_DIR, 0, 1)
    ink = INK_UNLIT + (INK_LIT - INK_UNLIT) * lambert
    order = np.argsort(-z[visible])  # far first, so near dots land on top
    xs, ys, vs = xi[visible][order], yi[visible][order], ink[visible][order]
    img = np.ones((size, size))
    for dy in range(DOT_PX):
        for dx in range(DOT_PX):
            img[ys + dy, xs + dx] = vs
    return img


def to_png_bytes(img: np.ndarray) -> bytes:
    import io
    from PIL import Image
    buf = io.BytesIO()
    Image.fromarray(np.round(np.clip(img, 0, 1) * 255).astype(np.uint8), mode="L").save(buf, format="PNG")
    return buf.getvalue()
