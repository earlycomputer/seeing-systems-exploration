"""Check a world, then compile it to MuJoCo XML. Like Elm's compiler: every problem at once, each one saying what
was found, where, why it matters, and what to write instead; and no XML at all until there are none.

    result = compile_world(world)
    if result.problems: print(render(result.problems))      # for people
    else: result.xml                                          # for MuJoCo
    [p.as_dict() for p in result.problems]                    # for agents: the same, as data
"""

from __future__ import annotations

import dataclasses
import types
import typing
from dataclasses import dataclass, field

import mujoco

from typed import parts as P
from typed.units import Quantity, Vec, Velocity

TIMESTEP = 0.002
OVERLAP = 0.002  # m: parts that start more than this far inside each other are a problem


@dataclass
class Problem:
    code: str  # e.g. "ANGLE WITHOUT A UNIT"
    path: str  # e.g. "Door.hinge.range[1]"
    found: str
    expected: str
    why: str
    hint: str

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)

    def render(self) -> str:
        bar = "-" * max(4, 72 - len(self.code) - len(self.path) - 4)
        return (f"-- {self.code} {bar} {self.path}\n\n"
                f"I was expecting {self.expected}, but I found:\n\n    {self.found}\n\n"
                + (f"{self.why}\n\n" if self.why else "") + (f"Hint: {self.hint}\n" if self.hint else ""))


@dataclass
class Compiled:
    world: P.World
    xml: str | None = None
    problems: list[Problem] = field(default_factory=list)
    owner: dict[str, str] = field(default_factory=dict)  # MuJoCo name -> "Part.piece"
    joints: list[dict] = field(default_factory=list)
    containers: list[tuple[str, tuple[float, float, float, float]]] = field(default_factory=list)  # name, x0 x1 y0 y1
    rings: list[tuple[str, tuple[float, float, float], float]] = field(default_factory=list)  # name, centre, inner r


def render(problems: list[Problem]) -> str:
    n = len(problems)
    head = f"{n} problem{'s' if n != 1 else ''} in this world. Nothing was built.\n\n"
    return head + "\n".join(p.render() for p in problems)


# ---- types --------------------------------------------------------------------------------------------

SPELLING = {"length": "m(0.4) or cm(40)", "angle": "deg(120) or rad(2.09)", "mass": "kg(0.5) or g(50)",
            "speed": "mps(3.0)", "spin": "rps(4.0) (radians per second)",
            "torsional stiffness": "Nm_per_rad(40)", "torsional damping": "Nms_per_rad(25)",
            "density": "kg_per_m3(1.2)"}

WHY_ANGLE = ("A bare number can't say whether it is degrees or radians. MuJoCo reads joint ranges in degrees "
             "but keyframe angles in radians, so 2.1 meant as radians becomes a 2.1 degree limit, and a door "
             "opened to 69 degrees starts outside it and snaps shut.")


def _describe(t) -> str:
    if isinstance(t, type) and issubclass(t, Quantity):
        return f"{'an' if t.kind[0] in 'aeiou' else 'a'} {t.kind}, like {SPELLING[t.kind]}"
    if t is Vec:
        return "a point in metres, like m3(0, 0, 1.0)"
    if t is Velocity:
        return "a velocity, like v3(mps(3.0), mps(0), mps(9.0))"
    return getattr(t, "__name__", str(t))


def _check(value, t, path: str, out: list[Problem]) -> None:
    origin = typing.get_origin(t)
    if origin in (typing.Union, types.UnionType):
        options = typing.get_args(t)
        if value is None and type(None) in options:
            return
        t = next(o for o in options if o is not type(None))
        origin = typing.get_origin(t)
    if origin is tuple:
        args = typing.get_args(t)
        if not isinstance(value, tuple) or len(value) != len(args):
            out.append(Problem("WRONG SHAPE", path, repr(value), f"{len(args)} values in a tuple",
                               "This field takes a fixed number of values.", f"write ({', '.join(_describe(a) for a in args)})"))
            return
        for i, (v, a) in enumerate(zip(value, args)):
            _check(v, a, f"{path}[{i}]", out)
        return
    if isinstance(t, type) and issubclass(t, Quantity):
        if isinstance(value, t):
            return
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            code = "ANGLE WITHOUT A UNIT" if t.kind == "angle" else f"{t.kind.upper()} WITHOUT A UNIT"
            why = WHY_ANGLE if t.kind == "angle" else f"A bare number has no unit, so nothing can check it is a {t.kind}."
            out.append(Problem(code, path, repr(value), _describe(t), why, f"write {SPELLING[t.kind]}"))
        elif isinstance(value, Quantity):
            out.append(Problem("WRONG KIND OF QUANTITY", path, repr(value), _describe(t),
                               f"This is a {value.kind}, and this field needs {_describe(t).split(',')[0]}.", f"write {SPELLING[t.kind]}"))
        else:
            out.append(Problem("WRONG TYPE", path, repr(value), _describe(t), "", f"write {SPELLING[t.kind]}"))
        return
    if t in (Vec, Velocity):
        if not isinstance(value, t):
            out.append(Problem("WRONG TYPE", path, repr(value), _describe(t),
                               "Points and velocities carry their units, so a plain tuple is not enough.",
                               "write " + ("m3(x, y, z)" if t is Vec else "v3(mps(x), mps(y), mps(z))")))
        return
    if dataclasses.is_dataclass(t):
        if not isinstance(value, t):
            out.append(Problem("WRONG TYPE", path, repr(value), f"a {t.__name__}", "", f"write {t.__name__}(...)"))
            return
        check_fields(value, path, out)
        return
    if t in (int, float, str, bool):
        if not isinstance(value, t) and not (t is float and isinstance(value, int)):
            out.append(Problem("WRONG TYPE", path, repr(value), f"a {t.__name__}", "", f"write a {t.__name__}"))


def check_fields(obj, path: str, out: list[Problem]) -> None:
    hints = typing.get_type_hints(type(obj), vars(P))
    for fld in dataclasses.fields(obj):
        if fld.name == "parts":
            continue
        _check(getattr(obj, fld.name), hints[fld.name], f"{path}.{fld.name}", out)


# ---- meaning ------------------------------------------------------------------------------------------

def check_meaning(c: Compiled) -> None:
    for j in c.joints:
        r, s = j.get("range"), j.get("start")
        if r and s is not None and not (r[0].si - 1e-9 <= s.si <= r[1].si + 1e-9):
            c.problems.append(Problem(
                "STARTS OUTSIDE ITS OWN RANGE", j["part"], f"starts at {s!r}, range ({r[0]!r}, {r[1]!r})",
                f"a starting angle between {r[0].deg:g} and {r[1].deg:g} degrees",
                "MuJoCo would push it back inside its limit in the first few steps: whatever it was meant to do "
                "from there, it would not.",
                "widen the range or change where it starts"))


def check_overlaps(c: Compiled) -> None:
    model = mujoco.MjModel.from_xml_string(c.xml)
    data = mujoco.MjData(model)
    key = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_KEY, "start")
    if key >= 0:
        mujoco.mj_resetDataKeyframe(model, data, key)
    mujoco.mj_forward(model, data)
    seen = set()
    for con in data.contact[: data.ncon]:
        if con.dist >= -OVERLAP:
            continue
        a, b = (c.owner.get(model.geom(g).name, model.geom(g).name) for g in (con.geom1, con.geom2))
        pair = tuple(sorted((a, b)))
        if pair in seen:
            continue
        seen.add(pair)
        c.problems.append(Problem(
            "PARTS START INSIDE EACH OTHER", f"{pair[0]} / {pair[1]}", f"{-con.dist * 1000:.0f} mm of overlap at t = 0",
            "parts that at most touch when the world starts",
            "MuJoCo pushes overlapping parts apart in the first steps, so the world starts with a kick nobody wrote.",
            "move one of them, or check the sizes"))


# ---- build --------------------------------------------------------------------------------------------

def compile_world(world: P.World) -> Compiled:
    c = Compiled(world)
    for i, part in enumerate(world.parts):
        if not dataclasses.is_dataclass(part):
            c.problems.append(Problem("NOT A PART", f"World.parts[{i}]", repr(part), "a part such as Ball(...)", "", ""))
            continue
        check_fields(part, type(part).__name__, c.problems)
    if world.air is not None:
        check_fields(world.air, "World.air", c.problems)
    if c.problems:
        return c  # types first: no point reasoning about a world whose numbers have no units

    e = P.Emit()
    for part in world.parts:
        part.emit(e)
    c.owner, c.joints = e.owner, e.joints
    c.containers = [(p.name.capitalize(), p.footprint()) for p in world.parts if isinstance(p, P.OpenBox)]
    c.rings = [("Hoop", p.rim_centre.si, p.inner_diameter.si / 2) for p in world.parts if isinstance(p, P.Hoop)]
    check_meaning(c)
    if c.problems:
        return c

    opt = f'  <option timestep="{TIMESTEP}"' + (f' density="{world.air.density.si:g}"' if world.air else "") + "/>"
    qpos = " ".join(f"{v:.6g}" for j in e.joints for v in j["qpos"])
    qvel = " ".join(f"{v:.6g}" for j in e.joints for v in j["qvel"])
    c.xml = "\n".join([f'<mujoco model="{world.name}">', '  <compiler angle="radian"/>', opt, "  <worldbody>",
                       *e.xml, "  </worldbody>",
                       *(["  <keyframe>", f'    <key name="start" qpos="{qpos}" qvel="{qvel}"/>', "  </keyframe>"] if e.joints else []),
                       "</mujoco>", ""])
    check_overlaps(c)
    if c.problems:
        c.xml = None
    return c
