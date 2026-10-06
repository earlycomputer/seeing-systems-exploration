```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0005

ball
  is a      sphere 3 cm radius, 80 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0005
  rests     on floor, 0 m along
  colour    orange

pivot
  is a  point
  at    6 cm behind ball, 63 cm up

pendulum
  is a           sphere 3 cm radius, 250 g
  at             6 cm behind ball, 60 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  swings         from −70° to 70°
  starts turned  35°
  damping        0.005 N·m·s/rad
  bounce         dead
  colour         grey

pendulum rod
  is a         rod 8 mm thick, from pivot to pendulum's top
  weighs       20 g
  attached to  pendulum
  colour       grey

cup
  is an             open box
  length            24 cm
  width             20 cm
  walls             9 cm
  wall thickness    5 mm
  base thickness    2 mm
  near wall height  2 mm
  friction          0.8, spinning 0.005, rolling 0.002
  bounce            dead
  sits              on floor, 1 m beyond ball
  colour            white

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Designing a pendulum setup**

I’m thinking about creating a credible physics setup without tools. I need to design a pendulum hinge while avoiding odd library stands. The ball should rest at a radius of 0.04, and the pivot should be behind it at 0.08. The cup's design might need to be open and low to allow the ball to roll into it. I should ensure minimal re-hitting and consider the friction coefficients for accurate calculations. It's all about fine-tuning parameters for optimal performance!

**Analyzing pendulum mechanics**

I’m calculating a pendulum's performance where it reaches a speed of 1.33 from a 30-degree angle with a length of 0.7 and a bob mass of 0.18. The ball's mass is 0.08, and it seems I need to address inelastic impacts. For energy delivery, I’m targeting a rolling speed of 0.9 to stop in about 1 meter, needing a deceleration of around 0.07. The cup dimensions are important here, with an initial nominal touch point set. Adjusting positions will ensure everything aligns well!

**Understanding contact mechanics**

I’m trying to figure out when contact happens in my pendulum setup. It seems that it occurs before reaching zero, with the equation for the bob’s position being x_bob = -0.06 - 0.6 sin(theta). So, as theta increases, the vertical height also grows. When theta is zero, it’s at the tangent point, but the contact occurs slightly negative after that before pushing the ball to the right. Keeping the hinge axis on the y-axis is important here!