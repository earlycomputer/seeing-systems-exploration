The cup is a shallow open box on the floor. Its near wall is only as tall as its 5 mm base, so it makes a flat lip that a rolling ball can climb over. Its high rolling friction stops ball3 well before the far wall.

`ball1` starts already rolling at 1.5 m/s (spin = v/r) and the balls are lively, so most of the motion passes down the row. `ball3` should reach the lip at about 0.6 m/s and stop about 12 cm inside. `ball1` and `ball2` are left crawling with leftover spin, but they should stop short of the cup.

These figures come from rough estimates, not from a run. They assume the higher rolling-friction value of a contacting pair is the one that applies. The `expect` block lists the result the run should be checked against.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor
  launched  1.5 m/s along
  spins     37.5 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    grey
  moves     freely
  rests     on floor, 20 cm beyond ball2

-- a shallow cup whose near wall is a flush 5 mm lip, so a rolling ball can enter
cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  5 mm
  friction          1.0, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  on floor, its base 49 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning the physics setup: three balls in a row where ball1 strikes ball2, ball2 strikes ball3, and ball3 rolls into an open cup/box to settle at rest. I'm thinking through how to make the box's near wall short enough for the ball to roll over and in, rather than blocking it.

With dead-contact walls, a rolling ball hitting the far wall would lose its normal velocity but keep spinning, and friction at the floor and wall contacts would keep driving it against the wall until spin dissipates — so it settles resting there, which works for my purpose. I'm now considering simplifying the cup geometry further, maybe just making the near wall as low as the base thickness so entry is easy, though that still needs some wall thickness to define.

Thinking through the step-climbing physics: with a 5mm lip and a 4cm ball radius, the height-to-radius ratio is small (0.125), so I need to check whether the ball's incoming speed is enough to climb over that edge versus bouncing off it.

Working out the required velocity, I get a threshold of roughly 0.37 m/s — well below a launch speed of 1 m/s, so climbing should succeed, especially since MuJoCo's soft contacts make it more forgiving. I'm also considering whether to launch the ball with pure translational velocity (which would slide before friction brings it to rolling at 5/7 v) or give it initial spin so it starts in pure rolling motion right away.

For the collision sequence, when ball1 strikes ball2, ball2 picks up translational velocity without spin, so it slides before settling into rolling motion, while ball1 retains its spin and keeps inching forward — meaning they could collide again, which is fine, and ball3 ends up with some fraction of the original speed.

After losses, ball3 probably hits the cup wall around 0.6-0.75 m/s, which seems sufficient to overcome the small lip. Meanwhile ball2, after its own collision with ball3, gains residual spin that friction converts into forward crawl at roughly 2/7 of its velocity, so it might also creep toward the cup eventually — this doesn't obviously conflict with the goal of ball3 settling in the cup, but I need to check whether ball2 catching up to ball3 afterward could disturb it.

I'm now working out how rolling friction affects distances: with MuJoCo's rolling friction coefficient around 0.002, deceleration for a ball of radius 0.04 m comes out to roughly 0.35 m/s². That means ball2 crawling at 0.2 m/s would stop after only about 6 cm, while ball3 moving faster at 0.7 m/s could travel nearly 70 cm before stopping. So I should keep the gap between the row and the cup fairly short, maybe around 30 cm, to make sure ball3 actually reaches the cup with enough speed.

Checking the numbers, ball3 would arrive at the cup around 0.5 m/s, which is fine. I'm considering giving the cup itself a higher rolling friction (like 0.01) so balls settle quickly once inside, since MuJoCo takes the max friction between contacting surfaces — this way ball3 entering around 0.6 m/s would stop within about 10 cm inside the cup, which works well for making it look settled.

Ball1 likely won't reach the cup either after its own collision-crawl. Working out the chain reaction: giving ball1 an initial rolling velocity of 1.5 m/s, it transfers momentum through ball2 and ball3 with rolling friction reducing each successive speed, ending with roughly 0.65 m/s entering the cup — which works. I'm keeping all balls aligned at y=0 with the cup width at 30 cm for lateral alignment.

Now I'm figuring out the cup geometry — an open box 30 cm long, 30 cm wide, 12 cm wall height, 2 cm wall thickness, 5 mm base — and deciding how to position it relative to ball3 using a placement clause like "its base 45 cm beyond ball3," checking whether "beyond" also constrains the lateral offset or just the forward distance.

I'm settling the near wall and base thickness at 5mm each, both resting on the floor with the lip flush, and centering the side walls along the base's length. For the balls, I'll describe each as resting on the floor with spacing relative to the prior one—ball2 30cm beyond ball1, ball3 20cm beyond ball2. I'm also considering whether MuJoCo's default contact damping will make ball collisions feel too inelastic rather than lively bounces.

Even if it bounces off the far wall, rolling friction inside the cup should slow it enough to settle—working out the deceleration from rolling resistance (~1.75 m/s²), it'd stop within about 0.12 m, so making the cup around 40 cm long should give enough room to keep the ball from rolling back out over the 5 mm lip.

I'm setting up the three balls (each 100 g, 4 cm radius) so ball1 touches ball2 and ball2 touches ball3, with ball3 expected to settle in the cup, then finalizing the scene with a default 6 m floor.

