The catapult arm is driven by a constant-torque motor whose control is set in the `start` keyframe. A joint limit stops the arm at 40°, and the ball leaves the cup at about 4.95 m/s, roughly 45° above horizontal. The ball and bucket use stiff contacts, and the ball has rolling friction so it settles. I sized the torque with an energy balance rather than by running the scene, so treat the 3 m landing as a calculation that still needs checking in simulation.

How the numbers were chosen:
- **Arm and ball:** the arm turns about a y-axis pivot at (0.55, 0, 0.4). The ball starts at x = 0, sitting on the arm against a small wall at the arm's tip.
- **Release speed:** an energy balance gives about 4.95 m/s at release. It includes the arm, wall and ball inertia and the gravity work done while the arm turns 40°.
- **Torque:** that speed needs a torque of 5.63 N·m.
- **Landing:** the ball's centre crosses z ≈ 0.4 m (just above the 0.38 m rim) at x = 3 m.
- **Bucket:** an octagonal tub centred 3 m from the ball's start, with an inner half-width of 0.35 m. That gives roughly ±10% margin on range.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" pos="0 0 0" rgba="0.8 0.85 0.8 1"/>

    <!-- catapult frame (visual only, non-colliding) -->
    <geom name="catapult_base" type="box" pos="0.55 0 0.02" size="0.3 0.15 0.02" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_post_left" type="box" pos="0.55 0.09 0.2" size="0.02 0.02 0.2" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_post_right" type="box" pos="0.55 -0.09 0.2" size="0.02 0.02 0.2" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0.55 -0.11 0.4 0.55 0.11 0.4" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- throwing arm: pivot at (0.55,0,0.4), arm extends along local -x, ball sits on local +z face -->
    <body name="catapult_arm" pos="0.55 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="-5 40"/>
      <geom name="catapult_arm" type="box" pos="-0.3 0 0" size="0.3 0.04 0.01" mass="0.3" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_wall" type="box" pos="-0.595 0 0.04" size="0.005 0.04 0.03" mass="0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <!-- ball resting in the cup -->
    <body name="ball" pos="0 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.01 0.01" solref="0.005 1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <!-- bucket: octagonal tub, centre 3 m from ball start -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_floor" type="cylinder" pos="0 0 0.02" size="0.39 0.02" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_0" type="box" pos="0.37 0 0.19" size="0.02 0.163 0.19" euler="0 0 0" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_45" type="box" pos="0.26163 0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 45" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_90" type="box" pos="0 0.37 0.19" size="0.02 0.163 0.19" euler="0 0 90" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_135" type="box" pos="-0.26163 0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 135" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_180" type="box" pos="-0.37 0 0.19" size="0.02 0.163 0.19" euler="0 0 180" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_225" type="box" pos="-0.26163 -0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 225" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_270" type="box" pos="0 -0.37 0.19" size="0.02 0.163 0.19" euler="0 0 270" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_315" type="box" pos="0.26163 -0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 315" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="5.63"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to figure out a catapult design that reliably launches a ball 3 meters to land in a bucket, where the trajectory depends on hinge release timing, which is tricky to predict without simulation. I'm considering whether a velocity-driven arm or a spring-loaded mechanism would give more predictable results.

Working through the geometry: if the hinge axis is along y at height 0.3, with a 0.5m arm starting pointing in -x and rotating upward, the ball's launch angle depends on where the arm stops. I calculate that stopping the arm at a 45° angle from horizontal gives a 45° launch velocity direction, which should maximize range for a given speed -- so the ball sits passively in a cup and gets flung forward when the arm hits its rotational stop.

Landing accuracy depends on release speed, which depends on motor dynamics and ball-cup contact — using a high-gain velocity actuator stopped abruptly by the joint limit risks a jolt that bounces the ball unpredictably off soft contact. I'm considering instead bypassing the hinge-stop dynamics entirely and releasing the ball more deterministically.

Working through the physics: tangential speed is ω times radius, so a constant-velocity arm gives a predictable launch speed, though a 5% error in v translates to roughly 10% error in range (~0.3m), which is tight given a bucket radius around 0.3-0.35m. I'm weighing whether to widen the bucket and ensure it's heavy enough not to tip, while also accounting for centrifugal effects on the ball as the arm swings.

For the cup design, I'm thinking the arm's upper face pushes the ball during the upward swing, with the ball resting on top initially and an outer wall at the tip containing it until release.

Since the ball sits offset from the pivot axis by both its arm-length position and a small normal offset (arm thickness plus ball radius), its velocity vector isn't purely tangential — there's a slight inward component I need to account for, introducing a small angular correction. Now I'm settling on concrete numbers: pivot height, ball radius around 4cm, mass near 0.1kg, and starting to size the arm itself.

Let me work through the arm geometry — box half-extents, center offset, ball position along the arm with the normal offset for thickness plus ball radius. I'm also checking the hinge's initial angle and joint limits to make sure the arm doesn't start pinned against a stop, then deriving the unit vectors for the arm direction and its perpendicular to get the ball's release velocity direction as a function of the arm angle.

Working out the release angle: with ball offset 0.55 and perpendicular offset 0.05, I compute the small angular correction of about 5.2° from the geometry, so the velocity direction ends up at 90° minus the arm angle minus that correction. Solving for a 45° launch angle gives an arm angle near 39.8°, which I'll use to pick where the joint limit should stop the arm — keeping in mind the ball doesn't release exactly at that limit.

I'm also checking whether the ball stays seated against the outer wall while the arm spins at constant ω, since the outer wall needs to supply the centripetal force while gravity contributes a small component along the arm toward the pivot, and with no tangential acceleration this balance should hold until the joint limit kicks in.

A cleaner alternative is to drive the arm with constant motor torque instead of an abrupt velocity profile, giving smooth angular acceleration. I can then estimate the release speed via work-energy balance — torque times angle minus the gravitational potential change of arm and ball equals the kinetic energy at release — which should be fairly accurate as long as the ball stays rigidly seated in the cup.

With velocity servo, the exponential approach time constant τ=I/kv just needs to be small enough relative to the swing angle so ω reaches ω_target before release, and steady-state error from gravity scales as gravity torque over kv, making this a robust approach. I'm now working out the actual required speed numerically.

Now I'm figuring out the launch geometry — I want the ball to cross the bucket rim height near the bucket's center (or just slightly short of it), treating the bucket as wide enough to tolerate some landing spread, then setting up the trajectory equations from release point to that target crossing point.

Setting up the pivot and ball position relative to the arm angle, aiming to pick the release angle where the arm decelerates enough for the ball to come off cleanly toward the bucket.

Checking whether the ball's velocity has an inward component relative to the arm when it stops abruptly — there's a small component toward the pivot, but it's minor enough that I can skip modeling an inner wall and just rely on friction holding the ball during the initial acceleration phase.

Then I worry about the outer wall: making sure it's tall enough to hold the ball against centrifugal force but still lets the ball clear it once it separates and starts drifting slightly inward. A wall extending about 0.06 above the face should work since the ball only reaches 0.04.

I also need to consider what happens as the arm hits its joint limit — it might overshoot and bounce back slightly before settling, which could matter if the ball hasn't fully separated yet.

Plugging in numbers, the critical damping coefficients give b≈105 and k≈2770 with natural frequency around 52.6, so max penetration from the initial velocity works out to roughly 0.07 rad. That means the deceleration kicks in almost instantly at contact — with a force like -105*10 right at onset — so the ball separates essentially right when the limit engages rather than after any noticeable overshoot.

I'm also considering tightening solreflimit to something like "0.01 1" for a stiffer stop, keeping in mind timeconst needs to stay at least twice the timestep. The remaining question is whether the ball's own soft contact lets it penetrate slightly before the arm's deceleration takes effect, since the push force stays small while angular velocity is roughly constant up to that point.

Now I'm checking the steady-state torque needed to overcome gravity on the arm and ball, picking an arm mass around 0.3 kg and solving for a gain large enough to keep steady-state error below 1% at the target angular velocity, which leads me to pick kv around 200 and work out the resulting time constant from the arm's moment of inertia.

With a time constant that short compared to the timestep, I realize the arm essentially snaps to its target velocity almost instantly. Since MuJoCo's default Euler integrator doesn't implicitly handle velocity-dependent actuator forces, I should switch to the implicitfast integrator, which accounts for the derivative of actuator force with respect to velocity and keeps things stable. But that near-instant ramp-up means the ball, initially at rest, gets hit by an arm that's essentially already slammed up to speed, so I need to think about how that impulsive contact plays out given the soft contact parameters.

Computing the max penetration depth with this damping value gives about 3.5 cm, which is way too deep for a 4cm ball — it'd essentially tunnel through. I need a more moderate kv so the time constant lands around 0.03-0.05s instead, though that introduces a notable steady-state velocity error from gravity (roughly 0.85 rad/s with kv=1.65), which is workable but not great.

I'm also considering switching to a constant-torque motor approach instead, working through the contact physics directly: tangential acceleration from the motor creates a force on the ball, and with MuJoCo's soft-contact model the penetration depth scales with that acceleration over the contact stiffness — trying to estimate whether that keeps penetration in a reasonable range.

So the jolt dynamics are still roughly governed by the damping and stiffness terms, keeping that rough penetration estimate reasonable, and constant pushing produces negligible penetration. I'll move forward assuming a constant torque motor, computing release speed from energy including gravity and then the resulting range, while flagging contact compliance and ball-rolling-along-the-arm-face as key uncertainty sources — particularly whether centrifugal force holds the ball against the outer wall or lets it roll inward toward the pivot.

Checking the inward forces, they're negligible compared to the centrifugal outward force, so the ball stays pinned to the outer wall. The ball's own rotational kinetic energy is also negligible compared to the arm's, so I can ignore it. Now I'm setting up the full dynamics with the ball positioned at its radius from the pivot and computing the gravitational potential energy terms for both the ball and the arm's center of mass based on their geometric offsets.

I'll widen the arm half-width to 0.04 for safety margin since the ball radius exceeds the original width, and skip adding side rails since lateral forces are negligible in this planar symmetric setup. Checking the rotation math confirms the local axes map correctly to the global u and n directions at hinge angle θ, so now I'm moving on to defining the arm's mass via its box density.

For collision filtering, since MuJoCo's parent filter only excludes world-body parent collisions in special cases, the arm body will actually collide with static frame geoms like base posts — so I need to position those posts off to the sides, beyond the arm's half-width, to keep the swing path clear.

The joint limit stop should handle the arm's end-of-travel fine, with the motor just pushing against it afterward, and the ball's trajectory should clear the frame structure near the pivot without issue. Now I'm working out the arm's moment of inertia about the pivot — treating it as a thin box and applying the parallel axis theorem gives roughly 0.036 for the arm itself, then adding the wall's contribution based on its distance from the pivot.

Adding the ball's contribution and a tiny spin term brings total inertia to about 0.0737. With that settled, I'm now setting up potential energy as a function of rotation angle, computing it separately for the arm's center of mass and the wall's center of mass based on their positions relative to the pivot.

Summing both contributions gives PE(θ) = 1.5392 sinθ + 0.0569 cosθ, and I'm now evaluating the change in potential energy between θ=0 and the target swing angle of 40°, plugging in sin(40°)=0.6428 and cos(40°)=0.7660.

I find ΔPE ≈ 0.9761 J at release. To get the release speed I need the range calculation, so I'm setting up the pivot position so the ball starts at x=0, then computing the ball's world coordinates at release by rotating its local position by 40° using the pivot offset of 0.55 in x and 0.05 in z.

Now I'm finding the velocity direction angle: δ = atan(0.05/0.55) ≈ 5.194°, giving α ≈ 44.806°, with cos α ≈ 0.7095 and sin α ≈ 0.7047. I'm choosing a pivot height of 0.4, which puts the release z-coordinate at about 0.792, and now I'm checking this against the bucket rim height to see where the ball should land.

I'm setting the target so the ball center passes through z=0.4 at x=3.0, close to the rim level for a centered shot. Computing the horizontal distance D≈2.839 and vertical drop Δz≈-0.392, I'm now plugging these into the projectile equation using tan α to solve for the required launch velocity.

Solving gives v²≈24.45, so v≈4.945 m/s — and with no drag assumed, I convert this to angular velocity ω≈8.95 rad/s using the ball radius of about 0.552.

Now computing kinetic energy as roughly 2.95 J, but I need to pin down the total moment of inertia more carefully by summing contributions from each component: the arm (treated as a box, using its dimensions and parallel-axis theorem to get about 0.036) and now the wall piece, working through its own box inertia formula.

Then for the ball, I'm treating it as a point mass contribution plus its spin inertia, giving about 0.0306. Summing everything gives a total system inertia around 0.0737, so KE comes out to roughly 2.954 J. From there I set up the work-energy balance — motor work equals KE plus the change in potential energy, about 0.976 J — solving for torque gives approximately 5.63 N·m.

I double-check whether the ball's own spin from friction matters much, concluding it's negligible (around 0.2% of total inertia). I also verify the arm's joint behavior near its limit, confirming the ball stays pressed against the face throughout the motion by checking the normal force component against gravity and tangential acceleration.

Working through the numbers, the angular acceleration comes out to roughly 56 rad/s², giving about 31 m/s² linear acceleration, with the arm reaching its release angle in about 0.158 seconds. I then consider small effects like contact compliance causing the ball to slightly lag behind the arm face due to centrifugal effects at release, but these seem minor enough not to change the overall picture.

Checking the steady-state joint penetration using the default solver parameters, I get something on the order of a millimeter, which is negligible. I also note that a 1% velocity error translates to roughly a 2% range error, about 6 cm given the throw distance, and the bucket's inner radius should provide enough margin to absorb that.

For the keyframe, I'm placing the ball's initial position so it just touches both the arm face and the outer wall — world position (0,0,0.45) works since the arm top sits at z=0.41 and the wall's inner face at x=-0.04 matches the ball's radius. I need to get the qpos ordering right, combining the hinge joint's single value with the ball's seven-value freejoint state, depending on body order in the tree.

Since MuJoCo defaults unspecified key attributes to qpos0, zero qvel, and zero ctrl, I can simplify the keyframe to just specify the control input directly, like setting ctrl="5.63" for the motor, with a reasonable ctrlrange like 0 to 10. I'm now thinking through how the bucket's position at x=3.0 relates to the ball's starting x-position at 0, confirming the arm begins rotating immediately once ctrl is applied at t=0.

The "3 meters away" distance is ambiguous — it could mean horizontal distance or full 3D distance between ball start and bucket center, since the ball starts at some height off the ground while the bucket sits lower. I'll just go with horizontal distance of 3 and place the bucket body accordingly, accepting that making it exactly 3 meters in true 3D isn't really feasible given the height offset.

For the bucket itself, I'll make it a static body welded to the world, with its geoms forming an octagonal approximation of a cylinder — using around 8 to 12 boxes arranged radially to form walls with a floor, sized so the inner radius is about 0.3 and the rim height is roughly 0.35.

I'm tracing the ball's trajectory near the rims: checking it clears the near rim at x=2.7 with good height margin, then estimating where it would hit the floor around x=3.32, near the far wall at x=3.3. It looks like the ball would actually strike the inner face of the far wall around height 0.13 and bounce back inward, which keeps it contained rather than escaping.

Since MuJoCo's default contacts are nearly critically damped with little restitution, the ball won't bounce much off the floor at ~5 m/s impact. But I'm worried about it rolling indefinitely around the octagon walls without rolling friction to dampen it, so I'm considering adding condim="6" with rolling friction to the ball geom to help it settle rather than circling forever.

Since contact uses the max condim across geoms anyway, that default of 3 on other objects won't matter here. I'm also checking that the ball's end velocity will actually fall below the 5 cm/s threshold given rolling friction, and estimating penetration depth when the ball lands in the bucket at impact speeds around 5 m/s, given the floor thickness and contact damping parameters.

That penetration estimate is worrying — roughly 3.5 cm could tunnel through a 2 cm floor, and the ball may actually hit the far wall first, which is even thinner and riskier. I should thicken the walls and floor and stiffen the ball's contact solref to reduce penetration to under a centimeter, while keeping the time constant above twice the timestep as MuJoCo recommends; this shouldn't break the catapult contact behavior either.

That penetration seems manageable given the step velocity, so a 0.05m wall width should hold up fine. I'm working out wall geometry now—making walls thicker (0.04m) with eight sides, computing the apothem and half-tangential width to size each panel properly, while also checking rim height and whether the ball could bounce out near the walls given low restitution. I'm now tracing the ball's trajectory near the close wall to see where it intersects, checking the x-range against the wall's actual position and thickness.

Computing the descent slope at landing, the ball clears the near wall with plenty of margin, around z≈0.78 compared to the 0.4 wall height. Tracking forward, the ball reaches floor level roughly at the same point it would reach the far wall, so I need to check whether it hits the floor or the wall corner first.

Checking tolerance for speed variation: if the ball travels 10% longer, the range increases about 0.3m, pushing the crossing point near x≈3.3 — close to the far wall's top edge, giving roughly a 9% margin before it clips the rim. On the short side, I'm checking whether the ball clears the near wall's top edge with enough clearance, since undershooting risks hitting that corner instead.

Translating this to speed sensitivity, an 8% range variation corresponds to about 4% in launch speed, which should be safe if my energy model holds that tightly — though contact compliance and friction could introduce error. I'm now resizing the bucket for margin: using an inner apothem around 0.35m, rim height 0.36m, and working out the floor and wall cylinder dimensions so the walls span from the base up past the rim.

With the rim settled around 0.38 and floor top at 0.04, I'm checking the target height for the trajectory — keeping it near 0.4 so the ball clears the wall with good margin at the center, while near the wall edges (around x≈2.65) it still needs to clear the rim height with roughly a third-meter margin for a short miss, and I'm now considering the long-miss boundary condition too.

I'm also checking that the ball clears the catapult's pivot and posts during flight, and confirming the arm (resting at its stop angle) won't interfere with the released ball moving forward and up. Then I'm double-checking the joint's angle limits, noting the compiler needs `angle="radian"` set for the range values to be interpreted correctly rather than defaulting to degrees.

Right, so I realize the default is actually degrees, so I'll explicitly set `compiler angle="degree"` and use range -5 to 40 with degree-based euler values. I'm also thinking through potential geometry overlap: the static axle cylinder at the pivot could physically intersect the arm's box geometry since the arm spans back to that pivot point, which would create unwanted contact forces, so I'll assign separate contype/conaffinity groups to the arm so it doesn't collide with the static frame geoms.

But then I catch that this breaks ball collision entirely, since mismatched bitmasks mean the arm and ball wouldn't interact either. So instead I'll keep the arm on the default contype/conaffinity (1/1) like the ball, and just set the frame geoms to contype="0" conaffinity="0" so they're purely visual and never collide with anything, which sidesteps the overlap problem cleanly. I'm also double-checking the post spacing at y=±0.08 against the arm's half-width to make sure there's no physical clash.

Static geoms like the floor and bucket won't collide with each other since both are static, and the ball starts clear of the floor so that's fine too. Once the ball leaves the arm, the arm just stays pinned at its joint limit from motor torque, no longer interacting with anything. I confirm the joint limit defaults are fine since release happens right at the limit onset anyway, and I verify the motor's torque is sufficient to hold the arm steady against the limit, and that the hinge axis orientation correctly raises the tip with positive rotation.

Checking the actuator setup with gear ratio 1 and a control range capped at 10, driven by the keyframe control value. I confirm the ball's inertia is properly accounted for while co-rotating with the arm, masses are assigned directly via geom attributes, and there's no damping or armature affecting the hinge. The joint limit sits cleanly at 40 degrees so that's not an issue, and any minor contact penetration between the ball, arm, and wall is negligible. I'm just double-checking that the ball stays properly seated on the arm under gravity before the release point.

Verifying that when the arm suddenly accelerates, the soft contact prevents any oscillation as the ball catches up, and that separation during deceleration happens cleanly with the ball moving away along the normal direction, eliminating friction concerns. I recompute the work done by torque to confirm it matches 3.9305, verify gravitational torque never exceeds the motor's capacity, and start working out kinetic energy at release.

Using KE=2.9545 I get ω²≈80.18, consistent with earlier figures. I confirm that MuJoCo's rolling and torsional friction don't matter mid-flight, and that the ball rotating along with the arm (no relative slip) keeps things simple. I reason the ball will settle in the bucket without jittering issues, then start laying out the bucket wall positions at 45-degree increments around a 0.37 radius, computing the first few coordinates.

I'm defining the bucket floor and walls using cylinder and box geoms, placing the floor inset to catch the ball, and setting matching solref values for stable contacts between ball and bucket. I also note adding a light source and keeping the default Euler integrator with a small timestep for the simulation.

Now I'm building the catapult's visual structure: a flat base box, two side posts rising to form a frame, and a cylindrical axle spanning between them using a fromto definition so it aligns horizontally along the y-axis, all set to contype 0 since they're purely visual.

I'm checking that the ball's release trajectory stays clear of the arm's cup wall — since the wall sits on the tip side and the ball moves inward toward the pivot during release, there's no collision. Now I'm assigning clear names to each body and geom (arm, cup wall, base, posts) along with the joint and actuator, before moving on to define the keyframe.

