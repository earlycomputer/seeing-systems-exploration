```world
world  falling weight seesaw

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

left bearing
  is a      box 8 by 8 by 80 cm
  stands    on floor, 18 cm to the left
  colour    grey

right bearing
  is a      box 8 by 8 by 80 cm
  stands    on floor, 18 cm to the right
  colour    grey

axle
  is a      rod 2 cm thick, from left bearing's top to right bearing's top
  touches nothing
  colour    grey

pivot
  is a      point
  at        80 cm up

seesaw
  is a           box 120 by 18 by 2 cm, 400 g
  at             80 cm up
  turns on       seesaw hinge, about y, at pivot
  swings         from 0° to 35°
  starts turned  0°
  damping        0.002 N·m·s/rad
  armature       0.0001 kg·m²
  friction       0.6, spinning 0.005, rolling 0.002
  bounce         dead
  colour         wood

ball
  is a      sphere 4 cm radius, 100 g
  moves     freely
  rolls
  rests     on seesaw, 52 cm behind seesaw
  friction  0.6, spinning 0.005, rolling 0.002
  bounce    dead
  colour    orange

weight
  is a      sphere 7 cm radius, 1 kg
  moves     freely
  rolls
  at        52 cm beyond seesaw, 3 m up
  friction  0.6, spinning 0.005, rolling 0.002
  bounce    dead
  colour    dark grey

expect
  weight touches seesaw
  ball touches seesaw
```

---
thinking (summarized):

**Considering support design**

I'm trying to make sense of the floor support design. It seems like I need to ensure the pivot point is at 0.8 height without colliding with the beams. I want to choose support posts while keeping them outside the beam width. It looks simpler to have a pivot point with a seesaw box that’s aligned at the center. My focus is on ensuring there are no collisions, so a single stand with just one hinge may be the best choice!

**Exploring support design**

I'm considering if I can use a fixed cylinder for support instead of a simple rod. The seesaw pivot needs to be centered to avoid intersecting the wood, ensuring it touches nothing at the natural axle. Using two bearing posts of 8x8x80 cm sounds practical, with the axle rod situated between the top points at 0.8. I’ll need clear references for positioning the rods from the left bearing's top to the right. The measurements and gaps look good at a width of 0.18 for clearance!

**Refining seesaw design**

I’m working on the seesaw design, which will be a box measuring 120 by 18 by 2 cm, weighing 120g. The hinge will allow it to turn about the pivot around the y-axis. I want to ensure that the seesaw is safely centered over the pivot at the reference level. I need to clarify the pivot's position, making sure it’s properly defined and that the rods and elements are clearly positioned at 80 cm up. I aim for precision in specifying these details!

**Calculating effective mass**

I'm considering using 500g with a .06 / r² = .22 effective, which gives me a 4.88 rise and 1.21; that seems enough. There's also a beam mass of 300g that provides an effectiveness of .133 plus .1, leading to .233, which totals to 5.23. I need to ensure all calculations align, so I'll double-check these figures to see if they support the overall outcome I want to achieve.