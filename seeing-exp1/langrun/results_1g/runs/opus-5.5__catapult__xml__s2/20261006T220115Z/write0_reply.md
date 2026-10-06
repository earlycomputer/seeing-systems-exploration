This catapult has a spring-free throwing arm driven by a constant-torque motor. The keyframe sets the motor control to 5.51 N·m. The arm swings up from horizontal and is stopped by its hinge limit at 40°. At that moment the ball leaves the cup on the arm tip at about 4.85 m/s, about 44° above horizontal.

**How the launch was sized**
- The torque came from an energy balance. Motor work over 40° equals arm, cup and ball kinetic energy plus the gravity lift.
- The ball should pass bucket-centre height x = 3 m at about mid-depth in the bucket.
- The calculated trajectory clears the near rim by about 0.12 m and falls short of the far wall by about 0.17 m.
- I haven't run it. The estimated margin corresponds to only about ±2% error in release speed.

**Two simplifications**
- **Stop bar is decorative.** The padded stop bar and the frame don't collide with anything. The joint limit does the actual stopping.
- **Wide bucket.** The bucket is a wide tub, 0.56 m inside diameter, to give the throw some tolerance.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" pos="0.35 0 0.025" size="0.4 0.18 0.025" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_upright_left" type="box" pos="0.5 0.12 0.185" size="0.02 0.015 0.135" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_upright_right" type="box" pos="0.5 -0.12 0.185" size="0.02 0.015 0.135" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" pos="0.5 0 0.3" euler="90 0 0" size="0.012 0.135" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_stop_post_left" type="box" pos="0.331 0.12 0.27" size="0.015 0.015 0.22" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_stop_post_right" type="box" pos="0.331 -0.12 0.27" size="0.015 0.015 0.22" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_stop_bar" type="cylinder" pos="0.331 0 0.4875" euler="90 0 0" size="0.02 0.135" contype="0" conaffinity="0" rgba="0.6 0.1 0.1 1"/>
    </body>

    <body name="catapult_arm" pos="0.5 0 0.3">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 40" limited="true" solreflimit="0.005 1"/>
      <geom name="catapult_arm_beam" type="box" pos="-0.275 0 0" size="0.275 0.03 0.015" mass="0.3" rgba="0.6 0.45 0.25 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.55 0 0.045" size="0.01 0.065 0.03" mass="0.02" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.44 0 0.045" size="0.01 0.065 0.03" mass="0.02" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_side_left" type="box" pos="-0.495 0.055 0.045" size="0.045 0.01 0.03" mass="0.02" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_side_right" type="box" pos="-0.495 -0.055 0.045" size="0.045 0.01 0.03" mass="0.02" rgba="0.4 0.3 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.355">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.05" condim="6" friction="0.8 0.005 0.002" solref="0.005 1" rgba="0.9 0.2 0.1 1"/>
    </body>

    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 -0.03" size="0.3 0.05" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.29 0 0.17" euler="0 0 0" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2511 0.145 0.17" euler="0 0 30" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.145 0.2511 0.17" euler="0 0 60" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.29 0.17" euler="0 0 90" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.145 0.2511 0.17" euler="0 0 120" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.2511 0.145 0.17" euler="0 0 150" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.29 0 0.17" euler="0 0 180" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2511 -0.145 0.17" euler="0 0 210" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.145 -0.2511 0.17" euler="0 0 240" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.29 0.17" euler="0 0 270" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.145 -0.2511 0.17" euler="0 0 300" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.2511 -0.145 0.17" euler="0 0 330" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="5.51"/>
  </keyframe>
</mujoco>
```

```expect
catapult_arm reaches its upper stop
ball touches bucket
ball comes to rest in bucket
```

---
thinking (summarized):

I need to design a catapult that reliably launches a ball 3 meters into a bucket, without the ability to test-run the simulation first. I'm considering a hinged arm with a cup holding the ball, driven by either a motor keyframe or a spring joint, but predicting the exact release velocity and trajectory analytically will be tricky since I can't iterate through actual testing.

I'm working through the geometry: setting the hinge axis along y, with the arm starting pointing horizontally backward and swinging forward until it hits a joint limit stop. The tip velocity at release is perpendicular to the arm's direction, so I'm computing the arm angle where that velocity vector points at roughly 45 degrees upward and forward to maximize range.

I also need the cup holding the ball to keep it seated during the swing via centripetal and surface contact forces, then check that at the release angle the ball separates cleanly from the cup walls without catching on them.

Simpler approach: rather than deal with catapult launch complexities, maybe I should give the arm an initial angular velocity directly through a keyframe, though this risks an unrealistic impulse if the ball starts at rest in the cup. A motor-driven arm that accelerates the ball, then stops abruptly at a joint limit, would let the ball's momentum carry it forward at release — I need to figure out what that release speed actually works out to.

Now I'm figuring out the release geometry: the tip position at a 135° swing differs from the start position, so I need the horizontal and vertical offsets between them to compute where the ball launches from relative to its starting point, then set concrete values like arm length and hinge height so the resulting projectile lands roughly 3 meters away in the bucket.

I'll treat the small arm-thickness offset as a minor correction for now and focus on the energy balance instead: motor torque times the 45° rotation angle, minus gravitational work from lifting the arm and ball, should equal the kinetic energy at release, which gives me the angular velocity and thus the launch speed needed to compute the projectile's horizontal range to the bucket.

The ball separates right as deceleration starts since it can't be pulled backward, and during the swing the cup wall needs to supply the centripetal force—roughly 50 m/s² per unit mass given ω²r—while tangential release should be clean since there's no wall conflict then. I should also double check the joint limit's soft stop behavior, since with default solref parameters the arm's penetration into the limit affects exactly when separation occurs.

Since timestep is 0.002, I should set the limit's timeconst to at least twice that, so 0.005 works well. A physical crossbar stop would look more classic, but the joint limit approach is simpler and cleaner to implement. Now I'm sizing the arm and ball: light arm around 0.2 kg with a rod-like inertia, and a ball roughly 0.05 kg at 4 cm radius to keep the dynamics reasonable for the motor torque calculation.

I'm working out the hinge geometry — placing the arm body with its hinge axis along y, starting oriented along -x, and deriving how rotation angle α maps tip position via standard rotation about y, confirming that positive α lifts the arm as expected.

Checking the joint range (0 to 45°) and confirming positive motor control gives positive torque driving positive α, matching the intended motion. I'm also working through the gravity torque on the arm at rest — computing the cross product of the arm's weight force with its position vector relative to the hinge, finding it produces a negative torque about y that pushes α below zero, against the joint limit.

Now I'm computing the work done against gravity as the arm rotates from 0 to 45°, using the rise in the center of mass height, and double-checking the arm's box geometry starting from the hinge point.

Still working out the cup geometry at the arm tip, positioning the ball and sizing the cup walls so the ball sits inside without clipping through.

At release, the ball should separate from the wall naturally since the arm stops and no centripetal force remains, so friction isn't an issue—any small penetration kick is minor and the walls could just be made short/thin if needed. I'm now computing the ball's distance from the hinge and its release velocity using the radius of 0.503 from the geometry.

Working out the velocity direction requires tracking the angle of the radius vector through the 45° rotation, since the tip starts at 180° and ends at 135°, giving a velocity direction 90° off that. To get roughly a 45° launch elevation, I can tune the stopping angle α to around 38°, though other values could work too since the exact angle isn't critical.

Computing the release coordinates, the ball starts at x=0, z=0.355, with the bucket centered at x=3. I'm also accounting for slight overshoot past the 40° limit as the arm decelerates before the ball separates, then estimating the bucket rim height and inner radius to define the landing target.

Given the sensitivity of the energy and timing calculations, small errors in speed translate into meaningful range errors, so I'm widening the bucket to roughly 0.25-0.3m inner radius—making it a larger tub—to give more margin for approximation error in the physics.

I also need to think about whether the ball will bounce out on impact rather than settling. With the default contact damping being fairly inelastic, a ball entering steeply at around 5 m/s should lose most of its energy rather than bouncing back over the rim, though I should account for it possibly clipping the far wall. Now I'm working out the projectile trajectory from the release point at roughly 43.7° elevation, aiming for the bucket center a few meters away.

Solving the projectile equation for launch speed gives v≈4.85 m/s, so angular velocity ω≈9.64 rad/s. Then I'm checking the descending trajectory at the target depth, computing velocity components and time of flight to verify the ball's approach angle into the hoop.

I'm verifying the ball rims into the bucket correctly, offsetting for both the rim and bottom thickness so landing lands around x≈3.08. The peak height stays low enough to clear the catapult frame.

Now I'm working out the arm's mass properties for the motor torque calculation, defining the box geometry and setting mass attributes for the arm, cup, and ball to compute the moment of inertia about the hinge.

Adding up wall inertia contributions...

Total I comes out to about 0.0632 for the arm, cup, and ball system combined, with the ball's own spin negligible since it moves rigidly with the arm. Now I need to work out the gravitational potential energy change as the arm rotates from 0 to 40 degrees, since the arm's center of mass rises by roughly 0.275·sin(40°).

I'm computing the height gain for each component: the arm contributes mgh = 0.3·9.81·0.1768 ≈ 0.52 J, the cup walls (centered around x=-0.5, z=0.045) rise by about 0.311 m giving 0.244 J of work, and now I'm working out the ball's rise using its position at (-0.5, 0.055) with the rotation formula.

So total gravitational work comes to about 0.916 J. Adding the kinetic energy at ω=9.642 (≈2.938 J) gives total work of 3.854 J, and dividing by the 40° (0.698 rad) swing gives a torque of about 5.52 N·m. But I'm second-guessing when release actually occurs — whether the joint limit constraint kicks in exactly at 40° with no damping or friction, and how MuJoCo's soft limit ramps up force once the angle exceeds that threshold.

I'm estimating the overshoot from the limit's time constant (~0.005s) against the arm's angular velocity, giving roughly 3° of overshoot — small enough that the motor's added energy during this window is negligible. I'm also checking whether the ball stays seated in the cup initially, since the arm rests against the lower limit and the motor torque engages right at t=0 to lift it, and whether the ball could fling out prematurely due to the arm's tangential acceleration early in the swing.

I'm computing the numbers: tangential acceleration from net torque over inertia comes out to ~64 rad/s², giving tip acceleration of ~32 m/s², which presses the ball against the arm surface — good, it stays seated. Centripetal acceleration reaches ~46 m/s² against the outer wall, plus gravity, so the ball remains held throughout the swing. Now I'm thinking through what happens right as the arm stops: the ball keeps moving in a straight line tangent to its circular path, which means its distance from the hinge increases over time, so I need to check whether the outer wall is positioned correctly relative to this trajectory as it separates.

The velocity perpendicular to that radius vector has a slight positive local-x component, meaning it moves toward the hinge and away from the outer wall—so it departs cleanly rather than digging in further. The residual spring penetration from centripetal loading would give a tiny inward velocity too, but that's negligible compared to the main motion.

I also need to check the catapult's static frame: the base, uprights, and hinge axle shouldn't collide with the arm itself. Since the arm starts right at its joint limit and the axle cylinder overlaps the arm body near the hinge, I should set the axle to not collide with the arm geoms to avoid spurious contact forces.

I'm working out the stop-bar placement by computing its position relative to the hinge using the rotated normal vector, then checking it against the ball's launch trajectory from the arm tip to make sure the geometry doesn't interfere with the shot.

I'll keep the bar as contype 0 so it's purely decorative, letting the joint limit handle the actual stop while the bar stands in visually for the crossbar. Now I'm moving on to defining the bucket body at position (3,0,0), setting up its static cylindrical bottom and starting on the walls.

Writing wall geometry loop...

At 3.24 giving margin 0.17 long side and 0.12 short side. Speed sensitivity is concerning—roughly 1.18m range change per m/s, meaning a 2% velocity error could shift landing by over a decimeter, and with energy accuracy around 4% that's risky. I'm considering just widening the bucket to a 0.35m inner radius to buy more margin, since MuJoCo will compute exact inertias from the geoms anyway.

The joint limit behavior matters too: contact softness causes the ball to lag slightly behind the arm, but stored spring energy is minor. Release happens right as the arm decelerates past 40°, with the ball's velocity matching the arm's angular velocity at separation—overall accuracy should land around 2%, which feels workable.

I'm also checking the geometry: no damping or armature in the joint, friction is default, and the arm's center-of-mass offset aligns with the hinge axis correctly. Working through the box inertia calculation for the arm about the hinge to confirm the moment of inertia value.

Now I'm adding up the cup's wall inertias (outer, inner, and side walls) using parallel-axis contributions, then combining with the ball's inertia to get the total system moment of inertia.

Computing kinetic energy from the total inertia and angular velocity, adding the gravitational potential term, and dividing by the angle to get torque of about 5.52. Then I catch a geometry issue — the side walls as placed would just touch the ball's surface rather than clearing it, so I need to adjust wall positions outward slightly to keep proper clearance, checking that both the side walls and the outer/inner walls leave the ball just touching rather than overlapping.

Recomputing the inertia with the adjusted inner wall gives a slightly smaller moment, so total I comes to about 0.0631 and KE around 2.933. I find the cup's center of mass x-position, then compute the height drop and corresponding gravitational work, totaling the energy contributions from all three gravity terms.

Summing everything gives total energy 3.8473, so torque works out to τ=5.511, which I'll round to 5.51. I also want to verify the ball-arm contact geometry is correct at the start—ball bottom touching arm top face exactly at z=0.015—and need to think through how to order qpos entries in the MuJoCo keyframe given the body hierarchy, since I may be able to omit the ball's qpos if it defaults to qpos0.

Setting the key with just a ctrl value avoids ordering headaches since qpos falls back to the default which already includes the ball's position. For the motor actuator I'm configuring gear ratio and control range, and noting the arm will keep pushing against its joint limit indefinitely once it hits the stop—need to set the hinge joint's range and limiting behavior, keeping in mind the compiler's default angle units are degrees.

With timestep at 0.002, a solref of 0.005 should be fine since it's at least double the timestep. I'm checking the ball won't collide with the arm again after release since the arm springs back to 40° with critical damping and no bounce while the ball moves away. For the ball settling in the bucket, I'm estimating contact penetration given the ball's impact velocity of 5.8 m/s against the default solver softness, roughly a few centimeters of penetration which seems within tolerance.

Though given the bucket's thin bottom (0.02) relative to that penetration depth, the ball could tunnel through it — I'm thinking through whether the sphere-cylinder contact geometry holds up, and considering stiffening the contact by setting a tighter solref directly on the ball and bucket geoms, or alternatively thickening the bucket's bottom to avoid tunneling entirely.

I should set solref=0.005 on both ball and bucket geoms since MuJoCo mixes them via weighted average, giving a stiffer but still reasonable combined value for arm contacts. With damping ratio 1, bounce should be minimal, so the ball should settle into the bucket rather than bouncing off the walls.

After the normal speed is killed on impact, the spin can persist and friction with the floor converts that spin back into motion toward the wall, so the ball keeps pressing in and settling slowly. I'm considering adding rolling and torsional friction coefficients to the ball's contact properties (something like friction="1 0.005 0.001" with condim 6) so it naturally damps out instead of spinning indefinitely.

Now I'm working out the geometry for the catapult frame: positioning the base box, ball start location, arm pivot height, uprights at x=0.5 with their box dimensions, and the axle cylinder running along y that needs its orientation rotated since cylinders default to the z-axis.

Everything stays non-colliding (contype 0) since these are visual-only supports. I'm computing the crossbar stop position relative to the hinge, converting to world coordinates, and adding support posts running from the base up to the crossbar at y=±0.12.

Now I'm working out the bucket wall geometry — twelve box segments arranged radially at 30° intervals, figuring out the chord widths at the inner and outer radii so each segment fits cleanly into the ring.

Continuing around the circle to fill in the remaining angles and their euler rotations, landing roughly at the expected bucket position near x=2.72. I check that gravity torque at the starting angle (about 1.44) stays well under the motor's available torque (5.51), confirming the mechanism can lift off, then I estimate the average angular acceleration toward release at around 68.

I work out release timing (about 0.14s to reach the release angle, plus 0.8s flight and a 5s settle), then verify the release position in world coordinates by converting the computed radius-angle and elevation into Cartesian terms, getting roughly (0.1522, 0.6634) with elevation about 43.72° — consistent with my earlier estimate. I note that soft-contact effects (ball penetration spring rebound) on release speed are negligible, and I start considering whether the joint limit might overshoot.

For naming, I decide to use "catapult_arm" as the body name and "catapult_arm_beam" as its geom, keeping the catapult_ prefix convention, and plan to phrase the expected event as "catapult_arm reaches its upper stop" alongside the ball coming to rest in the bucket.

