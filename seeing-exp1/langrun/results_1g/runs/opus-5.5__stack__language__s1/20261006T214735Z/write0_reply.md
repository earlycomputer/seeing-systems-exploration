A heavy ball rolls along the floor and strikes the bottom block of a five-block stack about a second after the start. The stack stands untouched until then. The blow knocks `block1` out from under the others, and the stack topples onto the floor.

```world
world  toppling stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 250 g
  friction  0.6
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball rolled at the bottom block
ball
  is a      sphere 4 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 50 cm along
  launched  2 m/s along

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm thinking through the mechanism for knocking over the stack—maybe a pendulum or a rolling ball that strikes the bottom block after the stack has settled. I'll set up five 10cm cube blocks stacked on the floor at roughly 1 meter horizontally, giving a 50cm tall tower as the target.

Going with a ball approach: a heavy ball (around 3kg) rolling in from a couple meters away at modest speed, arriving after roughly a second so the stack stands briefly before impact, which should be simpler to stage than pendulum geometry. The idea is the ball knocks the bottom block out, letting the upper four blocks collapse.

I need to work out positioning language carefully, probably placing both the stack and the ball using absolute coordinates along the floor rather than relative references, with the ball starting around 50cm along and launched at roughly 2 m/s toward the stack at 2m along, using lighter block masses (~250g) so the impact is decisive.

For the physics, since the ball starts sliding rather than spinning, friction will convert some of that initial velocity into rolling motion, settling around 5/7 of the original speed, which should still be enough to knock the bottom block out and topple the stack. I'll describe the expected outcome using generic contact language like "touches" so it covers various toppling behaviors, and set friction on the blocks to 0.6.

