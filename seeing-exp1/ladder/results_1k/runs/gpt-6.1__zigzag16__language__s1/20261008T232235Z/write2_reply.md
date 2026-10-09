```parts
part catch cup
  needs  base thickness, else 2 cm

  base
    is a  box 34 by 34 cm by base thickness
    on    floor

  near wall
    is a  box 2 by 34 by 20 cm
    on    base, at base's near end

  far wall
    is a  box 2 by 34 by 20 cm
    on    base, at base's far end

  left wall
    is a  box 30 by 2 by 20 cm
    on    base, at base's left side

  right wall
    is a  box 30 by 2 by 20 cm
    on    base, at base's right side
```

```world
world  passive gravity cascade

-- Untested candidate: the expect block specifies checks, not verified results.
-- Uses MuJoCo's default gravity of 9.81 m/s².
-- Numeric restitution 0.04 is unavailable; dead contacts are used.
-- Exact slide damping 0.20 N·s/m is unavailable; carts use fixed guides.
-- Every hinge has damping 0.04 N·m·s/rad.
-- Every moving body starts with zero velocity.
-- Separate hinged gravity boosters provide stored energy without adding
-- their mass to the named lever, pendulum or seesaw.
-- Ring centreline diameters allow for sixteen segments and 8 mm tubing.

floor
  size      12 m
  friction  0.72, spinning 0.001, rolling 0.0001

lever pivot
  is a  point
  at    0 m along, 0 m to the left, 65 cm up

lever near
  is a  point
  at    -0.052094453 m along, 0 m to the left, 0.945442326 m up

lever far
  is a  point
  at    0.052094453 m along, 0 m to the left, 0.354557674 m up

lever booster near
  is a  point
  at    -0.074978166 m along, 0 m to the left, 0.931253044 m up

lever booster far
  is a  point
  at    0.025737778 m along, 0 m to the left, 0.360064548 m up

ring1
  is a      ring 17.129131 cm across, 8 mm thick
  friction  0.72
  bounce    dead
  colour    orange
  at        -0.032398298 m along, 0 m to the left, 1.248915289 m up

lever1
  is a           plank from lever near to lever far, 10 cm wide, 4 cm thick
  weighs         0.50 kg
  friction       0.72
  bounce         dead
  colour         wood
  turns on       lever1 hinge, about y, at lever pivot
  swings         from -45 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

lever booster
  is a           cube 1 cm, 50 kg
  touches nothing
  at             0.0001 m along, 0 m to the left, 70 cm up
  turns on       lever booster hinge, about y, at lever pivot
  swings         from -45 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

lever booster coupling
  is a         plank from lever booster near to lever booster far, 8 cm wide, 1 cm thick
  weighs       2 g
  friction     0.72
  bounce       dead
  attached to  lever booster

ball1
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange
  centred over ring1, 30 cm above ring1

first slide bed
  is a      box 97 by 36 by 37 cm
  friction  0.72
  bounce    dead
  stands    on floor, 66.5 cm along, 0 m to the left

cart1
  is a      box 22 by 18 by 10 cm, 0.50 kg
  moves     freely
  friction  0.72
  bounce    dead
  colour    grey
  rests     on first slide bed, 31 cm along, 0 m to the left

first slide left rail
  is a      box 69 by 3 by 12 cm
  friction  0.72
  bounce    dead
  on        first slide bed, 52.5 cm along, 10.7 cm to the left

first slide right rail
  is a      box 69 by 3 by 12 cm
  friction  0.72
  bounce    dead
  on        first slide bed, 52.5 cm along, 10.7 cm to the right

first slide left roof
  is a      box 69 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        52.5 cm along, 7.5 cm to the left, 48.2 cm up

first slide right roof
  is a      box 69 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        52.5 cm along, 7.5 cm to the right, 48.2 cm up

first slide left bumper
  is a      box 4 by 3 by 10 cm
  friction  0.72
  bounce    dead
  on        first slide bed, 87 cm along, 6.5 cm to the left

first slide right bumper
  is a      box 4 by 3 by 10 cm
  friction  0.72
  bounce    dead
  on        first slide bed, 87 cm along, 6.5 cm to the right

domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    dead
  colour    wood
  stands    on first slide bed, 88 cm along, 0 m to the left

ramp high
  is a  point
  at    1.036058590 m along, 0 m to the left, 0.473226148 m up

ramp low
  is a  point
  at    1.975751211 m along, 0 m to the left, 0.131206005 m up

ramp1
  is a      plank from ramp high to ramp low, 30 cm wide, 4 cm thick
  friction  0.72
  bounce    dead
  colour    wood

ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange
  at        1.060000000 m along, 0 m to the left, 0.539004771 m up

ramp retaining lip
  is a      box 1 by 30 by 4 cm
  friction  0.72
  bounce    dead
  at        1.1025 m along, 0 m to the left, 0.486004771 m up

door1
  is a           box 4 by 32 by 42 cm, 0.45 kg
  friction       0.72
  bounce         dead
  colour         wood
  at             2.102592 m along, 0 m to the left, 24 cm up
  turns on       door1 hinge, about y, at its bottom
  swings         from 0 deg to 70 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

pendulum pivot
  is a  point
  at    2.802592 m along, 0 m to the left, 56 cm up

pendulum end
  is a  point
  at    2.494761262 m along, 0 m to the left, 0.165994623 m up

pendulum front coupling top
  is a  point
  at    2.820716247 m along, 0 m to the left, 0.545839786 m up

pendulum front coupling foot
  is a  point
  at    2.605234730 m along, 0 m to the left, 0.270036022 m up

pendulum back coupling top
  is a  point
  at    2.784467753 m along, 0 m to the left, 0.574160214 m up

pendulum back coupling foot
  is a  point
  at    2.568986236 m along, 0 m to the left, 0.298356449 m up

pendulum1
  is a           plank from pendulum pivot to pendulum end, 4 cm wide, 4 cm thick
  weighs         0.35 kg
  friction       0.72
  bounce         dead
  colour         grey
  turns on       pendulum1 hinge, about y, at pendulum pivot
  swings         from -38 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

pendulum booster
  is a           cube 1 mm, 30000 kg
  touches nothing
  at             2.802602 m along, 0 m to the left, 0.564 m up
  turns on       pendulum booster hinge, about y, at pendulum pivot
  swings         from -38 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

pendulum front coupling
  is a         plank from pendulum front coupling top to pendulum front coupling foot, 3 cm wide, 6 mm thick
  weighs       2 g
  friction     0.72
  bounce       dead
  attached to  pendulum booster

pendulum back coupling
  is a         plank from pendulum back coupling top to pendulum back coupling foot, 3 cm wide, 6 mm thick
  weighs       2 g
  friction     0.72
  bounce       dead
  attached to  pendulum booster

block1
  is a      cube 12 cm, 0.35 kg
  moves     freely
  friction  0.72
  bounce    dead
  colour    wood
  rests     on floor, 2.822592 m along, 0 m to the left

block left guide
  is a      box 48 by 3 by 14 cm
  friction  0.72
  bounce    dead
  on        floor, 2.987592 m along, 7.7 cm to the left

block right guide
  is a      box 48 by 3 by 14 cm
  friction  0.72
  bounce    dead
  on        floor, 2.987592 m along, 7.7 cm to the right

block left roof
  is a      box 48 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        2.987592 m along, 5 cm to the left, 13.2 cm up

block right roof
  is a      box 48 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        2.987592 m along, 5 cm to the right, 13.2 cm up

-- Cart2's box and its attached one-gram striker total 0.50 kg.

cart2
  is a      box 22 by 18 by 10 cm, 0.499 kg
  moves     freely
  friction  0.72
  bounce    dead
  colour    grey
  rests     on floor, 52 cm beyond block1, 0 m to the left

cart2 striker
  is a         box 2 by 10 by 126.9699 cm, 1 g
  friction     0.72
  bounce       dead
  on           cart2, at cart2's far end, 0 m to the left
  attached to  cart2

second slide left rail
  is a      box 72 by 3 by 14 cm
  friction  0.72
  bounce    dead
  on        floor, 3.592592 m along, 10.7 cm to the left

second slide right rail
  is a      box 72 by 3 by 14 cm
  friction  0.72
  bounce    dead
  on        floor, 3.592592 m along, 10.7 cm to the right

second slide left roof
  is a      box 72 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        3.592592 m along, 7.8 cm to the left, 11.2 cm up

second slide right roof
  is a      box 72 by 2 by 2 cm
  friction  0.72
  bounce    dead
  at        3.592592 m along, 7.8 cm to the right, 11.2 cm up

second slide left bumper
  is a      box 4 by 3 by 16 cm
  friction  0.72
  bounce    dead
  on        floor, 3.912592 m along, 6.5 cm to the left

second slide right bumper
  is a      box 4 by 3 by 16 cm
  friction  0.72
  bounce    dead
  on        floor, 3.912592 m along, 6.5 cm to the right

seesaw pivot
  is a  point
  at    85.5 cm beyond cart2, 0 m to the left, 1.386698730 m up

seesaw1
  is a           box 65 by 10 by 4 cm, 0.55 kg
  friction       0.72
  bounce         dead
  colour         wood
  at             seesaw pivot
  turns on       seesaw1 hinge, about y, at seesaw pivot
  swings         from -42 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

seesaw booster
  is a           cube 2 mm, 200 kg
  touches nothing
  at             4.197592 m along, 0 m to the left, 1.406698730 m up
  turns on       seesaw booster hinge, about y, at seesaw pivot
  swings         from -42 deg to 0 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

seesaw lower coupling
  is a         box 50 by 8 by 0.6 cm, 2 g
  friction     0.72
  bounce       dead
  at           4.197592 m along, 0 m to the left, 1.363698730 m up
  attached to  seesaw booster

seesaw upper coupling
  is a         box 50 by 8 by 0.6 cm, 2 g
  friction     0.72
  bounce       dead
  at           4.197592 m along, 0 m to the left, 1.409698730 m up
  attached to  seesaw booster

ring2
  is a      ring 17.129131 cm across, 8 mm thick
  friction  0.72
  bounce    dead
  colour    orange
  at        4.542592 m along, 6.5 cm to the left, 1.13 m up

-- These three posts leave the beam clear while guiding the ball vertically.

ball3 diagonal guide
  is a      box 1 by 1 by 130 cm
  friction  0.72
  bounce    dead
  at        4.501883 m along, 0.105709 m to the left, 1.65 m up

ball3 forward guide
  is a      box 1 by 1 by 130 cm
  friction  0.72
  bounce    dead
  at        4.598092 m along, 6.5 cm to the left, 1.65 m up

ball3 rear guide
  is a      box 1 by 1 by 130 cm
  friction  0.72
  bounce    dead
  at        4.542592 m along, 0.0095 m to the left, 1.65 m up

ball3
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange
  centred over ring2, 32 cm above ring2

final platform
  is a      box 60 by 36 by 60 cm
  friction  0.72
  bounce    dead
  stands    on floor, 4.60 m along, 6.5 cm to the left

domino2
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    dead
  colour    wood
  stands    on final platform, 2.5 cm behind ball3, 6.5 cm to the left

flap1
  is a           box 4 by 18 by 38 cm, 0.28 kg
  friction       0.72
  bounce         dead
  colour         wood
  at             24 cm beyond domino2, 6.5 cm to the left, 82 cm up
  turns on       flap1 hinge, about y, at its bottom
  swings         from 0 deg to 60 deg
  damping        0.04 N·m·s/rad
  starts turned  0 deg

cup1
  is a            catch cup
  base thickness  2 cm
  friction        0.72
  bounce          dead
  colour          grey
  on              floor, 5.236682 m along, 6.5 cm to the left

-- The shelf's upper face is 55 cm above the cup's wall tops.

shelf1
  is a      box 30 by 25 by 4 cm
  friction  0.72
  bounce    dead
  colour    wood
  at        4.946682 m along, 6.5 cm to the left, 75 cm up

ball4
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72, spinning 0.001, rolling 0.0001
  bounce    dead
  colour    orange
  rests     on shelf1, 14 cm beyond shelf1, 6.5 cm to the left

cup catch backboard
  is a      box 2 by 34 by 80 cm
  friction  0.72
  bounce    dead
  colour    grey
  at        5.396682 m along, 6.5 cm to the left, 62 cm up

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever1 reaches its lower stop
  lever1 touches cart1
  cart1 touches domino1
  domino1 touches ball2
  ball2 touches ramp1
  ball2 touches door1
  door1 touches pendulum1
  pendulum1 reaches its lower stop
  pendulum1 touches block1
  block1 touches cart2
  cart2 touches seesaw1
  seesaw1 reaches its lower stop
  seesaw1 touches ball3
  ball3 drops through ring2
  ball3 touches domino2
  domino2 touches flap1
  flap1 touches ball4
  ball4 comes to rest in cup1
```