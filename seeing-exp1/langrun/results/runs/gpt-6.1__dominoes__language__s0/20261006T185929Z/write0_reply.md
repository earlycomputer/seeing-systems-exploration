```world
world  ten falling dominoes

floor
  size      4 m
  friction  0.9, spinning 0.001, rolling 0.0001

domino
  is a             box 2 by 6 by 20 cm, 150 g
  colour           wood
  friction         0.9, spinning 0.001, rolling 0.0001
  bounce           dead
  moves            freely
  stands           on floor
  repeated         10 times, 7 cm apart along
  first one spins  8 rad/s about y
```

---
thinking (summarized):

**Calculating friction and torque**

I’m analyzing the forces affecting an object on a surface. I’m considering the different types of friction: spinning and rolling, along with their potential effects on torque and motion. There’s a lot of detail here about calculating rolling resistance and the conditions under which the object behaves. I seem to be balancing torque calculations against gravitational impacts and friction coefficients, but it looks like I need to establish some defaults for variables. Let's narrow down those values.