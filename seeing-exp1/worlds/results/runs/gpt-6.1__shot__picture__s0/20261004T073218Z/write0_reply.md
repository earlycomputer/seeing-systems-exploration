The regulation-size ball starts touching the floor and crosses the hoop’s center on its descending arc about 1.33 seconds after launch.

```xml
<mujoco model="basketball_shot">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="RK4"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="court_light" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <camera name="shot_view" pos="2 -11 6" xyaxes="1 0 0 0 0.341743 0.939793"/>

    <geom name="floor" type="plane" pos="0 0 0" size="10 7 0.1" rgba="0.64 0.43 0.25 1" friction="0.7 0.01 0.001"/>

    <!-- Radius 0.12 m gives a regulation circumference of approximately 0.754 m. -->
    <body name="ball" pos="0 0 0.12">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.12" mass="0.624" rgba="0.92 0.28 0.035 1" friction="0.8 0.01 0.001"/>
    </body>

    <!-- Rim center is 4 m horizontally from launch and 3.05 m above the floor. -->
    <body name="hoop" pos="4 0 3.05">
      <!-- The 32 capsule segments provide a minimum clear diameter of 0.4572 m. -->
      <geom name="rim_00" type="capsule" fromto="0.238750 0 0 0.234162 0.046578 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_01" type="capsule" fromto="0.234162 0.046578 0 0.220576 0.091366 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_02" type="capsule" fromto="0.220576 0.091366 0 0.198513 0.132642 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_03" type="capsule" fromto="0.198513 0.132642 0 0.168822 0.168822 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_04" type="capsule" fromto="0.168822 0.168822 0 0.132642 0.198513 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_05" type="capsule" fromto="0.132642 0.198513 0 0.091366 0.220576 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_06" type="capsule" fromto="0.091366 0.220576 0 0.046578 0.234162 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_07" type="capsule" fromto="0.046578 0.234162 0 0 0.238750 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_08" type="capsule" fromto="0 0.238750 0 -0.046578 0.234162 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_09" type="capsule" fromto="-0.046578 0.234162 0 -0.091366 0.220576 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_10" type="capsule" fromto="-0.091366 0.220576 0 -0.132642 0.198513 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_11" type="capsule" fromto="-0.132642 0.198513 0 -0.168822 0.168822 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_12" type="capsule" fromto="-0.168822 0.168822 0 -0.198513 0.132642 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_13" type="capsule" fromto="-0.198513 0.132642 0 -0.220576 0.091366 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_14" type="capsule" fromto="-0.220576 0.091366 0 -0.234162 0.046578 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_15" type="capsule" fromto="-0.234162 0.046578 0 -0.238750 0 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_16" type="capsule" fromto="-0.238750 0 0 -0.234162 -0.046578 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_17" type="capsule" fromto="-0.234162 -0.046578 0 -0.220576 -0.091366 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_18" type="capsule" fromto="-0.220576 -0.091366 0 -0.198513 -0.132642 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_19" type="capsule" fromto="-0.198513 -0.132642 0 -0.168822 -0.168822 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_20" type="capsule" fromto="-0.168822 -0.168822 0 -0.132642 -0.198513 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_21" type="capsule" fromto="-0.132642 -0.198513 0 -0.091366 -0.220576 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_22" type="capsule" fromto="-0.091366 -0.220576 0 -0.046578 -0.234162 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_23" type="capsule" fromto="-0.046578 -0.234162 0 0 -0.238750 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_24" type="capsule" fromto="0 -0.238750 0 0.046578 -0.234162 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_25" type="capsule" fromto="0.046578 -0.234162 0 0.091366 -0.220576 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_26" type="capsule" fromto="0.091366 -0.220576 0 0.132642 -0.198513 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_27" type="capsule" fromto="0.132642 -0.198513 0 0.168822 -0.168822 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_28" type="capsule" fromto="0.168822 -0.168822 0 0.198513 -0.132642 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_29" type="capsule" fromto="0.198513 -0.132642 0 0.220576 -0.091366 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_30" type="capsule" fromto="0.220576 -0.091366 0 0.234162 -0.046578 0" size="0.009" rgba="0.9 0.18 0.025 1"/>
      <geom name="rim_31" type="capsule" fromto="0.234162 -0.046578 0 0.238750 0 0" size="0.009" rgba="0.9 0.18 0.025 1"/>

      <!-- Backboard front is 0.381 m behind the rim center. -->
      <geom name="backboard" type="box" pos="0.3935 0 0.375" size="0.0125 0.9 0.525" rgba="0.82 0.89 0.95 0.45"/>
      <geom name="rim_mount" type="box" pos="0.31 0 -0.015" size="0.071 0.055 0.018" rgba="0.9 0.18 0.025 1"/>
      <geom name="mount_plate" type="box" pos="0.373 0 -0.015" size="0.008 0.09 0.075" rgba="0.22 0.24 0.27 1"/>

      <!-- Offset support leaves the ball's exit path unobstructed. -->
      <geom name="support_post" type="box" pos="0.70 1.05 -1.325" size="0.055 0.055 1.725" rgba="0.22 0.24 0.27 1"/>
      <geom name="support_arm" type="capsule" fromto="0.406 0.80 0.40 0.70 1.05 0.40" size="0.045" rgba="0.22 0.24 0.27 1"/>
    </body>
  </worldbody>

  <!-- At t = 4/3 s: x = 4 m, z = 3.05 m, and vertical velocity = -4.3425 m/s. -->
  <keyframe>
    <key name="start" time="0" qpos="0 0 0.12 1 0 0 0" qvel="3 0 8.7375 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Calculating basketball specifications**

I’m working through some calculations for a basketball hoop. The corrected centerline radius comes out to about .23875, with specific measurements at the midpoints and vertices. I wonder if using a 32-reg could work; it needs to fit visually for the capsule hoop.

I'm considering a 48 measurement that might help with coordinate precision. Additionally, I need to determine the backboard dimensions and location associated with the standard hoop to make everything fit properly. It’s quite the puzzle!

**Evaluating camera setup**

I'm working on the camera position and settings for a scene. I need to ensure that the camera is oriented correctly toward the center, focusing on the right axes. The camera position is at (2, -10, 5.8), aiming at (2, 0, 2.16), aligning with the y-axis. I also have to visualize the floor and the basketball setup effectively, ensuring no visual seams for the ball and using static elements for the hoop. The configurations need to be precise for a good overall scene.