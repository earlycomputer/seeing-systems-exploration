"""The history of a run in words, for any MuJoCo world: what moved, what touched what and when, where things ended.

The spacetime debugger (typed/spacetime.py) writes this for worlds in the world language, where it knows each part's
name. This narrator needs nothing but the MJCF and its run, so it works on any file a model writes. It reports what
MuJoCo did, never what the file says: a hinge's range is read back from the compiled model, in degrees.

    from worlds.tests import run
    print(history(run(xml)))
"""

from __future__ import annotations

import math

import mujoco
import numpy as np

from worlds.tests import Run

REST = 0.05  # m/s, as the tests
GAP = 0.03  # s: a touch that breaks for less than this is one touch (bounces and contact chatter)
EVERY = 0.25  # s between rows of the state table
MAX_TOUCHES = 4  # touch intervals listed per pair; the rest are counted
STOP = 0.5  # degrees (hinge) or 5 mm (slide) from a range end counts as at the stop

J = mujoco.mjtJoint
G_PLANE = mujoco.mjtGeom.mjGEOM_PLANE
NEAR = 0.5  # m: a closer pass by something never touched is reported
APPROACH = 0.1  # m: ...if it came at least this much closer than it started


def _f(x: float, n: int = 2) -> str:
    s = f"{x:.{n}f}"
    return "0." + "0" * n if s in ("-0." + "0" * n,) else s


def _p(p) -> str:
    return f"({_f(p[0])}, {_f(p[1])}, {_f(p[2])}) m"


class Narrator:
    def __init__(self, run: Run):
        self.run, self.m = run, run.model
        m = self.m
        self.label = {}
        for g in range(m.ngeom):
            gname, b = m.geom(g).name or f"geom{g}", int(m.geom_bodyid[g])
            bname = m.body(b).name
            self.label[g] = gname if b == 0 or not bname or gname.startswith(bname) else f"{bname}.{gname}"
        # Things that move: one entry per joint, named after its body (and the joint when a body has several).
        self.movers = []
        per_body = {}
        for j in range(m.njnt):
            per_body.setdefault(int(m.jnt_bodyid[j]), []).append(j)
        for b, js in per_body.items():
            for j in js:
                bname = m.body(b).name or f"body{b}"
                kind = int(m.jnt_type[j])
                name = bname if len(js) == 1 else f"{bname} ({m.joint(j).name or f'joint{j}'})"
                self.movers.append({"name": name, "body": b, "joint": j, "kind": kind,
                                    "adr": int(m.jnt_qposadr[j]), "vadr": int(m.jnt_dofadr[j])})
        self.moving_bodies = {mv["body"] for mv in self.movers}
        # a body made only of spheres turns as it rolls; its turning is not news
        self.round = {b: all(m.geom_type[g] == mujoco.mjtGeom.mjGEOM_SPHERE for g in range(m.ngeom) if m.geom_bodyid[g] == b)
                      for b in self.moving_bodies}
        T = len(run.times)
        self.speed = {mv["name"]: np.linalg.norm(run.qvel[:, mv["vadr"]: mv["vadr"] + 3], axis=1)
                      for mv in self.movers if mv["kind"] == J.mjJNT_FREE}
        self.T = T

    # ---- one moment ---------------------------------------------------------------------------------------
    def tilt(self, b: int, i: int) -> float:
        q0, q = self.run.xquat[0, b], self.run.xquat[i, b]
        return math.degrees(2 * math.acos(min(1.0, abs(float(np.dot(q0, q))))))

    def angle(self, mv: dict, i: int) -> float:
        q = self.run.qpos[i, mv["adr"]]
        return math.degrees(q) if mv["kind"] == J.mjJNT_HINGE else float(q)

    def rng(self, mv: dict):
        j = mv["joint"]
        if not self.m.jnt_limited[j]:
            return None
        lo, hi = self.m.jnt_range[j]
        return (math.degrees(lo), math.degrees(hi)) if mv["kind"] == J.mjJNT_HINGE else (float(lo), float(hi))

    def touching(self, i: int, b: int) -> list[str]:
        out = set()
        for g1, g2 in self.run.contacts[i]:
            b1, b2 = self.m.geom_bodyid[g1], self.m.geom_bodyid[g2]
            if b1 == b2:
                continue
            if b1 == b:
                out.add(self.label[g2])
            elif b2 == b:
                out.add(self.label[g1])
        return sorted(out)

    def state(self, mv: dict, i: int) -> str:
        run = self.run
        if mv["kind"] == J.mjJNT_FREE:
            p, v = run.xpos[i, mv["body"]], run.qvel[i, mv["vadr"]: mv["vadr"] + 3]
            s = float(np.linalg.norm(v))
            words = f"at {_p(p)}, " + (f"moving {s:.2f} m/s (vx {v[0]:+.2f}, vy {v[1]:+.2f}, vz {v[2]:+.2f})"
                                       if s >= REST else "at rest")
            t = self.tilt(mv["body"], i)
            if t >= 1 and not self.round[mv["body"]]:
                words += f", turned {t:.0f}° from how it started"
            return words
        if mv["kind"] in (J.mjJNT_HINGE, J.mjJNT_SLIDE):
            hinge = mv["kind"] == J.mjJNT_HINGE
            a, w = self.angle(mv, i), run.qvel[i, mv["vadr"]]
            w = math.degrees(w) if hinge else float(w)
            unit, rate = ("°", "°/s") if hinge else (" m", " m/s")
            fmt = (lambda x: f"{x:.1f}") if hinge else (lambda x: f"{x:.3f}")
            moving = abs(w) > (1 if hinge else 0.01)
            return f"at {fmt(a)}{unit}, " + (f"turning {w:+.0f}{rate}" if hinge and moving else
                                             f"moving {w:+.2f}{rate}" if moving else "still")
        return "(ball joint)"

    # ---- over time ----------------------------------------------------------------------------------------
    def intervals(self) -> dict[tuple, list]:
        run, m, spans = self.run, self.m, {}
        for i, pairs in enumerate(run.contacts):
            seen = set()
            for g1, g2 in pairs:
                b1, b2 = int(m.geom_bodyid[g1]), int(m.geom_bodyid[g2])
                if b1 == b2 or (b1 not in self.moving_bodies and b2 not in self.moving_bodies):
                    continue
                a, b = self.label[g1], self.label[g2]
                # the moving thing first, the floor last
                if (b1 not in self.moving_bodies) or (a == "floor"):
                    a, b = b, a
                key = (a, b)
                if key in seen:
                    continue
                seen.add(key)
                s, t = spans.setdefault(key, []), float(run.times[i])
                if s and t - s[-1][1] <= GAP + 1e-9:
                    s[-1][1] = t
                else:
                    s.append([t, t])
        return spans

    def events(self) -> list[tuple[float, str]]:
        run, ev, end = self.run, [], float(self.run.times[-1])
        for (a, b), spans in self.intervals().items():
            for k, (t0, t1) in enumerate(spans[:MAX_TOUCHES]):
                if t0 <= 0:
                    ev.append((0.0, f"{a} starts touching {b}"))
                else:
                    ev.append((t0, f"{a} {'first touches' if k == 0 else 'touches'} {b}{' again' if k else ''}"))
                if t1 < end - 1e-9:
                    ev.append((t1, f"{a} leaves {b}"))
            if len(spans) > MAX_TOUCHES:
                rest = spans[MAX_TOUCHES:]
                ev.append((rest[0][0], f"{a} touches {b} {len(rest)} more times between {rest[0][0]:.2f} s and "
                                       f"{rest[-1][1]:.2f} s" + ("" if rest[-1][1] < end - 1e-9 else ", still touching at the end")))
        for mv in self.movers:
            name = mv["name"]
            if mv["kind"] == J.mjJNT_FREE:
                b, sp = mv["body"], self.speed[name]
                free = np.array([not self.touching(i, b) for i in range(self.T)])
                i = 0
                while i < self.T:  # the top of each flight longer than 0.1 s
                    if not free[i]:
                        i += 1
                        continue
                    j = i
                    while j < self.T and free[j]:
                        j += 1
                    if run.times[j - 1] - run.times[i] > 0.1:
                        k = i + int(np.argmax(run.xpos[i:j, b, 2]))
                        if i < k < j - 1:
                            ev.append((float(run.times[k]), f"{name} is at the top of its flight, at {_p(run.xpos[k, b])}"))
                    i = j
                moving = np.nonzero(sp >= REST)[0]
                if not len(moving):
                    continue
                if moving[0] > 0:
                    ev.append((float(run.times[moving[0]]), f"{name} starts moving"))
                if moving[-1] == self.T - 1:
                    ev.append((end, f"{name} is still moving at the end, {sp[-1]:.2f} m/s"))
                else:
                    k = moving[-1] + 1
                    ev.append((float(run.times[k]), f"{name} comes to rest at {_p(run.xpos[k, b])}"))
            elif mv["kind"] in (J.mjJNT_HINGE, J.mjJNT_SLIDE):
                hinge = mv["kind"] == J.mjJNT_HINGE
                unit = "°" if hinge else " m"
                tol = STOP if hinge else 0.005
                q = np.array([self.angle(mv, i) for i in range(self.T)])
                r = self.rng(mv)
                if r:
                    lo, hi = r
                    if q[0] < lo - tol or q[0] > hi + tol:
                        ev.append((0.0, f"{name} starts at {q[0]:.1f}{unit}, outside its range of {lo:g}{unit} to {hi:g}{unit}"))
                    for which, val in (("lower", lo), ("upper", hi)):
                        at = np.abs(q - val) < tol
                        hits = np.nonzero(at[1:] & ~at[:-1])[0] + 1
                        if at[0]:
                            ev.append((0.0, f"{name} starts at its {which} stop ({val:g}{unit})"))
                        for n, i in enumerate(hits[:3]):
                            w = run.qvel[i - 1, mv["vadr"]]
                            w = f"{math.degrees(w):+.0f}°/s" if hinge else f"{w:+.2f} m/s"
                            ev.append((float(run.times[i]), f"{name} reaches its {which} stop ({val:g}{unit}) "
                                                            f"{'again ' if n or at[0] else ''}moving {w}"))
                        if len(hits) > 3:
                            ev.append((float(run.times[hits[3]]), f"{name} reaches its {which} stop {len(hits) - 3} more times"))
                k_hi, k_lo = int(np.argmax(q)), int(np.argmin(q))
                ev.append((float(run.times[k_hi]), f"{name} is at its largest, {q[k_hi]:.1f}{unit}") if k_hi > 0 else (0.0, f"{name} is at its largest at the start, {q[0]:.1f}{unit}"))
                if k_lo > 0:
                    ev.append((float(run.times[k_lo]), f"{name} is at its smallest, {q[k_lo]:.1f}{unit}"))
        ev += self.near_misses()
        return sorted(ev, key=lambda e: e[0])

    def near_misses(self) -> list[tuple[float, str]]:
        """For each moving body, its closest pass by every other body it never touched (within NEAR)."""
        run, m = self.run, self.m
        d = mujoco.MjData(m)
        group = lambda g: (int(m.geom_bodyid[g]), self.label[g]) if m.geom_bodyid[g] == 0 else (int(m.geom_bodyid[g]), None)
        touched = set()  # (moving body, group it touched); fixed geoms in the world body are each their own group
        for pairs in run.contacts:
            for g1, g2 in pairs:
                touched.add((int(m.geom_bodyid[g1]), group(g2)))
                touched.add((int(m.geom_bodyid[g2]), group(g1)))
        best = {}  # (mover name, other group) -> (dist, i, g_mover, g_other, fromto)
        start = {}  # (mover name, other group) -> distance at the start
        ft = np.zeros(6)
        movers = {mv["body"]: mv["name"] for mv in self.movers}
        for i in range(0, self.T, 5):
            d.qpos[:] = run.qpos[i]
            mujoco.mj_kinematics(m, d)
            for b, name in movers.items():
                for g1 in range(m.ngeom):
                    if m.geom_bodyid[g1] != b:
                        continue
                    for g2 in range(m.ngeom):
                        b2 = int(m.geom_bodyid[g2])
                        if b2 == b or m.geom_type[g2] == G_PLANE or (b, group(g2)) in touched:
                            continue
                        dist = mujoco.mj_geomDistance(m, d, g1, g2, 10.0 if i == 0 else NEAR, ft)
                        if i == 0:
                            k0 = (name, group(g2))
                            start[k0] = min(start.get(k0, 1e9), dist)
                        if dist < NEAR:
                            key = (name, group(g2))
                            if key not in best or dist < best[key][0]:
                                best[key] = (dist, i, g1, g2, ft.copy())
        out, said = [], set()
        for (name, (b2, lab)), (dist, i, g1, g2, f) in best.items():
            if start.get((name, (b2, lab)), 1e9) - dist < APPROACH:
                continue  # it was this close from the start: not a pass
            pair = frozenset((m.body(b2).name if not lab else lab, name))
            if pair in said:
                continue
            said.add(pair)
            other = lab or (m.body(b2).name or f"body{b2}")
            part = "" if lab or self.label[g2] == other else f" ({self.label[g2]})"
            out.append((float(run.times[i]), f"{name} passes {dist:.2f} m from {other}{part} without touching it: "
                                             f"nearest points {_p(f[:3])} and {_p(f[3:])}"))
        return out

    def moving_list(self) -> list[str]:
        out = []
        for mv in self.movers:
            m, j = self.m, mv["joint"]
            geoms = [self.label[g] for g in range(m.ngeom) if m.geom_bodyid[g] == mv["body"]]
            if mv["kind"] == J.mjJNT_FREE:
                kind = "free body"
            else:
                axis = m.jnt_axis[j]
                kind = f"{'hinge' if mv['kind'] == J.mjJNT_HINGE else 'slide' if mv['kind'] == J.mjJNT_SLIDE else 'ball'} " \
                       f"joint {m.joint(j).name or ''} about axis ({_f(axis[0])}, {_f(axis[1])}, {_f(axis[2])})".replace("  ", " ")
                r = self.rng(mv)
                if mv["kind"] in (J.mjJNT_HINGE, J.mjJNT_SLIDE):
                    unit = "°" if mv["kind"] == J.mjJNT_HINGE else " m"
                    kind += f", range {r[0]:g}{unit} to {r[1]:g}{unit} as MuJoCo applies it" if r else ", no range limit"
            out.append(f"- {mv['name']}: {kind}; its geoms: {', '.join(geoms)}; starts {self.state(mv, 0)}")
        return out

    def table(self) -> list[str]:
        times = self.run.times
        rows, last, quiet = [], None, None
        t = 0.0
        while t <= times[-1] + 1e-9:
            i = int(np.clip(np.searchsorted(times, t - 1e-9), 0, self.T - 1))
            cells = []
            for mv in self.movers:
                s = self.state(mv, i)
                touch = self.touching(i, mv["body"])
                cells.append(f"{mv['name']} {s}; touching {', '.join(touch) if touch else 'nothing'}")
            row = " | ".join(cells)
            if row == last:  # nothing changed: say so once, not row after row
                quiet = times[i]
            else:
                if quiet is not None:
                    rows.append(f"(the same through {quiet:.2f} s)")
                    quiet = None
                rows.append(f"{times[i]:.2f} s: " + row)
            last = row
            t += EVERY
        if quiet is not None:
            rows.append(f"(the same through {quiet:.2f} s)")
        return rows


def history(run: Run) -> str:
    n = Narrator(run)
    end = float(run.times[-1])
    out = [f"The run lasted {end:.2f} s" + (f" ({run.diverged})" if run.diverged else "") + ". "
           "Positions are of each body's origin in metres; z is up and the floor's top is z = 0.", ""]
    if not n.movers:
        return "\n".join(out + ["Nothing in the scene can move: it has no joints."])
    out += ["Things that can move:"] + n.moving_list() + ["", "What happened, in order:"]
    out += [f"{t:5.2f} s  {s}" for t, s in n.events()]
    out += ["", f"State every {EVERY:g} s:"] + n.table()
    out += ["", f"At the end ({end:.2f} s):"]
    for mv in n.movers:
        touch = n.touching(n.T - 1, mv["body"])
        out.append(f"- {mv['name']} {n.state(mv, n.T - 1)}; touching {', '.join(touch) if touch else 'nothing'}")
    return "\n".join(out)
