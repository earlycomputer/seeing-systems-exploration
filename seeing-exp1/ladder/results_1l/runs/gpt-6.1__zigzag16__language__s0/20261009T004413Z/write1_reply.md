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
world  gravity cascade with guided vertical launch

-- Gravity is the language default: 9.81 m/s².
-- No body has an initial linear or angular velocity.
-- Collision surfaces use friction 0.72 and restitution 0.04.

floor
  size      12 m
  friction  0.72

lever pivot
  is a  point
  at    0 m along, 0 m to the left, 0.55 m up

lever1
  is a           box 60 by 10 by 4 cm, 0.50 kg
  at             lever pivot
  friction       0.72
  bounce         0.04
  turns on       lever1 hinge, about y, at lever pivot
  swings         from −45° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°

ring1
  is a      ring 17.12975 cm across, 8 mm thick
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

-- The cart's near face initially bears against the lever's far end.
-- Its spring cannot translate it through the horizontal lever.
-- The falling ball tips the lever and releases the stored slide energy.

cart1
  is a         box 22 by 18 by 10 cm, 0.50 kg
  at           0.41 m along, 0.09 m to the right, 0.55 m up
  friction     0.72
  bounce       0.04
  slides on    cart1 slide, along x
  travels      from −60 cm to 0 cm
  spring       180 N/m toward −42 cm
  damping      0.20 N·s/m
  starts slid  0 cm

domino1 platform
  is a      box 40 by 7 by 4 cm
  at        −0.30 m along, 0.09 m to the right, 0.41 m up
  friction  0.72
  bounce    0.04

domino1 toe
  is a      box 1 by 6 by 3 cm
  at        −0.205 m along, 0.09 m to the right, 0.445 m up
  friction  0.72
  bounce    0.04

domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −0.16 m along, 0.09 m to the right, 0.55 m up

-- Ramp endpoint separation is 1.00 m at 20 degrees.
-- Its nominal low endpoint is 0.15 m above the floor.

ramp high
  is a  point
  at    −0.453941 m along, 0.09 m to the right, 0.492020 m up

ramp low
  is a  point
  at    −1.393634 m along, 0.09 m to the right, 0.15 m up

ramp1
  is a       ramp
  high end   ramp high
  low end    ramp low
  width      30 cm
  thickness  4 cm
  friction   0.72
  bounce     0.04

-- The lip is clear of ball2 at the initial position.

ball2 retaining lip
  is a      box 1 by 12 by 3 cm
  at        −0.48 m along, 0.09 m to the right, 0.51 m up
  friction  0.72
  bounce    0.04

ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −0.43 m along, 0.09 m to the right, 0.557798 m up

-- The tapered cover captures an energetic ball without closing the entry lip.

ramp cover high
  is a  point
  at    −0.385537 m along, 0.09 m to the right, 0.679959 m up

ramp cover low
  is a  point
  at    −1.348487 m along, 0.09 m to the right, 0.274039 m up

ramp cover
  is a      plank from ramp cover high to ramp cover low, 30 cm wide, 2 cm thick
  friction  0.72
  bounce    0.04

-- The door's incoming face is 10 cm beyond the nominal ramp endpoint.

door1
  is a           box 4 by 42 by 32 cm, 0.45 kg
  at             −1.513634 m along, 0.09 m to the right, 0.18 m up
  friction       0.72
  bounce         0.04
  turns on       door1 hinge, about z, at its left side
  swings         from −70° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°

pendulum pivot
  is a  point
  at    −1.9583 m along, 0.024 m to the right, 0.57 m up

-- Bob and attached rod together weigh 0.35 kg.
-- Pivot-to-bob-centre length is 0.50 m.

pendulum1
  is a           sphere 7 cm radius, 0.28 kg
  at             −1.9583 m along, 0.024 m to the right, 0.07 m up
  friction       0.72
  bounce         0.04
  turns on       pendulum1 hinge, about y, at pendulum pivot
  swings         from 0° to 45°
  damping        0.04 N·m·s/rad
  starts turned  0°

pendulum rod
  is a         rod 4 cm thick, from pendulum pivot to pendulum1's top
  weighs       0.07 kg
  attached to  pendulum1
  friction     0.72
  bounce       0.04

block1
  is a      cube 12 cm, 0.35 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −2.3681 m along, 0.04 m to the right, 0.06 m up

block left guide
  is a      box 68 by 2 by 4 cm
  at        −2.4281 m along, 0.035 m to the left, 0.02 m up
  friction  0.72
  bounce    0.04

block right guide
  is a      box 68 by 2 by 4 cm
  at        −2.4281 m along, 0.115 m to the right, 0.02 m up
  friction  0.72
  bounce    0.04

-- Cart2 and its light upright striker together weigh 0.50 kg.
-- The upright carries the floor-level cart's impact to the raised seesaw.

cart2
  is a         box 22 by 18 by 10 cm, 0.48 kg
  at           −2.8881 m along, 0.04 m to the right, 0.05 m up
  friction     0.72
  bounce       0.04
  slides on    cart2 slide, along x
  travels      from −65 cm to 0 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart2 upright
  is a         box 2 by 6 by 79 cm, 0.02 kg
  at           −2.9881 m along, 0.04 m to the right, 0.495 m up
  attached to  cart2
  friction     0.72
  bounce       0.04

seesaw pivot
  is a  point
  at    −3.7431 m along, 0.04 m to the right, 0.90 m up

-- The seesaw assembly has outer dimensions 65 by 10 by 4 cm.
-- Its centre hinge is at the centre of that outer envelope.
-- The two end tines leave a narrow slot for the launch guide.
-- Main beam plus tines weigh 0.55 kg.
-- Its hinge spring counterbalances the carried ball at the initial stop.

seesaw1
  is a           box 51 by 10 by 4 cm, 0.4509646 kg
  at             −3.6731 m along, 0.04 m to the right, 0.90 m up
  friction       0.72
  bounce         0.04
  turns on       seesaw1 hinge, about y, at seesaw pivot
  swings         from 0° to 42°
  spring         0.75 N·m/rad toward 42°
  damping        0.04 N·m·s/rad
  starts turned  0°

seesaw upper tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.9981 m along, 0.01 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

seesaw lower tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.9981 m along, 0.07 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

-- These fixed posts fit through the fork's central slot.
-- They suppress the horizontal component of the ball's launch.
-- At the final seesaw angle, the tines are clear of the falling line.

ball3 forward guide
  is a      box 1 by 1.8 by 85 cm
  at        −4.0031 m along, 0.04 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3 rear guide
  is a      box 1 by 1.8 by 85 cm
  at        −4.1131 m along, 0.04 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −4.0581 m along, 0.04 m to the right, 0.97 m up

ring2
  is a      ring 17.12975 cm across, 8 mm thick
  at        −4.0581 m along, 0.04 m to the right, 0.65 m up
  friction  0.72
  bounce    0.04

domino2 platform
  is a      box 45 by 7 by 4 cm
  at        −4.0231 m along, 0.04 m to the right, 0.10 m up
  friction  0.72
  bounce    0.04

domino2 toe
  is a      box 1 by 6 by 3 cm
  at        −4.0681 m along, 0.04 m to the right, 0.135 m up
  friction  0.72
  bounce    0.04

-- The falling line is offset 3.5 cm toward the domino's tipping edge.
-- Ball3's centre falls 24 cm from ring2 before touching the domino top.

domino2
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −4.0231 m along, 0.04 m to the right, 0.24 m up

-- The clear initial domino-to-flap gap is 18 cm.

flap1
  is a           box 4 by 18 by 38 cm, 0.28 kg
  at             −4.2631 m along, 0.04 m to the right, 0.44 m up
  friction       0.72
  bounce         0.04
  turns on       flap1 hinge, about y, at its top
  swings         from 0° to 60°
  damping        0.04 N·m·s/rad
  starts turned  0°

cup1
  is a      catch cup
  at        −4.635 m along, 0.04 m to the right, 0.11 m up
  friction  0.72
  bounce    0.04

-- Shelf top is 55 cm above the cup's inner floor.
-- Its far edge is clear of the flap's initial panel.

shelf1
  is a      box 30 by 25 by 4 cm
  at        −4.44 m along, 0.04 m to the right, 0.55 m up
  friction  0.72
  bounce    0.04

-- The ball is offset on the shelf toward the flap's swept path.

ball4
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  on        shelf1, −4.40 m along, 0.04 m to the right

-- Catch extensions remove excess horizontal speed above the cup.
-- They meet the cup walls at their tops.

cup backstop
  is a      box 2 by 34 by 80 cm
  at        −4.795 m along, 0.04 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

cup left catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.635 m along, 0.12 m to the left, 0.62 m up
  friction  0.72
  bounce    0.04

cup right catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.635 m along, 0.20 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

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
  cart2 upright touches seesaw1
  seesaw upper tine touches ball3
  ball3 drops through ring2
  ball3 touches domino2
  domino2 touches flap1
  flap1 reaches its upper stop
  flap1 touches ball4
  ball4 comes to rest in cup1
```