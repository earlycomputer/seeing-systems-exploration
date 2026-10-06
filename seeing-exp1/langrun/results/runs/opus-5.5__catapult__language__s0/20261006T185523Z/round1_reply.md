The catapult works, but the ball lands short of the bucket.

The arm reached its 40° stop at 0.11 s, turning at 591°/s (about 10.3 rad/s). It overshot to 44° and settled back at 40°. The ball left the scoop at about 0.12 s at roughly 4.2 m/s. It flew off lower than I planned, about 27° above level instead of about 42°, probably because it slid out against the scoop back. It peaked at 1.05 m and came down at about x = 2.06 m. That is just short of the bucket's near wall at about x = 2.18 m, while the bucket centre is at 2.58 m. The ball clipped the near wall's outside, bounced back onto the floor, and was still rolling slowly away at 6 s.

To land at mid-bucket from that release angle, the ball needs about 5.0 m/s, roughly 20% faster. That is about 40% more energy at the arm. From the run, the energy actually reaching the arm and ball is about 3.8 J. So I'm raising the spring from 5.5 to 7.5 N·m/rad and changing nothing else.

```world
world  catapult into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    50 cm
  arm mass      300 g
  swings        from 0° to 40°
  spring        7.5 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.01 kg·m²

ball
  is a      sphere 3 cm radius, 100 g
  colour    orange
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     in catapult

bucket
  is an   open box
  length  80 cm
  width   80 cm
  walls   30 cm
  at      its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

```json
{"what_happens": "The catapult arm springs to its 40° stop in 0.11 s and throws the ball at about 4.2 m/s, about 27° above level. The ball peaks at 1.05 m, comes down at about x = 2.06 m, just short of the bucket (centre at 2.58 m), clips the outside of the near wall, and ends up rolling slowly on the floor outside the bucket.", "works": false, "problem": "The throw is too weak, so the ball falls about 0.5 m short of the bucket centre and lands outside it."}
```

---
thinking (summarized):

The ball landed short of the bucket, hitting the floor near the wall around x≈2.06, while the bucket's near wall sits around x≈2.18, so it missed by just falling short at 0.77s. I'm now working out the release velocity components needed to close that gap.

Computing actual speed and angle at release: roughly 4.20 m/s at 26.6° elevation, much flatter than the predicted 42° — likely because the ball slid outward after contacting the scoop back rather than launching cleanly. To fix the undershoot, I'm reconstructing the release point by working backward from known position/velocity at 0.25s, then solving for the speed needed at that 26.6° angle to actually reach the bucket's target coordinates.

I find I need v≈4.98 m/s versus the current 4.20 — about 18.6% more speed, or roughly 40% more kinetic energy. I'm also weighing whether raising the stop angle to around 50° could recover some of that lost elevation, though the gap between the predicted 42° (minus 4° overshoot) and the actual 26.6° is large enough that I suspect the scoop back is pushing the ball outward during the arm's deceleration, which complicates any simple geometric fix.

Working through the energy balance, scaling the spring constant alone to match the needed velocity ratio gives roughly k=7.26 versus the current 5.5. But since higher speed could push overshoot further and lower elevation even more, the real sensitivity of range at low elevation makes this trickier than a straightforward spring-stiffness scaling.

Trying elevation 25° instead, I recompute required speed: v²≈25.35, v≈5.03, giving ratio 1.2 and stop ω≈12.4 rad/s. Using the effective inertia backed out from actual data (0.072, larger due to ball moving outward plus losses), the new KE needed is about 5.54 J, so total spring work should be roughly 6.4 J — meaning I need to bump up the spring constant accordingly.

Checking k=6.4/0.8529 gives about 7.5 N·m/rad, which fits comfortably within the bucket tolerance since I'm aiming dead center and the entry angle and bounce behavior still check out fine. I'll go with k=7.5.

