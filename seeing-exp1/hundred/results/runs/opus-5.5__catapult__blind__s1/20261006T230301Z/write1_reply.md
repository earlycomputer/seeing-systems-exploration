The chain runs along x to the weight drop, then turns 90°. The seesaw pivots about the x axis so it throws the ball along +y into a wide floor-standing cup. Because of this layout, where the weight lands along x does not change the seesaw's lever arm. I have not run this file; the figures below are hand estimates.

- **Pendulum:** the bob starts 0.6 m above its lowest point, reaches about 3.4 m/s and hits a 1.5 kg cart on a slide joint.
- **Cart:** it pushes a 1 kg block about 8 cm off the end of a table, then stops at its joint limit.
- **Weight:** the block falls about 0.19 m into a walled tray on the raised end of the seesaw.
- **Seesaw:** it swings from its 35° limit to its 15° lower limit. When it stops, the ball is thrown from a lipped holder at an estimated 2.3 m/s, about 10° off vertical.
- **Ball:** it should land in the cup, which tolerates launch speeds from roughly 1.6 to 3.2 m/s. Rolling friction on the ball then brings it to rest well before 6 s.

```xml
<mujoco model="pendulum_cart_seesaw_cup">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 0.3 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="pend_post" type="cylinder" fromto="0 -0.25 0 0 -0.25 1.45" size="0.02" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="pend_crossbar" type="cylinder" fromto="0 -0.25 1.41 0 -0.03 1.41" size="0.015" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="table_top" type="box" pos="0.248 0 0.63" size="0.128 0.1 0.02" friction="0.4 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    <geom name="table_leg" type="box" pos="0.14 0 0.305" size="0.015 0.08 0.305" contype="0" conaffinity="0" rgba="0.6 0.4 0.2 1"/>
    <geom name="seesaw_post_a" type="box" pos="0.396 0.16 0.165" size="0.015 0.015 0.165" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="seesaw_post_b" type="box" pos="0.736 0.16 0.165" size="0.015 0.015 0.165" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="seesaw_axle" type="cylinder" fromto="0.396 0.16 0.33 0.736 0.16 0.33" size="0.008" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    <body name="pendulum" pos="0 0 1.41">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.65" size="0.012" mass="0.05" rgba="0.3 0.3 0.8 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.7" size="0.05" mass="1.0" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="cart" pos="0.156 0 0.712">
      <joint name="cart_slide" type="slide" axis="1 0 0" limited="true" range="-0.02 0.13"/>
      <geom name="cart_body" type="box" size="0.1 0.07 0.06" mass="1.5" rgba="0.9 0.5 0.1 1"/>
    </body>
    <body name="weight" pos="0.346 0 0.6905">
      <freejoint name="weight_free"/>
      <geom name="weight_block" type="box" size="0.04 0.04 0.04" mass="1.0" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.2 1"/>
    </body>
    <body name="seesaw" pos="0.566 0.16 0.33">
      <joint name="seesaw_hinge" type="hinge" axis="-1 0 0" pos="0 0 0" limited="true" range="0.2618 0.6109"/>
      <geom name="seesaw_arm" type="box" pos="0 0.05 0" size="0.05 0.37 0.01" mass="0.15" rgba="0.2 0.7 0.2 1"/>
      <geom name="seesaw_tray" type="box" pos="0 -0.21 0" size="0.13 0.11 0.01" mass="0.04" rgba="0.2 0.6 0.2 1"/>
      <geom name="seesaw_tray_inner_wall" type="box" pos="0 -0.09 0.035" size="0.13 0.008 0.025" mass="0.005" rgba="0.1 0.5 0.1 1"/>
      <geom name="seesaw_tray_side_wall" type="box" pos="0.13 -0.21 0.035" size="0.008 0.11 0.025" mass="0.005" rgba="0.1 0.5 0.1 1"/>
      <geom name="seesaw_lip" type="box" pos="0 0.415 0.03" size="0.04 0.008 0.02" mass="0.01" rgba="0.1 0.5 0.1 1"/>
    </body>
    <body name="ball" pos="0.566 0.4919 0.1415">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.025" mass="0.03" condim="6" friction="0.8 0.01 0.003" rgba="0.9 0.1 0.1 1"/>
    </body>
    <body name="cup" pos="0 0 0">
      <geom name="cup_floor" type="box" pos="0.566 0.7875 0.005" size="0.16 0.1825 0.005" rgba="0.3 0.3 0.9 1"/>
      <geom name="cup_wall_near" type="box" pos="0.566 0.61 0.06" size="0.16 0.005 0.06" rgba="0.3 0.3 0.9 1"/>
      <geom name="cup_wall_far" type="box" pos="0.566 0.965 0.06" size="0.16 0.005 0.06" rgba="0.3 0.3 0.9 1"/>
      <geom name="cup_wall_left" type="box" pos="0.411 0.7875 0.06" size="0.005 0.1825 0.06" rgba="0.3 0.3 0.9 1"/>
      <geom name="cup_wall_right" type="box" pos="0.721 0.7875 0.06" size="0.005 0.1825 0.06" rgba="0.3 0.3 0.9 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.427448 0 0.346 0 0.6905 1 0 0 0 0.610865 0.566 0.4919 0.1415 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to wrap up the design now and commit to the y-axis seesaw layout, reconfirming the fixed elements: the pendulum pivot and bob dimensions, the cart body position and mass, and the slide range, plus the table slab geometry.

Now I'm working through the seesaw hinge math: determining the sign convention for rotation about the x-axis so that positive θ correctly lowers the weight end while raising the ball end, settling on using axis "-1 0 0" to get the right behavior, and landing on a rotation range of 0.2618 to 0.6109 radians with keyframe 0.610865. I'm also laying out the seesaw body geometry in its local frame, starting with the arm box spanning from the pivot toward the ball side.

I'm now sizing the weight tray box and solving for where the pivot needs to sit vertically so the weight lands at the cart line, factoring in the tilt angle to convert local tray coordinates into world-space height, then checking the resulting landing window as the tray position shifts from the inner wall to its outer edge.

I'm checking that the weight landing position stays within the tray bounds in x, then working through the pivot height math to get a believable fall distance of about 0.2 units, tuning the start and landing z-values to match.

Now I'm setting the pivot height to 0.33 for enough clearance margin, giving a fall distance of 0.187 and a landing velocity of 1.92. Moving into the dynamics setup, I'm computing the moment of inertia contributions from the arm, tray, and ball around the pivot point to prepare for the equations of motion.

Summing these gives a total moment of inertia near 0.073. I'm then working out the impact lever arm at the 35-degree contact angle to get an initial angular velocity around 4.2 rad/s, and separately computing the gravitational torque contributions from the weight, tray, ball, and arm at the 25-degree release angle, netting out to roughly 1.85 and an angular acceleration near 25.4.

Using that acceleration over the swing angle gives a final angular velocity near 5.9 rad/s, translating to a launch speed around 2.26 m/s, which sits comfortably within the acceptable 1.6-3.2 m/s tolerance band even accounting for impact assumptions. Now I'm computing the ball's position and velocity direction at launch in world coordinates, and starting to work out the cup's position for the trajectory check.

Setting the cup with 0.12m walls on the floor, I calculate the height difference between launch and rim at about 0.145m, then run the projectile landing calculations across the velocity range: at the low end (1.6 m/s) the ball lands around 0.483m out, at the center speed (2.26 m/s) it lands near 0.571m, and I'm working through the high end (3.2 m/s) to see how far it overshoots.

Checking the cup's inner span from 0.455 to 0.80, the slowest landing point barely clears the near wall with a small margin, so that edge case needs attention. I'm also verifying the arm's swing path doesn't clip the near wall at different angles, tracing the tip position through 15° and 35° rotations to confirm clearance.

Now I'm computing the world-space box dimensions for the cup assembly: finding the center and half-extents for the floor, near wall, and far wall boxes based on the cup's position and wall thickness.

For the ball's keyframe, I'm rotating its local body offset by 35 degrees to get the world position, then checking it clears the near wall of the cup with margin to spare. Lastly I'm placing decorative seesaw support posts just outside the tray's half-width.

Now I'm verifying clearances for the falling weight against the inner wall and seesaw arm geometry at various angles, confirming the gaps stay around 0.03-0.05 units which should be safe, then moving on to check the table slab doesn't collide with the tilted tray at 15 degrees.

I'm checking the cart's slide range against the limit stop and confirming the weight's push force of 0.08 clears the cart's travel bounds, then setting up the pendulum arm as a thin capsule with a bob sphere at its end.

Now I'm defining joint limits in radians for the seesaw and cart slide, then setting the ball's physics properties (size, mass, friction) and assigning masses to the seesaw's arm, tray, and lip geoms, plus adding the floor plane and lighting.

Checking torque balance before impact reveals a problem: the tray side (0.1 mass at 0.21m) actually outweighs the ball-plus-arm side, meaning the seesaw would tip toward the tray prematurely. I need to reduce the tray mass to around 0.04 and lighten the inner wall to correct this imbalance.

Verifying the geometry overlap confirms the arm and tray share the same top height (z=0.01), so the weight lands cleanly across both. For horizontal landing position, the weight's center of mass needs to fall between roughly x=0.436 and 0.696 to stay within the tray bounds, which means a v_h range of about 0.5-1.1 should work fine.

Since the weight will keep sliding horizontally after landing (friction 0.4 giving ~3.9 deceleration, dropping from 0.8 m/s over about 0.08m), it risks sliding off the far edge if it lands past x=0.62. I'm adding a small rail/wall at the outer edge of the tray (x=0.13 in body coordinates) to stop it — a thin box with half-dimensions (0.008, 0.11, 0.025) and mass 0.005 should do the job.

Now I'm working out the keyframe qpos values for the pendulum, cart, weight, seesaw, and ball positions to set up the initial scene state.

With the weight's friction set to "0.4 0.005 0.0001" against a table friction of 0.4, and the tray's default friction of 1 ensuring the weight sticks once it lands there, the outer wall becomes mostly a safety margin rather than strictly necessary — cart friction doesn't matter here. Time to write out the full XML.

