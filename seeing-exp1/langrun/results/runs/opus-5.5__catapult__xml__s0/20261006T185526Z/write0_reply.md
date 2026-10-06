The catapult is a spring-free, motor-driven arm. A filtered velocity servo spins it to a fixed angular speed. A hard stop then halts it at 40°, and the ball leaves the cup at about 4.70 m/s, roughly 46° above horizontal.

**Geometry**
- The ball starts at (−0.9, 0, 0.56).
- The bucket's centre is at (2.1, 0, 0.56), 3 m away both horizontally and in a straight line. The bucket sits on a stand to make that true.
- The bucket's inner radius is 0.30 m. Its rim is at z = 0.72 and its floor at z = 0.44.

**Hand-calculated flight (not simulated)**
- The ball should clear the near rim with about 0.14 m to spare.
- It should land about 1 cm past the bucket centre.
- The bucket's inner radius allows roughly ±3% error in launch speed.
- I haven't checked whether the ball stays in the bucket after landing. It arrives moving about 3 m/s horizontally and may roll against the far wall, which is 0.28 m high.

**Why the `implicitfast` integrator**
- The servo is stiff, and `implicitfast` keeps it stable at the 0.002 s timestep.
- The servo's control target is 5.233 rad/s. This makes up for its small steady lag against gravity, which is 1.74 N·m at release.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.85 0.8 1"/>

    <!-- catapult frame (visual only, does not collide) -->
    <geom name="catapult_base" type="box" pos="-0.3 0 0.03" size="0.7 0.2 0.03" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_post_left" type="box" pos="0 0.12 0.28" size="0.02 0.02 0.22" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.12 0.28" size="0.02 0.02 0.22" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_axle" type="cylinder" fromto="0 -0.14 0.5 0 0.14 0.5" size="0.015" rgba="0.3 0.3 0.3 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_post_left" type="capsule" fromto="-0.28 0.12 0.06 -0.2839 0.12 0.7839" size="0.012" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_post_right" type="capsule" fromto="-0.28 -0.12 0.06 -0.2839 -0.12 0.7839" size="0.012" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_bar" type="cylinder" fromto="-0.2839 -0.14 0.7839 -0.2839 0.14 0.7839" size="0.015" rgba="0.3 0.3 0.3 1" contype="0" conaffinity="0"/>

    <!-- catapult arm: pivot at z=0.5, angle 0 = pointing along -x, rotates up to 40 deg -->
    <body name="catapult_arm" pos="0 0 0.5">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 40" limited="true" solreflimit="0.006 1"/>
      <geom name="catapult_beam" type="box" pos="-0.43 0 0" size="0.53 0.04 0.02" mass="0.3" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_wall" type="box" pos="-0.95 0 0.06" size="0.01 0.04 0.04" mass="0.02" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
    </body>

    <!-- ball resting on the arm against the cup wall -->
    <body name="ball" pos="-0.9 0 0.56">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.005 1" rgba="0.85 0.1 0.1 1"/>
    </body>

    <!-- stand under the bucket -->
    <geom name="stand" type="cylinder" pos="2.1 0 0.2" size="0.15 0.2" rgba="0.5 0.5 0.55 1"/>

    <!-- bucket: centre exactly 3 m from the ball's start -->
    <body name="bucket" pos="2.1 0 0.56">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 -0.14" size="0.32 0.02" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0" euler="0 0 0" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2864 0.1186 0" euler="0 0 22.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.2192 0.2192 0" euler="0 0 45" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0.1186 0.2864 0" euler="0 0 67.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="0 0.31 0" euler="0 0 90" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.1186 0.2864 0" euler="0 0 112.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.2192 0.2192 0" euler="0 0 135" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2864 0.1186 0" euler="0 0 157.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.31 0 0" euler="0 0 180" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="-0.2864 -0.1186 0" euler="0 0 202.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="-0.2192 -0.2192 0" euler="0 0 225" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="-0.1186 -0.2864 0" euler="0 0 247.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_12" type="box" pos="0 -0.31 0" euler="0 0 270" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_13" type="box" pos="0.1186 -0.2864 0" euler="0 0 292.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_14" type="box" pos="0.2192 -0.2192 0" euler="0 0 315" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_15" type="box" pos="0.2864 -0.1186 0" euler="0 0 337.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <!-- velocity servo with a filtered (smoothly ramping) target: torque = 100*(act - qvel), act -> ctrl with tau 0.02 s -->
    <general name="catapult_motor" joint="catapult_hinge" dyntype="filter" dynprm="0.02" gaintype="fixed" gainprm="100" biastype="affine" biasprm="0 0 -100" ctrlrange="0 10" ctrllimited="true"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.9 0 0.56 1 0 0 0" qvel="0 0 0 0 0 0 0" act="0" ctrl="5.233"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that actually launches a ball into a bucket 3 meters away, so I'm thinking through the physics: an arm on a hinge driven by a motor or initial velocity, with the ball resting in the arm's cup before launch.

Rather than giving the arm initial velocity directly, a spring-driven hinge with a joint limit seems more controllable—the arm starts rotated away from the spring's rest angle, accelerates under spring torque, then hits a hard stop where the ball releases with whatever tangential velocity it's built up. I'm now setting up the geometry: arm pivoting about the y-axis to throw along x, starting horizontal and rotating upward to release the ball toward the bucket.

Actually the cup needs an outer wall since the ball tends to slide outward from centripetal effects, while tangential acceleration presses it against the cup floor. I'm weighing whether to simulate the release through contact dynamics with a soft joint limit, versus something simpler — precision is tight here, needing the ball to land within roughly 0.2m of a target 3m away, and there are multiple sources of imprecision like release velocity mismatch and rolling in the cup, so maybe avoiding full catapult dynamics is safer.

I can't verify this through simulation directly, so I need to design the bucket generously (say 0.25m radius) and carefully track that the ball's start position differs from its release position, computing the landing relative to the actual release angle. I'm also considering whether a velocity actuator driving the arm to a constant angular velocity, stopped by a joint limit, would give more predictable, kinematic-like motion than a spring-based system.

I'll pick arm mass and kv so the actuator time constant stays short, maybe I/kv around 0.01s. Then I'm checking the ball's dynamics mid-swing: during constant angular velocity the tangential force needed is just gravity's component, so the arm naturally supports the ball, while the centripetal term (ω²r, roughly 49 m/s² at ω~7 rad/s, r=1m) pushes the ball against the cup's outer wall, keeping it seated.

At release, since the ball sits on the leading face of the arm as it swings upward, abrupt stopping lets the ball fly off that leading surface following its tangential velocity, while any residual contact with the outer wall just slides tangentially with minor friction effects.

Actually since the wall is a flat plane perpendicular to the arm and the ball's tangential path runs parallel to that plane, it just slides along the wall surface briefly rather than pressing deeper into it—and once the arm stops, the centripetal requirement disappears so the normal force drops away too. I'll keep the wall height modest, maybe 0.06 m above the arm with a ball radius around 0.04 m, and use a lower friction coefficient (~0.3) on the ball to avoid excessive spin-induced effects.

During the swing, the ball is effectively pinned in the corner where the arm face meets the wall, pressed outward by the acceleration, so it's not really rolling until release. At release it carries the arm's angular velocity as spin, though that won't produce any Magrus-type curving in flight since there's no air density set—spin will only matter once it lands in the bucket. For release velocity, I need to compute the ball center's speed as ω times the actual pivot-to-ball-center distance (accounting for any offset from the arm's face), with direction perpendicular to that pivot-ball line rather than strictly perpendicular to the arm itself.

The joint limit is a soft constraint, so the arm will overshoot slightly and the ball separates gradually over a few milliseconds as the arm decelerates—meanwhile the velocity actuator keeps forcing the arm into the limit, with the constraint absorbing that force. The default solref time constant might let the arm bounce, so I should tighten solreflimit to something like "0.005 1" to reduce overshoot, meaning the actual release angle is close to the limit angle plus a tiny overshoot. I also need to check whether the ball separates from the arm face earlier than the limit, which depends on whether the normal force the face exerts on the ball stays non-negative as gravity's perpendicular component changes during the swing.

Working through the tangential equation of motion for the ball, I confirm the normal force stays positive throughout the swing since the tangent direction always has an upward component as the arm rotates from vertical to 45° back-up, so the ball stays in contact until release. Now I'm setting up the projectile trajectory after launch at 45°, figuring out the launch height and solving for where the ball needs to land to drop into the bucket opening at the target position.

Working out the hinge rotation direction: with axis set to +y, a positive angle rotates the arm from pointing along -x toward +z, so starting at horizontal-back and sweeping up to about 45° makes sense for the throwing motion. Now I need to pin down the release timing within that range.

Launch angle relates to the arm angle α by tangent velocity direction (sinα, cosα), so the throw angle from horizontal ends up being 90°−α — meaning α=45° gives a 45° launch, which works fine for now. I also need to account for the ball's offset on top of the arm, placing its center in the arm's local frame along -x with some vertical offset above the arm's top face plus the ball's radius.

r_b computes to about 0.902. I'll pick α=40°, giving a launch angle around 46.19°, and set up the ball's starting position with pivot height H=0.5, placing the ball near (-0.9, 0, 0.56) at the arm's lower limit before it swings through its range.

I also need to make sure the arm and frame geoms don't collide improperly — since the arm is a child of the world body, MuJoCo's default parent-child collision exclusion should prevent frame-arm contacts, though I should double check how that filter behaves when the parent is the world body itself.

To be safe, I'll mark the frame geoms as purely visual (no collision) since they're static anyway, while keeping the arm geoms collidable with the ball and floor as intended. I'm checking the arm's reach at different pivot angles to confirm it stays clear of the floor.

Now I'm computing the ball's release position at α=40°, working out the trigonometric values for the combined angle to find the exact coordinates relative to the pivot.

The release point comes out to roughly x = -0.651, z = 1.124. Then I work out the launch velocity components from the angular speed and radius, and start setting up the target bucket position, noting it's 3 meters from the ball's starting point.

I'm wrestling with whether that 3-meter distance should be purely horizontal or a true 3D distance, since the bucket's geometric center depends on its height off the floor — if the bucket sits on the ground with some height, its center isn't at the same elevation as the ball's start, which changes the math either way.

One way to satisfy both readings is to elevate the bucket on a stand so its geometric center matches the ball's starting height exactly, making horizontal and 3D distance equivalent. I'm sketching this as a static bucket body positioned at that height, with floor and wall geoms forming the container shape, fixed to the world with no joint needed.

I'm working out the wall construction with 12 boxes arranged around an inner radius of 0.25, plus a bottom cylinder sized to sit just above the stand. Then I'm shifting to the trajectory math, figuring out where the ball's center should be as it crosses the rim height and descends toward the bucket floor, aiming for an x-position near the rim before computing the final drop.

I also need the ball to clear both the near and far rim edges given the bucket's position and radius. I'm working through the projectile equation from the launch point, solving for the trajectory's height at x=2.15 to confirm it lands near the bucket floor at z=0.46.

I solve this to get vx² ≈ 10.737, giving vx ≈ 3.277 and launch speed v ≈ 4.733, which translates to an angular velocity ω ≈ 5.247 rad/s. Now I'm checking the trajectory height at the near rim position (x=1.78) to verify the ball passes above it without hitting.

The value comes out around 0.959, comfortably above the 0.75 threshold. I then check where the descending path crosses the rim plane height, finding a steep slope near x=2.15 (about 56.6°), so the crossing point lands around x≈1.985, well within the acceptable landing band between 1.84 and 2.36. Finally I'm estimating sensitivity—since landing distance scales roughly with v², a 1% error in speed shifts the landing by about 5-6 cm.

Solving for vx² gives about 10.6, so vx≈3.256, v≈4.703, and ω≈5.214. Now I'm checking the rim-plane crossing by solving a quadratic for d at z=0.71 to confirm the trajectory passes through the rim correctly.

I find x≈1.947 at that height, with the ball still clear of the inner wall at 1.80, so the geometry checks out. Now I'm turning to whether the arm's actuator can actually spin up to ω=5.21 fast enough within the joint's motion time (0.134 s), needing to estimate the arm's inertia and the actuator's velocity gain to check the spin-up time constant.

Bumping kv to 500 tightens the time constant to under a millisecond, dropping steady-state error to under 0.2%, though I could also lighten the arm mass to half a kilogram to reduce gravity torque further. I'm weighing whether to just compensate with a slightly higher commanded velocity rather than over-engineer the gains, and considering switching to MuJoCo's native velocity actuator instead of manually tuning kv.

One concern: with kv=400 and implicitfast integration, stability requires kv*dt/I to stay under 2, which explicit Euler can't satisfy here—so implicitfast is mandatory. But I also realize that once the arm hits its 40° limit, the velocity actuator will keep pushing with enormous force (kv times the velocity, over 2000 Nm), meaning the joint limit constraint has to absorb that load, so I need to check how much soft-constraint penetration that implies.

I'm now weighing whether to add a forcerange to cap the actuator torque, say ±30 Nm, and checking whether that still lets the arm spin up to the target angular velocity within the available travel before saturating.

I'm uncertain how MuJoCo's implicit integration treats the derivative when actuator force is clamped — whether the gain derivative term is zeroed out or still applied — and that ambiguity makes me wary of relying on forcerange here, so I'm considering avoiding a velocity actuator altogether.

Instead I'm weighing a constant-torque launch where release velocity comes from work-energy balance (½Iω² = τθ minus gravity work), which depends tightly on arm inertia and ball mass and is precise but fragile to compute exactly, versus a moderate-kv velocity servo without forcerange that spins up quickly (~0.01s time constant, kv≈40) and tolerates steady-state error from gravity torque — and I'm sketching out arm/ball inertia numbers to see if reducing arm mass keeps that error small enough.

Checking the gravity torque contribution at the release angle (~1.65 Nm combined from arm and ball weight) gives roughly a 0.8% velocity error at kv=40, which I could just add back as a feedforward correction to the control target; I'm also noting the resulting actuator force (~210 Nm) and starting to estimate the steady-state constraint penetration under the soft limit settings.

Working through the steady-state balance with impedance factor d gives a tiny penetration of about 0.0014 rad, well within tolerance. Now I'm estimating the overshoot from the arm's arrival velocity of 5.2 rad/s against the 5ms time constant, roughly on the order of 0.026 rad under critical damping.

So the overshoot magnitude comes out to about 0.01 rad, or 0.55°, during which the ball separates from the arm essentially instantaneously once deceleration exceeds gravity's component. Checking the timestep of 0.002s against the 0.005s time constant, MuJoCo's rule of thumb wants timeconst ≥ 2×timestep, so I might bump it to 0.006 for safety. I'm now wondering whether the actuator's spin-up at t=0 could cause an unwanted launch or bounce of the ball right at the start, computing the initial angular acceleration from the velocity-gain term.

This gives an enormous jolt at the ball's end — around 1050 m/s² — which could press the ball hard into the arm face. With the default soft contact (solref 0.02), that pressing force might cause penetration followed by spring-back, potentially bouncing the ball off the arm prematurely. I'm working through whether critical damping limits that rebound, and estimating the steady-state penetration depth using the effective contact stiffness from solref.

But the key subtlety is timing: the acceleration spike only lasts about 0.0045 s, much shorter than the contact's response timescale of 0.02 s, so the ball can't fully react before the arm has already moved on. I'm reasoning through how the relative displacement between ball and arm evolves under a critically damped system, checking whether velocities equalize smoothly without overshoot once gravity and the step-like forcing settle out.

Working through the penetration depth, I find the ball could sink roughly 3.5 cm into a 4 cm-thick arm with the current contact settings, which risks the ball passing straight through — not acceptable. I switch to a stiffer contact (solref 0.004 1), bringing the natural frequency up and cutting the penetration down to about 6.7 mm, which should keep the ball properly contained.

I also try softening the spin-up by lowering kv so the ramp time is around 0.03 s, but that trades off into a steady-state velocity error of roughly 5% due to gravity compensation lagging behind — a real complication since the error also depends on the arm angle during the swing, making this approach messier than I'd like.

A cleaner fix: use an actuator with filter dynamics so activation itself ramps smoothly from the keyframe toward the control target, letting the velocity gain stay high for tight tracking while the commanded velocity rises gradually. I'm setting up a general actuator with dyntype="filter" and a time constant, paired with gain and bias parameters so the output force tracks the filtered activation against velocity feedback.

Working through the numbers, the arm's effective acceleration cap from this filter time constant comes out around 175 rad/s², translating to roughly 158 m/s² at the ball. Checking contact penetration under quasi-steady assumptions with a stiffened solref, I get sub-millimeter penetration (~0.19mm) versus a few millimeters with default stiffness — so tightening the contact solref on the ball or bucket geoms should keep things numerically stable while still allowing a believable bounce with critical damping.

Now I'm estimating the actuator velocity lag: with kv=40 and inertia 0.18, the velocity time constant comes to about 4.5ms. Combining filter and velocity lag delays, total time to sweep the needed angle is about 0.169s, leaving a tiny ~0.36% shortfall in actuation at release — small enough to ignore, though I consider whether tightening τ_f to 0.02 would push peak acceleration higher, up near 262.

Checking the acceleration bound with that tighter filter still looks fine, and the resulting shortfall drops to about 0.04%, negligible. The steady-state gravity error scales as torque/kv, so bumping kv to 100 (using implicitfast) cuts the velocity lag to ~1.8ms and the residual velocity error to about 0.0165 rad/s, a 0.3% deviation — I can just nudge the target angular velocity up slightly to compensate, landing around 5.23. I also confirm that implicitfast properly incorporates the actuator's velocity-dependent bias term in its implicit derivative.

Even using explicit integration, the stability ratio kv·dt/I comes out to about 1.1, which is under the 2.0 threshold but a bit marginal — implicitfast handles it more safely. I also check the joint limit contact force: with the velocity actuator pushing a sizable torque into the limit, the resulting penetration depth works out to roughly 0.005 rad, which is acceptable given the default solimp parameters and the effective damping ratio near 0.95 at that depth.

Checking the ball's trajectory after the arm stops at 40° — it should clear the arm's forward stub since that sits lower and the frame geoms don't collide anyway, so that's fine. Now I'm defining the arm body itself: placed at the pivot height, hinged on the y-axis with a 0-40 degree range, and I'm laying out its geoms in the local frame — starting with the main beam as a box spanning from behind the pivot to just past it, centered off-axis with a specific half-length and thin cross-section.

Still placing geoms...

As the arm spins up, gravity's component along the arm pulls the ball inward while centripetal demand grows with ω²r; at full speed centripetal dominates gravity by a wide margin (24.5 vs 6.3), so I just need to confirm there's no brief window early in spin-up where gravity's inward pull exceeds the centripetal requirement and causes the ball to detach from the outer wall.

Checking the ball's resting position against the beam face confirms it's touching correctly at the keyframe, so settling should be minimal. I'm setting the ball mass to 0.1 and computing the arm's moment of inertia about the pivot using the beam's length and offset, getting a parallel-axis value of about 0.049.

Adding the cup wall inertia (~0.018) and ball contribution (~0.0814) gives a total system inertia of roughly 0.183, which seems reasonable. I'm also working out the gravity torque on the arm and ball at a 40° angle — computing the horizontal lever arm distance and multiplying by weight to get around 0.969 N·m resisting the motion.

I'm reconsidering the contact force where the ball touches the wall, since it's offset from the arm axis by 0.06, creating an additional torque component F times that offset. I need to account for the centripetal force on the ball moving in its circular path of radius r_b, combined with gravity's component along the arm, to get the net force driving that torque correctly.

Actually, stepping back, since the ball spins at constant angular velocity and its angular momentum about the pivot stays constant, the required actuator torque must simply balance the total gravitational torque on the arm-ball system — the contact forces and spin dynamics cancel out in that conservation argument.

That gives τ = 1.742 Nm regardless of internal force details. I'm also checking that kv = 100 gives a small steady-state velocity error, roughly 0.0174 rad/s, with negligible lag effects. The ball's release velocity equals ω_arm × r_b since it moves rigidly in the corner, so I need to confirm it stays fixed there by friction rather than rolling off the face during the rotation.

So target ω_arm works out to about 5.2137, and adding the correction gives a control value around 5.231. I'm now thinking through the separation dynamics as the arm hits its limit — the ball leaves the face contact but briefly retains contact with the wall, and as the arm decelerates past this point, the relative motion between ball and wall becomes more subtle since the wall is still rotating slightly during the overshoot.

I'm also checking whether the ball rolls or slips against the wall: during steady rotation the ball moves rigidly with the arm so there's no slip at the contacts, but once the arm stops, the ball's spin still carries tangential velocity at the contact point that no longer matches the (now stationary) wall, so I need to work out that relative velocity from the spin times radius in the tangential direction.

This relative sliding speed turns out small compared to the ball's translational velocity, and since the normal force drops once the ball no longer needs centripetal support, the resulting friction effect is negligible. I'm keeping the default friction coefficient of 1 for simplicity.

Now I'm working out how the ball separates from the arm's face after release: the ball's velocity is slightly off the face normal (by the small angle δ), so it pulls away from the face at a component v·cos δ while sliding along the face at v·sin δ.

Confirming the ball doesn't clip the arm as it releases - the inward drift is tiny, just 0.0067 per 0.1 rise, so it clears fine. The release timing lines up with when the arm starts decelerating at exactly α=40°, and the joint limit at angle 0 correctly holds the arm against gravity since the limit activates right at the boundary.

Tracing the ball's flight path: apex comes out around z=1.71m, and nothing in the frame geometry should intersect it on the way to the bucket. Checking the bucket geometry now - its cylindrical base and top surface heights, recalculating the contact point for the ball center against the bucket rim since my earlier floor-level assumption was slightly off (0.47 vs 0.46).

I'm also verifying the bucket's wall construction - 16 boxes arranged radially with inner radius 0.30 and small thickness, checking that circumference spacing matches the half-width per segment, and confirming wall heights span from -0.15 to +0.15 to meet the rim height of 0.71.

Now I'm computing the 16 wall-segment positions and orientations around the circle, placing each box at its angle with radial size 0.01, tangential width 0.062, and height 0.15, working through cosine/sine values for each 22.5° increment.

I'm checking that the ball's trajectory clears the near wall's top edge with enough margin, then tracing where it lands on the floor and computing its velocity components at impact.

After landing with near-critical damping, the ball rolls toward the far wall at roughly 2-3 m/s horizontally, friction gradually slowing it. I'm checking whether the far wall (0.28 high) could stop it or whether residual kinetic energy and spin might let it climb or bounce over, but it seems unlikely given the low restitution and energy available.

Working through the spin direction confirms positive y-axis rotation corresponds to forward topspin, matching the ball's actual spin, but since the spin rate (5 rad/s) is far below the ~81 rad/s needed for pure rolling at that speed, the ball is mostly sliding with slight spin rather than rolling cleanly.

I should also check the contact dynamics on landing: with a 5 m/s vertical impact and stiff contact settings, penetration depth looks manageable relative to the bucket's wall thickness, though I want to make sure timestep resolution doesn't cause tunneling given how far the ball travels per step versus the material thickness.

I'm considering thickening the bucket bottom slightly so the ball's center stays safely above it during contact, while keeping the bucket's visible top surface and wall positions unchanged -- just adjusting the bottom geometry's span and center so it protrudes a bit below the walls without affecting the overall look.

Solving that quadratic gives x≈2.1068 for the floor intersection point. Then I'm sizing a stand cylinder (radius 0.2, z from 0 to 0.40) beneath the bucket — since both are static bodies there's no collision concern, so I can keep defaults. Now I'm moving on to defining the catapult frame geometry in the worldbody.

Still writing frame geometry...

I'm computing the stop bar's support posts geometry and confirming the ball's path clears it since it's purely visual. Then I check the forward arm stub's height at the rotated angle and start defining the actuator for the mechanism.

I'm setting up the actuator with filtered dynamics and affine bias for gradual motor response, then working out the keyframe ordering—arm hinge qpos first, followed by the ball's free joint qpos/qvel, with the actuator's internal state defaulting to zero in the keyframe.

Checking the physics at startup: the ball rests touching the catapult face and settles, while the velocity actuator starts with zero activation so gravity initially holds the arm against its lower limit. I'm computing the torque balance needed from the beam, wall, and ball masses before the arm can lift off that limit as the actuator state builds up.

The delay before liftoff is negligible, on the order of a tenth of a millisecond, so the velocity quickly tracks the activation minus the gravity-torque offset. I'm verifying the arm's angular velocity at release matches the target closely, accounting for the gravity lag term, and confirming the release timing against the activation filter's decay constant.

Checking geometry now: the ball sits flush against the wall's inner face, the arm's beam spans correctly along its length, and the wall box is positioned so the ball contacts it at the right height — everything lines up as intended.

Moving on to ball inertia, which defaults fine from its mass, and I'm defining the catapult hinge joint with a y-axis, 0-40 degree range, and small solreflimit damping. I'm weighing whether to add an implicitfast integrator alongside the 0.002 timestep option, and checking that the ball's solref value satisfies the timestep constraint — now thinking through how MuJoCo mixes contact solref parameters between geoms via solmix weighting.

Working through the mixed solref value, I estimate the arm contact penetration depth using the ball's peak acceleration and stiffness, getting roughly 1.75mm, which seems acceptable, but then calculating the landing penetration gives a much larger 2.2cm — checking whether this causes the ball to sink through the bottom geometry given its thickness and position.

To be safe I'll just set explicit solref values of "0.005 1" on the bucket bottom, walls, arm beam, and ball geoms to tighten up contact stiffness across the board, which brings penetration down to something more reasonable. I'll leave friction at default for the landing, set the floor as a simple plane the ball probably won't reach, add basic lighting and colors, and now I'm writing the bucket body definition with its position and named geoms.

Now I'm defining the sixteen bucket wall segments arranged in a circle using position and rotation, sizing the cylindrical bottom so it fits snugly inside the walls, and placing the stand cylinder to support the bucket at the right height. I double-check that the distance between the ball's starting position and the bucket is exactly 3, then move on to defining the catapult base geometry.

