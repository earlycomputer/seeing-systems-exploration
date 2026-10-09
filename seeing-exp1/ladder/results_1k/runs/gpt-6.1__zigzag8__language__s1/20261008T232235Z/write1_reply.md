```world
world  gravity driven chain

-- Gravity relies on MuJoCo's default of 9.81 m/s2.
-- All moving bodies start with zero velocity.
-- Dead contacts approximate the requested low restitution.

floor
  size      6 m
  friction  0.72, spinning 0.001, rolling 0.0001

lever pivot
  is a  point
  at    35 cm up

lever1
  is a           box 60 by 10 by 4 cm, 500 g
  at             level with lever pivot
  turns on       lever hinge, about y, at lever pivot
  swings         from -45° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.72
  bounce         dead
  colour         wood

ring1
  is a      ring 18 cm across, 1 cm thick
  at        27 cm behind lever1, 67 cm up
  friction  0.72
  bounce    dead
  colour    orange

ball1
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  centred over ring1, 30 cm above ring1
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange

-- A remote vertical bearing approximates a horizontal slide.
-- Over 42 cm, its sideways departure is less than 1 mm.
-- Hinge damping / radius squared = 0.20 N s/m.
cart guide pivot
  is a  point
  at    10 cm along, 100 m to the left, 60.3 cm up

cart1
  is a           box 22 by 18 by 10 cm, 500 g
  at             10 cm along, 60.3 cm up
  turns on       cart guide, about z, at cart guide pivot
  swings         from -0.2464° to 0°
  damping        2000 N·m·s/rad
  starts turned  0°
  friction       0.72
  bounce         dead
  colour         grey

domino pedestal
  is a      box 18 by 22 by 32 cm
  stands    on floor, 47 cm behind lever1
  friction  0.72
  bounce    dead
  colour    dark grey

-- Explicit centring fixes both horizontal coordinates.
domino1
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  stands    on domino pedestal, centred over domino pedestal
  friction  0.72
  bounce    dead
  colour    white

-- Endpoint separation is 1 m at 20 degrees.
-- The low running surface is 15 cm above the floor.
ramp high
  is a  point
  at    59.7869 cm behind lever1, 47.3226 cm up

ramp low
  is a  point
  at    153.7562 cm behind lever1, 13.1206 cm up

ramp1
  is a      plank from ramp high to ramp low, 30 cm wide, 4 cm thick
  friction  0.72
  bounce    dead
  colour    wood

-- This keeper holds ball2 until domino1 drives it over the lip.
ball keeper
  is a      box 1.2 by 18 by 1.8 cm
  at        68.05 cm behind lever1, 47.61 cm up
  friction  0.72
  bounce    dead
  colour    dark grey

ball2
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  at        65 cm behind lever1, 52.8743 cm up
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange

-- The incoming face is 10 cm beyond the ramp's low surface edge.
door1
  is a           box 4 by 42 by 32 cm, 450 g
  at             166.4402 cm behind lever1, 19 cm to the left, 30 cm up
  turns on       door hinge, about z, at its left side
  swings         from -70° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.72
  bounce         dead
  colour         wood

-- The inverted pendulum is triggered by the door's strike.
pendulum pivot
  is a  point
  at    205.907 cm behind lever1, 26 cm to the left, 3 cm up

pendulum1
  is a           box 2 by 2 by 50 cm, 350 g
  at             205.907 cm behind lever1, 26 cm to the left, 28 cm up
  turns on       pendulum hinge, about x, at pendulum pivot
  swings         from -38° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.72
  bounce         dead
  colour         grey

block pedestal
  is a      box 16 by 22 by 35 cm
  stands    on floor, 205.907 cm behind lever1, 63.4 cm to the left
  friction  0.72
  bounce    dead
  colour    dark grey

-- Explicit centring fixes both horizontal coordinates.
block1
  is a      cube 12 cm, 350 g
  moves     freely
  stands    on block pedestal, centred over block pedestal
  friction  0.72
  bounce    dead
  colour    white

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever1 reaches its lower stop
  lever1 touches cart1
  cart1 touches domino1
  domino1 touches ball2
  ball2 touches ramp1
  ball2 touches door1
  door1 reaches its lower stop
  door1 touches pendulum1
  pendulum1 reaches its lower stop
  pendulum1 touches block1
```