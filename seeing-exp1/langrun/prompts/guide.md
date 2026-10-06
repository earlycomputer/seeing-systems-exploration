# The world language

A world is plain indented text, one fact per line, with no brackets. It compiles to a MuJoCo scene. Numbers carry
their units, positions are relations to things written above, and every problem is reported at the line that
caused it.

## Shape of a file

```
world  <a name>

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

<thing name>
  is a   <a primitive or a part>
  <one fact per line>
  <a position>
```

- `world` names the world. An optional `air  1.2 kg/m³` line gives air density (drag on things that are
  `slowed by air`).
- `floor` is the ground, its top at height 0. It takes `size` and `friction` lines only, and can be left bare.
- Every other thing has a name (any words), an `is a` (or `is an`) line, and indented facts. A thing may refer
  only to things written above it, so a world reads top to bottom. The floor can always be referred to.
- Key and value are separated by two or more spaces. A line starting with `--` is a comment.
- Directions: `along` is x, `across` (to the left) is y, `up` is z. A thing's near end faces back along x, its
  far end forward; its left side is +y, right side −y; top and bottom are up and down.

## Units

Every quantity needs its unit: lengths `mm cm m`, masses `g kg`, angles `° deg rad`, speed `m/s`, spin `rad/s`,
hinge stiffness `N·m/rad`, hinge damping `N·m·s/rad`, rotor inertia `kg·m²`, density `kg/m³`. Sums like
`pivot height − 6 cm` work when the kinds agree. Sizes like `16 by 24 by 34 cm` take the last unit for all three.

## Primitives (`is a ...`)

| Primitive | Written as |
|---|---|
| box | `box 16 by 24 by 34 cm` (length along x by width across y by height), optionally `, 2 kg` |
| cube | `cube 20 cm`, optionally `, 500 g` |
| sphere | `sphere 6 cm radius` or `sphere 12 cm across`, optionally `, 150 g` |
| rod | `rod 2 cm thick, from <point> to <point>` (a capsule) |
| plank | `plank from <point> to <point>, 40 cm wide, 4 cm thick` (a sloping box, like a ramp's deck) |
| post | `post 6 cm square, from floor to <point>` |
| ring | `ring 45.72 cm across, 8 mm thick` (lies flat; a hoop's rim) |
| point | `point` (no size; a named place to refer to, placed with `at`) |

A point in a rod, plank or post is a thing's name (its centre) or a face of it: `pivot`, `bob's top`,
`top's near end`, `its right side`.

## Facts

| Line | Meaning |
|---|---|
| `weighs  100 g` | its mass, if not given in `is a` |
| `friction  0.8, spinning 0.01, rolling 0.004` | sliding friction, optionally spinning and rolling |
| `rolls` | a ball that rolls properly (rolling contact) |
| `bounce  lively` or `bounce  dead` | a springy or a dead contact |
| `is  hollow, lively, slowed by air` | flags: `hollow` (a shell's inertia), `lively`, `dead`, `slowed by air`, `touches nothing` |
| `touches nothing` | seen, but nothing collides with it |
| `colour  orange` | orange, glass, black, grey, dark grey, wood, white |
| `moves  freely` | it is a loose thing, free to move (otherwise it is fixed in place) |
| `launched  3.21 m/s along, 9.3 m/s up` | its starting velocity (needs `moves freely`) |
| `spins  4 rad/s about y` | its starting spin (needs `moves freely`) |
| `stacked  5 high` | five copies, each on the one below, named `<name>1` (bottom) to `<name>5` |
| `repeated  10 times, 10 cm apart along` | copies in a row, named `<name>1` to `<name>10` |
| `first one spins  4 rad/s about y` | with copies: only the first starts spinning |
| `turns on  hinge, about z, at its right side` | it turns on a hinge with this name, about an axis, at a point |
| `swings  from 0° to 120°` | the hinge's range |
| `spring  40 N·m/rad toward 0°` | a spring on the hinge, pulling toward an angle |
| `damping  25 N·m·s/rad` | damping on the hinge |
| `armature  0.01 kg·m²` | rotor inertia on the hinge |
| `starts turned  69°` | the hinge's angle at the start |
| `attached to  <thing>` | moves with another thing (on its hinge, or loose with it) |

A thing with no `moves freely`, `turns on` or `attached to` is fixed in place. Things that move together become
one MuJoCo body.

## Positions

A position line lists clauses separated by commas; each fixes one direction (along, across or up), and a
direction may be fixed only once. It may start with `rests`, `sits`, `stands`, `hangs`, `lies` or `at`, or be
written bare.

| Clause | Meaning |
|---|---|
| `on floor`, `on table` | its bottom on the other's top |
| `on ramp, 12 cm from the top` | resting on a sloping plank, measured down from its high end |
| `in bucket` | on the base of a hollow part (a piece named `base` or ending in ` base`), centred over it |
| `under shelf` | its top at the other's bottom |
| `raised 2 cm`, `40 cm up`, `2 m along`, `30 cm to the left` | absolute heights and offsets |
| `1 m beyond ball` (also `ahead of`, `past`, `behind`, `above`, `below`, `left of`, `right of`) | centre offset from the other's centre in that direction |
| `at base's near end` | its near end flush with the other's near end (inside) |
| `8 cm outside frame's left side` | just outside that face, with an optional gap |
| `centred on base's far end`, `centred over table` | centred on a face, or over the other |
| `level with pivot` | the same height as the other's centre |
| `its far end at pivot` | one of its faces at a point |
| `its rim 4 m beyond ball` | placing a whole part by one of its pieces |

## Parts

A part is a named whole from the library below, used with `is a <part>` followed by the lines it `needs`
(a need with `else` has a default). A part also takes a thing's own facts (`friction`, `colour`, `bounce`,
`rolls`, `touches nothing`, `is`), which apply to every piece. Its pieces are named `<thing>.<piece>` in the run: `catapult.scoop base`.
Inside a world, positions may refer to a part's pieces the same way: `on bucket.base`.

You may also define new parts: put them in a ```parts block, written exactly as the library's parts are.

## Expectations (optional)

An `expect` block at the end lists what should happen, checked against the run:

```
expect
  ball touches ramp
  ball comes to rest in cup
  ball drops through hoop
  door reaches its lower stop
```

## Names in MuJoCo

Each top-level thing becomes a MuJoCo body or geom named after it; a part's pieces become geoms named
`<thing>_<piece>` with spaces as underscores (`bucket_near_wall`). A hinge is named by its `turns on` line, with
spaces as underscores. A hoop's ring pieces are named `rim_00` to `rim_15`.

## The library

```
{library}
```
