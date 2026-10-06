```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0002

ball
  is a      sphere 3 cm radius, 80 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0002
  colour    orange
  rests     on floor, 0 m along

pivot
  is a  point
  at    63 cm up, 5.5 cm behind ball

pendulum
  is a           sphere 2.5 cm radius, 300 g
  at             60 cm below pivot, 5.5 cm behind ball
  turns on       pendulum hinge, about y, at pivot
  swings         from -45° to 45°
  starts turned  35°
  damping        0.003 N·m·s/rad
  bounce         dead
  colour         grey

pendulum rod
  is a         rod 5 mm thick, from pivot to pendulum's top
  weighs       10 g
  attached to  pendulum
  colour       wood

cup
  is an             open box
  length            30 cm
  width             24 cm
  walls             10 cm
  wall thickness    1 cm
  base thickness    2 mm
  near wall height  2 mm
  friction          0.9, spinning 0.01, rolling 0.003
  bounce            dead
  colour            grey
  sits              on floor, 1 m beyond ball

entry foot
  is a  point
  at    22 cm behind cup, 0 m up

entry top
  is a  point
  at    13.5 cm behind cup, 2 mm up

entry ramp
  is a      plank from entry foot to entry top, 14 cm wide, 1 mm thick
  friction  0.6, spinning 0.001, rolling 0.0002
  bounce    dead
  colour    grey

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Analyzing pendulum dynamics**

I'm examining a pendulum with a start angle of 25 degrees, a length of 6, and a drop of .0562. Its speed is calculated at 1.05 m/s, with a mass of .3 for the ball and .08 for the rod. I'll check the effectiveness of an inelastic collision where the ball reaches .82 m/s, then slows down through friction. The entry point needs to yield sufficient velocity, estimating around .75-1.4 m/s for the cup placement and considering ramp adjustments for stability.

**Adjusting pivot position**

I’m trying to figure out the pivot positioning: it starts at .63 up and .055 behind the ball. The pendulum should be a sphere with a radius of 2.5 cm, weighing .3 kg, and hanging 60 cm below the pivot. I realize that positioning it "60 cm below pivot" will only fix the z-axis. To address the x and y positions, I need it to be “centered over pivot.” I'll refine my calculations.

**Defining a cup design**

I'm considering the design of a cup with sidewalls about 8 cm high and a low lip entry to allow easy ground rolling. It could be defined as an open box, except for the wall, which would be 2 mm high near the entry. The design requires specifications like a length of 30 cm and a wall height of 2 mm. I expect that when a ball rolls in, it will touch the pendulum and come to rest inside the cup.