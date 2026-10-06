The arm starts flat and pointing backwards, with the ball in a cup at its tip. A velocity servo swings the arm at about 7.84 rad/s until it hits a hard stop at 45°. At that point the ball leaves at roughly 4.7 m/s, about 40° above horizontal. The ball starts at x = −0.6 and the bucket's centre is at x = 2.4, so the bucket is 3 m away horizontally. The bucket's opening is 0.6 m wide.

These numbers come from a hand calculation; I have not run the file. The landing point depends on the launch speed, and the bucket's half-width leaves about ±4–5% of margin on that speed. The main uncertainty is the release: it assumes the arm stops close to 45° and the ball leaves cleanly. If the ball lands short or long, adjust the `ctrl` value in the keyframe.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="0 0.4 -1"/>
    <geom name="floor" type="plane" size="6 3 0.1" pos="0 0 0"/>
    <body name="catapult_base" pos="0 0 0">
      <geom name="catapult_baseplate" type="box" size="0.25 0.18 0.01" pos="0 0 0.01"/>
      <geom name="catapult_post_left" type="box" size="0.02 0.02 0.19" pos="0 0.12 0.21"/>
      <geom name="catapult_post_right" type="box" size="0.02 0.02 0.19" pos="0 -0.12 0.21"/>
      <geom name="catapult_axle" type="cylinder" size="0.012 0.12" pos="0 0 0.4" euler="90 0 0"/>
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" limited="true" solreflimit="0.005 1" damping="0"/>
        <geom name="catapult_beam" type="box" size="0.38 0.05 0.01" pos="-0.28 0 0" mass="0.2"/>
        <geom name="catapult_cup_outer" type="box" size="0.01 0.055 0.03" pos="-0.651 0 0.04" mass="0.03"/>
        <geom name="catapult_cup_inner" type="box" size="0.01 0.055 0.015" pos="-0.55 0 0.025" mass="0.02"/>
        <geom name="catapult_cup_side_left" type="box" size="0.04 0.005 0.02" pos="-0.6 0.05 0.03" mass="0.015"/>
        <geom name="catapult_cup_side_right" type="box" size="0.04 0.005 0.02" pos="-0.6 -0.05 0.03" mass="0.015"/>
      </body>
    </body>
    <body name="ball" pos="-0.6 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.005 0.001"/>
    </body>
    <body name="bucket" pos="2.4 0 0">
      <geom name="bucket_floor" type="box" size="0.32 0.32 0.01" pos="0 0 0.01"/>
      <geom name="bucket_wall_far" type="box" size="0.01 0.32 0.125" pos="0.31 0 0.135"/>
      <geom name="bucket_wall_near" type="box" size="0.01 0.32 0.125" pos="-0.31 0 0.135"/>
      <geom name="bucket_wall_left" type="box" size="0.3 0.01 0.125" pos="0 0.31 0.135"/>
      <geom name="bucket_wall_right" type="box" size="0.3 0.01 0.125" pos="0 -0.31 0.135"/>
    </body>
  </worldbody>
  <actuator>
    <velocity name="catapult_drive" joint="catapult_hinge" kv="30" forcelimited="true" forcerange="-15 15"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 -0.6 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="7.84"/>
  </keyframe>
</mujoco>
```

```expect
catapult_arm reaches its upper stop
ball touches bucket_floor
ball comes to rest in bucket
```

---
thinking (summarized):

I'm thinking through a catapult design that needs to launch a ball 3 meters into a bucket — a hinged arm driven by a motor or spring with a stop to release the ball, though tuning the exact mechanics without simulation is tricky, so I'm considering giving the arm an initial angular velocity while the ball starts at rest in its cup.

I'm leaning toward a spring-loaded joint with stiffness and springref, cocked and released, swinging to a limited range where the ball launches. Estimating the tip velocity and release angle analytically is messy, so I'm simplifying by assuming the arm stops around 45° past horizontal, giving the ball a forward-up release direction, while also considering a torque-driven motor approach where speed at the limit depends on torque, arm mass, and gravity, with the cup walls holding the ball until release.

Actually a velocity actuator seems cleaner: drive the arm to a target angular velocity quickly, let it hit the joint limit, and set release speed as ω times the arm radius, accounting for the ball's added inertia and center-of-mass radius. Now I'm working out the geometry -- pivot height, horizontal starting position of the ball, bucket position three meters away, and the arm's rotation from pointing backward-horizontal up to vertical, figuring the stop angle needed for the arm direction at release.

I'm factoring in the cup offset so the ball sits slightly above the arm's centerline, which shifts the velocity direction a bit flatter at release. Now I'm plugging in concrete numbers (R=0.6, d=0.05, h_p=0.4) to compute the actual release position and angle at θ=45°.

Working out the trajectory math: computing release velocity components, then setting up the equation to hit the bucket rim at x=2.4, z=0.3, solving for the angular velocity needed given the horizontal distance and gravity drop.

I get ω ≈ 7.865 rad/s giving velocity components of roughly vx=3.61, vz=3.06, total speed about 4.73 m/s. But then I realize release mechanics aren't actually instantaneous — the arm hitting its joint limit might cause a soft stop or bounce, and there's also a centripetal force issue: the cup needs to hold the ball against outward sliding along the arm before release, since the required centripetal acceleration is quite large relative to gravity.

So I'm thinking the cup needs an outer wall at the tip to contain the ball during spin-up, while the ball's actual release velocity (mostly perpendicular to the arm) shouldn't get blocked by that wall since it's moving roughly parallel to it. Tangential acceleration during the throw just presses the ball into the arm surface, which is fine — but maybe instead of relying on a bouncy joint limit, I should use a velocity servo to decelerate the arm smoothly for a cleaner release.

A velocity actuator alone would just hold constant ω forever, so I still need a joint limit as a hard stop; since the servo keeps pushing into the limit there's no bounce-back. The default limit stiffness means the arm decelerates over roughly the timeconst window, overshooting a few degrees before the ball separates — I'm considering tightening the solref to something stiffer like "0.005 1" for a sharper stop, keeping in mind the timestep constrains how small timeconst can go.

Now I'm working through the actuator gain: estimating total rotational inertia from the arm and ball mass, then checking what kv gives a reasonable response time relative to the timestep. A high kv like 50 would be too stiff for explicit Euler integration, so I'm leaning toward using "implicitfast" integration to handle the actuator damping properly, with something like kv=20 giving a more sensible time constant.

Bumping kv to 10 cuts the error to about 2%, which seems acceptable. Rather than fight gravity torque varying with angle, I'll just keep the arm light (0.2 kg) and set the ball mass explicitly to 0.1 kg rather than relying on default density. I should also double check whether the bucket's 0.25 m radius at 2.8 m distance gives enough tolerance given that range scales roughly with velocity squared.

Thinking through this more, a ±9% range tolerance means I only need ±4.5% speed accuracy, which is comfortable, so I'll make the bucket a bit generous anyway (0.3 m inner radius). I considered forcing a deterministic swing via keyframe velocities, but since the ball starts at rest that doesn't apply. Working out the gravity torque during the swing from horizontal to 45°, accounting for both the arm's and ball's weight contributions at the pivot radius.

Continuing the torque calculation, I translate the steady-state error into roughly 0.083 rad/s of adjustment needed, so I bump the control value up to about 7.95. Then I check whether the servo settles before release using the torque time-constant, and compute the arm's moment of inertia about the pivot (~0.0245 kg·m²) treating it as a rod offset from the pivot.

I add the ball and cup masses (~0.07 kg total), giving a settling time of roughly 7ms, well within the 35ms window before release, so the lag should be negligible. Then I shift to checking the release geometry itself — whether the ball exits the cup cleanly at the 45° stop, considering the cup's wall contact and the centripetal force (~3N) that the outer wall must support as the ball moves off perpendicular to the arm.

Once the arm stops rotating, the centripetal demand vanishes since the ball's path becomes straight, so the wall's normal force stays minimal and spin from rolling in the cup won't affect flight since MuJoCo doesn't model Magnus effects by default. I keep friction at default values for the cup contact, and note that the joint limit will simply absorb the servo's torque when the arm hits the stop. Finally I consider the ball's resting position at θ=0 with the arm horizontal, sitting atop the cup.

I also want to double-check that the catapult's base support posts don't collide unexpectedly with the arm or ball, given that worldbody-attached static geoms might not benefit from the usual parent-child collision exclusion that applies between an arm body and its child components.

So rotation about +y by angle φ pushes the tip from pointing -x toward +z, confirming the axis and 0-45 degree range work as intended. Now I'm laying out the arm geometry: a thin box from x=-0.66 to 0.1 with small thickness and width, placing the cup floor near z=0.01, and positioning a 0.04-radius ball resting on that floor around x=-0.6, z=0.05.

I'm working out the wall placements around the ball — outer wall centered near x=-0.65, inner wall near x=-0.55, and side walls at y=±0.05 with small thickness to keep the ball centered with enough clearance, checking that heights and gaps leave the ball resting correctly against the floor.

Adjusting the outer wall position slightly (centering around -0.651) to avoid any initial penetration with the ball, and double-checking that centripetal force during the swing pushes the ball toward the outer wall as expected, with the release velocity combining the tangential components correctly.

Recalculating the release point at exactly θ=45°: using x = -0.4 + R sin45 + d cos45 and the corresponding y, I get release coordinates around (-0.389, 0.860), confirming the ball separates cleanly once the arm's deceleration triggers the limit constraint.

Now I'm positioning the bucket at x=2.4, built from a floor box plus four wall boxes with 0.25 inner half-width and 0.3 wall height. Checking the ball's descent trajectory, it hits the rim height steeply (~51° angle) with horizontal tolerance around ±0.21 after accounting for ball radius, so I'm weighing how sensitive the landing range is to small velocity changes.

Widening the bucket to 0.3 inner half-width with 0.25 wall height loosens that tolerance to roughly ±4.5% speed error, which feels safer given servo gravity compensation. Now I'm wondering whether the ball will actually settle inside rather than bounce out, since it lands around 5.6 m/s — MuJoCo's default contact damping should keep bounce minimal, but I need to think about whether the bucket body should be fixed in place.

Treating the bucket as static works. The real worry is whether the ball keeps oscillating between walls for the remaining ~5 seconds after landing, since a smooth box floor gives little energy loss once wall impacts are absorbed. I'm considering giving the ball geom condim 6 with added rolling friction to help it settle, estimating the rolling deceleration from a small rolling friction coefficient relative to the ball's radius.

I also need to check for unintended collisions: the catapult's pivot axle near the base shouldn't intersect the ball or arm given parent-child filtering, and the arm's tip clearance above the base plate at rest position should avoid any floor contact.

Now estimating masses and torques: with arm ~0.2kg, cup pieces ~0.08kg each, and ball ~0.1kg, total gravity torque at θ=0 comes to roughly 1.6 N·m, giving an effective cosine-scaled torque near 1.14 once I account for the moment arms.

At a 45° release angle this translates to a steady-state servo error around 0.11-0.114, since the time constant is small. Bumping kv to 20 halves the error to about 0.057, so I'm setting ctrl to roughly 7.798+0.057≈7.855. I'm also double-checking the ball's actual horizontal lever arm (~0.389 vs the 0.424 I'd assumed), which nudges its gravity torque contribution down slightly to about 0.38.

Recomputing at 45° with both cup and ball lever arms (0.40 and 0.389 respectively), total torque comes to about 1.09, giving an error of 0.055 at kv=20, so ctrl≈7.853. I'm also noticing the initial torque spike (157 Nm) produces an angular acceleration of ~1745 rad/s² — that's about 100g of tangential acceleration on the ball, which seems too jerky, so I'm considering capping forcerange to something like 15 Nm to smooth it out.

With that force limit, the arm takes about 47ms to ramp up to steady torque, reaching 0.18 rad before the servo linearizes — I'll set forcerange="-15 15" with forcelimited="true", since steady-state torque (1.1) stays well below that limit. Bumping kv to 30 under this same force limit gives a smaller error (0.036), so ctrl rounds to about 7.84. I'm also noting joint damping and armature are both zero, and the upper joint limit is set to 0–45 degrees with the arm resting at the lower limit under gravity, with no hinge friction — now wondering if the ball might shift within the cup during motion.

Since the ball is pressed against the floor it probably doesn't get disturbed by the initial acceleration, though it may still roll in place. At the joint limit, the solref settings (0.005 1) govern how the stop behaves, and since the servo torque saturates at 15 Nm there, it should hold firmly. After release with the arm fixed at 45°, I'm working through whether the ball's trajectory clears the cup — tracking its velocity components relative to the arm's rotating frame, where the position is split into a radial term and perpendicular offset, giving a velocity component of -ωd along the arm's direction.

I'm now realizing that component points inward toward the pivot, not outward toward the outer wall — meaning the ball actually drifts toward the inner wall. I'm computing the geometry: the inner wall face sits near x=-0.56, and the ball's center starts at x=-0.6 with radial velocity ωd≈0.39 m/s inward while climbing at ωR≈4.7 m/s. I need to check whether the ball's rising center position clears the inner wall's top edge (around z=0.04) given it starts at z=0.05, so I'm comparing the ball's path against the wall corner coordinates to see if there's a collision.

Working through the distance check, the ball passes just barely clear of the inner wall corner (0.041 vs 0.04 radius), so it's fine in the post-swing frame. I'm also considering the earlier phase of the swing, where centripetal and tangential forces act on the ball while it rests on the floor — gravity and tangential acceleration keep it pressed down initially, so I don't think the ball rolls inward prematurely, but I want to keep the inner wall low just in case.

Now I'm verifying the side-wall geometry (x span, y half-width, z range) against the ball's radius and center position to confirm there's no overlap, and then double-checking the release velocity formula by plugging in ω, R, and d values to confirm it matches the expected components.

With that confirmed, I'm moving to the bucket geometry at x=2.4: setting up the floor box dimensions and position, then defining the side walls' half-extents and center heights to establish the inner cavity width.

Tracing the ball's trajectory confirms it clears the pivot posts over the catapult base with margin. Now I'm setting up the keyframe, ordering qpos entries by body sequence—arm hinge first, then the ball's freejoint position and orientation, plus the control value for the arm actuator.

I'm checking the ball's resting position on the arm matches world coordinates correctly, with a small gap from the outer wall, and confirming contacts between ball and arm geoms work during motion. Now I'm thinking through naming conventions for the expected test conditions, like whether the resting surface should be called "bucket_floor" or "catapult_cup_floor," and how the arm's stop condition should be phrased to match the body name with the joint.

I'll name the stop condition "catapult_arm reaches its upper stop" and move on to writing the XML, setting the ball's mass to 0.1 with condim 6 friction properties.

