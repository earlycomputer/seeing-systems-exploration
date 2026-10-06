**What happened:** The arm reached its 35° stop at about 719°/s (12.6 rad/s). It overshot softly to 39.6°, and the scoop back stayed on the ball a moment longer. The ball left at about 3.95 m/s, 31° above horizontal, not the 4.8 m/s at 44° I had planned. It peaked at 0.99 m high, landed on the floor at x ≈ 1.95 m, hit the outside of the bucket's near wall and settled at x = 2.16 m. That is short of the bucket, whose centre is at x = 2.64 m.

**Fix:** I reworked the throw from the launch actually measured.
- The measured release point (x ≈ −0.25 m, z ≈ 0.78 m) and the 31° angle fit the run's landing. Keeping that angle, the ball needs about 4.83 m/s, 1.22 times the old speed.
- That means 1.5 times the kinetic energy. Allowing for the losses this run showed, the spring goes from 4.53 to about 6.4 N·m/rad.
- I widened the bucket to 1 m for margin. Its base centre stays 3 m from the ball's start.

```json
{"what_happens": "The spring swings the catapult arm to its 35° stop in 0.09 s; the ball flies off at about 3.95 m/s, 31° above horizontal, peaks at 0.99 m, lands on the floor at about x = 1.95 m, glances off the outside of the bucket's near wall and comes to rest on the floor at x = 2.16 m, short of the bucket.", "works": false, "problem": "The throw is too weak (about 3.95 m/s at 31° instead of the planned 4.8 m/s), so the ball lands about half a metre short of the bucket."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- Measured last run: k = 4.53 gave ~3.95 m/s at 31° from (-0.25, 0.78) m.
-- Reaching the bucket at that angle needs ~4.83 m/s: about 1.5 times the
-- kinetic energy, so the spring is raised to ~6.4 N·m/rad.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    40 cm
  arm mass      300 g
  swings        from 0° to 35°
  spring        6.4 N·m/rad toward 90°
  damping       0 N·m·s/rad
  armature      0.001 kg·m²
  colour        wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

-- Base centre 3 m along from the ball's starting centre.
bucket
  is an   open box
  length  100 cm
  width   100 cm
  walls   25 cm
  bounce  dead
  friction  0.9, spinning 0.01, rolling 0.004
  colour  grey
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

The arm only reached 719°/s, short of the 13.04 rad/s target, so computing the ball's velocity at release gives roughly 3.95 m/s at a 31° launch angle, well below the expected 4.78 m/s at 44°.

This discrepancy suggests the ball wasn't rigidly pinned and slipped during release, possibly dragging against the scoop's back wall and losing speed while its direction rotated. Working backward from the tracked trajectory, I'm estimating the release position at roughly x=-0.25, z=0.78, which roughly matches the expected release point of (-0.255, 0.764), and the ball's first floor contact occurs near x=1.95 at t=0.74s.

Since I need the ball to land further out near x=2.52, I'm calculating how much I'd need to scale up the launch velocity while keeping the same 31° angle — solving the projectile equations gives a required speed of about 4.83 versus the current 3.95, suggesting the spring needs a meaningful boost.

Let me verify where the current trajectory actually lands by solving for when z drops to the table height and then to floor level, tracking the ball's position at each key crossing point.

Now I'm comparing the actual rotational speed to predicted: the measured ω (12.55) gives less kinetic energy than predicted (2.705 J vs 2.92 J), suggesting some energy loss beyond the spring work calculation, possibly from rolling or lateral ball motion. The actual-to-predicted KE ratio comes out to about 0.926, which I'll need to apply against the squared ratio of 1.496 to adjust the model.

Working through this, scaling by the same fractional efficiency gives a needed spring constant of about 6.41, though I'm not fully confident losses scale linearly this way — higher speeds might change the ball's centripetal dynamics differently. I'll accept this estimate for now rather than second-guess further, and I'm considering whether widening the bucket (rather than moving it, since it needs to stay 3 m from the ball's start) could help absorb uncertainty in the launch angle and range.

I'll widen the bucket to 1 m for margin, leaving the ball center room within the walls. I'm trying to understand why the elevation angle came out at 31° rather than matching the tangent trajectory — possibly interference from the scoop's back wall during the ball's release — but since I can't easily modify that mechanism, I'll just keep tuning the spring constant k empirically. I'm now setting up the landing condition: crossing the bucket height at a specific horizontal offset with the computed velocity and angle, then working through the shallower descent this lower angle implies for where the ball ultimately lands.

Running the numbers, the ball crosses the bucket rim height with a horizontal velocity around 4.14 m/s, taking about 0.67 seconds to reach that point, with a steep descent angle near 44.5°. Tracking it further to the bucket floor, it lands close to the center with a comfortable margin before hitting the near wall, confirming it clears safely. Given the 1 m bucket width and centered aim, I estimate roughly ±6% tolerance on speed, which seems workable with the spring torque I've settled on and the 31° elevation.

