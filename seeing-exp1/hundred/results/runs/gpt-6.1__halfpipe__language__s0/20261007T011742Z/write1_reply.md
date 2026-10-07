```parts
part faceted halfpipe
  entry
    is a  point
    at    0 m along, 68 cm up

  bend one
    is a  point
    at    25 cm along, 52 cm up

  bend two
    is a  point
    at    50 cm along, 40 cm up

  bend three
    is a  point
    at    75 cm along, 33 cm up

  bottom
    is a  point
    at    1 m along, 30.5 cm up

  bend four
    is a  point
    at    1.25 m along, 33 cm up

  bend five
    is a  point
    at    1.5 m along, 40 cm up

  bend six
    is a  point
    at    1.75 m along, 52 cm up

  exit
    is a  point
    at    2 m along, 68 cm up

  descending one
    is a  plank from entry to bend one, 32 cm wide, 2 cm thick

  descending two
    is a  plank from bend one to bend two, 32 cm wide, 2 cm thick

  descending three
    is a  plank from bend two to bend three, 32 cm wide, 2 cm thick

  descending four
    is a  plank from bend three to bottom, 32 cm wide, 2 cm thick

  ascending one
    is a  plank from bottom to bend four, 32 cm wide, 2 cm thick

  ascending two
    is a  plank from bend four to bend five, 32 cm wide, 2 cm thick

  ascending three
    is a  plank from bend five to bend six, 32 cm wide, 2 cm thick

  ascending four
    is a  plank from bend six to exit, 32 cm wide, 2 cm thick
```

```world
world  halfpipe pendulum drop

floor
  size      10 m
  friction  0.8, spinning 0.01, rolling 0.005

ramp
  is a       ramp
  high end   -1.2 m along, 1.58 m up
  low end    0 m along, 68 cm up
  width      32 cm
  thickness  2 cm
  friction   0.5, spinning 0.001, rolling 0.0002
  bounce     dead
  colour     wood

halfpipe
  is a      faceted halfpipe
  friction  0.5, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    grey

ball1
  is a      sphere 5.5 cm radius, 400 g
  rolls
  moves     freely
  friction  0.5, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    orange
  on        ramp, 50 cm from the top

striker shelf
  is a      box 24 by 32 by 4 cm
  at        2.10 m along, 68 cm up
  friction  0.12, spinning 0.001, rolling 0.001
  bounce    dead
  colour    wood

block
  is a      box 12 by 18 by 14 cm, 250 g
  moves     freely
  friction  0.12, spinning 0.001, rolling 0.001
  bounce    dead
  colour    wood
  on        striker shelf, 2.08 m along, 0 m to the left

pendulum pivot
  is a  point
  at    2.30 m along, 1.25 m up

pendulum
  is a           sphere 8 cm radius, 250 g
  at             2.30 m along, 80 cm up
  turns on       final striker hinge, about y, at pendulum pivot
  swings         from -60° to 10°
  starts turned  0°
  damping        0.003 N·m·s/rad
  friction       0.3, spinning 0.001, rolling 0.001
  bounce         dead
  colour         dark grey

pendulum rod
  is a         rod 2 cm thick, from pendulum pivot to pendulum's top
  weighs       15 g
  attached to  pendulum
  colour       grey

ball2 perch
  is a      box 3 by 8 by 76.5 cm
  on        floor, 2.52 m along, 0 m to the left
  friction  0.2, spinning 0.001, rolling 0.001
  bounce    dead
  colour    grey

ball2
  is a      sphere 5.5 cm radius, 120 g
  rolls
  moves     freely
  on        ball2 perch, 2.52 m along, 0 m to the left
  friction  0.9, spinning 0.015, rolling 0.01
  bounce    dead
  colour    white

hoop
  is a    ring 1.45 m across, 1 cm thick
  at      3.05 m along, 0 m to the left, 52 cm up
  bounce  dead
  colour  orange

cup
  is an           open box
  length          1.65 m
  width           1.65 m
  walls           36 cm
  wall thickness  2 cm
  base thickness  2.5 cm
  at              3.05 m along, 0 m to the left
  friction        0.9, spinning 0.015, rolling 0.01
  bounce          dead
  colour          wood

expect
  ball1 touches ramp
  ball1 touches halfpipe
  ball1 touches block
  block touches pendulum
  pendulum touches ball2
  ball2 drops through hoop
  ball2 comes to rest in cup
```

---
thinking (summarized):

**Clarifying ramp position values**

I need to ensure that I'm using the right grammar for the ramp position values, particularly with phrases like "at 1..." or "centred overpoint, level with." If the top value at the "high end" encounters an error, I should look to substitute it correctly. For example, changing the high-end value to “-1.2 m along, 1.58 m up” is valid. Also, it's critical to simplify the coordinates for clarity without unnecessary complexity. I'll strive to finalize the code neatly.