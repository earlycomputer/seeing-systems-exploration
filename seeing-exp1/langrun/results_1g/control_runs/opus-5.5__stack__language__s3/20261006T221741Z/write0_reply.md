A heavy ball rolls along the floor and strikes the bottom block of a five-cube stack. The stack stands still for about half a second until the ball arrives and knocks `block1` out. The four blocks above lose their support and tumble down.

```world
world  stack of five toppled from the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 300 g
  friction  0.6, spinning 0.005
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

ball
  is a      sphere 5 cm radius, 1 kg
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 1.5 m behind block1, level with block1
  launched  4 m/s along

expect
  ball touches block1
```

---
thinking (summarized):

I'm picturing a stack of five 10 cm cube blocks, 50 cm tall, sitting a meter along the floor, with a ball launched at the bottom block to knock it out so the stack above topples.

I'm working out collision physics: a 1 kg ball at 3 m/s striking a ~300 g wooden block transfers enough speed to send it flying while the blocks above drop and tilt. I'm checking positions so the ball (5 cm radius) starts 50 cm from the block and its surface lines up correctly with the block's center height at impact.

I widen the gap to around 1.5 m so the stack stays stable for about half a second before impact, accounting for rolling friction converting slide to roll (losing speed from 5/7 of initial, so starting faster at 4 m/s nets roughly 2.9 m/s on arrival). I'm also setting floor friction to 0.8 and block friction to 0.6, and confirming the stacked cubes rest stably under MuJoCo's default settings.

