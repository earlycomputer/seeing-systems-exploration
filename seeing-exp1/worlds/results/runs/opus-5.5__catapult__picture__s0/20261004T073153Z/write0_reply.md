The scene uses a 0.5 m throwing arm with a cup at its tip, hinged 0.4 m above the floor. A constant-torque motor, set by the `start` keyframe, swings the arm until a joint limit stops it at 45°. The ball then flies on toward an open bucket centred 3 m downrange.

**How the torque was chosen.** I worked it out by hand from the arm's energy and the ball's path; I have not run the simulation.
- The ball has to leave the cup at about 5.3 m/s, at about 39° above horizontal.
- A torque of 6.22 N·m over the 45° swing gives that speed. That figure allows for the work spent lifting the arm and ball against gravity.
- On that path, the ball clears the near rim with about 0.28 m to spare and drops in near the far side of the bucket.
- The bucket's inner diameter is 0.6 m. That allows roughly ±0.25 m of error in how far the ball travels before it misses.

**Contacts.** Collision bits keep the arm from touching the frame and the floor. The ball still collides with the cup.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="-0.3 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.85 0.8 1"/>

    <!-- static catapult frame -->
    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" size="0.4 0.15 0.03" pos="-0.15 0 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_post_left" type="box" size="0.03 0.015 0.185" pos="0 0.08 0.215" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_post_right" type="box" size="0.03 0.015 0.185" pos="0 -0.08 0.215" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" fromto="0 -0.1 0.4 0 0.1 0.4" size="0.01" rgba="0.3 0.3 0.3 1"/>

      <!-- throwing arm: hinge about y, swings from horizontal (pointing -x) up to 45 deg -->
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 45" solreflimit="0.01 1" damping="0"/>
        <geom name="catapult_hub" type="cylinder" fromto="0 -0.03 0 0 0.03 0" size="0.02" mass="0.02" contype="2" conaffinity="2" rgba="0.3 0.3 0.3 1"/>
        <geom name="catapult_beam" type="box" size="0.3 0.03 0.01" pos="-0.28 0 0" mass="0.3" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
        <geom name="catapult_lip_outer" type="box" size="0.015 0.03 0.03" pos="-0.555 0 0.04" mass="0.02" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
        <geom name="catapult_lip_inner" type="box" size="0.015 0.03 0.03" pos="-0.44 0 0.04" mass="0.02" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
      </body>
    </body>

    <!-- ball resting in the cup at the arm tip -->
    <body name="ball" pos="-0.5 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" rgba="0.9 0.2 0.2 1"/>
    </body>

    <!-- open bucket centred 3 m downrange, inner radius 0.30 m, rim at 0.36 m -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.32 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" size="0.01 0.062 0.18" pos="0.31 0 0.18" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" size="0.01 0.062 0.18" pos="0.2864 0.1186 0.18" euler="0 0 22.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" size="0.01 0.062 0.18" pos="0.2192 0.2192 0.18" euler="0 0 45" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" size="0.01 0.062 0.18" pos="0.1186 0.2864 0.18" euler="0 0 67.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" size="0.01 0.062 0.18" pos="0 0.31 0.18" euler="0 0 90" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" size="0.01 0.062 0.18" pos="-0.1186 0.2864 0.18" euler="0 0 112.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" size="0.01 0.062 0.18" pos="-0.2192 0.2192 0.18" euler="0 0 135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" size="0.01 0.062 0.18" pos="-0.2864 0.1186 0.18" euler="0 0 157.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" size="0.01 0.062 0.18" pos="-0.31 0 0.18" euler="0 0 180" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" size="0.01 0.062 0.18" pos="-0.2864 -0.1186 0.18" euler="0 0 202.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" size="0.01 0.062 0.18" pos="-0.2192 -0.2192 0.18" euler="0 0 225" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" size="0.01 0.062 0.18" pos="-0.1186 -0.2864 0.18" euler="0 0 247.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_12" type="box" size="0.01 0.062 0.18" pos="0 -0.31 0.18" euler="0 0 270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_13" type="box" size="0.01 0.062 0.18" pos="0.1186 -0.2864 0.18" euler="0 0 292.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_14" type="box" size="0.01 0.062 0.18" pos="0.2192 -0.2192 0.18" euler="0 0 315" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_15" type="box" size="0.01 0.062 0.18" pos="0.2864 -0.1186 0.18" euler="0 0 337.5" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="6.22"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that actually launches a ball into a bucket 3 meters away, with physics that works in simulation. I'm thinking of a hinged arm with a cup at the end, driven by a motor or spring, rotating until it hits a hard stop at the joint's range limit, releasing the ball at the right trajectory.

I'm working through the ballistics math now—figuring out launch angle, arm length, pivot height, and rotation direction so the ball releases tangent to the arc at roughly 45 degrees and lands in the bucket.

I also need to think about whether the ball actually separates cleanly from the cup when the arm stops abruptly, since the cup wall that pushes the ball is oriented along the tangential velocity direction at release.

So the ball rests on top of the arm, with gravity holding it down and the arm's upward motion acting as the tangential push; the outer end needs a small lip to resist centrifugal force during acceleration, but that lip won't block the ball's release since the velocity direction carries it away from the arm surface cleanly.

The arm hitting its joint limit will have some softness causing minor bounce or overshoot, but release should happen right around when deceleration starts, near the limit angle—good enough approximation given the uncertainty in exact timing from contact softness, so I'll pick a release angle and bucket size that's forgiving of this error.

A motor actuator with constant torque seems like a cleaner approach than setting initial joint velocity directly, which would hit the ball impulsively since it starts at rest. With constant torque, I can compute the arm's angular velocity at the stop angle using energy conservation—torque times angle swept, minus the gravitational work done lifting the arm and ball—then the motor continues pushing against the limit afterward, keeping things stable.

Now I'm setting up the geometry: catapult base at the origin, bucket target 3m away, pivot height 0.4m, arm length 0.5m. I'm working out where the ball sits relative to the arm's surface at the 45° release angle, accounting for arm thickness and ball radius to get the ball's offset along the arm's normal direction, then computing the ball's actual center position at release using the pivot location and rotated arm axis.

Using angular velocity ω about the y-axis, I'm cross-producting with the ball's position vector relative to the pivot to get launch velocity components, then finding the launch angle from the velocity ratio — coming out to about 39.3°.

Now I'm setting up the trajectory equation targeting the bucket opening at x=3.0, z=0.35, solving for the required launch speed v given the angle and gravity, working through the quadratic algebra to isolate v².

Solving gives v=5.35 m/s, so the angular velocity needed is about 10.64 rad/s. I'm also considering some slack in bucket sizing (0.25m inner radius vs 0.04m ball radius) and thinking about whether to model the arm dynamics more precisely, accounting for the ball sliding outward due to centrifugal force and starting in contact with the lip at radius L.

Now I'm working out the arm geometry in the local body frame - positioning the box for the arm, placing the ball's center and the lip relative to the pivot, and computing moments of inertia needed to determine the motor torque and energy required to reach the target angular velocity.

Once contact force drops to zero the friction is negligible, so I could shrink the lip height slightly to minimize interaction. During the soft-limit overshoot, the lip keeps rotating with the arm while the ball moves tangentially straight, so the ball just pulls ahead of the slower-moving lip — that's fine and shouldn't cause issues. I should double check the side walls stay symmetric so the ball doesn't drift sideways from any small asymmetry.

I'll skip adding side rails since the symmetry keeps y at zero numerically, and I should set the arm's rotation range to [0°, 45°] with a lower limit at the horizontal rest position, letting the motor torque start rotation immediately at t=0. I also need to exclude unwanted collisions between the arm and base by making the arm a child body of the base so they don't interact physically.

Actually the parent filter may not reliably exclude world-welded static bodies, so I'll just use contype/conaffinity groups instead: frame geoms get type 1, arm geoms get type 2 so they never collide with each other, while the ball needs a separate mask that lets it hit both.

For the physical layout, I'm placing pivot posts at z=0.4 with the arm swinging in the y=0 plane between posts at y=±0.1, axle as a cylinder, base as a ground box — and checking that the ball's flight path clears the pivot region as it passes overhead.

Now I'm checking clearances at the ball's starting position relative to the arm, confirming the bottom of the ball sits just above the arm's top surface with no initial overlap. Then I move to mass and inertia: assigning the arm a modest mass with small end lips, the ball a lighter mass, and starting to compute the arm's moment of inertia about the pivot based on its length and density distribution.

I should let motor torque dominate the calculation instead. Working out the energy, I get kinetic energy of about 3.85 J from the angular velocity and moment of inertia. Now I'm computing how much the arm's center of mass rises as it rotates 45 degrees, tracking the rotated coordinates for the box, lips, and ball components.

For potential energy, I calculate each component's rise separately (box: 0.198, outer lip: 0.381, inner lip: 0.303, ball: 0.339), weight them by mass, and sum to get PE ≈ 1.05 J. Adding this to the kinetic energy gives total work of 4.90 J, so the required torque comes out to about 6.24 N·m. I'm also noting I still need to account for the ball's translational kinetic energy in this calculation.

The ball's rotational energy contribution is negligible since its moment of inertia is tiny (~6.4e-5). For accuracy margins, a 2% speed error translates to roughly 4% range error—about 13 cm—so I want the bucket's inner radius generous (0.2 m) to tolerate this and other error sources like joint limit softness.

Since the limit constraint uses soft solref, there's overshoot: the motor keeps accelerating past the limit angle until constraint force catches up, causing a 1-2° release angle error that shifts range slightly, though near the optimal angle this effect is fairly muted. I'm considering tightening the limit stiffness (solreflimit around 0.005, timeconstant 0.01, respecting the timestep constraint) to make the catapult release timing more predictable and repeatable.

I should also double check the motor's gear and ctrlrange settings, confirm joint damping/armature/frictionloss are all zero, and verify the ball stays pinned at radius 0.5 against the outer lip from centrifugal force without sinking into the arm surface. One more thing to check is whether the joint's lower limit at θ=0 is set up correctly so the motor torque pushes away from it immediately, and whether to use a degree-based range like "0 45" given the compiler's default angle units.

For the keyframe, I need qpos to list all joints in body-tree order -- arm hinge first, then the ball's seven freejoint values -- but hinge values are always stored in radians regardless of compiler angle units. I'm considering just omitting qpos from the keyframe entirely and only specifying ctrl, since unspecified qpos should default to qpos0 from the model.

For the ball, I want it starting at rest, so qvel stays zero. For the bucket, I'm placing it at x=3.0, about 3 meters from the catapult pivot near the origin, and building its walls as a ring of boxes around a cylindrical base since cylinders themselves can't be hollow.

I'm now checking the actual trajectory: with my chosen launch angle and speed, the ball is descending steeply (around 47°) as it reaches x=3.0, and moving forward about 0.3m more while dropping from rim height to the bottom. That means targeting the bucket center at rim height isn't quite right — it would land outside the bucket, closer to x=3.3, so I need to aim the trajectory to cross the rim height a bit earlier instead.

Actually, if the ball hits the far wall it can just bounce back in and settle, since MuJoCo's default contact damping is fairly inelastic — so I just need the ball to clear the near rim and land somewhere inside the far wall below its top edge. With inner radius 0.25, the opening at rim height spans roughly x=2.75 to 3.25, so the ball's center needs to pass through about x=2.79 to 3.21 to make it in.

I'll keep the bucket static rather than giving it a freejoint, since a dynamic bucket risks tipping over on ball impact and static is simpler and more robust. Now I want to double check my velocity calculation more carefully, including how the ball is supported during the arm's acceleration phase.

Checking the centripetal force at full speed, it's well within reason. I also verify gravity torque doesn't stall the motor at the start of the swing, and estimate the torque balance at 45° once the arm hits its limit after release.

Then I trace the ball's flight path once released, confirming its trajectory clears the catapult frame and doesn't collide with the arm itself, since the arm's orientation points back and up while the ball launches forward. I'm also double-checking the geometry at the lip where the ball separates from the arm.

I check whether the ball maintains rigid-body rotation with the arm without slipping, which would mean no frictional losses to account for in the energy calculation, since the ball stays pressed against the lip and surface only until release.

The contact force pushing the ball against the surface is small, so penetration is minimal and negligible for the simulation. The limit constraint activates right around 45°, with the arm reaching max speed only slightly past that point — a negligible discrepancy, so I'll tighten the solreflimit setting to reduce softness.

Now I'm recomputing the release trajectory numerically: the ball's world position at θ=45° works out to roughly x=-0.318, z=0.789, and I'm now verifying the velocity vector direction given the hinge axis orientation about +y.

Checking against this, the velocity components come out as (0.389, 0.318)·w, which matches the position derivative, confirming consistency. For the target, I'm reconsidering the ball center height—maybe placing it at z=0.30 near x=3.0 makes more sense than 0.35, since that puts the ball more plausibly at rim level rather than fully inside it.

Computing moments of inertia for each geom using parallel axis theorem, working out box dimensions and masses for the arm and lip components to get accurate rotational dynamics.

Adding a small hub cylinder at the pivot contributes negligible inertia, so total moment of inertia sums to about 0.068. Computing kinetic energy from this with the angular velocity gives roughly 3.79 J, and now I'm working out the potential energy from the arm's rise using its center of mass position.

Summing the rises of the outer lip, inner lip, and ball positions gives a total PE of about 1.05 J, so total work is 4.841 J, yielding a torque of about 6.164 N·m. I'm double-checking whether treating the ball's energy this way is valid given it starts at rest nestled against the arm with soft contact.

I also want to account for uncertainty in the ball's settling position—with the bucket's inner radius giving roughly a ±0.2 m window, that translates to about 6% variation in radius, 3% in speed, and 6% in energy, which seems acceptable. I'm also checking whether penetration depth at the lip contact point shifts the ball's effective radius slightly from 0.5 m, and verifying the trajectory height near the bucket rim at x=2.75 to confirm clearance.

Redoing the trajectory math, I find the ball center passes about 0.52 m above the near rim (clearing the 0.35 m rim comfortably), and by the far rim at x=3.25 the ball center drops to essentially rim height, meaning it just reaches the far wall around x=3.21.

Solving for where the ball contacts the bucket bottom (accounting for bottom plate thickness at z=0.02), I get x≈3.205 — right at the far wall, consistent with landing near the bucket's far edge.

Tightening the aim, I consider targeting the ball's landing at the bucket's center bottom instead, around (2.95-3.0, 0.06), and need to check the trajectory clears the near rim at x≈2.75-2.78 without clipping the corner given the steep descent angle.

That gives x_r∈[2.78,3.13], a 0.35m window centered near 2.955, wide enough with a bucket radius of 0.25-0.3m that the ball lands softly on the far wall and settles inside rather than rimming out.

Working through the numbers, targeting the rim at (2.95, 0.39) with the given launch angle gives velocity ~5.34 m/s and angular speed ~10.6 rad/s, requiring torque around 6.2 N·m to achieve the needed kinetic energy. I'm now checking how sensitive the landing range is to small changes in that torque value, since range scales roughly with kinetic energy.

I'm estimating that a 1% torque increase nudges the range by about 4 cm, so a ±0.2 N·m window corresponds to roughly ±5% torque tolerance, which seems acceptable. I'm also sanity-checking the simulation timestep against the arm's swing time to confirm there are enough steps resolving the 45° motion, and considering whether soft contact at the lip (given the ball's compliance and contact stiffness) could meaningfully affect the ball's effective radius during release.

Working through the steady-state penetration formula, I get roughly 1 mm under the 56 m/s² acceleration and 0.19 mm under gravity — both negligible. The ball starts exactly touching the lip at radius 0.5, so I should check whether it could contact the arm's inner lip after release.

Adjusting the inner lip face position slightly to leave a small gap so the ball doesn't touch both lips simultaneously, which won't meaningfully affect inertia. I'm also checking the frame geometry — posts, axle cylinder, and hub placements relative to the arm — to make sure nothing improperly overlaps near the pivot.

Now I'm reviewing collision groups: frame geoms default to contype 1, and I'm confirming the ball's trajectory avoids them while the base box and posts sit correctly on the floor. I'm also considering whether a decorative crossbar between the posts would interfere with the arm resting at 45°, checking if the arm's width fits between the posts without colliding given its contype exclusion.

Skipping that extra strut idea, I'll move to setting up the floor, lighting, and keyframe controls, plus ball collision properties. Then I'm defining the bucket geometry — a cylindrical bottom and sixteen angled wall segments arranged around the rim to approximate a circular basket, working out their dimensions and overlap to fully enclose the bucket's interior.

Computing the positions for each wall segment...

Finishing the trig values for the remaining boxes, then checking the rim clearance at 0.36 — the ball should clear the near wall comfortably but barely clip the far wall at x≈3.26, giving a height around z=0.789 there.

Working through the drop with gravity, nominal landing comes out near z=0.034, meaning the ball settles just at the bottom near x≈3.2, right before the far wall — close to the 3.26 limit but inside it. That gives roughly a 0.25 m margin on the positive side before the ball would clear the far wall at too great a height.

Checking the near rim side, the clearance at x=2.70 with corner height 0.36 works out to about 0.638, which gives a similar roughly symmetric margin of about -0.25 m, so the overall window looks like ±0.25 m, or roughly ±7.5% of the range — I'm fine keeping the aim as is rather than shortening it. I also want to double check what happens physically once the ball hits the bottom, since it might bounce or roll rather than just stop.

Once it lands it'll likely roll along the floor toward the far wall and settle there, which is fine either way, and I'm setting y to zero for the ball. I'm defining the catapult's motor and hinge joint along with the arm body position, and placing the ball body accordingly.

Still writing arm geometry...

The difference is negligible, so torque settles around 6.2. I'm confirming the resting position at θ=0 makes sense, that the energy method correctly accounts for motor torque alone, and that armature defaults to zero. Now writing the final MJCF, including the visual light setup, default gravity, and an explicit compiler angle setting in degrees.

