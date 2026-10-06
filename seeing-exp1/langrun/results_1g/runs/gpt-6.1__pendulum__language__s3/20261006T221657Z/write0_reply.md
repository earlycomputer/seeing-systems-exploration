```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.65, spinning 0.003, rolling 0.0003

ball
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    dead
  friction  0.65, spinning 0.003, rolling 0.0003
  colour    orange
  rests     on floor, 7.5 cm along

pivot
  is a  point
  at    64.1 cm up, 7.5 cm behind ball

pendulum
  is a           sphere 4 cm radius, 200 g
  at             60 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  swings         from -12° to 35°
  starts turned  30°
  damping        0.005 N·m·s/rad
  bounce         dead
  friction       0.5, spinning 0.001, rolling 0.0001
  colour         grey

pendulum rod
  is a         rod 8 mm thick, from pivot to pendulum's top
  weighs       20 g
  attached to  pendulum
  colour       grey

cup
  is an            open box
  length           24 cm
  width            22 cm
  walls            14 cm
  wall thickness   3 mm
  base thickness   1 mm
  near wall height  1 mm
  friction         0.9, spinning 0.01, rolling 0.004
  bounce           dead
  colour           white
  sits             on floor, 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Calculating cup and ball dimensions**

I'm working with measurements for a cup: it has a length of 24, width of 20, wall thickness of 3mm, and a height of 12. The base is 1mm thick. The cup is positioned 1m ahead of a ball on the floor, with the walls being 2mm tall. I’m figuring out how the ball travels by calculating its contact point with the cup's base lip. I want to ensure these details align properly!

**Examining cup and ball design**

I’m thinking about how the ball touches the cup, and maybe there’s some redundancy with the ball rest covers. Two should be sufficient. I want to consider the geometry of the cup's base that’s placed on the floor, which brings the minimum global Z to 0 for both the base and walls. 

I also need to factor in that rolling friction applies to all. The cup is near the wall, 1mm thick and 3mm lower than the ball.