```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0001

ball1
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  sits      on floor, 0 m along
  launched  1.2 m/s along
  spins     24 rad/s about y

ball2
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    white
  moves     freely
  sits      on floor, 30 cm beyond ball1

ball3
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    grey
  moves     freely
  sits      on floor, 30 cm beyond ball2

cup
  is an             open box
  length            50 cm
  width             24 cm
  walls             14 cm
  wall thickness    1 cm
  base thickness    1 mm
  near wall height  1 mm
  friction          1.0, spinning 0.01, rolling 0.004
  bounce            dead
  colour            wood
  sits              on floor, 45 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Designing a simulation scenario**

I need to create a physical scene without using tools, focusing on a simulation without making any claims. The setup requires a cup on the floor that's low enough to allow balls to roll over its lip. I want to use three equal spheres in a row. When the first ball rolls, it should collide with the second and then the third, which eventually rolls into the cup. All the balls should start still except for the first one. I’m considering factors like speed, friction, and mass for realistic collisions.

**Setting up a physics scenario**

I’m choosing parameters like a radius of 4 cm and a mass of 100 g, with specific friction coefficients for the floor and the balls to allow for rolling and traversal. Ball 1 starts with a velocity of 0.9 m/s and a certain spin. There are specific gaps between the balls, leading to a cup that’s positioned strategically. I need to ensure that the balls bounce and exchange energy properly, allowing for realistic behavior after collisions, including retained spin and gradual slowing of speed.

**Calculating ball dynamics**

Starting with ball positions, I see ball 1 at 0.26 and ball 2 at 0.64, then analyzing elastic interactions where ball 2 ends at 0.18 and ball 3 at 0.46, leading to a cup entry velocity around 0.4. I need to consider the floor's rolling friction and its impact on deceleration. The rolling resistance coefficient might affect the last cup speed, which should be around 0.3. I also need to design entry lips carefully to ensure the balls can roll over effectively.

**Analyzing ball dynamics**

I'm looking at entry speed of .35 and stop at .175. The cup size is .5, centered at ball3, which is +.45 at the near edge. Starting cup contact center is .76 versus ball3 at .6, giving a delta of .16—seems good. The floor's rolling coefficient choice, considering a geometric pair maximum, indicates that the ball remains lively, so energetic bounce shouldn't be a problem. I need to ensure accuracy in the MuJoCo mapping for "lively," aiming for a restitution around .8 or .9.

**Examining library cup design**

I'm considering a library without cups, so there's a need for an open box that is a valid low-entry cup. It feels like a visual challenge, thinking about a rectangular vessel that’s obvious in its purpose. I'm curious what that would look like and how it would function in a library setting. It’s interesting to think about the design elements that would make this work effectively!