"""Load a scene, measure it, and break it on purpose.

Measurements are always read from MuJoCo state after mj_forward at t=0, never from the text and never by eye.
Errors are one-line text edits, so the model sees exactly one changed line.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import mujoco
import numpy as np

from config import TARGETS, TIMESTEP, TOLERANCE

# The authoring prompt asks for these names; see scene/author_prompt.md.
BALL = "ball"
HOOP = "hoop"
RIM_PREFIX = "rim"


@dataclass
class Loaded:
    model: mujoco.MjModel
    data: mujoco.MjData
    log: list[str] = field(default_factory=list)  # every adjustment made on load, so it shows its origin


def load(xml_text: str) -> Loaded:
    model = mujoco.MjModel.from_xml_string(xml_text)
    log = []
    if model.opt.timestep != TIMESTEP:
        log.append(f"timestep {model.opt.timestep} overridden to {TIMESTEP}")
        model.opt.timestep = TIMESTEP
    data = mujoco.MjData(model)
    mujoco.mj_forward(model, data)
    return Loaded(model, data, log)


def _geom_names(model: mujoco.MjModel) -> list[str]:
    return [model.geom(i).name for i in range(model.ngeom)]


def rim_center(s: Loaded) -> np.ndarray:
    """Mean world position of the rim geoms; falls back to the hoop body origin if none are named rim*."""
    names = _geom_names(s.model)
    ids = [i for i, n in enumerate(names) if n.startswith(RIM_PREFIX)]
    if ids:
        return s.data.geom_xpos[ids].mean(axis=0)
    s.log.append("no rim* geoms; hoop height read from the hoop body origin")
    return s.data.body(HOOP).xpos.copy()


def ball_geom_id(s: Loaded) -> int:
    names = _geom_names(s.model)
    if BALL in names:
        return names.index(BALL)
    body = s.model.body(BALL).id
    spheres = [i for i in range(s.model.ngeom)
               if s.model.geom_bodyid[i] == body and s.model.geom_type[i] == mujoco.mjtGeom.mjGEOM_SPHERE]
    if not spheres:
        raise ValueError("no sphere geom on the ball body")
    s.log.append("ball geom found by body, not by name")
    return spheres[0]


def measure(s: Loaded) -> dict:
    rim = rim_center(s)
    ball = s.data.body(BALL).xpos
    return {
        "hoop_height": float(rim[2]),
        "ball_hoop_distance": float(np.hypot(*(rim[:2] - ball[:2]))),
        "ball_radius": float(s.model.geom_size[ball_geom_id(s)][0]),
        "rim_center": rim.round(4).tolist(),
        "ball_xpos": ball.round(4).tolist(),
    }


def within(measurement: dict, key: str) -> bool:
    return abs(measurement[key] - TARGETS[key]) / TARGETS[key] <= TOLERANCE


def trajectory(s: Loaded, seconds: float = 2.0, every: float = 0.05) -> list[dict]:
    """Step the scene and record the ball's position. Leaves s.data at the end state."""
    out = []
    stride = round(every / s.model.opt.timestep)
    for step in range(round(seconds / s.model.opt.timestep) + 1):
        if step % stride == 0:
            out.append({"t": round(s.data.time, 4), "ball": s.data.body(BALL).xpos.round(4).tolist()})
        mujoco.mj_step(s.model, s.data)
    return out


# ---- deliberate errors (handoff, Measurement matrix) ----------------------------------------------

@dataclass
class Error:
    key: str
    label: str
    target_object: str  # what the model should name
    measured: str  # which measurement decides "fixed"


ERRORS = {
    "hoop_low": Error("hoop_low", "Hoop too low", HOOP, "hoop_height"),
    "ball_displaced": Error("ball_displaced", "Ball displaced", BALL, "ball_hoop_distance"),
    "ball_size": Error("ball_size", "Ball wrong size", BALL, "ball_radius"),
}
NONE = Error("none", "Unmodified", "none", "")


def _tag(xml: str, element: str, name: str) -> re.Match:
    m = re.search(rf'<{element}\b[^>]*\bname="{name}"[^>]*>', xml)
    if not m:
        raise ValueError(f'no <{element} name="{name}"> in scene text')
    if "\n" in m.group(0):
        raise ValueError(f'<{element} name="{name}"> spans lines; the edit would not be one line')
    return m


def _set_attr(tag: str, attr: str, value: str) -> str:
    if re.search(rf'\b{attr}="[^"]*"', tag):
        return re.sub(rf'\b{attr}="[^"]*"', f'{attr}="{value}"', tag, count=1)
    return tag.replace(">", f' {attr}="{value}">', 1) if not tag.endswith("/>") else tag[:-2] + f' {attr}="{value}"/>'


def _vec(tag: str, attr: str, default: str) -> list[float]:
    m = re.search(rf'\b{attr}="([^"]*)"', tag)
    return [float(v) for v in (m.group(1) if m else default).split()]


def _fmt(values: list[float]) -> str:
    return " ".join(f"{v:.4g}" for v in values)


def inject(xml: str, error_key: str) -> tuple[str, dict]:
    """Apply one deliberate error as a one-line edit. Returns the new text and a record of the edit."""
    if error_key == "none":
        return xml, {"error": "none"}
    if error_key == "hoop_low":
        m = _tag(xml, "body", HOOP)
        pos = _vec(m.group(0), "pos", "0 0 0")
        pos[2] -= 0.50  # 3.05 -> 2.55 when the hoop body is at world z 3.05
        new_tag = _set_attr(m.group(0), "pos", _fmt(pos))
    elif error_key == "ball_displaced":
        m = _tag(xml, "body", BALL)
        pos = _vec(m.group(0), "pos", "0 0 0")
        pos[0] += 1.50  # x, toward the hoop: 4.0 m becomes 2.5 m
        new_tag = _set_attr(m.group(0), "pos", _fmt(pos))
    elif error_key == "ball_size":
        m = _tag(xml, "geom", BALL)
        size = _vec(m.group(0), "size", "0")
        size[0] = 0.30
        new_tag = _set_attr(m.group(0), "size", _fmt(size))
    else:
        raise KeyError(error_key)
    new_xml = xml[: m.start()] + new_tag + xml[m.end():]
    line_no = xml.count("\n", 0, m.start()) + 1
    before = xml.splitlines()[line_no - 1]
    after = new_xml.splitlines()[line_no - 1]
    assert sum(a != b for a, b in zip(xml.splitlines(), new_xml.splitlines())) == 1
    return new_xml, {"error": error_key, "line": line_no, "before": before.strip(), "after": after.strip()}
