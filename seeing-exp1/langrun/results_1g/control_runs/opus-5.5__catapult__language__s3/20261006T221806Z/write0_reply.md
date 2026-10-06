The arm starts flat against its lower stop. A spring pulls it up, and at 45° it hits its upper stop, so the ball flies off at about 4.5 m/s, rising at about 38°.

The spring stiffness comes from an energy balance:
- **Turning inertia** of arm, scoop, ball and armature about the pivot: ≈0.111 kg·m².
- **Lifting the parts** from 0° to 45° costs ≈1.52 J.
- **Kinetic energy** at release: ≈3.56 J, for ω ≈ 8.0 rad/s.
- **Spring:** pulling toward 180°, it must supply ≈5.08 J, which gives k ≈ 2.355 N·m/rad.

The ball starts against the scoop's back wall, 56 cm behind the pivot. It leaves the scoop at about 95 cm high. Its path passes over the bucket's centre, 3 m from its start, at about 12 cm high. That is inside a 70 cm bucket with 25 cm walls, and the ball's dead bounce keeps it in.

These are hand calculations; I haven't run the world. The range comes out within roughly ±7%, set by the bucket's size.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      500 g
  swings        from 0° to 45°
  spring        2.355 N·m/rad toward 180°
  damping       0 N·m·s/rad
  armature      0.01 kg·m²
  colour        wood
  stands        on floor

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    70 cm
  width     70 cm
  walls     25 cm
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.01
  colour    grey
  stands    on floor, its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the physics and geometry for a catapult that needs to launch a ball roughly 3 meters into a bucket, starting with the stand and pivot dimensions and figuring out how the arm extends from the pivot point.

Now I'm placing the scoop on the near end of the arm and working through the rotation math about the hinge axis — confirming that rotating the arm about the y-axis swings the scoop upward and over, launching the ball in the +x direction, which tells me the bucket needs to sit on the +x side. I'm also thinking through how the arm should start cocked back before the spring releases it.

For the ball's initial placement, I'm reasoning that it's simplest to keep the "starts turned" angle at zero so the arm sits horizontal at the start, letting the ball rest naturally in the scoop without worrying about keyframe or qpos0 complications — then the spring can pull the arm toward a higher angle like 120° to fling it.

Working through the release physics: with range roughly 0° to 45°, the arm accelerates from horizontal and hits its stop at 45°, releasing the ball with velocity perpendicular to the arm, which at that angle points 45° above horizontal toward +x. I'm computing the scoop's position at that stop angle to find the ball's launch coordinates, then placing the bucket center 3 meters horizontally from that starting point. I'm also considering that the hinge limit acts as a semi-rigid stop, meaning the arm might bounce slightly while the ball continues on its tangential path, and thinking through how the scoop's back wall geometry affects the ball as it slides forward relative to the decelerating arm.

Since the base normal at 45° aligns exactly with the velocity direction, the ball lifts cleanly off the scoop without any sideways drift — a clean release. I'm now reasoning about the centripetal forces during acceleration: the ball gets pushed outward along the arm toward the near end, away from the pivot, while the scoop's back wall sits at the far-out position to contain it.

Now I need to work out concrete numbers — launch angle of 45°, release height, and where the ball should land. I'm sketching out a bucket roughly 50 cm square with 30 cm walls, sized so the ball comes to rest inside after landing.

Let me pin down the geometry: a pivot at 50 cm, a 60 cm arm, a 4 cm radius ball, and a scoop base around 16x16 cm positioned so the ball starts centered over it at a reasonable height before launch.

Now I'm working out the ball's position and velocity at a 45° arm rotation, computing its offset from the pivot, the radius vector magnitude, and the resulting launch height and velocity direction once released.

So horizontal distance to target is about 2.80m, landing around z=0.2m to drop into the bucket. I'm setting up the projectile equation relating the drop to launch angle and speed, plugging in tan and cos² of the 37.3° angle to solve for the required velocity.

Working through the algebra, I get v² ≈ 21.3, so v ≈ 4.62 m/s, which gives ω ≈ 8.80 rad/s at the arm's radius. I'm checking that the ball separates right at the joint limit since the spring keeps accelerating the arm the whole way, so the release speed should indeed be the speed at the stop — though I need to consider how MuJoCo's soft constraint at the limit might affect that.

I'm worried about precision though, since the final speed is quite sensitive to spring energy, arm inertia, and other parameters. With a 50cm-wide bucket at 2.8m range, that's only about ±9% tolerance on range, meaning I need roughly ±4.5% accuracy on speed — tight but maybe a wider 60cm bucket would help. I also need to decide on hinge damping; I'll just set it to zero or something negligible since the problem seems to require specifying some value.

Now I'm working through the moment of inertia calculations for the arm assembly — computing the arm's mass distribution, the scoop's contribution, and summing everything about the pivot axis to get a total rotational inertia I can use in the energy balance.

Adding the ball's own rotational contribution since it moves with the arm without slipping, giving about 6.4e-5. I also need to decide whether to include the armature's default inertia of 0.01 kg·m² — I'll keep it included rather than zeroing it out. Summing everything gives a total moment of inertia around 0.106842, and now I need to work out the gravitational potential energy change as the arm rotates from 0° to 45°.

I'm computing each component's height change using the rotation transform, then multiplying by weight to get the energy contribution — doing this for the arm, scoop base, and scoop back sections separately.

Then I sum these into a total potential energy of about 1.49 J, add in the kinetic energy needed (0.5·I·ω² ≈ 4.14 J), giving a total required spring work of roughly 5.63 J. Now I'm setting up the spring torque equation using the target angle as the spring reference, integrating the torque from 0° to 45° toward that target to find the work done.

Picking a spring target of 180° (π rad), I compute the required spring constant as roughly 2.6 N·m/rad, then check that the initial spring torque (~8.19 N·m) plus gravity torque (~2.14 N·m) gives a positive net torque so the arm actually lifts off from rest.

Since the arm starts right at the lower limit of its 0°–45° range, the spring launches immediately at t=0 with the ball at rest in the catapult, which seems fine. I'll set hinge damping to zero and estimate the initial angular acceleration at around 56 rad/s² from the net torque divided by moment of inertia.

Checking the ball's position against the base geometry — centrifugal acceleration reaches about 40 m/s² outward by the end of the swing, and the back wall (10cm tall) sits at the right height to catch the ball's center. I'm verifying the ball starts with enough clearance from the back wall given its radius and the base dimensions.

I'm assuming across position defaults to centre (0) unless specified, trusting that to hold. I'm checking whether placing "on catapult.scoop base" still works given the base is attached to the arm, but since positions are set in the initial configuration it should be fine, and the ball's exact contact with the back wall shouldn't cause issues beyond a small initial push. Now I need to work out the catapult's own placement — its stand sits on the floor with the pivot offset upward, and the along-position likely defaults to 0, so I'm figuring out the ball's absolute starting x-coordinate relative to that.

Checking the rotation geometry near the pivot confirms the arm clears the stand with minimal dip, staying above 0.48m even at the corners. The far end hangs over the floor safely at that height, so I'm good there. Now recomputing the ball's position gives x=-0.56, z=0.07, with r² = 0.3136.

Adding the offset term brings r² to 0.3185, giving r ≈ 0.5644, and the ball's moment of inertia works out to 0.031914. Summing all components—arm, stand, ball, pivot—total system inertia is about 0.111162.

Rotating the ball to θ=45° places it at roughly (-0.3465, 0.9455) in absolute position, with velocity direction perpendicular to that radius vector, proportional to (0.4455, 0.3465) for positive ω.

Now I'm computing the launch angle: α = atan(0.3465/0.4455) ≈ 37.87°, with cos² ≈ 0.6230 and tan ≈ 0.7778. I'm setting up the target bucket location (centered 3 m from the pivot) and working out the horizontal distance the ball needs to travel from release to reach the bucket's center, accounting for bucket dimensions and wall height for the landing calculation.

I need to figure out the descent angle so the ball crosses the rim and lands within the bucket's margins, checking against the near and far wall positions to ensure enough clearance on both sides given the ball's radius.

Given the tight tolerance (~±4% range, ±2% speed), I'm considering adjusting the bucket size or wall height to loosen the margin — maybe going with a 70 cm bucket with 30 cm walls, or shrinking the wall height to lower where the ball crosses the rim.

Settling on a 70 cm bucket with 25 cm walls, aiming the pass centre at z=0.12. Working through the projectile equations: solving for v² and v from the angle and displacement terms gives v≈4.52 m/s, which translates to ω≈8.0 rad/s, then I'm checking the descent by breaking velocity into its horizontal and vertical components.

Tracking the vertical velocity at the rim shows a descent angle near 53.9°, so I'm figuring out where the ball crosses the plane of the near wall's inner face to confirm it clears the rim height before reaching the bucket's edge.

Checking the landing margins on both the early and late side of the bucket, the ball stays within tolerance even with a fair speed error, roughly ±3.5%. After landing, the ball will likely roll and bounce once against the far wall, but the 25 cm walls should keep it contained within the bucket.

Now recomputing the energy: finding the ball's potential energy at the landing point gives about 1.52 J total, and the kinetic energy works out to roughly 3.56 J. Adding in rotational contributions, I get total work of about 5.08 J, and dividing by the angular displacement gives a spring constant near 2.35 N·m/rad — now I need to solve for the initial angle θ1.

I should check how sensitive this result is to errors: since velocity scales with the square root of kinetic energy, errors in inertia feed through roughly linearly. I also want to confirm MuJoCo's assumptions about mass and inertia — the scoop's box inertia from its given dimensions and mass, and the ball's inertia as a solid sphere derived from its given mass, both seem consistent with the setup.

As for the joint limit stop, with default solver parameters the arm decelerates over roughly 20ms, overshooting the 45° limit slightly before settling back. The ball likely separates right around that moment as the base decelerates, so its velocity direction corresponds closely to the nominal 45° angle, though the small overshoot could shift the effective launch angle to something like 37.9° instead of exactly 45°.

Checking the ball's velocity relative to the decelerating base, I'm computing the dot product with the outward arm direction and finding a small negative component, meaning the ball moves slightly inward toward the pivot rather than toward the back wall — which is good, since that means it separates cleanly. The dot product with the base normal direction comes out positive too, confirming the ball moves away from the scoop surface correctly.

Then I'm checking the spring versus gravity torque at the 45-degree stopping point and confirming the spring torque still dominates, so the arm keeps accelerating right until it hits the limit, meaning the ball stays pressed against the base throughout the swing. I'm also verifying the initial resting geometry — base top height, ball center height, and the resulting offset in the arm's local frame — to make sure the ball starts properly seated. I note I still need to confirm the joint limit requires the "limited" attribute to be set for MuJoCo to enforce the range correctly.

The scoop base placement extends slightly past the arm's physical end, but since it's still mounted at the correct height it should be fine, and I compute its inertia using its actual offset center. For release dynamics, I calculate the ball's apex height from its vertical velocity at launch, and decide not to add air drag unless explicitly required. Finally I start checking whether the ball's post-release trajectory might clip the catapult stand or arm as it arcs upward and forward over the pivot.

Now I'm figuring out how to position the bucket relative to the ball, using phrasing like "its base 3 m beyond ball" so the box's position is defined by offsetting from the ball's location along the forward axis, keeping it centered across.

Then I need to establish ordering: floor, catapult, ball, bucket, since the ball's resting position depends on the catapult's scoop end. I'm placing the ball at the near end of the catapult's scoop base, likely defaulting to zero lateral offset, confirming the scoop reference fixes the along-axis position without interfering with height. I also note the 3 m distance should represent the horizontal gap from where the ball starts.

For the catapult part itself, I'm defining its physical parameters: pivot height of 50 cm, arm length of 60 cm, arm mass of 500 g, rotation range from 0° to 45°, and spring force of 2.355 N.

Now I'm working through the spring and damping setup — using springref at 180° for MuJoCo's hinge joint, setting damping to zero for simplicity, and checking that having the arm start exactly at its 0° limit won't cause constraint issues given the default zero margin. I'm also starting to think about rolling friction for the ball.

Colour is optional and can apply uniformly across pieces. I'm verifying the final resting state description ("ball comes to rest in bucket") and recomputing the arm's inertia — a 60×6×4 cm box about the y-axis gives roughly 0.015 from the box term plus 0.045 from the parallel-axis shift at 0.30 m, totaling about 0.060 kg·m². I'm also confirming the arm's far end sits right at the pivot where the hinge is placed.

Minor numerical softness in contact solving or slight sinking at the ball-base contact is negligible, and the bucket position doesn't conflict with the catapult arm's swing. I'll set the floor to a generous 8 m half-extent and move on to writing the world definition.

