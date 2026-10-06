"""The spacetime debugger's recorder: a run's whole history, in the parts' own words, for a person and an agent alike.

A run is a pure function of the world, so the world text is the whole history: running it again gives the same
run to the step. This module runs a world once and keeps everything a debugger needs to move through it:

    h = record("weak spring", text)
    h["frames"]       # every moving part's state, 50 times a second, in numbers and in words
    h["events"]       # what happened, in order: touches, leaves, highest points, stops, rests
    h["expects"]      # each `expect` line, whether it held, and the moment that shows it
    h["cones"]        # for each expect, everything that could have caused its outcome (its past light cone)
    compare(a, b)     # two forks of one world: where they part, and which events moved or changed

The light cone is the debugger's answer to "why". Influence travels only through touch: a part can only have been
changed by what it touched, and those parts only by what they touched earlier. So starting from the moment an
expectation is decided, walk back through the contacts and keep every event inside that cone. Something fixed
(the floor, the stand) stops the walk: it never moves, so it carries no news from one part to another.

    python -m typed.spacetime       # writes typed/spacetime_output.md and the page, typed/spacetime.html
"""

from __future__ import annotations

import json
import math
import re
import time
from pathlib import Path

import mujoco
import numpy as np

from typed.compiler import render
from typed.lang import compile_program, expectations, parse
from typed.replay import REST, Trace
from worlds import tests
from worlds.viewer import geoms, motion

HERE = Path(__file__).parent
SECONDS = 6.0
FPS = 50
GAP = 0.03  # s: a touch that breaks for less than this is one touch (bounces and contact chatter)
APART = {"hinge": 0.5, "free": 0.005}  # deg, m: two forks have parted once a part differs by more than this


def _r(x, n=3):
    return round(float(x), n)


def lines(text: str) -> list[str]:
    return text.rstrip("\n").split("\n")


class Recorder:
    def __init__(self, compiled, run: tests.Run):
        self.c, self.run, self.m = compiled, run, run.model
        m = self.m
        self.label = {g: compiled.owner.get(m.geom(g).name, m.geom(g).name) for g in range(m.ngeom)}
        self.movers = []  # {"part", "kind", "body", "adr" (qpos), "vadr" (qvel), "range"}
        for j in compiled.joints:
            if j["kind"] == "free":
                b = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, j["name"].split(" ")[0])
                jid = tests.free_joint(m, b)
            else:
                jid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, j["name"])
                b = int(m.jnt_bodyid[jid])
            self.movers.append({"part": j["part"], "kind": j["kind"], "body": int(b), "adr": int(m.jnt_qposadr[jid]),
                                "vadr": int(m.jnt_dofadr[jid]),
                                "range": [v.deg for v in j["range"]] if j.get("range") else None})
        self.moving = {mv["body"] for mv in self.movers}
        self.body_of = {}  # label -> body
        for g, lab in self.label.items():
            self.body_of.setdefault(lab, int(m.geom_bodyid[g]))
        self.part_of_body = {mv["body"]: mv["part"] for mv in self.movers}
        self.intervals = self._intervals()

    # ---- state ------------------------------------------------------------------------------------------
    def touching(self, i: int, body: int) -> list[str]:
        out = set()
        for a, b in self.run.contacts[i]:
            ba, bb = self.m.geom_bodyid[a], self.m.geom_bodyid[b]
            if ba == bb:
                continue
            if ba == body:
                out.add(self.label[b])
            elif bb == body:
                out.add(self.label[a])
        return sorted(out)

    def state(self, i: int) -> dict:
        run, out = self.run, {}
        for mv in self.movers:
            touch = self.touching(i, mv["body"])
            if mv["kind"] == "free":
                p = run.xpos[i, mv["body"]]
                v = run.qvel[i, mv["vadr"]: mv["vadr"] + 3]
                speed = float(np.linalg.norm(v))
                climb = math.degrees(math.atan2(v[2], math.hypot(v[0], v[1]))) if speed > REST else 0.0
                words = f"{p[0]:.2f} m along, {p[2]:.2f} m up, " + (
                    f"{speed:.2f} m/s heading {climb:+.0f}°" if speed > REST else "at rest")
                out[mv["part"]] = {"x": _r(p[0]), "y": _r(p[1]), "z": _r(p[2]), "speed": _r(speed, 2),
                                   "heading": _r(climb, 0), "touching": touch,
                                   "words": words + (", touching " + " and ".join(touch) if touch else ", touching nothing")}
            else:
                a = math.degrees(run.qpos[i, mv["adr"]])
                w = math.degrees(run.qvel[i, mv["vadr"]])
                stop = ""
                if mv["range"]:
                    lo, hi = mv["range"]
                    stop = " at its lower stop" if abs(a - lo) < 0.5 else " at its upper stop" if abs(a - hi) < 0.5 else ""
                turning = f"turning {abs(w):.0f}°/s {'up' if w > 0 else 'down'}" if abs(w) > 1 else "still"
                out[mv["part"]] = {"angle": _r(a, 1), "rate": _r(w, 0), "touching": touch,
                                   "words": f"{a:.0f}°{stop}, {turning}"
                                   + (", touching " + " and ".join(touch) if touch else "")}
        return out

    # ---- contacts as intervals --------------------------------------------------------------------------
    def _intervals(self) -> list[dict]:
        """Every stretch of time two parts (pieces, by label) were touching, gaps under GAP closed."""
        run, m = self.run, self.m
        spans: dict[tuple, list] = {}
        for i, pairs in enumerate(run.contacts):
            seen = set()
            for a, b in pairs:
                if m.geom_bodyid[a] == m.geom_bodyid[b]:
                    continue
                la, lb = self.label[a], self.label[b]
                if la == lb:
                    continue
                key = tuple(sorted((la, lb), key=self._order))
                if key in seen:
                    continue
                seen.add(key)
                s = spans.setdefault(key, [])
                t = run.times[i]
                if s and t - s[-1][1] <= GAP:
                    s[-1][1] = t
                else:
                    s.append([t, t])
        out = []
        for (a, b), s in spans.items():
            for t0, t1 in s:
                out.append({"a": a, "b": b, "t0": _r(t0), "t1": _r(t1), "open": bool(t1 >= run.times[-1] - 1e-9)})
        return sorted(out, key=lambda x: (x["t0"], x["a"], x["b"]))

    def _order(self, lab: str):
        """Moving things first, then fixed ones, the floor last: 'ball first touches floor', not the reverse."""
        b = self.body_of.get(lab, 0)
        return (lab.lower() == "floor", b not in self.moving, lab)

    # ---- events -----------------------------------------------------------------------------------------
    def events(self, trace_events: list[str]) -> list[dict]:
        run, ev = self.run, []
        firsts = set()
        for iv in self.intervals:
            key = (iv["a"], iv["b"])
            if iv["t0"] <= 0:
                ev.append({"t": 0.0, "kind": "touch", "who": [iv["a"], iv["b"]],
                           "text": f"{iv['a']} starts against {iv['b']}"})
            else:
                again = key in firsts
                ev.append({"t": iv["t0"], "kind": "touch", "who": [iv["a"], iv["b"]],
                           "text": f"{iv['a']} {'touches' if again else 'first touches'} {iv['b']}{' again' if again else ''}"})
            firsts.add(key)
            if not iv["open"]:
                ev.append({"t": iv["t1"], "kind": "leave", "who": [iv["a"], iv["b"]],
                           "text": f"{iv['a']} leaves {iv['b']}"})
        # The highest point of each flight: a loose thing touching nothing for a while.
        for mv in self.movers:
            if mv["kind"] != "free":
                continue
            free = np.array([not self.touching(i, mv["body"]) for i in range(len(run.times))])
            i = 0
            while i < len(free):
                if not free[i]:
                    i += 1
                    continue
                j = i
                while j < len(free) and free[j]:
                    j += 1
                if run.times[j - 1] - run.times[i] > 0.1:
                    z = run.xpos[i:j, mv["body"], 2]
                    k = i + int(np.argmax(z))
                    if i < k < j - 1:
                        p = run.xpos[k, mv["body"]]
                        ev.append({"t": _r(run.times[k]), "kind": "apex", "who": [mv["part"]],
                                   "text": f"{mv['part']} is at its highest, {p[2]:.2f} m up, {p[0]:.2f} m along"})
                i = j
        # Stops, rings and rests, worded exactly as the replay says them (expect lines are checked against those).
        for line in trace_events:
            t, text = line.split("  ", 1)
            if " first touches " in text:
                continue
            kind = "stop" if " stop " in text else "rest" if "comes to rest" in text or "still moving" in text else "ring"
            who = [mv["part"] for mv in self.movers if text.startswith(mv["part"] + " ")]
            ev.append({"t": _r(float(t.strip().split()[0])), "kind": kind, "who": who, "text": text})
        ev.sort(key=lambda e: (e["t"], e["kind"] == "leave"))
        for e in ev:
            e["i"] = self.step(e["t"])
            s = self.state(e["i"])
            e["state"] = {p: s[p]["words"] for p in e["who"] if p in s}
        return ev

    def step(self, t: float) -> int:
        return int(np.clip(np.searchsorted(self.run.times, t - 1e-9), 0, len(self.run.times) - 1))

    # ---- why: the past light cone of a moment ------------------------------------------------------------
    def cone(self, label: str, t: float) -> dict[int, float]:
        """How late each body could still have influenced `label` at time t, through touch alone: its light cone.
        The same walk runs in the page (spacetime_template.html, cone()), so the two always agree."""
        horizon = {self.body_of.get(label, 0): t}
        changed = True
        while changed:
            changed = False
            for iv in self.intervals:
                ba, bb = self.body_of[iv["a"]], self.body_of[iv["b"]]
                for src, dst in ((ba, bb), (bb, ba)):
                    if src in horizon and src in self.moving and iv["t0"] <= horizon[src]:
                        h = min(iv["t1"], horizon[src])
                        if h > horizon.get(dst, -1):
                            horizon[dst] = h
                            changed = True
        return horizon

    def why(self, events: list[dict], label: str, t: float) -> tuple[dict[str, float], list[dict]]:
        """The events inside the light cone of (label, t), latest first, and how far back each moving part reaches."""
        h = self.cone(label, t)
        inside = lambda e: any(self.body_of.get(w) in h and e["t"] <= h[self.body_of[w]] + 1e-9 for w in e["who"])
        chain = [e for e in reversed(events) if e["t"] <= t + 1e-9 and inside(e) and not (e["kind"] == "touch" and e["t"] <= 0)]
        reach = {self.part_of_body[b]: _r(x) for b, x in h.items() if b in self.moving}
        return reach, chain


def record(name: str, text: str, note: str = "", seconds: float = SECONDS) -> dict:
    prog = parse(text)
    c = compile_program(prog)
    out = {"name": name, "note": note, "source": lines(text)}
    if c.problems:
        out.update(built=False, problems=render(c.problems).rstrip())
        return out
    run = tests.run(c.xml, seconds)
    trace = Trace(c, run)
    rec = Recorder(c, run)
    tev = trace.events()
    events = rec.events(tev)
    stride = max(1, round(1 / FPS / run.model.opt.timestep))
    idx = list(range(0, len(run.times), stride))
    frames = [{"t": _r(run.times[i]), "parts": rec.state(i)} for i in idx]

    expects = []
    for (n, line), (_, ok, evidence) in zip(prog.expect, expectations(prog, tev)):
        hit = next((e for e in events if e["text"].lower() == evidence.lower()), None)
        subject = line.split()[0]
        part = next((mv["part"] for mv in rec.movers if mv["part"] == subject or mv["part"].startswith(subject + ".")), subject)
        t = hit["t"] if hit else float(run.times[-1])
        cone, why = rec.why(events, part, t)
        expects.append({"line": line, "row": n, "ok": ok, "evidence": evidence, "t": t, "cone": cone,
                        "why": [{"t": e["t"], "text": e["text"], "state": e["state"]} for e in why]})

    g, _ = geoms(run.model)
    out.update(built=True, parts=[{"part": mv["part"], "kind": mv["kind"], "range": mv["range"]} for mv in rec.movers],
               frames=frames, events=events, intervals=rec.intervals, expects=expects,
               end=_r(run.times[-1]), geoms=g, anim=motion(run), body_of=rec.body_of, moving=sorted(rec.moving),
               part_of_body={str(b): p for b, p in rec.part_of_body.items()},
               containers=[{"name": n, "x0": _r(x0), "x1": _r(x1)} for n, (x0, x1, _, _) in c.containers],
               _run=run, _rec=rec)
    return out


# ---- forks ----------------------------------------------------------------------------------------------
def _key(text: str) -> str:
    """An event with its numbers taken out, so the same happening in two forks can be matched."""
    text = re.sub(r"\(?-?\d+(\.\d+)?( m/s| m| deg|°|%| cm)?\)?", "#", text)
    return re.sub(r"(# )?(short of|past|inside) .*$", "rest-place", text).strip()


def compare(a: dict, b: dict) -> dict:
    """Where fork b parts from run a, and what happened differently: events moved, changed, gone or new."""
    if not (a.get("built") and b.get("built")):
        return {"parted": None, "events": [], "summary": "One of the two does not build, so there is no run to compare."}
    ra, rb, reca = a["_run"], b["_run"], a["_rec"]
    n = min(len(ra.times), len(rb.times))
    parted, where = None, ""
    for mv in reca.movers:
        if mv["kind"] == "hinge":
            d = np.degrees(np.abs(ra.qpos[:n, mv["adr"]] - rb.qpos[:n, mv["adr"]]))
        else:
            d = np.linalg.norm(ra.xpos[:n, mv["body"]] - rb.xpos[:n, mv["body"]], axis=1)
        hit = np.nonzero(d > APART[mv["kind"]])[0]
        if len(hit) and (parted is None or ra.times[hit[0]] < parted):
            i = int(hit[0])
            parted = float(ra.times[i])
            gap = f"{d[i]:.1f}°" if mv["kind"] == "hinge" else f"{d[i] * 1000:.0f} mm"
            where = f"{mv['part']} is {gap} from where it is in the {a['name'].lower()} run"
    # Match events by what happened (numbers aside), in order of occurrence.
    pool: dict[str, list] = {}
    for e in b["events"]:
        pool.setdefault(_key(e["text"]), []).append(e)
    rows = []
    for e in a["events"]:
        k = _key(e["text"])
        if pool.get(k):
            f = pool[k].pop(0)
            dt = f["t"] - e["t"]
            if e["text"] == f["text"] and abs(dt) < 0.011:
                kind = "same"
            elif e["text"] == f["text"]:
                kind = "moved"
            else:
                kind = "changed"
            rows.append({"kind": kind, "a": e["text"], "ta": e["t"], "b": f["text"], "tb": f["t"], "dt": _r(dt)})
        else:
            rows.append({"kind": "gone", "a": e["text"], "ta": e["t"], "b": None, "tb": None, "dt": None})
    for k, left in pool.items():
        for f in left:
            rows.append({"kind": "new", "a": None, "ta": None, "b": f["text"], "tb": f["t"], "dt": None})
    rows.sort(key=lambda r: r["ta"] if r["ta"] is not None else r["tb"])
    ea = [x["ok"] for x in a["expects"]]
    eb = [x["ok"] for x in b["expects"]]
    summary = (f"The runs stay within 5 mm and 0.5° of each other until {parted:.2f} s, when {where}." if parted and parted > 0.01 else
               f"The runs differ from the first steps: {where}." if parted is not None else
               "The two runs are the same throughout.")
    if ea != eb:
        summary += " In the fork, " + "; ".join(f"`{x['line']}` {'holds' if y['ok'] else 'fails'}"
                                   for x, y in zip(a["expects"], b["expects"]) if x["ok"] != y["ok"]) + "."
    return {"parted": _r(parted) if parted is not None else None, "where": where, "events": rows, "summary": summary}


def edit(text: str, old: str, new: str) -> str:
    assert old in text, old
    return text.replace(old, new, 1)


BASE = (HERE / "worlds" / "catapult.world").read_text()
WEAK = edit(BASE, "spring        3 N·m/rad", "spring        2 N·m/rad")

RUNS = [  # (id, name, note, text)
    ("weak", "Weak spring", "1d's catapult break: the spring at 2 N·m/rad instead of 3.", WEAK),
    ("original", "Spring as 1d wrote it", "Fork: the spring back at 3 N·m/rad, as in the 1d brief.", BASE),
    ("mid", "Spring 2.5", "Fork: halfway, 2.5 N·m/rad.", edit(BASE, "spring        3 N·m/rad", "spring        2.5 N·m/rad")),
    ("nearer", "Bucket 20 cm nearer", "Fork: weak spring kept, the bucket moved 20 cm toward the catapult.",
     edit(WEAK, "2.92 m beyond ball", "2.72 m beyond ball")),
    ("unitless", "Spring with no unit", "Fork: the weak spring written as a bare 2. It never runs.",
     edit(BASE, "spring        3 N·m/rad", "spring        2")),
]
SWEEP = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0]


def sweep() -> list[dict]:
    """The weak world forked along one line: where the ball rests for each spring stiffness."""
    out = []
    for k in SWEEP:
        h = record(f"spring {k}", edit(BASE, "spring        3 N·m/rad", f"spring        {k:g} N·m/rad"))
        rest = next((e for e in h["events"] if e["kind"] == "rest" and e["who"] == ["ball"]), None)
        last = h["frames"][-1]["parts"]["ball"]
        left = max(e["t"] for e in h["events"] if e["kind"] == "leave" and e["who"][1].startswith("catapult.scoop"))
        land = next(e for e in h["events"] if e["kind"] == "touch" and e["t"] > left and e["who"][0] == "ball")
        lx = h["frames"][round(land["t"] * FPS)]["parts"]["ball"]["x"]
        out.append({"spring": k, "x": last["x"], "z": last["z"], "ok": h["expects"][0]["ok"],
                    "text": rest["text"] if rest else "", "land": land["text"], "land_t": land["t"], "land_x": lx})
    return out


def public(h: dict) -> dict:
    return {k: v for k, v in h.items() if not k.startswith("_")}


def history_md(h: dict, base: dict | None = None, diff: dict | None = None) -> list[str]:
    """One run as an agent (or a person) reads it: the world, what happened, what was expected, and why."""
    out = [f"## {h['name']}", "", h["note"], ""]
    if base is not None:
        changed = [(i + 1, a, b) for i, (a, b) in enumerate(zip(base["source"], h["source"])) if a != b]
        out += [f"Edited line {n}: `{a.strip()}` became `{b.strip()}`" for n, a, b in changed] + [""]
    else:
        out += ["```", *[f"{i + 1:3}  {s}" for i, s in enumerate(h["source"])], "```", ""]
    if not h["built"]:
        return out + ["Before time starts: the world does not build, so there is no run.", "", "```", h["problems"], "```", ""]
    out += ["### What happened", "", "| t | event | state then |", "|---|---|---|"]
    for e in h["events"]:
        out.append(f"| {e['t']:.2f} s | {e['text']} | {'; '.join(f'{p}: {w}' for p, w in e['state'].items())} |")
    out += ["", "### Expected", ""]
    for x in h["expects"]:
        out.append(f"- {'✓ holds' if x['ok'] else '✗ fails'}: `{x['line']}` (line {x['row']}). {x['evidence']}, at {x['t']:.2f} s.")
        if not x["ok"]:
            reach = ", ".join(f"{p} up to {t:.2f} s" for p, t in x["cone"].items())
            out += ["", f"  Why, walking back from {x['t']:.2f} s through touch alone ({reach}):", ""]
            out += [f"  - {e['t']:.2f} s  {e['text']}" + (f"  ({'; '.join(e['state'].values())})" if e["state"] else "")
                    for e in x["why"]]
    if diff:
        out += ["", f"### Against the {base['name'].lower()} run", "", diff["summary"], ""]
        moved = [r for r in diff["events"] if r["kind"] != "same"]
        out += [f"- {r['kind']}: " + (f"{r['a']} ({r['ta']:.2f} s)" if r["a"] else "") +
                (" → " if r["a"] and r["b"] else "") + (f"{r['b']} ({r['tb']:.2f} s)" if r["b"] else "") for r in moved]
    return out + [""]


def main() -> None:
    runs = {rid: dict(record(name, text, note), id=rid) for rid, name, note, text in RUNS}
    weak = runs["weak"]
    diffs = {f"{x}|{y}": compare(runs[x], runs[y]) for x in runs for y in runs if x != y}
    sw = sweep()
    wall = weak["containers"][0]
    md = ["# Spacetime debugger: the weak-spring catapult", "",
          "Generated by `python -m typed.spacetime`. No model calls. Each run below is a pure function of its world "
          "text: running it again gives the same history to the step. Events are worded in the parts' own names; "
          "`why` walks back from the moment an expectation was decided, through touch alone.", ""]
    md += history_md(weak)
    for rid, h in runs.items():
        if rid != "weak":
            md += history_md(h, weak, diffs[f"weak|{rid}"])
    md += ["## One line, many forks: the spring swept", "",
           f"The {wall['name']} spans {wall['x0']:.2f} to {wall['x1']:.2f} m along. Where the ball first hits something after "
           "leaving the scoop, and where it ends up:", "", "| spring | first hits | ball rests | holds |", "|---|---|---|---|"]
    md += [f"| {s['spring']:g} N·m/rad | {s['land'].removeprefix('ball ')} at {s['land_t']:.2f} s, {s['land_x']:.2f} m along "
           f"| {s['text'].removeprefix('ball comes to rest ').removeprefix('ball ')} | {'✓' if s['ok'] else '✗'} |" for s in sw]
    history = "\n".join(md) + "\n"
    (HERE / "spacetime_output.md").write_text(history)
    data = {"runs": [public(runs[rid]) for rid, *_ in RUNS], "diffs": diffs, "sweep": sw, "fps": FPS,
            "history": history, "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}
    page = (HERE / "spacetime_template.html").read_text()
    blob = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    (HERE / "spacetime.html").write_text(page.replace("/*__DATA__*/null", blob))
    print(history)


if __name__ == "__main__":
    main()
