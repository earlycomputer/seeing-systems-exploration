```world
world  spring chain scaffold

-- Gravity must come from the compiler default; this language cannot set it.
-- Numerical restitution 0.05 cannot be specified.
-- Cart1's slide joint, 18 N/m spring, 0.20 m compression,
-- and 0.20 N s/m slide damping cannot be expressed.
-- This remains a geometric scaffold, not a verified spring-driven chain.
-- All moving bodies start with zero velocity.

floor
  size      6 m
  friction  0.68

ramp high point
  is a  point
  at    0 m along, 0 m to the left, 0.487322 m up

ramp low point
  is a  point
  at    0.939693 m along, 0 m to the left, 0.145302 m up

-- Endpoint separation is 1.00 m at 20 degrees.
-- With this deck thickness, its upper low edge is 0.15 m high.
ramp1
  is a      plank from ramp high point to ramp low point, 0.30 m wide, 0.01 m thick
  friction  0.68
  colour    wood

cart support
  is a      box 0.75 by 0.30 by 0.02 m
  raised    0.469006 m, 0.425 m behind ramp high point
  friction  0.68
  colour    grey

-- Positioned 0.50 m before the approximate first-contact location.
-- This is a free cart, not the unsupported axial slide mechanism.
cart1
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  on        cart support, 0.642899 m behind ramp high point
  friction  0.68
  colour    orange

ball1
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  on        ramp1, 0 m from the top
  friction  0.68
  colour    white

pendulum pivot
  is a  point
  at    1.089693 m along, 0 m to the left, 0.655 m up

-- Explicitly align the bob beneath its pivot in both horizontal axes.
-- This keeps the rod vertical and clear of ramp1.
-- Bob plus rod mass is 0.35 kg; pivot-to-bob-centre length is 0.50 m.
pendulum1
  is a          sphere 0.10 m across, 0.30 kg
  at            1.089693 m along, 0 m to the left, 0.155 m up
  turns on      pendulum1 hinge, about y, at pendulum pivot
  swings        from -40° to 0°
  damping       0.04 N·m·s/rad
  starts turned 0°
  friction      0.68
  colour        orange

pendulum rod
  is a         rod 0.01 m thick, from pendulum pivot to pendulum1's top
  weighs       0.05 kg
  attached to  pendulum1
  friction     0.68
  colour       grey

-- Vertical panel: 0.42 m wide, 0.32 m high, 0.04 m thick.
-- Its lower angular stop is the clockwise 70-degree position.
door1
  is a          box 0.04 by 0.42 by 0.32 m, 0.45 kg
  raised        0.02 m, 1.481087 m along, 0 m to the left
  turns on      door1 hinge, about z, at its right side
  swings        from -70° to 0°
  damping       0.04 N·m·s/rad
  starts turned 0°
  friction      0.68
  colour        wood

block1
  is a      cube 0.12 m, 0.35 kg
  moves     freely
  on        floor, 1.92 m along, 0.068 m to the right
  friction  0.68
  colour    orange
```