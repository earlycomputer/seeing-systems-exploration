A heavy ball starts 1.5 m behind the stack and rolls into the bottom block. It knocks the block out, and the four blocks above fall and topple. The stack stands untouched for the first half-second or so while the ball travels.

```world
world  five-block stack knocked out at the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 200 g
  friction  0.6
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

ball
  is a      sphere 4.5 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  2.5 m/s along

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm planning the physical setup: five stacked blocks that topple when a launched ball strikes the bottom block, with the ball sized and positioned to collide at the block's center height.

I need to work out timing and positions so the stack visibly rests before impact—placing the ball far enough back and giving it enough speed to reach the stack after a brief delay, while using absolute coordinates for each object's position to avoid ambiguous references between objects.

For the collision itself, I'll have the ball strike roughly at the center of the bottom block so it knocks it out cleanly rather than tipping it, accounting for the friction forces resisting the block's motion and confirming the impulse is enough to dislodge it quickly. I'll set the expectation as block5 eventually touching the floor once the stack topples, and finalize friction coefficients for floor, blocks, and ball before writing it all out.

