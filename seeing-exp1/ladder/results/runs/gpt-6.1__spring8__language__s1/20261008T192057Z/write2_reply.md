```world
world  guided spring chain approximation

-- Ramp endpoint parameters now contain complete position clauses.
-- This remains an unverified approximation, not an exact implementation.
-- Gravity relies on the compiler's default.
-- Every moving body starts with zero velocity.
-- "bounce dead" does not document an exact restitution of 0.05.
-- Physical guides approximate slides; exact slide damping is unavailable.

floor
  size      6 m
  friction  0.68, spinning 0, rolling 0

ramp high point
  is a  point
  at    0 m along, 0 m to the left, 0.492020143 m up

ramp low point
  is a  point
  at    0.939692621 m along, 0 m to the left, 0.15 m up

ramp1
  is a       ramp
  high end   0 m beyond ramp high point, 0 m left of ramp high point, level with ramp high point
  low end    0 m beyond ramp low point, 0 m left of ramp low point, level with ramp low point
  width      0.30 m
  thickness  0.04 m
  friction   0.68, spinning 0, rolling 0
  bounce     dead

ball1
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        ramp1, 0 m from the top

-- A vertical guide allows gravity to assist the cart spring.
-- This is not the brief's exact axial slide joint.

cart1
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0.145 m behind ball1, 0 m left of ball1, 0.585707142 m above ball1

cart1 left guide
  is a      box 0.30 by 0.02 by 0.60 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0 m beyond cart1, 0.11 m left of cart1, 1.04 m up

cart1 right guide
  is a      box 0.30 by 0.02 by 0.60 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0 m beyond cart1, 0.11 m right of cart1, 1.04 m up

cart1 near guide
  is a      box 0.02 by 0.22 by 0.60 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0.13 m behind cart1, 0 m left of cart1, 1.04 m up

cart1 far guide
  is a      box 0.02 by 0.22 by 0.60 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0.13 m beyond cart1, 0 m left of cart1, 1.04 m up

cart1 catch
  is a      box 0.04 by 0.18 by 0.57 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 0.09 m behind cart1, 0 m left of cart1

cart1 driver pivot
  is a  point
  at    1 m behind cart1, 0 m left of cart1, 0.055 m above cart1

-- A one-metre arm maps 18 N m/rad approximately to 18 N/m at its tip.
-- Its 0.20-radian preload approximates 0.20 m compression.
-- It is not an exact axial spring.

cart1 spring driver
  is a           box 1.00 by 0.06 by 0.01 m, 0.01 kg
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  at             0.50 m beyond cart1 driver pivot, 0 m left of cart1 driver pivot, level with cart1 driver pivot
  turns on       cart1 driver hinge, about y, at cart1 driver pivot
  swings         from 0 deg to 11.459155903 deg
  spring         18 N·m/rad toward 11.459155903 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

-- The cart-operated gate retains ball1 until cart1 descends.

ball1 gate pivot
  is a  point
  at    0.06 m beyond ball1, 0.15 m left of ball1, level with ball1

ball1 gate
  is a           box 0.02 by 0.30 by 0.12 m, 0.005 kg
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  at             0.06 m beyond ball1, 0 m left of ball1, level with ball1
  turns on       ball1 gate hinge, about x, at ball1 gate pivot
  swings         from 0 deg to 85 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

ball1 gate pedal
  is a         box 0.08 by 0.10 by 0.01 m, 0.005 kg
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  at           0.145 m behind ball1, 0 m left of ball1, 0.030707142 m above ball1
  attached to  ball1 gate

pendulum1 pivot
  is a  point
  at    0.15 m beyond ramp low point, 0 m left of ramp low point, 0.705 m up

pendulum1
  is a           sphere 0.10 m across, 0.33 kg
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  at             0 m beyond pendulum1 pivot, 0 m left of pendulum1 pivot, 0.50 m below pendulum1 pivot
  turns on       pendulum1 hinge, about y, at pendulum1 pivot
  swings         from -40 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

pendulum1 rod
  is a         rod 0.01 m thick, from pendulum1 pivot to pendulum1's top
  weighs       0.02 kg
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  attached to  pendulum1

-- The rod and bob together weigh 0.35 kg.
-- The pivot-to-bob-centre distance is 0.50 m.

door1
  is a           box 0.04 by 0.42 by 0.32 m, 0.45 kg
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  at             1.481086426 m along, 0 m to the left, 0.18 m up
  turns on       door1 hinge, about z, at its right side
  swings         from -70 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

block1
  is a      cube 0.12 m, 0.35 kg
  moves     freely
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 1.942597730 m along, 0.066351540 m to the right

domino1
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 0.42 m beyond block1, 0 m left of block1

lever1 pivot
  is a  point
  at    0.33 m beyond domino1, 0 m left of domino1, 0.429254957 m up

lever1
  is a           box 0.60 by 0.10 by 0.04 m, 0.50 kg
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  at             0 m beyond lever1 pivot, 0 m left of lever1 pivot, level with lever1 pivot
  turns on       lever1 hinge, about y, at lever1 pivot
  swings         from -105 deg to -60 deg
  damping        0.04 N·m·s/rad
  starts turned  -60 deg

-- A light scoop retains ball2 on the initially elevated right end.
-- The scoop adds 0.002 kg beyond the specified bare lever mass.

lever1 scoop base
  is a         box 0.12 by 0.10 by 0.004 m, 0.001 kg
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  on           lever1, centred on lever1's far end
  attached to  lever1

lever1 scoop back
  is a         box 0.006 by 0.10 by 0.10 m, 0.001 kg
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  on           lever1 scoop base, at lever1 scoop base's near end
  attached to  lever1

ball2
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        0.082414120 m beyond lever1 pivot, 0 m left of lever1 pivot, 0.72 m up

-- An auxiliary guide redirects the launched ball away from the domino lane.
-- This additional guide is an approximation aid, not specified in the brief.

ball2 guide high point
  is a  point
  at    2.49 m along, 0.066351540 m to the right, 0.66 m up

ball2 guide low point
  is a  point
  at    2.27 m along, 0.32 m to the right, 0.49 m up

ball2 landing guide
  is a      plank from ball2 guide high point to ball2 guide low point, 0.20 m wide, 0.01 m thick
  friction  0.68, spinning 0, rolling 0
  bounce    dead

-- The ring uses the language's nominal diameter.
-- Exact clear diameter depends on the compiler's tube convention.

ring1
  is a      ring 0.16 m across, 0.008 m thick
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  at        2.17 m along, 0.40 m to the right, 0.32 m below ball2
  colour    orange

cart2
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 0 m beyond ring1, 0 m left of ring1

cart2 left guide
  is a      box 0.80 by 0.02 by 0.10 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 0 m beyond cart2, 0.105 m left of cart2

cart2 right guide
  is a      box 0.80 by 0.02 by 0.10 m
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  on        floor, 0 m beyond cart2, 0.105 m right of cart2

-- These are intended checks, not claims that an untested run passes.

expect
  cart1 touches ball1
  ball1 touches ramp1
  ball1 touches pendulum1
  pendulum1 reaches its lower stop
  pendulum1 touches door1
  door1 reaches its lower stop
  door1 touches block1
  block1 touches domino1
  domino1 touches lever1
  lever1 reaches its lower stop
  ball2 drops through ring1
  ball2 touches cart2
```