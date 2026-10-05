"""Replay a compiled world and say what happened in the world's own vocabulary: the readback in words.

MuJoCo is deterministic, so a run is a pure function of the world: the same parts give the same run, every time.
That makes the whole run a value you can scrub (`at(t)`), search (`events()`) and fork (edit a part, run again).

    trace = replay(compiled)
    trace.events()     # ["0.53 s  Pendulum.bob first touches Ball", "1.94 s  Ball comes to rest inside Cup", ...]
    trace.at(0.5)      # {"Ball": "at (0.10, 0.00, 0.05) m, 0.00 m/s", "Pendulum.pivot": "8 deg", ...}
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import mujoco
import numpy as np

from typed.compiler import Compiled
from typed.parts import Hoop, OpenBox
from worlds import tests

REST = 0.05  # m/s, as the tests
LIMIT = math.radians(0.5)  # within this of a range end counts as at the stop


@dataclass
class Trace:
    compiled: Compiled
    run: tests.Run

    def _label(self, g: int) -> str:
        name = self.run.model.geom(g).name
        return self.compiled.owner.get(name, name)

    def _step(self, t: float) -> int:
        return int(np.clip(np.searchsorted(self.run.times, t), 0, len(self.run.times) - 1))

    def at(self, t: float) -> dict[str, str]:
        """Every moving part's state at time t, in the vocabulary."""
        m, i, out = self.run.model, self._step(t), {}
        for j in self.compiled.joints:
            if j["kind"] == "free":
                b = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, j["name"].split(" ")[0])
                p = self.run.xpos[i, b]
                jid = tests.free_joint(m, b)
                v = float(np.linalg.norm(self.run.qvel[i, m.jnt_dofadr[jid]: m.jnt_dofadr[jid] + 3]))
                out[j["part"]] = f"at ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f}) m, {v:.2f} m/s"
            else:
                jid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, j["name"])
                out[j["part"]] = f"{math.degrees(self.run.qpos[i, m.jnt_qposadr[jid]]):.0f} deg"
        return out

    def events(self) -> list[str]:
        """What happened, in order: first touches between parts, stops reached, where things came to rest."""
        run, m, ev = self.run, self.run.model, []
        # First touch between two different parts (a part resting on something at t = 0 is not news).
        at_start = {tuple(sorted((self._label(a), self._label(b)))) for a, b in run.contacts[0]}
        seen = set(at_start)
        for i, pairs in enumerate(run.contacts):
            for a, b in sorted(pairs):
                la, lb = sorted((self._label(a), self._label(b)), key=lambda s: s == "Floor")
                if la.split(".")[0] == lb.split(".")[0]:
                    continue
                key = tuple(sorted((la, lb)))
                if key not in seen:
                    seen.add(key)
                    ev.append((run.times[i], f"{la} first touches {lb}"))
        # A hinge reaching either end of its range.
        for j in self.compiled.joints:
            if j["kind"] != "hinge" or not j.get("range"):
                continue
            jid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, j["name"])
            q = run.qpos[:, m.jnt_qposadr[jid]]
            for end, val in zip(("lower", "upper"), j["range"]):
                hit = np.nonzero(np.abs(q - val.si) < LIMIT)[0]
                if len(hit):
                    verb = "starts at" if hit[0] == 0 else "reaches"
                    ev.append((run.times[hit[0]], f"{j['part']} {verb} its {end} stop ({val.deg:.0f} deg)"))
        # A ball coming down through the height of a hoop's rim: through it, or how far off.
        for hoop in (p for p in self.compiled.world.parts if isinstance(p, Hoop)):
            cx, cy, cz = hoop.rim_centre.si
            inner = hoop.inner_diameter.si / 2
            for j in self.compiled.joints:
                if j["part"] != "Ball":
                    continue
                b = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, j["name"].split(" ")[0])
                z = run.xpos[:, b, 2]
                for i in np.nonzero((z[:-1] >= cz) & (z[1:] < cz))[0]:
                    k = (z[i] - cz) / (z[i] - z[i + 1])
                    x, y = run.xpos[i, b, :2] + k * (run.xpos[i + 1, b, :2] - run.xpos[i, b, :2])
                    off = math.hypot(x - cx, y - cy)
                    if off < inner:
                        ev.append((run.times[i], f"Ball drops through Hoop ({off * 100:.0f} cm from the rim's centre)"))
                    else:
                        side = f"{cx - x:.2f} m short of" if x < cx else f"{x - cx:.2f} m past"
                        ev.append((run.times[i], f"Ball comes down through rim height {side} the rim's centre"))
        # Where each loose thing comes to rest, and where that is relative to any open box.
        boxes = [p for p in self.compiled.world.parts if isinstance(p, OpenBox)]
        for j in self.compiled.joints:
            if j["kind"] != "free":
                continue
            b = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, j["name"].split(" ")[0])
            jid = tests.free_joint(m, b)
            v = np.linalg.norm(run.qvel[:, m.jnt_dofadr[jid]: m.jnt_dofadr[jid] + 3], axis=1)
            moving = np.nonzero(v >= REST)[0]
            if not len(moving):
                continue  # never moved: nothing to say
            if moving[-1] == len(v) - 1:
                ev.append((run.times[-1], f"{j['part']} is still moving at the end ({v[-1]:.2f} m/s)"))
                continue
            p = run.xpos[-1, b]
            where = f"at ({p[0]:.2f}, {p[1]:.2f}) m"
            for box in boxes:
                x0, x1, y0, y1 = box.footprint()
                name = box.name.capitalize()
                if x0 <= p[0] <= x1 and y0 <= p[1] <= y1:
                    where = f"inside {name}"
                elif abs(p[1]) <= y1 + 0.5:
                    where += f", {x0 - p[0]:.2f} m short of {name}" if p[0] < x0 else f", {p[0] - x1:.2f} m past {name}"
            ev.append((run.times[moving[-1] + 1], f"{j['part']} comes to rest {where}"))
        return [f"{t:5.2f} s  {s}" for t, s in sorted(ev)]


def replay(compiled: Compiled, seconds: float = 6.0) -> Trace:
    return Trace(compiled, tests.run(compiled.xml, seconds))
