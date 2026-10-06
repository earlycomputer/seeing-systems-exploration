## What happened in the run

The spring swung the arm up to its 45° stop in 0.17 s. It reached about 8 rad/s (457°/s), close to my estimate.

The ball, however, left flatter and slower than I predicted:

| | Predicted | In the run |
|---|---|---|
| Launch speed | 4.6 m/s | about 3.96 m/s |
| Launch angle above horizontal | 38° | about 27° |

It peaked at 1.12 m and came down at x ≈ 1.97 m, about 0.2 m short of the bucket's near wall. It glanced off the outside of that wall and came to rest on the floor at x = 1.92 m, outside the bucket. The throw falls short.

## The correction

I took the release this run actually produced: from about (−0.345, 0.954) m, at 27°. I assumed the angle stays about the same at higher speed.

To cross the rim height at x ≈ 2.40 m, that release needs about 4.76 m/s, which is 1.2× the measured speed. That means about 9.6 rad/s at the stop.

Scaling the spring's work by the efficiency this run showed gives a stiffness of about 5.2 N·m/rad. The new throw should come down at about x ≈ 2.4–2.6 m, inside the bucket.

```json
{"what_happens": "The spring swings the arm to its 45° stop at about 8 rad/s and the ball is thrown at about 3.96 m/s, 27° above horizontal (flatter and slower than intended). It lands on the floor at x ≈ 1.97 m, short of the bucket (whose inner span starts near x ≈ 2.06 m), glances off the outside of the near wall and comes to rest on the floor at x = 1.92 m.", "works": false, "problem": "The throw is too weak and flat, so the ball lands about half a metre short of the bucket instead of in it."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 45°
  spring        5.2 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.001 kg·m²
  colour        wood
  stands        on floor

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    80 cm
  width     80 cm
  walls     25 cm
  friction  1.0, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  stands    on floor, its base 3 m beyond ball

expect
  catapult reaches its upper stop
  ball comes to rest in bucket
```

---
thinking (summarized):

The ball fell short of target. The release spin matched closely at about 8 rad/s, but the vertical velocity was too small, giving a much flatter trajectory than predicted. I'm working backward to estimate what the actual release velocity components were around 0.17-0.18s, using the vz value at 0.25s and subtracting out the gravity contribution.

Comparing to the predicted launch speed and angle, the actual release is noticeably slower and flatter — speed near 3.94 m/s at 26° instead of the predicted 4.5 m/s at 38°. I suspect the ball is slipping or dragging against the scoop near release rather than releasing cleanly tangent to the arm's motion. Given the floor landing point falls about 0.65m short of where it needs to cross the rim, I'm considering whether increasing the stop angle to produce a steeper launch would compensate for this flatter-than-expected release.

Solving gives v²=22.62, so v=4.756, a ratio of about 1.2 over the original speed. Checking the landing point with this speed confirms the trajectory crosses z=0.29 near x=2.40 and lands within the valid range, so this speed works.

Now I'm estimating the spring stiffness needed: actual angular velocity is 7.98, but I need roughly 9.58 to hit this speed. Computing KE requirements, accounting for damping and efficiency mismatch between predicted and measured energy, gives a required spring work around 4.85 J, so k ≈ 5.24, roughly 5.2 N·m/rad. I'm now wondering whether the launch angle itself depends on this spring stiffness rather than staying fixed.

The loss factor scaling seems consistent enough, and the ball bouncing off the bucket near the wall is fine too. I'll go with k=5.2.

