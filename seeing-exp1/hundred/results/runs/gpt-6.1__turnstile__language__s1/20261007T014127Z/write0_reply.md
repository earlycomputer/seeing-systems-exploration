```world
world  ramp rotor latch and drop

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp foot
  is a  point
  at    0 cm along, 0 cm to the left, 45 cm up

ramp crest
  is a  point
  at    112.5833 cm behind ramp foot, 0 cm to the left, 110 cm up

ramp
  is a       ramp
  high end   ramp crest
  low end    ramp foot
  width      30 cm
  thickness  2 cm
  friction   0.6, spinning 0.001, rolling 0.0001
  colour     wood

runout
  is a      box 78 by 140 by 6 cm
  at        29 cm along, 20 cm to the left, 43 cm up
  friction  0.4, spinning 0.001, rolling 0.0001
  colour    grey

-- This ramp is 1.30 m long: ball1 starts 1 m up from its foot.
ball1
  is a      sphere 6 cm radius, 600 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0001
  rests     on ramp, 30 cm from the top
  colour    orange

rotor pivot
  is a  point
  at    25 cm along, 25 cm to the left, 51.5 cm up

rotor
  is a      box 4 by 130 by 10 cm, 80 g
  at        rotor pivot
  turns on  rotor hinge, about z, at rotor pivot
  swings    from 0° to 24°
  damping   0.004 N·m·s/rad
  armature  0.0002 kg·m²
  bounce    dead
  friction  0.25, spinning 0.001, rolling 0.0001
  colour    black

ball2
  is a      sphere 5 cm radius, 150 g
  moves     freely
  rolls
  bounce    dead
  friction  0.4, spinning 0.001, rolling 0.0001
  at        40 cm along, 35 cm to the right, 51 cm up
  colour    white

striker runway
  is a      box 122 by 20 by 6 cm
  at        119 cm along, 32 cm to the right, 43 cm up
  friction  0.4, spinning 0.001, rolling 0.0001
  colour    grey

-- The free latch is captured in a horizontal sliding channel.
right lower rail
  is a      box 120 by 4 by 4 cm
  at        115 cm along, 41 cm to the right, 45 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

left lower rail
  is a      box 120 by 4 by 4 cm
  at        115 cm along, 11 cm to the left, 45 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

right rail cap
  is a      box 120 by 4 by 2 cm
  at        115 cm along, 41 cm to the right, 62.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

left rail cap
  is a      box 120 by 4 by 2 cm
  at        115 cm along, 11 cm to the left, 62.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

right channel wall
  is a      box 120 by 2 by 16 cm
  at        115 cm along, 45 cm to the right, 54 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

left channel wall
  is a      box 120 by 2 by 16 cm
  at        115 cm along, 15 cm to the left, 54 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

latch
  is a      box 24 by 56 by 14 cm, 80 g
  moves     freely
  bounce    dead
  friction  0.015, spinning 0.0001, rolling 0.0001
  at        82 cm along, 15 cm to the right, 54 cm up
  colour    grey

latch end stop
  is a      box 4 by 60 by 18 cm
  at        177 cm along, 15 cm to the right, 54 cm up
  bounce    dead
  colour    grey

ring
  is a    ring 44 cm across, 1 cm thick
  at      82 cm along, 0 cm to the left, 30 cm up
  colour  orange

block
  is a      cube 10 cm, 200 g
  moves     freely
  bounce    dead
  friction  0.015, spinning 0.001, rolling 0.0001
  rests     on latch, 82 cm along, 0 cm to the left
  colour    wood

-- These guides keep the payload over the opening during withdrawal.
payload near guide
  is a      box 2 by 16 by 22 cm
  at        75 cm along, 0 cm to the left, 72.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

payload far guide
  is a      box 2 by 16 by 22 cm
  at        89 cm along, 0 cm to the left, 72.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

payload left guide
  is a      box 14 by 2 by 22 cm
  at        82 cm along, 7 cm to the left, 72.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

payload right guide
  is a      box 14 by 2 by 22 cm
  at        82 cm along, 7 cm to the right, 72.5 cm up
  friction  0.015, spinning 0.0001, rolling 0.0001
  colour    grey

box
  is an           open box
  length          56 cm
  width           56 cm
  walls           18 cm
  wall thickness  2 cm
  base thickness  2 cm
  on              floor, centred over ring
  bounce          dead
  friction        0.8, spinning 0.005, rolling 0.002
  colour          wood

expect
  ball1 touches ramp
  ball1 touches rotor
  rotor touches ball2
  ball2 touches latch
  block drops through ring
  block comes to rest in box
```

---
thinking (summarized):

**Evaluating latch mechanics**

I’m thinking about how the walls shouldn’t interfere with the latch sliding across certain points. If walls are positioned at z .565 to .9, they might prevent the latch from functioning correctly. I need to consider how guides stop just above the latch at .56 initially, which could lead to complications if the block is not supported properly. Without something to hold it up, there’s a risk of it falling laterally.

**Analyzing ball and rotor dynamics**

I'm working on some friction values here for a ball and rotor setup. Ball1 has ramp friction at .6, which seems compatible with rolling friction, and Platform friction at .3 is optional. Ball2 has a bit more friction with .4 for rolling. I’m thinking about rotor inertia and how it plays into this. The damping ratio is low, and I’m checking if latch rail guide caps could disrupt support during collisions. Let’s keep looking at these dimensions closely!

**Analyzing platform support dimensions**

I need to figure out the support requirements for the ball1 platform, which has specific dimensions with various extensions like x, y, and z. First, I’m noting the platform covers and gaps, particularly around x=.68 and y±.6 with a ring rim radius of .22. The current box length affects how it interacts with latches and contact points. I need to confirm the alignment at different angles and ensure everything fits as intended for proper functioning.

**Analyzing design constraints**

I’m thinking about how to optimize the guides and walls for the design, aiming for a balance that allows for negligible motion while maintaining a secure fit. The dimensions of the walls and clearances are crucial, with specific measurements leading to the right gaps. I need to ensure that the block doesn’t slip and that the various components fit together without issues. It’s a careful calibration of dimensions to get everything just right.

**Clarifying ramp design**

I'm working through some ramp design specifics now. It should be 1.30 m long, starting about 30 cm from the top, which places it 1 m up from its foot. The coordinates look fine, and I've calculated the length using some slope angles. The ramp's center shifts slightly due to normal forces, which I need to ensure is accurate. I'm also adding comments for clarity, like the height ambiguity. One thing I’m keeping in mind is the friction style to ensure it’s not too complicated.

**Finalizing design details**

I believe we have enough information for the final world layout, aiming for about 220 lines total. I could create rails named based on their positions, like "left lower," each consisting of around four lines, plus facts about friction, totaling roughly 200 lines. I must ensure the blocks have fixed count names supported with spaces and avoid extra caps. I also want to clarify the position settings, defining the ring before placing blocks to avoid duplication issues later. It's all about keeping things organized and clear!