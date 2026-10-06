**What happened.** The spring swung the arm from its 0° stop to its 45° stop in 0.17 s, arriving at about 456°/s (8 rad/s). The ball left the scoop at roughly (−0.34, 0.96) m, travelling about 4.1 m/s at only 25° above horizontal; I had planned for about 4.5 m/s at 38°. It peaked at 1.12 m and came down at x ≈ 2.0 m, only about 0.1 m above the floor. It struck the outside of the bucket's near wall, dropped to the floor, and rolled back to rest at x = 0.86 m, short of the bucket.

The shot falls short because the release is flatter and slower than I planned. As the arm stops, the ball is still pressed into the scoop's back wall, which pushes it forward and down and drags on it through friction.

**The fix.** I keep the measured release, about 25° from (−0.34, 0.96) m, and raise the release speed by about 14% so the ball comes down at the bucket's centre. This would carry it over the near wall about 0.5 m up and land it about 3.08 m from its start.
- **Speed:** that means about 14% more arm speed, or about 30% more energy. Allowing for the losses this run showed, the spring goes from 4.1 to about 4.95 N·m/rad.
- **Bucket width:** I also widen the bucket to 1 m, keeping its centre 3 m from the ball's start, to allow for some error in the launch.

```json
{"what_happens": "The spring swings the arm to its 45° stop at about 8 rad/s. The ball leaves at about 4.1 m/s, only 25° up, peaks at 1.12 m and comes down at x ≈ 2.0 m about 0.1 m above the floor. It hits the outside of the bucket's near wall, drops to the floor and rolls back to rest at x = 0.86 m, outside the bucket.", "works": false, "problem": "The throw is too weak and too flat (about 4.1 m/s at 25°), so the ball falls short and hits the outside of the bucket's near wall instead of landing inside."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- The last run released the ball at about 25°, 0.51 m/s per rad/s of arm speed, from (-0.34, 0.96) m.
-- To come down at the bucket's centre it needs about 4.2 m/s along, about 14% faster.
-- That takes about 30% more energy, so the spring rises from 4.1 to 4.95 N·m/rad.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 45°
  spring        4.95 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.002 kg·m²
  friction      0.8, spinning 0.01, rolling 0.004
  colour        wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on catapult.scoop base, 4.6 cm ahead of catapult.scoop back, 0 cm to the left

-- The bucket's centre is 3 m along from the ball's start.
-- At 1 m wide its near wall is 2.5 m out, and the ball should clear it by about 0.3 m.
bucket
  is an     open box
  length    1 m
  width     1 m
  walls     30 cm
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    grey
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm checking the ball's trajectory at impact, around 0.81s where x is near 1.8, and comparing that to where the near wall of the bucket should actually be positioned relative to the ball's starting point and the 3-unit throw distance.

Backing out the launch velocity from the position data near release time (~0.17s), I get a speed around 4.1 at roughly 25°, noticeably lower than the planned 4.54 at 38°. This suggests the arm's angular velocity was close to what was planned (~7.96 rad/s vs 8.06 planned), yet the ball didn't launch at the full rigid-body speed — meaning it likely slipped or rolled along the scoop before release rather than staying fixed to the arm, possibly due to that early scoop-back contact at 0.03s pulling the ball back before the throw.

I wonder if the 38° angle comes from the arm overshooting during the soft stop while the ball is still pressed against the back wall by centrifugal force, with friction at that contact governing how the ball slides tangentially as the arm decelerates.

This pushes the ball forward-down before release, tilting velocity lower than planned—vx comes out close to target but vz falls short, likely because friction along the wall's sliding motion opposes the ball's upward-forward relative motion, dragging vz down. Since friction applies uniformly and I can't easily isolate a low-friction wall, the practical fix is probably empirical: tune the stop angle higher and increase spring stiffness to compensate for this loss.

Trying to pin down the actual relationship: if I raise the stop toward 60°, the tangent angle shifts to about 52.9°, but the resulting launch angle is hard to predict directly. Instead I'll work backward from an observed data point—tracking the ball's position and velocity through its release trajectory to back-calculate what speed and angle actually occurred, so I can tune stiffness against that empirical relationship rather than guessing geometry.

Now checking this against the observed trajectory: the ball lands near z=0.35 close to the wall around x≈2.0, which roughly matches. I need it to cross center around x=2.44 at low height and still clear the near wall with enough margin, so I'm solving for the height at the center-crossing distance using the release velocity ratio (about 25.3° effective angle) and gravity drop to see if the clearance works out.

Solving the quadratic gives x=2.863, landing at 3.08 from release — that checks out against the target.

Now checking energy consistency: scaling launch speed by 1.142 implies KE should scale to about 3.26 J, and after subtracting PE and damping losses the required work is around 4.44 J. Comparing to the k=4.1 case, predicted KE of 2.62 J versus the measured 2.50 J suggests the effective work input is somewhat lower than the simple scaling estimate.

Accounting for the extra loss, I bump the required spring work to about 4.56 J, giving k ≈ 4.93-4.95. I also wonder whether wall-friction deceleration and launch angle stay consistent at higher ω, and consider enlarging the bucket from 80 cm toward 1 m to add tolerance, which would shift the near-wall boundary to roughly 1.94 m from start.

Checking the revised geometry, landing height comes out around 0.61, which works fine, so I'll enlarge the bucket to 1 m with 30 cm walls for better tolerance. The earlier shot fell a bit short of the 2.86 target, but the scaled numbers now line up well.

