```world
world  ball rolls down a ramp into a cup

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp high end
  is a  point
  at    0 cm along, 45 cm up

ramp low end
  is a  point
  at    1 m along, 12 cm up

ramp
  is a      plank from ramp high end to ramp low end, 30 cm wide, 2 cm thick
  friction  0.8, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    wood

cup
  is an             open box
  length            70 cm
  width             40 cm
  walls             25 cm
  near wall height  4 cm
  wall thickness    2 cm
  base thickness    2 cm
  friction          1.0, spinning 0.01, rolling 0.015
  bounce            dead
  colour            grey
  on                floor, 1.30 m along

ball
  is a      sphere 3.5 cm radius, 120 g
  rolls
  moves     freely
  friction  0.8, spinning 0.005, rolling 0.0005
  bounce    dead
  colour    orange
  on        ramp, 12 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Designing a ramp simulation**

I need to create a physically robust ramp into the cup within 6 seconds without any tools. I'll design units for the geometry using a ramp primitive plank that directly touches the geometry. The ramp will have a height of 45 cm and a low point of 13 cm over 1.2 m. The cup is designed as an open box near the wall, allowing the ball, which has a radius of 3 cm, to enter easily. The ball will roll down with a speed of around 2 m/s and drop approximately 0.16 m.

**Designing ramp dimensions**

I'm thinking about creating a modest ramp with a height of 0.30 m, a low point of 0.12 m, and a length of 0.90 m, while using a ball with a radius of 0.03 m that starts 8 cm from the top at a speed of about 1.5 m/s. The cup's dimensions near the wall need to be low enough at 0.04 m to avoid obstruction. The ramp endpoint will be positioned at 0.90 m height and will influence the ball's flight and landing calculations. I'll also consider friction effects for the ball after landing.

**Adjusting ball friction**

I need to ensure that the friction for the ball while rolling on the ramp is really low, ideally less than or equal to 0.001. This low friction will allow the ball to roll smoothly without significant resistance, which is important for accurate movement and behavior in the simulation. I'll focus on this aspect to get the desired performance on the ramp.