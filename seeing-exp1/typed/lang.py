"""The world language, decomposed: worlds and the parts they use are both written in it, down to primitives.

    world  catapult                          part catapult
                                               needs  pivot height
    catapult                                   ...
      is a          catapult                   stand
      pivot height  40 cm                        is a  box 16 by 24 by pivot height − 6 cm
      ...                                        on    floor
                                               arm
    ball                                         is a      box arm length by 6 by 4 cm, arm mass
      is a   sphere 6 cm radius, 150 g           its far end at pivot, level with pivot
      moves  freely                              turns on  catapult hinge, about y, at pivot
      sits   in catapult                       ...

Three ideas carry it:

- **Parts are named wholes made of pieces.** A part in library.world says what it needs and builds itself from
  primitives (box, cube, sphere, rod, plank, post, ring, point) or from other parts. A part has no code: nothing
  in Python knows what a catapult is.
- **Positions are relations, and one rule serves every part.** `sits in X` puts a thing on X's base, centred over
  it, whatever X is: a cup, a bucket or a catapult's scoop. `on`, `beyond`, `outside X's far end`, `centred on
  X's left side` and the rest work on any piece's extent, so the catapult never has to know a ball exists.
- **The world is a value and the run a pure function of it.** Pieces become MuJoCo bodies only at the end: what
  turns on a hinge, what moves freely, what is attached to what. The readback speaks in the pieces' paths
  (`pendulum.bob first touches ball`).

Numbers carry their units, and sums like `pivot height − 6 cm` are checked for kind. Every problem is reported
at the line that caused it, in the world file when a bad value was passed into a part.
"""

from __future__ import annotations

import copy as cp
import difflib
import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from typed import units as U
from typed.compiler import TIMESTEP, Compiled, Problem, check_meaning, check_overlaps

LIBRARY = Path(__file__).parent / "library.world"

# ---- numbers with units -------------------------------------------------------------------------------

UNITS = {  # written unit -> (kind, factor to SI)
    "mm": ("length", 0.001), "cm": ("length", 0.01), "m": ("length", 1.0),
    "g": ("mass", 0.001), "kg": ("mass", 1.0),
    "°": ("angle", math.pi / 180), "deg": ("angle", math.pi / 180), "rad": ("angle", 1.0),
    "m/s": ("speed", 1.0), "rad/s": ("spin", 1.0),
    "N·m/rad": ("torsional stiffness", 1.0), "Nm/rad": ("torsional stiffness", 1.0),
    "N·m·s/rad": ("torsional damping", 1.0), "Nms/rad": ("torsional damping", 1.0),
    "kg/m³": ("density", 1.0), "kg/m3": ("density", 1.0),
    "kg·m²": ("rotor inertia", 1.0), "kg m2": ("rotor inertia", 1.0),
}
QTYPE = {"length": U.Length, "mass": U.Mass, "angle": U.Angle, "speed": U.Speed, "spin": U.Spin,
         "torsional stiffness": U.TorsionStiffness, "torsional damping": U.TorsionDamping, "density": U.Density,
         "rotor inertia": U.RotorInertia}
EXAMPLE = {"length": "5 cm or 1.2 m", "mass": "200 g or 1 kg", "angle": "63° or 1.1 rad", "speed": "3 m/s",
           "spin": "4 rad/s", "torsional stiffness": "40 N·m/rad", "torsional damping": "25 N·m·s/rad",
           "density": "1.2 kg/m³", "rotor inertia": "0.01 kg·m²"}
NUM = r"-?\d+(?:\.\d+)?"
UNIT = "|".join(sorted(map(re.escape, UNITS), key=len, reverse=True))
QTY = re.compile(rf"({NUM})\s*({UNIT})?(?![\w/·³²])")
AXES = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}
COLOURS = {"orange": "0.9 0.3 0.05 1", "glass": "0.92 0.95 0.98 0.85", "black": "0.1 0.1 0.1 1",
           "grey": "0.25 0.25 0.3 1", "dark grey": "0.2 0.2 0.25 1", "wood": "0.6 0.45 0.3 1", "white": "0.95 0.95 0.95 1"}
CONVENTIONS = {"hoop_rim_": "rim_"}  # the 1d tests' own names, kept out of the language


class Bad(Exception):
    """A problem, or None when the cause has already been reported (so one mistake reports once)."""

    def __init__(self, problem: Problem | None):
        self.problem = problem


@dataclass
class Line:
    n: int
    text: str
    path: str  # "catapult.arm.swings"
    file: str = ""  # "" for the world, "library " for library.world
    subs: list = field(default_factory=list)  # (value text, Line in the world it came from)

    def problem(self, code, found, expected, why="", hint="") -> Bad:
        at = self
        for value, origin in self.subs:
            if found and (found in value or value in found):
                at = origin  # the bad value was written in the world, so point there
                break
        return Bad(Problem(code, f"{at.file}line {at.n}: {at.path}", found, expected, why, hint))


def an(kind: str) -> str:
    return f"{'an' if kind[0] in 'aeiou' else 'a'} {kind}"


def one_qty(text: str, kind: str, line: Line) -> float:
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
    return value * factor


def qty(text: str, kind: str, line: Line) -> U.Quantity:
    """A quantity, or a sum of them: `40 cm − 6 cm`. Every term must be the same kind."""
    text = text.strip()
    terms = re.split(r"\s+([+−])\s+", text)
    total, sign = 0.0, 1
    for i, t in enumerate(terms):
        if i % 2:
            sign = 1 if t == "+" else -1
        else:
            total += sign * one_qty(t, kind, line)
    return QTYPE[kind](total, text)


def number(text: str, line: Line) -> float:
    if not re.fullmatch(NUM, text.strip()):
        raise line.problem("NOT A NUMBER", text.strip(), "a plain number, like 0.8", "", "write a plain number")
    return float(text)


def dims(text: str, n: int, line: Line) -> list[float]:
    """`16 by 24 by 34 cm`: a bare number borrows the unit written at the end."""
    parts = [p.strip() for p in text.split(" by ")]
    if len(parts) != n:
        raise line.problem("WRONG NUMBER OF SIZES", text, f"{n} sizes joined by `by`, like "
                           + " by ".join(["10"] * (n - 1) + ["10 cm"]), "", "")
    tail = qty(parts[-1], "length", line).si  # read first: the unit the others borrow is written here
    unit = re.search(rf"({UNIT})$", parts[-1]).group(1)
    return [qty(p + (f" {unit}" if re.fullmatch(NUM, p) else ""), "length", line).si for p in parts[:-1]] + [tail]


def words(text: str, pattern: str, line: Line, expected: str, hint: str = "") -> re.Match:
    m = re.fullmatch(pattern, text.strip())
    if not m:
        raise line.problem("I CAN'T READ THIS", text.strip(), expected, "", hint)
    return m


def clauses(text: str) -> list[str]:
    return [c.strip() for c in text.split(",") if c.strip()]


# ---- shapes and pieces --------------------------------------------------------------------------------

def rot_y(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


@dataclass
class Shape:
    kind: str  # box, sphere, capsule, point
    pos: np.ndarray
    half: np.ndarray | None = None  # box
    radius: float = 0.0  # sphere, capsule
    pitch: float = 0.0  # box, turned about y (a plank)
    ends: tuple | None = None  # capsule

    def bbox(self):
        if self.kind == "point":
            return self.pos.copy(), self.pos.copy()
        if self.kind == "sphere":
            return self.pos - self.radius, self.pos + self.radius
        if self.kind == "capsule":
            a, b = self.ends
            return np.minimum(a, b) - self.radius, np.maximum(a, b) + self.radius
        e = np.abs(rot_y(self.pitch)) @ self.half
        return self.pos - e, self.pos + e

    def move(self, d) -> None:
        self.pos = self.pos + d
        if self.ends:
            self.ends = (self.ends[0] + d, self.ends[1] + d)


@dataclass
class Item:
    """A piece of a world: a primitive with shapes, or a part with pieces of its own."""
    name: str
    line: Line
    path: str = ""
    shapes: list[Shape] = field(default_factory=list)
    children: list["Item"] = field(default_factory=list)
    kind: str = ""  # the primitive or part it is
    mass: float | None = None
    props: dict = field(default_factory=dict)  # friction, rolls, bounce, hollow, drag, ghost, colour
    motion: dict | None = None  # {"kind": "free", ...} or {"kind": "hinge", ...}
    attached: "Item | None" = None
    plank: tuple | None = None  # (high end, low end, thickness)
    ring: float | None = None  # inner radius

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def solid(self) -> bool:
        return any(s.kind != "point" for s in self.shapes)

    def bbox(self):
        boxes = [s.bbox() for i in self.walk() for s in i.shapes if s.kind != "point"]
        if not boxes:
            boxes = [s.bbox() for i in self.walk() for s in i.shapes]
        if not boxes:
            return np.zeros(3), np.zeros(3)
        return np.min([b[0] for b in boxes], axis=0), np.max([b[1] for b in boxes], axis=0)

    def move(self, d) -> None:
        for i in self.walk():
            for s in i.shapes:
                s.move(d)
            if i.plank:
                i.plank = (i.plank[0] + d, i.plank[1] + d, i.plank[2])
            if i.motion and "anchor" in i.motion:
                i.motion["anchor"] = i.motion["anchor"] + d

    def find(self, name: str) -> "Item | None":
        return next((c for c in self.children if c.name == name), None)


GROUND = Item("floor", Line(0, "", "floor"), "floor", [Shape("box", np.array([0, 0, -0.05]), np.array([1e3, 1e3, 0.05]))])

# ---- references, points and relations -----------------------------------------------------------------

FACE = r"(near|far|left|right|top|bottom)(?: (?:end|side|edge|face))?"
FACES = {"near": (0, 0), "far": (0, 1), "right": (1, 0), "left": (1, 1), "bottom": (2, 0), "top": (2, 1)}
OFFSETS = {"beyond": (0, 1), "ahead of": (0, 1), "past": (0, 1), "behind": (0, -1), "above": (2, 1),
           "below": (2, -1), "left of": (1, 1), "to the left of": (1, 1), "right of": (1, -1), "to the right of": (1, -1)}
STARTERS = ("on ", "in ", "under ", "raised ", "centred ", "level ", "at ", "its ", "outside ")
SPOTS = (" beyond ", " behind ", " ahead of ", " past ", " above ", " below ", " left of ", " right of ",
         " outside ", " along", " up", " to the left", " to the right", " from the top")


def looks_like_place(text: str) -> bool:
    t = text + " "
    return t.startswith(STARTERS) or any(s in t for s in SPOTS)


def ref(name: str, scope: dict, line: Line) -> Item:
    name = name.strip().removeprefix("the ")
    head, *rest = name.split(".")
    if head in scope and scope[head] is None:
        raise Bad(None)  # that piece already has its own problem: don't pile a second one on top
    if head not in scope:
        close = difflib.get_close_matches(head, [k for k in scope if k != "floor"], 1)
        raise line.problem("UNKNOWN PART", head, "the name of a part written above this line",
                           "A position can only refer to parts already written, so a world reads top to bottom.",
                           f"did you mean {close[0]}?" if close else "write that part first")
    item = scope[head]
    for r in rest:
        nxt = item.find(r)
        if nxt is None:
            close = difflib.get_close_matches(r, [c.name for c in item.children], 1)
            raise line.problem("UNKNOWN PIECE", name, f"a piece of {item.name}: "
                               + ", ".join(c.name for c in item.children), "",
                               f"did you mean {item.name}.{close[0]}?" if close else "")
        item = nxt
    return item


def point(text: str, scope: dict, line: Line, me: Item | None = None) -> np.ndarray:
    """`pivot`, `bob's top`, `its right side`: a point, from a piece's extent."""
    text = text.strip()
    if m := re.fullmatch(rf"(.+?)'s {FACE}", text) or re.fullmatch(rf"(its) {FACE}", text):
        it = me if m.group(1) == "its" else ref(m.group(1), scope, line)
        lo, hi = it.bbox()
        p = (lo + hi) / 2
        axis, side = FACES[m.group(2)]
        p[axis] = (lo, hi)[side][axis]
        return p
    lo, hi = ref(text, scope, line).bbox()
    return (lo + hi) / 2


def planks(item: Item) -> list[Item]:
    return [i for i in item.walk() if i.plank]


def base_of(item: Item) -> Item | None:
    """The general sits-in rule looks for a piece called `base`, or ending in ` base`: a hollow's floor."""
    return next((i for i in item.walk() if i is not item and (i.name == "base" or i.name.endswith(" base"))), None)


def place(item: Item, text: str, scope: dict, line: Line) -> None:
    """Move an item by relations, one direction at a time. Each clause fixes a face or the centre of the item (or
    of one of its pieces, `its rim 4 m beyond ball`) in one direction; a direction may be fixed once."""
    fixed: dict[int, tuple] = {}  # axis -> (subject, which: 0 lo / 1 hi / 2 centre, value, clause, soft)

    def put(axis, which, value, clause, subject, soft=False):
        if axis in fixed and not fixed[axis][4]:
            if soft:
                return
            raise line.problem("TWO PLACES FOR ONE DIRECTION", f"{fixed[axis][3]} … {clause}",
                               f"one clause for each direction ({'along, across, up'.split(', ')[axis]} here)",
                               "Both clauses set where it is " + ("along x", "across y", "up z")[axis]
                               + ", so one of them would be ignored.", "keep the one you mean")
        fixed[axis] = (subject, which, value, clause, soft)

    cs = clauses(text)
    down = [c for c in cs if re.fullmatch(r".+ (?:down )?from the top", c)]
    along = qty(re.sub(r" (?:down )?from the top$", "", down[0]), "length", line).si if down else None
    for c in cs:
        if c in down:
            continue
        c = c.removeprefix("with ")
        subject = item
        if (m := re.fullmatch(r"its (.+)", c)) and not re.fullmatch(rf"its {FACE} at .+", c):
            ws = m.group(1).split()
            for k in range(len(ws) - 1, 0, -1):
                piece = item.find(" ".join(ws[:k]))
                if piece:
                    subject, c = piece, " ".join(ws[k:])
                    break
        relate(c, subject, scope, line, put, item, along)
    if down and not any(f[3].startswith(("on ", "rests on", "sits on")) for f in fixed.values()):
        raise line.problem("NOTHING TO MEASURE FROM", down[0], "`on <a ramp or plank>` in the same line",
                           "`from the top` measures down a sloping plank from its high end.", "")

    for axis, (subject, which, value, clause, soft) in fixed.items():
        lo, hi = subject.bbox()
        now = (lo[axis], hi[axis], (lo[axis] + hi[axis]) / 2)[which]
        d = np.zeros(3)
        d[axis] = value - now
        item.move(d)


def relate(c: str, me: Item, scope: dict, line: Line, put, whole: Item, along: float | None) -> None:
    def length(t):
        return qty(t, "length", line).si

    def box(name):
        return ref(name, scope, line).bbox()

    if m := re.fullmatch(rf"its {FACE} at (.+)", c):
        axis, side = FACES[m.group(1)]
        put(axis, side, point(m.group(2), scope, line, whole)[axis], c, me)
    elif m := re.fullmatch(r"(?:rests |stands |sits )?on (?:the )?(.+)", c):
        target = ref(m.group(1), scope, line)
        if target is not GROUND and (ps := planks(target)):
            fixed_plank(me, ps[0], along, put, c)
        else:
            put(2, 0, target.bbox()[1][2], c, me)
    elif m := re.fullmatch(r"(?:sits )?in (?:the )?(.+)", c):
        target = ref(m.group(1), scope, line)
        base = base_of(target)
        if base is None:
            raise line.problem("NOTHING TO SIT IN", m.group(1), f"a part with a base to sit on, like a cup or a "
                               f"bucket; {target.name} has " + (", ".join(i.name for i in target.children) or "no pieces"),
                               "`in` puts a thing on the base of a hollow part, centred over it.",
                               f"write `on {m.group(1)}` to rest on top of it")
        lo, hi = base.bbox()
        put(2, 0, hi[2], c, me)
        put(0, 2, (lo[0] + hi[0]) / 2, c, me, soft=True)
        put(1, 2, (lo[1] + hi[1]) / 2, c, me, soft=True)
    elif m := re.fullmatch(r"under (.+)", c):
        put(2, 1, box(m.group(1))[0][2], c, me)
    elif m := re.fullmatch(r"raised (.+)", c):
        put(2, 0, length(m.group(1)), c, me)
    elif m := re.fullmatch(rf"centred on (.+)'s {FACE}", c):
        axis, side = FACES[m.group(2)]
        put(axis, 2, box(m.group(1))[side][axis], c, me)
    elif m := re.fullmatch(r"centred (?:on|over) (.+)", c):
        lo, hi = box(m.group(1))
        put(0, 2, (lo[0] + hi[0]) / 2, c, me)
        put(1, 2, (lo[1] + hi[1]) / 2, c, me)
    elif m := re.fullmatch(r"level with (.+)", c):
        lo, hi = box(m.group(1))
        put(2, 2, (lo[2] + hi[2]) / 2, c, me)
    elif m := re.fullmatch(rf"at (.+)'s {FACE}", c):
        axis, side = FACES[m.group(2)]
        put(axis, side, box(m.group(1))[side][axis], c, me)
    elif m := re.fullmatch(rf"(?:(.+?) )?outside (.+)'s {FACE}", c):
        axis, side = FACES[m.group(3)]
        gap = length(m.group(1)) if m.group(1) else 0.0
        put(axis, 1 - side, box(m.group(2))[side][axis] + (gap if side else -gap), c, me)
    elif m := re.fullmatch(rf"(\S+)'s {FACE}", c):  # `at top's near end` with `at` as the line's key
        axis, side = FACES[m.group(2)]
        put(axis, side, box(m.group(1))[side][axis], c, me)
    elif m := re.fullmatch(rf"(.+?) ({'|'.join(sorted(OFFSETS, key=len, reverse=True))}) (.+)", c):
        axis, sign = OFFSETS[m.group(2)]
        lo, hi = box(m.group(3))
        put(axis, 2, (lo[axis] + hi[axis]) / 2 + sign * length(m.group(1)), c, me)
    elif m := re.fullmatch(r"(.+?) along", c):
        put(0, 2, length(m.group(1)), c, me)
    elif m := re.fullmatch(r"(.+?) to the (left|right)", c):
        put(1, 2, length(m.group(1)) * (1 if m.group(2) == "left" else -1), c, me)
    elif m := re.fullmatch(r"(.+?) up", c):
        put(2, 2, length(m.group(1)), c, me)
    else:
        raise line.problem("I CAN'T READ THIS POSITION", c, "a place like `on floor`, `in bucket`, `1 m beyond ball`, "
                           "`2 m along`, `40 cm up`, `raised 2 cm`, `at base's near end`, `outside frame's left side`, "
                           "`centred on base's far end`, `level with pivot` or `its far end at pivot`", "",
                           "use one of those")


def fixed_plank(me: Item, plank: Item, along: float | None, put, c: str) -> None:
    """Resting on a sloping plank: touching its upper face, `along` metres down from its high end (default:
    halfway). Writes all three directions."""
    a, b, t = plank.plank
    th = math.atan2(a[2] - b[2], b[0] - a[0])
    s = math.hypot(*(b - a)[[0, 2]]) / 2 if along is None else along
    lo, hi = me.bbox()
    up = t / 2 + (hi[2] - lo[2]) / 2
    p = a + s * np.array([math.cos(th), 0, -math.sin(th)]) + up * np.array([math.sin(th), 0, math.cos(th)])
    for axis in range(3):
        put(axis, 2, p[axis], c, me)


# ---- the primitives -----------------------------------------------------------------------------------

PRIMITIVES = ["box", "cube", "sphere", "rod", "plank", "post", "ring", "point"]


def primitive(item: Item, kind: str, rest: list[str], scope: dict, line: Line) -> None:
    def mass_clauses(cs):
        for cl in cs:
            item.mass = qty(cl, "mass", line).si

    if kind in ("box", "cube"):
        if not rest:
            raise line.problem("MISSING SIZE", kind, "its size, like `box 16 by 24 by 34 cm`" if kind == "box" else
                               "its side, like `cube 20 cm`", "", "")
        half = np.array(dims(rest[0], 3, line) if kind == "box" else [qty(rest[0], "length", line).si] * 3) / 2
        item.shapes = [Shape("box", np.zeros(3), half)]
        mass_clauses(rest[1:])
    elif kind == "sphere":
        m = re.fullmatch(r"(.+?) (radius|across)", rest[0] if rest else "")
        if not m:
            size = rest[0] if rest else "6 cm"
            raise line.problem("SAY WHAT IT MEASURES", f"sphere {size}", "a size that says what it measures, like "
                               "`sphere 6 cm radius` or `sphere 12 cm across`",
                               "A sphere's size could be its radius or its diameter, a factor of two either way.",
                               f"write `sphere {size} radius` or `sphere {size} across`")
        r = qty(m.group(1), "length", line).si / (1 if m.group(2) == "radius" else 2)
        item.shapes = [Shape("sphere", np.zeros(3), radius=r)]
        mass_clauses(rest[1:])
    elif kind in ("rod", "plank"):
        ends, thick, wide, others = None, None, None, []
        for cl in rest:
            if m := re.fullmatch(r"from (.+) to (.+)", cl):
                ends = (point(m.group(1), scope, line), point(m.group(2), scope, line))
            elif m := re.fullmatch(r"(.+) thick", cl):
                thick = qty(m.group(1), "length", line).si
            elif m := re.fullmatch(r"(.+) wide", cl):
                wide = qty(m.group(1), "length", line).si
            else:
                others.append(cl)
        need = {"`from ... to ...`": ends, "`... thick`": thick} | ({"`... wide`": wide} if kind == "plank" else {})
        for what, v in need.items():
            if v is None:
                raise line.problem("MISSING SIZE", ", ".join(rest), f"a {kind} with {what}", "", "")
        a, b = ends
        if kind == "rod":
            item.shapes = [Shape("capsule", (a + b) / 2, radius=thick / 2, ends=(a, b))]
        else:
            pitch = math.atan2(a[2] - b[2], b[0] - a[0])
            item.shapes = [Shape("box", (a + b) / 2, np.array([np.linalg.norm(b - a) / 2, wide / 2, thick / 2]), pitch=pitch)]
            item.plank = (a, b, thick)
        mass_clauses(others)
    elif kind == "post":
        m = words(rest[0] if rest else "", r"(.+) square", line, "`post 6 cm square, from floor to top`")
        side = qty(m.group(1), "length", line).si
        m2 = words(rest[1] if len(rest) > 1 else "", r"from floor to (.+)", line, "`from floor to <a point>`")
        p = point(m2.group(1), scope, line)
        item.shapes = [Shape("box", np.array([p[0], p[1], p[2] / 2]), np.array([side / 2, side / 2, p[2] / 2]))]
        mass_clauses(rest[2:])
    elif kind == "ring":
        d = qty(words(rest[0] if rest else "", r"(.+) across", line, "`ring 45.72 cm across, 8 mm thick`").group(1), "length", line).si
        t = qty(words(rest[1] if len(rest) > 1 else "", r"(.+) thick", line, "`8 mm thick`").group(1), "length", line).si
        R = d / 2 + t
        pts = [np.array([R * math.cos(k * math.pi / 8), R * math.sin(k * math.pi / 8), 0]) for k in range(17)]
        item.shapes = [Shape("capsule", (pts[k] + pts[k + 1]) / 2, radius=t, ends=(pts[k], pts[k + 1])) for k in range(16)]
        item.ring = d / 2
    elif kind == "point":
        item.shapes = [Shape("point", np.zeros(3))]


# ---- reading files ------------------------------------------------------------------------------------

@dataclass
class Node:
    n: int
    text: str
    children: list["Node"] = field(default_factory=list)


def tree(text: str, problems: list) -> list[Node]:
    """Indentation is the only structure: a line belongs to the line above it that is indented less."""
    root = Node(0, "")
    stack = [(-1, root)]
    for n, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.strip().startswith("--"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        while stack[-1][0] >= indent:
            stack.pop()
        node = Node(n, raw.strip())
        stack[-1][1].children.append(node)
        stack.append((indent, node))
    return root.children


def split_key(text: str, keys) -> tuple[str | None, str]:
    for k in sorted(keys, key=len, reverse=True):
        if text == k or text.startswith(k + " "):
            return k, text[len(k):].strip()
    return None, text


@dataclass
class PartDef:
    name: str
    n: int
    needs: list[tuple[str, str | None, int]]  # name, default text, line
    pieces: list[Node]


def read_library(text: str, problems: list) -> dict[str, PartDef]:
    lib = {}
    for node in tree(text, problems):
        m = re.fullmatch(r"part (.+)", node.text)
        if not m:
            problems.append(Problem("I CAN'T READ THIS", f"library line {node.n}", node.text, "`part <name>`", "", ""))
            continue
        needs, pieces = [], []
        for ch in node.children:
            if nm := re.fullmatch(r"needs\s+(.+?)(?:, else (.+))?", ch.text):
                needs.append((nm.group(1).strip(), nm.group(2), ch.n))
            else:
                pieces.append(ch)
        for need, _, n in needs:
            if any(p.text == need for p in pieces):
                problems.append(Problem("NAME USED TWICE", f"library line {n}: {m.group(1)}", need,
                                        "a need and a piece with different names",
                                        "Needs are written into the part's lines by name, so a piece with the same "
                                        "name would be replaced by the value.", "rename one of them"))
        lib[m.group(1)] = PartDef(m.group(1), node.n, needs, pieces)
    return lib


def subst(text: str, values: dict) -> tuple[str, list]:
    """Write each need's value in place of its name (whole words, longest name first, one pass)."""
    if not values:
        return text, []
    used = []
    pat = re.compile(r"(?<![\w'])(" + "|".join(re.escape(k) for k in sorted(values, key=len, reverse=True)) + r")(?![\w])")

    def sub(m):
        value, origin = values[m.group(1)]
        used.append((value, origin))
        return value
    return pat.sub(sub, text), used


ITEM_KEYS = ["is a", "is an", "is", "weighs", "friction", "rolls", "bounce", "colour", "touches nothing", "moves",
             "launched", "spins", "first one spins", "turns on", "swings", "spring", "damping", "armature",
             "starts turned", "attached to", "stacked", "repeated", "size"]
PLACE_KEYS = ["rests", "sits", "stands", "hangs", "lies", "at"]
FLAGS = {"hollow": ("hollow", True), "slowed by air": ("drag", True), "touches nothing": ("ghost", True),
         "rolls": ("rolls", True), "lively": ("bounce", "lively"), "dead": ("bounce", "dead")}


class Reader:
    def __init__(self, lib: dict[str, PartDef], problems: list):
        self.lib, self.problems = lib, problems

    # A body is a list of pieces, read top to bottom; each may refer only to pieces above it.
    def body(self, nodes: list[Node], values: dict, file: str, prefix: str) -> list[Item]:
        scope, items = {"floor": GROUND}, []
        for node in nodes:
            name = node.text
            try:
                made = self.item(node, scope, values, file, prefix)
                scope[name] = made[0] if len(made) == 1 else Item(name, made[0].line, name, children=made)
                items += made
            except Bad as b:
                scope[name] = None
                if b.problem:
                    self.problems.append(b.problem)
        return items

    def item(self, node: Node, scope: dict, values: dict, file: str, prefix: str) -> list[Item]:
        name, path = node.text, f"{prefix}{node.text}"
        lines = []  # (key, value, Line)
        is_line = next((c for c in node.children if split_key(c.text, ["is a", "is an"])[0]), None)
        part = None
        if is_line:
            _, v = split_key(is_line.text, ["is a", "is an"])
            v, _ = subst(v, values)
            part = next((p for p in sorted(self.lib, key=len, reverse=True) if v == p or v.startswith(p + ",")), None)
        keys = ITEM_KEYS + PLACE_KEYS if part is None else ["is a", "is an"] + [nd[0] for nd in self.lib[part].needs] + PLACE_KEYS
        for c in node.children:
            key, value = split_key(c.text, keys)
            ln = Line(c.n, c.text, f"{path}.{key.replace(' ', '_')}" if key else
                      (f"{path}.place" if looks_like_place(c.text) else path), file)
            if key is None:
                if looks_like_place(c.text):
                    v, ln.subs = subst(c.text, values)
                    lines.append(("place", v, ln))
                    continue
                close = difflib.get_close_matches(c.text.split("  ")[0].strip(), keys, 1) or \
                    difflib.get_close_matches(c.text.split()[0], keys, 1)
                raise ln.problem("I DON'T KNOW THIS LINE", c.text, f"a line {name} understands: {', '.join(keys)}", "",
                                 f"did you mean `{close[0]}`?" if close else "")
            v, ln.subs = subst(value, values)
            if part is not None and key not in PLACE_KEYS + ["is a", "is an"]:
                lines.append((key, v, ln))  # a need's value: written into the part as it stands
                continue
            if v == "nothing":
                continue  # an optional need that was not given
            lines.append(("place" if key in PLACE_KEYS else key, v, ln))
        if name == "floor" and not is_line:
            return [self.floor(node, lines, path)]
        if not is_line:
            raise Bad(Problem("MISSING LINE", f"{file}line {node.n}: {path}", f"no `is a` line under {name}",
                              f"an `is a` line saying what {name} is: a primitive ({', '.join(PRIMITIVES)}) or a "
                              f"part ({', '.join(self.lib)})", "", f"add `  is a ...` under {name}"))
        item = Item(name, Line(node.n, node.text, path, file), path)
        isv, isl = next((v, l) for k, v, l in lines if k in ("is a", "is an"))
        if part:
            item.kind = part
            self.instance(item, part, lines, file, path)
        else:
            kind = isv.split(",")[0].split(" ")[0]
            if kind not in PRIMITIVES:
                close = difflib.get_close_matches(isv.split(",")[0], PRIMITIVES + list(self.lib), 1)
                raise isl.problem("I DON'T KNOW THIS KIND OF THING", isv, f"a primitive ({', '.join(PRIMITIVES)}) or a "
                                  f"part from the library ({', '.join(self.lib)})", "",
                                  f"did you mean {close[0]}?" if close else "add it to library.world")
            item.kind = kind
            first, *more = isv[len(kind):].split(",")
            primitive(item, kind, [c.strip() for c in [first, *more] if c.strip()], scope, isl)
        copies = 1
        for key, v, ln in lines:
            if key == "place":
                place(item, v, scope, ln)
            elif part is None and key not in ("is a", "is an"):
                copies = self.fact(item, key, v, ln, scope, copies)
        made = self.copies(item, copies, lines)
        return made

    def instance(self, item: Item, part: str, lines, file: str, path: str) -> None:
        d = self.lib[part]
        given = {k: (v, ln) for k, v, ln in lines if k not in ("is a", "is an", "place")}
        values = {}
        for need, default, n in d.needs:
            if need in given:
                values[need] = given[need]
            elif default is not None:
                v, used = subst(default, values)
                values[need] = (v, used[0][1] if used else Line(n, default, f"{part}.{need}", "library "))
            else:
                raise Bad(Problem("MISSING LINE", f"{file}line {item.line.n}: {path}", f"no `{need}` line",
                                  f"a `{need}` line under {item.name}: {part} needs "
                                  + ", ".join(nd[0] for nd in d.needs if nd[1] is None), "",
                                  f"add `  {need} ...` under {item.name}"))
        item.children = self.body(d.pieces, values, "library ", f"{path}.")
        if len(item.children) != len(d.pieces):
            raise Bad(None)  # a piece failed: its problem is already reported

    def floor(self, node, lines, path) -> Item:
        item = Item("floor", Line(node.n, node.text, path), "floor", kind="floor")
        item.props["size"] = 8.0
        for key, v, ln in lines:
            if key == "size":
                item.props["size"] = qty(v, "length", ln).si
            elif key == "friction":
                item.props["friction"] = friction(v, ln)
            else:
                raise ln.problem("I DON'T KNOW THIS LINE", ln.text, "a floor line: size, friction", "", "")
        return item

    def fact(self, item: Item, key: str, v: str, ln: Line, scope: dict, copies: int) -> int:
        hinge = item.motion if item.motion and item.motion["kind"] == "hinge" else None
        if key == "weighs":
            item.mass = qty(v, "mass", ln).si
        elif key == "friction":
            item.props["friction"] = friction(v, ln)
        elif key in ("is", "rolls", "touches nothing"):
            for flag in clauses(v) if key == "is" else [key]:
                if flag not in FLAGS:
                    raise ln.problem("I DON'T KNOW THIS WORD", flag, f"one of: {', '.join(FLAGS)}", "", "")
                k, val = FLAGS[flag]
                item.props[k] = val
        elif key == "bounce":
            item.props["bounce"] = words(v, r"(lively|dead)", ln, "`bounce lively` or `bounce dead`").group(1)
        elif key == "colour":
            if v not in COLOURS:
                raise ln.problem("I DON'T KNOW THIS COLOUR", v, f"one of: {', '.join(COLOURS)}", "", "")
            item.props["colour"] = COLOURS[v]
        elif key == "moves":
            words(v, r"freely", ln, "`moves freely`")
            item.motion = {"kind": "free", "launch": np.zeros(3), "spin": np.zeros(3)}
        elif key in ("launched", "spins", "first one spins"):
            if not item.motion or item.motion["kind"] != "free":
                raise ln.problem("NOT FREE TO MOVE", ln.text, "`moves freely` written above this line",
                                 "Only a thing that moves freely can be launched or set spinning.", "add `moves  freely`")
            if key == "launched":
                for cl in clauses(v):
                    m = words(cl, r"(.+?) (along|across|up)", ln, "`3.21 m/s along, 9.3 m/s up`")
                    item.motion["launch"][("along", "across", "up").index(m.group(2))] = qty(m.group(1), "speed", ln).si
            else:
                m = words(v, r"(.+) about (x|y|z)", ln, "`4 rad/s about y`")
                spin = np.array(AXES[m.group(2)]) * qty(m.group(1), "spin", ln).si
                item.motion["first spin" if key == "first one spins" else "spin"] = spin
        elif key == "turns on":
            cs = clauses(v)
            if len(cs) != 3:
                raise ln.problem("I CAN'T READ THIS", v, "`turns on <joint name>, about <x, y or z>, at <a point>`",
                                 "", "like `turns on hinge, about z, at its right side`")
            ax = words(cs[1], r"about (x|y|z)", ln, "`about x`, `about y` or `about z`").group(1)
            at = words(cs[2], r"at (.+)", ln, "`at pivot` or `at its right side`").group(1)
            item.motion = {"kind": "hinge", "joint": cs[0].replace(" ", "_"), "axis": ax,
                           "anchor": point(at, scope, ln, item), "line": ln}
        elif key in ("swings", "spring", "damping", "armature", "starts turned"):
            if hinge is None:
                raise ln.problem("NOTHING TO TURN ON", ln.text, "a `turns on` line written above this one",
                                 f"`{key}` describes a hinge, and this piece has none.", "add `turns on ...` first")
            if key == "swings":
                m = words(v, r"from (.+) to (.+)", ln, "`from 0° to 120°`")
                hinge["range"] = (qty(m.group(1), "angle", ln), qty(m.group(2), "angle", ln))
            elif key == "spring":
                m = words(v, r"(.+) toward (.+)", ln, "`40 N·m/rad toward 0°`")
                hinge["stiffness"], hinge["rest"] = qty(m.group(1), "torsional stiffness", ln), qty(m.group(2), "angle", ln)
            elif key == "damping":
                hinge["damping"] = qty(v, "torsional damping", ln)
            elif key == "armature":
                hinge["armature"] = qty(v, "rotor inertia", ln)
            else:
                hinge["start"] = qty(v, "angle", ln)
        elif key == "attached to":
            item.attached = ref(v, scope, ln)
        elif key == "stacked":
            copies = int(words(v, r"(\d+) high", ln, "`stacked 5 high`").group(1))
            item.props["repeat"] = ("stacked", None)
        elif key == "repeated":
            m = words(v, r"(\d+) times, (.+) apart (along|across|up)", ln, "`repeated 10 times, 10 cm apart along`")
            copies = int(m.group(1))
            item.props["repeat"] = ("row", np.array(AXES[{"along": "x", "across": "y", "up": "z"}[m.group(3)]])
                                    * qty(m.group(2), "length", ln).si)
        else:
            raise ln.problem("I DON'T KNOW THIS LINE", ln.text, "", "", "")
        return copies

    def copies(self, item: Item, n: int, lines) -> list[Item]:
        if n == 1:
            return [item]
        out = []
        for i in range(1, n + 1):
            c = cp.deepcopy(item)
            c.name, c.path = f"{item.name}{i}", f"{item.path}{i}"
            if i > 1:
                how, step = item.props["repeat"]
                if how == "stacked":  # on the one below, centred over it
                    lo, hi = out[-1].bbox()
                    clo, chi = c.bbox()
                    c.move(np.array([*((lo + hi) / 2 - (clo + chi) / 2)[:2], hi[2] - clo[2]]))
                else:
                    c.move(step * (i - 1))
                if c.motion and "first spin" in c.motion:
                    del c.motion["first spin"]
            elif c.motion and "first spin" in c.motion:
                c.motion["spin"] = c.motion.pop("first spin")
            out.append(c)
        return out


def friction(v: str, ln: Line) -> tuple:
    vals = {"slide": None, "spinning": 0.005, "rolling": 0.0001}
    for c in clauses(v):
        m = words(c, r"(?:(spinning|rolling) )?(\S+)", ln, "friction like `0.8, rolling 0.002`")
        vals[m.group(1) or "slide"] = number(m.group(2), ln)
    return (vals["slide"], vals["spinning"], vals["rolling"])


# ---- a program: a world, its expectations, and every problem ------------------------------------------

@dataclass
class Program:
    name: str
    items: list[Item] = field(default_factory=list)
    air: float | None = None
    expect: list[tuple[int, str]] = field(default_factory=list)
    problems: list[Problem] = field(default_factory=list)


def parse(text: str, library: str | None = None) -> Program:
    """Every problem at once where it can: each piece is read on its own, so one bad line doesn't hide the rest."""
    prog = Program("world")
    lib = read_library(LIBRARY.read_text() if library is None else library, prog.problems)
    nodes = []
    for node in tree(text, prog.problems):
        if m := re.fullmatch(r"world\s+(.+)", node.text):
            prog.name = m.group(1).strip().replace(" ", "_")
        elif m := re.fullmatch(r"air\s+(.+)", node.text):
            try:
                prog.air = qty(m.group(1), "density", Line(node.n, node.text, "air")).si
            except Bad as b:
                prog.problems.append(b.problem)
        elif node.text == "expect":
            prog.expect = [(c.n, c.text) for c in node.children]
        else:
            nodes.append(node)
    prog.items = Reader(lib, prog.problems).body(nodes, {}, "", "")
    unique = {p.render(): p for p in prog.problems}  # a bad value used in several places reports once
    prog.problems = list(unique.values())
    return prog


# ---- from pieces to MuJoCo bodies ---------------------------------------------------------------------

def fmt(*xs) -> str:
    return " ".join(f"{x:.6g}" for x in xs)


def geom_name(leaf: Item, top: Item) -> str:
    return top.name if leaf is top else top.name + "_" + leaf.path[len(top.path) + 1:].replace(".", "_").replace(" ", "_")


def conventions(name: str) -> str:
    for old, new in CONVENTIONS.items():
        if name.startswith(old):
            return new + name[len(old):]
    return name


def mover(leaf: Item) -> Item | None:
    seen = leaf
    while seen is not None and not seen.motion:
        seen = seen.attached
    return seen


def compile_program(prog: Program) -> Compiled:
    c = Compiled(None)
    c.problems = list(prog.problems)
    if c.problems:
        return c
    xml, joints, owner = [], [], {}

    def geoms(leaf: Item, top: Item, origin: np.ndarray, indent: int, body_mass_owner: bool = False):
        base = geom_name(leaf, top)
        p = leaf.props
        for k, s in enumerate(leaf.shapes):
            if s.kind == "point":
                continue
            name = conventions(f"{base}_{k:02d}" if len(leaf.shapes) > 1 else base)
            owner[name] = leaf.path
            a = {}
            if s.kind == "box":
                a.update(type="box", pos=fmt(*(s.pos - origin)), size=fmt(*s.half))
                if s.pitch:
                    a["euler"] = fmt(0, s.pitch, 0)
            elif s.kind == "sphere":
                a.update(type="sphere", pos=fmt(*(s.pos - origin)), size=fmt(s.radius))
            else:
                a.update(type="capsule", size=fmt(s.radius), fromto=fmt(*(s.ends[0] - origin), *(s.ends[1] - origin)))
            if leaf.mass is not None and not p.get("hollow"):
                a["mass"] = fmt(leaf.mass / len([x for x in leaf.shapes if x.kind != "point"]))
            if p.get("rolls"):
                a["condim"] = "6"
            if "friction" in p:
                a["friction"] = fmt(*p["friction"])
            if "bounce" in p:
                a["solref"] = {"lively": "0.01 0.2", "dead": "0.01 1"}[p["bounce"]]
            if p.get("drag"):
                a.update(fluidshape="ellipsoid", fluidcoef="0.25 0.25 1.5 1.0 1.0")
            if p.get("ghost"):
                a.update(contype="0", conaffinity="0")
            if "colour" in p:
                a["rgba"] = p["colour"]
            xml.append("  " * indent + f'<geom name="{name}" ' + " ".join(f'{k}="{v}"' for k, v in a.items()) + "/>")

    for top in prog.items:
        if top.kind == "floor":
            a = {"type": "plane", "size": fmt(top.props["size"], top.props["size"], 0.1)}
            if "friction" in top.props:
                a["friction"] = fmt(*top.props["friction"])
            owner["floor"] = "floor"
            xml.append('    <geom name="floor" ' + " ".join(f'{k}="{v}"' for k, v in a.items()) + "/>")
            continue
        leaves = [i for i in top.walk() if i.solid()]
        groups: dict[int, tuple[Item, list[Item]]] = {}
        still = []
        for leaf in leaves:
            mv = mover(leaf)
            if mv is None:
                still.append(leaf)
            else:
                groups.setdefault(id(mv), (mv, []))[1].append(leaf)
        if not groups:
            xml.append(f'    <body name="{top.name}">')
            for leaf in still:
                geoms(leaf, top, np.zeros(3), 3)
            xml.append("    </body>")
        else:
            for leaf in still:
                geoms(leaf, top, np.zeros(3), 2)
        for mv, members in groups.values():
            bname = top.name if len(groups) == 1 else geom_name(mv, top)
            mo = mv.motion
            if mo["kind"] == "free":
                origin = mv.shapes[0].pos.copy()
                xml.append(f'    <body name="{bname}" pos="{fmt(*origin)}">')
                xml.append("      <freejoint/>")
                if mv.props.get("hollow") and mv.mass:
                    r = mv.shapes[0].radius
                    i = 2 / 3 * mv.mass * r * r
                    xml.append(f'      <inertial pos="0 0 0" mass="{fmt(mv.mass)}" diaginertia="{fmt(i, i, i)}"/>')
                joints.append({"name": f"{bname} (free)", "kind": "free", "part": mv.path,
                               "qpos": [*origin, 1, 0, 0, 0], "qvel": [*mo["launch"], *mo["spin"]]})
            else:
                origin = mo["anchor"]
                xml.append(f'    <body name="{bname}" pos="{fmt(*origin)}">')
                a = {"type": "hinge", "pos": "0 0 0", "axis": fmt(*AXES[mo["axis"]])}
                if mo.get("range"):
                    a.update(limited="true", range=fmt(mo["range"][0].si, mo["range"][1].si))
                if mo.get("stiffness"):
                    a["stiffness"] = fmt(mo["stiffness"].si)
                if mo.get("rest") is not None:
                    a["springref"] = fmt(mo["rest"].si)
                if mo.get("damping"):
                    a["damping"] = fmt(mo["damping"].si)
                if mo.get("armature"):
                    a["armature"] = fmt(mo["armature"].si)
                xml.append(f'      <joint name="{mo["joint"]}" ' + " ".join(f'{k}="{v}"' for k, v in a.items()) + "/>")
                start = mo.get("start")
                joints.append({"name": mo["joint"], "kind": "hinge", "part": mv.path, "qpos": [start.si if start else 0.0],
                               "qvel": [0], "range": mo.get("range"), "start": start})
            for leaf in members:
                geoms(leaf, top, origin, 3)
            xml.append("    </body>")
        base = base_of(top)
        if base is not None and mover(base) is None:
            lo, hi = top.bbox()
            c.containers.append((top.name, (lo[0], hi[0], lo[1], hi[1])))
        for leaf in leaves:
            if leaf.ring:
                lo, hi = leaf.bbox()
                c.rings.append((top.name, tuple((lo + hi) / 2), leaf.ring))

    c.owner, c.joints = owner, joints
    check_meaning(c)
    if c.problems:
        return c
    opt = f'  <option timestep="{TIMESTEP}"' + (f' density="{prog.air:g}"' if prog.air else "") + "/>"
    qpos = " ".join(f"{v:.6g}" for j in joints for v in j["qpos"])
    qvel = " ".join(f"{v:.6g}" for j in joints for v in j["qvel"])
    c.xml = "\n".join([f'<mujoco model="{prog.name}">', '  <compiler angle="radian"/>', opt, "  <worldbody>", *xml,
                       "  </worldbody>",
                       *(["  <keyframe>", f'    <key name="start" qpos="{qpos}" qvel="{qvel}"/>', "  </keyframe>"] if joints else []),
                       "</mujoco>", ""])
    check_overlaps(c)
    if c.problems:
        c.xml = None
    return c


# ---- expect, checked against the replay -----------------------------------------------------------------

def _is(name: str, label: str) -> bool:
    return label == name or label.startswith(name + ".")


def expectations(prog: Program, events: list[str]) -> list[tuple[str, bool, str]]:
    """Each `expect` line with whether the run did it, and the event that shows it (or the nearest one)."""
    ev = [e.split("  ", 1)[1].lower() for e in events]
    out = []
    for n, line in prog.expect:
        s = line.lower()
        if m := re.fullmatch(r"(\S+) touches (\S+)", s):
            a, b = m.groups()
            hits = [e for e in ev if (t := re.fullmatch(r"(.+) first touches (.+)", e))
                    and ((_is(a, t[1]) and _is(b, t[2])) or (_is(a, t[2]) and _is(b, t[1])))]
        elif m := re.fullmatch(r"(\S+) comes to rest in (\S+)", s):
            hits = [e for e in ev if e.startswith(m[1] + " ") and f"comes to rest inside {m[2]}" in e]
        elif m := re.fullmatch(r"(\S+) drops through (\S+)", s):
            hits = [e for e in ev if e.startswith(m[1] + " ") and f"drops through {m[2]}" in e]
        elif m := re.fullmatch(r"(\S+) reaches its (lower|upper) stop", s):
            hits = [e for e in ev if _is(m[1], e.split(" ")[0]) and f"reaches its {m[2]} stop" in e]
        else:
            out.append((line, False, "I can't read this expectation"))
            continue
        subject = s.split()[0]
        near = [e for e in ev if _is(subject, e.split(" ")[0])]
        out.append((line, bool(hits), hits[0] if hits else (near[-1] if near else "nothing happened to it")))
    return out
