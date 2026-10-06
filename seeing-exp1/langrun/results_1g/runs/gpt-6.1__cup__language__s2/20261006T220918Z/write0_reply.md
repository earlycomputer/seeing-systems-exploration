```world
world  ball rolls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp start
  is a  point
  at    0 m along, 60 cm up

ramp end
  is a  point
  at    1.25 m along, 18 cm up

ramp
  is a      plank from ramp start to ramp end, 24 cm wide, 2 cm thick
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    wood

cup
  is an             open box
  length            70 cm
  width             40 cm
  walls             30 cm
  near wall height  10 cm
  wall thickness    2 cm
  base thickness    2 cm
  friction          0.9, spinning 0.02, rolling 0.02
  bounce            dead
  colour            grey
  on                floor, 1.5 m along

ball
  is a      sphere 3.5 cm radius, 100 g
  rolls
  moves     freely
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    orange
  on        ramp, 15 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Designing a gravity ramp for cup catch**

I need to create a gravity ramp and cup catch without any tools, making sure the design is clear in language. The ramp can be a simple plank with high-low points, leading into an open box cup at the floor level. It's important to ensure that the ball rolls down the ramp with low friction while also damping properly in the cup. I need to get the dimensions right for the ramp and the cup to catch the ball effectively.

**Calculating ramp and cup dimensions**

I’m working with a ball that has a radius of 0.04 and a mass of 0.08. The ramp is high at coordinates (-1, 0.65) and low at (0.3, 0.2). The cup is centered at (0.65, length 0.9), with near and far edges at 0.2 and 1.1, respectively. I want to ensure the sphere stays on the ramp and lands in the cup with the right friction and height specifications. I also need to explore placement options for ramp supports.

**Defining ramp and cup specifications**

I'm considering ramp dimensions. The ramp is defined with a high end and a low end, measuring 24 cm in width and 2 cm in thickness. The ball will sit 15 cm from the top of the ramp, which gives me a good angle for a safe descent. I think a custom open box cup is acceptable, though a circular cup could be an option. The ramp's slope should be moderate, ensuring the ball speeds down correctly to land safely inside the cup without any overlap with the wall.

**Calculating ball dynamics**

I'm looking at a ball with a 3.5 cm radius and a weight of 100 g. It seems like it bounces dead. The ramp has a friction of 0.8 while the ball also has the same friction values for spinning and rolling. The default max friction for the cup is important too. It's something like 70 by 40 by 30 in dimensions, which is big but should work well as a catch cup.

**Clarifying simulation design**

I'm working on the simulation parameters: the time ramp is about 1.1 seconds, and I expect the ball to touch the ramp and settle in the cup. I’m considering the friction and physical components, like the ramp's collision with the cup. The cup has a high friction coefficient and the ramp is designed without visible supports. I'm planning to use specific identifiers for the ramp points and keeping the cup grey, ramp wood, and the ball orange.