**What happens in the run:** The stack stands still the whole time, and the push never comes. The ball was launched with no spin, so it skidded at first. Rolling friction then slowed it hard, about 0.5 m/s² (the floor's rolling 0.002 sets this). It came to rest at x = 1.41 m, exactly touching distance from block1, without pressing on it. Nothing toppled.

**Changes:**
- The ball now starts already rolling, with 30 rad/s about y to match 1.5 m/s on a 5 cm radius.
- Rolling friction on the floor and the ball is far lower, so the ball keeps its speed.
- It should reach block1 at about 0.85 s, still moving about 1.4 m/s.
- It is heavy and has a dead bounce, so it should keep shoving the thin block. That should slide the base forward and tip the tall stack.

```json
{"what_happens": "The five blocks stand still for the whole 6 s. The ball rolls toward them but rolling friction slows it to a stop at x = 1.41 m, just touching distance from block1, so it never pushes it and nothing topples.", "works": false, "problem": "The pusher loses all its speed to rolling friction and stops before it can push the bottom block."}
```

```world
world  stack toppled by a push at the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

block
  is a      box 8 by 16 by 12 cm, 400 g
  colour    wood
  friction  0.7
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

pusher
  is a      sphere 5 cm radius, 2 kg
  colour    grey
  rolls
  bounce    dead
  friction  0.8, spinning 0.001, rolling 0.0002
  moves     freely
  rests     on floor, 20 cm along
  launched  1.5 m/s along
  spins     30 rad/s about y

expect
  pusher touches block1
  block5 touches floor
```

---
thinking (summarized):

I'm working through the deceleration phases — sliding friction first, then a stronger rolling deceleration — and checking whether the ball's stopping distance of 1.41 falls just short of reaching the block, accounting for the ball's radius versus the block's face position at 1.46.

To fix this, I need to launch the ball faster, add proper spin (ω = v/r about the y-axis) so it rolls without slipping, and reduce the rolling friction coefficients on both the ball and floor to cut the deceleration down, since MuJoCo takes the max of the two surfaces' friction values. I'm settling on a launch speed of 2.5 m/s, starting position of 0.2 m, spin of 50 rad/s, and hit energy of 2, giving roughly half a second of travel before impact.

Now I'm thinking through the collision dynamics: a 2 kg ball at 2.5 m/s hitting a 0.4 kg block would send it shooting out fast, likely causing the stack to collapse rather than topple gracefully. I want a gentler push instead, so the bottom block slides out while the stack leans back — testing a lower contact speed like 1.0 m/s to see if that produces a more controlled, leaning collapse, accounting for floor friction load across the stacked blocks.

