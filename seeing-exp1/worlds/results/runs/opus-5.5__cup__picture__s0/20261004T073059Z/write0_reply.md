The ball starts at rest near the top of a 10° ramp. It rolls off the low end, clears the near wall of an open-topped box cup and drops in. A little rolling friction on the cup's floor and walls then brings it to rest well within the 6 s run.

```xml
<mujoco model="ball_ramp_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="ramp_mat" rgba="0.55 0.4 0.25 1"/>
    <material name="cup_mat" rgba="0.2 0.4 0.8 1"/>
    <material name="ball_mat" rgba="0.9 0.2 0.2 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 2" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" material="floor_mat"/>

    <!-- Ramp: tilted 10 deg, descending toward +x; low top edge at (0.21, 0.125) -->
    <geom name="ramp_deck" type="box" size="0.2 0.06 0.01" pos="0.0113 0 0.1499" euler="0 10 0" material="ramp_mat"/>
    <geom name="ramp_post_high" type="box" size="0.01 0.01 0.085" pos="-0.17 0 0.085" material="ramp_mat"/>
    <geom name="ramp_post_low" type="box" size="0.01 0.01 0.062" pos="0.1 0 0.062" material="ramp_mat"/>

    <!-- Cup: open-top box, inner floor at z=0.01, inner x from 0.2 to 0.4, walls up to z=0.1 -->
    <body name="cup" pos="0.3 0 0">
      <geom name="cup_base" type="box" size="0.11 0.11 0.005" pos="0 0 0.005" condim="6" friction="1 0.01 0.005" material="cup_mat"/>
      <geom name="cup_wall_near" type="box" size="0.005 0.11 0.045" pos="-0.105 0 0.055" condim="6" friction="1 0.01 0.005" material="cup_mat"/>
      <geom name="cup_wall_far" type="box" size="0.005 0.11 0.045" pos="0.105 0 0.055" condim="6" friction="1 0.01 0.005" material="cup_mat"/>
      <geom name="cup_wall_left" type="box" size="0.1 0.005 0.045" pos="0 0.105 0.055" condim="6" friction="1 0.01 0.005" material="cup_mat"/>
      <geom name="cup_wall_right" type="box" size="0.1 0.005 0.045" pos="0 -0.105 0.055" condim="6" friction="1 0.01 0.005" material="cup_mat"/>
    </body>

    <!-- Ball -->
    <body name="ball" pos="-0.1304 0 0.211">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.025" mass="0.05" material="ball_mat"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.1304 0 0.211 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning the scene layout: a tilted ramp box for the ball to roll down, landing at the bottom where a cup made from a flat base and surrounding walls catches it so it settles within 6 seconds.

I'm running through the physics of a sphere rolling down an incline to check its exit velocity, testing different ramp angles and lengths (like 20° and 10°) to see what speed the ball hits the cup at, since too much speed risks it bouncing out rather than coming to rest.

I could instead restrict rolling friction to just the cup base contact by using combined contact parameters — setting a high condim and rolling friction coefficient only on the cup floor geom, letting the ramp stay default, so the ball decelerates only once it reaches the cup. I'm working out the deceleration math from the rolling friction coefficient to make sure it settles the ball without over-damping on the ramp.

Now I'm sketching concrete geometry: a ball of radius 0.025, a tilted box ramp with set half-dimensions rotated 15° about y so it descends in the +x direction, checking the rotation convention to make sure the slope actually points the right way toward the cup.

I'm working out the cup dimensions next — base thickness, inner wall height and width sized to the ball's diameter — then positioning the ramp's lower end so it exits just above the cup's rim height, roughly at z≈0.09, so the ball clears the wall before dropping in.

Then I'm calculating the ball's launch speed off the ramp: using the slope angle and travel distance to get acceleration and exit velocity components, then estimating the fall time from the ramp's exit height down to the cup floor to check the trajectory lands inside.

Looking at the cup geometry, 0.11 m of horizontal travel seems tight against a 0.16 m inner width, so the ball would hit the far wall at around 1 m/s — with MuJoCo's default contact damping giving minimal bounce but still some rebound before friction settles it. I'm deciding to reduce the ramp angle to 10° and shorten the travel distance to about 0.25 m, which brings the exit speed down to roughly 0.78 m/s, a gentler and more realistic "rolling down a ramp" motion.

I'm now working out the actual coordinates: a 10° ramp with specific box dimensions, computing the surface normal and axis direction from the rotation, and placing the low edge of the ramp relative to a larger cup (half-width 0.1, wall height 0.08) centered at the origin.

I want the ramp's low end positioned so the ball clears the wall top at z=0.1, checking the bottom corner of the ramp end stays just above the wall rim while the top edge sits around (0.21, 0, 0.125) to drop the ball into the cup interior without colliding with the wall.

Now I'm calculating the ball's center position: it exits at the top edge of the ramp, offset by the normal vector times its radius, giving center roughly (0.0113, 0.1499), with the ramp's high end at about (-0.1839, 0.1945). I'll define the ball's starting center as a point offset distance s from the high end along the ramp's top surface, shifted outward by the radius along the normal.

Tracking the ball past the exit point, it falls roughly 0.1146m to reach the cup floor, landing around x=0.339, comfortably inside the inner wall at 0.4. It keeps moving at about 0.9 m/s, hits the far wall, and likely bounces back somewhat before rolling friction settles it.

Estimating rolling friction deceleration on the ramp, the ball should slow and stop within about 0.6 seconds, hitting the far wall with low remaining speed, so everything settles by roughly 2 seconds total. Default ramp friction (coefficient 1, condim 3) is well above what's needed for rolling without slipping at that incline, so the ball should roll cleanly rather than skid.

I'm applying matching friction and condim settings to the cup walls, setting ball mass via density (around 0.065 kg at radius 0.025, or explicitly via a mass attribute), and defining the initial keyframe so the ball starts at rest atop the ramp with its freejoint position matching the ramp's top surface height at that x-coordinate.

I'm also checking the ramp's incline geometry to confirm the ball sits exactly on the surface with a small clearance gap, then adding support posts beneath the high end of the ramp for visual realism, positioning a small box from the floor up to the ramp's underside based on the computed top and bottom heights at that location.

Since static geoms in the worldbody don't collide with each other, I don't need to worry about the post intersecting the ramp or ball path—placing it near x=0.1 keeps it clear of both the cup and the ball's landing zone. Now I'm setting up the cup as a static body with separate named wall and base geoms, then finishing with floor plane sizing and lighting before writing out the full scene.

