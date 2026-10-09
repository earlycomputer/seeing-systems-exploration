```world
world  spring and gravity cascade

-- Gravity is the language default: 9.81 m/s².
-- No starting velocities or spins are assigned.

floor
  size      8 m
  friction  0.68, spinning 0.005, rolling 0.002

ramp high
  is a  point
  at    0 m along, 0 m to the left, 0.473227 m up

ramp low
  is a  point
  at    0.939693 m along, 0 m to the left, 0.131206 m up

-- The deck is 1.00 m long at 20 degrees.
-- Its low-end upper surface is 0.15 m above the floor.
ramp1
  is a       ramp
  high end   ramp high
  low end    ramp low
  width      0.30 m
  thickness  0.04 m
  friction   0.68, spinning 0.005, rolling 0.002
  bounce     0.05

ball1 starting shelf
  is a      box 12 by 18 by 2 cm
  at        0.063941 m behind ramp high, 0 m to the left, 0.479005 m up
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05

-- A second, initially stationary spring pusher supplies supplemental energy.
-- Without it, the cart's 0.20 m preload cannot produce a 0.50 m
-- horizontal stroke, even in the absence of losses.
cart1 spring pusher
  is a       box 5 by 12 by 6 cm, 100 g
  at         0.818941 m behind ramp high, 0 m to the left, 0.539005 m up
  slides on  pusher track, along x
  travels    from 0 cm to 50 cm
  spring     12 N/m toward 80 cm
  damping    0.20 N·s/m
  friction   0.68, spinning 0.005, rolling 0.002
  bounce     0.05

cart1
  is a          box 22 by 18 by 10 cm, 0.50 kg
  at            0.483941 m behind ramp high, 0 m to the left, 0.539005 m up
  slides on     cart1 track, along x
  travels       from −20 cm to 32 cm
  spring        18 N/m toward 0 cm
  damping       0.20 N·s/m
  starts slid   −20 cm
  friction      0.68, spinning 0.005, rolling 0.002
  bounce        0.05

-- At its initial slide position, cart1's front is 0.50 m
-- behind the first contact position with ball1.
ball1
  is a      sphere 10 cm across, 0.20 kg
  at        0.023941 m behind ramp high, 0 m to the left, 0.539005 m up
  moves     freely
  rolls
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05

pendulum pivot
  is a  point
  at    1.089693 m along, 0 m to the left, 0.65 m up

-- Bob plus rigid rod have total mass 0.35 kg.
-- Pivot-to-bob-centre length is 0.50 m.
pendulum1
  is a           sphere 10 cm across, 0.30 kg
  at             0.50 m below pendulum pivot, 1.089693 m along, 0 m to the left
  turns on       pendulum1 hinge, about y, at pendulum pivot
  swings         from −50 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg
  friction       0.68, spinning 0.005, rolling 0.002
  bounce         0.05

pendulum rod
  is a         rod 1 cm thick, from pendulum pivot to pendulum1's top
  weighs       0.05 kg
  attached to  pendulum1
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

-- The panel is 0.42 m high, 0.32 m wide and 0.04 m thick.
-- Negative z rotation is clockwise viewed from above.
door1
  is a           box 4 by 32 by 42 cm, 0.45 kg
  at             1.481087 m along, 0 m to the left, 0.23 m up
  turns on       door1 hinge, about z, at its right side
  swings         from −70 deg to 0 deg
  spring         2.5 N·m/rad toward −70 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg
  friction       0.68, spinning 0.005, rolling 0.002
  bounce         0.05

door latch tooth
  is a         box 6 by 4 by 2 cm, 5 g
  at           2 cm beyond door1, 12 cm to the left, 0.45 m up
  attached to  door1
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

-- The latch reacts the door's preload horizontally.
-- Its vertical slide can be lifted by the rising pendulum bob.
door release latch
  is a       box 4 by 4 by 2 cm, 20 g
  at         7 cm beyond door1, 12 cm to the left, 0.45 m up
  slides on  door release track, along z
  travels    from 0 cm to 6 cm
  damping    0.20 N·s/m
  friction   0.68, spinning 0.005, rolling 0.002
  bounce     0.05

latch outer corner
  is a  point
  at    7 cm beyond door1, 20 cm to the left, 0.45 m up

latch rear corner
  is a  point
  at    1.411087 m along, 20 cm to the left, 0.45 m up

latch upper pickup
  is a  point
  at    1.411087 m along, 0 m to the left, 0.45 m up

latch pickup point
  is a  point
  at    1.411087 m along, 0 m to the left, 0.326978 m up

latch outer link
  is a         rod 6 mm thick, from door release latch to latch outer corner
  weighs       3 g
  attached to  door release latch
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

latch overhead link
  is a         rod 6 mm thick, from latch outer corner to latch rear corner
  weighs       3 g
  attached to  door release latch
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

latch cross link
  is a         rod 6 mm thick, from latch rear corner to latch upper pickup
  weighs       3 g
  attached to  door release latch
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

latch pickup link
  is a         rod 6 mm thick, from latch upper pickup to latch pickup point
  weighs       3 g
  attached to  door release latch
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

latch pickup
  is a         sphere 1 cm radius, 5 g
  at           latch pickup point
  attached to  door release latch
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

block1
  is a      cube 12 cm, 0.35 kg
  on        floor, 1.846627 m along, 0.050553 m to the right
  moves     freely
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05

-- Initial face-to-face separation from block1 is 0.32 m.
domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  on        floor, 0.42 m beyond block1, 0.050553 m to the right
  moves     freely
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05

-- This ledge holds the preloaded lever until the falling domino
-- pushes the ledge forward.
lever release latch
  is a       box 16 by 80 by 20 mm, 20 g
  at         0.18 m beyond domino1, 0.050553 m to the right, 0.145385 m up
  slides on  lever release track, along x
  travels    from 0 cm to 12 cm
  damping    0.20 N·s/m
  friction   0.68, spinning 0.005, rolling 0.002
  bounce     0.05

lever pivot
  is a  point
  at    0.312680 m beyond domino1, 0.050553 m to the right, 0.425192 m up

-- The initial tilt puts the left end within reach of the domino
-- while elevating the ball-carrying right end.
-- The arm and its two cradle pieces have total mass 0.50 kg.
lever1
  is a           box 60 by 10 by 4 cm, 0.49 kg
  at             lever pivot
  turns on       lever1 hinge, about y, at lever pivot
  swings         from −105 deg to −60 deg
  spring         2 N·m/rad toward −105 deg
  damping        0.04 N·m·s/rad
  starts turned  −60 deg
  friction       0.68, spinning 0.005, rolling 0.002
  bounce         0.05

-- These positions are in the lever's unturned configuration.
lever cradle support
  is a         sphere 5 mm radius, 5 g
  at           0.252372 m beyond lever1, 0.050553 m to the right, 0.467692 m up
  attached to  lever1
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

lever cradle back
  is a         sphere 5 mm radius, 5 g
  at           0.272501 m beyond lever1, 0.050553 m to the right, 0.542828 m up
  attached to  lever1
  friction     0.68, spinning 0.005, rolling 0.002
  bounce       0.05

ball2
  is a      sphere 10 cm across, 0.20 kg
  at        0.089378 m beyond lever1, 0.050553 m to the right, 0.72 m up
  moves     freely
  rolls
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05

-- An 8 mm tube on a 16.8 cm centreline diameter leaves
-- a nominal 16 cm clear opening.
-- The ring plane is 0.32 m below ball2's initial centre.
ring1
  is a      ring 16.8 cm across, 8 mm thick
  at        0.40 m behind lever1, 0.050553 m to the right, 0.40 m up
  friction  0.68, spinning 0.005, rolling 0.002
  bounce    0.05
  colour    orange

-- Ball-centre height at contact is 0.15 m:
-- another 0.25 m below the ring plane.
cart2
  is a       box 22 by 18 by 10 cm, 0.50 kg
  on         floor, 0.12 m behind ring1, 0.050553 m to the right
  slides on  cart2 track, along x
  travels    from −50 cm to 0 cm
  damping    0.20 N·s/m
  friction   0.68, spinning 0.005, rolling 0.002
  bounce     0.05

expect
  cart1 touches ball1
  ball1 touches ramp1
  ball1 touches pendulum1
  pendulum1 touches door1
  door1 reaches its lower stop
  door1 touches block1
  block1 touches domino1
  domino1 touches lever1
  lever1 reaches its lower stop
  ball2 drops through ring1
  ball2 touches cart2
```