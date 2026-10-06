The pendulum starts raised about 50° and swings down under gravity, knocking the ball toward +x. The ball rolls 0.5 m, climbs a shallow ramp, and drops over the low front wall of a box-shaped cup centred at x = 1 m. The cup's other walls are taller to catch it, and its base has rolling friction so the ball settles.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <asset>
    <material name="floormat" rgba="0.8 0.8 0.75 1"/>
    <material name="wood" rgba="0.6 0.45 0.3 1"/>
    <material name="metal" rgba="0.5 0.5 0.6 1"/>
    <material name="red" rgba="0.85 0.15 0.1 1"/>
    <material name="cupmat" rgba="0.2 0.4 0.8 1"/>
  </asset>
  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" material="floormat" friction="1 0.005 0.0001"/>

    <body name="stand" pos="-0.051 0 0">
      <geom name="stand_post1" type="box" size="0.01 0.01 0.215" pos="0 0.12 0.215" material="wood" contype="0" conaffinity="0"/>
      <geom name="stand_post2" type="box" size="0.01 0.01 0.215" pos="0 -0.12 0.215" material="wood" contype="0" conaffinity="0"/>
      <geom name="stand_bar" type="cylinder" size="0.006 0.13" pos="0 0 0.43" euler="90 0 0" material="metal" contype="0" conaffinity="0"/>
    </body>

    <body name="pendulum" pos="-0.051 0 0.43">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0" damping="0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.375" size="0.008" mass="0.05" material="metal"/>
      <geom name="pendulum_bob" type="sphere" size="0.025" pos="0 0 -0.4" mass="0.5" material="metal"/>
    </body>

    <body name="ball" pos="0 0 0.025">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.025" mass="0.06" material="red" friction="1 0.005 0.0001"/>
    </body>

    <body name="ramp" pos="0.7216 0 0.0226">
      <geom name="ramp" type="box" size="0.2026 0.06 0.01" axisangle="0 1 0 -9.23" material="wood"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" size="0.08 0.08 0.003" pos="0 0 0.003" material="cupmat" condim="6" friction="1 0.02 0.005"/>
      <geom name="cup_front" type="box" size="0.005 0.08 0.03" pos="-0.075 0 0.03" material="cupmat"/>
      <geom name="cup_back" type="box" size="0.005 0.08 0.06" pos="0.075 0 0.06" material="cupmat"/>
      <geom name="cup_left" type="box" size="0.07 0.005 0.06" pos="0 0.075 0.06" material="cupmat"/>
      <geom name="cup_right" type="box" size="0.07 0.005 0.06" pos="0 -0.075 0.06" material="cupmat"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.88 0 0 0.025 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches ramp
ball touches cup_base
ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the physics setup: a ball at the origin, a cup target slightly to the right, and a pendulum hinged above that swings down to strike the ball forward, starting from a raised horizontal position.

Now I'm wrestling with how the ball actually gets into the cup — a rolling ball can't climb over a rim easily, so I'm considering either a low-walled cup it can hop over with enough speed, or a ramp leading up into an open-topped enclosure whose interior floor matches the ground plane.

I need to balance the entrance wall/ramp height against the exit wall height so the ball enters with enough speed to clear the threshold but gets trapped bouncing off the taller far wall, with vertical interior walls preventing it from climbing back out. Settling on an enclosed box-shaped cup design with a ramp entrance seems safest to guarantee containment.

Since ramp and floor are both static bodies, their geometries won't register collisions with each other, so slight penetration at the low edge is harmless. I'll make the ramp its own separate static body rather than attaching it to the cup, with its top surface cresting right at the wall's top edge so the ball rolls up and over into the interior.

I'm estimating the ball's trajectory after it leaves the ramp: with a small gap raised above the wall to avoid snagging, the ball falls roughly 0.045m while traveling horizontally, landing it near the center of the 0.14m-wide interior cavity — comfortably within bounds even accounting for speed variation that might send it closer to the far wall before it settles.

Since the wall at 0.04m isn't quite tall enough to contain the ball's full radius, I'm bumping wall height to 0.06 and ramp top to 0.065, recalculating the ramp angle at that steeper rise over a 0.4m run. I'm working out the minimum rolling speed needed to climb that height (~0.95 m/s) and factoring in energy loss from the ball transitioning from sliding to rolling after impact, aiming for an arrival speed near 1.3 m/s at the ramp base.

Now I'm tracing the projectile path off the ramp crest—checking fall time and horizontal distance to see where the ball lands, and whether it clears or clips the far wall—while also setting bounds on launch speed so the ball neither stalls on the incline nor flies clean over the containing wall on the far side.

I'll raise just the side and back walls to 0.12, keeping symmetry in the lateral direction fine. For settling, the ball should bounce between walls and gradually dissipate energy through MuJoCo's default contact damping, though I might need to add rolling friction on the cup base to help it settle within the time limit.

I'm thinking of giving the cup a thin base plate (0.005 height) so the ball lands and rolls on it, with condim 6 and a small rolling friction coefficient around 0.0005. Running the numbers, this gives a rolling resistance deceleration of roughly 0.14 m/s² over a 0.6 m path, losing about 0.17 in v²—acceptable but adds some complexity to the model.

So I'll give the ball default condim 3 (no rolling friction on floor) and make the cup base condim 6 with strong friction, so only contact with the cup base applies rolling resistance (~1.4 m/s² decel), while floor and ramp stay condim 3. For the ball's mass, I'm estimating a solid sphere of radius 0.025 at density 1000 gives about 0.065 kg, so I'll just specify 0.06 kg. Now I'm working out the pendulum setup — hinge position, bob sphere radius 0.03 at the end of an arm, with the bob center height matched to the ball's resting height for a clean impact.

I realize the bob could penetrate the floor at the bottom of its swing, so I'm adjusting the bob's radius and center height to keep clearance above the floor while still striking the ball slightly off-center — I'm leaning toward bob radius 0.025 with center at z=0.03, giving 0.005 clearance and a contact direction angled down onto the ball's center at z=0.025.

Now I'm positioning the pendulum so the bob just touches the ball at the bottom of its arc: setting bob center x to roughly -0.051 for a small gap, placing the hinge above at height 0.03+L, and working out the impact speed using energy conservation from the release angle to get v = sqrt(2gL(1-cosθ0)) before setting up the collision equations.

With MuJoCo's contact model being fairly inelastic (critically damped spring-damper behavior), I'm reasoning that the restitution coefficient should be close to zero, meaning the ball and pendulum move together momentarily, sharing momentum roughly as M·v/(M+m). Since the bob mass is much larger than the ball, the ball picks up nearly the full pendulum velocity, which then transitions from sliding to rolling at 5/7 of that speed once friction takes over.

I'm trying to estimate a reasonable pendulum bob velocity accounting for the uncertainty in ball rolling speed, settling on something around 1.7 m/s so the resulting rolling range lands near my target of ~1.4.

Now I'm checking whether the pendulum could strike the ball a second time after the initial hit — tracking the ball moving away at ~1.3 m/s while the pendulum swings forward and back, and making sure its maximum excursion doesn't reach far enough to hit the ball again or collide with the ramp at x=0.52.

I'm picking L=0.4m and computing the required swing angle from energy conservation, getting θ0≈50.8° for a point-mass approximation, then refining using a physical pendulum model that accounts for the arm's moment of inertia and the bob's mass to get a more accurate torque and height relationship.

Running through the torque-balance equation, I solve for 1-cos(θ0)≈0.3625, giving θ0≈50.4° (0.88 rad). Checking the max horizontal excursion at this angle confirms it stays well within bounds, though I note the pendulum will lose energy to the ball after impact and swing less afterward.

Now I'm working out the rotation convention: with the hinge axis along +y, a positive θ rotation swings the bob toward -x, so setting the initial qpos to +0.88 with axis "0 1 0" means gravity will swing it through the bottom toward +x as intended.

I'm checking geometry for overlaps — the arm capsule and bob sphere stay within the same body so their contact is fine, and I verify the arm's bottom tip doesn't collide with the ball since they're offset in x. I also confirm there's no unwanted contact between the pendulum and the floor or world body, and I'm considering whether to add a static support post for visual framing.

I'm adding a simple static stand with a crossbar and two posts flanking the pendulum's swing, setting contype and conaffinity to 0 so it doesn't physically interact with anything. Then I'm setting up the ball's initial position and working out the keyframe qpos ordering, making sure the pendulum hinge joint comes before the ball's free joint in the model definition.

Now I'm computing the ramp geometry — figuring its length, slope angle, and box half-sizes, then finding the center position by offsetting down from the top surface along the ramp's normal vector so the box sits flush with the slope.

I'm working out the correct y-axis rotation (negative of the slope angle) so the box's local x-axis points up the incline, setting the euler angle to roughly -9.23 degrees, and checking the ramp's width fits within the cup's inner span. I'm also checking how the top end of the ramp's surface meets the front wall, since the box's end face extends slightly past x=0.92 and may overlap the wall there.

At the low end, I'm verifying the ramp surface meets the floor cleanly at x=0.52 without creating a protruding lip, since the box's bottom corner there dips slightly below floor level, which is fine. I'm also thinking about whether a ball rolling onto the 9° incline loses energy at the slope transition due to the corner impact, and trying to estimate that small velocity loss.

Now I'm checking the crest behavior: with speed 0.88 there, the ball likely leaves the surface since its speed exceeds the centripetal threshold at that curvature, so it goes into flight rather than staying in contact. I'm confirming it clears the front wall during this transition, then tracking where it lands relative to the base plate's top surface.

I'm computing fall time and horizontal travel during flight, factoring gravity and the small upward velocity component from the incline angle. This gives a landing point comfortably inside the target zone, before the back wall, so a faster roll speed is safely contained.

I also want to flag the failure case: if the rolling speed is too low, below roughly 0.95, the ball would just roll back down toward the pendulum instead of clearing the crest, so I should aim for a target speed around 1.35 to have margin, and I still need to account for friction losses along the way.

Checking MuJoCo's rolling behavior with condim 3 confirms it's nearly lossless, so a ball moving around 1.3 m/s covers the 0.52 m gap in about 0.4 seconds. Now I'm working out the cup's geometry — placing the base, front wall, and back wall boxes with specific sizes and offsets so the walls bound the correct x-range and height.

Side walls get positioned to define the interior region (roughly x 0.93–1.07, y ±0.07), and I set the base's friction so rolling and torsional resistance are strong enough to settle the ball by around six seconds, landing it in the cup. I'm now moving on to think through the pendulum setup.

Working through the collision dynamics more carefully: with soft contact (timeconst 0.02) the pendulum bob and ball reach a near-common velocity around 1.52 m/s, but since the ball decelerates quickly under μ=1 friction while the pendulum near the bottom of its swing loses speed much more slowly, the pendulum actually catches back up and keeps pushing the ball forward rather than separating cleanly.

Checking the trajectory to the back wall: ball center height stays around 0.09, safely under the 0.12 back wall, so it's contained. Bouncing back toward the front wall is trickier since that wall's inner face is only 0.06 tall, and the ball center at 0.09 might clear it entirely—I need to reconsider that geometry, though MuJoCo's non-elastic default collision with a critically damped response should keep the rebound small enough to stay safe. I'm also confirming the ramp half-width and setting up the floor plane dimensions.

Now I'm setting the success expectations: the pendulum needs to touch the ball, the ball needs to touch the ramp, and the ball needs to come to rest in the cup, possibly checking contact with the cup base specifically.

