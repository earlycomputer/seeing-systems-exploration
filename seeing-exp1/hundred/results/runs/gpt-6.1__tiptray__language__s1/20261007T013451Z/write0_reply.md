```world
world  falling weight and transfer balls

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

tray pivot
  is a  point
  at    0 m along, 0 m to the left, 1.2 m up

tray
  is a           box 80 by 32 by 2 cm, 700 g
  at             40 cm behind tray pivot, 0 cm to the left, level with tray pivot
  turns on       tray hinge, about y, at tray pivot
  swings         from -18° to 0°
  spring         20 N·m/rad toward 25°
  damping        2 N·m·s/rad
  armature       0.03 kg·m²
  starts turned  0°
  friction       0.5, spinning 0.002, rolling 0.0005
  bounce         dead
  colour         wood

tray left wall
  is a         box 80 by 2 by 12 cm, 30 g
  on           tray, 40 cm behind tray pivot, at tray's left side
  attached to  tray
  bounce       dead
  colour       wood

tray right wall
  is a         box 80 by 2 by 12 cm, 30 g
  on           tray, 40 cm behind tray pivot, at tray's right side
  attached to  tray
  bounce       dead
  colour       wood

weight retaining wall
  is a         box 2 by 28 by 20 cm, 50 g
  on           tray, 48 cm behind tray pivot, 0 cm to the left
  attached to  tray
  friction     0.6
  bounce       dead
  colour       wood

-- The tray top is at 1.21 m. The weight bottom starts at 1.81 m.
weight
  is a      cube 14 cm, 8 kg
  moves     freely
  at        34 cm behind tray pivot, 0 cm to the left, 1.88 m up
  friction  0.6
  bounce    dead
  colour    dark grey

ball1
  is a      sphere 6 cm radius, 450 g
  moves     freely
  rolls
  on        tray, 22 cm behind tray, 0 cm to the left
  friction  0.5, spinning 0.002, rolling 0.0005
  bounce    dead
  colour    orange

spill high
  is a  point
  at    82 cm behind tray pivot, 0 cm to the left, 93 cm up

spill low
  is a  point
  at    1.2 m behind tray pivot, 0 cm to the left, 79 cm up

spill ramp
  is a       ramp
  high end   spill high
  low end    spill low
  width      32 cm
  thickness  2 cm
  friction   0.35, spinning 0.002, rolling 0.0005
  bounce     dead
  colour     wood

runway
  is a      box 55 by 32 by 4 cm
  at        1.475 m behind tray pivot, 0 cm to the left, 78 cm up
  friction  0.12, spinning 0.002, rolling 0.0005
  bounce    dead
  colour    wood

ball2
  is a      sphere 6 cm radius, 450 g
  moves     freely
  rolls
  on        runway, 13 cm beyond runway, 0 cm to the left
  friction  0.5, spinning 0.002, rolling 0.0005
  bounce    dead
  colour    white

block
  is a      cube 10 cm, 60 g
  moves     freely
  on        runway, 17.5 cm behind runway, 0 cm to the left
  friction  0.03, spinning 0.002, rolling 0.001
  bounce    dead
  colour    orange

hoop
  is a    ring 110 cm across, 10 mm thick
  at      2.12 m behind tray pivot, 0 cm to the left, 57 cm up
  bounce  dead
  colour  orange

bin
  is an           open box
  length          1.9 m
  width           1.4 m
  walls           32 cm
  wall thickness  3 cm
  base thickness  3 cm
  on              floor, 2.15 m behind tray pivot, 0 cm to the left
  friction        0.9, spinning 0.01, rolling 0.01
  bounce          dead
  colour          grey

expect
  weight touches tray
  tray reaches its lower stop
  ball1 touches ball2
  ball2 touches block
  block drops through hoop
  block comes to rest in bin
```

---
thinking (summarized):

**Designing a custom tray**

I’m considering a custom tray with a platform and side walls. There’s a weight pocket behind where ball1 exits near the x-end, and I need an extension ramp for ball2. The tray pivot might sit at center x0, z1.2, with a length of 0.8 and positioned near x-0.4. The tray angle could be -12 or -18 degrees, and I need to ensure ball2 is stationary before ball1 arrives. Let's figure out these dimensions and make the design work!

**Configuring ball and ramp setup**

I'm working on a fixed ramp that connects at coordinates -0.74, z0.94 to -1.18, z0.81. Ball1 starts at -0.66 height. When the ramp tips to -18 degrees, it may drop and roll down a chute. Ball2 will roll on a flat lane at -1.3 and there's a block at -1.57. Also, I've got a hoop center at -1.9 with a rim height of z0.6. I need to ensure that ball transfer from the platform works smoothly and accurately!