A rolling 2 kg ball is the pusher. It starts 1.2 m behind the stack and rolls along the floor. It strikes the bottom block about 0.9 s in, at 6 cm height. That knocks the bottom block out, and the four tall blocks above fall.

```world
world  toppling stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 8 by 16 cm, 300 g
  friction  0.6, spinning 0.005, rolling 0.002
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1 m along

ball
  is a      sphere 6 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 1.2 m behind block1
  launched  1.2 m/s along
  spins     20 rad/s about y

expect
  ball touches block1
```

The ball's starting spin (20 rad/s = 1.2 m/s ÷ 6 cm) matches its speed, so it rolls from the start rather than sliding and losing speed. Nothing touches the stack until the ball arrives.

I haven't run this. The bottom block might shoot out from under the others instead of tipping them. If so, the upper blocks may drop more or less straight down rather than visibly topple. The expectation only checks that the ball hits `block1`, not that the stack actually falls over.

---
thinking (summarized):

I'm picturing a stack of five blocks standing stable until something strikes the bottom block and topples the stack. I'm considering options like a pendulum swinging in or a heavy box sliding along the floor with friction to deliver the hit, leaning toward the sliding box as the simplest mechanism.

Working through the forces: the ball's momentum transfers to block1, which has to overcome friction from the blocks stacked above plus floor friction, so it shoots forward while the upper blocks drop and likely topple. I'm reconsidering the geometry—maybe taller, narrower blocks (8x8x16 cm, 300g) stacked five high topple more easily, with the ball sized so it strikes at the right height, and I'm placing the ball 60 cm behind the stack on the floor for the setup.

Adjusting the starting distance to around 1.2 m with launch speed 1.2 m/s gives roughly 0.9 seconds before impact, accounting for the ball transitioning from sliding to rolling (slipping friction reduces speed to about 5/7 of initial, so ~0.86 m/s) and adding spin to match rolling motion from the start.

