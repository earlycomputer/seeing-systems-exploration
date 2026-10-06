A heavy ball rolls along the floor from about 1.3 m away. For roughly the first second the five-cube stack stands untouched. Then the ball strikes the bottom cube at mid-height, knocks it out, and the four cubes above lose their support and fall.

```world
world  five block stack knocked from below

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 200 g
  friction  0.6, spinning 0.005
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

pusher ball
  is a      sphere 5 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 20 cm along
  launched  1.5 m/s along

expect
  pusher ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm thinking a ball rolling in from a distance would give a natural delay before impact, letting the stack stand briefly before the bottom block gets struck and the whole thing topples—since the ball needs time to travel, unlike a pendulum that would hit almost immediately.

Now I'm working out the physics: a heavier rolling ball striking a lighter bottom cube transfers enough momentum to knock it out quickly while friction drags the upper blocks just enough to destabilize them, so I'm sizing the cubes and ball and placing them with enough separation along the floor to create a believable timing before collapse.

I'll set the success condition as the ball touching the bottom block, with the eventual toppling confirmed by the top block reaching the floor. I should also set the friction coefficient on the blocks to around 0.6 to get realistic sliding versus rolling behavior after impact.

