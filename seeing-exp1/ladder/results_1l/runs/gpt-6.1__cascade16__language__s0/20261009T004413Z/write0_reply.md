This includes passive supports, guides, strikers, and counterweights; moving assemblies retain the specified total masses. The `expect` block states intended checks, not a verified 20-second simulation result.

```world
world  passive ramp and pendulum chain

-- Gravity is the language default: 9.81 m/s².
-- No launch, spin, or nonzero starting joint velocity is used.
-- Attached pieces are included in their moving assembly's stated mass.

floor
  size      18 m
  friction  0.70, spinning 0, rolling 0

ramp1 high
  is a  point
  at    93.969262 cm behind floor, 49.202014 cm up

ramp1 low
  is a  point
  at    0 m along, 15 cm up

ramp1
  is a       ramp
  high end   ramp1 high
  low end    ramp1 low
  width      30 cm
  thickness  4 cm
  friction   0.70, spinning 0, rolling 0
  bounce     0.05

ball1
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on ramp1, 0 cm from the top

domino1
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  stands    on floor, 14 cm beyond ramp1 low

domino2
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  stands    on floor, 18 cm beyond domino1

flap1
  is a          box 4 by 20 by 40 cm, 300 g
  friction      0.70, spinning 0, rolling 0
  bounce        0.05
  stands        on floor, 18 cm beyond domino2
  turns on      flap1 hinge, about y, at its bottom
  swings        from 0° to 65°
  damping       0.04 N·m·s/rad
  starts turned 0°

-- The cart's low striker lets the standing flap contact the elevated cart.
-- Cart assembly mass: 490 g + 10 g = 500 g.

cart1
  is a         box 22 by 18 by 10 cm, 490 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           38 cm beyond flap1, 51.081466 cm up
  slides on    cart1 slide, along x
  travels      from 0 cm to 60 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart1 striker
  is a         box 2 by 18 by 43 cm, 10 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           0 cm beyond cart1, 29.5 cm up
  attached to  cart1

ramp2 high
  is a  point
  at    64 cm beyond cart1, 49.202014 cm up

ramp2 low
  is a  point
  at    93.969262 cm beyond ramp2 high, 15 cm up

ramp2
  is a       ramp
  high end   ramp2 high
  low end    ramp2 low
  width      30 cm
  thickness  4 cm
  friction   0.70, spinning 0, rolling 0
  bounce     0.05

-- A level staging pad prevents ball2 rolling before cart1 arrives.

ramp2 staging pad
  is a      box 6 by 30 by 2 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        4 cm behind ramp2 high, 50.081466 cm up

ball2
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on ramp2 staging pad, 1 cm beyond ramp2 staging pad

lever1 pivot
  is a  point
  at    43 cm beyond ramp2 low, 80 cm up

-- Lever assembly mass:
-- 187 g arm + 5 g striker + 5 g carrier
-- + 300 g counterweight + 3 g counterweight rod = 500 g.
-- The right-hand ball holds the lever against its initial upper stop.
-- A strike on the hanging left-hand striker releases the counterweight.

lever1
  is a          box 60 by 10 by 4 cm, 187 g
  friction      0.70, spinning 0, rolling 0
  bounce        0.05
  at            lever1 pivot
  turns on      lever1 hinge, about y, at lever1 pivot
  swings        from −45° to 0°
  damping       0.04 N·m·s/rad
  starts turned 0°

lever1 striker
  is a         box 2 by 10 by 68 cm, 5 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           30 cm behind lever1, 46 cm up
  attached to  lever1

lever1 carrier
  is a         box 24 by 14 by 1 cm, 5 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  on           lever1, 25 cm beyond lever1
  attached to  lever1

lever1 counterweight anchor
  is a  point
  at    8 cm behind lever1, 80 cm up

lever1 counterweight
  is a         cube 10 cm, 300 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           8 cm behind lever1, 2.4 m up
  attached to  lever1

lever1 counterweight rod
  is a         rod 1 cm thick, from lever1 counterweight anchor to lever1 counterweight's bottom
  weighs       3 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  attached to  lever1

ball3
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on lever1 carrier, 25 cm beyond lever1

-- For a sixteen-segment capsule rim, this centreline diameter gives
-- a 16 cm inscribed clear opening with an 8 mm tube.

ring1
  is a      ring 17.129131 cm across, 8 mm thick
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        0 cm beyond ball3, 35 cm below ball3

-- These fixed guides suppress the launch's horizontal component.
-- Their lower ends leave the pendulum impact unobstructed.

ball3 near guide
  is a      box 2 by 14 by 160 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        6.5 cm behind ball3, 1.2 m up

ball3 far guide
  is a      box 2 by 14 by 160 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        6.5 cm beyond ball3, 1.2 m up

ball3 left guide
  is a      box 11 by 2 by 160 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        0 cm beyond ball3, 6.5 cm left of ball3, 1.2 m up

ball3 right guide
  is a      box 11 by 2 by 160 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        0 cm beyond ball3, 6.5 cm right of ball3, 1.2 m up

pendulum1 resting bob
  is a  point
  at    8 cm beyond ball3, 19.055728 cm up

pendulum1 pivot
  is a  point
  at    0 cm beyond pendulum1 resting bob, 50 cm above pendulum1 resting bob

-- Pendulum assembly mass: 10 g bob + 340 g rigid rod = 350 g.
-- The off-centre falling-ball impact supplies a clockwise impulse.

pendulum1
  is a          sphere 14 cm across, 10 g
  friction      0.70, spinning 0, rolling 0
  bounce        0.05
  at            pendulum1 resting bob
  turns on      pendulum1 hinge, about y, at pendulum1 pivot
  swings        from −40° to 0°
  damping       0.04 N·m·s/rad
  starts turned 0°

pendulum1 rod
  is a         rod 1 cm thick, from pendulum1 pivot to pendulum1's top
  weighs       340 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  attached to  pendulum1

-- Contact is positioned at a 0.32 m bob arc, or 36.67 degrees.
-- The hinge permits continued travel to 40 degrees.

domino3
  is a      box 8 by 4 by 24 cm, 250 g
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  stands    on floor, 38.8083 cm beyond pendulum1

-- Door assembly mass: 240 g panel + 200 g counterweight
-- + 10 g rigid rod = 450 g.
-- Its counterweight is outside the block and cart lane.

door1
  is a          box 4 by 32 by 42 cm, 240 g
  friction      0.70, spinning 0, rolling 0
  bounce        0.05
  stands        on floor, 24 cm beyond domino3
  turns on      door1 hinge, about y, at its bottom
  swings        from 0° to 70°
  damping       0.04 N·m·s/rad
  starts turned 0°

door1 counterweight anchor
  is a  point
  at    0 cm beyond door1, 16 cm left of door1, 0 cm up

door1 counterweight
  is a         cube 10 cm, 200 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           0 cm beyond door1, 16 cm left of door1, 1 m up
  attached to  door1

door1 counterweight rod
  is a         rod 1 cm thick, from door1 counterweight anchor to door1 counterweight's bottom
  weighs       10 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  attached to  door1

block1
  is a      cube 12 cm, 350 g
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on floor, 14 cm beyond door1

-- Cart assembly mass: 490 g + 10 g = 500 g.
-- Its hanging rear striker receives the floor-level block.

cart2
  is a         box 22 by 18 by 10 cm, 490 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           66 cm beyond door1, 51.081466 cm up
  slides on    cart2 slide, along x
  travels      from 0 cm to 55 cm
  damping      0.20 N·s/m
  starts slid  0 cm

cart2 striker
  is a         box 2 by 18 by 52 cm, 10 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           10 cm behind cart2, 28 cm up
  attached to  cart2

ramp3 high
  is a  point
  at    61 cm beyond cart2, 49.202014 cm up

ramp3 low
  is a  point
  at    93.969262 cm beyond ramp3 high, 15 cm up

ramp3
  is a       ramp
  high end   ramp3 high
  low end    ramp3 low
  width      30 cm
  thickness  4 cm
  friction   0.70, spinning 0, rolling 0
  bounce     0.05

ramp3 staging pad
  is a      box 6 by 30 by 2 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        4 cm behind ramp3 high, 50.081466 cm up

ball4
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on ramp3 staging pad, 1 cm beyond ramp3 staging pad

-- Flap assembly mass: 270 g panel + 6 g riser + 4 g striker = 280 g.
-- The offset overhead striker reaches the shelf without crossing it.

flap2
  is a          box 4 by 18 by 38 cm, 270 g
  friction      0.70, spinning 0, rolling 0
  bounce        0.05
  stands        on floor, 12 cm beyond ramp3 low
  turns on      flap2 hinge, about y, at its bottom
  swings        from 0° to 60°
  damping       0.04 N·m·s/rad
  starts turned 0°

flap2 riser
  is a         box 2 by 2 by 52 cm, 6 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           0 cm beyond flap2, 64 cm up
  attached to  flap2

flap2 striker
  is a         box 2 by 32 by 2 cm, 4 g
  friction     0.70, spinning 0, rolling 0
  bounce       0.05
  at           0 cm beyond flap2, 14 cm left of flap2, 91 cm up
  attached to  flap2

shelf1
  is a      box 30 by 25 by 4 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        7 cm beyond flap2, 28 cm left of flap2, 78 cm up

ball5
  is a      sphere 10 cm across, 200 g
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  rests     on shelf1, 13 cm beyond shelf1, 0 cm left of shelf1

ring2
  is a      ring 17.129131 cm across, 8 mm thick
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        5 cm beyond ball5, 0 cm left of ball5, 30 cm below ball5

-- The short catch wall removes the shelf-exit horizontal motion.
-- Its top is low enough for the flap's overhead striker to pass.

ball5 far guide
  is a      box 2 by 14 by 47.5 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        12 cm beyond ball5, 0 cm left of ball5, 58.75 cm up

ball5 near guide
  is a      box 2 by 14 by 38 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        2 cm behind ball5, 0 cm left of ball5, 55 cm up

ball5 left guide
  is a      box 12 by 2 by 40 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        0 cm beyond ring2, 7 cm left of ring2, 55 cm up

ball5 right guide
  is a      box 12 by 2 by 40 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  at        0 cm beyond ring2, 7 cm right of ring2, 55 cm up

bin pedestal
  is a      box 36 by 36 by 13 cm
  friction  0.70, spinning 0, rolling 0
  bounce    0.05
  on        floor, centred over ring2

-- Walls centred on a 34 cm base leave a 32 cm inner footprint.
-- Base top is 15 cm high; a resting ball's centre is 20 cm high,
-- 35 cm below ring2.

bin1
  is an           open box
  length          34 cm
  width           34 cm
  walls           20 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        0.70, spinning 0, rolling 0
  bounce          0.05
  on              bin pedestal

expect
  ball1 touches ramp1
  ball1 touches domino1
  domino1 touches domino2
  domino2 touches flap1
  flap1 touches cart1
  cart1 touches ball2
  ball2 touches ramp2
  ball2 touches lever1
  lever1 reaches its lower stop
  ball3 drops through ring1
  ball3 touches pendulum1
  pendulum1 touches domino3
  domino3 touches door1
  door1 touches block1
  block1 touches cart2
  cart2 touches ball4
  ball4 touches ramp3
  ball4 touches flap2
  flap2 touches ball5
  ball5 drops through ring2
  ball5 comes to rest in bin1
```

---
thinking (summarized):

**Figuring out projections**

I’m calculating values related to a cart and some other measurements. It seems like I’m trying to position something with specific height requirements and determine where it fits. The numbers I’ve noted include 0.11 left, 0.37 for contacts, and others like 0.44 and 0.49 for the cart’s positioning. I also think about a flap reaching below the cart, so maybe adjusting that downward to 0.43 could help. I’ll need to organize these thoughts more clearly!

**Evaluating cart design feasibility**

I’m considering the design of a transfer cart and how the flap at the upper part can be integrated. It's essential to know if the flap hinge supports the cart's bottom and to assess the dimensions involved. I calculate the flap diameter and check the angle to ensure it's practical. I need to evaluate how the cart overlaps with the flap's initial position to confirm if everything fits together as intended.

**Analyzing cart and flap dimensions**

I’m working through the dimensions of a transfer cart and how the flap interacts with it. The flap width is 0.04, and I need to ensure there's no overlap at an angle of around 65 degrees while checking the pivot and various coordinate positions. I'm measuring the interaction points, especially concerning the sphere's radius and the thresholds required for ball movement. Ensuring all these elements work together is crucial for successful operation.

**Clarifying ramp dimensions**

I’m analyzing the dimensions for ramp 1, specifically focusing on its position and height. The low point appears to be at coordinates x0 and y0, with a top surface height of 0.15 and the higher point at 0.17. However, the high position isn’t fully defined since I see an incomplete notation with x-. I need to ensure I correctly establish all those measurements for accurate construction or operation of the ramp.

**Analyzing ball launch mechanics**

I'm working on moving the scoop center from the right x.15 to -0.077 relative to a pivot, and realizing that decreasing x by .23 means the ball will only move horizontally. If I guide the ball at initial x + 0.15, would the shelf disappear and then fall? Then, there's the need for a full launch angle of 45 degrees, but I want the ball to rise gently. It seems to raise vertically, but I'm concerned about dimensions and how they all fit together.

**Exploring lever and pendulum mechanics**

I'm thinking about adding a long carrier lever of 0.6 meters with an upward guide that supports the ball beneath the initial x of 0.15 until a certain angle is achieved. It seems like the ball can launch a few centimeters if I apply enough angular speed with a spring. I need to ensure that the ball stays in contact long enough, but it tends to slide off after about 60 degrees. There are several factors affecting how torque and trajectory come into play, especially regarding the impact with the pendulum bob.

**Designing pendulum mechanics**

I'm figuring out how the ring falls about 0.25 to touch the bob, affecting the impact elevation at zball3. I need to lower the bob center based on some calculations involving the radius. The pendulum has a length of 0.5 meters and a mass of 0.35, along with a bob sphere radius of about 0.045. I need to name the pendulum using a custom part, describing it as a rod that turns at the hinge with a bob attached. I want to make sure it's all clear and accurate!

**Exploring simulation challenges**

I'm considering the challenges with the high-end ramp setup and how the ball interacts with it. There isn't a strict match, so I'll need to mention fundamental incompatibilities and how to implement extra attachments. I can't refuse the request but need to clarify that conflicts exist. I should express that "the literal brief has geometric conflicts" and that outcomes can't be verified. My goal is to engineer a reliable setup, maximizing function with passive springs and thoughtful design.

**Analyzing spring mechanics**

I'm starting to think about the rest spring preloads and how they can help encode torque to guarantee the chain's effectiveness. The setup involves gravity-driven seed balls, with springs driving mechanisms based on input, secured by physical latches. I don’t need to state constraints for the springs explicitly. Adding arms could support the geometry necessary for contact, allowing initial springs to push, unless blocked by latches or other mechanisms like flap clocks. The dynamics of flap1 and spring positions will be crucial in managing impacts effectively.

**Analyzing pedestal adjustments**

I’m looking to add a pedestal with dimensions 0.36 by 0.36 by 0.13, and I need to consider how it interacts with the underbin causes and the base bottom. I’ll position bin1 raised by 13 cm, aligning it centered over ring2, but duplicating x and z might affect how centered it actually is. So, I need to focus on x and y adjustments if I want to raise the height to 13 cm while setting the z-low correctly.

**Visualizing staging setup**

I’m thinking about how to add a horizontally fixed lip to the "ramp2 staging pad." It needs to be centered above the high-end ramp joins, and I want the ball to rest on the pad, in a horizontal tangent at z.54. I’m considering shelf support slopes, too, to ensure everything is stable. After that, I’ll visualize how the ball will rest on this platform. There's a lot to confirm for this setup!

**Calculating ball launch parameters**

I’m looking at the launch parameters for a ball. The launch speed seems to be around 2.828 m/s with a rise of about 0.408 meters, reaching an apex of around 1.45 meters. If I'm calculating correctly, the top safety height appears to be 2.0 meters. I want to confirm that these numbers are accurate to ensure safety and effectiveness. Let’s verify if those values align with practical expectations!

**Evaluating ball contact mechanics**

I need to ensure that when the beam contacts the ball, it should hit above its center and push down rather than up. I noticed the initial beam measurement is z=0.89, not 0.87 at first contact, with an angle of 9.7 degrees. The z position of 0.877 is above the ball center of 0.85, so hitting the upper left produces a downward force that aids in channeling the ball once it passes the edge.

**Defining cart components**

I'm thinking about defining parts for the "slide cart." The top-level component, cart1, would include bodyboxpluspost with names like cart1 and so on. I need to incorporate tool capabilities at the top level for resolution and all geometries. Creating new parts with names matching collision elements, like cart1_, lever1_, and door1_, will be helpful. This way, I can expect to collect together pieces with matching name prefixes.