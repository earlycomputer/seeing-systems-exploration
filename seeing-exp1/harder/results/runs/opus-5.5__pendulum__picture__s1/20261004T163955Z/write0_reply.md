The pendulum starts 50° back and hits the ball at the bottom of its swing. The ball rolls 0.8 m, climbs a short ramp (part of the cup), drops over the low front lip into a walled cup centred at x = 1 m, and is held there by a tall back wall and a high-rolling-friction base plate. I worked out the geometry and speeds by hand and have not run this file in MuJoCo, so a 6 s run is still needed to confirm the ball ends up in the cup.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0.5 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- visual support beam at the pivot (no collisions) -->
    <geom name="support_beam" type="box" pos="-0.041 0 0.523" size="0.02 0.08 0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: pivot 0.5 m above the bob's lowest point, bob just behind the ball -->
    <body name="pendulum" pos="-0.041 0 0.523">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.48" size="0.005" mass="0.02" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.02" mass="0.3" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.02">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.02" mass="0.03" friction="1 0.005 0.0001" rgba="0.1 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball's start, with an entry ramp up to its low front lip -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.13895 0 0.007968" euler="0 -12.1 0" size="0.08182 0.05 0.005" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_front_wall" type="box" pos="-0.06 0 0.015" size="0.005 0.065 0.015" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_back_wall" type="box" pos="0.06 0 0.04" size="0.005 0.07 0.04" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_left" type="box" pos="0 0.065 0.04" size="0.065 0.005 0.04" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_right" type="box" pos="0 -0.065 0.04" size="0.065 0.005 0.04" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_base" type="box" pos="0 0 0.001" size="0.055 0.06 0.001" condim="6" friction="1 0.01 0.01" rgba="0.5 0.4 0.25 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.8727 0 0 0.02 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical setup: a small ball resting on the floor, a pendulum pivot positioned to swing and strike it toward a cup placed one meter away, and I need the cup to have some kind of opening or ramp so the rolling ball can actually settle inside it.

Maybe instead a small step is too lossy energetically, so I'm considering a tilted ramp approach: a thin wedge box angled upward leading to the cup's lip, letting the ball roll up and drop into walled cup floor on the other side, using the floor itself as the cup's interior surface.

Working through the rolling energy equations, a ball needing to clear a ramp height of 0.03m would need roughly 0.65 m/s at the top, accounting for rotational kinetic energy in rolling motion. I'm now worried this speed could cause the ball to bounce off the back wall and potentially ricochet back out over the ramp lip before settling.

Since the vertical ramp wall is only 0.03m tall but the ball's diameter is 0.04m, the ball's center contacts the wall below the top edge, giving a mostly horizontal bounce rather than enough lift to climb back over — so it should stay contained. I'm also reconsidering whether the ramp needs to be a separate geom or can simply be part of the cup body as an integrated lip.

Soft default contacts in MuJoCo should keep restitution low, helping the ball settle rather than bounce excessively. I'm now sketching the cup geometry: body centered at x=1.0 with inner walls spanning roughly 0.95 to 1.05, and an entry ramp running from about x=0.80 up to x=0.95 while rising to a height of 0.03.

Working out ramp box geometry and rotation...

Computing the box center gives roughly (0.87598, 0.0101). I'm also checking whether the tilted box might clip below the floor slightly, but since both the cup's geoms and the floor are static bodies welded to the world, MuJoCo's collision filtering should skip contacts between them anyway, so this isn't a concern.

Looking at the ramp's low end near x=0.80, the ball should transition fairly seamlessly onto the top surface, with just a minor kink from the box edge. At the high end near x=0.95, though, the gap underneath the ramp (roughly 0.025 between the ramp bottom and the floor) is smaller than the ball's diameter, so the ball shouldn't be able to slip underneath there.

To solve this, I'll add a thin vertical wall box as the front of the cup, spanning roughly x=0.945 to 0.955 with a height matching the ramp's top (about 0.03), so the ramp feeds directly into this wall and the ball rolls off the edge and drops into the cup rather than sneaking underneath.

Then I'm working out the physics of the launch: using energy conservation for rolling motion to get the ball's speed at the ramp's top (~0.76 m/s from an initial 1.0 m/s), factoring in the slope angle for the velocity components, and setting up the projectile equation to find how long it takes the ball to fall from the ramp's edge into the cup.

I'm adjusting wall heights for safety margins — back wall at 0.08 to prevent the ball flying over even at higher velocities, with side walls similarly tall. I'm also checking the low end: since MuJoCo's default contact model has no rolling resistance, only slip friction during the initial strike matters for whether the ball has enough speed to cross the 0.8 m gap.

Since the ball starts with pure translation and friction converts it to rolling (final rolling velocity = 5/7 of initial), I need the post-strike velocity around 1.4-2 m/s to get a final rolling speed near 1.0 m/s. I'm also thinking through what happens after impact — since the pendulum is heavier than the ball, it continues forward slower than the ball post-collision rather than catching up and striking it again.

Since MuJoCo's soft contacts are fairly inelastic, the pendulum and ball will move together briefly before the pendulum decelerates as it rises, letting the ball continue on alone — any later pendulum swing-back happens too late to matter since the ball will be a meter away by then, so I'll just add small joint damping. For the pendulum geometry, I'm placing the pivot at a height above the strike point, with the bob needing to be positioned so it contacts the ball at the right height without the bob itself clipping into the floor, which affects where the contact normal actually hits.

I'll place the pivot at x=-0.041, z=0.523 with L=0.5, and set up the hinge rotation about y so the bob starts at a positive angle behind the ball and swings forward in +x to strike it at the bottom of its arc, confirming the rotation math works out so release at φ>0 drives motion toward φ=0.

Now I'm estimating speeds: with φ=60°, the bob hits bottom around v≈2.21 m/s. Comparing a light ball (~0.0335 kg) against a heavier bob (~0.3 kg), I'm reasoning through the range of post-collision ball speeds from perfectly inelastic (~2.0 m/s) to elastic (~4 m/s), expecting MuJoCo's soft contact to land somewhere in between, closer to inelastic.

With the default critically-damped contact parameters, restitution is essentially zero, so the ball likely leaves with speed around 2 m/s — then once it's rolling without slipping, that becomes about 1.43 m/s after the 5/7 factor.

Tracking it up the ramp, speed squared drops to about 1.62, giving roughly 1.27 m/s at the top. Projecting the flight path, I find it lands past the back wall position, hitting it mid-flight at a low height, then bounces back and settles, rebounding toward the front wall.

I worry the ball might clear the front wall on rebound since its height is close to the wall's top, so I consider lowering the launch angle to 45° instead, which recalculates the top speed to about 0.89 after losses—comfortably above the 0.65 threshold needed.

Actually keeping φ=50° seems fine too: working through the energy loss at the ramp base gives a top speed near 1.01, with the flight landing close to the back wall. I'm now thinking about whether bouncing inside the cup could eject the ball—with soft, critically damped contacts the restitution should be near zero, so it should settle rather than bounce out.

For damping out residual back-and-forth rolling, I could add a thin base plate inside the cup with higher friction/condim to act as rolling resistance, rather than adding joint damping that would slow the ball everywhere including during the shot.

I should also double check the initial keyframe doesn't put the ball in collision with the pendulum rod, which swings down from 50° — need to verify the rod's path at the bottom doesn't intersect the ball's resting position.

For the pendulum bob mass, I'll just set mass="0.3" directly rather than computing density, and keep the rod capsule thin so it doesn't visually overwhelm the scene.

I'm setting up the pivot body and hinge geometry, plus a static visual support frame with collision disabled, then defining the keyframe qpos values for the pendulum angle and ball's free joint starting position.

Checking the geometry, I confirm the bob's trajectory nearly grazes the ball's center at the bottom of the swing, with contact happening just slightly before the lowest point given the small offset. I'm now considering the ball's sliding friction transition as it moves from pure sliding to rolling after impact.

The deceleration gives a transition time of about 0.049s, which is negligible. I'm also verifying that after the collision, the pendulum swings away from the ball's path on its forward motion, so no further contact occurs, and the overall timeline (ball travels roughly 0.8m at ~1.2 m/s, about 0.7s after the strike) fits comfortably within a 6-second simulation window, with the ramp-to-floor transition geometry also checking out fine.

Computing the ramp's box length and midpoint, I get a tilt angle of about 12.1 degrees, so the box center sits near (0.861, 0.008). Now I need to position the box at the ramp's upper end around x≈0.94 for the front wall face.

Now I'm converting the cup geometry into the cup body's local frame, shifting by the body's x-offset and laying out each wall, the base plate, and the ramp with their positions and half-extents relative to that frame.

Checking clearances: the side walls overlap the front wall corners fine, and the height difference between side and front walls isn't an issue. Tracing the ball's trajectory, it should land inside the cup's x-range near the back wall, which looks correct, and I'm setting the base plate's friction and rolling resistance values to control how it settles.

I'm also considering the floor plane, pendulum support collisions (disabling contype on the visual support), hinge damping, lighting, and naming conventions for the pendulum rod and bob geoms, plus checking that rod mass doesn't skew the energy balance.

For the pivot and support beam, I'll place it at roughly (-0.041, 0, 0.523) with a non-colliding box geom for the beam. The ball's free joint starts with zero velocity so it rests naturally on the floor, and contact friction between ball and pendulum should be fine even if it induces some spin — default Euler integration works, maybe bump ball condim to 3. Now writing the final file.

