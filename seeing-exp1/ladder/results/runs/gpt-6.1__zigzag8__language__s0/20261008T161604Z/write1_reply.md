```world
world  gravity driven contact chain

floor
  size      8 m
  friction  0.72, spinning 0, rolling 0

-- MuJoCo's default gravity is 9.81 m/s².
-- Dead contacts approximate, but do not specify, restitution 0.04.
-- The roller track approximates a horizontal slide.
-- Linear slide damping of 0.20 N s/m cannot be expressed here.
-- This scene has not been simulation-verified.

ring1
  is a      ring 16 cm across, 8 mm thick
  at        1.026274 m up, 19.799 cm behind floor, 0 m to the left
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    orange

ball1
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  at        30 cm above ring1, 19.799 cm behind floor, 0 m to the left
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    orange

lever pivot
  is a      point
  at        50 cm up, 0 m along, 0 m to the left

lever1
  is a           box 60 by 10 by 4 cm, 0.50 kg
  at             50 cm up, 0 m along, 0 m to the left
  turns on       lever hinge, about y, at lever pivot
  swings         from 0° to 45°
  starts turned  45°
  damping        0.04 N·m·s/rad
  friction       0.72, spinning 0, rolling 0
  bounce         dead
  colour         wood

-- A light inclined striking face converts the rising end's
-- motion into a horizontal impulse on the cart.
striker upper corner
  is a  point
  at    22 cm beyond lever pivot, 7 cm above lever pivot, 0 m to the left

striker lower corner
  is a  point
  at    34 cm beyond lever pivot, 5 cm below lever pivot, 0 m to the left

lever striking face
  is a         plank from striker upper corner to striker lower corner, 8 cm wide, 2 cm thick
  weighs       1 g
  attached to  lever1
  friction     0.72, spinning 0, rolling 0
  bounce       dead
  colour       wood

left bearing rail
  is a      box 70 by 3 by 4 cm
  at        55 cm along, 7.5 cm to the left, 38 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

right bearing rail
  is a      box 70 by 3 by 4 cm
  at        55 cm along, 7.5 cm to the right, 38 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

left bearings
  is a      sphere 6 mm radius, 1 g
  moves     freely
  rolls
  on        left bearing rail, 24 cm along, 7.5 cm to the left
  repeated  52 times, 12 mm apart along
  friction  0.72, spinning 0, rolling 0
  bounce    dead

right bearings
  is a      sphere 6 mm radius, 1 g
  moves     freely
  rolls
  on        right bearing rail, 24 cm along, 7.5 cm to the right
  repeated  52 times, 12 mm apart along
  friction  0.72, spinning 0, rolling 0
  bounce    dead

left cart guide
  is a      box 70 by 1 by 12 cm
  at        55 cm along, 10.5 cm to the left, 46 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

right cart guide
  is a      box 70 by 1 by 12 cm
  at        55 cm along, 10.5 cm to the right, 46 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

cart1
  is a      box 22 by 18 by 10 cm, 0.50 kg
  moves     freely
  at        35 cm along, 0 m to the left, 46.2 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    grey

domino pedestal
  is a      box 8 by 8 by 40 cm
  stands    on floor, 92 cm along, 0 m to the left
  friction  0.72, spinning 0, rolling 0
  bounce    dead

domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  stands    on domino pedestal, 92 cm along, 0 m to the left
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    wood

-- The horizontal perch keeps ball2 still until the domino hits it.
ball perch
  is a      box 10 by 18 by 2 cm
  at        1.10 m along, 0 m to the left, 50.08 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  on        ball perch, 18 cm beyond domino1, 0 m to the left
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    orange

ramp high end
  is a  point
  at    1.14 m along, 0 m to the left, 49.202014 cm up

ramp low end
  is a  point
  at    2.07969262 m along, 0 m to the left, 15 cm up

ramp1
  is a      plank from ramp high end to ramp low end, 30 cm wide, 4 cm thick
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    wood

-- The panel's near face is 10 cm beyond the ramp's low end.
door1
  is a           box 4 by 42 by 32 cm, 0.45 kg
  at             2.19969262 m along, 0 m to the left, 18 cm up
  turns on       door hinge, about z, at its right side
  swings         from -70° to 0°
  starts turned  0°
  damping        0.04 N·m·s/rad
  friction       0.72, spinning 0, rolling 0
  bounce         dead
  colour         wood

pendulum pivot
  is a  point
  at    40 cm beyond door1, 6.635 cm to the right, 60 cm up

pendulum upper end
  is a  point
  at    40 cm beyond door1, 6.635 cm to the right, 59 cm up

pendulum lower end
  is a  point
  at    40 cm beyond door1, 6.635 cm to the right, 11 cm up

-- Including its capsule end caps, this rigid pendulum is 50 cm long.
pendulum1
  is a           rod 2 cm thick, from pendulum upper end to pendulum lower end
  weighs         0.35 kg
  turns on       pendulum hinge, about y, at pendulum pivot
  swings         from -38° to 0°
  starts turned  0°
  damping        0.04 N·m·s/rad
  friction       0.72, spinning 0, rolling 0
  bounce         dead
  colour         grey

block pedestal
  is a      box 22 by 22 by 4 cm
  at        36.8 cm beyond pendulum pivot, 6.635 cm to the right, 16 cm up
  friction  0.72, spinning 0, rolling 0
  bounce    dead

block1
  is a      cube 12 cm, 0.35 kg
  moves     freely
  on        block pedestal, 36.8 cm beyond pendulum pivot, 6.635 cm to the right
  friction  0.72, spinning 0, rolling 0
  bounce    dead
  colour    wood

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever1 reaches its lower stop
  lever striking face touches cart1
  cart1 touches domino1
  domino1 touches ball2
  ball2 touches ramp1
  ball2 touches door1
  door1 reaches its lower stop
  door1 touches pendulum1
  pendulum1 reaches its lower stop
  pendulum1 touches block1
```