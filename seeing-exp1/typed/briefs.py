"""The seven 1d briefs, written in the typed vocabulary. Each is meant to be the hand-written fixture it replaces
(worlds/fixtures/*.xml, harder/fixtures/*.xml), said as parts instead of geoms."""

from __future__ import annotations

from typed.parts import (Air, Ball, Catapult, Door, DominoRow, Floor, Friction, Hinge, Hoop, OpenBox, Pendulum,
                         Pusher, Ramp, Stack, World)
from typed.units import Nm_per_rad, Nms_per_rad, deg, g, kg, kg_per_m3, m, m3, mps, rad, rps, v3


def shot() -> World:
    return World(name="shot", air=Air(density=kg_per_m3(1.2)), parts=[
        Floor(friction=Friction(0.8, 0.005, 0.0001), size=m(10)),
        Ball(radius=m(0.1194), mass=kg(0.62), at=m3(0, 0, 0.1194), hollow=True, drag=True, bounce="lively",
             friction=Friction(0.9, 0.01, 0.001), launch=v3(mps(3.21), mps(0), mps(9.3))),
        Hoop(rim_centre=m3(4, 0, 3.05)),
    ])


def cup() -> World:
    ramp = Ramp(high=m3(0, 0, 1.0), low=m3(1.6, 0, 0.45), width=m(0.4))
    return World(name="cup", parts=[
        Floor(friction=Friction(0.8, 0.005, 0.002), size=m(6)),
        ramp,
        Ball(radius=m(0.06), mass=kg(0.2), at=ramp.seat(m(0.06), along=m(0.12)), rolls=True, bounce="dead",
             friction=Friction(0.8, 0.01, 0.004)),
        OpenBox("cup", at=m3(2.05, 0, 0), length=m(0.9), width=m(0.6), wall_height=m(0.3)),
    ])


def door() -> World:
    return World(name="door", parts=[
        Floor(size=m(5)),
        Door(hinge_at=m3(0, 0, 0), width=m(0.9), height=m(1.96), thickness=m(0.04), mass=kg(20),
             hinge=Hinge("z", range=(deg(0), deg(120)), stiffness=Nm_per_rad(40), rest=deg(0), damping=Nms_per_rad(25)),
             opened=rad(1.2)),
    ])


def stack() -> World:
    grip = Friction(0.6, 0.005, 0.0001)
    return World(name="stack", parts=[
        Floor(friction=grip, size=m(6)),
        Stack(at=m3(0, 0, 0), count=5, side=m(0.2), mass=kg(0.5), friction=grip),
        Pusher(at=m3(-1.2, 0, 0.1), radius=m(0.1), mass=kg(4.0), velocity=v3(mps(3.0), mps(0), mps(0)),
               friction=Friction(0.3, 0.005, 0.0001)),
    ])


def catapult() -> World:
    arm = Catapult(pivot_at=m3(0, 0, 0.4), arm_length=m(1.0), arm_mass=kg(0.3),
                   hinge=Hinge("y", range=(deg(0), deg(55)), stiffness=Nm_per_rad(3.0), rest=deg(150),
                               damping=Nms_per_rad(0.05)))
    return World(name="catapult", parts=[
        Floor(),
        arm,
        Ball(radius=m(0.06), mass=kg(0.15), at=arm.seat(m(0.06)), rolls=True, bounce="dead",
             friction=Friction(0.8, 0.01, 0.004)),
        OpenBox("bucket", at=m3(2.0, 0, 0), length=m(0.8), width=m(0.8), wall_height=m(0.4)),
    ])


def dominoes() -> World:
    return World(name="dominoes", parts=[
        Floor(size=m(4)),
        DominoRow(start=m3(0, 0, 0), count=10, spacing=m(0.1), thickness=m(0.02), width=m(0.08), height=m(0.16),
                  mass=g(50), first_tip=rps(4)),
    ])


def pendulum() -> World:
    return World(name="pendulum", parts=[
        Floor(friction=Friction(0.8, 0.005, 0.002), size=m(4)),
        Pendulum(pivot_at=m3(0, 0, 1.01), length=m(0.95), bob_radius=m(0.05), bob_mass=kg(1.0), rod_mass=kg(0.1),
                 released_from=rad(1.1), damping=Nms_per_rad(0.01)),
        Ball(radius=m(0.05), mass=kg(0.2), at=m3(0.1, 0, 0.05), rolls=True, friction=Friction(0.8, 0.01, 0.004)),
        OpenBox("cup", at=m3(1.1, 0, 0), length=m(0.3), width=m(0.3), wall_height=m(0.12), wall=m(0.01), base=m(0.01),
                lip=m(0.025)),
    ])


BRIEFS = {"shot": shot, "cup": cup, "door": door, "stack": stack, "catapult": catapult, "dominoes": dominoes,
          "pendulum": pendulum}
