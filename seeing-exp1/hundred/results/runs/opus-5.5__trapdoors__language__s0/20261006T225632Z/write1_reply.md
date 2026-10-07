The chain runs toward −x. Ball1 falls through hoop1 onto flap1 about 30 cm from its hinge. That knocks flap1 down to its −45° stop, which drops the block about 0.9 m onto flap2's free end. Flap2 then snaps down to its −45° stop, and ball2, which sits near flap2's hinge, drops straight through hoop2 into the cup.

Both flaps are held closed by a preloaded spring against their 0° stop. This is checked as static torque balances, not by running it. Ball1 rolls off flap1 along y = 0, well clear of flap2, hoop2 and the cup, which all sit at y = 0.45 m.

Things I couldn't settle from the spec:
- **Ball1 reaching flap1's stop.** Ball1's resting weight alone would not quite hold flap1 at −45° against the spring. It depends on the impact's momentum, which I estimate is ample.
- **Part placement.** I wasn't sure parts can be placed by a piece. The hoops use `its rim at <point>` and the cup uses absolute offsets.
- **Hoop2's backboard.** It sits just below hoop1's backboard. They are both fixed, so it only looks crowded.

```world
world  two trapdoor relay

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

hoop1 spot
  is a  point
  at    0 cm along, 0 cm to the left, 245 cm up

hoop1
  is a        hoop
  rim height  245 cm
  its rim at hoop1 spot

ball1
  is a      sphere 6 cm radius, 1 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  at        0 cm along, 0 cm to the left, 80 cm above hoop1 spot

flap1 pivot
  is a  point
  at    30 cm along, 20 cm to the left, 194 cm up

flap1
  is a      box 80 by 70 by 2 cm, 150 g
  colour    wood
  friction  0.5
  its far end at flap1 pivot, level with flap1 pivot, 20 cm to the left
  turns on  flap1 hinge, about y, at flap1 pivot
  swings    from -45° to 0°
  spring    0.4 N·m/rad toward 330°
  damping   0.02 N·m·s/rad

block
  is a      cube 8 cm, 200 g
  colour    grey
  friction  0.5
  moves     freely
  on flap1, 72 cm behind flap1 pivot, 45 cm to the left

hoop2 spot
  is a  point
  at    13 cm along, 45 cm to the left, 45 cm up

hoop2
  is a        hoop
  rim height  45 cm
  its rim at hoop2 spot

flap2 pivot
  is a  point
  at    28 cm along, 45 cm to the left, 104 cm up

flap2
  is a      box 80 by 20 by 2 cm, 150 g
  colour    wood
  friction  0.5
  its far end at flap2 pivot, level with flap2 pivot, 45 cm to the left
  turns on  flap2 hinge, about y, at flap2 pivot
  swings    from -45° to 0°
  spring    0.18 N·m/rad toward 330°
  damping   0.02 N·m·s/rad

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    white
  moves     freely
  on flap2, 15 cm behind flap2 pivot, 45 cm to the left

cup
  is a      open box
  length    30 cm
  width     30 cm
  walls     12 cm
  colour    wood
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  on floor, 13 cm along, 45 cm to the left

expect
  ball1 drops through hoop1
  ball1 touches flap1
  flap1 reaches its lower stop
  block touches flap2
  flap2 reaches its lower stop
  ball2 drops through hoop2
  ball2 comes to rest in cup
```

---
thinking (summarized):

I'm finalizing the remaining world details: placing hoop1 at 245 cm height with its rim positioned there, and setting up ball1 as a 6 cm radius sphere, 1 kg, rolling with dead bounce, positioned 80 cm above hoop1.

I'm defining the cup as an open wood box, 30 cm by 30 cm with 12 cm walls, placed on the floor at specific offsets. I'm also working out the pivot points for flap1 and flap2, and confirming the object order: floor, hoop1, ball1, flap1 pivot and flap1, block, hoop2, flap2 pivot and flap2, ball2, cup -- making sure ball2 sits correctly on flap2 and the block on flap1, and settling on using a plain hyphen for negative angles like -45°.

