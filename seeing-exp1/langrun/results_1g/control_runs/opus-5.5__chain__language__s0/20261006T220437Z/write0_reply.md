Ball1 is launched rolling into ball2, ball2 knocks on into ball3, and ball3 rolls into a long, shallow cup.

The cup's near wall is a low 1.5 cm sill, so a ball moving at about 0.6 m/s or more can roll over it. Inside, the base sits 1 cm below the sill top, and the far wall is tall and dead, so ball3 is caught and stops there. I've worked the speeds out by hand but have not run the simulation.

```world
world  three balls in a row into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  sits      on floor, 50 cm along
  launched  2.5 m/s along
  spins     62.5 rad/s about y

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  sits      on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  sits      on floor, 30 cm beyond ball2

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             10 cm
  near wall height  1.5 cm
  base thickness    5 mm
  friction          0.8, spinning 0.01, rolling 0.005
  bounce            dead
  colour            wood
  on                floor, 2.1 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning a three-ball chain reaction where ball1 strikes ball2, which strikes ball3, which needs to end up in a cup—realizing a flat open box can't catch a rolling ball over its wall, so I'm thinking about sinking the cup into the floor or lowering its wall height so the ball can enter.

I'm working out the physics: a short near-wall (around 5mm) could let the ball climb in given enough momentum, while the far wall stops it with low restitution. I'm also factoring in that each collision transfers less energy due to rolling friction, so I need to pick a launch speed (around 2 m/s) strong enough to survive the chain and still settle inside the cup.

But I realize if the near wall and base are the same height, the ball could roll right back out after bouncing off the far wall, so the near wall needs to be taller than the base to actually trap it.

Let me check the physics with wall height 1.5 cm and ball radius 4 cm: using the rolling sphere step-climbing formula, the velocity reduction factor works out to about 0.73, giving a required entry speed around 0.63 m/s — comfortably achievable with a 1 m/s approach.

For the drop inside, with a 5 mm base thickness the ball falls about 1 cm, and climbing back out with h/R=0.25 gives factor 0.82, needing just v>0.46 m/s. The dead bounce off the far wall should kill most speed via high damping, and ball spin should keep friction pushing it against the wall rather than hopping over — the 10 cm far wall is well beyond the 4 cm radius so it shouldn't escape.

I'm now checking the rolling deceleration back near the wall: with μr/R≈0.05, decel ≈0.35 m/s², so a 0.3 m/s roll stops within about 1 second, well inside the 6s window. Ball1 and ball2 will likely keep sliding forward with residual spin and follow ball3 toward the cup, but since the brief only requires the third ball to roll in, that extra motion should be harmless.

Ball2 retains rolling spin so it reaches the cup at reduced speed, probably too slow to climb the 0.63 threshold step and just stops against the near wall — fine, since only ball3 should land in the cup. Rough speed estimate: launching ball1 at 2 m/s, with near-elastic collisions ball2 ends up sliding at ~1.8 then rolling at ~1.3, and ball3 picks up enough speed to clear the step. I might bump the launch speed to 2.5 m/s for extra margin, since overshooting into the far wall isn't a problem.

Now I'm working through the geometry: sphere radius 4 cm, step wall only 1.5 cm tall with 2 cm thickness, and ball positions spaced along the track at roughly 0.5 m, 0.8 m, and 1.1 m. I'm checking where the cup sits relative to the floor and confirming the ball and cup y-positions line up by default, while also pinning down what "along" means for each part's placement.

I'm computing the spin rate from v/R, getting about 62.5 rad/s about the y-axis, and verifying the sign convention so the contact point velocity cancels out correctly for rolling motion. For the cup, I'm setting friction to 0.8 and a small rolling resistance of 0.005 to help it settle, keeping bounce restitution at zero so it stays dead on contact, while giving the balls matching friction and spin parameters to roll naturally.

Now with masses at 150g each, I expect ball1 to touch ball2, ball2 to touch ball3, and ball3 to come to rest inside the cup -- time to write this out.

