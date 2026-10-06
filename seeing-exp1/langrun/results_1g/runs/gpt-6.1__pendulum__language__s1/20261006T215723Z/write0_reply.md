```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0002

ball
  is a      sphere 3 cm radius, 50 g
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 0 m along

pivot
  is a  point
  at    5.5 cm behind ball, 84 cm up

pendulum
  is a           sphere 3 cm radius, 200 g
  at             5.5 cm behind ball, 80 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  30°
  damping        0.005 N·m·s/rad
  bounce         dead
  friction       0.6, spinning 0.001, rolling 0.0002
  colour         grey

pendulum rod
  is a         rod 8 mm thick, from pivot to pendulum's top
  weighs       15 g
  attached to  pendulum
  colour       grey

cup
  is an            open box
  length           36 cm
  width            24 cm
  walls            14 cm
  wall thickness   5 mm
  base thickness   1 mm
  near wall height  1 mm
  sits             on floor, 1 m beyond ball
  friction         0.8, spinning 0.01, rolling 0.008
  bounce           dead
  colour           wood

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Considering cup design**

I'm thinking about a cup that captures something when hit with speed. It seems the cup's dimensions—0.3m in width and 0.12m in height—might provide enough retention. I wonder about using a pendulum that doesn't strike the ball too often and also keeps the floor clean. With a length of 0.8m for the pendulum and a bob radius of 0.03m, plus the bottom at 0.01m, that seems good.

**Calculating friction and motion**

I’m analyzing the rolling friction of a cup, with a value of .005 giving a deceleration of 1.167 and a stopping distance of about .13. Using a higher value of .008 improves the situation, leading to a better stop. The cup has a base friction of .8 and floor friction of .6. I’m realizing that the ball’s rolling friction is very low, which is good for the cup’s contact. There are interesting dynamics with the energy of the ball and its interaction with walls.

**Clarifying pendulum design**

I'm working on a pendulum design. I should place the pivot 80cm above the floor, with the pendulum bob located 5cm behind the ball. It sounds like I should label the hinge as the "pendulum hinge." The design should consist of a hinge body along with a rod that forms the pendulum, and I want to incorporate colors into it. I don't need any claims in this run. I'll make sure to keep everything concise in a single block.