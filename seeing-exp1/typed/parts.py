"""The parts a world is built from. Each says how it is built, with typed fields, and emits its own MuJoCo XML.

A part owns the names the tests need (`ball`, `hinge`, `catapult_*`...), so a world written from parts can never
miss one. Angles reach MuJoCo in radians only: the compiler sets `<compiler angle="radian"/>`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

from typed.units import (AXES, Angle, Density, Length, Mass, Spin, Speed, TorsionDamping, TorsionStiffness, Vec,
                         Velocity, m, m3)


def f(*xs) -> str:
    return " ".join(f"{x:.6g}" for x in xs)


class Emit:
    """What a part writes: worldbody XML, joints in file order (for the keyframe), and which part owns each name."""

    def __init__(self):
        self.xml: list[str] = []
        self.joints: list[dict] = []  # {name, kind: free|hinge, qpos: [...], qvel: [...], part, range}
        self.owner: dict[str, str] = {}  # geom or body name -> "Part.piece"

    def geom(self, owner: str, name: str, indent: int = 3, **attrs) -> None:
        self.owner[name] = owner
        self.xml.append("  " * indent + f'<geom name="{name}" ' + " ".join(f'{k}="{v}"' for k, v in attrs.items()) + "/>")


@dataclass(frozen=True)
class Air:
    density: Density


@dataclass(frozen=True)
class Friction:
    """Dimensionless coefficients: sliding, torsional, rolling."""
    slide: float
    torsion: float = 0.005
    roll: float = 0.0001

    def __str__(self) -> str:
        return f(self.slide, self.torsion, self.roll)


@dataclass(frozen=True)
class Hinge:
    """A hinge: which way it turns, how far, and the spring and damping on it. Angles are typed, never bare."""
    axis: str  # "x", "y" or "z"
    range: tuple[Angle, Angle] | None = None
    stiffness: TorsionStiffness | None = None
    rest: Angle | None = None  # where the spring pulls toward
    damping: TorsionDamping | None = None

    def attrs(self) -> dict:
        a = {"type": "hinge", "axis": f(*AXES[self.axis])}
        if self.range:
            a.update(limited="true", range=f(self.range[0].si, self.range[1].si))
        if self.stiffness:
            a["stiffness"] = f(self.stiffness.si)
        if self.rest:
            a["springref"] = f(self.rest.si)
        if self.damping:
            a["damping"] = f(self.damping.si)
        return a


@dataclass(frozen=True)
class Floor:
    friction: Friction | None = None
    size: Length = m(8)

    def emit(self, e: Emit) -> None:
        a = {"type": "plane", "size": f(self.size.si, self.size.si, 0.1)}
        if self.friction:
            a["friction"] = str(self.friction)
        e.geom("Floor", "floor", indent=2, **a)


@dataclass(frozen=True)
class Ball:
    radius: Length
    mass: Mass
    at: Vec  # centre
    launch: Velocity | None = None
    friction: Friction | None = None
    rolls: bool = False  # rolling friction on (condim 6)
    bounce: str | None = None  # "lively" or "dead"
    hollow: bool = False  # a shell, like a basketball
    drag: bool = False  # feels the air (World.air)
    name: str = "ball"

    def emit(self, e: Emit) -> None:
        e.owner[self.name] = "Ball"
        e.xml.append(f'    <body name="{self.name}" pos="{f(*self.at.si)}">')
        e.xml.append("      <freejoint/>")
        r, mass = self.radius.si, self.mass.si
        a = {"type": "sphere", "size": f(r)}
        if self.hollow:
            i = 2 / 3 * mass * r * r
            e.xml.append(f'      <inertial pos="0 0 0" mass="{f(mass)}" diaginertia="{f(i, i, i)}"/>')
        else:
            a["mass"] = f(mass)
        if self.rolls:
            a["condim"] = "6"
        if self.friction:
            a["friction"] = str(self.friction)
        if self.bounce:
            a["solref"] = {"lively": "0.01 0.2", "dead": "0.01 1"}[self.bounce]
        if self.drag:
            a.update(fluidshape="ellipsoid", fluidcoef="0.25 0.25 1.5 1.0 1.0")
        e.geom("Ball", self.name, indent=3, **a)
        e.xml.append("    </body>")
        v = self.launch.si if self.launch else (0, 0, 0)
        e.joints.append({"name": f"{self.name} (free)", "kind": "free", "part": "Ball",
                         "qpos": [*self.at.si, 1, 0, 0, 0], "qvel": [*v, 0, 0, 0]})


@dataclass(frozen=True)
class Hoop:
    """A regulation-style hoop: a rim of 16 short capsules, a bracket, a backboard and a support behind it."""
    rim_centre: Vec
    inner_diameter: Length = m(0.4572)
    tube: Length = m(0.008)

    def emit(self, e: Emit) -> None:
        cx, cy, cz = self.rim_centre.si
        e.owner["hoop"] = "Hoop"
        e.xml.append(f'    <body name="hoop" pos="{f(cx, cy, cz)}">')
        t = self.tube.si
        R = self.inner_diameter.si / 2 + t
        pts = [(R * math.cos(k * math.pi / 8), R * math.sin(k * math.pi / 8)) for k in range(17)]
        orange = "0.9 0.3 0.05 1"
        for k in range(16):
            (x0, y0), (x1, y1) = pts[k], pts[k + 1]
            e.geom("Hoop.rim", f"rim_{k:02d}", type="capsule", size=f(t), fromto=f(x0, y0, 0, x1, y1, 0), rgba=orange)
        e.geom("Hoop.bracket", "hoop_bracket", type="box", pos=f(0.3105, 0, -0.01), size=f(0.0705, 0.05, 0.012), rgba=orange)
        e.geom("Hoop.backboard", "backboard", type="box", pos=f(0.396, 0, 0.375), size=f(0.015, 0.9, 0.525),
               rgba="0.92 0.95 0.98 0.85")
        e.geom("Hoop.backboard", "backboard_square", type="box", pos=f(0.3805, 0, 0.145), size=f(0.0005, 0.295, 0.225),
               rgba="0.1 0.1 0.1 1", contype="0", conaffinity="0")
        e.xml.append("    </body>")
        top = cz + 0.35
        e.owner["hoop_support"] = "Hoop.support"
        e.xml.append(f'    <body name="hoop_support" pos="{f(cx + 1.2, cy, 0)}">')
        grey = "0.25 0.25 0.3 1"
        e.geom("Hoop.support", "support_base", type="box", pos=f(0, 0, 0.025), size=f(0.4, 0.4, 0.025), rgba="0.2 0.2 0.25 1")
        e.geom("Hoop.support", "support_pole", type="box", pos=f(0, 0, top / 2), size=f(0.1, 0.1, top / 2), rgba=grey)
        e.geom("Hoop.support", "support_arm", type="box", pos=f(-0.4445, 0, cz + 0.25), size=f(0.3445, 0.06, 0.06), rgba=grey)
        e.xml.append("    </body>")


@dataclass(frozen=True)
class Ramp:
    """A straight ramp, given by the centre line of its deck from the high end to the low end."""
    high: Vec
    low: Vec
    width: Length
    thickness: Length = m(0.04)
    leg: bool = True  # a post holding up the high end

    @property
    def pitch(self) -> float:
        (x0, _, z0), (x1, _, z1) = self.high.si, self.low.si
        return math.atan2(z0 - z1, x1 - x0)

    def seat(self, radius: Length, along: Length) -> Vec:
        """Where a ball of this radius rests on the deck, this far down from the high end."""
        th = self.pitch
        x0, y0, z0 = self.high.si
        s, up = along.si, self.thickness.si / 2 + radius.si
        return m3(x0 + s * math.cos(th) + up * math.sin(th), y0, z0 - s * math.sin(th) + up * math.cos(th))

    def emit(self, e: Emit) -> None:
        (x0, y0, z0), (x1, y1, z1) = self.high.si, self.low.si
        half = math.hypot(x1 - x0, z1 - z0) / 2
        e.geom("Ramp.deck", "ramp_deck", indent=2, type="box", pos=f((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2),
               euler=f(0, self.pitch, 0), size=f(half, self.width.si / 2, self.thickness.si / 2))
        if self.leg:
            h = z0 / 2
            e.geom("Ramp.leg", "ramp_leg", indent=2, type="box", pos=f(x0, y0, h), size=f(0.03, 0.03, h))


@dataclass(frozen=True)
class OpenBox:
    """A cup or bucket: a base and four walls, standing on the floor. `at` is the centre of its base on the floor.
    `near` is the wall facing back along x; a `lip` makes it low enough to roll over."""
    name: str
    at: Vec
    length: Length  # outer, along x
    width: Length  # outer, along y
    wall_height: Length
    wall: Length = m(0.02)
    base: Length = m(0.02)
    lip: Length | None = None  # height of a low near wall

    def footprint(self) -> tuple[float, float, float, float]:
        x, y, _ = self.at.si
        hx, hy = self.length.si / 2, self.width.si / 2
        return x - hx, x + hx, y - hy, y + hy

    def emit(self, e: Emit) -> None:
        n, P = self.name, self.name.capitalize()
        hx, hy, hz = self.length.si / 2, self.width.si / 2, self.wall_height.si / 2
        w, b = self.wall.si / 2, self.base.si / 2
        e.owner[n] = P
        e.xml.append(f'    <body name="{n}" pos="{f(*self.at.si)}">')
        e.geom(f"{P}.base", f"{n}_base", type="box", pos=f(0, 0, b), size=f(hx, hy, b))
        if self.lip:
            lz = self.lip.si / 2
            e.geom(f"{P}.lip", f"{n}_lip", type="box", pos=f(-hx, 0, lz), size=f(w, hy, lz))
        else:
            e.geom(f"{P}.near wall", f"{n}_near", type="box", pos=f(-hx, 0, hz), size=f(w, hy, hz))
        e.geom(f"{P}.far wall", f"{n}_far", type="box", pos=f(hx, 0, hz), size=f(w, hy, hz))
        e.geom(f"{P}.side wall", f"{n}_left", type="box", pos=f(0, hy, hz), size=f(hx, w, hz))
        e.geom(f"{P}.side wall", f"{n}_right", type="box", pos=f(0, -hy, hz), size=f(hx, w, hz))
        e.xml.append("    </body>")


@dataclass(frozen=True)
class Door:
    """A door on a hinge along its edge, with a post for its frame. `hinge_at` is the hinge line at the floor."""
    hinge_at: Vec
    width: Length
    height: Length
    thickness: Length
    mass: Mass
    hinge: Hinge
    opened: Angle  # where it starts
    clearance: Length = m(0.02)
    frame: bool = True

    def emit(self, e: Emit) -> None:
        x, y, _ = self.hinge_at.si
        zc = self.clearance.si + self.height.si / 2
        if self.frame:
            ph = (self.height.si + 0.14) / 2
            e.geom("Door.frame", "frame_post", indent=2, type="box", pos=f(x, y - 0.12, ph), size=f(0.04, 0.04, ph))
        e.owner["door"] = "Door"
        e.xml.append(f'    <body name="door" pos="{f(x, y, zc)}">')
        a = " ".join(f'{k}="{v}"' for k, v in self.hinge.attrs().items())
        e.xml.append(f'      <joint name="hinge" pos="0 0 0" {a}/>')
        e.geom("Door.panel", "door_panel", type="box", pos=f(0, self.width.si / 2, 0),
               size=f(self.thickness.si / 2, self.width.si / 2, self.height.si / 2), mass=f(self.mass.si))
        e.xml.append("    </body>")
        e.joints.append({"name": "hinge", "kind": "hinge", "part": "Door.hinge", "qpos": [self.opened.si], "qvel": [0],
                         "range": self.hinge.range, "start": self.opened})


@dataclass(frozen=True)
class Catapult:
    """A spring-loaded arm on a pivot. The arm points back along -x from the pivot with a cup at its end; the
    spring pulls toward `spring.rest` and the arm is free to swing through `hinge.range`."""
    pivot_at: Vec
    arm_length: Length
    hinge: Hinge
    arm_mass: Mass
    armature: float = 0.01  # rotor inertia, kg·m², MuJoCo's own knob for a stiff spring

    def seat(self, radius: Length) -> Vec:
        """Where a ball of this radius sits in the cup (settled 0.5 mm into contact)."""
        x, y, z = self.pivot_at.si
        return m3(x - (self.arm_length.si - 0.08), y, z + 0.03 + radius.si - 0.0005)

    def emit(self, e: Emit) -> None:
        x, y, z = self.pivot_at.si
        L = self.arm_length.si
        bh = (z - 0.06) / 2
        e.geom("Catapult.base", "catapult_base", indent=2, type="box", pos=f(x, y, bh), size=f(0.08, 0.12, bh))
        e.owner["catapult_arm"] = "Catapult.arm"
        e.xml.append(f'    <body name="catapult_arm" pos="{f(x, y, z)}">')
        a = " ".join(f'{k}="{v}"' for k, v in self.hinge.attrs().items())
        e.xml.append(f'      <joint name="catapult_hinge" {a} armature="{f(self.armature)}"/>')
        e.geom("Catapult.arm", "catapult_beam", type="box", pos=f(-L / 2, 0, 0), size=f(L / 2, 0.03, 0.02), mass=f(self.arm_mass.si))
        e.geom("Catapult.cup", "catapult_cup_floor", type="box", pos=f(-(L - 0.08), 0, 0.025), size=f(0.08, 0.08, 0.005), mass="0.02")
        e.geom("Catapult.cup", "catapult_cup_back", type="box", pos=f(-(L + 0.005), 0, 0.07), size=f(0.005, 0.08, 0.05), mass="0.01")
        e.xml.append("    </body>")
        e.joints.append({"name": "catapult_hinge", "kind": "hinge", "part": "Catapult.hinge", "qpos": [0], "qvel": [0],
                         "range": self.hinge.range, "start": None})


@dataclass(frozen=True)
class Stack:
    """Equal cubes stacked straight up from `at` on the floor, named block1 (bottom) upward."""
    at: Vec
    count: int
    side: Length
    mass: Mass
    friction: Friction | None = None

    def emit(self, e: Emit) -> None:
        x, y, _ = self.at.si
        s = self.side.si
        for i in range(1, self.count + 1):
            z = s * (i - 0.5)
            e.owner[f"block{i}"] = f"Stack.block{i}"
            e.xml.append(f'    <body name="block{i}" pos="{f(x, y, z)}">')
            e.xml.append("      <freejoint/>")
            a = {"type": "box", "size": f(s / 2, s / 2, s / 2), "mass": f(self.mass.si)}
            if self.friction:
                a["friction"] = str(self.friction)
            e.geom(f"Stack.block{i}", f"block{i}", **a)
            e.xml.append("    </body>")
            e.joints.append({"name": f"block{i} (free)", "kind": "free", "part": f"Stack.block{i}",
                             "qpos": [x, y, z, 1, 0, 0, 0], "qvel": [0] * 6})


@dataclass(frozen=True)
class Pusher:
    """A heavy ball sent rolling at something."""
    at: Vec
    radius: Length
    mass: Mass
    velocity: Velocity
    friction: Friction | None = None

    def emit(self, e: Emit) -> None:
        e.owner["pusher"] = "Pusher"
        e.xml.append(f'    <body name="pusher" pos="{f(*self.at.si)}">')
        e.xml.append("      <freejoint/>")
        a = {"type": "sphere", "size": f(self.radius.si), "mass": f(self.mass.si)}
        if self.friction:
            a["friction"] = str(self.friction)
        e.geom("Pusher", "pusher", **a)
        e.xml.append("    </body>")
        e.joints.append({"name": "pusher (free)", "kind": "free", "part": "Pusher",
                         "qpos": [*self.at.si, 1, 0, 0, 0], "qvel": [*self.velocity.si, 0, 0, 0]})


@dataclass(frozen=True)
class DominoRow:
    """Upright dominoes in a row along x from `start` (a floor point), domino1 first. The first is tipped by
    giving it a spin about y."""
    start: Vec
    count: int
    spacing: Length
    thickness: Length
    width: Length
    height: Length
    mass: Mass
    first_tip: Spin

    def emit(self, e: Emit) -> None:
        x0, y, _ = self.start.si
        hz = self.height.si / 2
        for i in range(1, self.count + 1):
            x = x0 + (i - 1) * self.spacing.si
            e.owner[f"domino{i}"] = f"Dominoes.domino{i}"
            e.xml.append(f'    <body name="domino{i}" pos="{f(x, y, hz)}">')
            e.xml.append("      <freejoint/>")
            e.geom(f"Dominoes.domino{i}", f"domino{i}", type="box",
                   size=f(self.thickness.si / 2, self.width.si / 2, hz), mass=f(self.mass.si))
            e.xml.append("    </body>")
            spin = self.first_tip.si if i == 1 else 0
            e.joints.append({"name": f"domino{i} (free)", "kind": "free", "part": f"Dominoes.domino{i}",
                             "qpos": [x, y, hz, 1, 0, 0, 0], "qvel": [0, 0, 0, 0, spin, 0]})


@dataclass(frozen=True)
class Pendulum:
    """A rod and bob hanging from a pivot on a stand, released from an angle about its axis. Positive angles about y
    lift the bob back along -x."""
    pivot_at: Vec
    length: Length  # pivot to the bob's centre
    bob_radius: Length
    bob_mass: Mass
    rod_mass: Mass
    released_from: Angle
    damping: TorsionDamping | None = None
    rod_radius: Length = m(0.01)

    def emit(self, e: Emit) -> None:
        x, y, z = self.pivot_at.si
        top = z + self.rod_radius.si + 0.04  # the arm clears the rod's rounded end
        ph = top / 2
        e.geom("Pendulum.stand", "stand_post", indent=2, type="box", pos=f(x, y - 0.3, ph), size=f(0.03, 0.03, ph))
        e.geom("Pendulum.stand", "stand_arm", indent=2, type="box", pos=f(x, y - 0.15, top - 0.02), size=f(0.03, 0.15, 0.02))
        e.owner["pendulum"] = "Pendulum"
        e.xml.append(f'    <body name="pendulum" pos="{f(x, y, z)}">')
        h = Hinge("y", damping=self.damping)
        a = " ".join(f'{k}="{v}"' for k, v in h.attrs().items())
        e.xml.append(f'      <joint name="pivot" {a}/>')
        rod = self.length.si - self.bob_radius.si
        e.geom("Pendulum.rod", "pendulum_rod", type="capsule", fromto=f(0, 0, 0, 0, 0, -rod), size=f(self.rod_radius.si),
               mass=f(self.rod_mass.si))
        e.geom("Pendulum.bob", "pendulum_bob", type="sphere", pos=f(0, 0, -self.length.si), size=f(self.bob_radius.si),
               mass=f(self.bob_mass.si))
        e.xml.append("    </body>")
        e.joints.append({"name": "pivot", "kind": "hinge", "part": "Pendulum.pivot", "qpos": [self.released_from.si],
                         "qvel": [0], "range": None, "start": self.released_from})


@dataclass(frozen=True)
class World:
    parts: list = field(default_factory=list)
    air: Air | None = None
    name: str = "world"
