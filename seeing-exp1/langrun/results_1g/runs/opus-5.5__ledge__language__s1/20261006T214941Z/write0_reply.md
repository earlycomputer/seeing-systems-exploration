The ball rolls off a 75 cm table at 1.55 m/s. It already has the matching spin, so friction doesn't slow it before the edge. A fall of about 0.39 s carries it roughly 60 cm out, onto the base of a 40 cm bucket centred 60 cm past the edge. On the way down it clears the 30 cm near wall with about 12 cm to spare.

```world
world  ball off a table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

-- table top runs from x = −50 cm to x = +50 cm, its top at 75 cm
table
  is a      table
  surface   100 by 60 cm
  height    75 cm
  friction  0.6, spinning 0.005, rolling 0.0001
  colour    wood

-- bucket centre 60 cm beyond the table's far edge (x = 1.1 m); inside spans about 0.91 to 1.29 m
bucket
  is an     open box
  length    40 cm
  width     40 cm
  walls     30 cm
  friction  0.8, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  on floor, 1.1 m along

-- 1.55 m/s with matching rolling spin (v / r = 1.55 / 0.03 ≈ 51.7 rad/s about +y)
ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.6, spinning 0.005, rolling 0.0001
  colour    orange
  moves     freely
  on table.top, 20 cm along
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

I need to figure out the table's physical setup—dimensions like 100 by 60 cm surface at 75 cm height, and how to position it relative to the floor since there's no explicit placement convention for centering it along an axis. I'll default to placing it at a sensible reference point if positioning syntax isn't clearly defined.

Then I work through the bucket placement, figuring its rim needs to sit a specific offset beyond the table's edge, so I'll express it as a position along the floor at roughly 1.1 meters, trusting that convention refers to the part's base origin. Finally I start considering the ball's trajectory as it rolls off the table edge, accounting for its radius in the calculation.

Checking the near wall clearance confirms the ball clears it with margin, and landing centers nicely in the bucket. Since friction will convert the slipping velocity into rolling, I need to account for the 5/7 speed reduction for a solid sphere, so I should give the ball an initial spin matching rolling motion rather than launching it with pure translation.

I'm calculating the required spin rate: for rolling without slipping at v=1.55 m/s with r=0.03, ω≈51.7 rad/s about the y-axis. Then factoring in rolling friction (0.002), the deceleration works out to roughly 0.47 m/s² effective, which over a 0.5 m roll reduces the velocity from 1.55 m/s down to about 1.4 m/s by the time it reaches the target.

Since that drag matters, I'll set the ball's and table's rolling friction coefficient explicitly to something tiny like 0.0001 (matching MuJoCo's default) instead of 0.002, making the deceleration negligible at around 0.02 m/s². Now I'm figuring out where to place the ball initially on the table surface, maybe starting it about 20-30 cm back from the edge.

I'm calculating the ball's trajectory: rolling at 1.55 m/s, it leaves the edge immediately since it exceeds the drop-off threshold, and lands around x=1.1, which falls comfortably within the bucket's inner span of roughly 0.91 to 1.27. With 30 cm high walls, the bucket should contain the ball even after some bouncing before it settles.

I'm also setting bucket friction higher (0.8) with rolling friction around 0.01 so the ball decelerates quickly (about 2.3 m/s²) once inside, while table friction stays lower (0.6, with small spin and rolling friction) and I'm enabling rolling contact via condim 6 for realistic ball physics.

Now I'm placing the pieces: ball mass 50g, bucket positioned on the floor about 1.1m along, with launch spin around 51.7 rad/s and initial speed 1.55 m/s. I'm checking that table legs and the ball's starting position don't collide, with the ball resting at the table height around z=0.75.

