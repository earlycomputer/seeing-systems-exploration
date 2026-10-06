The position can't name `block1`, so the ball is now placed on the floor at an absolute spot, 1.5 m behind the stack on the same line. I also dropped `level with block1`: `on floor` already fixes the height, and it puts the ball's centre at 5 cm, the middle of the bottom block.

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
  rests     on floor, 0 m along
  launched  4 m/s along

expect
  ball touches block1
```

---
thinking (summarized):

I can't reference block1 directly, so I'll use an absolute position instead: ball resting on the floor at 0 meters along, with the block at 1.5 meters along, leaving a 1.5 meter gap, both sharing the same default across position.

