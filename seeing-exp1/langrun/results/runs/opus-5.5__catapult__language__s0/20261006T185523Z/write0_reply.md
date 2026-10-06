The catapult arm swings 40° on a spring and hits its stop, which releases the ball at about 4.8 m/s. The bucket's base is centred 3 m along from where the ball starts.

How I sized it (hand calculation only, not simulated):

- **Release.** The ball sits 42 cm out and 6 cm up from the pivot. A 40° stop therefore sends it off at about 42° elevation. Near 45° the range barely changes, so a slight overshoot past the stop costs little distance.
- **Speed needed.** The ball leaves about 0.82 m up and 2.86 m short of the bucket centre. To pass through mid-bucket height there, it needs about 4.8 m/s, which is about 11.3 rad/s at the scoop.
- **Spring.** Spinning up the arm, scoop, ball and armature (about 0.059 kg·m² in total) takes about 3.8 J. Lifting them takes another 0.8 J. A spring of 5.5 N·m/rad pulling toward 90° gives about 4.7 J over the 0–40° swing, enough for both plus the small damping loss.
- **Bucket.** It is 80 cm square, so the ball can miss its centre by about ±0.35 m, roughly 12% of the range. It is dead-bounce so the ball settles inside.

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
  spring        5.5 N·m/rad toward 90°
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
  colour  wood
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

Since I can't simulate this, I need to reason through the physics carefully. I'm planning the catapult structure: a stand box supporting a pivot point, with an arm hinged at that pivot extending backward, and a scoop attached to the throwing end to hold and launch the ball toward the bucket 3 meters away.

Working out the rotation math, I confirm that swinging the arm with a positive angle about the hinge axis lifts the scoop from behind the pivot up and over to launch forward in the +x direction. Now I'm thinking through how to actuate the throw — likely using a spring that pulls the arm toward a target angle, with the ball releasing from the scoop once the arm decelerates or hits a stop, though I need to be careful since joint limits in this physics engine act as soft constraints rather than hard stops.

For maximum range, 45 degrees looks like the natural release angle, since the velocity direction of the scoop tip at that point is oriented perfectly up-and-forward. I'm also checking how tangential acceleration during the swing presses the ball against the scoop's base, which keeps it seated until release.

I need to confirm the spring preload is strong enough to overcome gravity at the starting position, and that the hinge limits (0° to 45°) make sense with the spring biased toward holding the arm against its upper stop. Now I'm setting up to calculate the actual release velocity based on pivot height and arm length geometry.

Working out the ball's resting position on the scoop base — stacking up the arm thickness, scoop base thickness, and ball radius to get its center height, then figuring out the right placement clause (`on` vs `centred over`) to position the ball correctly on the catapult's scoop base.

Working out the ball's center position relative to the pivot, accounting for the scoop base's near edge and a radius offset, giving roughly (−(L−0.08), 0.06). I'm also considering where the catapult itself sits — likely at the origin on the floor — before figuring out how to position it as a whole relative to the ball.

For the bucket, I'm thinking of placing its base 3 m beyond the ball along the horizontal axis, letting the across-position default to zero (in line with the catapult) and the height default to resting on the floor, since "beyond" only fixes one directional offset.

Now I need to size the bucket: say 60 cm square with 30 cm walls, giving the ball (3 cm radius, walls 2 cm thick) a landing tolerance of roughly ±0.25 m horizontally at a rim height of 0.3 m. From there I'm working out the launch trajectory — pivot height, arm length, and release angle near 45° — to figure out where the ball's position is relative to the pivot at the moment of release.

Then I compute the release velocity from the arm's angular speed and the radius vector to the ball, using the perpendicular relationship between position and velocity components during rotation.

Trying L = 0.5 m: with a = 0.42 and d = 0.06, the release position relative to the pivot works out to roughly (−0.2546, 0.3394), and the velocity direction normalizes to (0.8, 0.6), giving an elevation angle of about 36.87°.

I realize the elevation depends on both the stop angle θ and the initial offset angle φ = atan(d/a) ≈ 8.13°, roughly as elevation = 90° − (θ + φ). With θ = 45°, that gives 36.87° as computed; to get closer to 45° elevation I'd need to stop earlier, around θ ≈ 36.87°, though I could also just accept the 36.9° elevation from a 45° stop and adjust speed requirements accordingly.

I'm leaning toward stopping at θ = 40° instead, since a soft limit means the arm overshoots slightly and the ball departs mid-deceleration, which lowers the effective elevation a bit further anyway — lower elevation also makes the trajectory more sensitive. I also confirm the ball leaves the scoop smoothly, lifting off tangentially along the local "up" direction of the arm when it stops, with only minor friction/spin effects from the back of the scoop. Now I'm recalculating the geometry with θ=40°, a=0.42, d=0.06 using cos40° and sin40°.

Working out the release point gives x' ≈ -0.283 and z' ≈ 0.316 relative to the pivot, so with ball start at x=-0.42 and pivot height h, the release position is x=-0.283, z=h+0.316. Setting the bucket center at x=2.58 (pivot +3m), the horizontal distance from release to bucket center comes out to about 2.863 m, and if I choose h=0.5 with a target entry height around z=0.25, the release height becomes 0.816.

Using an elevation angle of about 41.87° (tanα≈0.897, cosα≈0.744) and plugging into the projectile range equation, I solve for the required launch speed and get v²≈23.16, so v≈4.81 m/s. From there, with the swing radius ρ=√(0.42²+0.06²)≈0.4243 m, the angular velocity at release works out to ω≈11.35 rad/s. Now I need to move to the energy balance involving the spring torque constant k.

Continuing the moment-of-inertia calculation, I'm adding the scoop base and scoop back components, computing each piece's distance from the pivot and parallel-axis contribution before summing toward a total system inertia.

I'm adding the armature's own moment of inertia, then treating the ball as a point mass at its radius with a small rolling-inertia correction, and summing everything to get a total I of about 0.0593 kg·m². Now I'm moving on to compute the kinetic energy using this inertia value.

For potential energy, I'm tracking how the arm's centre of mass and the scoop's base and back points rise as the arm swings through 40 degrees, computing each height change and converting it into PE contributions.

Scoop back rise gives PE = 0.0302 J, the ball's rise contributes PE = 0.251 J, bringing total PE to 0.806 J. Then I'm estimating damping losses roughly at 0.04 J, so the spring needs to supply work around 3.818 + 0.806 + 0.04 ≈ 4 J total.

Picking θ0 = 90°, I solve for the spring constant k using the energy equation, getting k ≈ 5.47 N·m/rad. Checking torque balance at θ=0, the spring torque (8.59 N·m) comfortably exceeds the combined gravity torque from the arm, scoop, and ball (about 1.28 N·m), so the design holds up — though I still need to verify the ball stays seated in the scoop throughout the motion.

The ball stays pressed against the scoop base during acceleration since the arm's tangential push dominates gravity, and centripetally it's held by the scoop back as it tends to fly outward. Near release at 40°, as the arm decelerates via the soft limit, the ball continues at its release velocity and separates — I need to check its trajectory relative to the scoop back to confirm clean separation.

Thinking about sensitivity: a 5% velocity error shifts range by about 10% (~0.29 m), which is risky against a narrow bucket. I'm widening the bucket to 80 cm with 30 cm walls, giving roughly 12% tolerance on ball center position — much safer. I also need to account for wall height, since the ball descends at a steep ~50° angle and must clear the rim at around 0.33 m height; I should refine the aim so the ball crosses that height near the bucket center.

As for the landing dynamics, if the ball crosses rim height at roughly center−0.12 m and continues at the same descent angle, it should settle near center+0.12 m at the base, comfortably clear of the near wall at center−0.38 m — so aiming for about 0.25 m height at the center looks right. I'm also considering making the ball's bounce "dead" so it settles in the bucket rather than bouncing back out, which shouldn't interfere with the throwing physics itself.

Now I'm checking whether the catapult arm clears the stand at a 40° launch angle — with the stand's top at 0.44 and the arm's pivot-side bottom at 0.48, I need to trace the rotated corner position of the arm's far end to confirm it doesn't clip the stand as it swings upward.

I'm also verifying the ball's resting position in the scoop (x=-0.42, z=0.56) stays clear of the scoop's back wall, and checking what happens to the arm's sag at the 0° starting angle under gravity before launch.

Then I need to work out the bucket's placement: its base centre should sit 3m horizontally beyond the ball's starting x-position, which gives x = 2.58. I'm using the ball's starting x as the reference for the trajectory distance calculation too.

For the scoop and ball placement on the arm, I'm confirming the ball sits just above the pivot level at the arm's near end. Finally I'm setting the catapult parameters: 50cm pivot height, 50cm arm length, 300g arm mass, swing range 0° to 40°, spring constant 5.5 N·m/rad toward 90°, and damping 0.01 N·m·s/rad.

Checking the limit softness — with the arm moving at roughly 11 rad/s, there's likely some penetration past the 40° limit, meaning the ball releases at slightly higher than 40°, which actually helps since the elevation near 42° is near the insensitive region for max range. The ball may pick up some spin from friction during release, but that shouldn't matter. I'm finalizing the ball as 100g, 3cm radius sphere, and the bucket as an 80cm×80cm open box with 30cm walls — color isn't important here.

With a dead bounce, the ball should settle near the bucket's base without overshooting the walls. I'm now placing the ball at rest in the catapult and positioning the bucket's base about 3 meters beyond it, along with appropriate floor friction.

