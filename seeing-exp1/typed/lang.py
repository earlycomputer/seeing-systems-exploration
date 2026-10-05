"""A world language: plain lines, indentation instead of brackets, units written into the numbers, and positions
said as relations. It parses into the typed parts (parts.py), so every check and test carries over.

    world  pendulum strikes ball

    pendulum
      hangs from  1.01 m up
      length      95 cm
      ...

    expect
      pendulum.bob touches ball
      ball comes to rest in cup

A part starts at the left margin with its name; its lines are indented under it. Each line is one fact: a key
(`length`, `hangs from`, `bob`) and a value made of clauses split by commas (`sphere 5 cm, 1 kg`). A number
that needs a unit must carry one. `expect` lists what should happen, in the replay's own words.
"""

from __future__ import annotations

import difflib
import math
import re
from dataclasses import dataclass, field

from typed import parts as P
from typed.compiler import Problem
from typed import units as U

# ---- numbers with units -------------------------------------------------------------------------------

UNITS = {  # written unit -> (kind, factor to SI)
    "mm": ("length", 0.001), "cm": ("length", 0.01), "m": ("length", 1.0),
    "g": ("mass", 0.001), "kg": ("mass", 1.0),
    "°": ("angle", math.pi / 180), "deg": ("angle", math.pi / 180), "rad": ("angle", 1.0),
    "m/s": ("speed", 1.0), "rad/s": ("spin", 1.0),
    "N·m/rad": ("torsional stiffness", 1.0), "Nm/rad": ("torsional stiffness", 1.0),
    "N·m·s/rad": ("torsional damping", 1.0), "Nms/rad": ("torsional damping", 1.0),
    "kg/m³": ("density", 1.0), "kg/m3": ("density", 1.0),
}
QTYPE = {"length": U.Length, "mass": U.Mass, "angle": U.Angle, "speed": U.Speed, "spin": U.Spin,
         "torsional stiffness": U.TorsionStiffness, "torsional damping": U.TorsionDamping, "density": U.Density}
EXAMPLE = {"length": "5 cm or 1.2 m", "mass": "200 g or 1 kg", "angle": "63° or 1.1 rad", "speed": "3 m/s",
           "spin": "4 rad/s", "torsional stiffness": "40 N·m/rad", "torsional damping": "25 N·m·s/rad",
           "density": "1.2 kg/m³"}
NUM = r"-?\d+(?:\.\d+)?"
QTY = re.compile(rf"({NUM})\s*({'|'.join(sorted(map(re.escape, UNITS), key=len, reverse=True))})?(?![\w/·³])")


class Bad(Exception):
    def __init__(self, problem: Problem):
        self.problem = problem


@dataclass
class Line:
    n: int
    text: str
    path: str  # "pendulum.length"

    def problem(self, code, found, expected, why, hint) -> Bad:
        return Bad(Problem(code, f"line {self.n}: {self.path}", found, expected, why, hint))


def an(kind: str) -> str:
    return f"{'an' if kind[0] in 'aeiou' else 'a'} {kind}"


def qty(text: str, kind: str, line: Line) -> U.Quantity:
    m = QTY.fullmatch(text.strip())
    if not m:
        raise line.problem("NOT A NUMBER", text.strip() or "(nothing)", f"{an(kind)}, like {EXAMPLE[kind]}", "",
                           f"write {EXAMPLE[kind]}")
    value, unit = float(m.group(1)), m.group(2)
    if unit is None:
        why = ("A bare number can't say whether it is degrees or radians, which is how a hinge range meant in "
               "radians became a 2.1 degree limit in experiment 1d." if kind == "angle"
               else f"A bare number has no unit, so nothing can check it is {an(kind)}.")
        raise line.problem(f"{kind.upper()} WITHOUT A UNIT", text.strip(), f"{an(kind)}, like {EXAMPLE[kind]}", why,
                           f"write {text.strip()} followed by its unit, like {EXAMPLE[kind]}")
    k, factor = UNITS[unit]
    if k != kind:
        raise line.problem("WRONG KIND OF QUANTITY", text.strip(), f"{an(kind)}, like {EXAMPLE[kind]}",
                           f"{unit} measures {k}, and this needs {an(kind)}.", f"write {EXAMPLE[kind]}")
    return QTYPE[kind](value * factor, text.strip())


def number(text: str, line: Line) -> float:
    if not re.fullmatch(NUM, text.strip()):
        raise line.problem("NOT A NUMBER", text.strip(), "a plain number, like 0.8", "", "write a plain number")
    return float(text)


def words(text: str, pattern: str, line: Line, expected: str, hint: str) -> re.Match:
    m = re.fullmatch(pattern, text.strip())
    if not m:
        raise line.problem("I CAN'T READ THIS", text.strip(), expected, "", hint)
    return m


# ---- positions as relations ---------------------------------------------------------------------------

def ref_x(part) -> float:
    for attr in ("at", "pivot_at", "rim_centre", "start", "hinge_at", "high"):
        if hasattr(part, attr):
            return getattr(part, attr).x.si
    return 0.0


@dataclass
class Place:
    on: str | None = None  # "floor" or a part
    inside: str | None = None
    x: float = 0.0
    y: float = 0.0
    z: float | None = None
    from_top: U.Length | None = None


def place(clauses: list[str], line: Line, known: dict) -> Place:
    p = Place()

    def part(name):
        if name in known and known[name] is None:
            raise Bad(None)  # that part already has its own problem: don't pile a second one on top
        if name not in known:
            close = difflib.get_close_matches(name, known, 1)
            raise line.problem("UNKNOWN PART", name, "the name of a part written above this line",
                               "A position can only refer to parts already written, so the world reads top to bottom.",
                               f"did you mean {close[0]}?" if close else "write that part first")
        return known[name]

    for c in clauses:
        c = c.strip()
        if m := re.fullmatch(r"(?:on|rests on|stands on|stand on) (?:the )?(\w+)", c):
            p.on = m.group(1)
            if p.on != "floor":
                part(p.on)
        elif m := re.fullmatch(r"(?:in|sits in) (?:the )?(\w+)", c):
            p.inside = m.group(1)
            part(p.inside)
        elif m := re.fullmatch(rf"(.+?) from the top", c):
            p.from_top = qty(m.group(1), "length", line)
        elif m := re.fullmatch(rf"(.+?) (beyond|ahead of|past|behind) (?:the )?(\w+)", c):
            d = qty(m.group(1), "length", line).si
            p.x = ref_x(part(m.group(3))) + (-d if m.group(2) == "behind" else d)
        elif m := re.fullmatch(r"(.+?) along", c):
            p.x = qty(m.group(1), "length", line).si
        elif m := re.fullmatch(r"(.+?) to the (left|right)", c):
            d = qty(m.group(1), "length", line).si
            p.y = d if m.group(2) == "left" else -d
        elif m := re.fullmatch(r"(.+?) up", c):
            p.z = qty(m.group(1), "length", line).si
        else:
            raise line.problem("I CAN'T READ THIS POSITION", c, "a place like `on floor`, `in catapult`, `1 m beyond "
                               "ball`, `2 m along`, `1.01 m up` or `12 cm from the top`", "", "use one of those")
    return p


# ---- the parts ----------------------------------------------------------------------------------------

def friction(clauses, line) -> P.Friction:
    vals = {"slide": None, "spinning": 0.005, "rolling": 0.0001}
    for i, c in enumerate(clauses):
        m = words(c, r"(?:(spinning|rolling) )?(\S+)", line, "friction like `0.8, rolling 0.002`", "")
        vals[m.group(1) or "slide"] = number(m.group(2), line)
    return P.Friction(vals["slide"], vals["spinning"], vals["rolling"])


def sphere(clauses, line) -> tuple[U.Length, U.Mass]:
    m = words(clauses[0], r"sphere (.+)", line, "`sphere 5 cm, 200 g`", "write `sphere <radius>, <mass>`")
    return qty(m.group(1), "length", line), qty(clauses[1], "mass", line)


def velocity(clauses, line) -> U.Velocity:
    v = {"along": 0.0, "across": 0.0, "up": 0.0}
    for c in clauses:
        m = words(c, r"(.+?) (along|across|up)", line, "`3.21 m/s along, 9.3 m/s up`", "")
        v[m.group(2)] = qty(m.group(1), "speed", line).si
    return U.v3(U.mps(v["along"]), U.mps(v["across"]), U.mps(v["up"]))


def build(kind: str, name: str, props: dict, known: dict):
    """props: key -> (clauses, Line). Returns a part."""
    def need(key):
        if key not in props:
            raise Bad(Problem("MISSING LINE", f"{name}", f"no `{key}` line", f"a `{key}` line under {name}",
                              f"A {kind} can't be built without it.", f"add `  {key} ...` under {name}"))
        return props[key]

    if kind == "floor":
        f = friction(*props["friction"]) if "friction" in props else None
        size = qty(props["size"][0][0], "length", props["size"][1]) if "size" in props else U.m(8)
        return P.Floor(friction=f, size=size)

    if kind == "ball":
        r, mass = sphere(*need("is a"))
        c, ln = need("rests") if "rests" in props else need("sits")
        pl = place(c, ln, known)
        if pl.inside:
            at = known[pl.inside].seat(r)
        elif pl.from_top is not None:
            at = known[pl.on].seat(r, along=pl.from_top)
        else:
            at = U.m3(pl.x, pl.y, pl.z if pl.z is not None else r.si)
        flags = props.get("is", ([], None))[0]
        return P.Ball(radius=r, mass=mass, at=at, name="ball",
                      launch=velocity(*props["launched"]) if "launched" in props else None,
                      friction=friction(*props["friction"]) if "friction" in props else None,
                      rolls="rolls" in flags, hollow="hollow" in flags, drag="slowed by air" in flags,
                      bounce="lively" if "lively" in flags else "dead" if "dead" in flags else None)

    if kind == "pusher":
        r, mass = sphere(*need("is a"))
        pl = place(*need("rests"), known)
        return P.Pusher(at=U.m3(pl.x, pl.y, r.si), radius=r, mass=mass, velocity=velocity(*need("launched")),
                        friction=friction(*props["friction"]) if "friction" in props else None)

    if kind == "hoop":
        pl = place(*need("rim"), known)
        return P.Hoop(rim_centre=U.m3(pl.x, pl.y, pl.z or 0.0))

    if kind == "ramp":
        hi, lo = place(*need("high end"), known), place(*need("low end"), known)
        c, ln = need("width")
        return P.Ramp(high=U.m3(hi.x, hi.y, hi.z or 0), low=U.m3(lo.x, lo.y, lo.z or 0), width=qty(c[0], "length", ln))

    if kind == "open box":
        c, ln = need("is an")
        m = words(c[0], r"open box (\S+) by (.+)", ln, "`open box 90 by 60 cm`", "write `open box <length> by <width>`")
        unit = QTY.fullmatch(m.group(2).strip())
        u = unit.group(2) if unit and unit.group(2) else ""
        length, width = qty(f"{m.group(1)} {u}", "length", ln), qty(m.group(2), "length", ln)
        opts = {"wall": U.m(0.02), "base": U.m(0.02), "lip": None, "walls": None}
        for cl in c[1:]:
            mm = words(cl, r"(walls|walls? thickness|base|low lip) (.+)", ln,
                       "`walls 30 cm`, `wall thickness 1 cm`, `base 1 cm` or `low lip 2.5 cm`", "")
            key = {"walls": "walls", "base": "base", "low lip": "lip"}.get(mm.group(1), "wall")
            opts[key] = qty(mm.group(2), "length", ln)
        if opts["walls"] is None:
            raise ln.problem("MISSING SIZE", ", ".join(c), "the height of the walls, like `walls 30 cm`",
                             "A cup with no walls is a plate.", "add `, walls <height>`")
        pl = place(*need("stands"), known)
        return P.OpenBox(name, at=U.m3(pl.x, pl.y, 0), length=length, width=width, wall_height=opts["walls"],
                         wall=opts["wall"], base=opts["base"], lip=opts["lip"])

    if kind == "door":
        c, ln = need("panel")
        w, h, t = (qty(x, "length", ln) for x in words(c[0], r"(.+) wide", ln, "`panel 90 cm wide, ...`", "").groups()
                   + words(c[1], r"(.+) tall", ln, "`196 cm tall`", "").groups()
                   + words(c[2], r"(.+) thick", ln, "`4 cm thick`", "").groups())
        mass = qty(c[3], "mass", ln)
        sc, sl = need("starts")
        opened = qty(words(sc[0], r"open (.+)", sl, "`open 69°`", "write `starts open <angle>`").group(1), "angle", sl)
        return P.Door(hinge_at=U.m3(0, 0, 0), width=w, height=h, thickness=t, mass=mass, hinge=hinge(props),
                      opened=opened)

    if kind == "catapult":
        c, ln = need("arm")
        pl = place(*need("pivot"), known)
        return P.Catapult(pivot_at=U.m3(pl.x, pl.y, pl.z or 0), arm_length=qty(c[0], "length", ln),
                          arm_mass=qty(c[1], "mass", ln), hinge=hinge(props))

    if kind == "stack":
        c, ln = need("is")
        m = words(c[0], r"(\d+) cubes of (.+)", ln, "`5 cubes of 20 cm, 500 g each`", "")
        mass = qty(c[1].removesuffix(" each"), "mass", ln)
        pl = place(*need("stands"), known)
        return P.Stack(at=U.m3(pl.x, pl.y, 0), count=int(m.group(1)), side=qty(m.group(2), "length", ln), mass=mass,
                       friction=friction(*props["friction"]) if "friction" in props else None)

    if kind == "dominoes":
        c, ln = need("are")
        m = words(c[0], r"(\d+) of (\S+) by (\S+) by (.+)", ln, "`10 of 2 by 8 by 16 cm`", "")
        u = QTY.fullmatch(m.group(4).strip()).group(2) or ""
        t, w, h = qty(f"{m.group(2)} {u}", "length", ln), qty(f"{m.group(3)} {u}", "length", ln), qty(m.group(4), "length", ln)
        mass = qty(c[1].removesuffix(" each"), "mass", ln)
        spacing = qty(words(c[2], r"(.+) apart", ln, "`10 cm apart`", "").group(1), "length", ln)
        pl = place(*need("stand"), known)
        tc, tl = need("first tipped at")
        return P.DominoRow(start=U.m3(pl.x, pl.y, 0), count=int(m.group(1)), spacing=spacing, thickness=t, width=w,
                           height=h, mass=mass, first_tip=qty(tc[0], "spin", tl))

    if kind == "pendulum":
        pl = place(*need("hangs from"), known)
        r, bm = sphere(*need("bob"))
        c, ln = need("rod")
        rod_r = qty(words(c[0], r"(.+) thick", ln, "`1 cm thick`", "").group(1), "length", ln)
        sc, sl = need("starts swung back")
        dc = props.get("damping")
        return P.Pendulum(pivot_at=U.m3(pl.x, pl.y, pl.z or 0), length=qty(need("length")[0][0], "length", need("length")[1]),
                          bob_radius=r, bob_mass=bm, rod_mass=qty(c[1], "mass", ln), rod_radius=U.Length(rod_r.si / 2, rod_r.written),
                          released_from=qty(sc[0], "angle", sl),
                          damping=qty(dc[0][0], "torsional damping", dc[1]) if dc else None)
    raise AssertionError(kind)


def hinge(props) -> P.Hinge:
    c, ln = props["turns"] if "turns" in props else props["swings"]
    m = words(c[0], r"about (x|y|z)", ln, "`about z`", "write `turns about x`, `y` or `z`")
    lo = hi = None
    for cl in c[1:]:
        r = words(cl, r"from (.+) to (.+)", ln, "`from 0° to 120°`", "")
        lo, hi = qty(r.group(1), "angle", ln), qty(r.group(2), "angle", ln)
    stiff = rest = damp = None
    if "spring" in props:
        sc, sl = props["spring"]
        s = words(sc[0], r"(.+) toward (.+)", sl, "`40 N·m/rad toward 0°`", "")
        stiff, rest = qty(s.group(1), "torsional stiffness", sl), qty(s.group(2), "angle", sl)
    if "damping" in props:
        damp = qty(props["damping"][0][0], "torsional damping", props["damping"][1])
    return P.Hinge(m.group(1), range=(lo, hi) if lo else None, stiffness=stiff, rest=rest, damping=damp)


KINDS = {  # a part's name picks its kind unless its first line says `is a ...`
    "floor": "floor", "ball": "ball", "pusher": "pusher", "hoop": "hoop", "ramp": "ramp", "cup": "open box",
    "bucket": "open box", "door": "door", "catapult": "catapult", "blocks": "stack", "stack": "stack",
    "dominoes": "dominoes", "pendulum": "pendulum",
}
KEYS = {  # the line keys each kind understands, longest first when matching
    "floor": ["friction", "size"],
    "ball": ["is a", "is", "rests", "sits", "launched", "friction"],
    "pusher": ["is a", "rests", "launched", "friction"],
    "hoop": ["rim"],
    "ramp": ["high end", "low end", "width"],
    "open box": ["is an", "stands"],
    "door": ["panel", "turns", "spring", "damping", "starts"],
    "catapult": ["pivot", "arm", "swings", "spring", "damping"],
    "stack": ["is", "stands", "friction"],
    "dominoes": ["are", "stand", "first tipped at"],
    "pendulum": ["hangs from", "length", "bob", "rod", "starts swung back", "damping"],
}


@dataclass
class Program:
    world: P.World | None
    expect: list[tuple[int, str]] = field(default_factory=list)
    problems: list[Problem] = field(default_factory=list)


def parse(text: str) -> Program:
    """Every problem at once where it can: each part is read on its own, so one bad line doesn't hide the rest."""
    prog = Program(None)
    sections: list[tuple[int, str, list[tuple[int, str]]]] = []
    name, air = "world", None
    for n, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.strip().startswith("--"):
            continue
        if not raw[0].isspace():
            head = raw.strip()
            if head.startswith("world"):
                name = head.removeprefix("world").strip().replace(" ", "_") or "world"
                continue
            if head.startswith("air"):
                try:
                    air = P.Air(density=qty(head.removeprefix("air").strip(), "density", Line(n, head, "air")))
                except Bad as b:
                    prog.problems.append(b.problem)
                continue
            sections.append((n, head, []))
        elif sections:
            sections[-1][2].append((n, raw.strip()))
        else:
            prog.problems.append(Problem("INDENTED TOO SOON", f"line {n}", raw.strip(), "a part's name at the margin first",
                                         "Indented lines belong to the part written above them.", "start with a part name"))
    known, parts = {}, []
    for n, head, body in sections:
        if head == "expect":
            prog.expect = body
            continue
        kind = KINDS.get(head)
        if kind is None:
            close = difflib.get_close_matches(head, KINDS, 1)
            prog.problems.append(Problem("I DON'T KNOW THIS KIND OF PART", f"line {n}", head,
                                         f"one of: {', '.join(sorted(KINDS))}", "",
                                         f"did you mean {close[0]}?" if close else "name the part by what it is"))
            continue
        props = {}
        try:
            for ln, txt in body:
                key = next((k for k in sorted(KEYS[kind], key=len, reverse=True) if txt == k or txt.startswith(k + " ")), None)
                if key is None:
                    word = txt.split()[0]
                    close = difflib.get_close_matches(word, KEYS[kind], 1)
                    raise Bad(Problem("I DON'T KNOW THIS LINE", f"line {ln}: {head}", txt,
                                      f"a {kind} line: {', '.join(KEYS[kind])}", "",
                                      f"did you mean `{close[0]}`?" if close else f"a {kind} understands those lines"))
                value = txt[len(key):].strip()
                clauses = [c.strip() for c in value.split(",")] if value else []
                if key == "is" and kind == "ball":  # flags: `is hollow, lively, slowed by air`
                    props.setdefault("is", ([], None))[0].extend(clauses)
                    continue
                props[key] = (clauses, Line(ln, txt, f"{head}.{key.replace(' ', '_')}"))
            part = build(kind, head, props, known)
            known[head] = part
            parts.append(part)
        except Bad as b:
            known[head] = None
            if b.problem:
                prog.problems.append(b.problem)
    if not prog.problems:
        prog.world = P.World(parts=parts, air=air, name=name)
    return prog


# ---- expect, checked against the replay -----------------------------------------------------------------

def expectations(prog: Program, events: list[str]) -> list[tuple[str, bool, str]]:
    """Each `expect` line with whether the run did it, and the event that shows it (or the nearest one)."""
    ev = [e.split("  ", 1)[1].lower() for e in events]
    out = []
    for n, line in prog.expect:
        s = line.lower()
        if m := re.fullmatch(r"([\w.]+) touches ([\w.]+)", s):
            a, b = m.groups()
            hits = [e for e in ev if "first touches" in e and a in e and b in e]
        elif m := re.fullmatch(r"([\w.]+) comes to rest in ([\w.]+)", s):
            a, b = m.groups()
            hits = [e for e in ev if e.startswith(a) and f"comes to rest inside {b}" in e]
        elif m := re.fullmatch(r"([\w.]+) drops through ([\w.]+)", s):
            hits = [e for e in ev if e.startswith(m.group(1)) and f"drops through {m.group(2)}" in e]
        elif m := re.fullmatch(r"([\w.]+) reaches its (lower|upper) stop", s):
            hits = [e for e in ev if m.group(1) in e and f"reaches its {m.group(2)} stop" in e]
        else:
            out.append((line, False, "I can't read this expectation"))
            continue
        subject = line.split()[0].lower()
        near = [e for e in ev if e.startswith(subject)]
        out.append((line, bool(hits), hits[0] if hits else (near[-1] if near else "nothing happened to it")))
    return out
