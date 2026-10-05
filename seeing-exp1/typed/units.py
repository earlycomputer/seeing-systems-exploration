"""Quantities with their units in the type. A bare number is never a length, an angle or a mass.

Every quantity stores SI (angles in radians) and remembers how it was written, so a problem can quote it back.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Quantity:
    si: float  # metres, radians, kilograms, m/s, rad/s, N·m/rad, N·m·s/rad, kg/m³
    written: str  # as the author wrote it, e.g. "deg(120)"

    kind = "quantity"

    def __repr__(self) -> str:
        return self.written


class Length(Quantity):
    kind = "length"


class Angle(Quantity):
    kind = "angle"

    @property
    def deg(self) -> float:
        return math.degrees(self.si)


class Mass(Quantity):
    kind = "mass"


class Speed(Quantity):
    kind = "speed"


class Spin(Quantity):
    kind = "spin"


class TorsionStiffness(Quantity):
    kind = "torsional stiffness"


class TorsionDamping(Quantity):
    kind = "torsional damping"


class Density(Quantity):
    kind = "density"


def m(x: float) -> Length: return Length(float(x), f"m({x})")
def cm(x: float) -> Length: return Length(float(x) / 100, f"cm({x})")
def deg(x: float) -> Angle: return Angle(math.radians(x), f"deg({x})")
def rad(x: float) -> Angle: return Angle(float(x), f"rad({x})")
def kg(x: float) -> Mass: return Mass(float(x), f"kg({x})")
def g(x: float) -> Mass: return Mass(float(x) / 1000, f"g({x})")
def mps(x: float) -> Speed: return Speed(float(x), f"mps({x})")
def rps(x: float) -> Spin: return Spin(float(x), f"rps({x})")  # radians per second
def Nm_per_rad(x: float) -> TorsionStiffness: return TorsionStiffness(float(x), f"Nm_per_rad({x})")
def Nms_per_rad(x: float) -> TorsionDamping: return TorsionDamping(float(x), f"Nms_per_rad({x})")
def kg_per_m3(x: float) -> Density: return Density(float(x), f"kg_per_m3({x})")


@dataclass(frozen=True)
class Vec:
    """A point or offset in metres: x along the floor, z up. Written m3(x, y, z)."""
    x: Length
    y: Length
    z: Length

    def __repr__(self) -> str:
        return f"m3({self.x.si:g}, {self.y.si:g}, {self.z.si:g})"

    @property
    def si(self) -> tuple[float, float, float]:
        return (self.x.si, self.y.si, self.z.si)

    def __add__(self, o: "Vec") -> "Vec":
        return m3(*(a + b for a, b in zip(self.si, o.si)))


def m3(x: float, y: float, z: float) -> Vec:
    return Vec(m(x), m(y), m(z))


@dataclass(frozen=True)
class Velocity:
    """A velocity in m/s, written v3(mps(x), mps(y), mps(z))."""
    x: Speed
    y: Speed
    z: Speed

    @property
    def si(self) -> tuple[float, float, float]:
        return (self.x.si, self.y.si, self.z.si)


def v3(x: Speed, y: Speed, z: Speed) -> Velocity:
    return Velocity(x, y, z)


AXES = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}
