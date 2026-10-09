"""Errors with the why in them: when an expectation fails, say when it was lost, how, and which lines to change.

Jono, 2026-10-07: "I want the why trace to show up in errors. The debugger is UI for a human to process information
that would be overwhelming to read. An agent can read much more, much faster." The spacetime debugger
(typed/spacetime.py) finds the why for a person to click through; this module writes it into the error itself, for
any world, written in the world language or in raw MuJoCo XML:

    from why.errors import explain
    print(explain(source, fmt="world", lines=["ball comes to rest in bucket"]))

For each expectation that fails, the error says, in this order:

1. **What you expected and what happened**, pointing at the expect line.
2. **When it was lost.** The moment an expectation is decided (the ball comes to rest at 1.88 s) is rarely when it
   went wrong (the ball came down 0.45 m short at 1.14 s). Each form has its own losing moment: the last landing
   before rest, the nearest pass for a touch, the crossing for a drop, the nearest approach for a stop.
3. **How it got there.** The light cone of that moment: walk back through touch alone, because a thing can only
   have been changed by what touched it. Only events inside the cone are listed, oldest first.
4. **The lines that set those things up**, from the file the author wrote: every thing in the cone, the things they
   touched on the way and the target.
5. **Which numbers move it.** Each number in those lines is forked (x1.1, x0.9, x1.5, x0.5) and the world run again; the
   numbers that move the miss most are listed with what happened in each fork, and whether the expectation then holds.
   Running is cheap (a third of a second a fork), so the error tries the forks instead of asking anyone to guess.

The error describes the run and points at lines; it never edits the world. Expectations use langrun/expect.py's forms.
"""

from __future__ import annotations

import math
import os
import re
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field

import mujoco
import numpy as np

from history.narrate import Narrator
from langrun import expect
from typed.compiler import render
from typed.lang import LIBRARY, compile_program, parse
from worlds.tests import Run, aabb, free_joint
from worlds.tests import run as run_world

SECONDS = 6.0
FLIGHT = 0.1  # s: touching nothing for longer than this is a flight
FACTORS = (1.1, 0.9, 1.5, 0.5)  # each number is forked to these multiples of itself, one at a time
MAX_FORKS = 240  # runs per error at most; numbers on moving things come first
TOP = 3  # numbers listed under "which numbers move it"
MAX_CHAIN = 14  # events listed under "how it got there"; the earliest are kept, the middle counted
SKIP_ATTRS = {"name", "type", "rgba", "axis", "condim", "contype", "conaffinity", "group", "class", "model", "mode",
              "material", "texture", "joint", "body", "mesh", "solimp", "quat", "euler", "zaxis", "fromto"}


# ---- a world, built and run ------------------------------------------------------------------------------------

@dataclass
class World:
    fmt: str  # "world" or "xml"
    source: str
    library: str | None = None
    xml: str | None = None
    owner: dict = field(default_factory=dict)
    joints: list = field(default_factory=list)
    problem: str | None = None
    run: Run | None = None


def build(source: str, fmt: str, library: str | None = None, seconds: float = SECONDS) -> World:
    w = World(fmt, source, library)
    if fmt == "world":
        lib = LIBRARY.read_text() if library is None else library
        try:
            c = compile_program(parse(source, lib))
        except Exception as e:  # noqa: BLE001 - a crash in the compiler is reported, not raised
            w.problem = f"The world could not be read: {type(e).__name__}: {e}"
            return w
        if c.problems:
            w.problem = render(c.problems)
            return w
        w.xml, w.owner, w.joints = c.xml, c.owner, c.joints
    else:
        w.xml = source
    try:
        w.run = run_world(w.xml, seconds)
    except Exception as e:  # noqa: BLE001
        w.problem = f"MuJoCo could not load the file: {e}"
    return w


# ---- the run as things, touches and events -----------------------------------------------------------------------

class Story:
    """The run told in the author's names: who moves, who touched whom and when, and the light cone of a moment."""

    def __init__(self, w: World):
        self.w, self.run, self.m = w, w.run, w.run.model
        n = Narrator(w.run)
        m = self.m
        if w.owner:
            for g in range(m.ngeom):
                if m.geom(g).name in w.owner:
                    n.label[g] = w.owner[m.geom(g).name]
        self.n, self.label = n, n.label
        self.name = {}  # moving body -> the author's name for it
        for mv in n.movers:
            b = mv["body"]
            labs = [n.label[g] for g in range(m.ngeom) if m.geom_bodyid[g] == b]
            self.name[b] = self.name.get(b) or (_common(labs) if w.owner else m.body(b).name) or mv["name"]
        for j in w.joints:  # the language names its hinged parts (catapult.arm)
            jid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, j["name"])
            if jid >= 0:
                self.name[int(m.jnt_bodyid[jid])] = j["part"]
        self.moving = set(self.name)
        self.body_of = {}
        for g, lab in self.label.items():
            self.body_of.setdefault(lab, int(m.geom_bodyid[g]))
        self.spans = n.intervals()  # (label a, label b) -> [[t0, t1], ...], moving thing first
        self.T = len(self.run.times)

    # one moment
    def i(self, t: float) -> int:
        return int(np.clip(np.searchsorted(self.run.times, t - 1e-9), 0, self.T - 1))

    def where(self, b: int, i: int) -> str:
        run = self.run
        mv = next(x for x in self.n.movers if x["body"] == b)
        if mv["kind"] == mujoco.mjtJoint.mjJNT_FREE:
            p, v = run.xpos[i, b], run.qvel[i, mv["vadr"]: mv["vadr"] + 3]
            s = float(np.linalg.norm(v))
            head = math.degrees(math.atan2(v[2], math.hypot(v[0], v[1])))
            return f"{p[0]:.2f} m along, {p[2]:.2f} m up, " + (f"{s:.2f} m/s heading {head:+.0f}°" if s >= expect.REST
                                                                 else "at rest")
        if mv["kind"] == mujoco.mjtJoint.mjJNT_HINGE:
            a, r = math.degrees(run.qpos[i, mv["adr"]]), math.degrees(run.qvel[i, mv["vadr"]])
            return f"at {a:.0f}°, " + (f"turning {r:+.0f}°/s" if abs(r) > 1 else "still")
        return self.n.state(mv, i)

    # events with who took part, for the cone
    def events(self) -> list[dict]:
        run, end, ev = self.run, float(self.run.times[-1]), []
        for (a, b), spans in self.spans.items():
            for k, (t0, t1) in enumerate(spans):
                if t0 <= 0:
                    ev.append({"t": 0.0, "who": [a, b], "text": f"{a} starts against {b}"})
                else:
                    ev.append({"t": t0, "who": [a, b], "text": f"{a} {'touches' if k else 'first touches'} {b}"
                                                             f"{' again' if k else ''}"})
                if t1 < end - 1e-9:
                    ev.append({"t": t1, "who": [a, b], "text": f"{a} leaves {b}"})
        for b in self.moving:
            name = self.name[b]
            for i, j in self.flights(b):
                k = i + int(np.argmax(run.xpos[i:j, b, 2]))
                if i < k < j - 1:
                    ev.append({"t": float(run.times[k]), "who": [self._label_of(b)],
                               "text": f"{name} is at its highest, {run.xpos[k, b, 2]:.2f} m up"})
        for mv in self.n.movers:
            r = self.n.rng(mv)
            if mv["kind"] != mujoco.mjtJoint.mjJNT_HINGE or not r:
                continue
            q = np.degrees(run.qpos[:, mv["adr"]])
            for which, val in (("lower", r[0]), ("upper", r[1])):
                at = np.abs(q - val) < 0.5
                for i in (np.nonzero(at[1:] & ~at[:-1])[0] + 1)[:3]:
                    ev.append({"t": float(run.times[i]), "who": [self._label_of(mv["body"])],
                               "text": f"{self.name[mv['body']]} reaches its {which} stop ({val:g}°)"})
        ev.sort(key=lambda e: (e["t"], "leaves" in e["text"]))
        return ev

    def _label_of(self, b: int) -> str:
        return next(lab for lab, x in self.body_of.items() if x == b)

    def flights(self, b: int) -> list[tuple[int, int]]:
        """Steps [i, j) when body b touched nothing for longer than FLIGHT."""
        free = [not self.n.touching(i, b) for i in range(self.T)]
        out, i = [], 0
        while i < self.T:
            if not free[i]:
                i += 1
                continue
            j = i
            while j < self.T and free[j]:
                j += 1
            if self.run.times[j - 1] - self.run.times[i] > FLIGHT:
                out.append((i, j))
            i = j
        return out

    def cone(self, b: int, t: float) -> dict[int, float]:
        """How late each body could still have influenced body b at time t, through touch alone (spacetime.py's walk)."""
        horizon, changed = {b: t}, True
        while changed:
            changed = False
            for (la, lb), spans in self.spans.items():
                ba, bb = self.body_of[la], self.body_of[lb]
                for t0, t1 in spans:
                    for src, dst in ((ba, bb), (bb, ba)):
                        if src in horizon and src in self.moving and t0 <= horizon[src]:
                            h = min(t1, horizon[src])
                            if h > horizon.get(dst, -1):
                                horizon[dst], changed = h, True
        return horizon


def _common(labels: list[str]) -> str:
    """catapult.arm, catapult.scoop base -> catapult.arm's owner part; ball -> ball."""
    if not labels:
        return ""
    heads = {lab.split(".")[0] for lab in labels}
    return labels[0] if len(set(labels)) == 1 else (labels[0].split(".")[0] if len(heads) == 1 else labels[0])


# ---- each form: did it hold, when was it lost, by how much -----------------------------------------------------

@dataclass
class Verdict:
    line: str
    ok: bool
    evidence: str
    subject: int | None = None  # body
    others: list = field(default_factory=list)  # bodies of the target that move
    target: str = ""
    t_lost: float | None = None
    t_decided: float | None = None  # when the run settled it, where that is a moment (coming to rest)
    lost: str = ""  # the losing moment in words
    miss: float | None = None  # how far from holding, in the form's own unit (m or °); 0 when it holds
    unit: str = "m"
    miss_words: str = ""


def _gs(run, name, owner):
    return expect.geoms(run, name, owner)


def _box_gap(p, lo, hi, start) -> tuple[float, str]:
    """How far point p is outside the footprint [lo, hi] (xy), and whether that is short of it or past it."""
    dx = max(lo[0] - p[0], 0, p[0] - hi[0])
    dy = max(lo[1] - p[1], 0, p[1] - hi[1])
    gap = math.hypot(dx, dy)
    if gap == 0:
        return 0.0, "inside"
    c = (lo[:2] + hi[:2]) / 2
    toward = c - start[:2]
    ahead = float(np.dot(p[:2] - start[:2], toward) / max(np.linalg.norm(toward), 1e-9))
    return gap, ("short of" if ahead < np.linalg.norm(toward) else "past") if abs(dx) >= abs(dy) else "to the side of"


def assess(line: str, s: Story, strict: bool = False) -> Verdict:
    """strict: judge by 1h's hidden-test forms (a touch must begin after the start, and so on), not the author's."""
    run, owner = s.run, s.w.owner
    if strict:
        from hundred.hidden import one as hidden_one  # read only; hundred/ belongs to another thread
        ok, _, evidence = hidden_one(line, run, owner)
    else:
        ok, evidence = expect.one(line, run, owner)
    v = Verdict(line, ok, evidence)
    low = line.strip().rstrip(".").lower()
    if m := re.fullmatch(r"(.+?) comes to rest in (.+)", low):
        a, b = _gs(run, m[1], owner), _gs(run, m[2], owner)
        free = [x for x in expect.bodies(run, a) if expect.free_joint_or_none(run, x) is not None]
        if not free or not b:
            return v
        x, v.target = free[0], m[2]
        v.subject, v.others = x, [y for y in expect.bodies(run, b) if y in s.moving]
        start = run.xpos[0, x]
        moving = np.nonzero(expect.speed(run, x) >= expect.REST)[0]
        if len(moving) and moving[-1] < s.T - 1:
            v.t_decided = float(run.times[moving[-1] + 1])
        inside = [bool(_box_gap(run.xpos[i, x], *aabb(run, b, i), start)[0] == 0 and run.xpos[i, x, 2] < aabb(run, b, i)[1][2])
                  for i in range(0, s.T, 5)]
        end_gap, end_side = _box_gap(run.xpos[-1, x], *aabb(run, b, -1), start)
        if any(inside) and not inside[-1]:
            k = (len(inside) - 1 - inside[::-1].index(True)) * 5
            v.t_lost = float(run.times[min(k + 5, s.T - 1)])
            v.lost = f"{m[1]} was inside {m[2]} until {run.times[k]:.2f} s, then left it ({s.where(x, k)})"
            v.miss, v.miss_words = end_gap, f"rests {end_gap:.2f} m {end_side} {m[2]}"
        else:
            fl = [f for f in s.flights(x) if f[1] < s.T]
            if fl:
                j = fl[-1][1]
                gap, side = _box_gap(run.xpos[j, x], *aabb(run, b, j), start)
                lo, hi = aabb(run, b, j)
                v.t_lost = float(run.times[j])
                touched = ", ".join(s.n.touching(j, x)) or "something"
                v.lost = (f"{m[1]} came down on {touched} {gap:.2f} m {side} {m[2]}, which spans {lo[0]:.2f} to "
                          f"{hi[0]:.2f} m along ({s.where(x, j)})") if gap > 0 else \
                         f"{m[1]} came down inside {m[2]}'s footprint on {touched} and did not stay ({s.where(x, j)})"
                v.miss, v.miss_words = gap, f"comes down {gap:.2f} m {side} {m[2]}"
            else:
                d = [_box_gap(run.xpos[i, x], *aabb(run, b, i), start)[0] for i in range(s.T)]
                k = int(np.argmin(d))
                v.t_lost = float(run.times[k])
                v.lost = f"{m[1]} was nearest {m[2]} at {run.times[k]:.2f} s, {d[k]:.2f} m from it ({s.where(x, k)})"
                v.miss, v.miss_words = d[k], f"gets within {d[k]:.2f} m of {m[2]}"
        if ok:
            v.miss = 0.0
        return v
    if m := re.fullmatch(r"(.+?) touches (.+)", low):
        a, b = _gs(run, m[1], owner), _gs(run, m[2], owner)
        if not a or not b:
            return v
        v.target = m[2]
        moving = [y for y in expect.bodies(run, a) if y in s.moving]
        v.subject = moving[0] if moving else None
        v.others = [y for y in expect.bodies(run, b) if y in s.moving]
        if v.subject is None and v.others:
            v.subject, v.others = v.others[0], []
        if ok:
            v.miss = 0.0
            return v
        d, best, ft = mujoco.MjData(s.m), (1e9, 0), np.zeros(6)
        for i in range(0, s.T, 5):
            d.qpos[:] = run.qpos[i]
            mujoco.mj_kinematics(s.m, d)
            for g1 in a:
                for g2 in b:
                    if s.m.geom_type[g2] == mujoco.mjtGeom.mjGEOM_PLANE or s.m.geom_type[g1] == mujoco.mjtGeom.mjGEOM_PLANE:
                        other = g1 if s.m.geom_type[g2] == mujoco.mjtGeom.mjGEOM_PLANE else g2
                        dist = float(aabb(run, [other], i)[0][2])  # its lowest point above the floor
                    else:
                        dist = mujoco.mj_geomDistance(s.m, d, g1, g2, 50.0, ft)
                    if dist < best[0]:
                        best = (dist, i)
        dist, k = best
        v.t_lost, v.miss = float(run.times[k]), dist
        v.lost = f"{m[1]} came nearest {m[2]} at {run.times[k]:.2f} s, {dist:.2f} m from it" + \
                 (f" ({s.where(v.subject, k)})" if v.subject is not None else "") + ", then drew away"
        v.miss_words = f"gets within {dist:.2f} m of {m[2]}"
        return v
    if m := re.fullmatch(r"(.+?) drops through (.+)", low):
        a, b = _gs(run, m[1], owner), _gs(run, m[2], owner)
        if not a or not b:
            return v
        x, v.target = expect.bodies(run, a)[0], m[2]
        v.subject = x
        z, best, top = run.xpos[:, x, 2], None, None
        for i in range(len(z) - 1):
            lo, hi = aabb(run, b, i)
            cz = (lo[2] + hi[2]) / 2
            if z[i] >= cz > z[i + 1]:
                c = (lo[:2] + hi[:2]) / 2
                rad = min(hi[0] - lo[0], hi[1] - lo[1]) / 2
                off = float(np.linalg.norm(run.xpos[i, x, :2] - c))
                if best is None or off - rad < best[0]:
                    best = (off - rad, i, c, rad)
            top = cz
        if best is not None:
            gap, k, c, rad = best
            p = run.xpos[k, x]
            side = "short of" if np.dot(p[:2] - c, c - run.xpos[0, x, :2]) < 0 else "past"
            v.t_lost, v.miss = float(run.times[k]), max(gap, 0.0)
            v.lost = (f"{m[1]} came down through {m[2]}'s height {np.linalg.norm(p[:2] - c):.2f} m from its centre, "
                      f"{side} it, its opening being {rad:.2f} m across from the centre ({s.where(x, k)})")
            v.miss_words = f"passes {max(gap, 0):.2f} m outside {m[2]}'s opening"
        else:
            k = int(np.argmax(z))
            v.t_lost, v.miss = float(run.times[k]), float(top - z[k]) if top is not None else None
            v.lost = f"{m[1]} rose no higher than {z[k]:.2f} m, at {run.times[k]:.2f} s; {m[2]} is at {top:.2f} m"
            v.miss_words = f"tops out {v.miss:.2f} m below {m[2]}"
        if ok:
            v.miss = 0.0
        return v
    if m := re.fullmatch(r"(.+?) reaches its (lower|upper) stop", low):
        mm, k_ = s.m, expect.key(m[1])
        js = [j for j in range(mm.njnt) if mm.jnt_type[j] == mujoco.mjtJoint.mjJNT_HINGE and mm.jnt_limited[j] and
              (expect.key(mm.joint(j).name) == k_ or mm.jnt_bodyid[j] in expect.bodies(run, _gs(run, m[1], owner)))]
        if not js:
            return v
        j = js[0]
        v.subject, v.target, v.unit = int(mm.jnt_bodyid[j]), f"its {m[2]} stop", "°"
        q = np.degrees(run.qpos[:, mm.jnt_qposadr[j]])
        end = math.degrees(mm.jnt_range[j][0 if m[2] == "lower" else 1])
        if abs(q[0] - end) < 0.5:
            v.t_lost, v.miss = 0.0, 0.0
            v.lost = (f"{m[1]} starts at its {m[2]} stop ({end:g}°), so reaching it is not something that happens; "
                      f"its largest swing away is {np.abs(q - end).max():.0f}°")
            v.miss_words = f"starts at its {m[2]} stop"
            if ok:
                v.miss = 0.0
            return v
        k = int(np.argmin(np.abs(q - end)))
        v.t_lost, v.miss = float(run.times[k]), float(abs(q[k] - end))
        touch = s.n.touching(k, v.subject)
        v.lost = (f"{m[1]} came nearest its {m[2]} stop ({end:g}°) at {run.times[k]:.2f} s, {v.miss:.0f}° from it"
                  + (f", touching {', '.join(touch)}" if touch else "") + f" ({s.where(v.subject, k)})")
        v.miss_words = f"gets within {v.miss:.0f}° of its {m[2]} stop"
        if ok:
            v.miss = 0.0
        return v
    return v


# ---- where things are written ----------------------------------------------------------------------------------

def blocks_world(source: str) -> dict[str, list[int]]:
    """Top-level thing name -> its line numbers (1-based) in a .world file."""
    out, cur = {}, None
    for n, raw in enumerate(source.splitlines(), 1):
        if raw.strip() and not raw[0].isspace():
            head = raw.strip()
            cur = None if re.match(r"(world|air|expect)\b", head) else head
            if cur:
                out[cur] = [n]
        elif cur and raw.strip():
            out[cur].append(n)
    return out


def blocks_xml(source: str) -> dict[str, list[int]]:
    """Body or loose geom name -> its line numbers in an MJCF file (a body's lines run to its closing tag)."""
    lines, out = source.splitlines(), {}
    for n, raw in enumerate(lines, 1):
        if m := re.search(r"<body\b[^>]*\bname=\"([^\"]+)\"", raw):
            depth, k = 0, n
            for k in range(n, len(lines) + 1):
                depth += len(re.findall(r"<body\b", lines[k - 1])) - len(re.findall(r"</body>", lines[k - 1]))
                if depth <= 0:
                    break
            out[m[1]] = list(range(n, k + 1))
        elif m := re.search(r"<geom\b[^>]*\bname=\"([^\"]+)\"", raw):
            out.setdefault(m[1], [n])
        elif re.search(r"<key\b", raw):
            out[f"<key {n}>"] = [n]
    return out


def lines_for(s: Story, names: set[str]) -> list[int]:
    """The lines where these things (labels like catapult.arm, ball, bucket.near wall) are written."""
    src = s.w.source
    if s.w.fmt == "world":
        blocks, keys = blocks_world(src), set()
        for name in names:
            head = name.split(".")[0]
            for cand in (head, re.sub(r"\d+$", "", head)):
                if cand in blocks:
                    keys.add(cand)
                    break
    else:
        blocks, keys = blocks_xml(src), set()
        m = s.m
        for name in names:
            b = s.body_of.get(name)
            if b:  # a body: its own block, or its outermost named ancestor's
                while m.body_parentid[b] != 0 and m.body(b).name not in blocks:
                    b = int(m.body_parentid[b])
                if m.body(b).name in blocks:
                    keys.add(m.body(b).name)
            gname = name.split(".")[-1]
            for k in (name, gname, name.replace(".", "_")):
                if k in blocks:
                    keys.add(k)
            if b is None or b == 0:
                for k in blocks:
                    if k == name or k.startswith(name + "_"):
                        keys.add(k)
        # a keyframe sets where everything starts and how fast it moves, so it belongs to every moving thing
        keys.update(k for k in blocks if k.startswith("<key"))
    return sorted({n for k in keys for n in blocks[k]})


# ---- forks ---------------------------------------------------------------------------------------------------

def numbers(source: str, rows: list[int], fmt: str) -> list[tuple[int, int, int, str]]:
    """Every number written on these lines that could be forked: (row, start, end, text)."""
    lines, out = source.splitlines(), []
    for n in rows:
        raw = lines[n - 1]
        if fmt == "world":
            body = raw.strip()
            if not raw[:1].isspace():
                continue  # a thing's name line
            key = re.match(r"\s*(.+?)(\s{2,}|$)", raw)
            if key and key[1] in ("stacked",):
                continue
            off = key.end() if key else 0
            for m in re.finditer(r"(?<![\w.])-?\d+(?:\.\d+)?", raw[off:]):
                out.append((n, off + m.start(), off + m.end(), m[0]))
        else:
            for a in re.finditer(r"(\w+)=\"([^\"]*)\"", raw):
                if a[1] in SKIP_ATTRS:
                    continue
                for m in re.finditer(r"-?\d+(?:\.\d+)?(?:e-?\d+)?", a[2]):
                    out.append((n, a.start(2) + m.start(), a.start(2) + m.end(), m[0]))
    return [x for x in out if float(x[3]) != 0]


def fork(source: str, row: int, i0: int, i1: int, value: float) -> str:
    lines = source.splitlines(keepends=True)
    raw = lines[row - 1]
    text = f"{value:.4g}"
    lines[row - 1] = raw[:i0] + text + raw[i1:]
    return "".join(lines)


def _one_fork(job: tuple) -> dict:
    src, fmt, library, seconds, line, value, strict = job
    fw = build(src, fmt, library, seconds)
    if fw.run is None:
        return {"value": value, "builds": False}
    fv = assess(line, Story(fw), strict)
    return {"value": value, "builds": True, "ok": fv.ok, "miss": fv.miss, "words": fv.miss_words, "lost": fv.t_lost}


def try_forks(w: World, v: Verdict, rows: list[int], seconds: float, first_rows: list[int] | None = None,
              strict: bool = False) -> dict:
    """Each number on these lines changed to each of FACTORS, one at a time, and the world run again (in parallel)."""
    t0 = time.monotonic()
    nums = numbers(w.source, rows, w.fmt)
    first = set(first_rows or [])
    nums = sorted(nums, key=lambda x: x[0] not in first)[: MAX_FORKS // len(FACTORS)]
    jobs = [(fork(w.source, row, i0, i1, float(text) * f), w.fmt, w.library, seconds, v.line, f"{float(text) * f:.4g}", strict)
            for row, i0, i1, text in nums for f in FACTORS]
    with ProcessPoolExecutor(max_workers=os.cpu_count() or 2) as pool:
        done = list(pool.map(_one_fork, jobs))
    out = []
    for k, (row, _, _, text) in enumerate(nums):
        tries = done[len(FACTORS) * k: len(FACTORS) * (k + 1)]
        moved = [abs(t["miss"] - v.miss) for t in tries if t.get("builds") and t["miss"] is not None and v.miss is not None]
        out.append({"row": row, "text": text, "tries": tries, "moves": max(moved) if moved else 0.0,
                    "fixes": any(t.get("ok") for t in tries)})
    out.sort(key=lambda r: (not r["fixes"], -r["moves"]))
    return {"forks": len(jobs), "skipped": len(numbers(w.source, rows, w.fmt)) - len(nums), "seconds": round(time.monotonic() - t0, 1), "rows": out}


# ---- the error ------------------------------------------------------------------------------------------------

def _src(source: str, rows: list[int]) -> list[str]:
    lines = source.splitlines()
    out, last = [], None
    for n in rows:
        if last is not None and n > last + 1:
            out.append("    ...")
        out.append(f"  {n:3}| {lines[n - 1]}")
        last = n
    return out


def expect_rows(source: str, fmt: str, line: str) -> int | None:
    for n, raw in enumerate(source.splitlines(), 1):
        if raw.strip().rstrip(".").lower() == line.strip().rstrip(".").lower():
            return n
    return None


def error(s: Story, v: Verdict, seconds: float = SECONDS, forks: bool = True, strict: bool = False) -> tuple[str, dict]:
    """One failed expectation as an error an agent reads: what, when it was lost, how, where, and what moves it."""
    w, run = s.w, s.run
    title = re.sub(r"\s+", " ", v.line.strip().rstrip(".")).upper()
    row = expect_rows(w.source, w.fmt, v.line)
    where = f"line {row}" if row else "expectation"
    out = [f"-- NOT TRUE: {title} {'-' * max(4, 66 - len(title) - len(where))} {where}", "",
           "You expected:", "", f"  {row:3}| {v.line.strip()}" if row else f"      {v.line.strip()}", "",
           f"but in the run, {v.evidence}.", ""]
    info = {"line": v.line, "t_lost": v.t_lost, "miss": v.miss}
    if v.subject is None or v.t_lost is None:
        return "\n".join(out), info
    subject = s.name.get(v.subject, s.m.body(v.subject).name)
    out += [f"It was lost at {v.t_lost:.2f} s, when {v.lost}." + (
        f" It came to rest {v.t_decided - v.t_lost:.2f} s later; the run after {v.t_lost:.2f} s only carried it there."
        if v.t_decided is not None and v.t_decided - v.t_lost > 0.05 else ""), ""]

    h = s.cone(v.subject, v.t_lost)
    for o in v.others:
        for b, t in s.cone(o, v.t_lost).items():
            h[b] = max(h.get(b, -1), t)
    reach = ", ".join(f"{s.name[b]} up to {t:.2f} s" for b, t in sorted(h.items(), key=lambda x: -x[1]) if b in s.moving)
    ev = [e for e in s.events() if e["t"] <= v.t_lost + 1e-9 and
          any(s.body_of.get(x) in h and e["t"] <= h[s.body_of[x]] + 1e-9 for x in e["who"])]
    shown = ev if len(ev) <= MAX_CHAIN else ev[:4] + [None] + ev[-(MAX_CHAIN - 4):]
    out += [f"How it got there. Only what touched {subject} can have changed it, so this walks back through touch "
            f"from {v.t_lost:.2f} s ({reach}); anything outside that is left out:", ""]
    if not shown:
        out.append(f"  Nothing touched {subject} before then.")
    for e in shown:
        if e is None:
            out.append(f"     ...  {len(ev) - MAX_CHAIN} more touches")
            continue
        mover = next((s.body_of[x] for x in e["who"] if s.body_of.get(x) in s.moving), None)
        state = f"   ({s.where(mover, s.i(e['t']))})" if mover is not None else ""
        out.append(f"  {e['t']:5.2f} s  {e['text']}{state}")
    out.append("")

    names = {lab for lab, b in s.body_of.items() if b in h and b in s.moving}
    for e in ev:
        names.update(e["who"])
    names.add(v.target) if v.target and not v.target.startswith("its ") else None
    names.discard("floor")
    rows = lines_for(s, names)
    info.update(cone=sorted(s.name[b] for b in h if b in s.moving), rows=rows, events=len(ev))
    if rows:
        out += ["These lines set up everything above:", ""] + _src(w.source, rows) + [""]
    if forks and rows and v.miss is not None:
        movers = {lab for lab, b in s.body_of.items() if b in h and b in s.moving}
        f = try_forks(w, v, rows, seconds, lines_for(s, movers), strict)
        info["forks"] = f
        top = [r for r in f["rows"] if r["moves"] > 0.005 or r["fixes"]][:TOP]
        if top:
            out += [f"Which numbers move it. Now {subject} {v.miss_words}. I ran the world again with each of the "
                    f"{len(f['rows'])} numbers on those lines changed alone to "
                    f"{', '.join(f'{x:g}' for x in FACTORS)} times itself ({f['forks']} runs, {f['seconds']:.0f} s"
                    + (f"; {f['skipped']} numbers on fixed things left unforked" if f["skipped"] else "")
                    + "). These moved it most, the ones that make it hold first:", ""]
            lines = w.source.splitlines()
            for r in top:
                tries = "; ".join(
                    (f"{t['value']}: does not build" if not t["builds"] else
                     f"{t['value']}: {'HOLDS' if t['ok'] else t['words']}") for t in r["tries"])
                out.append(f"  {r['row']:3}| {lines[r['row'] - 1].strip()}")
                out.append(f"       {r['text']} -> {tries}")
            out += ["", "Each fork changes one number and leaves the rest; two changes together can behave differently."]
        else:
            out += [f"None of the {len(f['rows'])} numbers on those lines moved it when changed alone to "
                    f"{', '.join(f'{x:g}' for x in FACTORS)} times itself ({f['forks']} runs): the cause is a bigger "
                    f"change, two numbers together, or something not written on them."]
        out.append("")
    return "\n".join(out), info


def explain(source: str, fmt: str, lines: list[str], library: str | None = None, seconds: float = SECONDS,
            forks: bool = True, strict: bool = False) -> tuple[str, list[dict]]:
    """Every expectation checked against the run; each one that fails gets an error with its why."""
    w = build(source, fmt, library, seconds)
    if w.run is None:
        return w.problem or "The world did not run.", []
    s = Story(w)
    verdicts = [assess(x, s, strict) for x in lines if x.strip()]
    if strict:  # 1h's hidden tests also want the lines to happen in order
        from hundred.hidden import judge, one as hidden_one
        j = judge([v.line for v in verdicts], w.run, w.owner)
        last = None
        for v in verdicts:
            ok_, t, _ = hidden_one(v.line, w.run, w.owner)
            if v.ok and not j["checks"].get(v.line, True):
                v.ok, v.evidence, v.miss = False, j["evidence"][v.line], None
                v.t_lost = t
                v.lost = f"`{v.line.strip()}` happened at {t:.2f} s, before `{last[0].strip()}` at {last[1]:.2f} s"
            if ok_ and t is not None:
                last = (v.line, t)
    held = sum(v.ok for v in verdicts)
    out = [f"{held} of {len(verdicts)} expectations hold in a {float(w.run.times[-1]):.0f} s run."
           + (f" {w.run.diverged}." if w.run.diverged else ""), ""]
    out += [f"- holds: {v.line.strip()} ({v.evidence})" for v in verdicts if v.ok]
    infos = []
    for v in verdicts:
        if not v.ok:
            text, info = error(s, v, seconds, forks, strict)
            out += ["", text]
            infos.append(info)
    return "\n".join(out).rstrip() + "\n", infos
