The ball starts rolling on a 75 cm table, 30 cm from the far edge, with a matching spin so it rolls without slipping. It is launched at 1.7 m/s. Falling from its centre height of 0.78 m takes about 0.33 s to reach the bucket's rim, by which point the ball is about 55 cm beyond the edge. It reaches the bucket floor at about 65 cm. The bucket is centred 60 cm beyond the edge and is 30 cm long, so the ball drops inside it. A dead bounce and 25 cm walls should keep it there.

```world
world  ball off the table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

-- table top spans 120 cm along, centred at x = 0, so its far edge is at x = 60 cm; top surface at 75 cm
table
  is a     table
  surface  120 by 60 cm
  height   75 cm

-- bucket centre at x = 120 cm, i.e. 60 cm beyond the table's far edge; rim 25 cm high
bucket
  is an   open box
  length  30 cm
  width   30 cm
  walls   25 cm
  on floor, its base 120 cm beyond table.top

-- rolling without slipping: spin = speed / radius = 1.7 / 0.03 ≈ 56.7 rad/s about y
ball
  is a      sphere 3 cm radius, 50 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.0001
  moves     freely
  on table.top, 30 cm beyond table.top
  launched  1.7 m/s along
  spins     56.7 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm setting up the physics scenario: a ball rolling off a table with height h and launch speed v, needing to land in a bucket centered 60 cm past the table's edge, while accounting for how rolling friction affects the ball's speed as it leaves the surface.

Now I'm working out the table's dimensions and placement — roughly a 120 by 60 cm surface at 75 cm height — and considering how to position it in the scene relative to the floor and bucket so the trajectory math works out correctly.

I'm unsure if "beyond" works with a face reference, so I'll go with the safer option of placing the bucket's base 120 cm beyond the table.top, keeping it on the floor and letting the across offset default to zero.

For the bucket itself, I'm sizing it 30 cm by 30 cm with 25 cm walls, 2 cm base thickness, and a rim at 25 cm.

Now I'm working through the ball's physics: a 3 cm radius ball rolling 0.9 m to the table edge needs enough initial velocity to overcome rolling friction, since MuJoCo's default rolling resistance would decelerate it significantly over that distance—so I should keep the ball's rolling friction coefficient small to let it travel the full distance.

I need the bucket rim at 0.25m and want the ball landing near the opening center around x=1.2, so I'm working out a fall from z=0.78 down to roughly z=0.15 inside the bucket mouth, giving a drop of 0.63m and computing the corresponding fall time to then back out the needed horizontal velocity.

Checking the trajectory at rim height (z=0.25) lands x≈1.15, well inside the opening, and at base contact (z≈0.05) it lands x≈1.246, still fine. For the launch point itself, since v²/r is much greater than g, the ball separates cleanly from the edge right as its center passes x=0.6.

Using v=1.7 m/s with spin of about 56.7 rad/s, I'll set the bounce to dead so the ball settles inside the bucket rather than bouncing back out, with the 25cm walls containing it after it hits the base and far wall. I'm confirming the ball clears the table legs since it launches forward and away from them, and the bucket sits comfortably within the table's 120x60 footprint.

For placement, I'll leave the table without a position line so it stays centered at the origin, since the raised bucket piece doesn't specify one either. The ball gets positioned on the table's top surface, offset 30cm forward, with a mass of 50g and friction settings of 0.8 sliding, 0.005 spinning, and 0.0001 rolling, running the simulation for 6 seconds to see it come to rest in the bucket.

