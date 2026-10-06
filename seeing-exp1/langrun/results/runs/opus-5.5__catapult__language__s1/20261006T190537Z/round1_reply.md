## What happened in the run

- **Swing:** the spring threw the arm up from 0°. It reached its 40° stop at 0.16 s, turning at 454°/s (7.9 rad/s), which is close to the 8.05 rad/s I planned for.
- **Launch:** the ball left the scoop at about (−0.38, 0.93) m. Its speed was only about 3.95 m/s at roughly 31° above the horizontal. I had planned 4.6 m/s at 44°.
  - The arm overshot its stop to 43.4° and stayed in contact with the ball until 0.17 s.
  - Friction from the scoop back, while the arm was stopping, likely took away part of the ball's upward speed.
- **Flight:** the ball peaked at 1.15 m at 0.37 s and hit the floor at about x = 1.94 m. That is short of the bucket, whose near wall is at about x = 2.08 m.
- **End:** the ball bounced off the outside of the near wall and came to rest on the floor at (2.02, 0, 0.03) m, outside the bucket.

## The correction

I kept the geometry and corrected for the losses that actually happened.

- **Speed needed:** from the measured release point and a 31° launch, landing near the bucket centre (x ≈ 2.45 m) needs about 4.55 m/s. That is 15% faster, so the arm must reach about 9.1 rad/s.
- **Spring needed:** in this run the spring delivered about 97.6% of its energy. Using that, the arm needs about 3.99 J at the stop, which gives k ≈ 4.8 N·m/rad.
- **Clearing the wall:** on this path the ball should pass over the near wall roughly 20 cm above its top, then come down well before the far wall.

```json
{"what_happens": "The spring swings the arm to its 40° stop at 0.16 s (about 7.9 rad/s), but the ball leaves at only about 3.95 m/s and 31°. It peaks at 1.15 m, lands on the floor at x ≈ 1.94 m, short of the bucket, bounces off the outside of the near wall and comes to rest outside at x ≈ 2.02 m.", "works": false, "problem": "The ball is thrown too slowly and too flat (friction and overshoot at the arm's stop cost speed), so it lands just short of the bucket instead of in it."}
```

```world
world  catapult into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 40°
  spring        4.8 N·m/rad toward 90°
  damping       0 N·m·s/rad
  armature      0.01 kg·m²
  stands        on floor

ball
  is a      sphere 3 cm radius, 60 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  sits      on catapult.scoop base, outside catapult.scoop back's far end

bucket
  is an   open box
  length  70 cm
  width   70 cm
  walls   25 cm
  stands  on floor, its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

The ball landed short, around x≈2.0 near the wall at 2.08, instead of reaching the bucket. Working backward from the release point, I calculate the speed at release as about 3.95 m/s at a 31° angle, versus the expected 4.62 m/s at 44°, so I need to adjust for the shortfall.

Checking the arm speed itself (7.92 rad/s vs planned 8.05) and back-calculating the ball's release position shows the arm is tracking reasonably close to plan, so the discrepancy seems to be in the ball's velocity direction and magnitude rather than timing. The expected velocity components were roughly (3.26, 3.15) but the actual came out (3.38, 2.04) — vx slightly high but vz much too low — which makes me suspect something like rolling friction against the scoop base, the ball sinking into a soft contact, or the arm decelerating differently than modeled near the release point.

This points toward friction between the ball and the scoop's back face during the arm's deceleration phase. As the arm slows down over roughly 0.01s before release, the ball likely stays pressed against the back by centrifugal force and slides along it, and friction bleeds off the velocity component normal to the arm while leaving the along-arm component relatively intact. Decomposing into arm-normal and arm-outward directions confirms this: the normal component lost about 0.8 m/s relative to expectation, consistent with friction dragging down that component as the arm stops.

Rather than chasing the exact physical mechanism further, I'm considering a more practical fix — simply tuning the ball-back friction coefficient or geometry empirically to hit the target range, since the full dynamics of contact release are getting complicated to model precisely.

Solving for required speed at the measured 31° angle: using the landing distance equation with gravity, I get v²≈20.67, so v≈4.547 versus current 3.95, giving a scale ratio of about 1.151. I'm also checking that this trajectory clears the wall near x≈2.06-2.08 given the target centered at 2.43 with a 70cm base.

Checking wall clearance at the near edge, the ball's height there comes out to about 0.479, clearing by roughly 0.2 which looks fine, and the landing point at 2.45 stays safely before the far inner wall at 2.77. Since the current bounce off the floor looks dead already, I just need to scale angular velocity up by the 1.151 ratio, which means kinetic energy needs to increase by about 1.325x.

Working through the arm's actual KE at the top (2.346 J vs planned 2.426, accounting for some loss), I calculate the required spring energy needs to rise to roughly 4.09 to deliver the needed 3.99 J after gravity losses, giving k ≈ 4.80 — though solving via the efficiency ratio instead gives η ≈ 0.976 or so, close enough to confirm the scaling approach is consistent.

I'll round to k = 4.8. The release angle might also shift slightly due to a bigger overshoot, but that's an acceptable uncertainty — checking the range margin, aiming for the center with ±0.32 m tolerance, and since range scales roughly with velocity squared, a 10% range error corresponds to only about 5% speed error, which is within acceptable bounds.

