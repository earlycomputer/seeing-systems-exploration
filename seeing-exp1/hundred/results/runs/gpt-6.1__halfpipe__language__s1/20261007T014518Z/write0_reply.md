```parts
part halfpipe track
  near lip
    is a  point
    at    -1.2 m along, 53 cm up
  near shoulder
    is a  point
    at    -90 cm along, 33 cm up
  near curve
    is a  point
    at    -60 cm along, 20 cm up
  near bottom
    is a  point
    at    -30 cm along, 14.5 cm up
  bottom
    is a  point
    at    13 cm up
  far bottom
    is a  point
    at    30 cm along, 14.5 cm up
  far curve
    is a  point
    at    60 cm along, 20 cm up
  far shoulder
    is a  point
    at    90 cm along, 33 cm up
  far lip
    is a  point
    at    1.2 m along, 53 cm up

  near upper deck
    is a  plank from near lip to near shoulder, 50 cm wide, 4 cm thick
  near middle deck
    is a  plank from near shoulder to near curve, 50 cm wide, 4 cm thick
  near lower deck
    is a  plank from near curve to near bottom, 50 cm wide, 4 cm thick
  near bottom deck
    is a  plank from near bottom to bottom, 50 cm wide, 4 cm thick
  far bottom deck
    is a  plank from bottom to far bottom, 50 cm wide, 4 cm thick
  far lower deck
    is a  plank from far bottom to far curve, 50 cm wide, 4 cm thick
  far middle deck
    is a  plank from far curve to far shoulder, 50 cm wide, 4 cm thick
  far upper deck
    is a  plank from far shoulder to far lip, 50 cm wide, 4 cm thick

  left rail
    is a  box 2.48 m by 4 cm by 80 cm
    at    27 cm to the left, 42 cm up
  right rail
    is a  box 2.48 m by 4 cm by 80 cm
    at    27 cm to the right, 42 cm up
```

```world
world  halfpipe striker chain

floor
  size      10 m
  friction  0.8, spinning 0.01, rolling 0.005

halfpipe
  is a      halfpipe track
  friction  0.35, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    grey

approach top
  is a  point
  at    -2.2 m along, 1.28 m up

ramp
  is a       ramp
  high end   approach top
  low end    halfpipe.near lip
  width      50 cm
  thickness  4 cm
  friction   0.35, spinning 0.001, rolling 0.0002
  bounce     dead
  colour     wood

-- The ramp is 1.25 m long. Starting 25 cm from its top
-- places ball1 exactly 1 m up the ramp from its foot.
ball1
  is a      sphere 8 cm radius, 600 g
  moves     freely
  rolls
  on        ramp.deck, 25 cm from the top
  friction  0.35, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    orange

striker platform
  is a      box 50 by 44 by 5 cm
  at        1.43 m along, 52.5 cm up
  friction  0.1, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    wood

block
  is a      box 20 by 28 by 16 cm, 350 g
  moves     freely
  on        striker platform, 1.35 m along
  friction  0.1, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    orange

pendulum pivot
  is a  point
  at    1.85 m along, 1.53 m up

pendulum
  is a           sphere 10 cm radius, 450 g
  at             1.85 m along, 63 cm up
  turns on       pendulum hinge, about y, at pendulum pivot
  swings         from -100° to 10°
  starts turned  0°
  damping        0.006 N·m·s/rad
  friction       0.15, spinning 0.001, rolling 0.0002
  bounce         dead
  colour         orange

pendulum rod
  is a         rod 8 mm thick, from pendulum pivot to pendulum's top
  weighs       20 g
  attached to  pendulum
  colour       grey

target perch
  is a      box 10 by 18 by 3 cm
  at        2.07 m along, 55.5 cm up
  friction  0.08, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    wood

ball2
  is a      sphere 6 cm radius, 200 g
  moves     freely
  rolls
  on        target perch
  friction  0.15, spinning 0.005, rolling 0.005
  bounce    dead
  colour    white

hoop
  is a    ring 1.8 m across, 8 mm thick
  at      2.8 m along, 35 cm up
  bounce  dead
  colour  orange

cup
  is an           open box
  length          2.4 m
  width           2 m
  walls           26 cm
  wall thickness  4 cm
  base thickness  3 cm
  at              2.9 m along
  friction        0.9, spinning 0.02, rolling 0.015
  bounce          dead
  colour          grey

expect
  ball1 touches ramp
  ball1 touches halfpipe
  ball1 touches block
  block touches pendulum
  pendulum touches ball2
  ball2 drops through hoop
  ball2 comes to rest in cup
```

---
thinking (summarized):

**Evaluating physics setup**

I’m considering the setup with a block on a shallow incline of 30 degrees and how the ball might interact with it. The block would slide immediately unless there’s significant static friction on the flat platform. I could also think about placing the block on a horizontal surface after a curve, maybe with a halfpipe that has a modest upward angle of 20 degrees to cause a hop. The heights I’m imagining are around 0.6 for the block bottom, and I need to consider the sphere’s center in relation to that.

**Analyzing halfpipe dimensions**

I'm breaking down some measurements for a halfpipe. The far end is at x1.2 with a z value of 0.75, and there's a block on the platform's top at 0.79 with a center value of 1.45. The ball has a radius of 0.08, and it reaches the center at approximately 0.87 before hitting the left face of the block at 1.39 for the ball's center at 1.31. I also need to consider the approach end at x1.2 with a z value.

**Evaluating pendulum and collisions**

I’m looking at a pendulum setup with a .65 kg ball and a .2 kg target ball, aiming for a target velocity of around 2 m/s. There’s a need for high damping and dead contacts, and I’m considering the coefficients of restitution in simulations. If I handle the collisions properly, I can potentially achieve the desired effects, but I’m also factoring in how the setup's dimensions and angles come into play. It’s all about finding the right balance for everything to work smoothly!

**Designing cup and pendulum setup**

I’m working on a huge cup with very low friction, aiming for it to roll to a stop in about 6 seconds. The second ball's speed needs to be around 1-3 m/s with specific cup friction levels. I’m adjusting the dimensions to ensure proper functionality—making the cup 2.4 by 1.8 meters and considering wall height too. There are some concerns about timing with the pendulum and ball interactions, but overall, I think the design can support smooth collisions and stable positioning.

**Evaluating ramp geometry**

I'm concerned about the primitive sphere's placement on a sloping deck. It needs to be specified more clearly, like "on ramp, 25 cm from the top," which should work better as "on ramp.deck, 25 cm from the top." The ramp width is .5 foot and needs to center correctly along the deck's centerline.

It's also fine if the rails aren't necessary since everything is coplanar, but adding them may still help visually. I have to ensure the point offsets are correct and that there's no issue with negative values for positioning.