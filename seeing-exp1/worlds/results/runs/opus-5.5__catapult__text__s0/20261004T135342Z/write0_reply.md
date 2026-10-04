The catapult arm is driven by a velocity motor set from the keyframe. A joint limit stops the arm at 45°, and the ball leaves the cup at about 5.25 m/s. It should come down at rim height over the centre of an octagonal bucket 3 m from the pivot. These numbers are hand-calculated from the ballistics and the geometry; I haven't run the simulation.

- **Release point:** pivot height 0.5 m, ball 0.86 m out along the arm, released at 45°. The ball leaves from about (−0.52, 0, 1.11).
- **Launch speed:** the motor holds the arm at ω ≈ 6.55 rad/s, plus a small allowance for gravity. That gives a velocity of about (3.98, 3.43) m/s.
- **Landing:** after about 0.88 s the ball reaches the rim height of 0.3 m at x ≈ 3.0. The bucket's inner radius is 0.25 m, so the range can be off by about ±0.2 m and the ball still lands inside.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="1.5 -2 5" dir="0 0.3 -1" diffuse="0.9 0.9 0.9"/>
    <geom name="floor" type="plane" pos="1.5 0 0" size="10 10 0.1" rgba="0.75 0.8 0.75 1"/>

    <!-- Catapult frame (static) -->
    <geom name="catapult_base" type="box" pos="0 0 0.02" size="0.3 0.18 0.02" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.095 0.27" size="0.04 0.02 0.23" rgba="0.5 0.33 0.17 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.095 0.27" size="0.04 0.02 0.23" rgba="0.5 0.33 0.17 1"/>

    <!-- Throwing arm: at q=0 it points backward (-x), horizontal; positive q lifts the cup -->
    <body name="catapult_arm" pos="0 0 0.5">
      <joint name="arm_hinge" type="hinge" axis="0 1 0" range="-5 45" armature="0.001"/>
      <geom name="catapult_hub" type="cylinder" fromto="0 -0.07 0 0 0.07 0" size="0.03" mass="0.1" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_beam" type="box" pos="-0.4 0 0" size="0.45 0.025 0.02" mass="0.4" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.851 0 0.05" size="0.01 0.04 0.03" mass="0.02" rgba="0.4 0.25 0.1 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.749 0 0.035" size="0.01 0.04 0.015" mass="0.02" rgba="0.4 0.25 0.1 1"/>
    </body>

    <!-- Ball, resting in the cup -->
    <body name="ball" pos="-0.8 0 0.56">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.85 0.1 0.1 1"/>
    </body>

    <!-- Bucket: octagonal wall, inner apothem 0.25 m, rim at 0.3 m, centred 3 m from the catapult pivot -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.27 0.01" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_0" type="box" pos="0.26 0 0.15" euler="0 0 0" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_1" type="box" pos="0.1838 0.1838 0.15" euler="0 0 45" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_2" type="box" pos="0 0.26 0.15" euler="0 0 90" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_3" type="box" pos="-0.1838 0.1838 0.15" euler="0 0 135" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_4" type="box" pos="-0.26 0 0.15" euler="0 0 180" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_5" type="box" pos="-0.1838 -0.1838 0.15" euler="0 0 225" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_6" type="box" pos="0 -0.26 0.15" euler="0 0 270" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_7" type="box" pos="0.1838 -0.1838 0.15" euler="0 0 315" size="0.01 0.115 0.15" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="arm_hinge" kv="100" ctrlrange="0 10" forcerange="-30 30"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  -0.8 0 0.56 1 0 0 0" qvel="0  0 0 0 0 0 0" ctrl="6.57"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that can launch a ball into a bucket 3 meters away, and it has to actually function correctly in simulation. I'm thinking through a setup with a hinged arm on a base, driven by a spring or motor, with a cup holding the ball that releases it once the arm hits a rotational stop.

Since tuning the exact landing spot is tricky without running the simulation, I'm leaning toward using a velocity actuator with high gain so the arm swings at a controlled angular velocity, then gets stopped abruptly by a joint limit -- the ball releases with velocity tangential to the arm's motion at that stop angle. I'm working out the geometry: pivot point, arm rotating in the x-z plane starting pointing backward, swinging through to release around 135°, which gives a clean 45° launch angle for the ball -- ideal for maximizing range toward the bucket.

The ball needs to stay seated in the cup through the whole swing, held by centrifugal force pressing it against the cup's outer face as the arm rotates upward, then fly free in a 45° direction once the arm hits its stop and halts abruptly.

Once the arm stops, the centripetal force vanishes so lip contact should become negligible, and gravity adds a radial component during the swing too. Maybe it's simpler to just drive the arm with a constant angular velocity actuator and work out the required speed from the geometry — pivot height, arm radius, ball offset — to hit the target bucket.

I'm setting up the body-frame rotation about the hinge axis, working through the sign conventions for how the arm orientation maps onto world coordinates so the ball's velocity vector at release comes out right.

Computing the cross product gives velocity ŷ × p = (z, 0, −x), confirming the arm tip moves forward-and-up at 45° at release. Then I factor in the ball's offset d from the arm axis, finding its rotated position and velocity components scale with (L+d) and (L−d), slightly tilting the launch angle above 45° depending on that offset.

I'm picking concrete numbers: arm length L=0.8, offset d=0.06 (ball radius 0.04, arm half-thickness 0.02), pivot height H=0.5. Computing the release position gives roughly (−0.52, 1.11) with velocity components vx=0.608ω and vz=0.523ω, then placing the bucket at 3m from the pivot to set up the trajectory calculation.

I solve for the angular velocity needed to land the ball at the bucket's rim height of 0.3m, working through the projectile equations for horizontal distance (3.52m) and vertical drop (0.808m), arriving at ω²≈42.9, so ω≈6.55 rad/s.

That gives a release speed around 5.25 m/s, which seems physically reasonable. But I'm now questioning whether the arm can actually reach that angular velocity within the 45° rotation before hitting the joint limit — the velocity actuator should ramp up quickly given high gain, but I need to think through how the arm's inertia and the ball's initial impulse interact, plus whether the joint limit (with its default soft stiffness) will hold cleanly once the arm reaches the stop.

I'm working through the separation dynamics: since the ball sits on the leading face of the arm (the arm pushes it from below as it rotates upward), once the arm begins decelerating at the limit, the ball should separate at essentially the arm's velocity right before deceleration starts, since the arm face moves away from the ball rather than continuing to push it. I should limit the actuator's force range to keep the limit penetration modest and avoid unrealistic overshoot.

Actually since velocity is perpendicular to the radial direction, the projection along the arm stays constant while the radial distance grows — so the ball just slides along the lip face rather than pushing into it, meaning near-zero normal force during this phase. Making the lip short, just enough to clear the ball's radius with a bit of margin, should avoid any penetration issues.

Now I'm checking the ball's initial resting position: at q=0 with the arm horizontal, gravity presses the ball down onto the arm's top surface, and I'm computing the keyframe coordinates so the ball sits just above that surface without penetrating it, using the arm length, cup depth, and ball radius. I also need to confirm the arm stays at rest at q=0 initially rather than being immediately driven by the actuator, which means checking the joint range and initial control values in the keyframe.

For the launch actuator, I'm using a velocity actuator on the hinge with a gain term, setting the control target and estimating the arm's rotational inertia (treating it as a rod plus the ball's point mass) to gauge how quickly it reaches the target angular velocity given the chosen gain, since a small time constant means the arm snaps to speed almost instantly.

That torque is way too extreme — it'd slam into the ball with enormous acceleration and likely cause the contact to penetrate unrealistically given the default softness settings. I should cap the actuator's force range to something more reasonable, like ±30 Nm, to keep the launch physically plausible.

Checking the numbers: with a capped acceleration around 100 rad/s², reaching the target velocity takes about 0.065s and only sweeps 12° of arm rotation, well within the 45° limit. Ball acceleration comes out to roughly 8g, giving modest penetration into the soft contact, which seems acceptable, though the ball's velocity will lag slightly behind the arm's rotation before release.

I also want to check the velocity actuator's steady-state error from gravity torque on the arm and ball — the gain seems high enough that the resulting velocity error is only around 1-2%, which should be negligible for the throw.

Increasing kv to around 200 with a force cap near 30 would cut that error down further, to under half a percent, which barely affects the throw range. I'll also widen the bucket's inner radius a bit to tolerate any residual error, and keep the rim and walls modest in size. The key variable that actually determines the throw is the arm's velocity at the instant of release, since that's what the ball inherits.

Checking the actuator stability: with kv=200, dt=0.002, and the arm's inertia around 0.3, the damping ratio comes out stable but a little oscillatory under explicit integration, so I should switch to the implicitfast integrator to be safe, and maybe dial kv back to 100 instead. I also want to lighten the arm itself to reduce the gravity torque error, so I'll shrink the arm box a bit.

Setting the arm mass to about 0.5 kg centered near -0.4 gives a gravity torque near 2 Nm, and the ball adds roughly 0.8 Nm, so total error with kv=100 comes out to about 0.4% — acceptable, though I could pre-compensate with a feedforward control term around 6.58. I'm also working through the inertia calculation for the acceleration phase to make sure the 30 Nm force range is sufficient, figuring out the arm box geometry more precisely.

Computing moment of inertia about the pivot gives roughly 0.2 total, so with 30 Nm available the angular acceleration is about 150 rad/s², which reaches target angular velocity in about 0.045s over a 0.15 rad swing — that's fine. I'm also checking what happens when the arm hits its joint limit at 45° while still moving fast, confirming the actuator just saturates against the stop without causing instability.

Flight time for the ball from release to bucket works out to about 0.885s. The arm likely overshoots a few degrees past 45° before bouncing back off the limit, but since the ball has already left the cup by then along the tangential direction, this shouldn't interfere with its trajectory.

Checking gravity's effect post-release: the ball moves outward quickly at ~5 m/s while the arm settles at 45°, so there's no risk of it falling back onto the arm. I also need to verify the arm doesn't collide with the base during its swing — checking post placement relative to arm width, and confirming the arm and base bodies won't generate spurious contacts given the hinge setup.

Since the arm is a child of the world body, I recall that MuJoCo's parent-child contact filter doesn't exclude world-child pairs by default, so I still need enough geometric separation between arm and base geoms to avoid unwanted collisions. The joint range alone should handle the stopping point rather than relying on geometry, and I'll double check the floor clearance at the arm's horizontal rest position before placing the ball initial position.

Now I'm working out where to place the outer lip so the ball sits stable at q=0 and gets pushed outward by centripetal force during acceleration, sizing the lip box dimensions relative to the ball radius and arm top height.

I'm reconsidering whether an inner lip is even necessary — since centripetal acceleration (ω²L≈34 m/s²) dominates over gravity's tangential component during the swing, the ball should stay pressed against the outer lip throughout, so maybe I can skip the inner lip and just rely on friction to hold the ball at rest initially.

Actually I'll keep a small inner lip for clarity with a 1mm gap: ball center at x=−0.80, outer lip face at −0.841, inner lip face at −0.759, each lip 0.01 half-width. I'm double-checking that the ball's initial resting height (0.56) matches the arm top (0.52) so contact is exact, and noting that any rolling/spin from friction won't matter since there's no Magnus effect in flight — now I need to recheck the release velocity calculation.

Using the actual offset d=0.06 and arm length L=0.80 from before, with minor sinkage from contact softness being negligible, I'm now checking whether the ball clears the near rim of the bucket at x=3.0 (width giving a rim at x=2.75). Computing the descending trajectory's slope near landing (vz≈−5.26, vx≈3.98, slope≈−1.32), I find that at x=2.75 the ball's height would be about z≈0.63, well above the rim, so it clears fine before landing at z=0.3 at x=3.0.

The ball continues past center into the far side (x=3.25) while descending through the rim height, giving roughly ±0.2 m margin horizontally for the 0.04 radius ball against the 0.25 bucket radius — solid tolerance. I'm also considering whether the vertical impact speed (~5 m/s) against the bucket bottom might cause bouncing out, given MuJoCo's default near-inelastic contact behavior.

For the bucket itself, I'm sketching an octagonal approximation using 8 wall boxes instead of a true cylinder — computing wall placement at radius 0.26 with half-thickness 0.01, half-length ~0.115 to cover the octagon segments, and walls spanning roughly z=0.02 to 0.32 so the rim sits near 0.3.

I'm making the bucket a static body positioned at (3,0,0), with a flush bottom disk and no self-collision concerns since it's one rigid structure. Now computing the exact angular positions and rotated box coordinates for each of the eight wall segments using 45° increments.

Then I'm moving on to the catapult frame — placing vertical support posts on either side of the pivot axis down to the floor, and setting up an axle cylinder to run through the pivot point.

I'm checking the arm's hub cylinder and post geometry to confirm there's no overlap, then adding a base platform box sized to support the frame. I decide to skip adding a decorative crossbar stop near the 45° position since it risks colliding with the arm's swept path, and conclude no front stop is needed either.

Now I'm assigning masses to each component—arm box, hub, lips, and ball—and working out the arm's moment of inertia from its dimensions.

Estimating total inertia around 0.18, then checking gravity torque at q=0 (about 2.67 Nm) versus at 45° (around 1.9 Nm), accounting for the arm, lips, and ball contributions. I'm also checking the velocity error under the kv=100 gain, giving a control output near 6.57, and now wondering whether the actuator fully reaches steady state before hitting the 45° mark during its acceleration phase.

Setting up the hinge joint with its range and damping settings, then defining the velocity actuator with its gain, control range, and force limits. Now I'm building the keyframe with the control value and figuring out the full qpos vector size for the hinge plus free joint.

For body ordering, the ball needs its own body placed after the catapult arm since the free joint must sit at the top level, giving qpos as the hinge angle followed by the ball's position and quaternion. Double-checking the starting hinge angle of zero falls within the allowed range, and verifying the rotation math confirms that increasing the hinge angle correctly rotates the arm end upward.

Confirming that positive control to the velocity actuator produces positive hinge velocity and lift, matching MuJoCo's right-hand convention. I'm also checking clearances — the ball's radius keeps it clear of the support posts, and tracing its trajectory through the pivot point shows plenty of height margin, with the arm overshooting safely into its upper limit after launch.

Now I'm recomputing the release velocity components from the angular speed (~6.55 rad/s), getting roughly vx=3.98 and vz=3.43, then solving the projectile equation for when the ball center drops to z=0.3, finding t≈0.885s and working out the corresponding horizontal distance traveled.

Checking whether the arm's joint limit catches exactly at 45° matters: since the arm only rotates slightly further during deceleration, the launch angle shifts by maybe 1°, which barely changes the range given we're near the 45° optimum. I'm also confirming that the ball's contact softness against the arm during the swing doesn't meaningfully affect the steady-state velocity before release.

Friction-induced rolling at release doesn't matter here, and I've confirmed the ball stays pressed against the outer lip during the swing due to centripetal acceleration. Now I'm setting up the scene visuals—adding lighting, materials using rgba colors, and a floor plane sized and positioned appropriately. I'll write the XML with degree-based angles, a 0.002 timestep, and the implicitfast integrator.

