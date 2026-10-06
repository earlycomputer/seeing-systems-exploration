The catapult arm is hinged at 0.5 m height and driven by a velocity motor whose control the keyframe sets. A soft joint limit at θ = 0.7105 rad acts as the stop. At that angle the ball leaves the cup at about 45° and 4.55 m/s, which corresponds to ω ≈ 5.67 rad/s. The control is set slightly higher to cover the steady gravity torque. The ball starts at x = −0.8 m, so the open octagonal bucket is centred at x = 2.2 m.

These numbers come from hand calculation, not from running the simulation:

- **Landing:** the computed trajectory enters the rim about 0.1 m short of the bucket centre and first touches the bottom about 0.08 m past it. That allows roughly ±3% error in launch speed before the ball hits a wall rim.
- **Coming to rest:** the ball has rolling friction (condim 6), so it should stop well before the 6 s mark.

```xml
<mujoco model="catapult_to_bucket">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 6 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <!-- Catapult frame (static) -->
    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" size="0.12 0.16 0.01" pos="0 0 0.01" rgba="0.45 0.3 0.15 1"/>
      <geom name="catapult_post_left" type="box" size="0.03 0.015 0.25" pos="0 0.1 0.25" rgba="0.45 0.3 0.15 1"/>
      <geom name="catapult_post_right" type="box" size="0.03 0.015 0.25" pos="0 -0.1 0.25" rgba="0.45 0.3 0.15 1"/>

      <!-- Throwing arm: points toward -x at angle 0, swings up and forward about +y -->
      <body name="catapult_arm" pos="0 0 0.5">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 0.7105" solreflimit="0.005 1" damping="0"/>
        <geom name="catapult_pin" type="cylinder" size="0.015 0.12" pos="0 0 0" euler="1.5708 0 0" mass="0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
        <geom name="catapult_beam" type="box" size="0.45 0.03 0.02" pos="-0.4 0 0" mass="0.5" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_lip" type="box" size="0.01 0.04 0.0225" pos="-0.85 0 0.0425" mass="0.02" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_rail_left" type="box" size="0.04 0.01 0.02" pos="-0.8 0.055 0.04" mass="0.01" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_rail_right" type="box" size="0.04 0.01 0.02" pos="-0.8 -0.055 0.04" mass="0.01" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      </body>
    </body>

    <!-- Ball, resting in the cup at the arm tip -->
    <body name="ball" pos="-0.8 0 0.56">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.268" condim="6" friction="1 0.02 0.02" solref="0.005 1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <!-- Bucket: centre 3 m (in x) from the ball start, open octagonal cup -->
    <body name="bucket" pos="2.2 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.33 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_0" type="box" size="0.01 0.133 0.165" pos="0.31 0 0.185" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_1" type="box" size="0.01 0.133 0.165" pos="0.2192 0.2192 0.185" euler="0 0 0.7854" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_2" type="box" size="0.01 0.133 0.165" pos="0 0.31 0.185" euler="0 0 1.5708" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_3" type="box" size="0.01 0.133 0.165" pos="-0.2192 0.2192 0.185" euler="0 0 2.3562" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_4" type="box" size="0.01 0.133 0.165" pos="-0.31 0 0.185" euler="0 0 3.1416" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_5" type="box" size="0.01 0.133 0.165" pos="-0.2192 -0.2192 0.185" euler="0 0 3.9270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_6" type="box" size="0.01 0.133 0.165" pos="0 -0.31 0.185" euler="0 0 4.7124" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_7" type="box" size="0.01 0.133 0.165" pos="0.2192 -0.2192 0.185" euler="0 0 5.4978" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="50" ctrllimited="true" ctrlrange="0 10" forcelimited="true" forcerange="-25 25"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.8 0 0.56 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="5.7316"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the physics of a catapult that needs to launch a ball 3 meters horizontally into a bucket, considering whether to use a hinged arm driven by a motor or spring, with the ball resting in a cup at the arm's end.

A velocity-controlled actuator seems more predictable: the arm accelerates rapidly to a target angular velocity, then hits a joint limit stop, launching the ball tangentially at speed equal to angular velocity times arm length. I'm weighing how the ball sits in the cup during rotation, since centripetal force would press it against the cup walls until release.

Working out the geometry: if the arm rotates from horizontal and stops at 45°, the tip velocity direction becomes roughly (0.707, 0.707) scaled by ωL, giving a natural 45° launch angle. I need to make sure the cup orientation keeps the ball seated against the arm's surface through the swing so it doesn't fly out early, only releasing cleanly once the arm stops.

Checking that the joint limit stop won't cause bouncing or penetration issues that would mess up the release timing — I may need a stiff limit or an alternative mechanical stop to get a clean, repeatable launch.

Once the arm decelerates, the ball continues in a straight line while the pivot's radial distance grows slightly, so a lip at the tip could catch it—unless the lip is kept short. Without any lip, centripetal force during spin-up would need friction alone to hold the ball, which likely isn't sufficient since the only normal force is gravity's component. I'll use a shallow lip, shorter than the ball's radius, so it can still slide free once the arm decelerates.

For the contact solver, I'm tuning the soft-limit parameters so the time constant stays near the minimum allowed given the simulation timestep.

I'm reconsidering whether a joint-limit based release is predictable enough, and working through the physics of when the arm hits its stop: the ball's launch velocity depends on angular velocity at separation, which depends on how quickly the velocity actuator can spin up the arm against its inertia and torque limits, and the ball's release velocity direction is perpendicular to the vector from pivot to ball center.

Now I'm planning the landing geometry: I need the ball to travel 3m horizontally from its starting position to the bucket center, so I'll figure out where the arm releases the ball relative to its start, then solve for launch speed to land inside the bucket at the right height. For the bucket itself, I'm thinking of approximating a cylinder with wall boxes plus a base, using fairly inelastic contact settings so the ball doesn't bounce out, with tall enough walls to contain it as it settles.

Since a flat-bottomed bucket with frictionless rolling would let the ball roll forever, I need rolling resistance so it actually comes to rest by 6 seconds -- I'm considering setting condim to 6 on the ball with torsional/rolling friction parameters to add that decelerating torque.

I'm also deciding the bucket should be a static body (no joint), fixed directly to the world, which is simpler than giving it a free joint. Now I'm working out the arm geometry: pivot height, arm length, and the rotation convention for a hinge about the y-axis so I can compute how the cup's position transforms with angle θ.

The ball will sit on the arm's top face, so I need the face normal to rotate consistently with θ—at rest the normal points straight up, and as the arm swings forward the contact normal tilts accordingly, which determines when the ball slides or launches off.

At release angle θ_stop, I'm computing the ball's world position and velocity by differentiating the arm-tip motion relative to the pivot, accounting for the offset h (half-thickness plus ball radius), then using that velocity's components to find the launch angle via arctangent.

Solving for the angle gives θ≈40.7°, close enough to 45° that I'll just pick θ_stop around 0.7 rad since the real sensitivity issue is speed, not angle. I'm also noting that release actually happens when the arm hits the soft limit and starts decelerating, not exactly at a fixed geometric angle.

Checking the solref/solimp math, the damping coefficient from dampratio 1 gives b≈400 for a 0.005 timeconst, so once the limit becomes active the deceleration is abrupt — essentially the ball releases right at θ_stop, which simplifies things nicely.

Now computing the ball's initial and release positions: it starts at rest at (-0.8, 0.56) relative to the pivot, and at release θ=0.7103 rad, with sin≈0.6521 and cos≈0.7581, I get x_rel≈-0.5674 and z_rel≈0.5672, placing the release point at roughly (-0.5674, 1.0672).

I'm computing the release speed using radius r=sqrt(0.8²+0.06²)≈0.80225 and v=ωr, with the launch direction near 45°. For the target bucket, I'm placing its center at x=2.2 (3 units from the ball's start), estimating rim height around 0.3 and inner radius ~0.25, and aiming the descending trajectory to pass near the rim at x=2.2 before continuing down to settle near the bucket's bottom center.

Solving for u², I get u≈3.215, giving speed v≈4.546 m/s at 45°, so ω≈5.667 rad/s. Checking the rim crossing confirms x lands around 2.105 at the rim height, which fits inside the bucket opening as intended.

Checking the wall clearance confirms the ball stays well above the wall top near x≈1.86. Now I'm worried about range sensitivity: roughly dR/R ≈ 2·dv/v, so a window of about ±6% on range translates to needing speed accuracy within ±3%, which is moderately tight given the velocity actuator's steady-state behavior under gravity torque load.

I estimate the gravity torque with a light arm and a ~0.27 kg ball at radius 0.8 m gives roughly 2.5 N·m, and with kv=1000 the resulting velocity error is negligible (~0.0025 rad/s out of 5.67). I still need to check stability of the explicit-Euler velocity actuator, since kv/I·dt must stay below 2, and I'm estimating the combined ball+arm inertia to verify that condition holds.

That huge tangential acceleration worries me about contact softness — the ball could penetrate the cup face significantly under such impulsive loading, so I'm checking whether the soft contact parameters would let the ball bounce off or lag unrealistically rather than staying seated.

So instead of relying on raw high torque, I should limit the actuator force and accelerate the arm more gradually: computing the needed angular acceleration to reach the target angular velocity before the stop angle, then picking something like 60 rad/s² so the ball's tangential acceleration stays reasonable and contact penetration is small.

I'm also checking that stiffening the ball contact parameters keeps penetration down to roughly a millimeter while still being compatible with the simulation timestep, and confirming the centripetal force at full speed is something the lip geometry can hold with stiff contact. Then I need to verify the arm actually reaches target velocity by the stop angle given the force-limited actuator dynamics as it converges.

Now I'm working through the arm and cup geometry dimensions — sizing the arm box, positioning the ball relative to the lip, and checking that the lip height clears the ball radius so the contact geometry actually makes sense.

Then I'm tracing what happens on release: the ball moves outward in a straight line relative to the rotating arm frame, so I need to check whether that straight-line path actually carries it radially into the lip or away from it, since that determines whether it gets caught again after launch.

I'm reconsidering the lip geometry — trying a shorter lip so contact happens near the ball's lower region, checking whether the lip edge actually reaches the sphere surface at different heights, and adjusting the lip's top z-position until the edge-to-center distance falls within the ball's radius.

Actually I should check the release direction properly: the tangential velocity from rotation should point perpendicular to the radius vector from pivot to ball, and I need to verify whether that direction pushes the ball toward or away from the lip in the arm's local frame.

I'll keep the lip slightly above ball-center contact height, which should be fine, and I should add small side rails near the ball to prevent lateral rolling, keeping clearance just larger than the ball radius. Now I'm thinking through arm inertia — picking a density for the arm geometry so the mass works out reasonably for the box dimensions.

Computing moment of inertia about the pivot for both ball and arm, I estimate the gravity torque at the starting angle is around 4.65 N·m, and with a torque limit of ±25 N·m the resulting angular acceleration is roughly 62 rad/s². That gets the arm to the target angular velocity well within the allowed swing angle, with peak tangential acceleration on the ball around 50 m/s² — all within reasonable bounds.

Now checking the velocity gain: with kv=200 the steady-state tracking error from gravity torque is small (~0.35% of speed), and bumping kv to 500 shrinks that further to under 1%. I'm weighing whether implicitfast integration properly accounts for force clamping in its derivative computation, since that affects stability when the actuator saturates near the force limit.

But if clamping isn't respected in the derivative, the implicit integration effectively adds extra damping while clamped — at kv=500 this cuts effective acceleration by roughly 75%, which isn't enough to reach the target angle in time, so that's too risky. Dialing kv back to 50 instead only reduces effective acceleration by about 23%, which seems safer.

Now I'm working out the steady-state velocity error: the gravity torque at the stopping angle comes out around 3.52 N·m once I include the full arm mass, giving an error of about 0.07 rad/s against kv=50, so I bump the control setpoint to 5.737 to compensate. I still need to check whether the system actually reaches steady state by the time it hits that angle, which depends on the velocity loop's time constant of I/kv.

Checking that time constant gives roughly 6.6 ms, so there's plenty of margin before release. I'm also weighing whether to worry about the actuator/gravity interplay versus just leaning on joint damping or gravcomp, but since I can't gravcomp the ball itself, I'll leave it as is. For integration, I verify that Euler stability holds here since kv*dt/I comes out to about 0.3, well under the threshold of 2, so Euler integration should be stable for this setup, and implicitfast would work fine too.

I'm also checking the joint limit configuration - the arm starts right at its lower limit boundary but is moving away so that's fine, and I need the time constant for the limit softness to be at least twice the timestep, so I'll set it around 0.005. Estimating the penetration overshoot from the angular velocity and damping, it comes out to roughly 0.03 radians, which seems acceptable.

I'm now checking where the released ball travels and confirming it clears the pivot supports and frame posts without any unintended collisions along its trajectory.

I also want to make sure the arm itself doesn't clip the support posts as it swings—since the gap between arm width and post spacing is tight, I may need to adjust contype/conaffinity bits so parent-child frame and arm geoms don't register spurious contacts.

I should just focus on spacing geometry properly to avoid overlaps: posts with gaps from the arm, a pin that's visual-only with contacts disabled, and side rails positioned to leave a small clearance around the ball. I also need to figure out the ball's initial resting position relative to the arm's pivot when the arm angle is zero.

Now I'm setting the bucket's position offset from the arm pivot and laying out its geometry — a base cylinder plus an octagonal ring of boxes approximating circular walls, sized to a given inner apothem and wall thickness.

Computing impact velocity: vz reaches about -5.49 at t≈0.887s when it hits bottom, with the stiff damped contact limiting bounce. Horizontally it's moving around 3.2 m/s toward the far wall 0.2m away, so it'll strike that wall hard before friction and rolling resistance settle it, since there's no ramp for it to climb the vertical wall.

Plugging numbers gives deceleration around 3.5 m/s², enough to stop rolling within a fraction of a second, which seems reasonable. I'm also checking that rolling friction doesn't matter while the ball sits on the arm, and that spin gained in flight has no aerodynamic consequence, before moving on to the ball's mass and contact solver settings.

Since solref values get averaged between contacting geoms, mixing the ball's softer solref with a stiffer default produces too much stiffness and noticeable penetration under high acceleration—around 7-8mm, which is too much. So I should set matching solref values on the arm, bucket, and floor geoms too, keeping solimp at its default since that's fine. I'm also confirming that arm-ball penetration during centripetal loading stays acceptable before moving on to check the actuator ramp and ball dynamics.

Working through the spin-up dynamics now: with torque clamped at 25 Nm and kv=50, the time constant comes out to about 6.6ms, and the stability factor checks out around 0.3, which is fine even though the effective inertia changes slightly depending on whether the ball is coupled to the arm. I'm being careful about mass assignments for the arm box and other components to make sure the inertia calculation is accurate before pinning down the exact angular velocity at the release point using the steady-state torque balance equation.

Now I'm computing the gravity torque at the stop angle precisely, working out the ball's horizontal lever arm distance from the pivot to get the torque magnitude, then defining the arm's component geometries (main arm box, lip, and rails) with their specific sizes, positions, and masses to nail down the arm's own center of mass contribution.

Computing the torque contributions: the main arm mass at (-0.4,0) gives roughly 1.487 N·m, and the small lip mass at (-0.85,0.0425) adds about 0.121 N·m, both working in the same rotational direction at this angle.

Adding the rails contribution of about 0.114 N·m, the arm torque totals 1.722 N·m, and combining with the ball's 1.492 N·m gives roughly 3.214 N·m overall. I'm also checking whether angular acceleration effects or centripetal terms from the ball add anything beyond the gravity torque already accounted for, and it seems they don't contribute separately since the ball's tangential dynamics are already captured in that gravity-driven torque term.

Solving for control input, ω = ctrl - 3.214/50 = ctrl - 0.0643, and since I want ω = 5.667, that gives ctrl ≈ 5.731. Now I want to double-check the target speed more carefully using the exact stopping angle: with tanθ = 0.74/0.86, I get θ ≈ 0.7102 rad, sinθ ≈ 0.65224, cosθ ≈ 0.75801. Computing the velocity direction components from these values gives approximately (0.5673, 0.5673), which lines up nicely with a 45° launch direction.

Computing the release position relative to the pivot gives roughly (-0.5673, 0.5673), which is a pleasing symmetric result -- and in world coordinates with the pivot at (0, 0.5), that puts the release point near (-0.5673, 1.0673). I'm now considering exactly when release occurs, which should be when the arm hits its soft angular limit near θ≈0.71.

For the target, I want the ball's center to pass through z=0.2 at x=2.2 (relative offset from the ball's start at x=-0.8, so x=2.2 absolute). Using u=3.215 for matched vx and vz, I get v≈4.5466, and with r=√(0.64+0.0036)≈0.80225, that gives ω≈5.6673 and ctrl≈5.732, consistent with my earlier estimate. Now I'm verifying the entry window against the bucket's inner walls, positioned at x=1.9 and x=2.5 with an apothem of 0.3.

Checking clearances at the rim plane (x=2.105): the ball should clear the far wall comfortably since it hits bottom around x=2.284, well before the far wall's effective edge near 2.46, giving about a 6% speed tolerance margin (~3% on velocity). For the near wall, I need the ball's height to clear the wall top near x=1.88–1.90 at z>0.39, and comparing distances (2.672 needed vs 2.507 available) gives a similar ~6% margin, so roughly ±3% speed tolerance there too. I'm now considering whether my ω estimate holds up within that tolerance, accounting for possible errors from Euler integration during flight (which should be negligible) and from the release dynamics itself -- specifically, the small penetration depth caused by the ball being pressed into the arm face by gravity during the constant-ω phase, estimated as the gravity component divided by the contact stiffness.

This penetration is tiny, and when the arm decelerates, releasing that compressed contact gives only a minor extra push to the ball's velocity, so I'll treat it as negligible. I'm also checking the contact solver parameters between ball and arm, confirming they're consistent and small, then verifying the lip contact handles centripetal loading fine given the stiffness. I'm also confirming the ball's initial position touches the lip with zero gap, that the rail gap is too wide to contact the ball, and that geometric overlaps between the arm box and lip box are fine since they belong to the same body -- all before moving to check the hinge joint setup.

Looking at the hinge joint configuration, I'm checking the limit parameters and confirming the lower limit isn't active since the motor pushes positive torque from the start and the actuator force gets clamped to 25 Nm. I'm now computing the initial gravitational torque on the arm by summing contributions from the box, lip, rails, pin, and ball, then computing the total rotational inertia by adding up each component's contribution, giving me an angular acceleration around 65.6 rad/s² — letting me estimate the time and angle at which the arm reaches its clamped angular velocity.

Now I'm working through the physical layout: setting the ball's mass from its volume and density, placing the support posts and base relative to the arm's pivot, and checking whether the rails, lip, and arm width clear the posts without collision. I'm also verifying the base dimensions don't interfere with the arm's short end as it rotates.

The joint limit itself will act as the mechanical stop, so I'm skipping a separate decorative crossbar. I'll set the floor plane size and move on to placing the bucket.

For the keyframe, I'm setting the starting qpos values, ordering the arm joint first followed by the ball's freejoint position and orientation.

I'm checking ball placement against the arm's resting geometry—arm top face at pivot z 0.52, so with ball radius 0.04, z=0.56 puts it just resting on the arm, which works since it settles slightly under gravity but starts essentially at rest.

I need to confirm the ball's freejoint position matches this keyframe, and verify no collision occurs between arm and ball after release—the arm overshoots briefly but decelerates fast enough that the ball has already moved clear. Then I need to work out the flight timing so the ball lands and comes to rest well before the 6s mark, tracing through the acceleration phase to reach the launch angle.

Now I'm sketching the bucket geometry: a cylindrical bottom, octagonal walls made of overlapping boxes at specific radii and heights, and making sure these contact surfaces interface properly with the floor.

I'm also checking the ball's contact parameters—condim 6 with torsional/rolling friction values—confirming they won't meaningfully interfere during the launch phase or while the ball settles against the bucket wall.

For solver stiffness, I'm planning to use a slightly softer solref for the ball compared to other geoms, so the mixed contact with the bucket is gentler for landing while still handling the 5.5 m/s impact fine.

Now I'm computing positions for an octagonal wall arrangement, placing each wall segment at 45-degree increments around the ring using cosine/sine values scaled by the radius.

For the catapult motor, I'm defining a velocity actuator on the hinge joint with a kv gain of 50 and a force range limited to ±25, then setting its control range to "0 10" since velocity actuators don't have a default ctrlrange.

I realize I need to switch the compiler's angle setting to radians since joint ranges use the same units as the euler angle convention, so I'm converting the hinge range and wall euler angles accordingly—using values like 0.7854, 1.5708, 2.3562, and so on for evenly spaced wall orientations around the circle. I'm also working out the stop angle by computing arctan of the ratio between the two coordinates to pin down the exact threshold value.

Separately, I'm computing the release control value by adding the gravity torque compensation term, and estimating the lag effect from changing gravity torque as the arm rotates—differentiating the torque with respect to angle and multiplying by angular velocity to get the rate of change, then using that to figure out the steady-state velocity tracking error relative to the velocity gain.

