The spring-loaded arm throws the ball, and a hinge stop at 45° releases it at about 4.5 m/s. These numbers are hand calculations, not results from a run. On paper the ball crosses the near rim about 35 cm above it and lands near the middle of an 80 cm open box. The box's centre is 3 m along from the ball's starting point, measured horizontally.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- Arm 60 cm long, pivot at 50 cm. The scoop is at the near end, 0.56 m from the pivot.
-- The spring pulls toward 90° but the hinge stops at 45°.
-- Spring work ≈ 3.79 J. That covers lifting the arm, scoop and ball (≈1.10 J), damping (≈0.07 J)
-- and ≈2.6 J of spin: about 8.1 rad/s, so the ball leaves at ≈4.55 m/s, about 38° up.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 45°
  spring        4.1 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.002 kg·m²
  friction      0.8, spinning 0.01, rolling 0.004
  colour        wood

-- The ball sits in the scoop with 1 mm to spare against the scoop's back wall,
-- so it starts where the throw pushes it.
ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on catapult.scoop base, 4.6 cm ahead of catapult.scoop back, 0 cm to the left

-- The bucket's centre is 3 m along from the ball's start.
-- The ball should cross the near rim about 35 cm above it and land near the middle.
bucket
  is an     open box
  length    80 cm
  width     80 cm
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

I'm working out the catapult's geometry—sizing the stand, pivot height, and arm so the hinge and scoop align properly for launching the ball toward the bucket 3 meters away.

Now I'm checking the rotation math: a positive angle about the hinge axis raises the scoop end and swings it forward, so at 45° the launch velocity points diagonally up-and-forward, which is what I want for the throw. I still need to figure out the release angle and the stop mechanism that halts the arm's swing so the ball flies off with the right trajectory.

At release, the ball's velocity is tangential, pointing at 45° above horizontal when θ=45°. I need to work out the ball's position at that instant—accounting for pivot height, arm radius, and the offset from arm to ball center—so I can compute its launch point before figuring out the projectile range.

The target is a bucket whose center sits 3 m horizontally from the ball's starting position, and I'm placing the ball directly on the catapult's scoop base so it's centered correctly at the start.

I'll start the arm resting at 0° with the spring driving it toward a higher angle, stopping at the joint's upper limit—say a 0° to 45° range—so the spring torque launches the ball once the simulation begins. Need to check how MuJoCo handles the hinge limit and stop behavior there.

Checking geometry: the stand under the pivot and the arm's reach shouldn't collide given their dimensions, with roughly a 4 cm gap, and the lower joint limit of 0° prevents the arm from drooping under gravity before launch.

Now figuring out the launch mechanics: picking a 45° launch angle, I set pivot height at 50 cm and arm length 60 cm, giving the scoop's near-end pivot radius r ≈ 0.52 m, with offset d accounting for arm half-width, base thickness, and ball radius, so I can compute the release point's horizontal displacement from the start position.

I need to account for the offset angle since the ball's velocity direction isn't exactly along the arm's normal—I'm computing the derivative of the ball's position with respect to θ to get the true velocity direction at release.

At 45° release, the launch angle works out to about 37.3° with speed proportional to 0.5245·ω, so I'll either adjust the stop angle or rework the speed to hit the target. Now I need to figure out where the bucket sits—its height, wall thickness, and the rim height the ball must clear to land inside, treating landing position at roughly x=3m from the start.

I'm aiming for the ball to cross the rim around 0.3-0.34m and settle near the bucket's base, around 0.2m, giving me the horizontal distance (~2.8m) and vertical drop (~0.717m) needed. Now I'm setting up the trajectory equation with tan and cos² of 37.3° to solve for the required velocity.

Working through this, I get v² ≈ 21.31, so v ≈ 4.617 m/s, which translates to an angular velocity of about 8.80 rad/s. I'm second-guessing this a bit though, since the arm's stop isn't instantaneous -- it decelerates gradually and the ball detaches somewhere during that process, plus the arm may swing a touch past 45°. Given the bucket is 50cm wide, I'm checking how sensitive the range is to velocity errors -- roughly dR/dv ≈ 2R/v, suggesting about ±0.25m of tolerance in range for a given velocity precision.

That tolerance feels tight (~4% on v), so widening the bucket to 80cm (with 30cm walls) gives more margin, around ±7%, which seems safer without being able to test empirically. I also briefly consider whether the arm itself could just be "launched" rather than spring-driven, but that feels like it defeats the purpose of a catapult that actually throws something -- so I'm sticking with the spring-based design and continuing to work out the required angular velocity.

I'm computing spring energy by integrating torque over the swing angle from 0 to 45°, then subtracting the gravitational potential gained by the arm, scoop, and ball as they rise, plus accounting for damping losses. I'm deciding to keep damping minimal, essentially negligible, since the spring will hold the arm against its stop after the throw anyway.

Now I'm working out the moment of inertia of the arm about the pivot, picking a 0.3 kg arm with given dimensions and computing its combined centroidal plus parallel-axis inertia, then starting on the scoop's contribution at its offset position.

I'll set armature to 0.002 instead. For the ball, picking 100 g mass and 4 cm radius, its distance² from axis gives 0.2753, so as a point mass that's 0.02753. I should also consider whether the ball rolls or slides outward toward the scoop back under centrifugal force during acceleration, since it starts with a 4 cm gap from the back wall.

Comparing the gravity component along the arm against centrifugal force at different angles, I'm finding that at 45° gravity pulls inward with about 6.9 m/s² while centrifugal force at ω=8.8 reaches 40 m/s², clearly dominating. So I'll assume the ball slides all the way out to rest against the back, putting it at r_ball = 0.56.

Rather than relying on "in catapult" which just centers the ball, I should position it explicitly relative to the scoop back — if the scoop back center sits at −0.605 in the arm frame and I want the ball centered at −0.56, that's roughly 4.5 cm ahead of the scoop back.

I'll go with "on catapult.scoop base, 4.5 cm ahead of catapult.scoop back," letting the across position default to 0 since the catapult sits at the origin. That puts the ball's edge at about −0.6, just touching the back face, which seems right.

Now I'm recomputing the moment of inertia for the ball: with r=0.559 and offset d=0.07, the distance squared comes to 0.3174, giving a point-mass inertia of 0.03174. Since the ball rotates rigidly with the arm (held against the back and base without slipping), I need to add its own spin inertia, 2/5 m R², to this.

Adding everything up, the total moment of inertia comes to about 0.079. Now I'm recomputing the release position and velocity direction at the 45° stop angle using the updated r and d values to work out the kinetic energy and launch speed.

I'm also checking whether the back wall interferes with the ball's tangential release trajectory — since the ball's velocity is parallel to the back wall face at release, it shouldn't be obstructed, but I need to confirm the vertical span of the ball against the 10cm wall height.

The arm's soft stop in MuJoCo will cause some overshoot given the timeconst and angular velocity, adding maybe 2-3° to the launch angle, but this is a minor effect on the roughly 38° exit angle. Now I'm turning to the bucket's position, roughly 3 meters from the starting point horizontally.

Computing the required launch distance and height drop to clear the bucket's near wall and land near its center, I'm solving for the velocity needed given gravity and the angle, arriving at a target of gD² ≈ 76.2.

Solving gives v² ≈ 20.64, v ≈ 4.543 m/s, and angular velocity ω ≈ 8.064 rad/s. Checking the trajectory at the near wall (x≈2.387 from release) gives z≈0.628, well clear of the 0.34 m threshold, but at the far wall (x≈3.187) the height drops to about −0.45, meaning the ball lands inside before reaching the far wall, which is expected since it should land in the bucket.

Finding where z crosses the base level (0.06) gives x≈2.852 from release, so the ball lands about 3.065 m from start, roughly 6.5 cm past center — well within the ±40 cm tolerance. Now checking where the trajectory crosses the rim height (0.34) on its way down to make sure it clears the rim properly.

Since the landing speed is fairly low (~6 m/s) and contact is mostly inelastic by default, I should avoid bounce-out by configuring the ball with a dead bounce so it settles in the bucket rather than rebounding over the wall.

Computing the decel from rolling friction gives about 0.7 m/s², which is manageable within the bucket's timeframe. Now I'm tallying the energy budget needed to reach the target angular velocity at 45°, factoring in kinetic energy and the gravitational PE gain of the arm and scoop as they rotate up.

Adding the ball's PE contribution and estimating damping losses around 0.07 J, the total PE change comes to about 1.102 J, so the full work required combines this with the kinetic energy and damping terms.

For the spring, I'm solving for stiffness k by targeting a reference angle of 90° so the spring provides torque over the 0-45° range, giving k ≈ 4.046 N·m/rad — though I pause to check whether the spring torque at the starting position (θ=0) would actually overpower gravity and cause unwanted motion before the intended release.

Summing gravity torques on each component (arm, scoop, back, ball) gives about 1.59 N·m opposing a net upward torque of 4.77 N·m, so the arm accelerates upward right away — which is the desired throwing motion, and the ball starts at rest as required. I'm now checking whether the resulting angular acceleration (~60 rad/s²) might cause the ball to slip relative to the scoop due to the large tangential acceleration at launch.

Checking the direction of the ball's required acceleration relative to the base and back wall, since the base only pushes perpendicular to the arm and initially there's no centripetal component needed, so the ball should stay seated without needing outward support from the back wall. I'm working through the geometry of the position vector (accounting for the small 7° offset) to find the exact direction of the ball's acceleration relative to the arm.

Comparing to the base's own acceleration (1.5 m/s²), the difference is small — the ball would roll just a few millimeters toward the pivot before centrifugal force later pushes it back, so it's negligible. I'm more concerned about whether the arm or scoop physically collides with the stand near the 45° stop, which needs checking against the stand height.

No collision at 45° since the ball's release trajectory (forward-up at 38° from x=−0.346, z=0.945) clears the pivot region well above the arm's far end. The arm decelerates while the ball flies ahead, so even if the arm bounces slightly off its soft limit, the ball is already clear by then.

That confirms the ball separates from the back wall correctly and moves away from the base too, so the release geometry checks out. Spin from the arm's rotation won't matter until the ball lands in the bucket since there's no Magnus effect in flight. I'm also double-checking the floor and stand geometry don't interfere with the arm's rest position.

With the MuJoCo joint starting at the 0° limit and the hinge axis set to y, rotating positive moves the near end of the arm upward in z while the scoop swings toward +x — exactly the forward-throwing direction I wanted for the catapult, so the mechanism orientation is consistent with the intended design.

The scoop sits just beyond the arm's end, extending past where the arm physically terminates, so it overhangs slightly unsupported but remains attached regardless. For the bucket, I'm working out placement as an open box with 80cm length and width and 30cm walls, positioning its base relative to the ball using the specified offset, keeping it centered across and resting on the floor since the component pieces default to floor-level placement within the part.

I'll treat "3 m from where the ball starts" as a horizontal distance rather than full Euclidean, since that's the more natural reading, though the vertical gap from the ball's starting height to the bucket's base near the floor would technically push the true distance slightly higher — I'll assume the checker uses horizontal distance. I also need to keep the write order correct: floor, catapult, ball, then bucket, and apply dead bounce behavior to both the ball and bucket.

The bucket base is 2 cm thick, so the ball rests at z = 0.06. After landing roughly 6.5 cm past center while moving forward at ~3.6 m/s, it should slide toward the far wall 34 cm away, hit it with a dead bounce, and come to rest quickly due to rolling friction — I also need to account for the ball's backspin from the arm's rotation, checking that the angular velocity direction matches rolling motion in the +x direction.

I'm confirming the dead bounce setup uses high damping, then working through the landing physics: computing vertical velocity at impact (~-5.01 m/s) and horizontal velocity (~3.585 m/s) at the steep landing angle, so the ball slides forward and strikes the far wall at about 3.5 m/s before the dead bounce absorbs most of the energy.

I'm sanity-checking whether 30 cm walls are tall enough — confirming the near-wall clearance works with some margin, and deciding to keep the 30 cm wall height rather than increasing it. I'm also stress-testing sensitivity: if spring force comes in 5% low, range drops enough that the ball could land near the edge of the bucket, so I'm checking the margins at both the near and far wall crossings to make sure it still clears safely.

Now I'm double-checking the arm dynamics — armature value, the MuJoCo spring torque model, and how the joint limit at 45° interacts with release timing, since a slight overshoot in launch angle shouldn't meaningfully hurt range near the 40-45° optimum. I'm also setting the arm mass to 300g with a wood appearance and giving the scoop a friction value of 0.8.

I'm settling on a 4cm radius, 100g ball, with damping around 0.02 N·m·s/rad, a spring constant near 4.05 N·m/rad pulling toward 90°, and arm swing range from 0° to 45°, pivot height 50cm and arm length 60cm. I'm also checking whether the stand geometry (a box roughly 16×24×44cm centered at the origin) might interfere with the arm's swing path.

Working out the ball's resting position relative to the scoop, placing it 4.6cm ahead of the scoop's back edge, I'm computing the x-coordinate accounting for the scoop's offset to make sure the ball sits correctly in the catapult before launch.

I'm nudging the spring constant up slightly (k=4.1) to account for unmodeled energy losses like rolling friction and contact softness, which bumps the kinetic energy slightly and increases the exit velocity by about 1%, keeping the bucket landing expectation intact.

Regarding the ball's motion during the arm's swing, I'm considering whether it separates from the back wall early on and then gets slammed back by centrifugal effect near the end — likely a small, dead bounce that doesn't change the outcome much. Time to write out the floor friction definitions and finalize the world setup.

