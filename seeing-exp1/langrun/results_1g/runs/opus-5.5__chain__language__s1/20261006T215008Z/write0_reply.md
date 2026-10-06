Three 4 cm balls sit 50 cm apart along x. `ball1` is launched already rolling at 2 m/s, with a matching back-spin of 50 rad/s about y. The balls are lively, so each collision passes most of the motion on to the next ball.

The cup is an open box with a dead bounce and high rolling friction. Its base and near wall are only 5 mm tall, so `ball3` can roll straight in over the low step and be stopped by the far wall.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  on floor, 0.5 m along
  launched  2 m/s along
  spins     50 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  on floor, 1 m along

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  on floor, 1.5 m along

cup
  is an            open box
  length           30 cm
  width            20 cm
  walls            10 cm
  wall thickness   1 cm
  base thickness   5 mm
  near wall height  5 mm
  friction         1, spinning 0.01, rolling 0.02
  bounce           dead
  colour           wood
  on floor, 2.15 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning a scene with three balls in a row that collide sequentially, with the last one rolling into a cup, thinking through how MuJoCo's somewhat inelastic contact physics will affect the momentum transfer and rolling behavior.

For the cup geometry, I'm weighing the problem of the ball needing to climb over the base/wall of an open box—a thin base (around 5mm) with a similarly low near wall should let a larger ball (radius ~4cm) climb in easily, then settle against the far and side walls once rolling friction slows it to rest within the time limit.

I'm estimating the rolling friction needed: with a coefficient around 0.004 and ball radius 0.04m, deceleration works out to roughly 0.7 m/s², meaning a ball moving at 1 m/s stops after about 0.7m. To ensure a cleaner stop inside the cup, I could bump the cup's friction higher (rolling ~0.02) for stronger deceleration (~3.5 m/s²) combined with low restitution so the ball doesn't bounce back out over the low wall.

Since MuJoCo combines contact friction by taking the max between two geoms, the cup's higher rolling friction will dominate when the ball contacts it, which works in my favor, while the floor can have its own lower rolling friction (~0.002) for free rolling. I also need to think about whether to launch the ball with pure sliding velocity (which transitions to rolling at 5/7 speed) or give it initial spin matching rolling motion directly.

For the collision between equal-mass balls, given MuJoCo's default contact solref is fairly inelastic (near-zero restitution), the striking ball will essentially stop translationally but retain its spin, then roll forward again at a reduced fraction, while the struck ball picks up most of the velocity and begins sliding before transitioning to rolling.

Chaining through multiple balls with this momentum transfer and rolling friction decay, I'm laying out positions (ball1 at 0, ball2 at 0.5m, ball3 at 1.0m, cup near 1.5m) and tracking how each successive collision reduces the transferred velocity by roughly the 5/7 rolling fraction each time.

Climbing the small step at that speed works fine, and decelerating inside the cup with rolling friction stops it within about 5 cm, so a 30 cm cup length is comfortable. I also need to check whether ball2's residual spin carries it forward into the cup after hitting ball3 — it'd settle into rolling around 0.34 m/s and decelerate from there, which could cause it to trail ball3 rather than stopping short.

Checking ball2's and ball1's resulting travel distances after collisions, their spacing seems to keep things clear enough that any secondary contact with each other is gentle rather than disruptive. Now I'm laying out approximate positions for the three balls and the cup along the floor, sizing the balls and cup dimensions, and confirming the floor is large enough to contain the whole setup.

I'm working out the cup's geometry — base thickness, wall heights, and especially how the near wall should sit flush at only 5 mm so it effectively acts like a small step rather than a tall barrier. Then I'm figuring out how to phrase the cup's placement on the floor at the 2.15 m mark, settling on using "on floor, 2.15 m along" similar to how an open box would be positioned by its center.

Now I'm checking that the balls stay precisely on the y=0 line with no lateral drift, confirming widths fit inside the cup walls, and sequencing the collision chain so ball1 hits ball2, ball2 hits ball3, and ball3 ends up resting in the cup. I'm also assigning restitution values — lively for the balls so momentum transfers well, dead for the cup — and calculating the spin rate needed (50 rad/s) based on the velocity and ball radius.

I'm setting friction coefficients: balls get 0.8 sliding, 0.005 spinning, 0.002 rolling; the cup gets 1, 0.01, and 0.02 respectively, checking that the higher rolling friction near the cup's edge won't meaningfully resist the ball's motion. I'm satisfied that ball3 arriving at 0.6 m/s against the dead far wall will simply stop there, so I'm ready to write this out.

