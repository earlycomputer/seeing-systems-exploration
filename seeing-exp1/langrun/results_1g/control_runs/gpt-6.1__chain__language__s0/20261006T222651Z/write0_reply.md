```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.7, spinning 0.001, rolling 0.0001

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.7, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  1.2 m/s along
  spins     30 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.7, spinning 0.001, rolling 0.0001
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.7, spinning 0.001, rolling 0.0001
  colour    grey
  moves     freely
  rests     on floor, 30 cm beyond ball2

-- A low entry lip lets the ball roll into the receiving cup.
cup
  is an             open box
  length            44 cm
  width             20 cm
  walls             12 cm
  wall thickness    1 cm
  base thickness    1 mm
  near wall height  1 mm
  friction          0.8, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  sits              on floor, 39 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Evaluating rolling ball experiment**

I need to craft a credible design for the balls rolling into a cup setup, but I don't have any tools available to simulate it. First, I need to consider the dimensions, friction, and how the balls will bounce and transfer motion to the cup. I should optimize the setup with identical balls and manage their spacing and velocity as they enter the cup. Determining the right dimensions for the ball spacing and height of the walls is also crucial for proper functionality.

**Analyzing ball dynamics**

I need a springy impulse around 0.8 m/s for the first ball, which then leads ball two at 0.9 m/s without spin. On the floor, it accelerates, but the velocity falls to 0.64 m/s. Meanwhile, ball one keeps its original spin and ends up at 0.36 m/s, while ball two stabilizes around 0.4 m/s due to friction. There are calculations to consider for the cup’s dimensions and the energy dynamics as the balls approach the cup, aiming for proper containment.

**Examining cup and ball dynamics**

I'm assessing the friction at the cup, which is 0.02, to see how it affects the balls. When the first ball rolls, I find that max rolling friction is 0.002 compared to the cup's 0.008. With my calculations, this leads to a braking acceleration that means the ball decelerates quickly. I might need to adjust the rolling friction values for both the floor and the balls so they can better reach the cup without stopping too soon.

**Designing a cup for ball entry**

I'm thinking about a custom cup with high entry walls so the third ball rolls over and drops into it, but also having a separate low platform ramp. It seems like designing an upright cup with a small entry notch near the wall height will work. I want to ensure that the ball can roll in smoothly without stopping prematurely. I also need to avoid secondary collisions that could disrupt the chain of balls descending into the cup.