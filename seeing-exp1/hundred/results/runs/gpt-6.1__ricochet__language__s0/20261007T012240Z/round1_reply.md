The ball falls onto wall1, but then hits target **before** reaching wall2. After rebounding from wall2, it hits target again and swings it to its lower stop. The block leaves the shelf, but lands on the fallen target and remains there—not on the bin’s base.

The correction below lowers target to clear the outgoing ball and narrows it so the released block can fall past it into the bin. This revised world has not yet been simulated.

```world
world  two ricochets and a gravity release

floor
  size      10 m
  friction  0.9, spinning 0.01, rolling 0.005

bin
  is an           open box
  length          4.6 m
  width           1.2 m
  walls           28 cm
  wall thickness  3 cm
  base thickness  4 cm
  friction        0.9, spinning 0.01, rolling 0.005
  bounce          dead
  colour          grey
  at              25 cm along

first wall high
  is a  point
  at    92 cm along, 168 cm up

first wall low
  is a  point
  at    108 cm along, 152 cm up

wall1
  is a      plank from first wall high to first wall low, 24 cm wide, 2 cm thick
  friction  0
  bounce    lively
  colour    grey

second wall low
  is a  point
  at    165 cm along, 80 cm up

second wall high
  is a  point
  at    185 cm along, 190 cm up

wall2
  is a      plank from second wall low to second wall high, 50 cm wide, 4 cm thick
  friction  0
  bounce    lively
  colour    grey

-- The outgoing ball passes above this lower target.
-- The returning ball strikes it below its shelf.
target
  is a      box 2.5 by 16 by 90 cm, 120 g
  at        125 cm along, 80 cm up
  turns on  release hinge, about y, at its bottom
  swings    from -90° to 0°
  damping   0.025 N·m·s/rad
  friction  0.2
  bounce    dead
  colour    orange

-- The shelf extends sideways to carry the payload outside
-- the narrow target's eventual horizontal footprint.
release shelf
  is a         box 18 by 50 by 2 cm, 20 g
  on           target, 8 cm beyond target, 17 cm left of target
  attached to  target
  friction     0.5
  bounce       dead
  colour       wood

block
  is a      cube 8 cm, 80 g
  moves     freely
  on        release shelf, 8 cm beyond target, 30 cm left of target
  friction  0.8, spinning 0.01, rolling 0.005
  bounce    dead
  colour    wood

ball
  is a      sphere 6 cm radius, 250 g
  moves     freely
  rolls
  bounce    lively
  friction  0
  colour    orange
  at        centred over wall1, 1 m above wall1

expect
  ball touches wall1
  ball touches wall2
  ball touches target
  target reaches its lower stop
  block comes to rest in bin
```

```json
{
  "what_happens": "The ball falls onto wall1, hits target before wall2, then rebounds from wall2 and hits target again. Target swings to its lower stop and releases block, but block lands on the fallen target and rests there above the bin base.",
  "works": false,
  "problem": "The ball hits target before wall2, and the released block rests on target rather than in the bin."
}
```