```xml
<mujoco model="basketball_launch">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="Euler"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
    <rgba haze="0.12 0.15 0.2 1"/>
  </visual>

  <asset>
    <material name="basketball_material" rgba="0.95 0.32 0.035 1" specular="0.15" shininess="0.1"/>
    <material name="rim_material" rgba="0.95 0.18 0.035 1" specular="0.4" shininess="0.5"/>
    <material name="board_material" rgba="0.85 0.9 0.95 1" specular="0.3" shininess="0.3"/>
    <material name="support_material" rgba="0.12 0.16 0.22 1"/>
    <material name="floor_material" rgba="0.55 0.38 0.22 1"/>
  </asset>

  <worldbody>
    <light name="court_light" pos="1 -3 7" dir="0.25 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="2 -8 3.6" xyaxes="1 0 0 0 0.242536 0.970143" fovy="48"/>

    <geom name="floor" type="plane" pos="0 0 0" size="12 12 0.1" material="floor_material" friction="0.7 0.005 0.0001" solref="0.01 0.5" solimp="0.95 0.99 0.001"/>

    <!-- Size-7 basketball: circumference 0.7502 m, mass 0.620 kg. -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.1194" mass="0.620" material="basketball_material" friction="0.7 0.005 0.0001" solref="0.01 0.5" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- The rim center is exactly 4 m horizontally from launch, at z = 3.05 m. -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" fromto="0.238100 0 0 0.233525 0.046451 0" size="0.0095" material="rim_material"/>
      <geom name="rim_01" type="capsule" fromto="0.233525 0.046451 0 0.219976 0.091119 0" size="0.0095" material="rim_material"/>
      <geom name="rim_02" type="capsule" fromto="0.219976 0.091119 0 0.197973 0.132281 0" size="0.0095" material="rim_material"/>
      <geom name="rim_03" type="capsule" fromto="0.197973 0.132281 0 0.168362 0.168362 0" size="0.0095" material="rim_material"/>
      <geom name="rim_04" type="capsule" fromto="0.168362 0.168362 0 0.132281 0.197973 0" size="0.0095" material="rim_material"/>
      <geom name="rim_05" type="capsule" fromto="0.132281 0.197973 0 0.091119 0.219976 0" size="0.0095" material="rim_material"/>
      <geom name="rim_06" type="capsule" fromto="0.091119 0.219976 0 0.046451 0.233525 0" size="0.0095" material="rim_material"/>
      <geom name="rim_07" type="capsule" fromto="0.046451 0.233525 0 0 0.238100 0" size="0.0095" material="rim_material"/>
      <geom name="rim_08" type="capsule" fromto="0 0.238100 0 -0.046451 0.233525 0" size="0.0095" material="rim_material"/>
      <geom name="rim_09" type="capsule" fromto="-0.046451 0.233525 0 -0.091119 0.219976 0" size="0.0095" material="rim_material"/>
      <geom name="rim_10" type="capsule" fromto="-0.091119 0.219976 0 -0.132281 0.197973 0" size="0.0095" material="rim_material"/>
      <geom name="rim_11" type="capsule" fromto="-0.132281 0.197973 0 -0.168362 0.168362 0" size="0.0095" material="rim_material"/>
      <geom name="rim_12" type="capsule" fromto="-0.168362 0.168362 0 -0.197973 0.132281 0" size="0.0095" material="rim_material"/>
      <geom name="rim_13" type="capsule" fromto="-0.197973 0.132281 0 -0.219976 0.091119 0" size="0.0095" material="rim_material"/>
      <geom name="rim_14" type="capsule" fromto="-0.219976 0.091119 0 -0.233525 0.046451 0" size="0.0095" material="rim_material"/>
      <geom name="rim_15" type="capsule" fromto="-0.233525 0.046451 0 -0.238100 0 0" size="0.0095" material="rim_material"/>
      <geom name="rim_16" type="capsule" fromto="-0.238100 0 0 -0.233525 -0.046451 0" size="0.0095" material="rim_material"/>
      <geom name="rim_17" type="capsule" fromto="-0.233525 -0.046451 0 -0.219976 -0.091119 0" size="0.0095" material="rim_material"/>
      <geom name="rim_18" type="capsule" fromto="-0.219976 -0.091119 0 -0.197973 -0.132281 0" size="0.0095" material="rim_material"/>
      <geom name="rim_19" type="capsule" fromto="-0.197973 -0.132281 0 -0.168362 -0.168362 0" size="0.0095" material="rim_material"/>
      <geom name="rim_20" type="capsule" fromto="-0.168362 -0.168362 0 -0.132281 -0.197973 0" size="0.0095" material="rim_material"/>
      <geom name="rim_21" type="capsule" fromto="-0.132281 -0.197973 0 -0.091119 -0.219976 0" size="0.0095" material="rim_material"/>
      <geom name="rim_22" type="capsule" fromto="-0.091119 -0.219976 0 -0.046451 -0.233525 0" size="0.0095" material="rim_material"/>
      <geom name="rim_23" type="capsule" fromto="-0.046451 -0.233525 0 0 -0.238100 0" size="0.0095" material="rim_material"/>
      <geom name="rim_24" type="capsule" fromto="0 -0.238100 0 0.046451 -0.233525 0" size="0.0095" material="rim_material"/>
      <geom name="rim_25" type="capsule" fromto="0.046451 -0.233525 0 0.091119 -0.219976 0" size="0.0095" material="rim_material"/>
      <geom name="rim_26" type="capsule" fromto="0.091119 -0.219976 0 0.132281 -0.197973 0" size="0.0095" material="rim_material"/>
      <geom name="rim_27" type="capsule" fromto="0.132281 -0.197973 0 0.168362 -0.168362 0" size="0.0095" material="rim_material"/>
      <geom name="rim_28" type="capsule" fromto="0.168362 -0.168362 0 0.197973 -0.132281 0" size="0.0095" material="rim_material"/>
      <geom name="rim_29" type="capsule" fromto="0.197973 -0.132281 0 0.219976 -0.091119 0" size="0.0095" material="rim_material"/>
      <geom name="rim_30" type="capsule" fromto="0.219976 -0.091119 0 0.233525 -0.046451 0" size="0.0095" material="rim_material"/>
      <geom name="rim_31" type="capsule" fromto="0.233525 -0.046451 0 0.238100 0 0" size="0.0095" material="rim_material"/>

      <geom name="rim_mount_left" type="capsule" fromto="0.229 0.065 0 0.381 0.065 0" size="0.010" material="rim_material"/>
      <geom name="rim_mount_right" type="capsule" fromto="0.229 -0.065 0 0.381 -0.065 0" size="0.010" material="rim_material"/>
      <geom name="backboard" type="box" pos="0.401 0 0.375" size="0.02 0.9 0.525" material="board_material"/>

      <geom name="target_top" type="box" pos="0.379 0 0.445" size="0.001 0.295 0.0125" rgba="0.85 0.12 0.025 1" contype="0" conaffinity="0"/>
      <geom name="target_bottom" type="box" pos="0.379 0 0.020" size="0.001 0.295 0.0125" rgba="0.85 0.12 0.025 1" contype="0" conaffinity="0"/>
      <geom name="target_left" type="box" pos="0.379 0.2825 0.2325" size="0.001 0.0125 0.225" rgba="0.85 0.12 0.025 1" contype="0" conaffinity="0"/>
      <geom name="target_right" type="box" pos="0.379 -0.2825 0.2325" size="0.001 0.0125 0.225" rgba="0.85 0.12 0.025 1" contype="0" conaffinity="0"/>
    </body>

    <!-- Offset support leaves the ball's landing path unobstructed. -->
    <body name="hoop_support" pos="4.75 1.1 0">
      <geom name="support_base" type="box" pos="0 0 0.045" size="0.35 0.35 0.045" material="support_material"/>
      <geom name="support_pole" type="cylinder" pos="0 0 1.9" size="0.07 1.9" material="support_material"/>
      <geom name="support_arm" type="capsule" fromto="0 0 3.7 -0.329 -1.1 3.7" size="0.055" material="support_material"/>
    </body>
  </worldbody>

  <!--
    Ball starts tangent to the floor with an upward launch velocity.
    With the specified Euler timestep, free flight reaches the rim center
    at t = 1.25 s, descending at approximately 3.777 m/s.
  -->
  <keyframe>
    <key name="start" time="0" qpos="0 0 0.1194 1 0 0 0" qvel="3.2 0 8.48554 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing a basketball scene**

I’m creating a scene with a pure orange basketball, ensuring it's a seamless sphere. The material's rough specularity is set at quite low values, and I’m naming it "ball_mat" without any textures for simplicity. For the floor, I want it dark and without texture, adding court lines to show a clear boundary. I’m avoiding unnecessary geometry with the ball. Finally, I’ll ensure ambient lighting and descriptive comments for clarity in the model.