A heavy ball rolls along the floor into the bottom block. The stack stands untouched for about a second before the ball arrives. The ball's centre sits at the bottom block's mid-height, so it shoves `block1` forward. Friction then drags the base of the blocks above forward while their tops lag behind, so the stack tips back and falls.

```world
world  five-block stack toppled from the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 300 g
  friction  0.8, spinning 0.005, rolling 0.002
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball, centre at the bottom block's mid-height,
-- rolling in from 1.5 m back so the stack stands for about a second first
ball
  is a      sphere 5 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    dark grey
  moves     freely
  rests     on floor, 50 cm along
  launched  1.5 m/s along

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm picturing a stack of five cubes on the floor, with the bottom one getting struck sideways by something set in motion by the world—like a rolling ball or swinging pendulum—to trigger a toppling chain reaction rather than a clean vertical drop.

Working through the tipping condition: the required acceleration to topple about the rear edge is roughly 2 m/s², well below what friction-based impulsive sliding can deliver (around 8 m/s²), so the stack should tip rather than slide intact. If the bottom block slides out, inter-block friction limits how well the upper blocks can follow, meaning they likely lag behind and the stack collapses rather than staying upright.

Running the numbers with a 1 kg ball at 1.5 m/s hitting a 0.2 kg block: the struck block shoots forward near 2.5 m/s, but friction from the floor and the stack above decelerates it around 70 m/s², stopping it within a few centimeters before the ball catches up again — leaving the upper blocks to fall onto the floor with some rotation.

Let me set positions explicitly: block stack at 2 m along the floor, ball at 0.5 m along, launched at 1.5 m/s, giving roughly a 1.4 m gap so it takes about a second to reach the stack — long enough that the stack visibly stands before impact. I'll account for slight rolling friction too.

I'm also checking the event syntax — "ball touches block" seems valid based on earlier examples like "ball touches ramp," so I'll include that as an expectation. For the cube materials, I'll set friction to 0.8 and specify its size and mass directly.

