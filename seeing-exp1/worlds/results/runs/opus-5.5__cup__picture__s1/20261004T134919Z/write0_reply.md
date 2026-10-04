The ball starts at rest near the top of a 10° static ramp. The low end of the ramp overhangs the open top of a flat-bottomed box cup on the floor, so the ball rolls off the edge and drops into the cup. The walls stop it, and rolling friction brings it to rest. I worked out the launch, landing point and settling by hand and haven't run the simulation.

```xml
<mujoco model="ball_ramp_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="ramp_mat" rgba="0.55 0.35 0.2 1"/>
    <material name="cup_mat" rgba="0.2 0.4 0.8 1"/>
    <material name="ball_mat" rgba="0.9 0.15 0.15 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 2" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" pos="0 0 0" material="floor_mat"/>

    <!-- Static ramp: 10 deg slope, top surface low edge at (0, 0, 0.115) -->
    <geom name="ramp_board" type="box" size="0.2 0.06 0.01" pos="-0.1987 0 0.1399" euler="0 10 0" material="ramp_mat" friction="1 0.005 0.001"/>
    <geom name="ramp_support_high" type="box" size="0.02 0.05 0.08" pos="-0.37 0 0.08" material="ramp_mat"/>
    <geom name="ramp_support_low" type="box" size="0.01 0.05 0.0525" pos="-0.06 0 0.0525" material="ramp_mat"/>

    <!-- Cup: open box, inner floor at z=0.01, rim at z=0.10, inner x from 0.015 to 0.315 -->
    <body name="cup" pos="0.165 0 0">
      <geom name="cup_base" type="box" size="0.16 0.16 0.005" pos="0 0 0.005" material="cup_mat"/>
      <geom name="cup_wall_near" type="box" size="0.005 0.16 0.045" pos="-0.155 0 0.055" material="cup_mat"/>
      <geom name="cup_wall_far" type="box" size="0.005 0.16 0.045" pos="0.155 0 0.055" material="cup_mat"/>
      <geom name="cup_wall_left" type="box" size="0.15 0.005 0.045" pos="0 0.155 0.055" material="cup_mat"/>
      <geom name="cup_wall_right" type="box" size="0.15 0.005 0.045" pos="0 -0.155 0.055" material="cup_mat"/>
    </body>

    <!-- Ball resting on the ramp near its upper end -->
    <body name="ball" pos="-0.3395 0 0.2053">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" material="ball_mat" condim="6" friction="1 0.005 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.3395 0 0.2053 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the scene layout — a tilted ramp with a ball rolling down and dropping into a cup. I need the ramp to end right above the cup opening so the ball falls in directly, since a ball rolling on the floor couldn't climb over raised cup walls.

Running the physics: with a 15° incline, rolling-without-slipping acceleration works out to about 1.81 m/s², giving an exit speed around 1.48 m/s after 0.6m of travel. That's actually too fast for a clean drop into the cup, so I'm reconsidering a shorter ramp or shallower angle to slow the ball enough that it lands inside rather than overshooting.

I'm working out the drop trajectory after the ball leaves the ramp: release point around rim height, falling roughly 0.10 m to settle in the cup base, giving a fall time near 0.13 s and horizontal travel of about 0.108 m. That tells me the cup's interior needs to span at least around 0.2 m between near and far walls for the ball to land properly inside.

Given MuJoCo's default contact damping, the ball will lose most of its bounce on impact but retain spin, which should let it roll and climb the walls slightly before settling — I expect it to stabilize within the 6-second window with some added rolling friction.

I should also keep the cup floor flat rather than concave, confirm the wall height (0.1) is enough to prevent the ball from hopping over after impact, and make sure the ramp (a thin static box) ends just before the near wall without colliding with the cup geometry.

Now I'm working out the ramp's exact placement: at a 10° incline, the lower edge needs to sit at a position where the ball's center clears the near wall (ball bottom at 0.115 vs wall top at 0.10) so it rolls forward into the cup rather than catching on the wall edge.

Checking the ball's landing speed in the cup confirms it's a soft inelastic landing. Now I'm computing the ramp box geometry, placing its center by moving back along the slope direction from the edge point and offsetting by half-thickness along the surface normal.

I orient the box using a y-axis rotation so its face angles down the slope, then I'm placing the ball's starting contact point further up the ramp (around 0.35 along the slope from the edge) and setting the ball's center by offsetting from that contact point by the ball's radius along the normal.

I'm estimating that with a drop of 0.35m the ball reaches around 0.92 m/s, giving a landing point roughly 0.11-0.12 m past the edge, which seems reasonable without needing side rails since there's no lateral force. I should add support geometry under the ramp's upper end so it's physically held up, and set the initial keyframe with the ball's position and zero velocity.

That support position checks out too, positioned close to the cup's near wall with reasonable clearance. For physics, the ball with default density gives a sensible mass, the cup is static as intended, and the friction parameters (including a small rolling friction coefficient) should only cause gentle deceleration in a rolling ball.

I decide on 0.001 for rolling friction and 0.005 for torsional friction, balancing ramp motion decay against expected cup collision losses. I'll stick with the default Euler integrator and move on to finalizing the file with lights and floor setup.

