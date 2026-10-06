```world
world  ball rolls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp start
  is a  point
  at    0 m along, 65 cm up

ramp end
  is a  point
  at    1.8 m along, 22 cm up

ramp
  is a      plank from ramp start to ramp end, 40 cm wide, 4 cm thick
  friction  0.8, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    wood

cup
  is an             open box
  length            1 m
  width             60 cm
  walls             50 cm
  near wall height  12 cm
  wall thickness    2 cm
  base thickness    2 cm
  sits              on floor, 35 cm beyond ramp end
  friction          1, spinning 0.02, rolling 0.02
  bounce            dead
  colour            grey

ball
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  rests     on ramp, 15 cm from the top
  friction  0.8, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    orange

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Analyzing ball dynamics**

I'm considering how a ball behaves in a system with walls and ramps. There’s a chance it can escape the near wall if it has enough velocity, while energy loss affects how far it travels. I’m designing a ramp to ensure smooth operation in this setup, paying attention to dimensions and angles to optimize rolling resistance. I need to evaluate how friction will factor in and adjust the ramp height to prevent stalling. Overall, it's important to balance elements for efficient movement.

**Calculating sphere dynamics**

I’m looking at a sphere with a radius of 0.04 that starts on a ramp 12 cm from the top, dropping about 0.35 to 0.4. The slope seems to be around 0.24, which looks fine. I also note that the cup has a rolling distance of 0.02, and if the initial exit speed is 2 m/s, it should stop in about 0.6 seconds. This setup appears to be working well!