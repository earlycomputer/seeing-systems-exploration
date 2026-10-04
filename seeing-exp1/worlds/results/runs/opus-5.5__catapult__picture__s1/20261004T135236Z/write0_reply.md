The catapult arm is driven by a speed-controlled motor that spins it at a steady 8.85 rad/s. A joint limit stops the arm at 40°, and the ball leaves the cup at about 5.4 m/s and 45° from z ≈ 0.83 m. That flight should reach the rim height of the bucket centred at x = 3 m.

I worked out the launch numbers by hand and have not run the file.

- The landing tolerance at the rim is roughly ±0.15 m, which is about ±2% of launch speed.
- The motor reaches its target speed after about 15° of the 40° swing, so the release speed is set by the motor rather than by the swing.
- The ball and bucket contacts are made stiffer so a fast ball cannot pass through the thin bucket walls.
- The cup surfaces have low friction so the ball doesn't drag on the cup wall as it lifts off.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="radian"/>
  <option timestep="0.002" integrator="implicitfast"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="1.5 0 0" size="5 3 0.1" rgba="0.75 0.8 0.75 1"/>

    <geom name="catapult_base" type="box" pos="0 0 0.02" size="0.3 0.15 0.02" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_upright_left" type="box" pos="0 0.09 0.23" size="0.04 0.015 0.19" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_upright_right" type="box" pos="0 -0.09 0.23" size="0.04 0.015 0.19" rgba="0.45 0.3 0.15 1"/>

    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 0.6981" limited="true" solreflimit="0.005 1"/>
      <geom name="catapult_axle" type="cylinder" fromto="0 -0.07 0 0 0.07 0" size="0.015" mass="0.02" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_beam" type="box" pos="-0.32 0 0" size="0.36 0.03 0.015" mass="0.3" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.655 0 0.04" size="0.01 0.06 0.025" mass="0.02" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.55 0 0.027" size="0.01 0.06 0.012" mass="0.02" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_cup_side_left" type="box" pos="-0.6 0.052 0.03" size="0.055 0.008 0.015" mass="0.02" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_cup_side_right" type="box" pos="-0.6 -0.052 0.03" size="0.055 0.008 0.015" mass="0.02" priority="1" friction="0.1 0.005 0.0001" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="ball" pos="-0.604 0 0.455">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.005 1" rgba="0.85 0.1 0.1 1"/>
    </body>

    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.02" size="0.26 0.02" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall0" type="box" pos="0.24 0 0.155" euler="0 0 0" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1697 0.1697 0.155" euler="0 0 0.7854" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.24 0.155" euler="0 0 1.5708" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.1697 0.1697 0.155" euler="0 0 2.3562" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.24 0 0.155" euler="0 0 3.1416" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1697 -0.1697 0.155" euler="0 0 3.9270" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.24 0.155" euler="0 0 4.7124" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall7" type="box" pos="0.1697 -0.1697 0.155" euler="0 0 5.4978" size="0.02 0.11 0.155" solref="0.005 1" rgba="0.2 0.35 0.7 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="40" forcelimited="true" forcerange="-20 20" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.604 0 0.455 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="8.89"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that reliably launches a ball into a bucket 3 meters away, thinking through the physics carefully. I'm considering a hinged arm driven by a motor or spring, with the ball resting in a cup at the arm's end that releases as the arm swings and hits a stop—leaning toward a velocity-controlled hinge for reliability.

I'm working out the geometry: pivot height, arm length rotating about the y-axis from a cocked-back position, with the ball's launch velocity determined by the tangential speed at the tip when the arm hits its rotational limit, solving for the angle and speed needed to land in the bucket at x=3m.

I need a radial wall at the tip to keep the ball from sliding outward along the arm under centripetal force, so the cup must have an outer lip holding it in place during the swing, releasing only once the arm decelerates near the stop.

I need to account for the ball's offset from the arm surface by its radius plus half the arm thickness when computing its actual position and velocity at launch. I'm now working out the geometry at φ=45°—placing the pivot, arm length, and offset to get the ball's exact center position—and assigning reasonable physical values like a 0.04m radius for the ball.

Positioning the bucket three meters from the pivot with a reasonable rim height and inner radius. Rather than hand-calculating the exact launch speed from motor torque and impact dynamics, it's simpler to drive the arm with a velocity actuator targeting a specific angular velocity, letting the ball release naturally once the arm hits its joint limit.

The release happens as the arm decelerates near the limit — the ball keeps its velocity while the arm slows, so the separation angle sets the release direction. I should tighten solreflimit to something like "0.005 1" for a sharper stop, respecting MuJoCo's constraint that timeconst stay at least twice the timestep. Alternatively, I could skip the hard stop entirely and let the ball separate naturally before any limit engages.

I'm also weighing whether to drive the arm with velocity instead of position control, since velocity makes it simpler to compute release speed directly from torque and inertia — I need to work out the ball's and arm's rotational inertia about the pivot to size the actuator properly.

Now I'm figuring out the geometry: placing the pivot point, sizing the arm as a box extending along one axis, and positioning the ball at a fixed radius above the arm's centerline so it sits snugly in a cup pocket at the starting angle, accounting for wall clearance so the ball stays contained until release.

I could add side walls too since they're cheap, though symmetry means no lateral forces push the ball sideways anyway. Checking the physics during the swing: centrifugal force pushes the ball outward against the outer wall while gravity's radial component stays small until higher angles, so the arm accelerates the ball tangentially without issue before release.

Now I'm working out the release geometry at φ=45°, computing the ball's position relative to the pivot by combining the radial offset with the perpendicular wall thickness, then figuring out the corresponding velocity vector from the angular velocity and position using the rotation-about-y-axis relationship.

Since 45° launch angle is relatively robust to small variations, I'll pick a limit angle of φ=50° and recompute the release position and velocity direction, checking that it lands close to the 45° target for range insensitivity.

I should set the joint angle units explicitly to radians to avoid ambiguity with MuJoCo's default degree compiler setting, using a range of roughly 0 to 0.698 radians (0 to 40°). I also need to confirm the arm starts resting at the lower limit under gravity before the motor engages, so the initial position is stable.

Computing the release geometry at φ=40°, the relative position from pivot works out to about (-0.424, 0.428), giving an absolute release point near x=-0.424, z=0.828, roughly a 45° trajectory. I should also account for overshoot past the joint limit — with angular velocity around 9 rad/s and a soft-limit timeconst of 0.005s, the arm could penetrate the limit by a few degrees before stopping, and the ball likely separates right as deceleration begins.

Now I'm working out where the bucket should be placed relative to the catapult — say the bucket center at x=3, with rim height around 0.3m and inner radius 0.2m — and aiming for the ball to cross the rim plane near x=3 while descending steeply enough to land inside rather than skip across.

If the descent angle is around 47°, the ball drops roughly 0.25m more in x after crossing the rim, so I need it to cross rim height closer to x≈2.95 so it doesn't clip the far wall before the ball radius is accounted for. Since contact damping is mostly inelastic by default, bounce-out risk should be low, but widening the bucket to inner radius 0.25 and height 0.35 would give more margin.

Let me settle on inner radius 0.22 and wall height 0.3, then work out the required launch speed to reach crossing point (2.95, 0.3) at 45° from the release position — solving the trajectory equation gives v≈5.35 m/s, so ω≈8.88 rad/s. I need to also account for the fact that release isn't instantaneous.

Checking whether the velocity actuator can spin up fast enough: with inertia ~0.09 and a torque cap around 20 Nm, the arm reaches 8.88 rad/s in about 0.04s, covering roughly 10° before settling into steady velocity. Gravity torque on the arm plus ball is about 1.5 Nm, which with a velocity-servo gain of 20 gives a steady-state speed error of around 1% — bumping gain to 50 would tighten that further.

Setting kv=50 with forcerange ±30 gets steady error down to about 0.3%, which looks acceptable, and the gravity load from the ball's weight is already folded into that torque estimate. I'm also checking whether the ball might slip off during the acceleration phase — at that torque the tangential acceleration at the ball is around 200 m/s², strongly pressing it into the arm wall, so it should stay seated; once the arm hits steady speed and acceleration drops, I need to verify the ball stays put under centripetal force and gravity's component in the rotating frame.

But then I realize that same 200 m/s² acceleration might cause excessive contact penetration between ball and arm given the soft contact solver settings — rough math suggests penetration could balloon to something like 8 cm, which would be way too much and signals I need to tighten the contact stiffness or solver parameters.

Plugging numbers in, that gives about 4mm penetration, which seems acceptable, though the spring-back when acceleration stops could give the ball a tiny outward velocity—likely negligible with critical damping though. To be safer I'm considering reducing forcerange so the acceleration is gentler: with forcerange 10, net α≈100, the arm would sweep 23° in 0.09s before leveling off to constant angular velocity for the remaining 17°.

Trying forcerange 15 instead gives α≈150, sweeping just 15° in 0.059s, which feels more reasonable. Now I'm working out the arm's inertia more precisely — modeling it as a beam geom with specific half-dimensions, I realize the default density gives it way too much mass (~1.3 kg), so I'll need to override the mass explicitly on the geom.

Setting arm mass to 0.3 kg, which gives a pivot inertia around 0.0437 using the parallel axis theorem. Now I'm checking the cup geometry attached to the arm's end, figuring out wall placement and height relative to the ball's center so it actually holds the ball without it spilling over the top.

I'm now positioning the ball itself: it needs to sit close to the inner wall face but with a tiny gap of about 1-5mm so it can slide freely before contact, recomputing the radial distance from the pivot accordingly.

Next I'm placing the inner retaining wall with small clearance from the ball's rest position, then working out the side walls as thin boxes offset along y to constrain the ball laterally.

I'm then estimating the arm's total rotational inertia by summing contributions from the arm beam, walls, and ball, assigning masses so the numbers come out reasonable. I'm also computing the gravity torque at zero angle by summing each component's weight times its lever arm.

With forcerange set to 20, I calculate the angular acceleration reaches about 164 rad/s², letting the arm hit 9 rad/s within roughly 0.055s over about 14° of rotation, with ball tangential acceleration giving a small, acceptable penetration depth. I'm setting up a velocity actuator on the catapult hinge with a kv gain of 50 and force limits of ±20, then considering how the keyframe control value should represent the target angular velocity.

I'm checking the velocity actuator's steady-state error: with 2 Nm of gravity torque and kv=50, the error is negligible (~0.4% of target speed), though I should nudge the target slightly higher to compensate. I also verify stability with explicit Euler integration—kv*dt/inertia comes out to 0.9, which is safely below the stability threshold of 2, though I still need to think through how ball contact forces interact with this.

Considering the full arm-plus-ball system, even with ball-only inertia the stability factor stays under 2, though it's oscillatory. I decide to switch to the implicitfast integrator for safety, since it handles actuator velocity derivatives better than plain Euler (which only implicitly damps dof damping, not actuator kv). I'll pair implicitfast with a slightly lower kv of 40, and now turn to figuring out exactly when the ball separates from the arm during release.

The arm hits its angular limit at φ=40°, decelerating while the ball keeps going — so I compute the release velocity as ω times the ball's radius vector at that instant, perpendicular to that vector. Plugging in r_radial=0.605 and offset=0.055, I work out the relative position components at φ=40°, getting a magnitude of about 0.6075 and a velocity direction angle near 44.8°. Now I need to pin down the absolute release position, which means deciding where exactly to place the pivot point.

Placing the catapult base at x=0 and the bucket center 3 m away at x=3, I get a release point around x=-0.428, z=0.831. I'm also considering whether the arm's deceleration as it nears the limit meaningfully delays release, since the ball separates from the arm surface once it starts decelerating relative to the ball's straight-line motion — I need to check how this affects the outer wall contact as the arm's rotation slows.

That 3mm radial shift means the ball would push slightly into the outer wall, causing friction, though the arm's continued rotation partly compensates. To avoid this, I should lower the wall top to around 0.065 relative height so the contact point sits right at the ball's center height, giving a clean horizontal contact normal instead of a problematic angled one.

Now I'm working out the launch trajectory at 44.8°, targeting the rim at z=0.3 and x≈2.95, computing the horizontal and vertical deltas and the tangent of the angle to solve for velocity.

I get v²≈28.61, so v≈5.35 m/s and angular speed ω≈8.8 rad/s; I check that centrifugal effects against the outer wall produce only ~1mm penetration, which is negligible, and move on to estimate steady-state error from gravity torque at the current angle.

For tolerance checking: with the small gravity torque correction, setting ctrl≈8.85 keeps error near 8.81, which seems workable. Given the bucket's inner radius minus ball radius leaves roughly ±0.18 tolerance, I translate that into a velocity tolerance of about ±0.1 m/s using the sensitivity of landing position to launch speed, which should keep the ball landing safely within the rim margins I calculated for the front and back walls.

Recomputing with target x=3.0, I get the deltas and solve for required speed: v²≈28.89, so v≈5.375 and ω≈8.848, which I'll round to a control value of 8.89. I should also check the arm's velocity servo dynamics—with kv=40 and inertia 0.11, the time constant is only 0.0028s, fast enough that saturation isn't a concern during the release window.

I'm also considering the joint limit behavior: once the arm hits the boundary, the soft constraint with solreflimit=0.02 kicks in, and at 8.9 rad/s the overshoot before the limit force fully engages could be roughly 5-10°. The release effectively happens right as this damping/stiffness response starts decelerating the arm at the boundary.

For crisper stopping I'll tighten solreflimit to "0.005 1" (keeping it at least double the timestep). I don't expect bounce-back since the system is critically damped.

Now for the bucket geometry, since there's no native hollow cylinder primitive, I'm constructing it from boxes arranged as an octagon ring for the walls plus a bottom disc, working out box half-thicknesses and lengths from the desired inner apothem of 0.22.

Computing wall placement...

I'm checking the octagon corner geometry to make sure the wall segments meet cleanly around the bucket, confirming the gaps are negligible relative to the ball's radius. Then I work out the ball's trajectory—apex height and timing—and start verifying the ball's initial resting position relative to the arm pivot.

Now I'm placing the catapult structure precisely: base, uprights, and axle pivot at (0,0,0.4), then computing the upright and arm wall widths so the ball sits flush against the arm surface without clipping.

I also need to check whether MuJoCo filters contacts between the arm body and the static base geoms - since the parent is worldbody, parent-child collision exclusion doesn't apply, so I have to make sure the arm beam's swept positions don't overlap the uprights or base at any rotation angle.

I'm considering making the axle itself a geom on the arm body, a cylinder passing through the pivot along y, but need to check its extent doesn't collide into the uprights' inner faces.

Checking the rest state at φ=0: gravity pulls the ball side down, which matches the lower limit, so the arm settles naturally at the joint stop without needing an extra constraint. I also note the opposite end of the arm swings downward as the arm rotates, so I should verify it doesn't clip into anything.

I'll skip adding a separate stop geometry for the catapult since the joint limits already handle that, and instead focus on the base and upright supports—sizing the base box, positioning the uprights symmetrically, and making sure the arm beam sits above them without intersecting.

Now I'm computing the ball's position relative to the pivot to confirm it rests properly on the arm cup, checking clearances against the inner and outer walls so there's a small gap of a few millimeters on each side. Writing cup wall geometry...

The ball should rise cleanly in the normal direction without hitting the shorter walls, since its center sits above their heights. Checking masses: beam at 0.3, walls at 0.02 each, axle 0.02, ball 0.1, with default friction and contact settings that should keep the ball settled once inside the bucket. One concern is whether the ball might tunnel through the thin 0.02m walls given its impact speed, so I should double check the timestep handles that collision properly.

Working through the solref math more carefully, I estimate the decay rate from the damping and stiffness coefficients, giving a time constant around 0.0105 s — which at v=5.4 m/s suggests penetration near 5.6 cm, enough to tunnel through a 2 cm wall. But I realize the impedance factor isn't constant and actually scales with penetration depth under the default solimp parameters, so the real number is likely smaller than this worst-case estimate.

Working through the math, max penetration comes out to roughly 3.8 cm with default timeconst, which is still too large. Tightening the ball's solref to something like "0.005 1" would cut that down to under a centimeter, so that's the fix — just need to keep timeconst above the minimum of 2*dt.

I should also stiffen the bucket walls and floor with matching solref since MuJoCo averages contact parameters between the two geoms via solmix, otherwise the softer wall value would dilute the ball's stiffness. I'll thicken the bucket walls to 0.02m half-width and the bottom cylinder to 0.02m half-height too, which should keep penetration from the ball's impact velocity (roughly 5 m/s on drop) within a reasonable 1cm tolerance.

Checking the trajectory near the rim, I want to confirm the ball crosses z=0.3 close to x=3.0 so it actually lands inside rather than clipping the edge.

Continuing the trajectory past z=0.31, the ball clears the near rim comfortably and descends steeply, landing near the bottom close to the far wall corner around x≈3.17-3.18, well within tolerance since the slope is steeper than 45 degrees.

Now I'm worrying about friction effects: as the ball presses outward against the wall under centrifugal force while the arm decelerates, there's tangential relative sliding between ball and wall surface, which introduces friction forces I hadn't accounted for yet.

Working out that the spring-back displacement is negligible, around 0.06 mm, so the residual penetration doesn't contribute much force. Now I'm tracking what happens once the arm stops: the ball continues along a straight tangent path while the wall keeps rotating briefly, so I need to work out the radial gap that opens up between the ball and the wall face as their positions diverge during that short window.

So the corner clearance condition only kicks in once the ball drifts enough radially, which given the tiny overshoot (~0.0157 rad penetration, arm stopping within 0.005s) means the arm's motion is essentially negligible compared to the ball's own trajectory. The ball then travels nearly straight at 5.4 m/s, taking about 0.0056s to rise 0.03m with only a 0.74mm radial drift, so corner contact seems unlikely to significantly alter the outcome.

Though I should check the soft constraint force at that small penetration - it works out to roughly 3N, giving a brief deceleration that only shaves off about 1% of speed, which is acceptable but adds some uncertainty to the model. It might be cleaner to just lower the outer wall's height so the ball clears it faster, or adjust the friction to reduce this edge case entirely.

Actually, since contact friction takes the max of the two geoms' values, I realize I could use the priority attribute instead - giving the catapult cup geoms higher priority with low friction would let those contacts use that lower value directly, without needing to touch the ball's friction setting at all. This seems like the cleanest fix since the ball-on-arm interaction relies mainly on normal forces anyway.

When torque saturates and ω hits target, the arm's angular acceleration drops abruptly, pressing the ball into the arm slightly, but penetration is tiny (~0.12mm) and damped out, so negligible. I'm also confirming the release trajectory clears the catapult frame uprights, rising well above their height as the ball passes over x=0.

With apex around 1.56m, I compute flight time of roughly 0.89s, landing about 1 second after launch into the bucket. I'm also verifying the arm reaches target angular speed before 40° by estimating total moment of inertia from the beam, walls, axle, and ball (~0.109 kg·m²), giving an angular acceleration of about 165 rad/s² under the net torque.

Checking that this acceleration gets the arm to 8.4 rad/s within 0.051s and about 12° of rotation, with a short exponential settling time after. I'm also confirming the tangential acceleration on the ball (~100 m/s²) and checking the steady-state error from gravity torque at φ=40°, finding the required controller speed of 8.89 rad/s yields an actual ω of about 8.852, close enough to the target 8.848.

I'm also verifying the ball's centripetal force doesn't contribute torque since it's radial, confirming the velocity actuator's steady-state is unaffected by implicit integration, and double-checking the hinge rotation direction — rotating about +y by a small positive angle correctly lifts the tip upward, consistent with a positive control signal producing positive joint velocity. Now I'm checking whether the joint range is auto-limited by default.

I need to make sure the keyframe's qpos vector accounts for both the hinge joint and the ball's 7-value freejoint, ordered according to body tree definition, with the arm starting near rest and the actuator control already engaged at t=0. I'm also working out solref blending between the ball and bucket/arm geoms, since differing contact softness values get averaged via solmix.

Given that penetration depths stay sub-millimeter even at high accelerations, the contact parameters look fine, so I'll leave the floor's solref at default since the ball likely never contacts it. Since the cup geoms have higher priority, their solref/solimp values fully override the mixed values in any contact, so I should explicitly set the cup's solref to match the ball's for consistency.

I'm also checking the outer wall's friction setup, confirming condim 3 with tangential friction 0.1 is adequate, and that joint armature/damping don't need extra tuning. Geom mass attributes handle inertia properly, so I'm now finalizing the floor plane size and position, adding a light source, and double-checking the bucket rim height before recomputing the release position for the throw.

Then I'm verifying the ball stays pinned against the arm by centripetal force until the arm decelerates sharply at the stop, at which point the ball separates cleanly since it's already near the top edge of the outer wall and lifts free as it rises further.

I'm confirming the geometry fits: the outer wall doesn't extend past the beam span, the uprights leave enough clearance for the hinge axle, and the ball's starting position is well clear of the uprights, so no unintended collisions at rest. Now I'm putting together the static catapult geometry — base, uprights, and axle — before finalizing the model.

Defining bucket geometry...

Computing the eight wall positions and rotations around the bucket rim at 45-degree increments, placing each wall segment at the correct radius with matching euler angles.

Finishing with the ball body setup, the catapult's velocity actuator with force and control limits, and defining the initial keyframe with starting position and zero velocities.

Now I'm adding the arm body with its hinge joint, axis, range, and solreflimit for proper contact solving, verifying the ball starts touching the arm at zero distance, and confirming default margin settings before finalizing the file.

