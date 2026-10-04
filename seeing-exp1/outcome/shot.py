"""The shot: add air, fly the ball from the `shot` keyframe to its first landing, and judge where it went.

Everything here is MuJoCo state, never the text and never by eye. Two flights are run per shot:

- the real flight, with every contact, decides whether the shot is made;
- a ghost flight, with the hoop and its support made non-colliding, says where the ball's path crosses the
  rim's plane on the way down. That crossing, measured along and across the shot's line, is what "short",
  "long", "left" and "right" mean, whatever the ball then hits.

Edits to the scene are one line each, like experiment 1's errors, so the model sees exactly what changed.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

import mujoco
import numpy as np

from outcome.settings import AIR_DENSITY, BALL_FLUID, MAX_FLIGHT_S, MISSES, SHOT_KEY
from scene import sim

# ---- one-line edits -----------------------------------------------------------------------------------


def _one_line(xml: str, pattern: str, what: str) -> re.Match:
    m = re.search(pattern, xml)
    if not m:
        raise ValueError(f"no {what} in scene text")
    if "\n" in m.group(0):
        raise ValueError(f"{what} spans lines; the edit would not be one line")
    return m


def _replace_line(xml: str, m: re.Match, new_tag: str) -> tuple[str, dict]:
    new_xml = xml[: m.start()] + new_tag + xml[m.end():]
    line_no = xml.count("\n", 0, m.start()) + 1
    assert sum(a != b for a, b in zip(xml.splitlines(), new_xml.splitlines())) <= 1
    return new_xml, {"line": line_no, "before": xml.splitlines()[line_no - 1].strip(),
                     "after": new_xml.splitlines()[line_no - 1].strip()}


def add_air(xml: str) -> tuple[str, list[dict]]:
    """Air as two one-line edits: density on <option>, the ellipsoid fluid model on the ball's geom."""
    edits = []
    m = _one_line(xml, r"<option\b[^>]*>", "<option> element")
    xml, e = _replace_line(xml, m, sim._set_attr(m.group(0), "density", f"{AIR_DENSITY:g}"))
    edits.append({"what": "air density", **e})
    m = sim._tag(xml, "geom", sim.BALL)
    tag = m.group(0)
    for attr, value in BALL_FLUID.items():
        tag = sim._set_attr(tag, attr, value)
    xml, e = _replace_line(xml, m, tag)
    edits.append({"what": "ball fluid model", **e})
    return xml, edits


def shot_tag(xml: str) -> re.Match:
    return _one_line(xml, rf'<key\b[^>]*\bname="{SHOT_KEY}"[^>]*>', f'<key name="{SHOT_KEY}">')


def shot_qvel(xml: str) -> list[float]:
    m = re.search(r'\bqvel="([^"]*)"', shot_tag(xml).group(0))
    if not m:
        raise ValueError(f'<key name="{SHOT_KEY}"> has no qvel')
    return [float(v) for v in m.group(1).split()]


def _fmt(values) -> str:
    return " ".join(f"{v:.6g}" for v in values)


def set_qvel(xml: str, qvel) -> tuple[str, dict]:
    m = shot_tag(xml)
    return _replace_line(xml, m, sim._set_attr(m.group(0), "qvel", _fmt(qvel)))


def scaled(qvel: list[float], factor: float) -> list[float]:
    """Launch speed times factor, same direction; spin unchanged."""
    return [v * factor for v in qvel[:3]] + list(qvel[3:])


def turned(qvel: list[float], degrees: float) -> list[float]:
    """Aim turned about the vertical by degrees, toward +y for positive; spin turned with it."""
    c, s = math.cos(math.radians(degrees)), math.sin(math.radians(degrees))
    rot = lambda v: [c * v[0] - s * v[1], s * v[0] + c * v[1], v[2]]  # noqa: E731
    return rot(qvel[:3]) + (rot(qvel[3:6]) if len(qvel) >= 6 else []) + list(qvel[6:])


def inject(xml: str, miss: str, step: float) -> tuple[str, dict]:
    """A deliberate miss as a one-line edit to the keyframe. Returns the new text and a record of the edit."""
    kind = MISSES[miss]["kind"]
    if kind == "none":
        return xml, {"miss": "none"}
    qvel = shot_qvel(xml)
    new = scaled(qvel, 1 + step) if kind == "speed" else turned(qvel, step)
    new_xml, e = set_qvel(xml, new)
    return new_xml, {"miss": miss, "kind": kind, "step": step, **e}


# ---- flight -------------------------------------------------------------------------------------------


LANDING_Z = 0.5  # m, ball center: a contact below this after leaving the floor is a landing


@dataclass
class Flight:
    times: np.ndarray  # (T,) s, every physics step from launch to first landing (or MAX_FLIGHT_S)
    pos: np.ndarray  # (T, 3) ball center
    quat: np.ndarray  # (T, 4) ball orientation, for drawing the dots where they really are
    landed_at: float | None  # first floor contact after leaving the floor
    touched: list[str] = field(default_factory=list)  # geoms the ball hit before landing, in order

    def at(self, t: float) -> tuple[np.ndarray, np.ndarray]:
        i = int(np.argmin(np.abs(self.times - t)))
        return self.pos[i], self.quat[i]


@dataclass
class Shot:
    loaded: sim.Loaded
    key_id: int
    rim: np.ndarray  # rim center, world
    inner_radius: float  # horizontal, rim center to the inside of the tube
    ball_radius: float


def load(xml: str) -> Shot:
    s = sim.load(xml)
    key_id = mujoco.mj_name2id(s.model, mujoco.mjtObj.mjOBJ_KEY, SHOT_KEY)
    if key_id < 0:
        raise ValueError(f'no <key name="{SHOT_KEY}"> in the scene')
    rim = sim.rim_center(s)
    names = [s.model.geom(i).name for i in range(s.model.ngeom)]
    rim_ids = [i for i, n in enumerate(names) if n.startswith(sim.RIM_PREFIX)]
    if rim_ids:
        dist = np.hypot(*(s.data.geom_xpos[rim_ids][:, :2] - rim[:2]).T)
        inner = float(dist.min() - s.model.geom_size[rim_ids, 0].max())
    else:
        inner = 0.2286  # regulation, 18 in
        s.log.append("no rim* geoms; inner radius taken as regulation 0.2286 m")
    return Shot(s, key_id, rim, inner, float(s.model.geom_size[sim.ball_geom_id(s)][0]))


def fly(shot: Shot, ghost: bool = False) -> Flight:
    """Reset to the keyframe and step until the ball first lands after leaving the floor."""
    m, d = shot.loaded.model, shot.loaded.data
    saved = (m.geom_contype.copy(), m.geom_conaffinity.copy())
    ball_body = m.body(sim.BALL).id
    ball_geom = sim.ball_geom_id(shot.loaded)
    floor = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_GEOM, "floor")
    if ghost:  # only the ball and the floor collide
        keep = {ball_geom, floor}
        for g in range(m.ngeom):
            if g not in keep:
                m.geom_contype[g] = m.geom_conaffinity[g] = 0
    try:
        mujoco.mj_resetDataKeyframe(m, d, shot.key_id)
        mujoco.mj_forward(m, d)
        times, pos, quat, touched = [d.time], [d.xpos[ball_body].copy()], [d.xquat[ball_body].copy()], []
        airborne, landed = False, None
        while d.time < MAX_FLIGHT_S:
            mujoco.mj_step(m, d)
            times.append(d.time), pos.append(d.xpos[ball_body].copy()), quat.append(d.xquat[ball_body].copy())
            hits = set()
            for c in d.contact[: d.ncon]:
                if ball_geom in (c.geom1, c.geom2):
                    hits.add(c.geom2 if c.geom1 == ball_geom else c.geom1)
            for g in sorted(hits - {floor}):
                name = m.geom(g).name or f"geom{g}"
                if not touched or touched[-1] != name:
                    touched.append(name)
            if not airborne and floor not in hits and pos[-1][2] > shot.ball_radius + 0.02:
                airborne = True
            elif airborne and hits and pos[-1][2] < LANDING_Z:
                landed = float(d.time)  # the floor, or anything standing on it (a support's base plate)
                break
        return Flight(np.array(times), np.array(pos), np.array(quat), landed, touched)
    finally:
        m.geom_contype[:], m.geom_conaffinity[:] = saved


def _down_crossings(flight: Flight, z: float) -> list[np.ndarray]:
    """Points where the ball center passes down through height z, interpolated between steps."""
    out = []
    p = flight.pos
    for i in np.nonzero((p[:-1, 2] >= z) & (p[1:, 2] < z))[0]:
        f = (p[i, 2] - z) / (p[i, 2] - p[i + 1, 2])
        out.append(p[i] + f * (p[i + 1] - p[i]))
    return out


def judge(xml: str) -> dict:
    """Made or not, and where the path crosses the rim's plane, along and across the shot's line."""
    shot = load(xml)
    qvel = shot_qvel(xml)
    real, ghost = fly(shot), fly(shot, ghost=True)
    made_at = next((c for c in _down_crossings(real, shot.rim[2])
                    if np.hypot(*(c[:2] - shot.rim[:2])) < shot.inner_radius), None)
    out = {
        "made": made_at is not None,
        "rim_center": shot.rim.round(4).tolist(), "inner_radius": round(shot.inner_radius, 4),
        "launch_speed": round(float(np.linalg.norm(qvel[:3])), 4),
        "launch_elevation_deg": round(math.degrees(math.atan2(qvel[2], math.hypot(qvel[0], qvel[1]))), 3),
        "launch_azimuth_deg": round(math.degrees(math.atan2(qvel[1], qvel[0])), 3),
        "apex_z": round(float(real.pos[:, 2].max()), 4),
        "landed_at_s": real.landed_at, "landed_xy": real.pos[-1, :2].round(3).tolist(),
        "touched": real.touched, "load_log": shot.loaded.log,
    }
    # The shot's line: horizontal, from the ball's start toward the rim center.
    start = real.pos[0]
    u = shot.rim[:2] - start[:2]
    u = u / np.linalg.norm(u)
    left = np.array([-u[1], u[0]])
    crossing = next(iter(_down_crossings(ghost, shot.rim[2])), None)
    if crossing is None:
        out.update(along=None, across=None, direction="short", direction_basis="never reached rim height",
                   ghost_apex_z=round(float(ghost.pos[:, 2].max()), 4))
    else:
        off = crossing[:2] - shot.rim[:2]
        along, across = float(off @ u), float(off @ left)
        if abs(along) >= abs(across):
            direction = "long" if along > 0 else "short"
        else:
            direction = "left" if across > 0 else "right"
        out.update(along=round(along, 4), across=round(across, 4), direction=direction,
                   direction_basis="ghost path crossing the rim plane",
                   ghost_off_center=round(float(np.hypot(along, across)), 4))
    out["outcome"] = "made" if out["made"] else out["direction"]
    out["_real"], out["_ghost"] = real, ghost  # for drawing; stripped before logging
    return out


def public(j: dict) -> dict:
    return {k: v for k, v in j.items() if not k.startswith("_")}


def clear_cut(j: dict, miss: str) -> bool:
    """A deliberate miss is clear-cut when it misses, its path misses the rim's opening, and the direction
    is the one we meant."""
    if miss == "none":
        return j["made"]
    return (not j["made"]) and j["direction"] == miss and (j.get("ghost_off_center") or 9.9) > j["inner_radius"]


def clean_make(j: dict) -> bool:
    """Made, and by its own path: the ghost crosses the rim plane inside the opening (not a bank shot)."""
    return j["made"] and j.get("ghost_off_center") is not None and j["ghost_off_center"] < j["inner_radius"]


def tune_speed(xml: str, lo: float = 0.7, hi: float = 1.4, step: float = 0.002) -> tuple[float | None, list]:
    """Scale the launch speed, same direction, to the middle of the widest run of clean makes."""
    qvel = shot_qvel(xml)
    factors = np.round(np.arange(lo, hi + step / 2, step), 4)
    made = []
    for f in factors:
        trial, _ = set_qvel(xml, scaled(qvel, f))
        made.append(clean_make(judge(trial)))
    runs, start = [], None
    for f, ok in zip(list(factors) + [None], made + [False]):
        if ok and start is None:
            start = f
        if not ok and start is not None:
            runs.append((start, prev))
            start = None
        prev = f
    if not runs:
        return None, []
    best = max(runs, key=lambda r: r[1] - r[0])
    return round((best[0] + best[1]) / 2, 4), [(float(a), float(b)) for a, b in runs]
