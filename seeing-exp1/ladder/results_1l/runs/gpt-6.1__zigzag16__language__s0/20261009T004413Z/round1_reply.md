The run does **not** complete the chain. Ball1 drops through ring1 and touches lever1, but the lever only reaches about −1.1°: cart1 remains pressed against it and never slides. Ball2 independently falls off the high end of the ramp, contacts the ramp leg and domino platform, and settles there without being struck by domino1.

Ball1 subsequently falls to the floor and rolls into door1, which turns only about −9.8°. Pendulum1, block1, cart2, domino2, and flap1 remain stationary. Ball3 is never launched, and ball4 remains on shelf1 rather than entering cup1.

The revision below removes the initial lever–cart contact, uses a separate gravity-held release gate, and corrects ball2’s placement on the ramp’s uphill-facing normal. It has not yet been run.

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
world  gated gravity cascade

-- Gravity is the language default: 9.81 m/s².
-- Every moving body starts with zero linear and angular velocity.

floor
  size      12 m
  friction  0.72

lever pivot
  is a  point
  at    0 m along, 0 m to the left, 0.55 m up

-- Lever and attached gate lifter together weigh 0.50 kg.

lever1
  is a           box 60 by 10 by 4 cm, 0.497 kg
  at             lever pivot
  friction       0.72
  bounce         0.04
  turns on       lever1 hinge, about y, at lever pivot
  swings         from −45° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°

lever gate lifter
  is a         box 1.5 by 3.5 by 16.5 cm, 3 g
  at           0.10 m along, 0 m to the left, 0.6525 m up
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

-- This independent gate holds cart1, not lever1.
-- The lifter begins 1 cm below the gate.
-- A small upward gate movement clears the cart's top edge.

cart1 release gate
  is a         box 27 by 11 by 1 cm, 10 g
  at           0.165 m along, 0.04 m to the right, 0.75 m up
  friction     0.72
  bounce       0.04
  slides on    cart1 gate slide, along z
  travels      from 0 cm to 5 cm
  damping      0.20 N·s/m
  starts slid  0 cm

-- The cart begins above and clear of the lever.
-- The gate restrains its spring until the falling ball tips the lever.
-- The rising lever end can then strike the moving cart's underside.

cart1
  is a         box 22 by 18 by 10 cm, 0.50 kg
  at           0.41 m along, 0.09 m to the right, 0.70 m up
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

-- Endpoint centres are 1.00 m apart at 20 degrees.
-- With the 4 cm deck thickness, its low top surface is at 0.15 m.
-- The uphill-facing surface normal points toward negative x.

ramp high
  is a  point
  at    −0.406059 m along, 0.09 m to the right, 0.473226 m up

ramp low
  is a  point
  at    −1.345752 m along, 0.09 m to the right, 0.131206 m up

ramp1
  is a       ramp
  high end   ramp high
  low end    ramp low
  width      30 cm
  thickness  4 cm
  friction   0.72
  bounce     0.04

-- The ball is displaced from the high endpoint by the correct
-- upward surface normal, rather than beyond the unsupported uphill edge.

ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −0.43 m along, 0.09 m to the right, 0.539004 m up

ball2 retaining lip
  is a      box 1 by 12 by 2 cm
  at        −0.48 m along, 0.09 m to the right, 0.492 m up
  friction  0.72
  bounce    0.04

-- A tapered cover leaves room to cross the retaining lip,
-- then keeps an energetic ball on the descending ramp.

ramp cover high
  is a  point
  at    −0.474463 m along, 0.09 m to the right, 0.661165 m up

ramp cover low
  is a  point
  at    −1.390899 m along, 0.09 m to the right, 0.255245 m up

ramp cover
  is a      plank from ramp cover high to ramp cover low, 30 cm wide, 2 cm thick
  friction  0.72
  bounce    0.04

-- The incoming door face is 10 cm beyond the ramp endpoint.

door1
  is a           box 4 by 42 by 32 cm, 0.45 kg
  at             −1.465752 m along, 0.09 m to the right, 0.18 m up
  friction       0.72
  bounce         0.04
  turns on       door1 hinge, about z, at its left side
  swings         from −70° to 0°
  damping        0.04 N·m·s/rad
  starts turned  0°

pendulum pivot
  is a  point
  at    −1.910418 m along, 0.024 m to the right, 0.57 m up

-- Bob and attached rod together weigh 0.35 kg.
-- Pivot-to-bob-centre length is 0.50 m.

pendulum1
  is a           sphere 7 cm radius, 0.28 kg
  at             −1.910418 m along, 0.024 m to the right, 0.07 m up
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
  at        −2.320218 m along, 0.04 m to the right, 0.06 m up

block left guide
  is a      box 68 by 2 by 4 cm
  at        −2.380218 m along, 0.035 m to the left, 0.02 m up
  friction  0.72
  bounce    0.04

block right guide
  is a      box 68 by 2 by 4 cm
  at        −2.380218 m along, 0.115 m to the right, 0.02 m up
  friction  0.72
  bounce    0.04

-- Cart2 and its upright together weigh 0.50 kg.
-- Block1 travels 35 cm before reaching the cart's incoming face.

cart2
  is a         box 22 by 18 by 10 cm, 0.48 kg
  at           −2.840218 m along, 0.04 m to the right, 0.05 m up
  friction     0.72
  bounce       0.04
  slides on    cart2 slide, along x
  travels      from −65 cm to 0 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart2 upright
  is a         box 2 by 6 by 79 cm, 0.02 kg
  at           −2.940218 m along, 0.04 m to the right, 0.495 m up
  attached to  cart2
  friction     0.72
  bounce       0.04

seesaw pivot
  is a  point
  at    −3.695218 m along, 0.04 m to the right, 0.90 m up

-- Main beam and end tines have a combined mass of 0.55 kg.
-- Their outer envelope is 65 by 10 by 4 cm, hinged at its centre.
-- The fork admits the fixed vertical launch guides.
-- Cart2's upright reaches the struck end after 42 cm of travel.

seesaw1
  is a           box 51 by 10 by 4 cm, 0.4509646 kg
  at             −3.625218 m along, 0.04 m to the right, 0.90 m up
  friction       0.72
  bounce         0.04
  turns on       seesaw1 hinge, about y, at seesaw pivot
  swings         from 0° to 42°
  spring         0.75 N·m/rad toward 42°
  damping        0.04 N·m·s/rad
  starts turned  0°

seesaw upper tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.950218 m along, 0.01 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

seesaw lower tine
  is a         box 14 by 4 by 4 cm, 0.0495177 kg
  at           −3.950218 m along, 0.07 m to the right, 0.90 m up
  attached to  seesaw1
  friction     0.72
  bounce       0.04

ball3 forward guide
  is a      box 1 by 1.8 by 85 cm
  at        −3.955218 m along, 0.04 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3 rear guide
  is a      box 1 by 1.8 by 85 cm
  at        −4.065218 m along, 0.04 m to the right, 1.225 m up
  friction  0.72
  bounce    0.04

ball3
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        −4.010218 m along, 0.04 m to the right, 0.97 m up

ring2
  is a      ring 16 cm across, 8 mm thick
  at        −4.010218 m along, 0.04 m to the right, 0.65 m up
  friction  0.72
  bounce    0.04

domino2 platform
  is a      box 45 by 7 by 4 cm
  at        −3.975218 m along, 0.04 m to the right, 0.10 m up
  friction  0.72
  bounce    0.04

domino2 toe
  is a      box 1 by 6 by 3 cm
  at        −4.020218 m along, 0.04 m to the right, 0.135 m up
  friction  0.72
  bounce    0.04

-- The falling line is offset toward the domino's tipping edge.
-- Ball3's centre is 24 cm below ring2 when it first meets the top.

domino2
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  friction  0.72
  bounce    0.04
  at        −3.975218 m along, 0.04 m to the right, 0.24 m up

-- Initial clear gap from domino2 to flap1 is 18 cm.

flap1
  is a           box 4 by 18 by 38 cm, 0.28 kg
  at             −4.215218 m along, 0.04 m to the right, 0.44 m up
  friction       0.72
  bounce         0.04
  turns on       flap1 hinge, about y, at its top
  swings         from 0° to 60°
  damping        0.04 N·m·s/rad
  starts turned  0°

cup1
  is a      catch cup
  at        −4.587118 m along, 0.04 m to the right, 0.11 m up
  friction  0.72
  bounce    0.04

-- Shelf top is 55 cm above the cup's inner floor.
-- Its far edge is clear of the flap's initial panel.

shelf1
  is a      box 30 by 25 by 4 cm
  at        −4.392118 m along, 0.04 m to the right, 0.55 m up
  friction  0.72
  bounce    0.04

ball4
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  on        shelf1, −4.352118 m along, 0.04 m to the right

-- Catch extensions meet the cup walls at their tops.
-- They arrest excess horizontal motion above the cup.

cup backstop
  is a      box 2 by 34 by 80 cm
  at        −4.747118 m along, 0.04 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

cup left catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.587118 m along, 0.12 m to the left, 0.62 m up
  friction  0.72
  bounce    0.04

cup right catch guide
  is a      box 30 by 2 by 80 cm
  at        −4.587118 m along, 0.20 m to the right, 0.62 m up
  friction  0.72
  bounce    0.04

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever gate lifter touches cart1 release gate
  lever1 touches cart1
  lever1 reaches its lower stop
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

```json
{
  "what_happens": "Ball1 drops through ring1 and touches lever1, but lever1 only turns about 1.1 degrees and cart1 never slides. Ball2 falls off the ramp's high end and settles on the domino platform. Ball1 later rolls along the floor into door1, turning it about 9.8 degrees. The remaining chain does not activate; ball3 is never launched and ball4 remains on shelf1.",
  "works": false,
  "problem": "The chain stalls because cart1 restrains lever1, while ball2 falls off its starting ramp position before domino1 can strike it."
}
```

---
thinking (summarized):

**Calculating dimensions and stability**

I’m trying to determine the necessary dimensions for a project. I need to calculate the initial distances based on measurements like the ball's lip and edge. The numbers include things like the overlap and ensuring it’s ballistic stable at a height of 1 cm. I’m figuring out dimensions for the lipbox and adjusting the center based on the specific targets. It's a bit intricate, but I'm managing to navigate through these calculations!