This is a torque-driven throwing arm. A constant motor torque swings the arm through 40.4° until it reaches a stiff joint limit. At that point the ball leaves the cup at about 4.65 m/s, 45° upward, and should drop into a bucket 3 m away. I have not run it in MuJoCo, so this is a hand calculation.

How the numbers were chosen:
- **Release point:** the ball is released at (0.218, 1.032).
- **Target:** to cross the rim height z = 0.3 at x = 3, the ball needs v² = gΔx²/(Δx − Δz) ≈ 21.61 m²/s², so v ≈ 4.648 m/s and ω ≈ 6.178 rad/s.
- **Energy balance:** T·Δθ = ½·I·ω² + ΔPE = 4.188 J + 2.199 J, which gives T ≈ 9.05 N·m.
  - I = 0.2194 kg·m² is the arm plus the ball, which is held in the cup.
- **Joint limit:** set to 40.43° so that the ball's launch direction is exactly 45°.
- **Tolerance:** the bucket's inner radius is 0.3 m. The ball should land in it as long as the launch speed is within about ±3%.
- **Main error sources:** contact compliance and how sharply the joint limit stops the arm. I expect these to be about 1%, but I haven't checked that in simulation.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="radian"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- static catapult frame (visual only, no collisions) -->
    <geom name="catapult_base" type="box" pos="0.75 0 0.02" size="0.3 0.15 0.02" contype="0" conaffinity="0" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_left" type="box" pos="0.75 0.08 0.26" size="0.03 0.02 0.24" contype="0" conaffinity="0" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_right" type="box" pos="0.75 -0.08 0.26" size="0.03 0.02 0.24" contype="0" conaffinity="0" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0.75 -0.1 0.5 0.75 0.1 0.5" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- throwing arm: pivot at (0.75, 0, 0.5), points along -x at q = 0, swings up about +y -->
    <body name="catapult_arm" pos="0.75 0 0.5">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 0.705569" solreflimit="0.005 1"/>
      <geom name="catapult_beam" type="box" pos="-0.4 0 0" size="0.4 0.04 0.02" mass="0.5" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_lip_outer" type="box" pos="-0.8 0 0.045" size="0.01 0.04 0.025" mass="0.05" solref="0.005 1" rgba="0.4 0.25 0.1 1"/>
      <geom name="catapult_lip_inner" type="box" pos="-0.69 0 0.045" size="0.01 0.04 0.025" mass="0.05" solref="0.005 1" rgba="0.4 0.25 0.1 1"/>
    </body>

    <!-- ball resting in the cup, touching the arm surface and the outer lip -->
    <body name="ball" pos="0 0 0.56">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.005 1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <!-- bucket centred 3 m (horizontally) from the ball start, inner radius 0.30, rim at z = 0.3 -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.32 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0.15" euler="0 0 0" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.26847 0.155 0.15" euler="0 0 0.5236" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.155 0.26847 0.15" euler="0 0 1.0472" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.31 0.15" euler="0 0 1.5708" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.155 0.26847 0.15" euler="0 0 2.0944" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.26847 0.155 0.15" euler="0 0 2.6180" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.31 0 0.15" euler="0 0 3.1416" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.26847 -0.155 0.15" euler="0 0 3.6652" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.155 -0.26847 0.15" euler="0 0 4.1888" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.31 0.15" euler="0 0 4.7124" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.155 -0.26847 0.15" euler="0 0 5.2360" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.26847 -0.155 0.15" euler="0 0 5.7596" size="0.01 0.085 0.15" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 20"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="9.05"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that launches a ball 3 meters into a bucket, which means thinking through the physics carefully. I'm considering a hinged arm driven by a motor or spring, with the ball sitting in a cup at the end, and using a joint range limit to act as a stop so the arm releases the ball at the right trajectory.

The ball should start at rest, so the arm can't already be moving when the ball is placed -- otherwise it'd collide unpredictably. A velocity actuator on the hinge seems like the cleanest approach: the arm spins up to a near-constant angular velocity and then gets stopped abruptly by a joint limit, launching the ball at a predictable speed and angle at that stop point.

The tricky part is keeping the ball in the cup during acceleration -- it needs centripetal support, so a flat plate alone won't hold it. I'm thinking a basket shape with a back plate (radial support) and an outer lip could work: at release, the ball moves tangentially away from the back plate while sliding harmlessly along the lip, as long as the lip is positioned to not block that tangential path.

Now I'm setting up the geometry: hinge along the y-axis, arm swinging in the x-z plane, launching toward +x with the bucket centered about 3 meters horizontally from the ball's starting point. I'm working out how the arm starts pointing backward and rotates upward until it stops at some angle, trying to pin down the exact rotation direction and stopping point for the throw.

Checking that the arm tip velocity at φ=180 points upward, confirming the ball resting on top gets pushed correctly, then releasing at φ=135 for a 45° swing with velocity directed up and toward +x. I'm weighing whether to start the arm lower instead, but a ball resting on an angled arm without a cup would just roll off, so sticking with the 180° start makes more sense.

Working out the hinge joint math: defining joint angle q so q=0 corresponds to φ=180, with the hinge axis along +y, and deriving that φ = 180−q. This means I can set the axis to the y-direction and give the joint a range from 0 to 45 degrees (0.785 rad) to match the desired swing.

I should be explicit about using radians in the compiler settings rather than relying on the MJCF default of degrees, to avoid unit confusion. I'm also thinking through what happens when the arm hits the joint limit at speed with a velocity actuator still commanding motion into the stop — the actuator keeps pushing with force bounded by its gain, the constraint resists, and with the default solver reference timeconstant the arm decelerates over roughly tens of milliseconds, which should keep things physically reasonable without excessive bounce or penetration.

Since the launch is near 45°, small overshoot in release angle barely affects range, so the bigger sensitivity is in release speed, where the error scales roughly linearly with speed but quadratically into range — meaning I need the bucket to have decent tolerance, maybe a 0.25 m inner radius, to absorb that. I'm also considering whether a hard mechanical stop would be a more robust alternative to relying purely on the joint limit constraint.

Thinking about the ball's dynamics in the cup: its release velocity is ω times the radial distance from the hinge, assuming it rides along with the arm without slipping, which requires enough centripetal force from the cup walls — with ω around 10 rad/s and r near 1 m, that's roughly 100 m/s² of centripetal acceleration the cup needs to supply, so the pocket geometry (a pushing face plus an end wall) needs to be solid enough to contain the ball through the swing.

So for the lip to work, its height needs to be short enough that the ball only contacts it below the equator, meaning the lip's normal force pushes the ball both inward and against the arm surface rather than blocking it outward entirely—so the ball stays wedged in the corner between the arm surface and the lip until it rotates enough to clear it.

I'm trying to work out the geometry of ball clearing the lip edge using the arm's rotating reference frame, where the ball's centrifugal drift over tangential distance s follows s²/(2R), and I need to find when contact occurs at the lip's top corner as the ball moves along the arm surface.

Since the ball's release velocity is perpendicular to the radial line through its (slightly offset) center rather than through the arm axis itself, its path tilts at a small angle relative to the lip face—roughly atan(offset/r)—rather than being exactly parallel to it as I'd assumed.

Actually the centripetal requirement has a −d component that the arm surface can't provide by pushing, since it only pushes outward (+d); this must come from lip friction instead. Checking the ratio, friction from the lip (μ times the normal force) easily exceeds the small ω²d term as long as μ is above roughly 0.05, so the lip's friction keeps the ball seated against the surface despite the tiny outward drift.

But with only one contact point at the lip, the ball could roll up the lip face driven by that same ω²d forcing term, with effective rolling acceleration of 5/7 ω²d. Plugging in ω=10 and d=0.06 gives roughly 3 m/s², so over a tenth of a second the ball might drift on the order of a centimeter or so.

But checking gravity: when the arm is horizontal, gravity actually presses the ball onto the lip surface rather than away, and at the 135° position its component along d (~0.707 g, about 7) exceeds the ω²d outward term (6), so the ball stays seated. The release speed also depends on actual actuator angular velocity times the ball's radial position, so I should account for actuator inertia rather than assuming instantaneous ω.

For the velocity actuator, I'm using a high gain kv with no force limit so the arm tracks its commanded velocity quickly, but explicit Euler integration could go unstable with such high gains — switching to implicitfast integration handles the actuator's velocity derivative implicitly, so large kv stays stable. With implicitfast, the steady-state tracking error from gravity torque becomes small since it scales as torque/kv.

Working through the time constant I/kv, the arm's rotational inertia is tiny, so it reaches full commanded speed in roughly a millisecond — meaning the ball sitting on the arm gets struck almost instantaneously, and since the default contact solver is critically damped, I need to think about whether this causes a sudden launch or a smooth push.

I decide it's better to soften the gain so the arm ramps up over roughly 5-10 ms instead, giving a gentler pickup that still reaches near full speed well before the 45-degree swing completes.

Wait, the default contact solref timeconst of 0.02s is slower than my arm ramp time, meaning the ball would penetrate deeply into the arm surface before the spring-damper pushes back—potentially tunneling through. I need a gentler ramp with τ much greater than 0.02s, but that requires more swing angle than is practical, so maybe a constant-torque motor is a better approach instead of velocity ramping.

A torque-driven arm is analytically tractable: I can compute release speed from energy balance—torque times swept angle equals kinetic energy gained plus potential energy change, using the total rotational inertia including the arm, the ball's point mass at its radius, and the ball's own spin inertia since it co-rotates rigidly with the arm (assuming friction keeps it from sliding in its pocket).

Working out the angular acceleration needed to hit ω=8 rad/s over a 45° swing gives about 40.7 rad/s², meaning the ball experiences roughly 4g tangential acceleration—I'm now checking whether the contact stiffness and timeconst can handle that without excessive penetration, working through the steady-state contact reference acceleration formula tied to the solref parameters.

With the default solref, penetration under this acceleration could reach a centimeter or more, which is too soft, so I'm stiffening the ball's contact (smaller time constant like 0.005-0.006) to cut penetration down to about a millimeter, while keeping it at least double the simulation timestep for stability.

Now I'm thinking through the release dynamics: since the joint limit has a damping ratio of 1, the arm shouldn't bounce when it hits the stop, but it does keep pushing against the limit while the ball continues moving with the tangential velocity I calculated. I need to figure out the exact release angle, factoring in the arm's position at the moment it stops plus any additional travel during deceleration.

Gravity helps keep the ball seated against the arm until release, so that's fine. For the keyframe, I need the ball starting at rest in the pocket and the arm at rest at q=0, which means working out the qpos ordering carefully depending on body tree order — I'll structure the XML with the arm body first, then the ball, then a static bucket body with no joint.

Actually, I realize I can simplify this: instead of specifying full qpos in the keyframe, I can just rely on qpos0 defaults for the arm and ball positions and only specify ctrl in the keyframe, since omitted qpos defaults to the model's initial qpos0 anyway. That means the simulation resets to that keyframe with ctrl active from t=0, which is exactly what I want. Now I'm figuring out the geometry and where to place the pivot point.

I'm working out the lip geometry so the ball rests against its inner face at a=0.79 while the lip itself spans a small radial band—checking that the lip height exceeds the ball's center offset so it actually contains the ball. I also need to confirm that with the arm starting horizontal, the ball won't roll inward prematurely since there's no slope to drive it before release.

I'll give the inner lip a small gap too, placing its face at a=0.70, and confirm the ball separates cleanly since it's drifting slightly inward. Computing the ball's actual radial distance from center gives about 0.7524 m, offset roughly 4.57° from the arm's direction—now I need to work out the ball's release position once the arm stops at angle q_s.

Figuring out the ball's angular position relative to the arm direction φ=180−q, I track how d (the push direction) relates to φ, confirming the geometry matches (−0.997, 0.08). Setting the velocity direction for a 45° upward launch toward +x, I solve ψ−90=45 giving ψ=135, so φ=139.574° and q_s≈40.426°.

I'll just go with a 45° launch angle for simplicity, even though range sensitivity to θ isn't zero given the height difference—I can revisit optimizing it later if needed. Now I'm computing the release position: with the pivot at height 0.5, the ball's center at release sits at x_p − 0.532 horizontally and 1.032 vertically, and I'm working out the ball's starting x-coordinate using the 175.426° angle and the 0.7524 radius.

Setting the start position to x=0 gives x_p = 0.75, so the release point becomes x=0.21797, z=1.03203, with the bucket centered at x=3. Now I'm figuring out the target entry height into the bucket, which sits on the floor with a 0.3m rim and 0.25 inner radius, aiming for the trajectory to pass through the bucket opening near its center.

Aiming for the ball center to cross the rim plane near x=3.0 gives decent tolerance either way (±0.21), and since the bucket walls will catch bounces without much restitution, hitting the far wall and settling inside should still count as success.

Now I'm solving for the launch speed at 45°: with start point roughly (0.218, 1.032) and target (3.0, 0.3), I set up the projectile equation using Δx=2.782 and Δz=−0.732, then solve for v² using g=9.81, getting v²≈21.6 so v≈4.65 m/s.

With that speed I compute angular velocity ω=v/r_c≈6.18 rad/s, confirm flight time via horizontal speed (~0.846 s), and note no drag is involved. Now I'm moving on to energy balance, setting up torque times the angular swing Δq (0.706 rad) equal to the kinetic plus potential energy change needed for the motion.

Now I'm defining the arm's geometry for the inertia calculation — placing the pivot, setting the beam as a lightweight 0.5 kg box extending along the negative x-axis, and positioning an outer lip box further out to represent the catapult's throwing end.

I'm working out the lip positions: outer lip centered near x=−0.80 spanning a small z-range above the ball's resting height, giving a well shape, with a lighter inner lip at x=−0.69 forming the other wall so the ball sits in a shallow pocket at drop time. Mass for each lip set at 0.05 kg.

Now I'm checking whether the ball clears the lip edge during release, comparing the ball's resting height against the lip's top height to make sure the geometry allows it to launch rather than catch on the rim.

I also need to make sure the catapult's static support posts and base don't collide with the arm or ball during motion, so I'm thinking through contype/conaffinity settings to disable collisions among the catapult's own static parts while keeping the dynamic ball and arm interactions intact.

I'll disable collisions on static catapult parts since they're fixed anyway, keeping arm-ball and ball-bucket collisions active while checking the arm clears the floor and frame at its resting angle. Now I'm computing the arm's moment of inertia about the hinge axis, treating the beam as a box and using the standard parallel-axis formula for its mass distribution.

I'm summing up the inertia contributions from the beam, outer lip, and inner lip — each shifted by their offset distance from the hinge — to get a total arm inertia around 0.1628, then I'll add the hinge's own contribution.

Adding the ball's inertia (both its translational term about the hinge and its own spin term since it rotates with the arm) gives a total system inertia of about 0.2194. Using this with the angular velocity at release, I compute the kinetic energy at release to be roughly 4.188, and now I'm starting to work out the potential energy change by finding the arm's center of mass position in the body frame.

Computing the updated sine and cosine values, I get the arm's center-of-mass height change and resulting potential energy of about 1.7357 J. Then for the ball starting at (−0.75, 0.06) in the body frame, I calculate its height change comes out to roughly 0.472, matching my earlier release-point check.

Adding this to the arm's PE gives total potential energy of 2.19874 J, and combining with kinetic energy of 4.18768 J gives total energy of 6.38642 J, so required torque is about 9.0514 N·m. I double-check the release angle q_s using atan(0.08) and confirm it's 0.705569 rad, consistent with before. Now I want to verify the ball stays in contact with the arm throughout the swing by checking the initial angular acceleration against gravity torque at q=0.

I compute gravity torque at the start: arm contributes 2.693 N·m and ball contributes 0.736 N·m, totaling 3.429 N·m, giving net angular acceleration of about 25.6 rad/s² — the ball should stay pressed against the arm. I then check at the stop angle q_s whether net torque remains positive, computing the horizontal distances of the arm and ball COM from the pivot to get updated gravity torque contributions there.

Checking whether the torque stays positive at the limit, I get a total around 2.54 N·m versus the control torque of 9.05 N·m, so the arm keeps accelerating throughout. I verify the ball stays pressed against the surface by comparing centrifugal and tangential acceleration components — the tangential acceleration dominates, confirming the ball remains firmly in contact. I note the constant control torque persists once the arm is pinned at the limit, and flag contact compliance (small deformation at the ball-surface interface affecting the radius) as a remaining uncertainty.

Checking the initial setup, the ball starts touching both the surface and lip exactly at the boundary positions, so it'll settle by a few millimeters due to solver stiffness. I estimate the sensitivity of range changes to this settling is small, with contact penetration of about 2mm only shifting the radius by roughly 0.3%. I also consider how MuJoCo's joint limit constraint only activates once the position exceeds the range with zero margin, which matters for how cleanly release occurs just past that point.

Once the arm starts decelerating at q_s, the ball separates naturally since gravity pulls it toward the surface at a much gentler rate than the arm's deceleration — so that separation behavior looks correct. The joint starts exactly at its lower limit with torque pushing it away, which should be fine, so I'm setting the range to 0 to 0.705569 with explicit limited="true". For solreflimit, I need a timeconst of at least twice the timestep, so I'll use 0.005 instead of 0.004.

Checking the arm's release speed and inertia, then verifying the ball's trajectory clears the arm itself as it decelerates past the release point. I'm also checking whether the ball clears the bucket rim near x=2.75, working out the ball's height at that horizontal offset using the projectile equation.

I find the ball crosses the rim well above it at a steep ~57° descent angle, then lands on the bucket floor around x=3.157 before sliding into the far wall — confirming a good landing with some margin to spare given the tolerance on the rim crossing zone.

Given the ~3.5% sensitivity to speed, I decide to enlarge the bucket's inner radius to 0.3 for safety margin, widening the acceptable crossing range to roughly (2.74, 3.26), which still reads clearly as a bucket. For construction, I'm approximating the circular wall using primitives — a floor disc plus a ring made of 12 boxes arranged around the inner radius, working out each box's tangential width from the circle geometry.

Calculating box positions...

For the catapult frame visual, I'm sketching a base box with two uprights supporting an axle cylinder, all set with no collision so they're purely decorative. I'm naming each piece with a catapult prefix and double-checking that the arm's rotation won't visually clash with the support posts.

Checking contact solver parameters—since the ball's soft solref averages with the arm's default value during contact mixing, I should set matching solref values on the arm geoms so collisions feel consistent, while leaving the bucket soft for catching the ball properly.

Thinking through the motor actuator setup with gear ratio and ctrlrange bounds, plus the keyframe control value. I'm also reasoning about whether the ball could roll when wedged against the lip and surface—friction and the pyramidal contact model should keep it effectively locked in place, with inertia computed automatically from the geom masses on the arm body.

Checking the ball's inertia matches a solid sphere formula, verifying the floor plane dimensions, and confirming the arm starts exactly at its joint limit with soft constraint settings preventing overshoot. I'm also checking how sensitive the projectile range is to small variations in release angle—seems mild given the drop height involved.

I'm also considering contact compliance effects: the ball slightly penetrates the surface under centripetal acceleration, and this small penetration depth could release extra spring-back velocity upon separation, though the magnitude looks negligible compared to the main launch velocity.

Since damping is critical and the arm decelerates during the unload time, that spring rebound effect is probably under 1%, well within the 3.5% tolerance, so I'll move forward without further correction.

Now I'm working out the bucket wall positions around the circle, computing coordinates for each segment based on radius 0.31.

Writing arm body XML...

I'm double-checking the hinge rotation direction about the y-axis confirms the beam tip moves upward as expected, then verifying the ball's rotated position matches the target angle of 135° — the math checks out with x' and z' both equal at roughly 0.532. Now confirming the motor applies positive torque about the +y axis.

For the static catapult structure, I'm laying out the base box, side posts, and axle cylinder dimensions as fixed geometry, deciding to skip adding a stop crossbar for simplicity. I'm recomputing total kinetic energy terms carefully, working through moment of inertia, radius, velocity, and angular velocity values to get ω² ≈ 38.1671.

With KE ≈ 4.18768 and PE ≈ 2.19874, the sum divided out gives a control value of roughly 9.05, which I'll use as the ctrl setting. Now I'm moving on to finalize lighting and write up the complete setup.

