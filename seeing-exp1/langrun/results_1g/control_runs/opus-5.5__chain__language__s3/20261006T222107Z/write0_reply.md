Ball1 starts rolling at 2 m/s along the floor. Each collision passes most of its speed to the next ball, so ball3 should reach the cup at roughly 0.8 m/s; I estimated this and have not run it. The cup's near lip is only 8 mm high, so a ball rolling along the floor can climb in. The cup is `dead`, so its far wall kills ball3's speed. I estimate it then can't get back over the lip, which needs about 0.4 m/s. Ball1 and ball2 keep some forward spin after their collisions, so they may roll on behind ball3 and could also end up in the cup.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.003
  colour    orange
  moves     freely
  on floor, 1 m along
  launched  2 m/s along
  spins     50 rad/s about y

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.003
  colour    white
  moves     freely
  on floor, 20 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.003
  colour    black
  moves     freely
  on floor, 20 cm beyond ball2

cup
  is an             open box
  length            30 cm
  width             20 cm
  walls             10 cm
  base thickness    3 mm
  near wall height  8 mm
  bounce            dead
  friction          1.0, spinning 0.01, rolling 0.01
  colour            wood
  on floor, its base 55 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning a chain-reaction scene with three balls in a row, where the first ball strikes the second, which rolls into the third, which then rolls into a cup — thinking through how to make the cup's near wall low enough for the ball to roll in rather than bounce off.

I'm reasoning through how to keep ball3 settled in the cup after rebounding off the far wall — launching it at a moderate speed so the dead bounce plus rolling friction leaves it resting near the back rather than climbing back out over the low near wall.

Working through the energy balance for climbing the edge: after impact the ball rotates about the step edge, and I need its rotational kinetic energy to exceed the gravitational potential needed to lift the center of mass over the 1 cm step. Plugging in r=4cm, h=1cm gives a required coefficient relating velocity squared to g*h, roughly 0.47v² needing to exceed g*h.

This gives a threshold velocity around 0.46-0.5 m/s to climb the step, so I'm thinking the ball will need similar speed on the return trip near the far wall too, though contact softness in MuJoCo may make this approximate. I'm considering reducing the near wall height to around 7-8mm with a 3mm base thickness, and launching ball1 at 1.5 m/s to ensure enough speed carries through, while also noting that collision restitution in MuJoCo depends on solver reference parameters and spin isn't initialized on the launched ball.

Sliding friction will convert ball1's initial 1.5 m/s into rolling speed of roughly 1.07 m/s (5/7 factor), so I'm working out whether to instead give it initial spin — calculating that spinning about the y-axis at about 37.5 rad/s (v/r with r=4cm) would let it roll immediately without slipping, confirming the sign convention makes ω_y positive for forward motion. Then I'm turning to the collision between ball1 and ball2, considering a lively/elastic contact setting.

This is getting messy with ball1's residual motion possibly blocked at the lip or nudging ball2 and ball3 further. Since expectations only concern ball3 reaching the cup, I should just try a higher launch speed—maybe 2 m/s for ball1—to give enough margin through the elastic collision chain, estimating ball2 picks up close to the full velocity depending on the restitution coefficient.

Now I'm working out the floor layout: ball1 placed a meter in, ball2 offset 20 cm beyond it, ball3 another 20 cm beyond that, and the open-box cup positioned so its base sits roughly 55 cm beyond ball3, leaving enough clearance for the rolling sequence to reach it.

mm, base thickness 3mm, so the wall sits on floor with its top at 8mm, extending 1cm outside the base; ball ramps over this step and drops 5mm onto base top, which seems fine. I also want ball1 to have rolling spin with friction applied, each ball 150g and 4cm radius, spaced 20cm apart center-to-center along the row. Timing-wise, ball1 at 2 m/s should reach quickly, with the whole sequence wrapping up in about a second.

Things settle by 6s — the ball hitting the far wall might oscillate a bit before rolling friction brings it to rest. Ball2, trailing slower, might also drift into the cup and bump ball3, and ball1 could follow too, but that's acceptable. I'll note the expected outcome: ball1 contacts ball2, ball2 contacts ball3, and ball3 ends up at rest in the cup.

