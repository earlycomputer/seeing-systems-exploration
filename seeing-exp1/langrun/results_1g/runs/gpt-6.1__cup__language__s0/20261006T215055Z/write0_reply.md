```world
world  ball rolls into a cup

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    0 m along, 70 cm up

ramp foot
  is a  point
  at    1.2 m along, 28 cm up

ramp
  is a      plank from ramp top to ramp foot, 26 cm wide, 4 cm thick
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    wood

cup
  is an             open box
  length            60 cm
  width             36 cm
  walls             24 cm
  near wall height  20 cm
  wall thickness    2 cm
  base thickness    2 cm
  friction          1.0, spinning 0.02, rolling 0.025
  bounce            dead
  colour            grey
  sits              on floor, 26 cm beyond ramp foot

ball
  is a      sphere 3 cm radius, 120 g
  rolls
  moves     freely
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    orange
  rests     on ramp, 12 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Evaluating equipment configuration**

I need to make sure that the strong friction cup settles properly, and I can use a rectangular cup without visual confusion. There shouldn't be any movement with the ball resting in place. I don’t need to launch it, so the ramp rail isn't necessary if I keep everything stable at y=0 without any disturbances. I also need to check if the floor can affect the ramp; a low foot might touch it, but it seems fine without needing any supports.