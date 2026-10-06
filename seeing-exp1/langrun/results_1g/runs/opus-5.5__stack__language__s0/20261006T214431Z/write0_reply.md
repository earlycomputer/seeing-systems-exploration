A heavy ball rolls along the floor and strikes the bottom block of a five-cube stack side-on. Friction then drags the block above along while the top of the stack lags behind, so the stack should tip over.

```world
world  toppling stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 200 g
  friction  0.6, spinning 0.005, rolling 0.002
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1 m along

ball
  is a      sphere 5 cm radius, 1.5 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 60 cm behind block
  launched  2.5 m/s along

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I need a stack of five blocks that stays stable until something strikes the bottom block, so I'm thinking of using a launched box or pendulum that swings in from the world itself to knock the base out and topple the stack.

Actually a pendulum with a precise bob height and arm placement feels fussy, so I'm leaning toward a rolling ball instead — rolling friction keeps it from decelerating like a sliding box would, and sizing it at 5 cm radius lets it strike the bottom block right at the midpoint for a clean hit. I'm settling on 10 cm cube blocks stacked five high, with a 2 kg ball positioned some distance behind the stack and given an initial launch velocity so it rolls freely into the base.

I'm also weighing whether a fast hard hit will actually topple the stack or just cause the base block to shoot out from under it (tablecloth effect) while the top blocks drop straight down. A slower, heavier push with friction dragging the base block along seems more likely to make the upper blocks lag behind and tip the stack over, so I'm considering reducing the ball's speed and increasing its mass to get that toppling behavior.

That friction causes the top block to lag and topple, so I'll settle on cubes with 0.6 friction, roughly 10 cm and 200 g each. I'll place the ball 60 cm behind block1, launch it around 2.5 m/s to account for skidding losses, and set the expectation as the ball touching block1 and block5 eventually touching the floor.

