The catapult arm is driven by a torque-limited velocity motor at 9.56 rad/s and is stopped by a hinge limit at 45°. The ball rests against a lip at 0.5 m from the pivot and leaves the arm at about 4.8 m/s, roughly 39° above horizontal. That speed is calculated to land the ball at the centre of an octagonal bucket placed 3 m from the ball's start (x = −0.5 → x = 2.5). The landing point depends strongly on launch speed, so this is the part most likely to need adjusting after a run.

```xml
<mujoco model="catapult_bucket">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- catapult frame (visual only, non-colliding) -->
    <geom name="catapult_base" type="box" pos="0 0 0.01" size="0.1 0.12 0.01" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.08 0.2" size="0.03 0.02 0.2" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.08 0.2" size="0.03 0.02 0.2" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>

    <!-- catapult arm: hinge about y at z=0.4, arm points along -x, swings up to 45 deg -->
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" limited="true" solreflimit="0.01 1"/>
      <geom name="catapult_beam" type="box" pos="-0.26 0 0" size="0.30 0.04 0.01" mass="0.3" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_lip" type="box" pos="-0.55 0 0.04" size="0.01 0.04 0.03" mass="0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" pos="0 0 0" euler="90 0 0" size="0.015 0.06" mass="0.02" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- bucket: centre at x=2.5, 3 m from ball start at x=-0.5 -->
    <body name="bucket" pos="2.5 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.29 0.01" condim="6" friction="1 0.01 0.001" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.27 0 0.17" euler="0 0 0" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1909 0.1909 0.17" euler="0 0 45" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.27 0.17" euler="0 0 90" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.1909 0.1909 0.17" euler="0 0 135" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.27 0 0.17" euler="0 0 180" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1909 -0.1909 0.17" euler="0 0 225" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.27 0.17" euler="0 0 270" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.1909 -0.1909 0.17" euler="0 0 315" size="0.01 0.117 0.15" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- ball resting on the arm against the lip -->
    <body name="ball" pos="-0.5 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="20" forcelimited="true" forcerange="-10 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.5 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="9.56"/>
  </keyframe>
</mujoco>
```

```expect
ball touches catapult_beam
catapult_arm reaches its upper stop
ball touches bucket
ball comes to rest in bucket
```

---
thinking (summarized):

I'm thinking through a catapult design with a hinged arm and ball cup, driven by a motor or spring to launch toward a bucket 3 meters away. Since exact range is hard to predict without running the simulation, I'm considering making the bucket larger to tolerate variance in landing position.

Good news: since the ball's release velocity is tangential to the arm's rotation, it's effectively normal to the arm surface, so it lifts cleanly away without catching on the cup's walls as long as the lips stay low. I'm setting up the hinge axis along y, working out how rotation angle θ maps the arm tip position, confirming that positive θ lifts the tip upward and finding the release angle that sends the ball on the desired trajectory.

For the 45-degree launch, release happens at θ=45°, and I'm computing the tip velocity direction as (sinθ, cosθ) to confirm it points forward-up correctly. Now I'm accounting for the ball sitting slightly off the arm's surface due to its radius and the arm's thickness, working out the ball's actual position and velocity as a function of this offset and the rotation.

There's a small tangential component in the ball's velocity due to this offset, but since the ball is also moving away from the arm normally at release, it separates cleanly without sliding issues. Now I'm setting up the initial conditions — ball starting at rest with the arm at some initial angle, considering whether a spring mechanism is involved in the launch.

Instead of a spring, maybe a motor with constant torque works better, giving a roughly constant angular acceleration minus gravity's torque contribution. Actually, a velocity servo could be cleaner — drive the arm to spin up to a target angular velocity quickly, then let it hit the joint limit at 45°, which gives precise control over ω at release regardless of mass ratios, as long as the servo is stiff and the arm is light. The ball rides along on the arm as it accelerates upward, though there's an initial jerk from the contact force.

Thinking about how the ball stays in the cup during the swing: the centripetal acceleration ω²L toward the pivot needs to come from friction or the cup wall pressing on the ball. The outer wall at the arm's tip, perpendicular to the arm, holds the ball against that radial force. Once the arm stops, there's no more centripetal requirement since the ball moves freely — its velocity at release is roughly perpendicular to the arm (since it equals ω cross r, with r pointing from pivot to ball center).

I'm deciding a shallow cup made from two short lips (inner and outer, about 0.6 times the ball radius in height) is simplest, since the ball mostly slides parallel to the outer wall anyway, minimizing contact issues. For the arm's stop, I'm weighing whether to use a soft joint limit (letting it overshoot slightly while the velocity servo keeps pushing) versus a physical bumper geom, and estimating the launch speed as roughly ω times the ball's distance from the pivot. I think a dedicated bumper geom with a defined joint range is cleaner than relying on soft limit parameters.

Separately, I'm reasoning through the release timing: since the ball leaves the arm once deceleration starts, the effective release velocity is basically the arm's speed right when it hits the limit margin (approximated as zero). For the velocity servo, I'm working out the force equation with a chosen gain and estimating the arm's moment of inertia from its mass and length to get a rough time constant for spin-up.

With a gain like 50, the time constant comes out too fast relative to the timestep, which could cause instability with explicit integration — unless I switch to an implicit integrator that properly handles actuator velocity feedback, or just lower the gain to something like 10 for a more reasonable ~0.01s constant. I'm checking how much the arm rotates during that spin-up window before reaching the needed angular velocity for the full 45-degree swing, and I still need to factor in gravity torque on the arm.

The ball sits on top of the arm, so the rapid acceleration pushes it upward with it; contact forces will be large but manageable given the critically-damped solref settings, meaning the ball should lag only briefly before matching arm velocity without bouncing. Gravity on the ball gets supported by the arm's normal force, with centripetal effects factoring into the contact dynamics as well.

Now I'm working out the launch geometry: pivot at height 0.4, arm length 0.5 to the ball center, with the ball radius and arm thickness setting an offset of 0.05 from the arm's centerline. Starting with the arm horizontal, the ball begins at x=-0.5, z=0.45, and the bucket center sits at x=2.5. I'm computing where the ball actually is at the release angle of 45 degrees, accounting for both the arm rotation and the perpendicular offset from the ball sitting on top of the arm.

I'm also deriving the release velocity direction from the angular velocity, factoring in both the tangential motion and the offset contribution, giving a launch angle around 39 degrees above horizontal. Now I need to figure out what target height and position the ball should land at to drop cleanly into the bucket's opening, considering the bucket's rim height and inner radius.

Aiming for the rim at roughly z=0.25 near x=2.5, I set up the projectile equations for horizontal distance and vertical drop under gravity, solving for time of flight and then back-solving for the required angular velocity ω, arriving at approximately 9.5 rad/s.

This gives a landing speed around 4.78 m/s with a steep descent angle near 50°, which should work well for entry into the bucket. Checking sensitivity, range scales with ω², so a 1% error in ω produces roughly 2% range error (~6 cm), and the bucket's tolerance of about ±0.2 m limits acceptable ω error to roughly ±0.3 rad/s — so I need the release dynamics and gravity assumption to be fairly precise, with no air drag in the default model. I'm also considering how the ball behaves as the arm decelerates near its soft limit, since it's no longer being forced at that point.

I'm working through the geometry of where the ball separates from the arm — whether the outer lip of the holder contacts the ball given its velocity direction, which is perpendicular to the radius vector at a slight angle from the arm's axis, and how that affects the exact release point.

So the ball needs to clear the inner lip before sliding inward—given the 0.1 slope ratio, a small gap with a modest lip height should work fine geometrically. I'm also checking whether the inner lip is even necessary, since during spin-up the tangential and centripetal accelerations naturally push the ball against the arm surface, with the arm-axis component of acceleration helping keep it in place.

Working through the forces: centripetal acceleration points toward the pivot, meaning the ball needs a net force toward the pivot or it'll slide outward and rely on the outer lip. The angular acceleration term also demands a pivot-ward force, again from the outer lip. Gravity's component along the arm direction is -g·sinθ, which is zero at θ=0 when the arm is horizontal, so at rest the ball just sits fine on the flat surface—though early in the spin-up when α is large, the outer lip is doing the work of holding the ball in place.

Comparing magnitudes at θ=45°, gravity pulling toward pivot is only about 6.9 versus a centripetal requirement near 45, so the outer lip stays pressed throughout — meaning I can skip the inner lip entirely and just keep the outer containment. Side (y) containment isn't really needed either since drift there should stay minimal. I'll position the ball resting lightly against the outer lip at the start, with the lip face placed just outside the ball's resting surface, and set the ball on top of the arm at the appropriate height.

As for release dynamics, friction at the outer lip fades as the arm decelerates near the joint limit, and the ball's spin from moving with the arm doesn't matter in flight since there's no aerodynamics modeled — though it could matter once it lands in the bucket. I'm also considering that the servo keeps pushing torque against the joint limit even as velocity should be zero there, so the limit constraint has to hold firm, with slight overshoot determining the exact release angle and timing.

I'm now working out the steady-state gravity torque balance: setting arm mass around 0.3 kg and ball mass around 0.1 kg, computing torque from their centers of mass about the pivot to match against the velocity servo's restoring torque.

Checking the time constant, the system's effective inertia is tiny compared to the servo gain, so the response is nearly instantaneous — well within implicit integration stability even with small timesteps, meaning the arm should spin up quickly before release.

Limiting motor force to ±10 N·m gives α≈180 rad/s², reaching ω in 0.053s over just 14° of rotation. That's still roughly 9g of acceleration at the tip, so I need to estimate how much the soft contact's stiffness and damping (from the timeconst/dampratio reference) would actually limit penetration under that load.

With d≈0.9-0.95, penetration resolves to roughly 2mm for a0=90, which seems fine. I'm also checking the centripetal force at the outer lip is manageable, and that gravity torque modestly reduces acceleration without issue since forcerange clamping just zeroes the derivative there — now I'm checking whether the target angular velocity gets reached before 45 degrees.

Working through the net angular acceleration with gravity subtracted gives roughly 120 rad/s², reaching 21° well within the 45° limit, and the servo region kicks in quickly afterward with a fast time constant. Using forcerange 10 for margin still keeps the angle under limit at ~17°, and the joint limit itself should hold against the servo's push without issue.

Checking that the arm rests at 45° so the ball flies off correctly, and verifying the ball stays pressed against the arm surface during steady rotation since gravity's normal component is balanced by the arm — radial containment from the outer lip looks fine, and the ball's release velocity should match ω times its radius from the pivot.

Now I'm thinking about the velocity actuator setup, confirming the control range is unlimited by default since no ctrlrange is specified. Then I'm working out the bucket geometry at x=2.5 — a cylindrical base with square walls forming a container, sizing the inner width, wall thickness, and height.

Placing each wall box radially around the octagon with thin radial thickness, keeping inner apothem at 0.26. Checking the physics: the ball lands around 50° at roughly 5.8 m/s, and since MuJoCo's default contact isn't very bouncy, it should settle inside the bucket after a bit of bouncing between walls within the 6-second window, though with no rolling friction it may drift slowly on the flat bottom.

Computing the deceleration with μ_roll=0.02 gives about 3.5 m/s², which stops the ball quickly—maybe too fast, so I try 0.005 for a gentler ~0.9 m/s² stop, settling on 0.01 as reasonable. Checking the trajectory against the bucket rim, I verify the ball's descent angle puts it just inside the rim at the right height and position, confirming it clears the wall correctly.

I check the ball clears both inner walls of the bucket with margin to spare on entry and near the bottom, confirming the trajectory lands safely inside. Then I start verifying that the ball's flight path in the y=0 plane doesn't collide with the catapult's support posts positioned at y=±0.1.

Peak height from vz=3.03 gives a rise of about 0.467, putting the apex around z=1.26, which looks fine. I re-pin the geometry: pivot at (0,0,0.4) with hinge axis along y, arm body positioned there, joint range 0-45 degrees matching the MJCF compiler's default degree units.

The arm starts at qpos 0 in the keyframe. I'm working out the arm geometry (a box stub behind the pivot) and the outer lip dimensions, checking where the ball's resting height intersects the lip's top surface to find the contact point between the ball and the lip face.

Since the ball's edge contact with the lip at that height gives a normal force component that's small relative to gravity's normal component, the ball could actually lift off the arm and ride over the lip, which would be a problem. So I'm considering increasing the lip height to prevent that from happening.

Now I'm working out the support structure: posts at y=±0.07 flanking the arm, with the pivot axle as a cylinder running through them. Since MuJoCo excludes contact between a body and its direct parent by default, I need to think through whether the arm-axle overlap is actually filtered correctly.

Rather than relying on that filter working as expected with world as parent, I'm deciding to just disable collisions entirely between the structural parts using contype/conaffinity flags, which sidesteps the ambiguity.

Since that's world-world anyway, I'll just make base and posts non-colliding to keep things simple since the ball won't touch them regardless.

I'm assigning masses: ball 0.1, arm box 0.3, lip 0.03, axle 0.02, then checking the steady-state gravity torque at 45° — roughly 1 N·m, giving a position error around 1/kv under the current gain.

With kv=200 that error drops to 0.005, so I'll add that correction into the ctrl value, landing around 9.52. I'm also second-guessing whether the ball truly tracks arm velocity in steady state (it should, via soft contact coupling) and worrying that when the soft joint limit engages, the arm's deceleration over ~0.02s could cause a noticeable overshoot of several degrees — but since the ball separates from the arm right as contact/deceleration begins, that overshoot may not actually matter for the release trajectory.

I should bump timeconst to 0.01 to be safe for the given dt. The limit engages exactly at θ=0.7854 rad as expected, and I'm checking penetration depths are small enough to not affect the center distance meaningfully (ball stays near L=0.501). Verifying the steady rotation numbers hold up against the release velocity calculation of ω=9.514 rad/s.

At t=0, the arm starts at its lower limit (θ=0) holding against gravity before the motor engages, which is fine. For the bucket geometry, I'm confirming the bottom cylinder spans z=0 to 0.02 and the walls extend from 0.02 up to a rim at z=0.32, giving a consistent containment height for the ball.

For success conditions, I should settle on safe, verifiable expectations: the ball touching the catapult arm initially, and the ball coming to rest inside the bucket near z=0.06 above the floor at z=0.02. I'll avoid negated conditions like "does not touch floor" since the format doesn't support that, and stick to simple positive checks like "ball touches bucket" or "ball comes to rest in bucket."

Now I'm writing out the full XML, computing octagon wall positions using the formula pos = (0.27·cosφ, 0.27·sinφ, 0.17) for φ at 45° increments, with wall half-length around 0.117 to close the corners properly.

Then I'm defining the catapult_arm body with a hinge joint at pos (0 0 0.4), axis along y, limited range 0-45 degrees, plus a beam geom and lip geom...

Adding axle geometry and checking positions...

Now I'm verifying the hinge rotation direction—working through the rotation matrix about the y-axis to confirm a positive angle raises the arm tip correctly from its starting position at (-L, 0, 0).

I'm checking the posts and base geometry, making sure nothing overlaps with collision geometry while keeping the clearances small enough to look visually connected.

Then I check the bucket and ball placement, confirming the bucket walls will collide with the ball and the bottom has sufficient friction. For the keyframe, I'm working out the qpos ordering based on body tree order—arm hinge joint first, then the ball's free joint with its seven values.

I'm reconsidering defining the ball body after the arm to keep qpos ordering clean. I'm also setting up the simulation options with a small timestep and implicitfast integrator, then defining the catapult's velocity actuator with force limits, while weighing how MuJoCo's implicit integration handles actuator force derivatives when the force hits its clamped range.

To avoid depending on uncertain engine behavior, I'll just pick a conservative kv so explicit Euler stays stable regardless: kv < 56 gives margin, so kv=20 keeps kv*dt/I well under the stability threshold while still damping settling oscillations reasonably.

I'm weighing kv values — 25 seems like a safer middle ground given the instability risk if the ball separates from the arm. I'm also working out the precise gravity torque by summing moments from the arm's center of mass, the lip, and the ball's position at 45°.

Total control value comes to about 9.56, and I confirm the torque stays clamped at the forcerange limit of 10 since the raw computed value would be far higher. I check that keeping this clamp prevents an unrealistic jump in the arm's motion, and the ball's initial acceleration from gravity and contact forces looks reasonable without further adjustment.

Now I set the floor dimensions to 5x5x0.1 centered at origin, confirming it spans from -5 to 5 which comfortably covers the ball's starting position at x=-0.5. I lay out the key success conditions to check: the ball touching the catapult beam, the arm reaching its upper stop, the ball touching the bucket, and the ball finally coming to rest inside it.

