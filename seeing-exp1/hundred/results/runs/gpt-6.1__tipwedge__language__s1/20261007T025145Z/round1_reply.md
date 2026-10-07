The block falls onto the wedge at 0.32 s, and the wedge tips into ball1 at 0.44 s. However, ball1 is only nudged along the level shelf; it never reaches the ramp or flap. The block subsequently touches ball1, then settles near the ramp entrance. The flap stays at its upper stop throughout, holding ball2 outside the cup.

The revision below shortens the level shelf, lightens ball1, separates the falling weight from its lane, and enlarges the catch area. It has not yet been simulated.

```world
world  falling weight tips wedge and releases a ball

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

starting shelf
  is a      box 75 by 30 by 4 cm
  raised    58 cm
  at        1.6 m along
  friction  0.7, spinning 0.003, rolling 0.0002
  bounce    dead

-- The level shelf ends just 1 cm behind ball1's starting centre.
ramp
  is a       ramp
  high end   1.225 m along, 6 cm to the right, 60.75 cm up
  low end    6.5 cm along, 6 cm to the right, 38.75 cm up
  width      18 cm
  thickness  2.5 cm
  friction   0.6, spinning 0.003, rolling 0.0002
  bounce     dead
  colour     wood

-- These four pieces move together as one loose tipping wedge.
wedge
  is a      box 38 by 24 by 1.5 cm, 120 g
  moves     freely
  at        1.5 m along, 81 cm up
  friction  0.9, spinning 0.005, rolling 0.001
  bounce    dead
  colour    orange

wedge heel
  is a         box 8 by 24 by 2 cm, 150 g
  on           starting shelf, 1.5 m along
  attached to  wedge
  friction     0.9, spinning 0.005, rolling 0.001
  bounce       dead
  colour       orange

wedge apex
  is a  point
  at    1.5 m along, 0 m to the left, 17 cm below wedge

wedge near corner
  is a  point
  at    19 cm behind wedge, 0 m to the left, level with wedge

wedge far corner
  is a  point
  at    19 cm beyond wedge, 0 m to the left, level with wedge

wedge near face
  is a         plank from wedge near corner to wedge apex, 24 cm wide, 1.5 cm thick
  weighs       100 g
  attached to  wedge
  friction     0.9, spinning 0.005, rolling 0.001
  bounce       dead
  colour       orange

wedge far face
  is a         plank from wedge apex to wedge far corner, 24 cm wide, 1.5 cm thick
  weighs       100 g
  attached to  wedge
  friction     0.9, spinning 0.005, rolling 0.001
  bounce       dead
  colour       orange

-- The block's bottom starts 0.5 m above the wedge's crown.
-- Its narrow footprint is offset across from ball1's lane.
block
  is a      box 8 by 6 by 10 cm, 650 g
  moves     freely
  raised    1.3175 m
  at        1.37 m along, 5 cm to the left
  friction  0.9, spinning 0.005, rolling 0.001
  bounce    dead
  colour    grey

ball1
  is a      sphere 5.5 cm radius, 200 g
  moves     freely
  rolls
  on        starting shelf, 1.235 m along, 6 cm to the right
  friction  0.6, spinning 0.003, rolling 0.0002
  bounce    dead
  colour    white

flap pivot
  is a  point
  at    0 m along, 0 m to the left, 29 cm up

flap
  is a           box 2.5 by 40 by 45 cm, 400 g
  raised         29 cm
  at             0 m along, 0 m to the left
  turns on       release hinge, about y, at flap pivot
  swings         from -85° to 6°
  starts turned  6°
  damping        0.03 N·m·s/rad
  friction       0.6, spinning 0.003, rolling 0.0004
  bounce         dead
  colour         orange

upper guide high end
  is a  point
  at    58 cm along, 11 cm to the left, 72 cm up

upper guide low end
  is a  point
  at    6 cm along, 11 cm to the left, 61 cm up

ball2 guide
  is a      plank from upper guide high end to upper guide low end, 12 cm wide, 2 cm thick
  friction  0.6, spinning 0.003, rolling 0.0002
  bounce    dead
  colour    wood

ball2
  is a      sphere 3.5 cm radius, 25 g
  moves     freely
  rolls
  at        9.2 cm along, 11 cm to the left, 66.3 cm up
  friction  0.6, spinning 0.003, rolling 0.0004
  bounce    dead
  colour    white

cup
  is an           open box
  length          140 cm
  width           50 cm
  walls           22 cm
  wall thickness  2.5 cm
  base thickness  3 cm
  on              floor, 15 cm behind flap pivot, 4 cm to the left
  friction        1.0, spinning 0.02, rolling 0.015
  bounce          dead
  colour          grey

expect
  block touches wedge
  ball1 touches ramp
  ball1 touches flap
  flap reaches its lower stop
  ball2 comes to rest in cup
```

```json
{
  "what_happens": "The block falls onto the wedge, which tips and nudges ball1 along the level shelf. Ball1 never reaches the ramp or flap. The flap remains at its upper stop, and ball2 stays held against it on its guide.",
  "works": false,
  "problem": "The wedge does not push ball1 far enough to reach the ramp, so the flap is never triggered and ball2 is never released into the cup."
}
```

---
thinking (summarized):

**Calculating ball dynamics**

I’m thinking about how to lighten ball1 to achieve better performance. If I lighten it by 0.2, the wedge will push it larger, and I'm estimating the flap can handle a barrier. The kinetic energy of ball1 becomes 0.225, which seems sufficient. Lightening it by 0.15 will increase shove and torque, calculating that gives me enough tip and barrier interaction. I'm considering point mass impulse too, but with gravity in the mix, 0.2 seems safe.

**Evaluating block dimensions**

The user is mentioning that the block's falling tip weight on one side is the same at x1.37, with no across requirement. They want to keep the block dimensions at 8 by 6 by 10 and position it 3.5 cm to the left, possibly narrower by 0.06 at a range of +0.05. I think picking a 5 cm left position with a 6 cm width to wedge across seems interesting. The block geometry mass is noted as 0.65 for stable gravity drop.