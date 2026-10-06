The catapult's arm lies flat at the start. Its hinge spring pulls toward 90°, which flings the arm up until it hits a stop at 38°. At that point the ball leaves at about 45° and about 4.7 m/s. A hand estimate of energy and flight puts its first landing near the centre of an 80 cm open bucket, 3 m ahead of where the ball starts. This estimate has not been run; if the ball lands long or short, `spring` is the value to adjust.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- The arm runs back (−x) from the pivot; a positive angle lifts the scoop end.
-- The spring pulls toward 90°, so the arm flies up from 0° and stops hard at 38°.
-- Scoop radius about 0.52 m, so the ball leaves at about 45° elevation and about 4.7 m/s.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 38°
  spring        5.2 N·m/rad toward 90°
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
  length  80 cm
  width   80 cm
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

I'm working out the catapult's physical structure—sizing the stand, pivot height, and arm dimensions so the throwing mechanism rotates correctly about the hinge point.

Thinking through the hinge rotation using the right-hand rule, I work out that a positive rotation about the y-axis lifts the scoop end up and forward, which matches how a real catapult launches: the arm starts tilted back, then swings forward and up, releasing the ball at an angle like 45° where the velocity vector points forward-up.

I confirm the ball travels in the +x direction, pushed by the scoop base whose surface normal also rotates forward-up, while centrifugal force naturally pushes the ball toward the scoop's back wall for containment. I'm now thinking about how the ball should start at rest positioned on the scoop base within the catapult's geometry.

Simplifying, I decide the arm starts at 0° (horizontal) with the spring tension pulling it toward 90°, so no awkward initial angle is needed -- the ball sits naturally in the scoop at rest, then the spring accelerates the arm until it hits the 45° stop and launches the ball. I'm now checking whether the stand's position could cause any collision with the swinging arm.

Unlikely to overlap regardless, so I'll move on. Now placing the ball at rest in the scoop near the arm's end, computing its position based on the scoop dimensions and pivot height, with some radius for the ball. Then I need the bucket's center positioned 3 meters horizontally from this starting ball position.

For the bucket I'll just place its base 3 m beyond the ball along that axis, letting the across and vertical positions default naturally since it's an open box resting on the floor.

Switching to absolute coordinates with L=60cm, so ball starts at x=−52cm, bucket at 2.48m. Now I need the launch physics: the ball's position relative to the pivot is (−0.52, 0.06), giving radius r≈0.523m, and the release velocity direction is perpendicular to this radius vector as the arm rotates through angle θ.

I work out the elevation angle offset: the initial radius vector sits 6.6° above the −x axis, so for a 45° launch angle the arm needs to rotate to θ≈38.4°. But the catch is that the ball doesn't release exactly at the stop angle -- when the arm hits the joint limit it decelerates abruptly, and the ball continues with whatever velocity it had at that instant, so I need to account for that transition more carefully.

So horizontal distance to bucket center becomes 2.85 m. I'm picking a target landing height around the rim top, roughly 0.3 m, assuming a bucket about 60 cm wide with 30 cm walls, giving decent tolerance. With pivot height at 0.5 m and release height 0.87 m, I need the ball to drop 0.57 m over that horizontal span.

Solving the projectile equation at 45° release, I get v ≈ 4.83 m/s, which translates to an angular velocity ω ≈ 9.23 rad/s. Now I'm second-guessing whether the ball truly leaves the arm at exactly this speed when it hits the mechanical stop, since the stop isn't instantaneous — the arm decelerates briefly while the spring continues applying torque right up until contact, so I need to account for the spring's energy input up to the stop angle rather than just assuming a clean release velocity.

I'm working through the energy balance: spring work input, minus gravitational work on the arm-scoop-ball assembly, minus damping losses, equals the kinetic energy at the stop. To get that kinetic energy I need the total moment of inertia, so I'm estimating each component — the arm itself, the scoop base, the scoop back, and the ball — computing each piece's contribution based on assumed mass and radius values.

Now I'm summing these to get a total inertia around 0.0825, then calculating gravitational work for each component by tracking how far their centers of mass rise as the arm swings through the stop angle.

Adding the scoop back and ball contributions brings total gravity work to about 0.95 J. Then I'm computing kinetic energy required at the target angular velocity (around 3.51 J) and starting to account for a small damping coefficient's energy loss.

Summing it all gives a required spring work near 4.53 J, which I use to solve for the spring constant via the integral of torque over the angle range, getting k ≈ 5.47 N·m/rad. I'm then checking the initial spring torque against the gravity torque from the arm and ball at the starting angle to see if it makes physical sense.

I'm also worried about the release moment — when the arm hits its stop, the ball needs to separate cleanly along the tangential direction (perpendicular to the arm), flying off the scoop base rather than catching on it.

But MuJoCo's joint limit is soft, so the arm likely overshoots the stop by a few degrees instead of stopping instantly. That overshoot matters because the ball actually separates earlier, right when the arm's deceleration first exceeds what gravity alone would produce, so its release velocity is close to ω times radius at that point rather than at the nominal stop angle.

After that, the arm bounces and settles while the ball just keeps flying — rolling versus sliding on the scoop doesn't change things since the arm's angular acceleration pushes the ball along the normal, not along the base, so there's no slip force to worry about. Air drag won't factor in unless explicitly enabled, and with a 3 cm ball landing at roughly 4.83 m/s into a 60 cm bucket, there's a real chance it bounces back out rather than staying in.

I should set both the bucket and ball to dead bounce so the ball settles instead of rebounding. Walking through the 45° trajectory: with vx=vz0≈3.415 m/s, it takes about 0.835 s to cover Δx=2.85 m, landing at height z≈0.30 m with descending velocity around −4.78 m/s — so I need to check where exactly it crosses the rim height relative to the bucket's 30 cm walls.

Checking the landing spot against the bucket's inner half-width of 0.29 m, it's landing about 0.2 m past centre, which is uncomfortably close to the far wall. I should probably retarget the throw so it crosses the rim closer to −0.1 from centre and lands nearer +0.1, or just make the bucket bigger (like 80 cm) to give more margin for error.

Recomputing with the larger 80 cm bucket and a flatter target height of 0.05 m at the bucket centre, I work out Δz = −0.82 and solve for v² ≈ 21.71, giving v ≈ 4.66 m/s and ω ≈ 8.91 rad/s. From there the kinetic energy comes out to about 3.275 J, so the spring needs to supply roughly 4.30 J once I add in the extra losses.

So k ≈ 5.19. I'm also weighing the uncertainties — a 5% error in energy translates to maybe 10 cm of range error, which the 80 cm bucket width (±40 cm) and 30 cm bucket walls should comfortably absorb, and I check that the ball's bounce dynamics (downward and horizontal velocity components) stay within the bucket's dead-bounce behavior. I also want to make sure the armature offset is set explicitly to 0.01 rather than left as default, since that could shift the pivot geometry slightly.

Checking the ball's flight path doesn't clip the stand or arm — the stand tops out at 0.44 m while the ball passes well above 1 m, so that's clear, and the arm itself has no forward protrusion to worry about after release. I'm also confirming the arm settles against its stop without problematic oscillation since the spring holds it there, and double-checking that the rotation direction convention (positive about the y-axis) matches what I intended for lifting the arm's far end.

I'll place the ball `in catapult`, relying on the scoop base being the hollow piece, and it should center there since the ball needs to move freely with rolling friction. For the bucket, I'm placing the open box on floor 3 m beyond the ball, using default centering across since only the along-axis is fixed by "beyond."

Checking heights: arm top at 2 cm, scoop base top at 3 cm, ball center at 6 cm with 3 cm radius, all level with the pivot assumption that the arm's far end sits there. Recomputing the ball's position relative to pivot gives a release angle θs of about 38°, rounding from 38.4°, which makes the launch elevation 45.4°—then I redo the coefficient k using θs = 0.663 rad, getting θ0θs − θs²/2 ≈ 1.0417.

I'm checking the ball's rotational kinetic energy if it rolls without slipping on the arm — it comes out negligible, around 0.0014 J, while the arm's moment of inertia about its end checks out to roughly 0.036. Then I start estimating the damping term using an average angular velocity of about 5 rad/s over the 0.663 s swing.

No joint frictionloss needed, and the soft contact between ball and scoop base should be fine despite some penetration. For the spring behavior, I'll use MuJoCo's springref toward 90°. With a 100 g ball of 3 cm radius, I expect the outcome to simply be the ball coming to rest in the bucket rather than something like the catapult hinge hitting its stop — keeping the description simple. I still need to add floor friction.

