The catapult is a hinged arm with a cup at its tip. A motor, whose torque the keyframe sets, swings the arm up until a joint limit at 45° stops it, and the ball flies on toward an open bucket centred 3 m away. I haven't run this file. I picked the torque by hand from an energy balance: about 5.7 N·m should give roughly 4.7 m/s at release, which lands the ball about 3.05 m out on the bucket floor. The bucket's inner radius of 0.30 m leaves some margin, but if it misses, the torque is the value to adjust. Rolling friction on the ball is meant to bring it to rest inside the bucket well before 6 s, but I haven't checked that either.

```xml
<mujoco model="catapult_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- static catapult frame -->
    <geom name="catapult_base" type="box" pos="0.5 0 0.02" size="0.3 0.2 0.02" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_l" type="box" pos="0.5 0.12 0.21" size="0.03 0.02 0.19" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_r" type="box" pos="0.5 -0.12 0.21" size="0.03 0.02 0.19" rgba="0.5 0.3 0.1 1"/>

    <!-- throwing arm, pivot at (0.5, 0, 0.4); positive rotation about +y lifts the cup end -->
    <body name="catapult_arm" pos="0.5 0 0.4">
      <inertial pos="-0.26 0 0" mass="0.5" diaginertia="0.0003 0.015 0.015"/>
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-10 45" solreflimit="0.01 1" damping="0"/>
      <geom name="catapult_axle" type="cylinder" pos="0 0 0" euler="90 0 0" size="0.02 0.09" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_beam" type="box" pos="-0.26 0 0" size="0.30 0.03 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_base" type="box" pos="-0.5 0 0" size="0.06 0.062 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.552 0 0.03" size="0.01 0.062 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.455 0 0.018" size="0.01 0.062 0.008" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_side_l" type="box" pos="-0.5 0.052 0.03" size="0.06 0.01 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_side_r" type="box" pos="-0.5 -0.052 0.03" size="0.06 0.01 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <!-- bucket, centre 3 m from the ball's start (0,0,0.45) -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.32 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0.145" euler="0 0 0" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2685 0.155 0.145" euler="0 0 30" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.155 0.2685 0.145" euler="0 0 60" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.31 0.145" euler="0 0 90" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.155 0.2685 0.145" euler="0 0 120" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.2685 0.155 0.145" euler="0 0 150" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.31 0 0.145" euler="0 0 180" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2685 -0.155 0.145" euler="0 0 210" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.155 -0.2685 0.145" euler="0 0 240" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.31 0.145" euler="0 0 270" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.155 -0.2685 0.145" euler="0 0 300" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.2685 -0.155 0.145" euler="0 0 330" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- ball resting in the catapult cup -->
    <body name="ball" pos="0 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="0.8 0.01 0.01" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="5.7"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through a catapult mechanism that launches a ball 3 meters horizontally into a bucket, settling by 6 seconds — considering whether to drive the arm with a motor and stop, or simply give it an initial angular velocity through a keyframe to achieve the right launch trajectory.

The ball should start at rest while the arm rotates, so release velocity depends on where I place the joint stop: if the arm halts around 45° from horizontal, the tip's tangential velocity direction at that instant determines the launch angle and speed needed to land in the bucket.

The outer lip needs to counter centrifugal force keeping the ball radially contained, while the inner edge handles centripetal constraint toward the pivot — this works fine for release since the ball's velocity is tangential at separation. Rather than relying purely on collision geometry, I think a joint limit with range constraints is simpler than adding a physical crossbar stop, and I'll drive the arm with a motor using constant control.

Now I need to work out the actual projectile math: with arm length 0.5m from pivot to ball center, I need to compute the required launch speed for a 3m horizontal range at 45°, accounting for the height difference between launch point and target bucket.

I also realize the ball doesn't sit exactly on the pivot-to-end axis — it rests slightly offset above the arm's surface by its radius, so I need to factor that perpendicular offset into the release position calculation along with the arm angle.

Working through the velocity vector, I find the actual launch angle is slightly less than 45° because of this offset — with a small offset value, the effective angle comes out closer to 39°, which I should use for the trajectory computation.

Separation likely happens near the angle limit itself, since the joint's soft constraint only kicks in with a short time constant as the arm decelerates, so the ball's velocity at separation should closely match the velocity at the limit angle despite continued motor and gravity effects. I'm fairly confident the ball stays in contact with the arm throughout the swing given the combined inertia, rather than trying to track exact motor energy input.

I can solve for the needed angular velocity at 45° and back out the required motor torque using an energy balance that accounts for gravitational work on both arm and ball plus total rotational inertia; a few percent of error here translates to roughly 10 cm of range error out of 3 m, which a generously sized bucket (say 0.25 m inner radius) should absorb. To reduce sensitivity to the ball's exact contribution, I'm considering making the arm heavy relative to the ball and computing its inertia precisely, possibly specifying an explicit inertial element for the arm body rather than relying on MuJoCo's automatic mass computation from geometry.

Now I'm accounting for the ball's rolling contact against the arm floor and lip — it likely co-rotates with the arm, so its effective contribution includes both the translational term from its radius and a small rotational term (2/5 m R²) from its own spin, both of which I'll fold into the total inertia. I'm settling on numbers for the ball: radius 0.04 m, mass around 0.1 kg.

For the arm's hinge, I'm working out which rotation direction about the y-axis lifts the cup tip from -x position upward — positive rotation about +y does this, so I'll set the axis accordingly with a 0 to 45 degree range, keeping in mind the compiler uses degrees by default for ranges but radians for keyframe qpos values.

I'm considering whether to switch the compiler to radian angles for clarity, and thinking through the initial hinge position relative to the limit — since gravity will pull the arm down at the lower limit but the motor torque should easily overcome it, I'll just leave the initial qpos near zero and let the motor accelerate the arm immediately once simulation starts.

Now I'm working out the arm's box geometry and placing the cup precisely so the ball rests touching the cup's outer wall, computing coordinates for the pivot, box half-lengths, and wall positions to ensure correct contact.

Centrifugal force will push the ball outward slightly during rotation, but that's negligible movement. For pivot height, I'll set H=0.4m, checking that the arm clears the ground at the lower rotation limit of -0.2 rad, and placing the pivot at x=0.5 so the ball starts at world x=0.

Now I'm computing the rotational inertia of the arm-ball system about the pivot: the arm contributes about 0.0488 kg·m² using the rod formula plus parallel axis theorem, the ball adds about 0.02525 from its distance squared plus a tiny spin term, giving a total around 0.0741 kg·m².

With friction assumed to keep the ball rolling with the arm, I'm figuring out release conditions at a 45° arm angle. I compute the ball's world position by rotating its offset (-L, d) from the pivot, getting roughly x=0.182, z=0.789, and then derive the release velocity direction from the angular rate, getting components proportional to (L+d) and (L-d) scaled by 0.707.

Now I'm thinking about where the ball needs to land to land inside the bucket—aiming for a point somewhere between the bucket's rim and bottom, around z=0.15-0.3, so the steep ~45° descent lands it near the bucket's interior rather than overshooting past x=3.

Default MuJoCo contacts are fairly inelastic, so bouncing should be minimal. For the ball settling in the bucket, I'm considering adding rolling friction via condim 6 and a friction tuple with a small rolling coefficient so it doesn't roll forever after wall collisions.

With a rolling friction coefficient around 0.005, the deceleration works out to roughly 1.2 m/s², which should bring the ball to rest quickly without needing an absorbent floor material. Now I need to figure out the launch speed required to land the ball in the bucket, starting from the ball's initial position and working out the target landing point near the bucket floor.

Computing the displacement components, I get a launch angle around 39.3 degrees, and I'm now solving the projectile equation to match the horizontal and vertical drop to the target point, isolating the term involving velocity squared to solve for the required speed.

Working through it, I get v² ≈ 21.9, so v ≈ 4.68 m/s, giving angular velocity ω ≈ 9.31 rad/s from ω = v/r. Then I compute the rotational kinetic energy and start setting up the gravitational potential energy change from the arm's center of mass rising as it swings through angle φ.

Checking gravity torque magnitude stays below the applied torque, so angular acceleration stays positive throughout. The real question is when the ball separates from the arm—since the joint limit uses a soft constraint with a small solref, the arm starts decelerating right as it crosses 45°, and the ball would separate almost immediately once that deceleration begins, given it needs centripetal support from the arm's lip.

Once the centripetal constraint vanishes, the ball travels in a straight tangent line that drifts outward from the circular path, away from the pivot. In the arm's frame, this means the ball moves along the normal direction but with a slight component back toward the pivot side, since the release velocity is ω times (L along the normal minus d along the radial direction toward the tip). So the ball's trajectory relative to the arm has this subtle inward bias even as it separates outward overall.

Checking the corner distance calculation, it comes out just barely over the ball radius, so contact is avoided as the ball rises and moves inward during the arm's motion—the distance to the lip corner only increases from there. I'm also considering whether the inner lip matters at all, since on a horizontal arm at rest the ball just stays put until acceleration begins.

As the arm tilts upward, gravity pulls the ball toward the pivot while centrifugal force pushes it outward, and early on with low angular velocity the inward gravity term dominates, so the inner lip is still necessary—I'll just make it shorter, lowering its half-height and adjusting its z-range. Side walls seem fine as configured for clearance. I'm also thinking about adding friction to the ball-cup contact and making sure the arm doesn't collide with the static frame geoms, possibly by excluding contacts between them or structuring the arm as a child body appropriately.

I'm uncertain whether MuJoCo's parent-child collision filter applies when the parent is the world body, so rather than rely on that, I should position the frame geoms—like the support posts and axle cylinder at the pivot—so they physically avoid intersecting the arm geometry.

Checking the dimensions: posts at y=±0.12 with width 0.10-0.14 won't overlap the axle if its half-length stays around 0.09, and the arm's width of ±0.04 keeps clear too. The ball travels at y=0, well inside the posts at |y|≥0.1, and the ground base at z 0-0.04 sits below the arm's lowest swing angle, so nothing should collide unexpectedly.

The arm shouldn't hit anything beyond its limit — it rests there with the motor pushing against a soft limit with small penetration from the solref settings, and since it's critically damped it won't bounce back toward where the ball used to be. Now I need to verify the ball's trajectory clears the bucket rim, checking that the ball's center height exceeds the rim top plus its radius as it passes near x≈2.75.

Computing the trajectory with v=4.679 m/s at α=39.29°, I get vx≈3.62 and vz0≈2.96. Tracking z(t) against the quadratic equation, the ball reaches peak height around 1.68 at t=0.604s, well clear. Solving for when z drops to 0.06, I find t≈0.792s giving x≈3.049, matching the target landing spot — confirming the ball clears the wall at height 0.3.

I'll make the bucket a bit more generous to add margin—inner radius 0.3 with a 0.25 wall height, built as a ring of 12 angled box segments around the circle plus a cylindrical bottom plate, giving enough tolerance for small velocity variations in the landing trajectory.

Computing wall positions...

I'm making the bucket body static with no joint, welded to world, since both it and the floor are static so no collision computation needed between them. Placing the bucket center about 3 meters from where the ball starts.

Checking the ball's trajectory into the bucket—it should land near the bottom, roll with friction, and possibly contact the far wall. The joint limits and contact softness seem reasonable given the default solimp settings, and the ball's spin at release shouldn't cause issues. Now I'm looking at the motor actuator definition for the catapult.

Working out qpos ordering—since the arm body comes before the ball in the tree, qpos should be hinge angle followed by the ball's seven freejoint values. I'm verifying the ball's world position by transforming its arm-frame coordinates through the pivot, confirming it lands at (0,0,0.45), and now checking lip clearance on the bucket's outer rim.

For the keyframe, I'll explicitly include the full qpos string rather than relying on defaults, just to be safe. For contact properties, I'm setting condim=6 with friction values tuned so torsional and rolling resistance are realistic—rolling friction around 0.005 should decelerate the ball gradually after it lands at roughly 3.6 m/s horizontal speed, letting it roll out naturally rather than sliding indefinitely.

I'm timing the arm launch: angular acceleration around 55 rad/s² gets the arm to 0.785 rad in about 0.17s, with the ball landing around 1 second in, leaving plenty of simulation time before it settles. I'm bumping rolling friction up slightly to 0.01 for safety, which gives a bit more deceleration (~2.5 m/s²) and should avoid any weird jitter from soft contacts without causing problems during the catapult launch phase itself.

Now I'm setting up the catapult geometry: solver and integrator can stay at defaults (Euler, implicitfast), the ball gets a sensible mass/density, and I'm placing the base box, side posts (sized so their tops align with the axle height), and figuring out where the arm tip sits relative to the ball's starting position so the throw geometry works out correctly.

Adding the side walls and axle cylinder for the cup geometry, then double-checking the explicit inertial properties (mass, diagonal inertia) are correctly specified relative to the body's center of mass about the pivot.

For the hinge joint, I'm setting a limited range with damping, and tuning solreflimit to be stiff enough for a crisp stop while remaining compatible with the simulation timestep.

Verifying the rotation direction confirms the arm swings upward correctly, and gravity torque at zero angle is properly overcome by the motor so the arm doesn't droop. I'm now tracing where the arm settles at the 45° limit and checking the ball's trajectory clears the pivot as it launches forward and up.

