The catapult arm is driven by a torque-limited velocity motor. It spins up to a set speed and then hits a stiff hinge stop. At that moment the ball leaves the cup at about 45° and 4.95 m/s, which should carry it into a bucket whose centre is 3 m downrange of the ball's start (x = −0.5 → x = 2.5).

The speed was chosen with a hand ballistics calculation, and I have not simulated the file. The motor's speed-tracking error is estimated, so the throw distance may need a small adjustment of `ctrl` after the first run.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <geom name="catapult_base" type="box" pos="0 0 0.03" size="0.3 0.15 0.03" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.07 0.215" size="0.02 0.012 0.185" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.07 0.215" size="0.02 0.012 0.185" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0 -0.09 0.4 0 0.09 0.4" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 38.16" solreflimit="0.004 1"/>
      <geom name="catapult_arm_beam" type="box" pos="-0.27 0 0" size="0.28 0.025 0.02" mass="0.6" solref="0.004 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.5455 0 0.05" size="0.005 0.04 0.03" mass="0.02" solref="0.004 1" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.435 0 0.03" size="0.005 0.04 0.01" mass="0.01" solref="0.004 1" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="ball" pos="-0.5 0 0.46">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.004 1" condim="6" friction="0.8 0.01 0.005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="bucket" pos="2.5 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.23 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.21 0 0.17" size="0.01 0.06 0.15" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.18187 0.105 0.17" size="0.01 0.06 0.15" euler="0 0 30" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0.105 0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 60" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="0 0.21 0.17" size="0.01 0.06 0.15" euler="0 0 90" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.105 0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 120" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.18187 0.105 0.17" size="0.01 0.06 0.15" euler="0 0 150" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="-0.21 0 0.17" size="0.01 0.06 0.15" euler="0 0 180" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="-0.18187 -0.105 0.17" size="0.01 0.06 0.15" euler="0 0 210" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall8" type="box" pos="-0.105 -0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 240" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall9" type="box" pos="0 -0.21 0.17" size="0.01 0.06 0.15" euler="0 0 270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall10" type="box" pos="0.105 -0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 300" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall11" type="box" pos="0.18187 -0.105 0.17" size="0.01 0.06 0.15" euler="0 0 330" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="20" forcelimited="true" forcerange="-25 25"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.5 0 0.46 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="9.92"/>
  </keyframe>
</mujoco>
```

```expect
ball touches catapult_arm_beam
ball touches bucket_bottom
ball comes to rest in bucket
```

---
thinking (summarized):

I'm thinking through the physics of a catapult that launches a ball 3 meters horizontally into a bucket, considering options like a hinged arm driven by a spring or actuator, with the ball starting at rest and the arm possibly given an initial angular velocity via a keyframe.

I'm leaning toward a design where a spring torque accelerates the arm from rest, which then hits a hard stop at an angle giving a 45-degree launch direction — the ball's velocity equals the cup's tangential speed at that stop, so I need to calculate the required angular velocity to achieve a 3 m range from that launch angle.

Instead, I'm considering a velocity actuator driving the arm to a target angular speed against the joint limit, but I need to make sure the cup geometry holds the ball against centrifugal force during acceleration before it's flung off at the stop — working through the pivot-and-cup geometry to figure out exactly how the arm's orientation translates to the ball's release direction.

Computing the position derivative, I find that stopping the arm at 45° gives a launch velocity split evenly between horizontal and vertical components, which is the ideal 45° trajectory for maximum range. The cup just needs an outer lip at the arm's tip to contain the ball against centrifugal force until release, so I'm picturing a simple floor-plus-wall design for that.

Working out the hinge axis, I determine that rotating about the +y axis by angle φ moves the arm end from pointing along -x upward correctly, so the joint should use axis 0 1 0 with a range of 0 to 45 degrees. I'm now considering that MuJoCo's joint limit acts as a soft constraint, meaning the arm will decelerate rather than stop instantly, so the ball's momentum carrying it forward after the limit is hit needs more thought, especially with a velocity actuator still driving the arm.

The ball should launch cleanly since at the moment of release its velocity points along the cup floor's normal direction, perpendicular to the arm, so the inner and outer walls (aligned with the arm) won't obstruct its exit. For launch speed, I'm setting up v = ω·r_ball where r_ball accounts for the ball center being offset above the arm surface by some height d, giving arm-frame coordinates (-L, d) for computing the precise launch velocity direction.

I'm now considering whether to drive the arm with a velocity actuator that ramps up to ω quickly, versus just setting the arm's initial qvel directly via a keyframe so the ball starts at rest in the cup and gets launched impulsively as the cup floor pushes it—though that risks a rough contact transition.

I'm also weighing whether to set qvel directly for the arm via keyframe while keeping the ball at rest, but sticking with a velocity actuator is simpler. Estimating the arm's moment of inertia (~0.08 kg·m² for a rod plus cup) to pick a reasonable kv gain so the response time constant is fast without being unstable at the default timestep, since MuJoCo's integrator handles actuator damping somewhat implicitly.

Switching to the implicitfast integrator lets me use a kv around 20 for a ~4ms time constant, so now I'm working out the geometry: placing the pivot, sizing the arm length, and figuring out where the ball starts and where it launches at 45° so I can compute the horizontal distance to the bucket and the resulting trajectory height needed to land it.

I'm sketching the physical setup more concretely now — a pivot at a fixed height, an arm box of a given length and thickness, and a small cup at the arm's end sized to hold the ball, with wall placement still to work out.

I'm working out the launch angle: with α the ball's offset angle from the arm axis (~6.84°), the velocity direction relates to θ=φ+α, and elevation above horizontal equals 90°-θ since the velocity is tangential to the rotation, perpendicular to the radius vector.

But I realize the cup floor normal differs from the pure tangential direction by α, so when the arm stops the ball retains a velocity with a small inward component (~v·sinα) toward the pivot, along with the main outward/upward component. This means the ball must rise about 0.06 to clear the inner wall (wall top at 0.08, floor at 0.02) while also drifting slightly inward during that rise — I need to check whether this inward drift causes it to clip the wall.

Computing the drift gives about 0.0072, against a wall-ball gap of 0.005, so there's a slight scrape — I should lower the inner wall or widen the gap. Then I reconsider whether the inner wall is even necessary: during acceleration, centrifugal force dominates and pushes the ball outward against the outer wall, while gravity's component along the arm is comparatively small, so the inner wall's role is mostly to contain the ball during deceleration rather than acceleration.

I'll shorten the inner wall (top at z=0.04, centered around 0.03) and reposition it near x=-0.44, with the outer wall at x=-0.55 reaching up to 0.08. I also check that during deceleration the ball moves away from the outer wall rather than into it, which confirms no interference. Side walls seem unnecessary since there's no y-direction motion, so I decide to skip them to keep the setup simple. Finally I start working out the arm's stopping angle so the final elevation comes out to 45 degrees.

Aiming to land just above the rim at x=2.5, z=0.35, I compute the horizontal distance and height drop from launch, then plug into the projectile range equation for 45° to solve for the required launch speed v, getting 80.02/v² plus the D·tanθ term equal to the needed Δz.

I find v≈4.95 m/s, giving angular velocity ω≈9.835 rad/s for the arm. Now I'm checking whether a velocity-controlled actuator with gain kv can reach this speed quickly enough over the 38° swing — the time constant τ=I/kv needs to be small, so I'm considering making the arm lighter, maybe around 0.3 kg, to reduce inertia and allow faster spin-up.

Trying a ball mass around 0.1 kg, I estimate combined inertia near 0.055, so with kv=50 the time constant is about 0.0011 s, which should keep the spin-up angle error negligible (~0.011 rad). Checking the steady-state error from gravity torque, I get roughly 1.5 N·m, which translates to about a 0.3% speed error — small enough to barely affect the launch range.

Now I'm worried the initial torque of kv*ω (~490 N·m) could create unrealistic acceleration on the ball, pushing it from 0 to 5 m/s in about a millisecond, which implies a contact force around 500 N on a 0.1 kg ball. I'm thinking through whether MuJoCo's soft contacts can handle that force without the ball penetrating the cup floor — estimating equilibrium penetration depth based on the default solref timeconst of 0.02 and working out the implied contact stiffness and natural frequency.

I'm calculating that penetration could reach around 2 meters at this acceleration, which is clearly unacceptable — the ball would pass right through the cup floor. The real problem is the instantaneous spin-up torque, not the steady-state centripetal motion. I'm considering fixes: limiting actuator force via forcerange so angular acceleration is bounded, smoothing the spin-up with a spring-like ramp, or stiffening the contact solref between ball and cup to handle the higher forces.

So I need to figure out a reasonable angular acceleration — limiting spin-up to happen over about 0.3 rad gives roughly 161 rad/s², producing a tangential acceleration around 81 m/s² and a final centripetal value of 48 m/s², both tolerable with a stiffer solref producing only millimeter-scale penetration. Then I need to make sure the velocity actuator transitions smoothly from force-limited acceleration to the clamped feedback control once it approaches target angular velocity.

Now I'm sketching the arm and cup geometry — sizing the arm box, placing it relative to the pivot, and assigning masses to the arm and the inner/outer cup walls so the overall inertia and torque requirements stay consistent with the spin-up budget.

Adding ball's contribution, total moment of inertia ≈0.063. Checking gravity torque against applied torque: with forcerange ±15N, net angular acceleration ≈216 rad/s², giving spin-up angle ≈0.224 rad for the swing — that looks good.

Tangential acceleration at ball comes out to roughly 109 m/s², which seems fine. I'm deciding joint damping isn't necessary since kv already handles steady-state error, and the small gravity-induced droop (~0.25% velocity error) is acceptable without extra compensation. I'm checking whether implicitfast integration properly accounts for the actuator's velocity derivative when the force output is clamped by forcerange limits.

I'm not fully certain whether MuJoCo skips the derivative when force is clamped, so to sidestep the risk entirely I'll just pick a smaller, safer gain: checking the explicit Euler stability bound gives kv < 63, so using kv=20 keeps things well-damped without oscillation, leaving a steady-state error of about 0.0625 rad/s that I can compensate for in the control signal.

A velocity actuator is clearly the better choice over a constant-torque motor hitting a joint limit, since the motor's stopping speed would depend messily on energy balance with gravity, whereas the velocity actuator gives a clean time constant of about 0.0032s for the approach phase. I'm now thinking through how the ball's inertia loads the arm through contact during spin-up, and how at steady angular velocity the ball gets pressed outward against the wall by centrifugal force while gravity acts normal to the floor.

I'm working through the joint limit mechanics at the 38.16° stop — with default soft solref timeconst of 0.02s and the arm hitting at ω≈9.8 rad/s, the overshoot could be roughly 0.2 rad, which is substantial. That means the ball wouldn't release at a single clean angle but rather over a range as the arm decelerates gradually, so I need to figure out exactly when the ball separates from the cup during that deceleration.

I'm reasoning that separation happens once the deceleration-induced tangential force exceeds the gravity component holding the ball against the floor, which with soft limits would occur very early in the limit engagement. To get a cleaner release angle, I should stiffen the limit (solreflimit around 0.004, 1), cutting overshoot down to roughly 0.04 rad, and I'm also checking that the ball's contact with the outer wall during centrifugal pressing doesn't complicate the separation moment.

I'm thinking through the catapult's static frame — base, posts holding the axle, and making sure the arm's geometry clears the posts without colliding, while the joint limit at φ=0 holds against gravity pulling the arm down before the actuator fires.

Simplest fix: set contype/conaffinity to 0 on the static frame geoms (base, posts) so they're visual-only and never collide, since the ball won't touch the frame anyway, while the arm keeps default collision properties against the floor.

Now I'm placing a non-colliding pivot axle cylinder between the posts at the pivot height, then designing the bucket body at the far end — a thin bottom cylinder plus a ring of boxes forming the walls.

I'm checking the ball's trajectory: entering at roughly 52° with horizontal speed ~3.5 m/s, it falls through the 0.3m wall height and lands inside, striking the far wall around x≈2.66 near the bucket floor, confirming the geometry captures the ball properly.

With default damping settings the bounce should stay fairly contained rather than launching the ball back out. I need to think about solref mixing between ball and cup geoms — since MuJoCo averages solref parameters by default, a stiff ball value combined with a softer cup value would produce an intermediate contact stiffness, so I should set matching solref values on the cup geoms too to keep behavior predictable.

I'm also wondering if the ball might keep rolling slowly around the bucket floor after landing, since there's no rolling friction by default. Adding condim 6 with a small rolling friction coefficient on the ball should let it settle within a few seconds rather than drifting indefinitely.

For the bucket geometry, I'm settling on a 12-sided ring of boxes for the walls — inner radius 0.2, wall thickness 0.02, height 0.3 — computing each segment's center position and half-width based on the chord length at that radius.

Writing the 12 box definitions, each rotated by its segment angle, with the whole bucket placed as a static body at (2.5,0,0) welded to the world.

For the launch, if the ball starts at x=-0.5 relative to a pivot at zero, the bucket at x=2.5 gives roughly 3 meters of horizontal travel. Recomputing the trajectory with a target height around z=0.3 (near the bucket rim), I get Δz=-0.456, leading to v²≈24.16 and v≈4.915, ω≈9.76. The bucket's inner radius minus the ball radius gives about ±0.16 m of landing tolerance, so I'm checking how sensitive the range is to small velocity errors.

I'm also considering timing effects during deceleration — since the ball likely separates from the arm early due to tangential deceleration exceeding gravity's component, launch angle errors should stay small. One tricky detail: the ball may drift outward against the arm's outer wall during spin-up due to centrifugal force, so I should place it resting against that wall from the start so its initial position is well-defined.

I'll set the outer wall's inner face just slightly beyond the ball's resting position (around -0.5405), with the ball starting at -0.5 — nearly touching, with negligible slack of about 0.0005, which is fine since friction with the floor handles the spin-up phase anyway. I'm also double-checking that this wall placement stays within the arm's outer boundary at -0.55, which it does.

Estimating contact penetration under the centrifugal and gravity loads, I get roughly 1.4 mm at steady speed and up to 1.7 mm during the tangential acceleration of spin-up — both acceptable given the solver's stiffness parameters. I'm now thinking through the actuator's steady-state compensation for gravity torque on the arm at a swing angle of about 30 degrees.

Working out the moment arm and torque balance, I get about 1.18 N·m resisting torque, giving a velocity error of roughly 0.059 rad/s with the chosen gain, which seems small enough not to matter. Checking the settling transient after spin-up saturates, the velocity loop time constant is about 3.2 ms, so it settles within about 0.05 rad of angle, comfortably inside the total travel budget.

I'll set the control target around 9.82 and define the velocity actuator with kv=20 and a force limit of ±15 N·m, keeping ctrllimited off since it's not needed. For the ball mass, I'm just setting it directly to 0.1 kg rather than deriving density, since that's simpler and sufficiently accurate.

Checking stability with Euler integration: with kv=20 and arm inertia alone, the discrete response ratio h·kv/I comes out to about 1.06, which risks oscillatory overshoot, though contact coupling with the ball likely brings this down near 0.63. To be safe I'll lower kv to 15, which gives a ratio of about 0.79 for the arm alone and keeps the steady-state error around 0.079 rad/s — a more comfortable margin for stability.

Trying another approach: bumping arm mass to 0.6 kg raises its inertia to about 0.068, dropping the ratio to 0.59 even with kv=20. That does increase gravity torque demand to roughly 1.84, pushing steady-state error to about 0.092 rad/s, but checking torque capacity against a forcerange of 25 still leaves plenty of angular acceleration headroom (~245 rad/s²), so arm mass 0.6, kv=20, forcerange 25 looks like a workable configuration, giving ball tangential acceleration near 123 m/s². I want to recompute the gravity torque more precisely at the average swing angle during the constant-speed phase, roughly 0.4 to 0.66 rad.

At release angle 38°, recalculating each component's torque contribution — arm, outer wall, inner wall, and ball — gives a total gravity torque of about 1.72 N·m, with the dynamic lag from changing gravity torque being small enough to ignore. Dividing by kv=20 gives a steady-state error of about 0.086 rad/s, corresponding to a control signal around 9.

Small penetration effects (the ball sitting slightly outward into the wall, or slightly into the floor) shift the radius by a fraction of a percent, which I'll neglect as negligible. Checking the launch geometry, the release elevation angle works out to 45° as intended, with only a few millimeters of overshoot into the soft limit, which seems acceptable given the actuator torque limit of 25 N·m.

I'm also checking that the ball doesn't clip the inner wall of the cup during release — tracing through the tangential and inward displacement components shows there's still about 3cm of clearance, so it clears fine. No rebound of the arm occurs since the limit damping ratio is set to 1, so the motion stays clean after the stop.

Now I'm working out the ball's spin, roughly 9.8 rad/s about the y-axis, carried into flight since MuJoCo doesn't model Magnus effects — that spin will just slightly affect the landing. For the keyframe, I need to set the initial qpos correctly: the hinge angle first, then the ball's freejoint position and orientation, with the ball starting at rest on the arm at the correct height based on the pivot and arm length, along with the initial control value for the actuator.

Checking the geometry: ball height 0.46 lines up with the arm's top surface at 0.42 plus the ball radius 0.04, confirming contact at rest. I'm also setting up the visual floor, catapult frame geoms, and lighting for the scene.

For the trajectory check, I'm recomputing the release point and velocity at the 45° launch angle, getting position (-0.356, 0.756) and velocity components around 3.48 m/s each in x and z, then solving for the time to reach x=2.5m and the corresponding height at that point using the kinematic equations.

I'm verifying the ball clears the rim by checking its height at the inner rim position (x=2.30) and confirming it's well above the 0.32 rim height, then solving a quadratic to find exactly when the ball descends to the rim height of 0.36m to confirm safe clearance through the hoop.

Working out the solution gives x≈2.45m, which falls nicely within the bucket's 2.3-2.7m span. There's reasonable slack in the landing position (roughly ±0.15m) which translates to a velocity tolerance of about -1.9% to +3.5%, so I'm considering aiming slightly further to center the shot better at x=2.5.

Bumping v up by 0.8% gives ω=9.84, control≈9.92. Checking the far-wall scenario: entering at 2.5 at a steep descent angle, the ball should hit around x=2.66 at a height of ~0.15, which stays inside the bucket before bouncing with low restitution — that looks fine. Now I need to think about what happens to the ball's velocity relative to the cup right after it separates, once the arm stops moving.

The ball should stay pressed against the floor and outer wall as centrifugal force pushes it outward during spin-up, and the arm's top surface at release looks fine too. Now I'm writing the MuJoCo XML for the frame geometry — defining the base box, support posts, and the axle cylinder with appropriate positions and orientations...

Still writing the arm and bucket geometry...

I'm checking the outer and inner ring spacing confirms no overlap issues, then sizing the bottom cylinder and estimating where the ball rests at z=0.06. Now I'm thinking through which success conditions to write—likely "ball touches bucket_bottom" and "ball comes to rest in bucket"—and considering whether to reference the catapult_arm geom by name as well.

For the ball itself, I'm defining its sphere geometry with mass, solref, and friction values, settling on condim 6 with small torsional and rolling friction coefficients.

