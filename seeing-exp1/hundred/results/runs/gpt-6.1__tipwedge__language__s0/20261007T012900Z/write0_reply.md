This uses a loose triangular rocker and an over-centre release flap. I haven’t simulation-tested it.

```parts
part rocking wedge
  base
    is a  box 12 by 30 by 4 cm, 200 g
    on    floor

  crest
    is a         box 48 by 30 by 2 cm, 200 g
    at           28 cm above base, centred over base
    attached to  base

  near tip
    is a  point
    at    24 cm behind base, level with crest

  far tip
    is a  point
    at    24 cm beyond base, level with crest

  near slope
    is a         plank from base to near tip, 30 cm wide, 2 cm thick
    weighs       50 g
    attached to  base

  far slope
    is a         plank from base to far tip, 30 cm wide, 2 cm thick
    weighs       50 g
    attached to  base
```

```world
world  falling weight tips wedge and releases ball

floor
  size      6 m
  friction  0.9, spinning 0.005, rolling 0.001

wedge
  is a      rocking wedge
  moves     freely
  friction  1.5, spinning 0.01, rolling 0.002
  bounce    dead
  colour    wood
  on        floor, 0 cm along

block
  is a      box 8 by 18 by 10 cm, 3 kg
  moves     freely
  friction  0.8
  bounce    dead
  colour    dark grey
  at        50 cm outside wedge.crest's top, 18 cm beyond wedge.base

starting pad
  is a      box 24 by 30 by 9 cm
  on        floor, 46 cm along
  friction  0.7, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    grey

ramp high end
  is a  point
  at    56 cm along, 8 cm up

ramp low end
  is a  point
  at    150 cm along, 2.5 cm up

ramp
  is a       ramp
  high end   ramp high end
  low end    ramp low end
  width      30 cm
  thickness  2 cm
  friction   0.7, spinning 0.005, rolling 0.0005
  bounce     dead
  colour     wood

ball1
  is a      sphere 6 cm radius, 1 kg
  moves     freely
  rolls
  friction  0.7, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    orange
  on        starting pad, 6 cm behind starting pad

flap pivot
  is a  point
  at    146 cm along, 20 cm up

flap
  is a           box 2 by 18 by 30 cm, 100 g
  at             149 cm along, 25 cm up
  turns on       release hinge, about y, at flap pivot
  swings         from -90° to 0°
  starts turned  0°
  damping        0.001 N·m·s/rad
  friction       0.7
  bounce         dead
  colour         wood

flap shelf
  is a         box 16 by 40 by 1 cm, 5 g
  at           140 cm along, 18 cm to the left, 32 cm up
  attached to  flap
  friction     0.7, spinning 0.005, rolling 0.001
  bounce       dead
  colour       wood

ball2
  is a      sphere 1.5 cm radius, 10 g
  moves     freely
  rolls
  friction  0.8, spinning 0.01, rolling 0.003
  bounce    dead
  colour    white
  on        flap shelf, 1 cm beyond flap shelf, 12 cm left of flap shelf

cup
  is an           open box
  length          80 cm
  width           24 cm
  walls           5 cm
  wall thickness  1 cm
  base thickness  1 cm
  on              floor, 123 cm along, 30 cm to the left
  friction        1, spinning 0.01, rolling 0.01
  bounce          dead
  colour          grey

expect
  block touches wedge
  wedge touches ball1
  ball1 touches ramp
  ball1 touches flap
  flap reaches its lower stop
  ball2 comes to rest in cup
```

---
thinking (summarized):

**Considering design and structure**

I need to think about a physically plausible design without using tools. It’s important to create a world that’s honest and solid in its structure. I’m considering geometries like a wedge made from angled planks. Maybe a new part could be a multi-plank wedge or a triangular sloping box supported by a fulcrum. It should allow for a tipping mechanism, allowing free assembly while avoiding pre-triggering gravity issues. I also need to manage the available tokens effectively.

**Exploring seesaw design**

I’m considering a seesaw-like "wedge" using a triangular assembly that features a sloping deck, a low floor strip, and a thick vertical end. The wedge needs to rest on a supporting fulcrum without hinges, as floor friction prevents unwanted movement. When a weight block hits one side, it lifts the opposite end, which could push ball1 up a ramp. The design aims for the wedge to tip freely and lever the weight, allowing for an effective ramp mechanism.

**Analyzing wedge and support design**

I’m thinking about how to effectively design the base support for the wedge. If it’s too small, it might create torque with left impact. The wedge should have a high rear end, and I need to ensure the center of mass is near the pivot for stability. An alternative idea is to tip the triangular wedge onto ball1, allowing the block to impact one side and push ball1 horizontally instead of just kicking it. I want the wedge to rotate forward while pushing ball1 down the ramp effectively.

**Clarifying measurements**

I need to determine dimensions carefully. When I say "50 cm above the wedge," I mean the center, not the surface. There's some ambiguity in placing "raised 50 cm" on the wedge, since it might create confusion about what fits properly. If I say "50 cm above the wedge's top," would that refer to the bottom? I think I could clarify by saying "50 cm outside the wedge's top" to make sure I’m measuring accurately from the surface known as wedge AABB.

**Clarifying library parts**

I'm trying to unravel the concept of library parts and how they function internally. So, if a part isn't attached, can it move freely? It seems like a document suggests that a part has its own properties. It doesn’t explicitly say if a freely moving part also has names. For standard parts, it appears they need attached internal components. I’m thinking about custom parts, particularly how to connect a body using attached elements on the deck. It's tricky, but I’ll figure it out!

**Calculating panel dimensions**

I'm trying to figure out the dimensions of a hinged tall panel box. Its thickness is .02, width is .30, and height is .25. For rotation, the pivot is located at the bottom, measuring .025. At the start, when it's fully upright, I’ll set some axis values: x=1.65 and z=.15. It seems straightforward, but I want to make sure I'm calculating everything accurately for whatever purpose it’s serving!

**Designing ball mechanisms**

I'm considering how Ball2 should be positioned near the bottom ledge before it's released by the upward-swinging flap. I need to make sure the cup beneath doesn't block the path of Ball1 as it falls through the lower area. For the design, Ball2 will rest on a shelf that's anchored to the flap, initially set at z 0.25 and x 1.75. The flap needs to maintain a vertical position at x 1.6, with hinge points at upper z 0.40 and lower 0.07, and the shelf will extend forward by 0.15.

**Analyzing ramp setup**

I'm considering a panel setup where it rotates from a negative angle to positive positions along the x and z axes. The shelf rises, potentially affecting ball2's movement. I could place ball2 on the upstream side of the shelf to use the shelf's rotation to direct it towards a cup. It’s essential to ensure the cup's position supports ball2 falling into it after rolling down the ramp. Also, I need to think about the shelf's stability and how it affects both balls.

**Exploring ball movement dynamics**

I'm considering ball2's initial position and how it interacts with the panel's hinge. There's a risk of missing the cup if it hits the panel at the wrong spot. When ball1 moves, it pushes the panel, causing it to tilt and release ball2 towards the cup. Gravity and the weight of the shelf affect the torque on the system. I need to ensure stability while managing the angles and any potential counterweights to keep everything balanced and functioning.

**Considering ballast effects**

I’m thinking about adding ballast on the downstream side to support ball2 before it strikes. I need to ensure the ballast is light enough so that ball1 can still flip. There’s a flap box thickness to consider, and I’m calculating the center of mass relative to the pivot point. The hinge position is at x1.65, which affects how I balance the masses of the different components against each other. It’s crucial to think this through to maintain stability!

**Considering contact points**

I’m thinking about the angle of the wedge's underside front slopes and how they might hit the ball earlier. The slope line transforms from base to crest—it sounds like there's a specific area near the crest that I should focus on. I’m estimating where the nearest contact circle might be located, especially around the values I calculated, like x and z coordinates. There’s definitely some geometry at play that I need to clarify!

**Considering ramp and ball setup**

I’m working through whether a global variable is necessary for a local configuration with specific measurements. The crest shape seems to be an inverted triangle that I can call a "triangular rocking wedge." I’m pondering the order of components: should I place the wedge, block, start pad, and ramp before the ball? It seems like setting the ball 12 cm left of the flap shelf and calculating torque values will create a stable setup. I want to ensure everything has a clear and organized integration!

**Planning ball and cup setup**

I'm organizing the positioning of ball two at a height of 0.3 and ensuring the shelf runs from 1.49 to 1.67 in the x-axis. The center of ball two will be at 1.59, which is close to my initial contact point underneath the shelf. I’m placing the cup near the wall, checking its dimensions, with a height of 8 cm and ensuring everything is cleared properly. After motion, I might adjust the ball's center to around 1.6. I want to ensure this setup works well!

**Evaluating expectations for simulation**

I need to understand how the expectation system works. It seems that when ball 1 touches the flap, ball 2 should touch the cup, and then the flap reaches its lower stop. There’s something about the block touching the wedge, and it seems the wedge also touches ball 1. It’s crucial to ensure that "wedge touches ball 1" is supported and correct, but I'm uncertain about some of the parts. Let's clear this up!