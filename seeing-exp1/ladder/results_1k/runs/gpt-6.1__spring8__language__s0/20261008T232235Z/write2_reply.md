I moved the bearing row 11 mm back, leaving 1 mm clearance between its last roller and `ramp1.leg`.

```world
world  spring cart and gravity chain approximation

-- MuJoCo's default gravity is 9.81 m/s2.
-- No body has a launch velocity or starting spin.
-- "dead" approximates, but does not specify, restitution 0.05.
-- Contact guides substitute for unavailable slide joints.
-- Exact linear spring and slide damping settings remain unexpressible.
-- Expectations describe intended outcomes, not verified results.

floor
  size      8 m
  friction  0.68, spinning 0, rolling 0

-- A 1.00 m deck at 20 degrees.
-- Endpoint heights account for the 2 cm deck thickness.

ramp high
  is a  point
  at    0 m along, 0 m to the left, 0.482623 m up

ramp low
  is a  point
  at    0.939693 m along, 0 m to the left, 0.140603 m up

ramp1
  is a       ramp
  high end   ramp high
  low end    ramp low
  width      0.30 m
  thickness  0.02 m
  friction   0.68, spinning 0, rolling 0
  bounce     dead
  colour     wood

cart1 runway
  is a      box 1.20 by 0.20 by 0.04 m
  at        -0.60 m along, 0 m to the left, 0.449005 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    grey

-- Shifted 11 mm backward.
-- Bearing20 is centred at x = -0.041 m.
-- Its forward surface is at x = -0.031 m.
-- Ramp1's leg begins at x = -0.030 m.

bearing left endpoint
  is a  point
  at    -0.991 m along, 0.07 m to the left, 0.479005 m up

bearing right endpoint
  is a  point
  at    -0.991 m along, 0.07 m to the right, 0.479005 m up

runway bearing
  is a      rod 2 cm thick, from bearing left endpoint to bearing right endpoint
  weighs    1 g
  moves     freely
  repeated  20 times, 5 cm apart along
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    grey

cart1 left guide
  is a      box 1.20 by 0.02 by 0.025 m
  at        -0.60 m along, 0.11 m to the left, 0.501505 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

cart1 right guide
  is a      box 1.20 by 0.02 by 0.025 m
  at        -0.60 m along, 0.11 m to the right, 0.501505 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

cart1
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  at        -0.639479 m along, 0 m to the left, 0.539005 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    orange

-- Rotational approximation to the axial launch spring.
-- A 2 m radius and 72 N m/rad approximate 18 N/m locally.
-- Initial deflection stores 0.36 J.
-- The driver stops after approximately 0.20 m of travel.

cart1 driver pivot
  is a  point
  at    -0.754479 m along, 2 m to the right, 0.539005 m up

cart1 driver tip
  is a  point
  at    -0.754479 m along, 0 m to the left, 0.539005 m up

cart1 spring driver
  is a           rod 1 cm thick, from cart1 driver pivot to cart1 driver tip
  weighs         5 g
  turns on       cart1 driver hinge, about z, at cart1 driver pivot
  swings         from -5.729578° to 0°
  spring         72 N·m/rad toward -5.729578°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  colour         grey

-- A short horizontal ledge supports ball1 before the cart arrives.
-- The initial cart-to-ball surface gap is 0.50 m.

ball1 starting ledge
  is a      box 0.04 by 0.30 by 0.02 m
  at        0.005 m along, 0 m to the left, 0.479005 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    wood

ball1
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  at        0.020521 m along, 0 m to the left, 0.539005 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    orange

-- Pivot-to-bob-centre length is 0.50 m.
-- Bob and rigid rod together weigh 0.35 kg.

pendulum pivot
  is a  point
  at    1.089693 m along, 0 m to the left, 0.68 m up

pendulum1
  is a           sphere 0.10 m across, 0.15 kg
  at             1.089693 m along, 0 m to the left, 0.18 m up
  turns on       pendulum1 hinge, about y, at pendulum pivot
  swings         from -80° to 15°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  colour         grey

pendulum rigid rod
  is a         rod 2 cm thick, from pendulum pivot to pendulum1's top
  weighs       0.20 kg
  attached to  pendulum1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       grey

pendulum support top
  is a  point
  at    1.089693 m along, 0.24 m to the left, 0.71 m up

pendulum support post
  is a      post 4 cm square, from floor to pendulum support top
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

pendulum support beam
  is a      box 0.04 by 0.24 by 0.02 m
  at        1.089693 m along, 0.12 m to the left, 0.70 m up
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

-- The bob reaches the upright panel at a 40 degree forward swing.
-- Panel dimensions: 0.42 m high, 0.32 m wide, 0.04 m thick.

door pivot
  is a  point
  at    1.481087 m along, 0 m to the left, 0.02 m up

door1
  is a           box 0.04 by 0.32 by 0.42 m, 0.45 kg
  at             1.481087 m along, 0 m to the left, 0.23 m up
  turns on       door1 hinge, about y, at door pivot
  swings         from 0° to 70°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  colour         wood

block1
  is a      cube 0.12 m, 0.35 kg
  moves     freely
  on        floor, 1.80 m along, 0 m to the left
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    grey

-- Initial block-to-domino surface gap: 0.32 m.

domino1
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  on        floor, 2.22 m along, 0 m to the left
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    white

-- The arm and attached striker/lips together weigh 0.50 kg.
-- The hanging striker is an additional geometric approximation.

lever pivot
  is a  point
  at    2.70 m along, 0 m to the left, 0.65 m up

lever1
  is a           box 0.60 by 0.10 by 0.04 m, 0.490 kg
  at             2.70 m along, 0 m to the left, 0.65 m up
  turns on       lever1 hinge, about y, at lever pivot
  swings         from -45° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.68, spinning 0, rolling 0
  bounce         dead
  colour         wood

lever striker upper
  is a  point
  at    2.40 m along, 0.12 m to the left, 0.65 m up

lever striker lower
  is a  point
  at    2.40 m along, 0.12 m to the left, 0.20 m up

lever striker contact
  is a  point
  at    2.40 m along, 0 m to the left, 0.20 m up

lever striker top crossbar
  is a         rod 2 cm thick, from lever1's near end to lever striker upper
  weighs       1 g
  attached to  lever1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       grey

lever striker vertical
  is a         rod 2 cm thick, from lever striker upper to lever striker lower
  weighs       4 g
  attached to  lever1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       grey

lever striker foot
  is a         rod 2 cm thick, from lever striker lower to lever striker contact
  weighs       1 g
  attached to  lever1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       grey

lever near retaining lip
  is a         box 0.01 by 0.12 by 0.035 m, 2 g
  on           lever1, 0.19 m beyond lever1
  attached to  lever1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       wood

lever far retaining lip
  is a         box 0.01 by 0.12 by 0.035 m, 2 g
  on           lever1, 0.31 m beyond lever1
  attached to  lever1
  friction     0.68, spinning 0, rolling 0
  bounce       dead
  colour       wood

ball2
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  on        lever1, 0.25 m beyond lever1
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    orange

-- Nominal catcher position, not simulation-tuned.
-- Ring height is 0.32 m below ball2's initial centre.

ring1
  is a      ring 0.16 m across, 6 mm thick
  at        0.32 m behind ball2, 0.32 m below ball2
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    orange

-- Physical guides substitute for cart2's slide joint.
-- The specified 0.20 N s/m slide damping cannot be represented.

cart2 left guide
  is a      box 0.60 by 0.02 by 0.03 m
  on        floor, 2.57 m along, 0.11 m to the left
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

cart2 right guide
  is a      box 0.60 by 0.02 by 0.03 m
  on        floor, 2.57 m along, 0.11 m to the right
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    dark grey

cart2
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  on        floor, 2.57 m along, 0 m to the left
  friction  0.68, spinning 0, rolling 0
  bounce    dead
  colour    orange

expect
  cart1 touches ball1
  ball1 touches ramp1
  ball1 touches pendulum1
  pendulum1 touches door1
  door1 reaches its upper stop
  door1 touches block1
  block1 touches domino1
  domino1 touches lever1
  lever1 reaches its lower stop
  ball2 drops through ring1
  ball2 touches cart2
```