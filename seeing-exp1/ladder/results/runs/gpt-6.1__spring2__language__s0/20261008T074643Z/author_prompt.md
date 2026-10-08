Write a world in the world language for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Cart1 starts with its axial slide spring compressed 0.20 m; the spring stiffness is 18 N/m, and cart1 travels 0.50 m before touching ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches the bob of pendulum1.
</brief>

The world compiles to a MuJoCo scene. MuJoCo will build it, start it as written and simulate it for 6 s.
Nothing else acts on the world: whatever moves must be set moving by the world itself, for example by a launch, a
spin, a spring, a hinge's starting angle, or gravity.

Names the other tools need. They fix names, not what you build: Name the things exactly: `cart1` (spring driven cart, slides); `ball1` (first ramp ball, moves freely); `ramp1` (first inclined ramp, fixed); `pendulum1` (first pendulum, turns on a hinge).

Here is the language, with its whole parts library:

<language>
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
-- The parts library, written in the world language itself.
--
-- A part says what it needs, then builds itself from pieces: primitives (box, cube, sphere, rod, plank, post,
-- ring, point) or other parts. Each piece is placed by relations to the floor or to pieces written above it.
-- Nothing here is Python: a new part is a new block in this file.
--
-- Directions: along is x (beyond, ahead of, behind; a thing's near end faces back along x, its far end
-- forward), to the left is y (left side, right side), up is z (top, bottom).

part open box
  needs  length
  needs  width
  needs  walls
  needs  wall thickness, else 2 cm
  needs  base thickness, else 2 cm
  needs  near wall height, else walls

  base
    is a  box length by width by base thickness
    on    floor
  near wall
    is a  box wall thickness by width by near wall height
    on    floor, centred on base's near end
  far wall
    is a  box wall thickness by width by walls
    on    floor, centred on base's far end
  left wall
    is a  box length by wall thickness by walls
    on    floor, centred on base's left side
  right wall
    is a  box length by wall thickness by walls
    on    floor, centred on base's right side


part ramp
  needs  high end
  needs  low end
  needs  width
  needs  thickness, else 4 cm

  top
    is a  point
    at    high end
  foot
    is a  point
    at    low end
  deck
    is a  plank from top to foot, width wide, thickness thick
  leg
    is a  post 6 cm square, from floor to top


part door
  needs  width
  needs  height
  needs  thickness
  needs  mass
  needs  swings
  needs  spring
  needs  damping
  needs  starts open

  frame
    is a  box 8 by 8 cm by height + 14 cm
    on    floor, 12 cm to the right
  panel
    is a           box thickness by width by height, mass
    raised         2 cm
    8 cm outside frame's left side
    turns on       hinge, about z, at its right side
    swings         swings
    spring         spring
    damping        damping
    starts turned  starts open


part catapult
  needs  pivot height
  needs  arm length
  needs  arm mass
  needs  swings
  needs  spring
  needs  damping
  needs  armature, else 0.01 kg·m²

  stand
    is a  box 16 by 24 by pivot height − 6 cm
    on    floor
  pivot
    is a  point
    at    pivot height up
  arm
    is a      box arm length by 6 by 4 cm, arm mass
    its far end at pivot, level with pivot
    turns on  catapult hinge, about y, at pivot
    swings    swings
    spring    spring
    damping   damping
    armature  armature
  scoop base
    is a         box 16 by 16 by 1 cm, 20 g
    on           arm, at arm's near end
    attached to  arm
  scoop back
    is a         box 1 by 16 by 10 cm, 10 g
    on           arm, outside scoop base's near end
    attached to  arm


part pendulum
  needs  pivot height
  needs  length
  needs  bob size
  needs  bob mass
  needs  rod thickness
  needs  rod mass
  needs  starts swung back
  needs  damping, else nothing

  pivot
    is a  point
    at    pivot height up
  bob
    is a           sphere bob size, bob mass
    length below pivot
    turns on       pivot, about y, at pivot
    damping        damping
    starts turned  starts swung back
  rod
    is a         rod rod thickness thick, from pivot to bob's top
    weighs       rod mass
    attached to  bob
  stand arm
    is a  box 6 by 30 by 4 cm
    on    rod, its left side at pivot
  stand post
    is a  post 6 cm square, from floor to stand arm's top
    centred on stand arm's right side


part hoop
  needs  rim height
  needs  rim size, else 45.72 cm
  needs  tube, else 8 mm

  rim
    is a    ring rim size across, tube thick
    at      rim height up
    colour  orange
  bracket
    is a    box 14.1 by 10 by 2.4 cm
    31.05 cm beyond rim, 1 cm below rim
    colour  orange
  backboard
    is a    box 3 by 180 by 105 cm
    outside bracket's far end, 37.5 cm above rim
    colour  glass
  square
    is a    box 1 mm by 59 by 45 cm
    outside backboard's near end, 14.5 cm above rim
    touches nothing
    colour  black
  pole base
    is a    box 80 by 80 by 5 cm
    on      floor, 120 cm beyond rim
    colour  dark grey
  pole
    is a    box 20 by 20 cm by rim height + 35 cm
    on      floor, 120 cm beyond rim
    colour  grey
  arm
    is a    box 68.9 by 12 by 12 cm
    outside backboard's far end, 25 cm above rim
    colour  grey


part table
  needs  surface
  needs  height
  needs  legs, else 6 cm

  top
    is a  box surface by 3 cm
    raised height − 3 cm
  near left leg
    is a  post legs square, from floor to top's bottom
    at top's near end, at top's left side
  near right leg
    is a  post legs square, from floor to top's bottom
    at top's near end, at top's right side
  far left leg
    is a  post legs square, from floor to top's bottom
    at top's far end, at top's left side
  far right leg
    is a  post legs square, from floor to top's bottom
    at top's far end, at top's right side


part raised bucket
  needs  table height
  needs  size
  needs  walls

  table
    is a    table
    surface size by size
    height  table height
  bucket
    is an   open box
    length  size
    width   size
    walls   walls
    on      table
```
</language>

An example world, for a different brief:

```world
world  drop onto a block

floor
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 40 by 40 by 20 cm
  stands    on floor, 1 m along

wall
  is a      box 4 by 60 by 30 cm
  stands    on floor, 1.6 m beyond block

ball
  is a      sphere 5 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  centred over block, 1.5 m up
  launched  0.2 m/s along

expect
  ball touches block
```

Reply with the complete world in one ```world code block (and a ```parts block if you define new parts). A
sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
