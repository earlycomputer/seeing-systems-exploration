The ball (r = 0.12 m, 0.62 kg, hollow-shell inertia) starts on the floor at x = 0. Its keyframe velocity is (2.687, 0, 9.269) m/s, so it peaks at about 4.5 m and comes down through the center of the rim (3.05 m, x = 4 m) at roughly 63° below horizontal. At that angle the opening the ball sees is about 0.41 m, compared with its 0.24 m diameter. Checked by hand only, not by running it: along the path the ball's surface stays about 9 cm clear of the rim tube, and gravity's semi-implicit integration shifts the crossing point by less than 1 cm.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <asset>
    <material name="court" rgba="0.76 0.6 0.42 1"/>
    <material name="leather" rgba="0.85 0.4 0.12 1"/>
    <material name="steel" rgba="0.9 0.3 0.1 1"/>
    <material name="glass" rgba="0.8 0.9 1 0.35"/>
    <material name="post" rgba="0.2 0.2 0.25 1"/>
  </asset>
  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="2.5 -8 2.5" xyaxes="1 0 0 0 0.25 1"/>
    <geom name="floor" type="plane" size="12 12 0.1" material="court" solref="0.01 0.3"/>

    <body name="ball" pos="0 0 0.121">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005952 0.005952 0.005952"/>
      <geom name="ball" type="sphere" size="0.12" material="leather" friction="0.8 0.01 0.001" solref="0.01 0.3"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.22854 0.06124 0" material="steel"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.22854 0.06124 0 0.20490 0.11830 0" material="steel"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.20490 0.11830 0 0.16730 0.16730 0" material="steel"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.16730 0.16730 0 0.11830 0.20490 0" material="steel"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0.11830 0.20490 0 0.06124 0.22854 0" material="steel"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="0.06124 0.22854 0 0 0.2366 0" material="steel"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="0 0.2366 0 -0.06124 0.22854 0" material="steel"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.06124 0.22854 0 -0.11830 0.20490 0" material="steel"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.11830 0.20490 0 -0.16730 0.16730 0" material="steel"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.16730 0.16730 0 -0.20490 0.11830 0" material="steel"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.20490 0.11830 0 -0.22854 0.06124 0" material="steel"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.22854 0.06124 0 -0.2366 0 0" material="steel"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.22854 -0.06124 0" material="steel"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="-0.22854 -0.06124 0 -0.20490 -0.11830 0" material="steel"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="-0.20490 -0.11830 0 -0.16730 -0.16730 0" material="steel"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="-0.16730 -0.16730 0 -0.11830 -0.20490 0" material="steel"/>
      <geom name="rim_16" type="capsule" size="0.008" fromto="-0.11830 -0.20490 0 -0.06124 -0.22854 0" material="steel"/>
      <geom name="rim_17" type="capsule" size="0.008" fromto="-0.06124 -0.22854 0 0 -0.2366 0" material="steel"/>
      <geom name="rim_18" type="capsule" size="0.008" fromto="0 -0.2366 0 0.06124 -0.22854 0" material="steel"/>
      <geom name="rim_19" type="capsule" size="0.008" fromto="0.06124 -0.22854 0 0.11830 -0.20490 0" material="steel"/>
      <geom name="rim_20" type="capsule" size="0.008" fromto="0.11830 -0.20490 0 0.16730 -0.16730 0" material="steel"/>
      <geom name="rim_21" type="capsule" size="0.008" fromto="0.16730 -0.16730 0 0.20490 -0.11830 0" material="steel"/>
      <geom name="rim_22" type="capsule" size="0.008" fromto="0.20490 -0.11830 0 0.22854 -0.06124 0" material="steel"/>
      <geom name="rim_23" type="capsule" size="0.008" fromto="0.22854 -0.06124 0 0.2366 0 0" material="steel"/>
      <geom name="bracket" type="box" pos="0.311 0 -0.012" size="0.068 0.06 0.012" material="steel"/>
    </body>

    <body name="backboard" pos="4.394 0 3.435">
      <geom name="board" type="box" size="0.015 0.915 0.535" material="glass"/>
      <geom name="arm" type="box" pos="0.81 0 -0.1" size="0.795 0.05 0.05" material="post"/>
      <geom name="pole" type="cylinder" fromto="1.606 0 -3.435 1.606 0 -0.05" size="0.1" material="post"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.121 1 0 0 0" qvel="2.687 0 9.269 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm setting up the physical parameters for a basketball shot scene—ball radius and mass, rim diameter and height—then working out the trajectory needed for the ball to launch from the floor 4 meters away and drop through the hoop.

I need the descent angle steep enough (over ~32°) so the ball's effective opening through the rim exceeds its own diameter, so I'm picking an apex height around 4.5m and calculating the launch velocity and fall times to get a roughly 50° descent angle at the hoop.

Computing the horizontal velocity, descent velocity, and angle at impact, I get about 63°, which gives plenty of clearance since the effective rim opening comfortably exceeds the ball's diameter. Since MuJoCo has no default air density, drag isn't a concern, so now I just need to verify the ball's trajectory clears the front edge of the rim as it passes through at x=4, checking the rim's front and back boundary positions.

Working out the perpendicular distance from the ball's flight path to both the front and back rim points, accounting for the tube radius, I get roughly 0.203m clearance on each side, which is well above the needed margin.

For 3D sanity, the rim is a circle so the side points sit at y=±0.2366, which is consistent. I'm also double-checking the ball's start position at z=0.12 on the floor, nudging it slightly if needed to avoid initial floor contact. I'm considering whether to add a backboard behind the hoop, noting the real-world offset of about 0.15m between rim and backboard, and tracing where the ball would land on the floor after passing through if it doesn't hit the rim.

Checking whether the ball actually reaches the backboard's position as it falls past the rim height — it doesn't, since it's already descending toward x=5.08 before it gets close to the board's x location, so it clears underneath. I need to place the support pole far enough behind (realistically over a meter back) so the ball doesn't collide with it after passing through.

Skipping the net for simplicity, I'm computing the rim geometry as a ring of 24 capsule segments at the hoop height, working out the angular coordinates at 15° increments to position each segment around the circle.

I finish computing the remaining points around the full circle of 24, completing the polygon vertices, then note the chord sagitta formula for checking how far the chord midpoint sits inside the circle.

Now I'm working out the rim-to-backboard bracket geometry, figuring where the rim's attachment point on the +x side meets the backboard face, then sizing a connecting bracket box between them with appropriate half-dimensions, while also checking ball clearance near the back of the rim.

I'm checking the ball's path at various heights to confirm it clears the bracket, then confirming the hoop body is a static child of the worldbody so the ball passes through freely. I'm sizing the backboard box's thickness, x-position, and vertical extent based on NBA rim height and board lower edge specs.

For the support arm and pole, I'm reasoning through whether the ball's post-bounce trajectory might collide with the pole given its radius and position—deciding that's actually realistic rather than a bug, and settling on placing the pole further out at x=6.0 for a longer arm.

For bounce physics, I'm considering solref parameters to give the ball a realistic basketball-like coefficient of restitution on contact with the floor, and thinking about whether to model the ball as a hollow shell for more accurate inertia.

I settle on a radius of 0.12m matching a standard basketball circumference, and work out the explicit inertial properties for the keyframe. For initial conditions I'm setting the freejoint qpos and qvel to launch the ball forward with a vertical arc, possibly adding backspin for realism.

Checking the contact setup though, if the ball starts exactly touching the floor at z=0.12, MuJoCo might register a contact at distance zero right at t=0, so I bump the starting height slightly to 0.1205 to avoid any unwanted friction kick on the first step.

Recomputing more precisely with z0=0.121 and apex 4.5, I get vz0≈9.269 and vx≈2.687 to hit the target time. I also need to account for the small discretization error from semi-implicit Euler integration — roughly g·dt·t/2 per step — which could shift the apparent apex slightly from the ideal projectile math.

The timestep error turns out to shift the landing by under a centimeter horizontally, so it's negligible and default gravity/friction settings should be fine. Now I'm thinking through scene setup details: naming every body, geom, and light, adding a camera, and defining the floor plane dimensions.

I'll skip extra court markings or launch visuals to keep things minimal, and put the backboard and pole geoms together in a static body while making sure the hoop body's origin aligns with the rim center. Time to write out the full XML.

