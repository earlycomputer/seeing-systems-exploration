```world
world  drop powered spring plunger

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- The free plunger slides horizontally between fixed guide rails.
-- A hinged spring follower presses against its rear face.

plunger
  is a      box 60 by 50 by 6 cm, 500 g
  moves     freely
  friction  0.025, spinning 0.001, rolling 0.001
  bounce    dead
  colour    grey
  at        0 m along, 0 m to the left, 45 cm up

lower left guide
  is a      box 140 by 3.5 by 4 cm
  friction  0.025
  at        10 cm behind plunger, 23.25 cm to the left, 40 cm up

lower right guide
  is a      box 140 by 3.5 by 4 cm
  friction  0.025
  at        10 cm behind plunger, 23.25 cm to the right, 40 cm up

upper left guide
  is a      box 140 by 3.5 by 3 cm
  friction  0.025
  at        10 cm behind plunger, 23.25 cm to the left, 49.7 cm up

upper right guide
  is a      box 140 by 3.5 by 3 cm
  friction  0.025
  at        10 cm behind plunger, 23.25 cm to the right, 49.7 cm up

left side guide
  is a      box 140 by 3 by 9 cm
  friction  0.025
  at        10 cm behind plunger, 26.7 cm to the left, 45 cm up

right side guide
  is a      box 140 by 3 by 9 cm
  friction  0.025
  at        10 cm behind plunger, 26.7 cm to the right, 45 cm up

left travel stop
  is a      box 2 by 4 by 6 cm
  bounce    dead
  at        39 cm beyond plunger, 23 cm to the left, 45 cm up

right travel stop
  is a      box 2 by 4 by 6 cm
  bounce    dead
  at        39 cm beyond plunger, 23 cm to the right, 45 cm up

spring pivot
  is a      point
  at        32.5 cm behind plunger, 0 m to the left, 125 cm up

spring contact point
  is a      point
  at        32.5 cm behind plunger, 0 m to the left, 45 cm up

spring follower
  is a           rod 2 cm thick, from spring pivot to spring contact point
  weighs         80 g
  turns on       return spring hinge, about y, at spring pivot
  swings         from −20° to 40°
  spring         240 N·m/rad toward 0°
  damping        0.3 N·m·s/rad
  armature       0.0001 kg·m²
  starts turned  0°
  friction       0.01
  colour         grey

spring contact
  is a         sphere 2.5 cm radius, 30 g
  at           spring contact point
  attached to  spring follower
  friction     0.01
  bounce       dead

-- The falling block drives this descending wedge to the rear.
-- Its separate lane keeps the block away from the ball.

compression high end
  is a      point
  at        20 cm behind plunger, 12 cm to the right, 85 cm up

compression low end
  is a      point
  at        20 cm beyond plunger, 12 cm to the right, 45 cm up

compression wedge
  is a         plank from compression high end to compression low end, 16 cm wide, 2 cm thick
  weighs       150 g
  attached to  plunger
  friction     0.03
  bounce       dead
  colour       grey

striker
  is a         box 2 by 2.5 by 14 cm, 70 g
  on           plunger, 31 cm beyond plunger, 12 cm to the left
  attached to  plunger
  friction     0.02
  bounce       lively
  colour       grey

-- At the block's left bottom edge, the wedge surface is 0.74414 m high.
-- The block starts with its bottom 0.5 m above that surface.

block
  is a      box 8 by 10 by 10 cm, 2 kg
  moves     freely
  friction  0.03
  bounce    dead
  colour    dark grey
  at        4 cm behind plunger, 12 cm to the right, 1.29414 m up

-- Two staging rails support the ball while leaving a slot for the striker.

ball staging right rail
  is a      box 16 by 1.5 by 2 cm
  friction  0.3
  at        36 cm beyond plunger, 9 cm to the left, 50.5 cm up

ball staging left rail
  is a      box 16 by 1.5 by 2 cm
  friction  0.3
  at        36 cm beyond plunger, 15 cm to the left, 50.5 cm up

ramp toe
  is a      point
  at        42 cm beyond plunger, 12 cm to the left, 51 cm up

ramp crest
  is a      point
  at        120 cm beyond plunger, 12 cm to the left, 97 cm up

ramp
  is a       ramp
  high end   ramp crest
  low end    ramp toe
  width      25 cm
  thickness  2 cm
  friction   0.3, spinning 0.001, rolling 0.001
  bounce     dead
  colour     wood

ball
  is a      sphere 3.5 cm radius, 50 g
  moves     freely
  rolls
  friction  0.3, spinning 0.001, rolling 0.001
  bounce    dead
  colour    orange
  at        37 cm beyond plunger, 12 cm to the left, 54.2 cm up

hoop
  is a      ring 3 m across, 8 mm thick
  colour    orange
  at        215 cm beyond plunger, 12 cm to the left, 80 cm up

cup
  is an           open box
  length          3.4 m
  width           3.4 m
  walls           35 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        1.0, spinning 0.02, rolling 0.02
  bounce          dead
  colour          wood
  at              215 cm beyond plunger, 12 cm to the left
  on              floor

expect
  block touches compression wedge
  ball touches ramp
  ball drops through hoop
  ball comes to rest in cup
```

---
thinking (summarized):

**Defining parts and mechanisms**

I'm diving into defining a wedge-slider mechanism with specific components like a block box and a sloping plank. I noticed the library mentions that a part can have its own properties, but I’m wondering how the “moves freely” aspect fits into that. I need to clarify how the plunger works within this setup, especially as it interacts with the wedge piece. It looks like the plunger should be designed to move along a predefined path while connected to other components.

**Positioning the falling block**

I need to determine how to position a block that falls from 0.5m above the ramp's wedge. I'll explicitly place the bottom of the block at the top of the wedge. The wedge's geometric top is well-defined as an AABB, and I have to ensure that the block is positioned correctly. The block should be set at a height calculated based on the z-coordinate to avoid duplication. I’ll set the center of the block just above that contact point.

**Exploring vertical guidance**

I'm thinking about how to guide a block vertically using a fixed catcher shelf. This shelf would need to intercept the block at the right coordinates, specifically at x.25 and z.5 beyond the wedge end. I'm also considering the shelf's width, which should be around .15. There's a lot to unpack here, like how these measurements will work together, but I'm eager to clarify any challenges that arise during this process!

**Optimizing lever mechanics**

I'm analyzing a lever system with compression limits, where it maxes out at certain slider values. I've identified the vertical component that pushes a plunger up, and I'm contemplating adjusting lever lengths and pivot points. The goal is to ensure the system operates effectively without obstruction. It’s important to carefully consider the lever’s angle and position to maintain proper functionality while allowing for safe operation, especially in regards to the ball path and compression settings.