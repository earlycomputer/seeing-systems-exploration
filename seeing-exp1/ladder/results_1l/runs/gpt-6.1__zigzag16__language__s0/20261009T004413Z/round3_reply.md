The world still **does not follow the brief**.

Cart1 escapes its gate at about **0.01 s**, before ball1 reaches lever1. It hits domino1 at **0.09 s**, and domino1 hits ball2 at **0.13 s**. Ball1 passes through ring1 and strikes lever1 later, at **0.34 s**; the lever subsequently reaches its −45° stop, but it did not initiate the cart’s motion.

Ball2 rolls down ramp1 and hits door1 at **0.83 s**. Door1 reaches only about **−62.9°**, rather than −70°. It touches pendulum1, but the pendulum swings only **2.7°**, never reaching block1. Everything downstream remains inactive: ball3 is not launched, and ball4 stays on shelf1.

The revision below restores a deeper cart latch, adds a separately latched spring-assisted door, and provides the pendulum with a low striking attachment positioned to meet block1 at 38°. These changes are proposed corrections, not a verified successful run.

```parts
part catch cup
  base
    is a  box 34 by 34 by 2 cm
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
world  restrained cascade with assisted door

-- Gravity is the language default: 9.81 m/s².
-- Every moving body starts with zero linear and angular velocity.
-- Initial latch contacts are restraints, not expected new touch events.

floor
  size      12 m
  friction  0.72

lever pivot
  is a  point
  at    0 m along, 0 m to the left, 0.55 m up

-- Lever assembly mass:
-- 411 g beam, 80 g counterweight, 1 g stem,
-- 3 g gate lifter, 3 g striker, 2 g striker link.

lever1
  is a           box 60 by 10 by 4 cm, 0.411 kg
  at             lever pivot
  friction       0.72
  bounce         0.04
  turns on       lever1 hinge, about y, at lever pivot
  swings         from −45° to 0°
  spring         0.03 N·m/rad toward −45°
  damping        0.04 N·m·s/rad
  starts turned  0°

lever counterweight
  is a         cube 4 cm, 80 g
  at           0.015 m along, 0.03 m to the left, 0.85 m up
  attached to  lever1
  friction     0.72
  bounce       0.04

lever counterweight stem
  is a         rod 4 mm thick, from lever pivot to lever counterweight's bottom
  weighs       1 g
  attached to  lever1
  friction     0.72
  bounce       0.04

lever gate lifter
  is a         box 1.5 by 16 by 16.5 cm, 3 g
  at           0.10 m along, 0.045 m to the left, 0.6525 m up
  attached to  lever1
  friction     0.72
  bounce       0.04

lever cart striker
  is a         sphere 1 cm radius, 3 g
  at           0.29 m along, 0.13 m to the right, 0.57 m up
  attached to  lever1
  friction     0.72
  bounce       0.04

lever striker link
  is a         rod 1 cm thick, from lever1's far end to lever cart striker
  weighs       2 g
  attached to  lever1
  friction     0.72
  bounce       0.04

ring1
  is a      ring 16 cm across, 8 mm thick
  at        −0.285 m along, 0.04 m to the left, 0.87 m up
  friction  0.72
  bounce    0.04

ball1
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −0.285 m along, 0.04 m to the left, 1.17 m up

-- The latch overlaps the cart's height by 5 mm, rather than 1 mm.
-- The gate lifter initially has 1 cm of vertical clearance.
-- The lifter and main beam remain outside the cart's lateral lane.

cart1 release gate
  is a         box 27 by 25 by 1 cm, 40 g
  at           0.165 m along, 0.02 m to the right, 0.75 m up
  friction     0.72
  bounce       0.04
  slides on    cart1 gate slide, along z
  travels      from 0 cm to 5 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart1
  is a         box 22 by 18 by 10 cm, 0.50 kg
  at           0.41 m along, 0.15 m to the right, 0.70 m up
  friction     0.72
  bounce       0.04
  slides on    cart1 slide, along x
  travels      from −60 cm to 0 cm
  spring       180 N/m toward −42 cm
  damping      0.20 N·s/m
  starts slid  0 cm

domino1 platform
  is a      box 40 by 7 by 4 cm
  at        −0.30 m along, 0.15 m to the right, 0.41 m up
  friction  0.72
  bounce    0.04

domino1 toe
  is a      box 1 by 6 by 3 cm
  at        −0.205 m along, 0.15 m to the right, 0.445 m up
  friction  0.72
  bounce    0.04

domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −0.16 m along, 0.15 m to the right, 0.55 m up

-- Endpoint centres are 1.00 m apart at 20 degrees.
-- Including deck thickness, the low top surface is at 0.15 m.

ramp high
  is a  point
  at    −0.406059 m along, 0.15 m to the right, 0.473226 m up

ramp low
  is a  point
  at    −1.345752 m along, 0.15 m to the right, 0.131206 m up

ramp1
  is a       ramp
  high end   ramp high
  low end    ramp low
  width      30 cm
  thickness  4 cm
  friction   0.72
  bounce     0.04

ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −0.43 m along, 0.15 m to the right, 0.539004 m up

ball2 retaining lip
  is a      box 1 by 12 by 2 cm
  at        −0.48 m along, 0.15 m to the right, 0.492 m up
  friction  0.72
  bounce    0.04

-- The cover ends before the door-release cam.

ramp cover high
  is a  point
  at    −0.474463 m along, 0.15 m to the right, 0.661165 m up

ramp cover low
  is a  point
  at    −1.296930 m along, 0.15 m to the right, 0.289447 m up

ramp cover
  is a      plank from ramp cover high to ramp cover low, 30 cm wide, 2 cm thick
  friction  0.72
  bounce    0.04

-- This latch restrains the door's preloaded hinge spring.
-- Its tongue overlaps the panel's upper edge by 5 mm.
-- Ball2 lifts it by contacting the underside of the sloping cam.

door1 release gate
  is a         box 1 by 5 by 1 cm, 20 g
  at           −1.490752 m along, 0.285 m to the right, 0.340 m up
  friction     0.72
  bounce       0.04
  slides on    door1 gate slide, along z
  travels      from 0 cm to 8 cm
  damping      0.20 N·s/m
  starts slid  0 cm

door latch rear stem
  is a         box 0.5 by 2 by 2 cm, 2 g
  at           −1.490752 m along, 0.285 m to the right, 0.350 m up
  attached to  door1 release gate
  friction     0.72
  bounce       0.04

door latch bridge
  is a         box 11.2 by 18 by 1 cm, 5 g
  at           −1.439752 m along, 0.22 m to the right, 0.355 m up
  attached to  door1 release gate
  friction     0.72
  bounce       0.04

door latch front stem
  is a         box 1 by 2 by 10.5 cm, 2 g
  at           −1.388752 m along, 0.15 m to the right, 0.3075 m up
  attached to  door1 release gate
  friction     0.72
  bounce       0.04

door cam front reference
  is a  point
  at    −1.388752 m along, 0.15 m to the right, 0.26 m up

door cam rear reference
  is a  point
  at    −1.438752 m along, 0.15 m to the right, 0.16 m up

door release cam
  is a         plank from door cam front reference to door cam rear reference, 12 cm wide, 1 cm thick
  weighs       20 g
  attached to  door1 release gate
  friction     0.72
  bounce       0.04

-- The incoming panel face is 10 cm beyond the ramp endpoint.
-- The gate, not an initial velocity, restrains the stored hinge energy.

door1
  is a           box 4 by 42 by 32 cm, 0.45 kg
  at             −1.465752 m along, 0.09 m to the right, 0.18 m up
  friction       0.72
  bounce         0.04
  turns on       door1 hinge, about z, at its left side
  swings         from −70° to 0°
  spring         8 N·m/rad toward −70°
  damping        0.04 N·m·s/rad
  starts turned  0°

-- The bob is positioned on the sweeping panel's striking face,
-- rather than beyond its nearly radial free-end trajectory.
-- It starts 5 mm clear of the floor.

pendulum pivot
  is a  point
  at    −1.874482 m along, 0.012058 m to the right, 0.575 m up

-- Pendulum assembly mass:
-- 275 g bob, 70 g shaft, 1 g reach rod,
-- 2 g lateral rod, 2 g block striker.
-- Pivot-to-bob-centre length is 0.50 m.
-- The small spring bias keeps the off-centre striker at the initial stop.

pendulum1
  is a           sphere 7 cm radius, 0.275 kg
  at             −1.874482 m along, 0.012058 m to the right, 0.075 m up
  friction       0.72
  bounce         0.04
  turns on       pendulum1 hinge, about y, at pendulum pivot
  swings         from 0° to 45°
  spring         0.10 N·m/rad toward −5°
  damping        0.04 N·m·s/rad
  starts turned  0°

pendulum rod
  is a         rod 4 cm thick, from pendulum pivot to pendulum1's top
  weighs       0.070 kg
  attached to  pendulum1
  friction     0.72
  bounce       0.04

pendulum striker root reference
  is a  point
  at    −1.714482 m along, 0.012058 m to the right, 0.055 m up

pendulum block striker
  is a         sphere 1 cm radius, 2 g
  at           −1.714482 m along, 0.25 m to the right, 0.055 m up
  attached to  pendulum1
  friction     0.72
  bounce       0.04

pendulum reach rod
  is a         rod 5 mm thick, from pendulum1 to pendulum striker root reference
  weighs       1 g
  attached to  pendulum1
  friction     0.72
  bounce       0.04

pendulum lateral rod
  is a         rod 5 mm thick, from pendulum striker root reference to pendulum block striker
  weighs       2 g
  attached to  pendulum1
  friction     0.72
  bounce       0.04

-- At 38 degrees, the low striker meets the block's incoming face.
-- The bob itself is laterally clear of the block lane.

block1
  is a      cube 12 cm, 0.35 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −2.138544 m along, 0.25 m to the right, 0.06 m up

-- Low rails do not obstruct the pendulum's lateral striking rod.

block left guide
  is a      box 68 by 2 by 1 cm
  at        −2.198544 m along, 0.175 m to the right, 0.005 m up
  friction  0.72
  bounce    0.04

block right guide
  is a      box 68 by 2 by 1 cm
  at        −2.198544 m along, 0.325 m to the right, 0.005 m up
  friction  0.72
  bounce    0.04

-- Cart2 and its upright together weigh 0.50 kg.
-- Block1 travels 35 cm before contacting the cart.

cart2
  is a         box 22 by 18 by 10 cm, 0.48 kg
  at           −2.658544 m along, 0.25 m to the right, 0.05 m up
  friction     0.72
  bounce       0.04
  slides on    cart2 slide, along x
  travels      from −65 cm to 0 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart2 upright
  is a         box 2 by 6 by 79 cm, 0.02 kg
  at           −2.758544 m along, 0.25 m to the right, 0.495 m up
  attached to  cart2
  friction     0.72
  bounce       0.04

seesaw pivot
  is a  point
  at    −3.513544 m along, 0.25 m to the right, 0.90 m up

-- Main beam and tines total 0.55 kg.
-- Their outer envelope is 65 by 10 by 4 cm, hinged at its centre.
-- Cart2's upright reaches the struck end after 42 cm of travel.

seesaw1
  is a           box 51 by 10 by 4 cm, 0.4509646 kg
  at             −3.443544 m along, 0.25 m to the right, 0.90 m up
  friction       0.72
  bounce         0.04
  turns on       seesaw1 hinge, about y, at seesaw pivot
  swings         from 0° to 42°
  spring         0.75 N·m/rad toward 42°
  damping        0.04 N·m·s/rad
  starts turned  0°

seesaw upper tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.768544 m along, 0.22 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

seesaw lower tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.768544 m along, 0.28 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

ball3 forward guide
  is a      box 1 by 1.8 by 85 cm
  at        −3.773544 m along, 0.25 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3 rear guide
  is a      box 1 by 1.8 by 85 cm
  at        −3.883544 m along, 0.25 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −3.828544 m along, 0.25 m to the right, 0.97 m up

ring2
  is a      ring 16 cm across, 8 mm thick
  at        −3.828544 m along, 0.25 m to the right, 0.65 m up
  friction  0.72
  bounce    0.04

domino2 platform
  is a      box 45 by 7 by 4 cm
  at        −3.793544 m along, 0.25 m to the right, 0.10 m up
  friction  0.72
  bounce    0.04

domino2 toe
  is a      box 1 by 6 by 3 cm
  at        −3.838544 m along, 0.25 m to the right, 0.135 m up
  friction  0.72
  bounce    0.04

domino2
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −3.793544 m along, 0.25 m to the right, 0.24 m up

-- The falling line is 3.5 cm toward the domino's tipping edge.
-- Ball3's centre falls another 24 cm below ring2 before contact.
-- The initial clear domino-to-flap gap is 18 cm.

flap1
  is a           box 4 by 18 by 38 cm, 0.28 kg
  at             −4.033544 m along, 0.25 m to the right, 0.44 m up
  friction       0.72
  bounce         0.04
  turns on       flap1 hinge, about y, at its top
  swings         from 0° to 60°
  damping        0.04 N·m·s/rad
  starts turned  0°

cup1
  is a      catch cup
  at        −4.405444 m along, 0.25 m to the right, 0.11 m up
  friction  0.72
  bounce    0.04

-- Shelf top is 55 cm above the cup's inner floor.

shelf1
  is a      box 30 by 25 by 4 cm
  at        −4.210444 m along, 0.25 m to the right, 0.55 m up
  friction  0.72
  bounce    0.04

ball4
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  on        shelf1, −4.170444 m along, 0.25 m to the right

cup backstop
  is a      box 2 by 34 by 80 cm
  at        −4.565444 m along, 0.25 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

cup left catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.405444 m along, 0.09 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

cup right catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.405444 m along, 0.41 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever gate lifter touches cart1 release gate
  lever cart striker touches cart1
  lever1 reaches its lower stop
  cart1 touches domino1
  domino1 touches ball2
  ball2 touches ramp1
  ball2 touches door release cam
  ball2 touches door1
  door1 reaches its lower stop
  door1 touches pendulum1
  pendulum block striker touches block1
  block1 touches cart2
  cart2 upright touches seesaw1
  seesaw upper tine touches ball3
  ball3 drops through ring2
  ball3 touches domino2
  domino2 touches flap1
  flap1 reaches its upper stop
  flap1 touches ball4
  ball4 comes to rest in cup1
```

```json
{
  "what_happens": "Cart1 escapes its latch before ball1 reaches lever1, striking domino1 at 0.09 s and releasing ball2 at 0.13 s. Ball1 later passes through ring1, strikes lever1, and the lever reaches -45 degrees. Ball2 rolls down ramp1 and strikes door1, but the door reaches only about -62.9 degrees and pendulum1 swings only 2.7 degrees. Block1 and the remaining chain never activate, and ball4 stays on shelf1.",
  "works": false,
  "problem": "Cart1 moves prematurely, and the door-to-pendulum transfer is too weak to activate block1 and the downstream chain."
}
```