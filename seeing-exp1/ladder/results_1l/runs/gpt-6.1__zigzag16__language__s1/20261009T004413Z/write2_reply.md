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


part notched shelf
  needs  centre

  anchor
    is a  point
    at    centre

  main board
    is a  box 10.4 by 25 by 4 cm
    at    9.8 cm behind anchor, 0 cm left of anchor, level with anchor

  left finger
    is a  box 19.6 by 3 by 4 cm
    at    5.2 cm beyond anchor, 11 cm left of anchor, level with anchor

  right finger
    is a  box 19.6 by 3 by 4 cm
    at    5.2 cm beyond anchor, 11 cm right of anchor, level with anchor
```

```world
world  gravity and spring cascade

-- Gravity is the language's fixed 9.81 m/s².
-- Every body starts with zero velocity.
-- Expectations are intended checks, not verified simulation results.

floor
  size      8 m
  friction  0.72, spinning 0.005, rolling 0.0002

lever1 pivot
  is a  point
  at    0 m along, 10 cm to the right, 58 cm up

lever1
  is a      box 60 by 10 by 4 cm, 0.50 kg
  at        lever1 pivot
  friction  0.72
  bounce    0.04
  turns on  lever1 hinge, about y, at lever1 pivot
  swings    from -45 deg to 0 deg
  damping   0.04 N·m·s/rad
  colour    wood

ring1
  is a      ring 16 cm across, 4 mm thick
  at        28 cm behind lever1, 10 cm to the right, 90 cm up
  friction  0.72
  bounce    0.04
  colour    orange

ball1
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  at        28 cm behind lever1, 10 cm to the right, 30 cm above ring1
  colour    orange

cart1
  is a      box 22 by 18 by 10 cm, 0.50 kg
  at        33.5 cm beyond lever1, 0 m to the left, 69 cm up
  slides on cart1 slide, along x
  travels   from -65 cm to 0 cm
  damping   0.20 N·s/m
  friction  0.72
  bounce    0.04
  colour    grey

domino1 pedestal
  is a      box 10 by 8 by 45 cm
  stands    on floor, 23.5 cm behind lever1, 7 cm to the left
  friction  0.72
  bounce    0.04
  colour    dark grey

domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  stands    on domino1 pedestal, centred over domino1 pedestal
  moves     freely
  friction  0.72
  bounce    0.04
  colour    white

-- These points describe the deck centreline.
-- Its top surface at the low end is 0.15 m above the floor.
ramp1 high end
  is a  point
  at    -0.39105859 m along, 7 cm to the left, 0.47322629 m up

ramp1 low end
  is a  point
  at    -1.33075121 m along, 7 cm to the left, 0.13120615 m up

ramp1
  is a      plank from ramp1 high end to ramp1 low end, 30 cm wide, 4 cm thick
  friction  0.72
  bounce    0.04
  colour    wood

ball2 chock
  is a      box 16 by 100 by 15 mm
  at        -0.441 m along, 7 cm to the left, 0.4852 m up
  friction  0.72
  bounce    0.04
  colour    dark grey

ball2
  is a      sphere 10 cm across, 0.20 kg
  at        18 cm behind domino1, 7 cm to the left, 0.53900477 m up
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  colour    orange

-- The door is bottom-hinged.
-- Its approaching face is 0.10 m beyond the ramp's low surface edge.
door1
  is a      box 4 by 32 by 42 cm, 0.45 kg
  at        -1.45759161 m along, 7 cm to the left, 31 cm up
  turns on  door1 hinge, about y, at its bottom
  swings    from -70 deg to 0 deg
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    0.04
  colour    wood

door1 pendulum support
  is a         box 6 by 10 by 0.8 cm, 5 g
  at           -1.45759161 m along, 36 cm to the left, 31.1 cm up
  attached to  door1
  friction     0.72
  bounce       0.04
  colour       wood

pendulum pivot
  is a  point
  at    -1.81114500 m along, 36 cm to the left, 0.01144661 m up

pendulum initial tip
  is a  point
  at    -1.45759161 m along, 36 cm to the left, 0.365 m up

-- Rod plus bob have total mass 0.35 kg and a 0.50 m rigid length.
pendulum1
  is a      rod 12 mm thick, from pendulum pivot to pendulum initial tip
  weighs    0.10 kg
  turns on  pendulum1 hinge, about y, at pendulum pivot
  swings    from 0 deg to 38 deg
  spring    70 N·m/rad toward 38 deg
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    0.04
  colour    dark grey

pendulum1 bob
  is a         sphere 10 cm across, 0.25 kg
  at           pendulum initial tip
  attached to  pendulum1
  friction     0.72
  bounce       0.04
  colour       grey

block1
  is a      cube 12 cm, 0.35 kg
  stands    on floor, -1.20487194 m along, 36 cm to the left
  moves     freely
  friction  0.72
  bounce    0.04
  colour    wood

-- The cart is carried by its slide, 5 mm clear of the floor.
cart2
  is a      box 22 by 18 by 10 cm, 0.50 kg
  at        -0.68487194 m along, 36 cm to the left, 5.5 cm up
  slides on cart2 slide, along x
  travels   from 0 cm to 140 cm
  damping   0.20 N·s/m
  friction  0.72
  bounce    0.04
  colour    grey

seesaw1 pivot
  is a  point
  at    0.05512806 m along, 36 cm to the left, 1.30 m up

seesaw1
  is a      box 65 by 10 by 4 cm, 0.55 kg
  at        seesaw1 pivot
  turns on  seesaw1 hinge, about y, at seesaw1 pivot
  swings    from -42 deg to 0 deg
  spring    0.80 N·m/rad toward -42 deg
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    0.04
  colour    wood

seesaw left striker top
  is a  point
  at    -0.26987194 m along, 36 cm to the left, 1.30 m up

seesaw left striker tip
  is a  point
  at    -0.14487194 m along, 36 cm to the left, 4.5 cm up

seesaw1 left striker
  is a         rod 20 mm thick, from seesaw left striker top to seesaw left striker tip
  weighs       15 g
  attached to  seesaw1
  friction     0.72
  bounce       0.04
  colour       dark grey

ball3
  is a      sphere 10 cm across, 0.20 kg
  at        0.39012806 m along, 36 cm to the left, 1.36898979 m up
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  colour    orange

ball3 right guide
  is a      box 2 by 14 by 100 cm
  at        0.45512806 m along, 36 cm to the left, 1.59 m up
  friction  0.72
  bounce    0.04
  colour    glass

ball3 left-side guide
  is a      box 12 by 2 by 100 cm
  at        0.39012806 m along, 42.5 cm to the left, 1.59 m up
  friction  0.72
  bounce    0.04
  colour    glass

ball3 right-side guide
  is a      box 12 by 2 by 100 cm
  at        0.39012806 m along, 29.5 cm to the left, 1.59 m up
  friction  0.72
  bounce    0.04
  colour    glass

ring2
  is a      ring 16 cm across, 4 mm thick
  at        centred over ball3, 32 cm below ball3
  friction  0.72
  bounce    0.04
  colour    orange

-- All three dimensions use metres, avoiding mixed-unit size interpretation.
domino2 pedestal
  is a      box 0.12 by 0.08 by 0.51898979 m
  stands    on floor, 0.42012806 m along, 36 cm to the left
  friction  0.72
  bounce    0.04
  colour    dark grey

domino2
  is a      box 8 by 4 by 24 cm, 0.25 kg
  stands    on domino2 pedestal, centred over domino2 pedestal
  moves     freely
  friction  0.72
  bounce    0.04
  colour    white

flap1
  is a      box 4 by 18 by 38 cm, 0.28 kg
  at        0.18012806 m along, 36 cm to the left, 0.70898979 m up
  turns on  flap1 hinge, about y, at its bottom
  swings    from -60 deg to 0 deg
  damping   0.04 N·m·s/rad
  friction  0.72
  bounce    0.04
  colour    wood

cup1
  is a      catch cup
  at        -0.19487194 m along, 36 cm to the left, on floor
  friction  0.72
  bounce    0.04
  colour    grey

shelf1 centre
  is a  point
  at    0.09512806 m along, 36 cm to the left, 55 cm up

-- Overall shelf dimensions remain 0.30 by 0.25 by 0.04 m.
-- The central notch clears both the initial flap and its swept path.
-- Its top is 0.55 m above the cup's inner base.
shelf1
  is a      notched shelf
  centre    shelf1 centre
  friction  0.72
  bounce    0.04
  colour    wood

ball4
  is a      sphere 10 cm across, 0.20 kg
  rests     on shelf1.main board, -0.03987194 m along, 36 cm to the left
  moves     freely
  rolls
  friction  0.72
  bounce    0.04
  colour    orange

cup1 catch backstop
  is a      box 2 by 25 by 70 cm
  at        -0.25487194 m along, 36 cm to the left, 56 cm up
  friction  0.72
  bounce    0.04
  colour    glass

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
  seesaw1 reaches its lower stop
  ball3 drops through ring2
  ball3 touches domino2
  domino2 touches flap1
  flap1 reaches its lower stop
  flap1 touches ball4
  ball4 comes to rest in cup1
```

---
thinking (summarized):

**Clarifying dimensions and placement**

I need to work with mixed units for some parts, ensuring consistency. The dimensions for the box appear uniform, but I’m checking the specifics for shelf1, which is 30 by 25 by 4 cm. I’m verifying how the center aligns, calculating overlaps, and determining the door hinge flap's rotation against the bottom placement. It's a bit tricky figuring out the semantics of "up" versus "bottom." I want to ensure everything fits and is placed accurately!

**Evaluating parts and translation**

I'm thinking about the origin of basic components in my analysis process. There seems to be an exploration of translation and centering, but some pieces remain unknown or unchanged. I’m compiling everything fine, making sure to address the notched shelf component and its placement in this world perspective. Overall, it feels somewhat static and absolute, and I'm pondering how to make sense of all these elements together.