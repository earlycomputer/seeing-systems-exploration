Positions can't refer to `block1`, so the ball is now placed by absolute positions. The stack moves to 2.5 m along and the ball starts at 20 cm along. That gives about 2.3 m of rolling, so the stack stands untouched for most of a second before it is hit.

```world
world  five block stack knocked from below

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 8 by 12 cm, 150 g
  friction  0.9, spinning 0.005
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2.5 m along

pusher ball
  is a      sphere 5 cm radius, 3 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 20 cm along
  launched  3.5 m/s along
  spins     70 rad/s about y

expect
  pusher ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm working out positioning so the ball lags behind the block by about a meter, giving a roughly 0.3 second delay, and deciding whether to use relative or absolute coordinates to keep it unambiguous—probably safest to just place the block at 2.5 m and the ball further back along the same axis.

