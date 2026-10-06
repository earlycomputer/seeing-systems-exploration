**What happened.** The arm swung up and the ball left the scoop at about 0.11 s. It left early, with the arm still at roughly 35° and overshooting the soft stop to 40°. The throw came out at about 4.3 m/s and only 30° above horizontal, not the 45° I planned. The ball peaked at 1.1 m and crossed the bucket's rim height around x ≈ 1.9 m, about 0.6 m short of the bucket centre at 2.54 m. It struck the outside of the near wall at 0.78 s, bounced back and rolled to rest on the floor at x = 0.62 m.

**The fix.**
- **Stronger spring.** I keep the catapult's shape, so the launch angle should stay near 30°. I fit the path to the observed release point, about (−0.30, 0.86) m. For the ball to cross rim height near the bucket centre, the horizontal speed must rise from 3.71 to about 4.33 m/s. That means roughly 37% more useful spring energy, so the spring goes from 4.85 to 6.3 N·m/rad.
- **Longer bucket.** I lengthen the bucket along the throw to 1 m. At this flatter angle the ball can then cross the rim anywhere within about ±0.45 m of the aim and still drop in. The dead bounce stops it inside.

The bucket's centre is still 3 m from the ball's start. The 6.3 N·m/rad figure is an estimate. A stronger spring could also change how early the ball leaves the scoop, so the launch angle may shift.

```json
{"what_happens": "The spring arm swings up and releases the ball early at about 0.11 s, at about 4.3 m/s and only 30° elevation. The ball peaks at 1.1 m, falls short, hits the outside of the bucket's near wall at 0.78 s, bounces back and rolls to rest on the floor at x = 0.62 m, well outside the bucket.", "works": false, "problem": "The throw is too slow and too flat (about 4.3 m/s at 30°), so the ball lands about 0.6 m short of the bucket and bounces off its near wall onto the floor."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    50 cm
  arm mass      300 g
  swings        from 0° to 36°
  spring        6.3 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.01 kg·m²
  friction      0.8

ball
  is a      sphere 4 cm radius, 60 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    100 cm
  width     60 cm
  walls     40 cm
  bounce    dead
  friction  0.9
  colour    grey
  its base 3 m beyond ball

expect
  ball touches catapult
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

Working through the velocity data, I estimate the ball launched around 0.11-0.12s with a speed of roughly 4.29 and angle near 30°, suggesting it left the scoop before the arm actually reached its stop position.

So release is around (−0.30, 0.86) with apex near 1.10 at x=0.52, but the ball hits near the wall too early at roughly x≈2.0 when it needed to reach about 2.51 — falling short by half a meter and bouncing back. That means I need to boost speed and correct the launch angle, since the current 30° trajectory doesn't carry far enough; tuning the stop angle should steepen the release to around 51° effectively.

I'm wondering if the arm's deceleration dynamics are adding extra velocity — maybe as the joint hits its soft limit and overshoots slightly due to the solver's reference time constant, the scoop continues moving briefly and the ball separates from the back wall during that overshoot, altering the effective launch condition.

Checking the geometry instead, expected launch angles come out around 45° at 36° arm angle and 41° at 40°, but I'm seeing roughly 30°, so something other than pure tangential release must explain it — perhaps the ball is sliding along the scoop base itself, with an inward radial velocity component (toward the pivot) combining with the tangential velocity to produce a shallower resultant angle than expected.

Maybe this inward drift comes from contact dynamics: when the arm decelerates near the stop, the strong centripetal loading presses the ball into the back wall, and MuJoCo's soft-contact penetration recovery kicks it inward once that load releases, lowering the effective launch angle. Rather than modeling this precisely, I'll try an empirical fix — since the deviation from ideal seems like a consistent 11-15° shortfall, reducing the stop angle (e.g. to 25°) should steepen the launch toward the desired 40-45° range.

Working through the kinematics for a 30° launch: given the release point and target position, I compute the required horizontal distance (2.81) and vertical drop (-0.42), then solve the projectile equation for the needed exit velocity — landing on vx ≈ 4.355 m/s, about 1.17x the current 3.71 m/s, meaning roughly 1.38x more kinetic energy is needed to hit the target at that angle.

I sanity-check this against the observed trajectory data — at t=0.75s the ball was near (2.04, 0.28), and solving for where z=0.44 gives x≈1.86-1.92, which is a reasonable match to the predicted crossing point.

Now I'm considering sensitivity: a ±0.3m window out of ~2.8m range means the required velocity only has about ±5% tolerance, and the launch angle itself might shift with speed too — so maybe a steeper launch angle would be less sensitive to these errors and worth considering instead.

Looking at energy balance, the spring input (3.83 J) doesn't match observed ball KE — the ball's speed implies a system KE of 2.30 J versus an expected 3.07 J, suggesting real losses of about 0.87 J beyond gravity, likely from early separation or damping. I estimate the ball speed needs to scale by about 1.174× to hit the target, and I'm trying to figure out how to model the useful energy transfer to get there.

If I scale the net available energy (spring minus gravity) by 1.378, that points toward a stiffer spring around k≈6.37, though increasing launch speed could also change contact penetration and shift the launch angle unpredictably. I'm also considering just enlarging the bucket's opening to relax the precision needed, and I'm now working through the landing geometry — checking the descent slope near the bucket wall using the horizontal and vertical velocity components to see if the trajectory clears the target window.

Actually hitting the far wall below 0.40 is fine too since it's a dead bounce, so the real requirement is just that the ball's center stays below ~0.40 by the time it reaches the far inner face — giving a crossing window of about [x_c−0.50, x_c+0.40], roughly ±0.45 m around my aim point. I'll use a bucket of 100 cm length and 60 cm width, and retarget the aim point to x=2.49, solving for the new drop distance D≈2.79.

Solving the velocity equation gives vx≈4.334, with a ratio of 1.168 and KE ratio 1.365. Working through spring vs gravity contributions, I land on spring energy ≈4.99 J, giving k≈6.32 — though a stronger spring means more arm deflection, which could affect launch angle, so I'll approximate with k=6.3 and assume losses scale proportionally. I also confirm the bucket base position still keeps it 3 m from the ball, and with the bucket's 100 cm span centered near x_c, placing it close to the wall checks out fine.

