I shortened `cart2 roof` by 2 cm at its seesaw-facing end, keeping its other end unchanged. This removes the reported initial overlap with `seesaw input rod`.

```parts
part catch cup
  base
    is a  box 34 by 34 by 2 cm
    on    floor

  near wall
    is a  box 2 by 34 by 20 cm
    on    base, 16 cm behind base

  far wall
    is a  box 2 by 34 by 20 cm
    on    base, 16 cm beyond base

  left wall
    is a  box 30 by 2 by 20 cm
    on    base, 16 cm left of base

  right wall
    is a  box 30 by 2 by 20 cm
    on    base, 16 cm right of base


-- Sixteen 8 mm tubes form a horizontal polygonal ring.
-- Its centre-line apothem is 84 mm, leaving 80 mm clear radius.
part clear hoop
  v00
    is a  point
    at    8.5645657 cm along, 0 m to the left, 0 m up
  v01
    is a  point
    at    7.9126270 cm along, 3.2775174 cm to the left, 0 m up
  v02
    is a  point
    at    6.0560625 cm along, 6.0560625 cm to the left, 0 m up
  v03
    is a  point
    at    3.2775174 cm along, 7.9126270 cm to the left, 0 m up
  v04
    is a  point
    at    0 m along, 8.5645657 cm to the left, 0 m up
  v05
    is a  point
    at    3.2775174 cm behind floor, 7.9126270 cm to the left, 0 m up
  v06
    is a  point
    at    6.0560625 cm behind floor, 6.0560625 cm to the left, 0 m up
  v07
    is a  point
    at    7.9126270 cm behind floor, 3.2775174 cm to the left, 0 m up
  v08
    is a  point
    at    8.5645657 cm behind floor, 0 m to the left, 0 m up
  v09
    is a  point
    at    7.9126270 cm behind floor, 3.2775174 cm to the right, 0 m up
  v10
    is a  point
    at    6.0560625 cm behind floor, 6.0560625 cm to the right, 0 m up
  v11
    is a  point
    at    3.2775174 cm behind floor, 7.9126270 cm to the right, 0 m up
  v12
    is a  point
    at    0 m along, 8.5645657 cm to the right, 0 m up
  v13
    is a  point
    at    3.2775174 cm along, 7.9126270 cm to the right, 0 m up
  v14
    is a  point
    at    6.0560625 cm along, 6.0560625 cm to the right, 0 m up
  v15
    is a  point
    at    7.9126270 cm along, 3.2775174 cm to the right, 0 m up

  rim 00
    is a  rod 8 mm thick, from v00 to v01
  rim 01
    is a  rod 8 mm thick, from v01 to v02
  rim 02
    is a  rod 8 mm thick, from v02 to v03
  rim 03
    is a  rod 8 mm thick, from v03 to v04
  rim 04
    is a  rod 8 mm thick, from v04 to v05
  rim 05
    is a  rod 8 mm thick, from v05 to v06
  rim 06
    is a  rod 8 mm thick, from v06 to v07
  rim 07
    is a  rod 8 mm thick, from v07 to v08
  rim 08
    is a  rod 8 mm thick, from v08 to v09
  rim 09
    is a  rod 8 mm thick, from v09 to v10
  rim 10
    is a  rod 8 mm thick, from v10 to v11
  rim 11
    is a  rod 8 mm thick, from v11 to v12
  rim 12
    is a  rod 8 mm thick, from v12 to v13
  rim 13
    is a  rod 8 mm thick, from v13 to v14
  rim 14
    is a  rod 8 mm thick, from v14 to v15
  rim 15
    is a  rod 8 mm thick, from v15 to v00


part vertical launch guide
  near left bottom
    is a  point
    at    2.5 cm behind floor, 5.35 cm to the left, 1.21 m up
  near left top
    is a  point
    at    2.5 cm behind floor, 5.35 cm to the left, 1.90 m up
  near right bottom
    is a  point
    at    2.5 cm behind floor, 5.35 cm to the right, 1.21 m up
  near right top
    is a  point
    at    2.5 cm behind floor, 5.35 cm to the right, 1.90 m up
  far left bottom
    is a  point
    at    2.5 cm beyond floor, 5.35 cm to the left, 1.21 m up
  far left top
    is a  point
    at    2.5 cm beyond floor, 5.35 cm to the left, 1.90 m up
  far right bottom
    is a  point
    at    2.5 cm beyond floor, 5.35 cm to the right, 1.21 m up
  far right top
    is a  point
    at    2.5 cm beyond floor, 5.35 cm to the right, 1.90 m up

  near left rail
    is a  rod 8 mm thick, from near left bottom to near left top
  near right rail
    is a  rod 8 mm thick, from near right bottom to near right top
  far left rail
    is a  rod 8 mm thick, from far left bottom to far left top
  far right rail
    is a  rod 8 mm thick, from far right bottom to far right top
```

```world
world  restrained cascade revision

-- Unverified revision.
-- Assumes compiler gravity 9.81 m/s2.
-- Every body starts with zero velocity.
-- Dead contacts do not encode exact restitution 0.04.
-- Guided free carts approximate slides; slide damping is not expressible.
-- Auxiliary gravity assists add mass to the hinged assemblies.

floor
  size      10 m
  friction  0.72, spinning 0.005, rolling 0.002

lever pivot
  is a  point
  at    30 cm along, 0 m to the left, 28 cm up

ring1
  is a      clear hoop
  at        27 cm behind lever pivot, 0 m to the left, 60 cm up
  friction  0.72
  bounce    dead
  colour    orange

lever1
  is a      box 60 by 10 by 4 cm, 500 g
  at        30 cm along, 0 m to the left, 28 cm up
  turns on  lever1 hinge, about y, at lever pivot
  swings    from -45° to 0°
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    dead
  colour    wood

lever gravity assist
  is a         cube 1 cm, 600 kg
  at           0.02 mm beyond lever pivot, 22 cm to the right, 2 cm above lever pivot
  attached to  lever1
  friction     0.72
  bounce       dead
  colour       dark grey

lever striking head
  is a         sphere 4 cm radius, 5 g
  at           30 cm beyond lever pivot, 25 cm to the left, level with lever pivot
  attached to  lever1
  friction     0.72
  bounce       dead
  colour       grey

ball1
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  at        30 cm above ring1, centred over ring1
  friction  0.72
  bounce    dead
  colour    orange

cart1 left runner
  is a      box 90 by 2.6 by 2.5 cm
  at        15 cm along, 32.4 cm to the left, 41.25 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 right runner
  is a      box 90 by 2.6 by 2.5 cm
  at        15 cm along, 17.6 cm to the left, 41.25 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 left guide
  is a      box 90 by 2 by 16 cm
  at        15 cm along, 35.1 cm to the left, 50 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 right guide
  is a      box 90 by 2 by 16 cm
  at        15 cm along, 14.9 cm to the left, 50 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 left roof
  is a      box 63 by 2.6 by 2.5 cm
  at        17.5 cm along, 32.5 cm to the left, 53.95 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 right roof
  is a      box 63 by 2.6 by 2.5 cm
  at        17.5 cm along, 17.5 cm to the left, 53.95 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1
  is a      box 22 by 18 by 10 cm, 500 g
  moves     freely
  at        38 cm along, 25 cm to the left, 47.5 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart1 striking mast
  is a         box 3 by 4 by 12 cm, 5 g
  at           9.5 cm behind cart1, 25 cm to the left, 58.5 cm up
  attached to  cart1
  friction     0.72
  bounce       dead
  colour       grey

domino1 pedestal
  is a      box 15 by 18 by 42.5 cm
  on        floor, 21.5 cm behind floor, 25 cm to the left
  friction  0.72
  bounce    dead
  colour    wood

domino1
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  on        domino1 pedestal, 19 cm behind floor, 25 cm to the left
  friction  0.72
  bounce    dead
  colour    wood

ramp1
  is a       ramp
  high end   29 cm behind floor, 25 cm to the left, 0.49202014 m up
  low end    1.22969262 m behind floor, 25 cm to the left, 15 cm up
  width      30 cm
  thickness  4 cm
  friction   0.72
  bounce     dead
  colour     wood

ball2 retaining lip
  is a      box 1.6 by 30 by 2 cm
  at        40.2 cm behind floor, 25 cm to the left, 48.3 cm up
  friction  0.72
  bounce    dead
  colour    wood

ball2
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  at        18 cm behind domino1, 25 cm to the left, 53.74 cm up
  friction  0.72
  bounce    dead
  colour    orange

door1
  is a      box 4 by 32 by 42 cm, 450 g
  at        1.34969262 m behind floor, 37 cm to the left, 31 cm up
  turns on  door1 hinge, about z, at its left side
  swings    from -70° to 0°
  spring    3.40 N·m/rad toward -100°
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    dead
  colour    wood

door latch tab
  is a         box 4 by 8 by 1 cm, 1 g
  at           1.34969262 m behind floor, 23 cm to the left, 60 cm up
  attached to  door1
  friction     0.72
  bounce       dead
  colour       grey

door latch pedestal
  is a      box 2 by 6 by 2 cm
  at        1.38969262 m behind floor, 23 cm to the left, 58 cm up
  friction  0.72
  bounce    dead
  colour    grey

door latch
  is a      box 4 by 5 by 2 cm, 3 kg
  moves     freely
  at        1.38969262 m behind floor, 23 cm to the left, 60 cm up
  friction  0.72
  bounce    dead
  colour    dark grey

pendulum pivot
  is a  point
  at    1.9878 m behind floor, 42 cm to the left, 60 cm up

pendulum1
  is a      sphere 10 cm radius, 330 g
  at        30.78307 cm beyond pendulum pivot, 42 cm to the left, 39.40054 cm below pendulum pivot
  turns on  pendulum1 hinge, about y, at pendulum pivot
  swings    from 0° to 38°
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    dead
  colour    grey

pendulum rod
  is a         rod 12 mm thick, from pendulum pivot to pendulum1
  weighs       20 g
  attached to  pendulum1
  friction     0.72
  bounce       dead
  colour       grey

pendulum gravity assist
  is a         cube 4 mm, 2500 kg
  at           0.044 mm behind pendulum pivot, 22 cm to the right, 1 cm above pendulum pivot
  attached to  pendulum1
  friction     0.72
  bounce       dead
  colour       dark grey

block1 left roof
  is a      box 72 by 1.2 by 2.5 cm
  at        2.4438 m behind floor, 47.5 cm to the left, 13.45 cm up
  friction  0.72
  bounce    dead
  colour    grey

block1 right roof
  is a      box 72 by 1.2 by 2.5 cm
  at        2.4438 m behind floor, 36.5 cm to the left, 13.45 cm up
  friction  0.72
  bounce    dead
  colour    grey

block1
  is a      cube 12 cm, 350 g
  moves     freely
  on        floor, 2.1438 m behind floor, 42 cm to the left
  friction  0.72
  bounce    dead
  colour    wood

cart2 left guide
  is a      box 95 by 2 by 12 cm
  on        floor, 2.90 m behind floor, 52.1 cm to the left
  friction  0.72
  bounce    dead
  colour    grey

cart2 right guide
  is a      box 95 by 2 by 12 cm
  on        floor, 2.90 m behind floor, 31.9 cm to the left
  friction  0.72
  bounce    dead
  colour    grey

-- Bounds along x are now -3.18 m to -2.5538 m.
-- The shortened seesaw-facing end clears the input rod.
cart2 roof
  is a      box 62.62 by 20 by 2.5 cm
  at        2.8669 m behind floor, 42 cm to the left, 11.45 cm up
  friction  0.72
  bounce    dead
  colour    grey

cart2
  is a      box 22 by 18 by 10 cm, 500 g
  moves     freely
  on        floor, 2.6638 m behind floor, 42 cm to the left
  friction  0.72
  bounce    dead
  colour    grey

seesaw pivot
  is a  point
  at    3.3588 m behind floor, 42 cm to the left, 1.18 m up

seesaw1
  is a      box 65 by 10 by 4 cm, 550 g
  at        3.3588 m behind floor, 42 cm to the left, 1.18 m up
  turns on  seesaw1 hinge, about y, at seesaw pivot
  swings    from 0° to 42°
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    dead
  colour    wood

seesaw input point
  is a  point
  at    15 cm beyond seesaw pivot, 42 cm to the left, 5 cm up

seesaw input rod
  is a         rod 12 mm thick, from seesaw1's far end to seesaw input point
  weighs       10 g
  attached to  seesaw1
  friction     0.72
  bounce       dead
  colour       grey

seesaw input pad
  is a         box 3 by 10 by 5 cm, 5 g
  at           15 cm beyond seesaw pivot, 42 cm to the left, 5 cm up
  attached to  seesaw1
  friction     0.72
  bounce       dead
  colour       grey

seesaw gravity assist
  is a         cube 2 cm, 100 kg
  at           0.5 mm beyond seesaw pivot, 22 cm to the right, 4 cm above seesaw pivot
  attached to  seesaw1
  friction     0.72
  bounce       dead
  colour       dark grey

ball3
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  at        33.5 cm behind seesaw pivot, 42 cm to the left, 1.25 m up
  friction  0.72
  bounce    dead
  colour    orange

ball3 guide
  is a      vertical launch guide
  centred over ball3
  friction  0.72
  bounce    dead
  colour    grey

ring2
  is a      clear hoop
  at        32 cm below ball3, centred over ball3
  friction  0.72
  bounce    dead
  colour    orange

domino2 pedestal
  is a      box 16 by 12 by 40 cm
  on        floor, 3.6938 m behind floor, 39.5 cm to the left
  friction  0.72
  bounce    dead
  colour    wood

domino2
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  on        domino2 pedestal, 3.6938 m behind floor, 39.5 cm to the left
  friction  0.72
  bounce    dead
  colour    wood

flap1
  is a      box 18 by 4 by 38 cm, 280 g
  at        3.6938 m behind floor, 57.5 cm to the left, 66 cm up
  turns on  flap1 hinge, about x, at its top
  swings    from 0° to 60°
  spring    0.90 N·m/rad toward 90°
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    dead
  colour    wood

flap latch pedestal
  is a      box 8 by 5 by 2 cm
  at        3.6938 m behind floor, 62 cm to the left, 45 cm up
  friction  0.72
  bounce    dead
  colour    grey

flap latch
  is a      box 6 by 4 by 5 cm, 800 g
  moves     freely
  at        3.6938 m behind floor, 61.5 cm to the left, 48.5 cm up
  friction  0.72
  bounce    dead
  colour    dark grey

cup1
  is a      catch cup
  on        floor, 3.6938 m behind floor, 1.175 m to the left
  friction  0.72
  bounce    dead
  colour    grey

shelf1
  is a      box 30 by 25 by 4 cm
  at        3.6938 m behind floor, 1 m to the left, 59 cm up
  friction  0.72
  bounce    dead
  colour    wood

ball4
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  on        shelf1, 3.6938 m behind floor, 88 cm to the left
  friction  0.72
  bounce    dead
  colour    orange

cup catch screen
  is a      box 34 by 2 by 150 cm
  at        3.6938 m behind floor, 1.335 m to the left, 97 cm up
  friction  0.72
  bounce    dead
  colour    grey

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
  pendulum1 touches block1
  block1 touches cart2
  cart2 touches seesaw1
  seesaw1 touches ball3
  ball3 drops through ring2
  ball3 touches domino2
  domino2 touches flap1
  flap1 touches ball4
  ball4 comes to rest in cup1
```