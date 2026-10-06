The spring-loaded arm swings up and is stopped by its hinge limit at 34°, and the ball leaves the scoop at about 45° and 4.8 m/s. The bucket is a 1.2 m long open box whose centre is placed 3 m beyond the ball's starting point. I haven't run it; the numbers below are hand estimates.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- Spring-loaded arm: starts flat (0°), spring pulls toward 90°, hard stop at 34°.
-- Release ~34° gives a ~45° launch from the scoop; the ball needs ~4.8 m/s.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 34°
  spring        5.3 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.002 kg·m²
  colour        wood
  stands        on floor

ball
  is a      sphere 7 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    orange
  moves     freely
  rests     in catapult

-- Long open box so the landing has room either side of the aim point.
bucket
  is an   open box
  length  1.2 m
  width   80 cm
  walls   30 cm
  bounce  dead
  colour  grey
  its base 3 m beyond ball, on floor

expect
  ball comes to rest in bucket
```

How the numbers were set:

- **Required speed:** the ball leaves the scoop about 0.88 m up and 0.14 m ahead of where it starts. I aimed it to drop to about 20 cm height over the bucket centre, which needs about 4.8 m/s.
- **Spring stiffness:** that speed means about 3.0 J of kinetic energy, with a total moving inertia of about 0.076 kg·m². Lifting the arm, scoop and ball takes about 0.85 J, and damping loses a little more. That leaves about 4.0 J for the spring, so the spring is about 5.3 N·m/rad pulling toward 90°.
- **Margin:** the bucket still catches the ball if the speed comes out roughly 9% slow or 11% fast.

---
thinking (summarized):

I'm working out the catapult's physical layout since I can't simulate it directly—figuring out the stand dimensions, pivot height, and how the arm extends from that pivot point so the geometry makes sense for launching the ball toward the bucket.

Now I'm computing the hinge rotation math: using the rotation matrix about the y-axis to track how the scoop end moves as the arm swings from its rest angle upward, and deriving the velocity direction at each angle so I can figure out the launch trajectory at release.

So the ball needs to fly toward +x, meaning the bucket should sit along that direction. Since the ball starts at rest in the scoop and the arm swings via spring force until hitting a hinge limit, I need to roughly estimate the release angle and velocity to size and place the bucket appropriately — placing its center a few meters out along +x to catch the trajectory.

I'm picturing the geometry: pivot height around 40 cm, arm length 60 cm, ball resting near the end of the scoop with a small radius, trying to figure out the ball's starting position and height relative to the pivot so I can estimate its launch speed and angle once the arm swings into the limit.

I'm now thinking about the starting angle — if the arm begins horizontal, the ball sits at rest until the spring fires at t=0, so that should work fine without the arm needing a separate resting mechanism. But I'm reconsidering whether a negative starting angle (scoop tilted lower) would give the arm more swing distance and a better launch, checking that the geometry still clears the stand at that angle before placing the ball in the rotated scoop position.

Thinking through the launch mechanics: stopping the arm at 45° gives a tangential velocity perpendicular to the arm, but since the scoop's back wall sits on the outer side, the ball would actually separate from the base at that moment rather than being held against it — so I need to check whether the ball truly releases cleanly in the intended launch direction at the stop angle.

I should also account for real-world imperfections, like soft joint limits in MuJoCo causing some bounce or penetration at the stop, meaning the actual release angle could be a few degrees off from ideal but within acceptable tolerance. Now I'm setting up the geometry to compute the required launch speed, defining the ball's position relative to the pivot in terms of arm length and perpendicular offset.

As ω increases, centrifugal force dominates and pulls the ball outward until it settles against the scoop back around r≈0.55 at release, rolling along the arm. I'm now working out the velocity of the ball at release, accounting for the rotation geometry with the small offset d≈0.07 from centre, setting up the position transform under rotation by θ.

Computing release angle and velocity components, I get vx≈0.438ω and vz≈0.339ω at θ=45°, giving a launch angle around 37.7°, which is lower than the target ~43°, so I'm checking θ=50° instead to see if that gets the trajectory closer to the desired launch angle.

Computing release position relative to pivot gives roughly (-0.39, 0.39) above it, assuming the ball stays centered at radius 0.52 from pivot—though I'm not fully certain it stays fixed there. The scoop itself is 16 cm long, and since I can't modify the library part directly, I may need to define my own catapult part with a smaller scoop so a 14 cm diameter ball fits appropriately without sliding freely.

With a ball radius of 7 cm, it can only shift about 1 cm in the scoop, so I'm working out the scoop back height and ball center position: the back rises 10 cm above the arm, placing the ball's center at a height where the back still comfortably covers it, giving r ≈ 0.525 from the pivot. Since the ball is fairly large, the bucket will need to be sized accordingly, maybe around 80 cm, to properly catch and hold it at rest.

Now I'm recomputing the geometry with r=0.525 and offset d=0.10: the tilt angle works out to about 10.8°, so for a 45° launch I need a release angle of roughly 34°. I'm tracking through the arm thickness and pivot surfaces, then computing the ball's exact release position relative to the pivot using the rotation—getting x' ≈ -0.379 and z' ≈ 0.377—before moving to figure out the ball's actual starting coordinates in the scoop.

I'm finishing the launch angle calculation (around 45.2°) and the speed formula tied to angular velocity and arm length, then setting up the bucket placement problem: positioning the catapult at the origin on the floor, placing the ball's starting x at roughly -0.52, and now working out where to put the bucket center so the ball lands inside it.

I need to figure out how to express the bucket's position relative to the ball — using a clause like "its base 3 m beyond ball" to fix the horizontal offset, then "on floor" to fix height, while being careful about build order (floor, catapult, ball, bucket) and whether the stated 3 m distance is horizontal or a full 3D distance accounting for the ball's starting height above the pivot.

Now I'm working out the bucket's dimensions and the ball's landing trajectory, aiming for the ball to clear the rim and land roughly at the bucket's center position around the rim height.

I should think about how MuJoCo's soft joint limit actually behaves — the arm penetrates the limit by some amount before decelerating, which affects the release angle and velocity of the ball. Without the limit, the spring would just pull the arm back toward equilibrium and the ball would separate once the tangential deceleration exceeds gravity's component along the arm's path, which gives a more natural release condition to model.

I'm working through the energy balance for the arm's rotation from 0 to 34°, accounting for spring work, gravitational potential rise, and a small damping term, to get the kinetic energy and release angular speed. Then I'm setting up the launch position and target coordinates to solve for the required projectile speed so the ball reaches the bucket.

Choosing a pivot height of 0.5 m gives a release height and target drop that I plug into the 45° projectile equation, solving for the speed-distance relation needed to hit the target.

Working through the arithmetic, I get v² ≈ 23.69, so v ≈ 4.868 m/s at roughly 45.2°, which is close enough to ignore the small angle deviation. From there I find the arm's angular velocity ω ≈ 9.109 rad/s, but I need to account for the ball's own spin too — since it's pressed into a scoop and rotates with the arm, its rotational kinetic energy (using the solid sphere moment of inertia 2/5 mR²) adds to the point-mass kinetic energy, so I should include that in the total energy budget.

Now I'm assigning plausible masses to the pieces: a 0.3 kg arm (60×6×4 cm box), a 20 g scoop base, 10 g scoop back, and a 100 g ball with 7 cm radius — treating it like a light plastic ball, with no air drag to worry about. Then I start computing the arm's moment of inertia about the pivot, breaking it into the box's centroidal inertia term plus the parallel-axis contribution from its offset.

Setting armature explicitly to 0.002 kg·m² instead of the large default, giving total I = 0.07598.

Required KE works out to about 3.153 J using ½Iω² with ω=9.109.

Now I'm computing the gravitational PE rise for each mass as the arm swings to θ=34°, using the rotated height formula Δz = -x sinθ + z(cosθ-1), starting with the arm's center of mass.

Summing contributions from the base, back, and ball gives a total mass-weighted height change of 0.08694 kg·m, so PE rise ≈ 0.853 J.

For damping, I'm trying a coefficient of 0.05 N·m·s/rad, estimating energy loss as roughly c times average angular velocity times angle traveled, which comes out around 0.15 J — though I suspect I should reconsider the damping value.

Dropping damping to 0.02 and estimating average ω as about two-thirds of the final velocity (~6.1 rad/s), the loss comes to roughly 0.072 J. Adding gravity PE (0.853 J) plus damping loss (0.072 J) to the kinetic energy requirement (3.153 J) gives a total spring work needed of about 4.078 J, and I'm now setting up the spring work equation using θ_s = 0.5934 rad, picking an equilibrium angle θ_eq of 90° (1 rad) to solve for k.

Using θ_eq = 1.5708 rad instead, I get k ≈ 5.394 N·m/rad from the work equation, and checking torque at θ=0 (about 8.47 N·m) against the gravity torque on the arm (~1.56 N·m) confirms the spring can initiate motion. Now I need to reconcile this with the stated "spring 40 N·m/rad toward 0°" setup and figure out whether MuJoCo's springref should be set relative to qpos0 given the arm starts at 0°.

I'm checking whether the ball cleanly separates during the swing — angular acceleration comes out to roughly 90 rad/s², giving tangential acceleration around 47 m/s² at the ball's location, while centrifugal effects push it outward against the scoop's back wall by about a centimeter, which seems physically reasonable for keeping the ball seated until release.

At release, the ball's velocity is perpendicular to the arm, matching the scoop's orientation so there's no interference as it separates. The remaining concern is the soft limit stop: when the arm hits its limit it may rebound slightly, and I want to confirm the ball is already far enough away by the time the arm springs back up that it doesn't get struck again.

Checking whether the ball clears the pivot stand - tracing its trajectory relative to the arm at 34° confirms it passes comfortably above the pivot with margin, even accounting for gravity. I also want to verify the scoop geometry itself (ball radius 7cm vs scoop base 16cm) is consistent with the back wall's starting position near the pivot end.

Now I'm checking whether the arm collides with the support stand as it rotates from 0°. The stand top sits at 0.44 and the arm bottom at 0.48, so there's clearance, but I need to trace the pivot-end corner of the arm as it sweeps upward to make sure no part of it dips into the stand's footprint during rotation.

I'm also considering whether MuJoCo's automatic parent-child contact exclusion applies here, since the stand is anchored to the world body and the arm is a sibling body connected through its own joint rather than directly to the stand.

Checking the ball's starting placement, it rests properly inside the scoop with its bottom touching the base. Then I work through the projectile trajectory numerically: at release angle 34° and launch angle 45.2°, computing time-of-flight and landing height confirms the ball lands near z=0.349, matching expectations, and I test sensitivity by bumping speed 5% to see how the landing point shifts.

I find speed variations shift the landing point by about ±0.25 m, which comfortably fits within the bucket's inner half-width tolerance of roughly ±8% speed variation. Now I'm considering whether the arm's limit softness could cause the ball to release slightly later than the ideal 34° due to gradual deceleration near the joint limit.

The ball should behave as rigid with the arm while rolling in the scoop, so I can treat small energy losses from sliding or rotation as negligible. Checking the trajectory, the ball enters the bucket at roughly 54° below horizontal with enough downward velocity that it should land near center and stay contained within the 30cm walls without bouncing out.

I should check that the ball clears the near wall at the right height, then verify it reaches resting height exactly at the bucket's centre, accounting for the wall's exact position and thickness so the ball's edge clears it with margin.

Trying a target height of 0.2 at the centre gives a short-side tolerance around -6% and long-side tolerance around +6.5%, though I need to double check what happens if the ball passes above the far wall but still falls short of clearing it entirely.

Extending the bucket to 1.2 m long and 0.8 m wide, keeping it centered at 3 m, should give roughly ±8% tolerance on both the near-wall clearance and far-wall entry height, since lateral motion isn't a factor here.

Redoing the target with Δz = −0.6765 and Δx = 2.86, I solve for required launch speed: v² ≈ 22.69, so v ≈ 4.76 m/s, giving ω ≈ 8.91 rad/s. Kinetic energy works out to about 3.02 J from rotation, plus roughly 0.85 J and 0.07 J from damping, totaling around 3.94 J — which gives a spring constant k ≈ 5.2 N·m/rad aimed at 90°.

I'm double-checking whether damping accounted for the armature term I already included, and confirming other energy sinks like ball rolling friction and contact compliance are negligible. I'm also testing sensitivity by shifting the ball's centrifugal position slightly and recomputing for a 1.2 m bucket case, working out the required Δx and Δz to get the velocity-squared relation for that shorter configuration.

For the short case, I get v≈4.344, about 8.8% below the baseline. For the long case—ball clearing the far wall near its inner face below the 0.30 height limit—I compute v≈5.309, about 11.5% above baseline, and conclude hitting the far wall at that height is fine since it stays dead rather than bouncing back up.

Given that tolerance band of roughly -17%/+24% in kinetic energy terms, I'm nudging the spring constant upward to around 5.3 to center things better, recomputing KE and confirming the velocity ratio comes out close to 1.01 — a good balance point. I also want to check the soft hinge limit behavior in MuJoCo near 34°, since the limit force's time constant of about 0.02s could matter at the angular velocities I'm working with.

Actually the arm only travels about 10° before the constraint kicks in hard: the soft constraint's damping term produces an immediate large deceleration force (on the order of hundreds of rad/s²) even before significant penetration builds up, since the reference acceleration depends on velocity directly through the solref parameters. That means the ball at its release radius experiences deceleration comparable to or exceeding gravity almost instantly, which determines exactly when it separates from the arm.

Given the arm's swing range from 0° to 34°, the ball releases right near that 34° endpoint, while the arm itself continues rotating a few more degrees into the joint limit before fully stopping — but by then the ball has already separated since the arm decelerates faster than the ball can follow. I also need to check that this 34° figure is measured in the same reference frame as the arm's defined starting rotation, which it should be.

For the landing behavior, I'm thinking through how the ball settles inside the 1.2 x 0.8 bucket — bouncing briefly, then rolling with a small rolling friction coefficient until it comes to rest within a several-second window.

That stops in roughly 1.2s, so maybe I should bump rolling friction up to 0.01 for the ball. Checking the spin direction too: positive rotation about y means the top of the ball moves forward in +x, consistent with forward rolling motion, though the actual spin of 8.9 rad/s is much slower than the 68 rad/s pure rolling would require at that speed — so it's mostly sliding initially.

Now for the bucket placement, I'm thinking through how to specify its position relative to the ball using "its base 3 m beyond ball, on floor" so the part's internal pieces shift together, keeping it resting on the floor. Since "beyond" only affects the along-axis, the across position defaults to zero, meaning I need to confirm whether the ball's y-coordinate is also zero for alignment.

Then I move to defining a catapult part with pivot height, arm length, arm mass, swing range, spring stiffness toward a target angle, damping, and armature inertia, specifying it stands on the floor -- noting that since it's not nested inside another part, its default orientation stays at zero without needing extra positioning.

For the ball, I define it as a sphere with radius and mass, giving it rolling behavior, dead bounce, friction and spin/roll coefficients, free movement, and placing it resting inside the catapult's scoop base -- working through how the "in" syntax resolves to the correct hollow part when referencing the catapult versus explicitly naming the scoop base.

I'll keep damping around 0.02 and confirm the arm settles against its stop after the spring drives it up from the starting rest position. I'm checking that friction between the ball and scoop base works correctly during acceleration — the tangential push presses the ball into the base while centrifugal force slides it outward and back, with friction letting it roll rather than hitting the arm or bucket wall. Now I'm double-checking the ball's starting position coordinates.

Spring work calculation checks out: k(θeq·θ − θ²/2) ≈ 4.007 J, confirming "toward 90°" means spring reference at 90°. Good enough to finalize — I'll proceed to write up the solution.

