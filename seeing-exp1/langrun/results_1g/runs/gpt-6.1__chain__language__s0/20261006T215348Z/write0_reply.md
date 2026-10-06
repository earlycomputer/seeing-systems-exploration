```world
world  three balls into a cup

floor
  size      6 m
  friction  0.6, spinning 0.0001, rolling 0.0001

ball1
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.0001, rolling 0.0001
  colour    black
  sits      on floor, 0 m along
  launched  4 m/s along
  spins     100 rad/s about y

ball2
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.0001, rolling 0.0001
  colour    white
  sits      on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.0001, rolling 0.0001
  colour    orange
  sits      on floor, 50 cm beyond ball2

ramp foot
  is a  point
  at    20 cm beyond ball3, 0 cm up

ramp lip
  is a  point
  at    45 cm beyond ramp foot, 9 cm up

ramp
  is a      plank from ramp foot to ramp lip, 24 cm wide, 1 cm thick
  friction  0.6, spinning 0.0001, rolling 0.0001
  bounce    dead
  colour    wood

cup
  is an             open box
  length            50 cm
  width             24 cm
  walls             18 cm
  wall thickness    1 cm
  base thickness    2 mm
  near wall height  8 cm
  friction          0.8, spinning 0.01, rolling 0.03
  bounce            dead
  colour            grey
  sits              on floor, 25 cm beyond ramp lip

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ramp
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Considering cup design mechanics**

I'm thinking about how to create a robust cup capture system with an inclined ramp that allows balls to roll into an upturned cup. The ramp's entry needs to be carefully designed, considering gravity effects and ball speed. I want the design to account for ball velocities, ensuring they reach at least 1.5 m/s. It’s also essential that the cup can properly trap the balls without letting them escape due to incorrect geometry.

**Evaluating cup and ball physics**

I'm considering the design of a cup with a base thickness of 2 mm and walls that are 15 cm tall, with a 3 cm lip. The ball needs to overcome this lip and, if the speed is too high, it might bounce over the walls. I’m setting the masses of the balls: b1 at 500 g, b2 at 200 g, and b3 at 100 g. I want to see if this creates a stable amplification chain when they interact.

**Analyzing ramp and ball dynamics**

I'm considering a setup where a low cup near the wall measures 7 cm. The base has a 2 mm length, with the cup measuring 22 cm long and 18 cm wide. The ramp inclines to 8 cm high at one end, situated near the wall. I need to think about whether a support leg at the high end will block the ball as it rolls. The balls are launched at 3 m/s, and I’m exploring the dynamics of their travel and collisions.

**Evaluating dimensions for a cup ramp**

I’m considering dimensions for a cup ramp. The cup point sits 25 cm beyond the ramp's lip, with a width of 24 cm and ball diameter of 8 cm. The ramp lip is 9 cm high, which means the far wall is 18 cm away. I can also think about a large 50 cm elongated tray. I’m calculating entry points and how the ball may interact with the ramp, checking height and friction factors. This needs to fit within the 42 width.