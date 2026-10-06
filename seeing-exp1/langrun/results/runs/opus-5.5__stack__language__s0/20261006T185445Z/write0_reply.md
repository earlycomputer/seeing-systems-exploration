A heavy ball rolls along the floor and strikes the bottom block low, below its centre, about a second after the start. Until then the stack stands untouched. The hit knocks `block1` out from under the stack, so the four blocks above drop and topple.

```world
world  stack of five knocked from below

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 200 g
  friction  0.6, spinning 0.005, rolling 0.001
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball rolled at the bottom block, hitting it below its centre
ball
  is a      sphere 4 cm radius, 1 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0.5 m along
  launched  2 m/s along

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm thinking through the physical setup: five stacked cube blocks with a sphere pusher sliding along the floor to strike the bottom block at the right height, triggering a toppling chain reaction.

I'll set the ball back about 1.5m at 2 m/s so the stack visibly stands before impact, letting it transition from sliding to rolling before reaching the blocks. With light 200g blocks and a heavier 1kg ball, the momentum transfer should be enough to kick the bottom block out via friction and destabilize the stack.

I'm also working out positioning — using absolute placement for the ball and block rather than relative offsets to keep things simple and avoid ambiguity with the "behind" direction convention.

With a 4 cm radius sphere hitting the block's bottom face below center, that should give the kick I want for toppling. I'll add some friction between the blocks, and for the success condition I'll use "ball touches block1" plus try adding "block5 touches floor" to see if that syntax is supported.

