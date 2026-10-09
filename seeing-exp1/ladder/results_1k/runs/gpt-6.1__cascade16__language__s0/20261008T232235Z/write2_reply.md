```parts
part final catch bin
  base
    is a  box 0.36 by 0.36 by 0.02 m
    on    floor

  near wall
    is a  box 0.02 by 0.36 by 0.20 m
    on    base, its near end at base's near end

  far wall
    is a  box 0.02 by 0.36 by 0.20 m
    on    base, its far end at base's far end

  left wall
    is a  box 0.32 by 0.02 by 0.20 m
    on    base, its left side at base's left side

  right wall
    is a  box 0.32 by 0.02 by 0.20 m
    on    base, its right side at base's right side
```

```world
world  guided gravity chain draft

-- This is an untested approximation, not a verified exact realization.
-- The grammar cannot specify numeric restitution or linear slide damping.
-- Dead contacts approximate the requested low restitution.
-- Contact guides approximate horizontal slides.
-- Auxiliary gravity weights change the mechanisms' effective masses and inertias.
-- Gravity relies on MuJoCo's standard 9.81 m/s2 default.
-- All free bodies and hinges start with zero velocity.
-- The expect block contains tests to run, not claims that they have passed.

floor
  size      24 m
  friction  0.70, spinning 0, rolling 0

-- Ramp endpoints are deck centreline endpoints.
-- Their separation is 1.00 m at 20 degrees.
-- With a 0.04 m deck, the low top surface is at 0.15 m.

ramp1 high
  is a  point
  at    0 m along, 0 m across, 0.473226291 m up

ramp1 low
  is a  point
  at    0.939692621 m beyond ramp1 high, 0.131206148 m up

ramp1
  is a      plank from ramp1 high to ramp1 low, 0.30 m wide, 0.04 m thick
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    wood

ball1
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  at        0.023941410 m beyond ramp1 high, 0.539004774 m up
  colour    orange

domino1
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  stands    on floor, 0.146840403 m beyond ramp1 low
  colour    white

domino2
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  stands    on floor, 0.18 m beyond domino1
  colour    white

flap1
  is a           box 0.04 by 0.20 by 0.40 m, 0.30 kg
  friction       0.70, spinning 0, rolling 0
  bounce         dead
  at             0.18 m beyond domino2, 0.35 m up
  turns on       flap1 hinge, about y, at its bottom
  swings         from 0° to 65°
  damping        0.04 N·m·s/rad
  starts turned  0°
  colour         wood

-- A balanced upright gravity driver is tipped by flap1's impact.
-- Its side mast keeps the striker's support outside the cart channel.

flap1 side foot
  is a  point
  at    0 m beyond flap1, 0.35 m left of flap1, 0.16 m up

flap1 side top
  is a  point
  at    0 m beyond flap1, 0.35 m left of flap1, 1.11 m up

flap1 striker place
  is a  point
  at    0 m beyond flap1, 1.11 m up

flap1 side mast
  is a         rod 0.012 m thick, from flap1 side foot to flap1 side top
  weighs       0.02 kg
  attached to  flap1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

flap1 striker bar
  is a         rod 0.008 m thick, from flap1 side top to flap1 striker place
  weighs       0.01 kg
  attached to  flap1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

flap1 striker
  is a         sphere 0.03 m radius, 0.02 kg
  at           0 m beyond flap1 striker place, level with flap1 striker place
  attached to  flap1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

flap1 gravity weight
  is a         sphere 0.04 m radius, 20 kg
  at           0 m beyond flap1, 0.35 m left of flap1, 0.27 m up
  attached to  flap1
  friction     0.70, spinning 0, rolling 0
  bounce       dead
  colour       dark grey

cart1
  is a      box 0.22 by 0.18 by 0.10 m, 0.50 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  at        0.98 m beyond flap1, 0.539004774 m up
  colour    grey

cart1 slide base
  is a      box 0.72 by 0.26 by 0.04 m
  at        1.18 m beyond flap1, 0.469004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

cart1 slide left
  is a      box 0.80 by 0.02 by 0.12 m
  at        1.32 m beyond flap1, 0.115 m left of flap1, 0.539004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

cart1 slide right
  is a      box 0.80 by 0.02 by 0.12 m
  at        1.32 m beyond flap1, 0.115 m right of flap1, 0.539004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

cart1 slide roof
  is a      box 0.80 by 0.26 by 0.02 m
  at        1.32 m beyond flap1, 0.609004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

cart1 left stop
  is a      box 0.02 by 0.03 by 0.10 m
  at        0.57 m beyond cart1, 0.075 m left of cart1, 0.539004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

cart1 right stop
  is a      box 0.02 by 0.03 by 0.10 m
  at        0.57 m beyond cart1, 0.075 m right of cart1, 0.539004774 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

ramp2 high
  is a  point
  at    0.586058590 m beyond cart1, 0.473226291 m up

ramp2 low
  is a  point
  at    0.939692621 m beyond ramp2 high, 0.131206148 m up

ramp2
  is a      plank from ramp2 high to ramp2 low, 0.30 m wide, 0.04 m thick
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    wood

ball2
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  at        0.023941410 m beyond ramp2 high, 0.539004774 m up
  colour    orange

-- A retaining corner prevents ball2 from independently starting at time zero.
-- Cart1 must strike it over this corner.

ball2 retaining lip
  is a      box 0.014 by 0.12 by 0.03 m
  at        0.051 m beyond ball2, 0.500256090 m up
  friction  0.70, spinning 0, rolling 0
  bounce    dead

-- Lever1 is initially inclined 60 degrees.
-- Its centreline is 0.60 m long.
-- Turning by -45 degrees lowers its left endpoint from 0.18 to 0.15 m.

lever1 left
  is a  point
  at    0.144160911 m beyond ramp2 low, 0.18 m up

lever1 right
  is a  point
  at    0.30 m beyond lever1 left, 0.519615242 m above lever1 left

lever1 pivot
  is a  point
  at    0.15 m beyond lever1 left, 0.259807621 m above lever1 left

lever1
  is a           plank from lever1 left to lever1 right, 0.10 m wide, 0.04 m thick
  weighs         0.50 kg
  friction       0.70, spinning 0, rolling 0
  bounce         dead
  turns on       lever1 hinge, about y, at lever1 pivot
  swings         from -45° to 0°
  spring         0.75 N·m/rad toward 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  colour         wood

lever1 cup
  is a         box 0.06 by 0.04 by 0.02 m, 0.02 kg
  at           0 m beyond lever1 right, 0.01 m above lever1 right
  attached to  lever1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

lever1 counterweight place
  is a  point
  at    0 m beyond lever1 left, 0.20 m left of lever1 left, 0.04 m above lever1 left

lever1 counterweight arm
  is a         rod 0.006 m thick, from lever1 left to lever1 counterweight place
  weighs       0.002 kg
  attached to  lever1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

lever1 counterweight
  is a         sphere 0.04 m radius, 0.218 kg
  at           0 m beyond lever1 left, 0.20 m left of lever1 left, 0.04 m above lever1 left
  attached to  lever1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

lever1 gravity mast
  is a         box 0.012 by 0.012 by 0.20 m, 0.01 kg
  at           0 m beyond lever1 pivot, 0.25 m left of lever1 pivot, 0.10 m above lever1 pivot
  attached to  lever1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

lever1 gravity weight
  is a         sphere 0.04 m radius, 0.50 kg
  at           0 m beyond lever1 pivot, 0.25 m left of lever1 pivot, 0.20 m above lever1 pivot
  attached to  lever1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

ball3
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  at        0 m beyond lever1 right, 0.07 m above lever1 right
  colour    orange

-- Four corner guides constrain the launch and return path.
-- They begin above the lever's swept panel.

ball3 guide near left
  is a      box 0.008 by 0.008 by 1.20 m
  at        0.041 m behind ball3, 0.041 m left of ball3, 0.575 m above ball3
  friction  0.70, spinning 0, rolling 0
  bounce    dead

ball3 guide near right
  is a      box 0.008 by 0.008 by 1.20 m
  at        0.041 m behind ball3, 0.041 m right of ball3, 0.575 m above ball3
  friction  0.70, spinning 0, rolling 0
  bounce    dead

ball3 guide far left
  is a      box 0.008 by 0.008 by 1.20 m
  at        0.041 m beyond ball3, 0.041 m left of ball3, 0.575 m above ball3
  friction  0.70, spinning 0, rolling 0
  bounce    dead

ball3 guide far right
  is a      box 0.008 by 0.008 by 1.20 m
  at        0.041 m beyond ball3, 0.041 m right of ball3, 0.575 m above ball3
  friction  0.70, spinning 0, rolling 0
  bounce    dead

ring1
  is a      ring 0.16 m across, 0.008 m thick
  at        0.35 m below ball3, centred over ball3
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    orange

-- A lateral bob offset supplies an impact torque.
-- The rigid side frame routes the pendulum around ring1 rather than through its rim.

pendulum1 bob rest
  is a  point
  at    0.07 m beyond ball3, 0.671414284 m below ball3

pendulum1 pivot
  is a  point
  at    0.50 m above pendulum1 bob rest, centred over pendulum1 bob rest

pendulum1 outer pivot
  is a  point
  at    0 m beyond pendulum1 pivot, 0.15 m left of pendulum1 pivot, level with pendulum1 pivot

pendulum1 outer bob
  is a  point
  at    0 m beyond pendulum1 bob rest, 0.15 m left of pendulum1 bob rest, level with pendulum1 bob rest

pendulum1
  is a           sphere 0.10 m across, 0.34 kg
  at             0 m beyond pendulum1 bob rest, level with pendulum1 bob rest
  turns on       pendulum1 hinge, about y, at pendulum1 pivot
  swings         from -40° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°
  friction       0.70, spinning 0, rolling 0
  bounce         dead
  colour         dark grey

pendulum1 top arm
  is a         rod 0.008 m thick, from pendulum1 pivot to pendulum1 outer pivot
  weighs       0.002 kg
  attached to  pendulum1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

pendulum1 side rod
  is a         rod 0.008 m thick, from pendulum1 outer pivot to pendulum1 outer bob
  weighs       0.006 kg
  attached to  pendulum1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

pendulum1 bottom arm
  is a         rod 0.008 m thick, from pendulum1 outer bob to pendulum1 bob rest
  weighs       0.002 kg
  attached to  pendulum1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

pendulum1 gravity mast
  is a         box 0.012 by 0.012 by 0.30 m, 0.01 kg
  at           0 m beyond pendulum1 pivot, 0.35 m left of pendulum1 pivot, 0.15 m above pendulum1 pivot
  attached to  pendulum1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

pendulum1 gravity weight
  is a         sphere 0.035 m radius, 2 kg
  at           0 m beyond pendulum1 pivot, 0.35 m left of pendulum1 pivot, 0.30 m above pendulum1 pivot
  attached to  pendulum1
  friction     0.70, spinning 0, rolling 0
  bounce       dead

domino3
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  stands    on floor, 0.388597721 m beyond pendulum1
  colour    white

door1
  is a           box 0.04 by 0.32 by 0.42 m, 0.45 kg
  raised         0.025 m
  0.24 m beyond domino3
  turns on       door1 hinge,