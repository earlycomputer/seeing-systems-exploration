A heavy ball rolls along the floor and strikes the bottom block of a tall, thin stack about 0.8 s into the run. Each block is thin in the direction of the push, so when the bottom block is shoved forward the column leans back and topples.

```world
world  stack toppled by a push at the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 16 by 12 cm, 400 g
  colour    wood
  friction  0.7
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

pusher
  is a      sphere 5 cm radius, 2 kg
  colour    grey
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     on floor, 20 cm along
  launched  1.5 m/s along

expect
  pusher touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm picturing five stacked blocks that stand still until a ball or pendulum rolls in after about a second and knocks the bottom one out, toppling the stack. I'm sizing the blocks around 10cm cubes, roughly 200g each, stacked to about 50cm tall, and thinking through how the impact should be delayed and aimed at the base.

I'm checking whether a 1kg ball launched slowly from a meter or two away gives enough momentum to knock the lighter bottom block clear so the rest collapse, accounting for rolling friction slowing it slightly before impact.

Floor friction on block1 decelerates it quickly while the upper blocks lag behind, which should make the stack topple rather than just collapse straight down. I'm thinking a tall, slender box shape — like 8 by 16 by 12 cm — would topple more easily than a cube, so I'll make the stack out of thin boxes around 60 cm tall with an aspect ratio near 7.5. I'll position the ball at the right height to strike the bottom block near its center and place the stack about a meter along the floor.

I need to figure out how to position the ball relative to the stack using absolute coordinates — something like placing the block at 1.5 m along and the ball at 20 cm along, with a modest launch velocity of 1.5 m/s so it reaches the stack in under a second while decelerating along the way.

