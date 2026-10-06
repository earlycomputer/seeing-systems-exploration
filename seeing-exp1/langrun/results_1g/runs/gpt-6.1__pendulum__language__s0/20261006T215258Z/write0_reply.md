```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0001

ball
  is a      sphere 4 cm radius, 50 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    orange
  rests     on floor, 0 m along

pivot
  is a  point
  at    55 cm up, 8 cm behind ball

pendulum
  is a           sphere 4.5 cm radius, 300 g
  centred over pivot, 50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  swings         from 0° to 30°
  starts turned  30°
  damping        0.01 N·m·s/rad
  bounce         dead
  colour         grey

pendulum rod
  is a         rod 8 mm thick, from pivot to pendulum's top
  weighs       10 g
  attached to  pendulum
  colour       grey

-- A low entrance lip lets the ball roll into the cup.
-- The other three walls retain it, and the base slows its rolling.
cup
  is an            open box
  length           24 cm
  width            22 cm
  walls            12 cm
  wall thickness   6 mm
  base thickness   1 mm
  near wall height  1 mm
  friction         0.9, spinning 0.01, rolling 0.01
  bounce           dead
  colour           white
  on               floor, 1 m beyond ball

expect
  pendulum touches ball
  ball comes to rest in cup
```

---
thinking (summarized):

**Calculating performance metrics**

I’m thinking about the requirements for speed and rolling coefficients. I need a faster rate of about 1 m/s and a rolling coefficient of 0.0004 with a deceleration of 0.098. I want to reach that speed of around 0.8 and achieve a bounce that will settle into a cup effectively. It’s important to optimize these factors to ensure good performance. Let's explore how these metrics can work together!

**Analyzing ball dynamics in a cup**

I'm figuring out the dimensions for a cup, including its length and width, and checking the thickness of the walls and base. The ball has to fit within certain bounds to roll properly. I'm considering friction levels and how they influence the ball's movement and deceleration. I’m assessing how the design, including the raised base and wall heights, affects how the ball behaves when rolling and bouncing inside the cup.

**Evaluating pendulum dynamics**

I'm analyzing a pendulum setup with a custom bob and various measurements, including the mass and length. The ball's movement and impact before reaching the bottom are crucial. I need to calculate velocity and how the overall mechanics affect the ball's launch, estimating its speed to be around 1 m/s. For a non-elastic collision, I’m considering the friction and how it impacts the motion of both the sphere and the pendulum, especially how energy transfers during contact.

**Analyzing pendulum mechanics**

I'm working with a standard reference for a pendulum setup, at 50 cm below the pivot. The rod connects to the pendulum's top, with certain measurements for length and radius. I'm considering the physics, like the effects of gravity, mass, and the energy loss during swings. The system has an expected collision model and spring damper dynamics, leading to something approximating restitution. I'm curious how all of these aspects interrelate in motion!

**Considering physics expectations**

I'm thinking about expectations in physics: specifically, when a pendulum touches a ball and how that ball comes to rest in a cup. I wonder if the expectation supports arbitrary touches, like if the ball were to touch a ramp instead. It feels intriguing to consider how different interactions could affect outcomes. There seems to be a lot of interesting dynamics at play, especially in understanding the behavior of objects in motion.

**Analyzing pendulum setup**

I’m considering a pendulum that starts on the floor at 0m and pivots 55cm up, positioned 8cm behind the ball. The pendulum is 50cm below the pivot and centered over it. This setup follows the same pattern as the example. 

I should factor in damping at 0.01 N·m·s/rad, which could cause a slight loss in energy. The ball rolls freely without any launch, needing to bounce on the floor without friction. I’ll focus on keeping everything complete.