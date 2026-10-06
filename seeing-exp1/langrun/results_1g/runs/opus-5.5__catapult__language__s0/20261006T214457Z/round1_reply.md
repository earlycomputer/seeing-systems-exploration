**What happens in the run:** The catapult works as built. Its arm flies up from 0° and hits its 38° stop at 0.14 s, moving at 469°/s, then settles there.

The ball leaves the scoop at about (−0.40, 0.92) m. It goes out at about 4.0 m/s, and only about 32° above the horizontal; I had expected 4.7 m/s at 45°. That makes it fall short. It touches the floor near x ≈ 1.98 m at 0.84 s, just in front of the bucket's near wall at 2.08 m. It clips the outside of that wall and comes to rest on the floor at x = 2.01 m, outside the bucket.

**The fix:** I fitted the real launch: 32° from (−0.40, 0.92), reaching 4.03 m/s at the old spring. That fit reproduces the observed landing. To land at the bucket centre (x = 2.48 m), the ball needs about 4.6 m/s. That is about 30% more energy, so I raised the spring from 5.2 to 6.3 N·m/rad. I also widened the bucket to 1 m for more margin. The ball should still clear the 30 cm near wall by roughly 35 cm.

```json
{"what_happens": "The catapult arm swings up to its 38° stop at 0.14 s and releases the ball at about 4.0 m/s, only about 32° above horizontal. The ball lands on the floor at x ≈ 1.98 m, just short of the bucket's near wall at 2.08 m, clips the outside of that wall and comes to rest on the floor at x = 2.01 m, outside the bucket.", "works": false, "problem": "The throw is too weak and too flat, so the ball lands about half a metre short of the bucket centre and never gets in."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- The arm runs back (−x) from the pivot; a positive angle lifts the scoop end.
-- The spring pulls toward 90°, so the arm flies up from 0° and stops hard at 38°.
-- Measured launch is about 32° from (−0.40, 0.92) m; landing at the bucket centre needs about 4.6 m/s.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 38°
  spring        6.3 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.01 kg·m²
  colour        wood

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     in catapult

-- Bucket centre 3 m ahead of the ball's start; dead walls so the ball stays in.
bucket
  is an   open box
  length  1 m
  width   1 m
  walls   30 cm
  bounce  dead
  colour  grey
  on floor, 3 m beyond ball

expect
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm estimating the ball landed short of the bucket by about half a meter, falling around 2.0 m instead of reaching 2.48 m, so I'm working backward through the velocity components near release to see where the trajectory diverged.

Backtracking further, the release speed comes out around 4.0 m/s at a 32° angle, noticeably lower than the expected 45° from the arm's swing speed. That discrepancy makes me think the ball wasn't launched cleanly at the arm's tip — the scoop's back geometry and the ball's position relative to the pivot suggest it had outward radial sliding velocity in addition to the arm's rotation, which would explain the flatter-than-expected launch angle.

Rather than chasing the exact physics further, I'll just tune empirically: given the current launch speed and angle, I need to figure out what adjustment (likely spring strength) gets the ball to land at the bucket center around x=2.48, z=0.05.

Checking the current model with v=4.03 confirms the landing point matches, so the physics tracks well. Now I need to scale v up to 4.60, which means raising kinetic energy by a factor of about 1.3; working backward through the spring's energy input versus estimated losses from gravity and damping, I'm solving for the new spring constant k needed to supply that extra energy, landing around k≈6.22, though the loss terms may not scale linearly so I need to double check that assumption.

I'm also checking tolerance — with a ±0.4m landing bucket, the range sensitivity to velocity suggests roughly ±0.33 m/s margin, which seems workable. Then I'm checking the landing trajectory's steepness and whether the ball clears the wall near the target, tracing through the velocity components and time of flight to get the slope at landing and position relative to the wall.

