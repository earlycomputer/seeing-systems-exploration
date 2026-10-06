```world
world  ball rolls into a cup

floor
  size      5 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp start
  is a  point
  at    50 cm up, 0 m along, 0 m to the left

ramp finish
  is a  point
  at    18 cm up, 1.2 m beyond ramp start, 0 m to the left

ramp
  is a      plank from ramp start to ramp finish, 30 cm wide, 3 cm thick
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    wood

cup
  is an             open box
  length            60 cm
  width             45 cm
  walls             30 cm
  wall thickness    2 cm
  base thickness    2 cm
  near wall height  8 cm
  on                floor, 28 cm beyond ramp finish, 0 m to the left

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  moves     freely
  friction  0.8, spinning 0.01, rolling 0.002
  bounce    dead
  colour    white
  rests     on ramp, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Evaluating MuJoCo Collisions**

I'm considering how collisions work in MuJoCo, particularly with a ball rolling towards a wall while spinning. If it hits the wall, friction can create some upward spin resulting in a small rebound, but the restitution is dead, meaning it won’t bounce back significantly. Once the ball comes to rest against the wall, the spin could reverse slightly due to friction, but it would exhaust within a second. I noticed I just need to remove three unsupported lines and there's no need for any color changes for the cup.