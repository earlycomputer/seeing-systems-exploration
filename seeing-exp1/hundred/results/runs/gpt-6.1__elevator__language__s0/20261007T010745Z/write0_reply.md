```world
world  falling weight and guided lift

floor
  size      5 m
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    40 cm up

lever
  is a           box 120 by 10 by 4 cm, 300 g
  level with     pivot
  turns on       lever hinge, about y, at pivot
  swings         from -12° to 0°
  starts turned  0°
  damping        0.02 N·m·s/rad
  friction       1
  bounce         dead
  colour         wood

-- The weight's bottom starts 0.5 m above the lever's top.
weight
  is a      cube 12 cm, 2 kg
  moves     freely
  raised    92 cm, 45 cm behind pivot
  friction  1
  bounce    dead
  colour    dark grey

-- These shoulders support the lift without obstructing the lever.
-- They preserve the initial 4 cm lever-to-lift gap.
left lift shoulder
  is a      box 6 by 4 by 2 cm
  at        45 cm along, 9 cm to the left, 45 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead

right lift shoulder
  is a      box 6 by 4 by 2 cm
  at        45 cm along, 9 cm to the right, 45 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead

-- Four fixed guides constrain the long shank to vertical sliding.
-- Their bottoms are above the lever's entire travel.
near lift guide
  is a      box 2 by 24 by 30 cm
  at        42.4 cm along, 71 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead
  colour    grey

far lift guide
  is a      box 2 by 24 by 30 cm
  at        47.6 cm along, 71 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead
  colour    grey

left lift guide
  is a      box 10 by 2 by 30 cm
  at        45 cm along, 11.1 cm to the left, 71 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead
  colour    grey

right lift guide
  is a      box 10 by 2 by 30 cm
  at        45 cm along, 11.1 cm to the right, 71 cm up
  friction  0, spinning 0, rolling 0
  bounce    dead
  colour    grey

-- The rounded head strikes the ball below and behind its centre.
lift
  is a      sphere 3.5 cm radius, 25 g
  moves     freely
  at        45 cm along, 90 cm up
  friction  0.2, spinning 0, rolling 0
  bounce    dead
  colour    orange

lift shank
  is a         box 3 by 20 by 44 cm, 275 g
  raised       46 cm, 45 cm along
  attached to  lift
  friction     0, spinning 0, rolling 0
  bounce       dead
  colour       grey

-- The lever can raise the shank only about 5.4 cm before its stop.
-- The remaining head-to-ball clearance must be crossed in free ascent.
bridge
  is a      box 66.2 by 24 by 4 cm
  raised    104 cm, 81.9 cm along
  friction  0.6, spinning 0.001, rolling 0.0003
  bounce    dead
  colour    wood

cup
  is an             open box
  length            50 cm
  width             40 cm
  walls             26 cm
  wall thickness    2 cm
  base thickness    2 cm
  near wall height  4 cm
  raised            94 cm, 138 cm along
  friction          1, spinning 0.02, rolling 0.02
  bounce            dead
  colour            orange

ball
  is a      sphere 4 cm radius, 100 g
  moves     freely
  rolls
  on        bridge, 50.5 cm along
  friction  0.6, spinning 0.001, rolling 0.0003
  bounce    dead
  colour    white

expect
  weight touches lever
  lever reaches its lower stop
  ball touches lift
  ball touches bridge
  ball comes to rest in cup
```

---
thinking (summarized):

**Evaluating downward rebound lift**

I'm thinking about the mechanism of downward rebound lift. It seems like the initial stop at the bottom needs to lower to allow the lever to function correctly. I notice that it lifts to .527 and then finishes at .067 relative to the start. The head position is at .967 while the bottom is at .932 compared to the rail at .86, which seems acceptable. When weight is at rest, the lever is pinned down, causing the lift to rest on the lever support.

**Considering custom builds**

I'm thinking about creating a more robust custom part called the "guided striker" for the stem box. It would be positioned at the floor head, centered above the stem. I wonder how each piece will remain fixed relative to the whole while also allowing movement. For instance, with a catapult, the hinge inside moves freely, but there might be something odd when it comes to nesting parts. It’s an interesting design challenge!

**Clarifying bridge support options**

I’m considering the user’s comments on the bridge support options. It seems that the fixed and floating supports are both valid. The user mentions "bridge fixed cup," and that gives me some ideas about how to make posts for aesthetics; it looks optional. I'm looking into hinge pivot settings and checking if "at pivot" can define the position correctly. It appears I need to clarify how "at pivot" interacts with horizontal and vertical settings in different contexts.