The catapult's arm starts flat against its lower stop. A spring pulls it toward 90°, so it swings up at once and hits its stop at 40°. That releases the ball at about 43° elevation and about 4.8 m/s. These figures are my hand calculation, not a run.

- **Launch speed:** I balanced the spring's work against the arm, scoop and ball inertia (about 0.091 kg·m²) and the gravity they climb (about 1.19 J). That gives 5.3 N·m/rad.
- **Bucket:** a 70 cm open box whose base centre is exactly 3 m along from the ball's starting centre (x ≈ 2.44 m). The ball is aimed to drop past the wall-top height just before the centre, leaving roughly ±30 cm of tolerance.
- **What's unchecked:** I haven't run it. The softness of MuJoCo's hinge stop and contacts could shift the landing by a few tens of centimetres.

```world
world  catapult into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  40 cm
  arm length    60 cm
  arm mass      400 g
  swings        from 0° to 40°
  spring        5.3 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.002 kg·m²
  colour        wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    70 cm
  width     70 cm
  walls     30 cm
  bounce    dead
  friction  1.0, spinning 0.02, rolling 0.01
  colour    grey
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I need to design a catapult that launches a ball 3 meters into a bucket, working through the physics carefully. I'm planning the stand as a box sized relative to pivot height, with the pivot point positioned at the origin, and an arm extending from that pivot as a separate box component.

The scoop and scoop-back attach near one end of the arm, positioned to hold the ball securely before launch. Thinking through the hinge rotation about the y-axis, I realize positive rotation lifts the near end of the arm upward, so the arm should start near horizontal and swing up under spring tension until it hits a stop, at which point the ball releases perpendicular to the arm's motion with velocity determined by the arm's angular speed at release.

I'm reasoning that at a stop angle around 45°, the ball's velocity has both forward and upward components, which should throw the ball toward the bucket positioned roughly 3 meters from the ball's starting x-position. The tricky part is that MuJoCo's hinge joint limit acts as a soft stop, so the arm decelerates rapidly but not instantaneously, and I need to think about how centripetal and tangential acceleration during the swing keep the ball pressed against the scoop base rather than flying out early.

I'm working out whether the scoop's back wall actually helps retain the ball — since centripetal force points inward toward the pivot, the ball's inertia pushes it outward against that back wall, which then pushes back inward, so the geometry works in the ball's favor during the swing. Now I need to figure out the exact release angle and required angular velocity to hit the bucket, which depends on the arm's moment of inertia and spring energy, so I'm setting up the projectile motion equations for a 45-degree launch.

I'm computing the arm's moment of inertia by treating it as a rotating rod about its far end, then adding the scoop base, scoop back, and ball as point masses at their respective distances from the pivot, accounting for the ball sitting against the back wall. For the spring, I'm integrating torque over the swing from 0 to 45 degrees to get total work done, and considering what damping coefficient to use, leaning toward a small value like 0.01 N·m·s to keep energy loss minimal while still being physically realistic.

I'm also factoring in gravitational work from lifting the arm and ball through the 45-degree swing, and worrying about accuracy given MuJoCo's soft joint limits — the arm may overshoot slightly past 45°, which affects exactly when the ball separates from the scoop. Getting the ball to land within ±25 cm at 3 meters is a tight target given these uncertainties, so I'm thinking the bucket should be sized generously, maybe a 60 cm wide open box, to give some margin for error.

Since the ball stays pressed against the back wall by centrifugal force until release, I can treat its release velocity as simply ω times R at the moment the arm hits the stop, which simplifies the energy calculation considerably.

I need to account for the ball center's actual position relative to the pivot — it sits offset above the arm's line by the combined thickness of the arm, base, and ball radius, so the velocity direction at release isn't purely tangential to a simple radius. Let me pick concrete numbers: a 40 cm pivot height, 60 cm arm, a 4 cm ball radius with 100 g mass, and a 16 cm scoop base, then work out the geometry at θ=0 explicitly.

At that starting angle, nothing holds the arm up except the spring — gravity on the mass near the end creates a torque pulling the arm downward, so the spring torque has to exceed that to get things moving, and I need to nail down exactly where the ball's center sits at launch along the scoop base.

I should use `on catapult.scoop base, at catapult.scoop base's near end` to pin the ball's near end flush against the back wall, giving it a starting center around x = -0.56, touching at contact. Now I need to check whether the catapult itself defaults to origin, since that determines the ball's absolute position.

I'm placing the bucket center at x = -0.56 + 3.0 = 2.44 m, interpreting the "3 m from where the ball starts" as a horizontal distance, with the bucket on the floor and the ball starting at height 0.47. Now I'm setting up the rotational physics: defining the ball's position relative to the pivot at θ=0 and working out how rotation about the y-axis transforms its coordinates as the catapult arm swings.

At 45°, I compute the ball's rotated position and absolute coordinates, then derive its velocity vector from ω × p, which gives me the components needed to find the launch elevation angle.

I'm getting an elevation of about 37.9° given the offset, with the pivot radius around 0.564. I'm now working out the relationship between the rotation angle θ and the launch elevation—since the pivot starts at 7.1° from the -x axis, elevation = 90° − (θ + 7.1°), meaning θ ≈ 37.9° gives a 45° release, though I still need to account for exactly when separation occurs as the arm decelerates.

The ball separates once the arm begins decelerating at the limit, so with a soft stop around 40°, elevation comes out closer to 42.9°, and since range is fairly insensitive near 45° this should be fine. I'm also checking the landing condition at the bucket, aiming for the ball to cross around z=0.2 at x=2.44 so it lands inside walls roughly 30 cm tall.

Computing the release geometry at θ=40°, I get the release point and velocity direction, giving an elevation of about 42.9° and a horizontal travel distance from roughly x=-0.384 out to x=2.44.

Solving the projectile equation with this trajectory for a drop of about 0.61 m over a horizontal range of 2.82 m, I find v²≈22.5, so v≈4.745 m/s, giving a required angular velocity ω≈8.41 rad/s at release. Now I need the kinetic energy needed at that configuration, which means working out the inertias about the pivot.

I'm computing component inertias: the arm (treated as a box) contributes about 0.048 kg·m² for an assumed mass of 0.4 kg, and I'm now adding the scoop base and back pieces, placing each at its offset from the pivot and using the parallel axis theorem to get their contribution.

Now I'm adding the ball's inertia (about 0.032 kg·m² plus a negligible spin term), then considering the default armature inertia of 0.01 kg·m², which adds directly to the joint's total rotational inertia unless I override it.

Summing everything gives total I ≈ 0.0911 kg·m², so KE = 0.5·0.0911·8.41² ≈ 3.22 J. Now I'm computing the gravitational PE change from 0° to 40°: the arm's center shifts to raise it by about 0.193 m (ΔPE ≈ 0.757 J), and I'm starting to work out the scoop base's height change as well.

Adding damping losses brings the total energy requirement to roughly 4.45 J. Working backward through the spring energy formula with a swing angle of about 0.698 rad, I'm solving for stiffness and getting around 5.22 N·m/rad if the spring reference is set toward 90°, which I need to translate into MuJoCo's springref parameter convention.

Checking initial torque balance: the spring provides about 8.2 N·m at the start compared to roughly 1.89 N·m of gravity torque from the arm, ball, and scoop combined, so the net torque is positive and the mechanism should move. A larger spring-to-gravity ratio would give more constant torque, so that's acceptable. Now I need to verify the ball stays seated against the scoop during the acceleration phase by checking tangential acceleration.

I'm also checking what happens at release: the arm hits its stop and rebounds, so I need to confirm the ball clears the arm and scoop as it departs, tracing the ball's trajectory relative to the pivot to make sure it doesn't collide with the arm on its way out.

Checking the trajectory at x=0, the ball reaches height 1.11, well clear of the pivot area. Then I'm verifying the arm doesn't collide with the stand geometrically — arm bottom sits at 0.38 while stand top is at 0.34, leaving a 4 cm gap, so they're fine as separate bodies.

Now I'm worried about the joint limit softness: with angular velocity around 8.4 rad/s, MuJoCo's default solref might let the arm penetrate the limit by roughly 5 degrees before stopping, which could matter for the launch accuracy.

equals arm's angular velocity at release, so that's the key handoff value I'm using. There's minor uncertainty from the ball's own contact softness and small settling under gravity, but those should be negligible compared to the dominant spring-driven acceleration, which pushes q from 0 toward the limit with torque proportional to displacement from the spring reference.

Now I need to pin down the bucket's geometry and placement more carefully — it's an open box 60 by 60 with 30 cm walls, and its position has to be inferred from phrases like "its rim 4 m beyond ball," meaning I offset the base centre from the ball's x-coordinate by the stated distance to get its actual placement.

I should also double-check the ball's trajectory as it crosses near the bucket's near wall, computing the time to reach that horizontal distance using the known velocity components.

Checking the height at that point gives roughly 0.57 m, which is above the wall's top, so I continue to the next wall position, finding it drops to about 0.2 m there, under the 0.3 m threshold, but then by the far wall it dips to negative, meaning it crosses below the rim height somewhere before the far wall — so now I need to solve for the exact x where z equals 0.30 to confirm the ball actually clears or lands inside the bucket.

Aiming for the z=0.3 crossing near x=2.42 gives roughly ±0.31m of margin, and since range sensitivity scales with v², a 10% energy error could shift things by about 0.28m — workable but tight. I'll go with a bigger bucket, 70cm wide with 30cm walls, and now need to recompute the launch velocity.

Solving for v at that crossing point gives v≈4.80 m/s, ω≈8.505 rad/s, kinetic energy ≈3.30J, total energy ≈4.53J, yielding a spring stiffness k≈5.3 N·m/rad. I should double check the bucket is still 3m from the ball's start position.

The ball should land near the base around x~2.6 and settle inside without bouncing out, so the geometry checks out. I also need to confirm the armature setting (0.002 kg·m²) and the arm mass specification (400g) are written correctly in the final parameters.

Other potential energy losses I should account for: friction between ball and scoop, contact softness, and ball spin inertia during launch — the ball's angular velocity needs to match the frame's rotation without slipping, which I've already accounted for. The rolling contact friction setting should also be fine with the current configuration.

Now I'm setting up the swing range from 0° to 40° with a spring toward 90° and light damping, positioning the ball flush at the scoop base's near end, setting moderate ball friction and high bucket friction so it stops properly, and defining the final expectation that the ball comes to rest in the bucket. I'm also double-checking that the scoop back doesn't interfere with the ball's path at the 40° position before writing everything out.

