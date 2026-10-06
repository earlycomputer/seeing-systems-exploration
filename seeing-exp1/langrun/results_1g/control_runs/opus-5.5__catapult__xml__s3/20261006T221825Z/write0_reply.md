A velocity-servo catapult arm swings up to a joint stop and releases the ball. The ball should land in a wide, shallow bucket whose centre is 3 m downrange. I worked out the release speed and trajectory by hand; I did not run the simulation.

**Catapult**
- **Arm and drive:** The arm is hinged about y at (0.6, 0, 0.4). A velocity actuator (kv = 200, torque capped at 20 N·m) spins it at about 7.84 rad/s. A stiff joint limit at 0.70 rad stops it.
- **Ball start:** The ball starts at rest at (0, 0, 0.46). It sits on the arm, held against an outer lip by centrifugal force while the arm turns.
- **Launch:** When the arm stops, the ball leaves at about 4.73 m/s at about 44° above horizontal.
- **Release point:** The release point is (0.18, 0.83). The catapult surfaces in contact with the ball use low friction, so the ball is not dragged as it separates.

**Expected flight**
- The ball centre should pass the rim height at about x ≈ 2.93 m and reach the bucket floor at about x ≈ 3.08 m.
- That leaves roughly ±0.18 m of margin, which is about ±3 % in launch speed.

**Bucket**
- It is a static tub with a 0.3 m inner radius, built from 12 wall boxes and a floor disc, centred at (3, 0).
- Its geoms use rolling and torsional friction (condim 6), so the ball should stop rolling. My estimate is that it is still within about 1.5 s of landing, well before 6 s.

```xml
<mujoco model="catapult_to_bucket">
  <compiler angle="radian"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="1.5 -2 5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="1.5 0 0" size="5 5 0.1" rgba="0.8 0.85 0.8 1"/>

    <!-- catapult frame (static) -->
    <geom name="catapult_base" type="box" pos="0.6 0 0.15" size="0.2 0.2 0.15" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_l" type="box" pos="0.6 0.09 0.355" size="0.025 0.02 0.055" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_r" type="box" pos="0.6 -0.09 0.355" size="0.025 0.02 0.055" rgba="0.45 0.3 0.15 1"/>

    <!-- catapult arm: points along -x at angle 0, rotates up about +y -->
    <body name="catapult_arm" pos="0.6 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="-0.2 0.70" solreflimit="0.005 1"/>
      <geom name="catapult_hub" type="cylinder" fromto="0 -0.06 0 0 0.06 0" size="0.03" mass="0.2" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_beam" type="box" pos="-0.3 0 0" size="0.35 0.03 0.02" mass="1.0" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_lip_outer" type="box" pos="-0.656 0 0.04" size="0.015 0.04 0.02" mass="0.05" priority="1" friction="0.05 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_lip_inner" type="box" pos="-0.545 0 0.0275" size="0.01 0.04 0.0075" mass="0.03" priority="1" friction="0.05 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
    </body>

    <!-- ball, resting in the cup -->
    <body name="ball" pos="0 0 0.46">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.15 0.1 1"/>
    </body>

    <!-- bucket (static), centre 3 m downrange of the ball start -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_floor" type="cylinder" pos="0 0 0.01" size="0.33 0.01" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0.13" euler="0 0 0" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.26847 0.155 0.13" euler="0 0 0.523599" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.155 0.26847 0.13" euler="0 0 1.047198" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.31 0.13" euler="0 0 1.570796" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.155 0.26847 0.13" euler="0 0 2.094395" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.26847 0.155 0.13" euler="0 0 2.617994" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.31 0 0.13" euler="0 0 3.141593" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.26847 -0.155 0.13" euler="0 0 3.665191" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.155 -0.26847 0.13" euler="0 0 4.188790" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.31 0.13" euler="0 0 4.712389" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.155 -0.26847 0.13" euler="0 0 5.235988" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.26847 -0.155 0.13" euler="0 0 5.759587" size="0.01 0.085 0.11" priority="1" condim="6" friction="1 0.02 0.01" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="200" ctrllimited="true" ctrlrange="0 10" forcelimited="true" forcerange="-20 20"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.46 1 0 0 0" qvel="0  0 0 0 0 0 0" ctrl="7.86"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the physics of a catapult design that needs to throw a ball 3 meters into a bucket—considering a hinged arm with a cup for the ball, driven by either a motor or a spring-loaded mechanism with a joint range limit to control the launch angle and stop point.

I need to work out the release velocity mathematically: the arm rotates until it hits a stop, and the ball leaves the cup with tangential velocity equal to angular velocity times the cup's radius from the hinge, directed perpendicular to the arm at that stop angle. The tricky part is designing the cup geometry so it doesn't obstruct the ball's release trajectory once the arm decelerates at the limit.

A simpler plunger-based launch has the same release-angle issue. The bigger concern is precision: since range scales with velocity squared, even a small velocity error produces a large landing error, so I should make the bucket generously sized—maybe 0.3 m inner radius—to give margin for error, and ensure the ball settles without bouncing by tuning contact damping.

For predictability, I think a velocity-controlled actuator is the better approach: drive the arm with a high-gain velocity servo toward a target angular speed, let it accelerate while the ball sits in the cup, then have it hit a joint limit and hold there so the ball releases at a known speed equal to ω times the arm radius.

Forcerange caps torque so acceleration stays moderate rather than instantaneous, with solref damping preventing oscillation in the contact. I'm checking the centripetal requirement: at R=0.8m and ω≈6.75 rad/s, the needed inward acceleration is about 36 m/s², which the lip can supply, and making the arm heavy relative to the ball should keep the ball's reaction from perturbing the arm's motion much.

Now I'm working out the throw geometry for a 45° launch toward +x: the arm starts lying back toward -x and sweeps upward, stopping when it's tilted 45° from vertical so the tip velocity (perpendicular to the arm) points at 45° above +x. I'm parameterizing the tip position as it rises through angle α from the -x axis to get the velocity direction right at release.

With only a 45° swing to work with, I compute the angular acceleration needed if the motor ramps up over the first half of that arc, getting roughly 57 rad/s², which seems feasible. Now I need to think about how the ball actually rests on the arm's surface during the swing, starting from the arm's initial horizontal position.

As the arm rotates up to 45°, the ball's supporting surface faces the direction of motion, so it needs lips on both sides to counteract gravity pulling the ball inward early in the swing before centrifugal force takes over. I'm also working out the rotation direction about the y-axis using the right-hand rule to confirm the arm sweeps correctly toward the launch direction.

Now I'm setting up the hinge joint: axis along y, angle α starting at zero, with a range like -0.1 to 0.7854 radians. I'm considering a slight negative starting offset since gravity would initially pull the arm down before the velocity actuator ramps up.

For the release calculation, I need the ball's center position offset from the arm's pivot by both the arm radius and a small perpendicular offset for thickness plus ball radius, then compute the release velocity as ω cross r — accounting for the fact that r isn't perfectly perpendicular to the arm due to that offset. The ball separates from the arm as it decelerates near the upper limit, continuing on its own trajectory afterward.

Working through the rotation, I compute that the offset d shifts the exit angle slightly below 45° by roughly atan(d/R), so the release direction is approximately 45° minus that small correction for small d/R.

Now I'm picking concrete values: pivot height 0.4 m, arm radius 0.6 m, ball radius 0.04 m, arm thickness giving d=0.06 m, which gives β=atan(0.1)≈5.71°, and setting up the stop angle accordingly.

I'll set the stop angle at about 0.70 rad (~40.1°), giving a launch angle near 44.2°, close enough to the ideal 45° for max range. Then I'm computing the ball's release position using the pivot geometry, working out the trig for x and z coordinates at that stop angle.

Setting pivot_x = 0.6 so the ball starts at x=0, which puts the bucket center at x=3.0 since it needs to be 3 m away horizontally. That gives a release position around x=0.18, z=0.83, and now I need to figure out where the ball lands relative to the bucket rim height.

I'm aiming for the ball to reach roughly z=0.3 (bucket rim plus a bit) at x≈3.0, meaning a horizontal distance of 2.82 m and a drop of about 0.532 m from release. Using the trajectory equation with launch angle 44.2°, I'm solving for the required velocity by plugging in x tanθ ≈ 2.74 and setting up the gravity term to match the needed drop.

Working through the numbers, I get v² ≈ 23.18, so v ≈ 4.815 m/s and ω ≈ 7.985 rad/s. But I realize this only lands the ball at bucket-center-rim level while it's still descending steeply, so it'll actually land further forward than intended — I need to re-aim so the ball's descending path crosses the rim plane right where the bucket opening is centered.

Now I'm sizing the bucket itself (inner radius ~0.25m, bottom near z≈0.06 accounting for ball radius) and tracing the ball's steep ~50° descent from rim to bottom to figure out where to aim the rim-crossing point so it lands centered within the bucket's inner radius tolerance.

Plugging in x=2.82, I solve for the needed velocity (~4.73 m/s, ω≈7.84 rad/s) to hit the target drop. Checking sensitivity, I find range scales roughly 2x with velocity error, so a 1% velocity error shifts landing by ~0.06m — within the ±0.15m tolerance if ω is held precisely through release, though I need to account for any speed change during the arm's deceleration near the joint limit stop.

Thinking through contact physics at release: the ball separates once the plate decelerates since the ball keeps its velocity, and the centripetal force at the end lip is small given the mass and radius, so compression energy stored there is negligible and shouldn't meaningfully kick the ball outward. I'm also considering whether friction between the ball and lip during separation could matter, but since the lip surface runs parallel to the ball's motion direction, this effect should be minor too.

During the acceleration phase, I'm checking that the ball stays seated on the plate: at constant ω, the ball's normal acceleration is zero since tangential acceleration vanishes in circular motion, so the required normal force just equals gravity's component along the normal, which the plate can supply. Since the velocity servo is first-order with no overshoot, there's no risk of excess acceleration launching the ball prematurely during spin-up.

Adding gravity torque gives roughly 3.6 Nm, so with a velocity servo of torque = kv(ω_target−ω), low kv leaves a steady-state error from gravity loading — I need kv around 200 to keep error under 1%, but that makes the implied time constant faster than the simulation timestep, raising questions about whether MuJoCo's Euler integrator handles that stiffness correctly without an implicit solver.

I should switch to the implicitfast integrator since kv*dt/I ≈1.6 is marginal for explicit Euler, and also cap actuator torque with forcerange so acceleration stays bounded — with a 40 Nm limit, the arm reaches target velocity in about 0.05s after traveling roughly 0.21 rad, after which the servo holds steady state with gravity-dependent error scaling as cos(α).

At the moment torque is applied the ball sees roughly 9g of acceleration through the plate, and I'm now thinking through how MuJoCo's soft contact model (with its default timeconst and solref parameters) would handle that penetration depth, since the effective stiffness and damping depend on the contact impedance settings.

3cm penetration is too much for a 4cm ball-arm overlap, so I should stiffen the contact with a shorter solref timeconstant like 0.005 (still above the 2*dt minimum), which cuts penetration down to about 2mm. I also want to scale back the torque range so the net angular acceleration stays reasonable rather than causing excessive force.

Now I'm working through the actual arm geometry and mass properties to get a real moment of inertia instead of estimating. I'm placing the catapult arm body at its pivot, setting up the hinge joint axis, and defining the beam geometry as a box extending out from the pivot point.

I'm also sketching out the cup walls that hold the ball — using the beam's top surface as the base and adding outer lip boxes positioned so their inner face just touches the ball's radius, figuring out the right height and position for containment.

Thinking about release velocity at the pivot: computing the local-frame cross product shows the ball moves slightly inward (+x) and upward as it rotates, which means it naturally clears the outer lip without friction issues. Now I need to check the inner lip — since the ball's trajectory has a specific rise-to-inward ratio, I need the inner lip's height low enough that the ball clears it during release.

Checking the clearance math, placing the lip's inner face at a safe offset so the ball's chord stays clear as it rises—the gap only grows, so this works fine. Then I reconsider whether the inner lip is even necessary, since gravity only pulls the ball inward when centrifugal force is weaker than gravity, which is mainly during the early low-speed phase before acceleration ramps up.

I decide the tangential acceleration acts normal to the plate so it doesn't induce rolling torque, and skip y-direction side walls since the setup is planar and symmetric, with drift being negligible. I settle on positioning the ball at x=-0.6 so it starts touching the outer lip exactly, resting there until centrifugal force takes over.

I then work out the outer lip box geometry so its contact face aligns with the ball's center height, giving a purely horizontal, centripetal-aligned normal force. But I realize that once the arm stops at release, the ball's velocity carries it inward relative to the arm rather than outward, meaning it moves away from the outer lip and toward the inner one instead.

Now I'm defining the inner lip geometry alongside the counterweight hub cylinder mounted along the pivot axis, then sketching out the static base box dimensions and figuring out where the arm's pivot height sits relative to the base's top surface.

I'm checking the geometry to make sure the rotating arm clears the base when it swings down — verifying bottom edge positions at different rotation angles against the base's top and side extents so nothing intersects the static frame.

I'll size the posts at y 0.07–0.11, z 0.29–0.41, keeping a 1cm gap from the hub ends at y=0.06 so nothing collides. I'll skip adding a visual stop bar since the joint limit already handles the stopping, and just confirm the ball rests clear of the base.

Now I'm working out arm mass and inertia: setting ball mass to 0.1, then computing the beam's rotational inertia about the pivot by combining its center-of-mass inertia with the parallel axis term from its offset, and assigning explicit masses to the outer and inner lips (0.05 and 0.03) to get their contributions at their respective distances from the pivot.

Summing the hub, ball, and lip contributions gives a total inertia around 0.198, and now I'm computing the gravitational torque about the pivot by adding up each component's mass times its distance from the axis.

Working out the velocity actuator dynamics: with kv=200 and forcerange ±20, the net torque of ~16 gives an angular acceleration near 81 rad/s², reaching the target velocity in about 0.1s. Then I'm checking the steady-state error caused by gravity torque at the resting angle, which pulls the actual angular velocity slightly below the commanded value by roughly 0.015 rad/s.

I'll bump ctrl to about 7.86 to compensate, and verify the resulting force stays under the 20 Nm limit — it's fine at about 3 Nm. For the joint limit stop, I'm considering stiffer solreflimit values like "0.005 1" to minimize penetration depth, estimating it comes out to roughly 0.002 rad given the torque and stiffness, which seems acceptable, and I'm working through how the arm decelerates once it hits the limit.

With a time constant around 0.005s, the arm stops within about 0.01s, giving an overshoot of roughly 0.04 rad — so the effective release angle shifts to around 0.70–0.74 rad, lowering the launch angle by maybe 0.5–2°. The ball releases right as deceleration begins near α≈0.70, since contact force vanishes once the arm stops pushing it forward, and penetration energy there is negligible. Now I'm considering whether friction against the outer lip at the moment of release matters too.

As the arm decelerates, the centripetal force on the ball stays near 3.7N, but the lip also decelerates with the arm while the ball tends to keep moving — friction between them would act to slow the ball's normal motion as long as contact persists, so I'm working out whether contact actually breaks immediately or whether compression against the lip delays separation slightly.

I estimate the ball separates from the lip within roughly 0.8mm of relative displacement, which takes only a couple milliseconds as the arm slows. During that brief contact window, friction could still apply up to ~37 m/s² deceleration on the ball, costing maybe 1.5% of its exit velocity — enough to noticeably shorten the throw. To avoid this I'm considering lowering the friction coefficient on the outer lip geometry, though I need to remember that MuJoCo combines contact friction by taking the max of the two geoms' values, so I'll need to adjust the ball's friction too if I want this fix to actually take effect.

Lowering ball friction raises a new concern though: since rolling friction is zero by default, a ball rolling on a flat bucket bottom would never naturally come to rest—it'd just keep rolling until it collides with a wall. That's risky given the requirement that the ball settle below 5 cm/s by 6 seconds. I'm weighing options like using condim 6 with explicit rolling friction on the bucket floor.

That gives a deceleration of about 1.75 m/s², so the ball stops quickly—good. With ball friction default 1 and bucket 0.8, the max coefficient used is 1, which is fine.

I'm also considering the beam's friction during the brief separation phase—since the lip is what actually restrains the ball centrifugally, the beam itself doesn't need high friction, so I could give the whole beam surface a low friction value like 0.1 since the lip does the holding.

During the early acceleration phase I should check the inertial forces more carefully: at small α and growing ω, centrifugal force (ω²R) quickly dominates gravity's component along the arm (g sinα), so the ball stays pinned against the outer lip from the start rather than sliding inward. Now I want to recompute the expected trajectory precisely using the actual angular velocity value, ω=7.84.

I'm working out the release radius (r=0.6030, giving v=4.728) and confirming the ball's resting position against the beam, accounting for the small contact penetration. Then I'm figuring out the release angle, accounting for where the joint limit constraint softly engages and decelerates the arm—this gives a launch angle around 44.18°, which I'll use to get the velocity components.

Now I'm computing the velocity components (vx≈3.39, vz≈3.29) and the release position (x0≈0.180, z0≈0.832) from the arm geometry, then double-checking an earlier velocity calculation to make sure it's consistent.

Tracing the trajectory forward, I check the rotation convention against MuJoCo's y-axis rotation matrix applied to the local arm point, confirming the tip rises as expected. Then I find the time to reach x=3.0 (about 0.832 s) and compute the ball's height there, arriving at z≈0.179.

Now I'm estimating where the bucket sits—floor around z=0 to 0.02, walls up to 0.30—and solving for when the ball descends to the bucket's bottom depth (z=0.06), setting up the quadratic in t to find that landing time.

Solving that gives t≈0.856s, landing at x≈3.08, about 8cm past center—looks good. I also check where the ball crosses the rim height (z=0.34, accounting for ball radius) at t≈0.798s, x≈2.884, comparing that against the near wall's inner edge position (around x=2.78 for an inner radius of 0.22) to confirm the ball clears the rim without striking the wall.

But that margin is only about 6cm, roughly 1% velocity tolerance—too tight for reliability. So I'm reconsidering the bucket geometry: making it shallower and wider, with inner radius 0.3 and wall height 0.2, then recomputing the rim-crossing time and position for this new configuration.

I'm worried about bounce dynamics too — with near-critical damping the ball shouldn't rebound much off the bottom, but the horizontal slide speed of ~3 m/s when it hits the far wall could cause it to climb up the wall if there's topspin from rolling friction, which I need to check doesn't launch it back out.

Friction brings the ball to rolling at reduced speed with spin energy around 0.117 J, then it contacts the far wall with rolling friction decelerating it slightly; I'm working out how the topspin's contact-point velocity at the wall interacts with the wall friction, since the spin direction determines whether friction pushes the ball up or down on impact.

I'm estimating that the friction impulse during the wall collision could give the ball a vertical velocity boost proportional to its spin, roughly around 0.69 m/s, causing it to climb a few centimeters — small enough to be safe for the simulation.

Checking the wall height against the trajectory, if the rim is around 0.25-0.29m tall, the ball passes with a comfortable margin, so I'll settle on roughly 0.22m for the wall height. I need to make sure rolling friction on the bucket floor eventually brings the ball to rest, using condim 6 contacts and combining the ball's and bucket's friction coefficients to get a rolling friction around 0.01, which should let the ball settle naturally against the wall or floor.

For the catapult beam, I'll use geom priority to make its friction values take precedence, confirming that's a valid MuJoCo attribute. For the bucket itself, I'm approximating the cylindrical wall using a ring of boxes — something like 12 segments — with a floor plate around 0.33m radius and walls rising from just above the floor to about 0.24m high.

Now I'm checking the ball's trajectory clearance against the rim and walls: recalculating where the ball crosses the near wall height gives a landing point with roughly 0.18-0.19m margin from the inner wall faces on both sides, and checking the floor-level landing distance similarly clears the far wall with margin. With that confirmed, I'm now working out the exact box dimensions for each of the 12 wall segments given the inner apothem of 0.30m and wall thickness.

Computing segment positions...

I'll make the bucket a static body at (3,0,0), consistent with the target being 3 m horizontally from the ball's start. For the ball, I'm placing it at x=0, z=0.46 as its starting position.

Now I need to set the keyframe qpos matching body tree order (arm hinge, then ball freejoint), giving arm angle 0 and ball position 0 0 0.46 with identity quaternion, plus a ctrl value of 7.86. I'm also double-checking the ball doesn't initially penetrate the beam or its outer lip, since the ball sits right at the beam's top surface with negligible overlap, and verifying its x-range doesn't overlap the lip's world-space bounds.

I'm confirming there's an adequate gap between the ball and the inner lip at launch (roughly 1.4 cm clearance after accounting for the chord width at that height), and checking the timing: the ball releases around 0.13 s, stays airborne for about 0.86 s, lands near 1 s, leaving plenty of margin within a 5 s simulation to settle. After the arm hits its limit, I'm noting the actuator continues pushing to hold it there.

Now I'm tracing the ball's trajectory to make sure it clears the arm and base structure—checking that the arm swings back after a small overshoot without intersecting the ball's path, and verifying at x=0.6 the ball's height (about 1.165) clears the base and posts (tops at 0.3 and 0.41 respectively).

I also want to confirm the arm's velocity servo reaches target angular velocity before 0.70s: with torque-limited acceleration around 83 rad/s², it hits the target ω of 7.86 rad/s in roughly 0.095s at 0.37 rad, after which servo tracking takes over, accounting for gravity torque on the beam at the release angle.

Summing moment contributions — beam, ball, outer lip, inner lip — gives a total gravity torque of about 3.01 Nm, producing a steady-state error of 0.015 rad/s against the velocity gain, bringing ω down to about 7.845, close enough to the 7.84 value I'm using.

I'm also considering whether the implicit integrator's derivative handling changes when actuator force saturates at its limits — I recall MuJoCo may zero out that derivative term when clamped, but either way the simulation should remain stable.

I'll configure the velocity actuator for the catapult motor with its force limits and control range, and set the integrator to implicitfast. For contact stiffness, I need to account for how MuJoCo mixes solref parameters between the ball and beam geoms (averaging by default), so I may need to set solref on both or use priority to control which geom's parameters dominate.

I'm giving the beam and lips priority 1 with solref="0.005 1" so their contact parameters take precedence, and giving the bucket geoms priority 1 too with appropriate friction and condim settings, leaving the ball and floor at defaults. Then I'm checking whether penetration might occur during the acceleration phase given the arm's high angular acceleration, working through the impedance and stiffness math from the default solimp values.

Working through the steady-state penetration estimate, I get roughly 1.1mm which seems acceptable for this soft contact model. I'm also setting solreflimit="0.005 1" on the joint limits and explicitly marking the hinge as limited="true" rather than relying on auto-detection, then starting to estimate the ball's separation distance based on the arm's deceleration timescale.

With critical damping the ball leaves the plate cleanly right away, and since gravity alone presses it onto the plate, separation should be clean. The lip friction coefficient of 0.05 and beam friction of 0.1 both seem low enough that friction losses stay negligible — around 0.1% — and I confirm the ball doesn't need matched angular velocity since it's just sliding, not rolling-coupled. At rest with zero acceleration, nothing pushes the ball along the low-friction beam either, which is correct. For the floor, I'm placing an infinite collision plane sized "6 3 0.1" centered around (1.5, 0, 0) so it spans the relevant area properly.

I'm defining the bucket floor as a static cylinder plate, and since it's static against a static base there's no unnecessary collision computation happening between them. I consider adding a visual crossbar between the posts but decide to skip it, then move on to lighting and the ball's color. I also verify the ball won't collide with the arm hub at the start.

Working through the landing dynamics: the ball should hit the bottom near 3.08 with roughly 2.4 m/s, decelerating under rolling friction at about 1.75 m/s², giving it around 1.6 m of travel before it would naturally stop — but since that's farther than available space, it reaches the far wall first with margin to spare, then rebounds inelastically and continues rolling back and forth as it loses energy.

I'm estimating rolling friction limits the ball to about 1.4 seconds of free rolling, with wall contacts dissipating further energy so it should settle by around 6 seconds, while torsional friction handles killing off any residual vertical spin. I double check that the rolling friction coefficient combined with condim 6 won't cause odd spin artifacts — this is standard setup. Then I work through the physics: the rolling friction torque opposes angular velocity, giving a linear deceleration of about μ_r·g/(1.4r), which comes out to roughly 0.01 times 9.81 divided by that factor.

I verify the outer lip friction and gravity setup against the ball are consistent, make sure default qvel is zeroed for the ball's keyframe, and confirm all the geom and body names are set correctly — ball, catapult_arm, catapult_base, posts, hub, beam, and inner/outer lips. I check the hub cylinder placement along the pivot axis and the post positions, noting hub inertia isn't a concern. Now I'm working out the arm body's inertia based on its geoms.

With no armature on the joint and a stiff velocity servo, I think through whether the instant torque jump at t=0 causes contact transients with the ball — since the plate accelerates instantly, the ball may momentarily lag then catch up, but critical damping should prevent overshoot or separation. I also check what happens when torque drops sharply later in the motion, verifying the compression release doesn't cause the ball to pop off the plate given the damping characteristics.

During the constant angular velocity phase, I confirm the ball only needs gravity's normal component to stay pressed against the plate, which checks out fine. I'm also considering whether sliding during the transition might shift the ball's position, but the lip constraint should handle that, and I'm working through the servo's torque-clamping behavior as velocity error shrinks below threshold.

Checking the release point more carefully: when the joint hits its limit at q=0.70, the arm decelerates sharply, but the ball's velocity at that moment (computed from ω·r) is nearly identical whether I use the exact release angular velocity or a close approximation, so the difference is negligible. I verify the launch direction by transforming the plate's local z-axis into world coordinates and confirming it roughly matches the ball's velocity vector, accounting for the slight forward tilt from offset d — this all lines up with the plate facing forward-up as expected. Now I'm putting together the XML with degree-based angles for the bucket walls and joint definitions.

Settling on bucket radius 0.33. Now I'm checking the base and post geometry: base top at z=0.3, posts spanning roughly z 0.30–0.41, hub at z 0.4 with radius 0.03 spanning 0.37–0.43, and verifying the beam clears the posts laterally since the beam's half-width is smaller than the post offset. I'm also checking whether the arm beam could strike the base top at any swing angle given its length behind the pivot.

At the extreme swing angle checked, the lowest beam point still clears the base top by a safe margin, and the front swing angle never gets reached so no conflict there. The ball's starting position is clear of the base footprint, and the lip width versus ball radius leaves enough clearance too, so I'm skipping any extra visual stop and considering the geometry finalized.

