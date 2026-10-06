The ball starts on the floor and is launched by its keyframe velocity. Its trajectory carries it downward through the regulation-size rim, centered 4 m away at a height of 3.05 m.

```xml
<mujoco model="basketball_shot">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <visual>
    <global azimuth="90" elevation="-15"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65"/>
  </visual>

  <asset>
    <material name="court_material" rgba="0.55 0.38 0.22 1"/>
    <material name="ball_material" rgba="0.85 0.29 0.055 1"/>
    <material name="rim_material" rgba="0.95 0.16 0.035 1"/>
    <material name="board_material" rgba="0.88 0.91 0.95 1"/>
    <material name="support_material" rgba="0.16 0.19 0.23 1"/>
  </asset>

  <worldbody>
    <light name="court_light" pos="2 -3 7" dir="0 0.3 -1"/>
    <camera name="overview" pos="2 -10 5" xyaxes="1 0 0 0 0.287348 0.957826"/>

    <geom name="floor" type="plane" pos="0 0 0" size="12 8 0.1" material="court_material" friction="0.8 0.01 0.002"/>

    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.12" mass="0.624" material="ball_material" friction="0.6 0.01 0.002" solref="0.01 0.8"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <!-- Rim tube radius: 9 mm; nominal clear diameter: 457.2 mm. -->
      <geom name="rim_00" type="capsule" fromto="0.237600 0 0 0.233035 0.046352 0" size="0.009" material="rim_material"/>
      <geom name="rim_01" type="capsule" fromto="0.233035 0.046352 0 0.219514 0.090926 0" size="0.009" material="rim_material"/>
      <geom name="rim_02" type="capsule" fromto="0.219514 0.090926 0 0.197557 0.132003 0" size="0.009" material="rim_material"/>
      <geom name="rim_03" type="capsule" fromto="0.197557 0.132003 0 0.168009 0.168009 0" size="0.009" material="rim_material"/>
      <geom name="rim_04" type="capsule" fromto="0.168009 0.168009 0 0.132003 0.197557 0" size="0.009" material="rim_material"/>
      <geom name="rim_05" type="capsule" fromto="0.132003 0.197557 0 0.090926 0.219514 0" size="0.009" material="rim_material"/>
      <geom name="rim_06" type="capsule" fromto="0.090926 0.219514 0 0.046352 0.233035 0" size="0.009" material="rim_material"/>
      <geom name="rim_07" type="capsule" fromto="0.046352 0.233035 0 0 0.237600 0" size="0.009" material="rim_material"/>
      <geom name="rim_08" type="capsule" fromto="0 0.237600 0 -0.046352 0.233035 0" size="0.009" material="rim_material"/>
      <geom name="rim_09" type="capsule" fromto="-0.046352 0.233035 0 -0.090926 0.219514 0" size="0.009" material="rim_material"/>
      <geom name="rim_10" type="capsule" fromto="-0.090926 0.219514 0 -0.132003 0.197557 0" size="0.009" material="rim_material"/>
      <geom name="rim_11" type="capsule" fromto="-0.132003 0.197557 0 -0.168009 0.168009 0" size="0.009" material="rim_material"/>
      <geom name="rim_12" type="capsule" fromto="-0.168009 0.168009 0 -0.197557 0.132003 0" size="0.009" material="rim_material"/>
      <geom name="rim_13" type="capsule" fromto="-0.197557 0.132003 0 -0.219514 0.090926 0" size="0.009" material="rim_material"/>
      <geom name="rim_14" type="capsule" fromto="-0.219514 0.090926 0 -0.233035 0.046352 0" size="0.009" material="rim_material"/>
      <geom name="rim_15" type="capsule" fromto="-0.233035 0.046352 0 -0.237600 0 0" size="0.009" material="rim_material"/>
      <geom name="rim_16" type="capsule" fromto="-0.237600 0 0 -0.233035 -0.046352 0" size="0.009" material="rim_material"/>
      <geom name="rim_17" type="capsule" fromto="-0.233035 -0.046352 0 -0.219514 -0.090926 0" size="0.009" material="rim_material"/>
      <geom name="rim_18" type="capsule" fromto="-0.219514 -0.090926 0 -0.197557 -0.132003 0" size="0.009" material="rim_material"/>
      <geom name="rim_19" type="capsule" fromto="-0.197557 -0.132003 0 -0.168009 -0.168009 0" size="0.009" material="rim_material"/>
      <geom name="rim_20" type="capsule" fromto="-0.168009 -0.168009 0 -0.132003 -0.197557 0" size="0.009" material="rim_material"/>
      <geom name="rim_21" type="capsule" fromto="-0.132003 -0.197557 0 -0.090926 -0.219514 0" size="0.009" material="rim_material"/>
      <geom name="rim_22" type="capsule" fromto="-0.090926 -0.219514 0 -0.046352 -0.233035 0" size="0.009" material="rim_material"/>
      <geom name="rim_23" type="capsule" fromto="-0.046352 -0.233035 0 0 -0.237600 0" size="0.009" material="rim_material"/>
      <geom name="rim_24" type="capsule" fromto="0 -0.237600 0 0.046352 -0.233035 0" size="0.009" material="rim_material"/>
      <geom name="rim_25" type="capsule" fromto="0.046352 -0.233035 0 0.090926 -0.219514 0" size="0.009" material="rim_material"/>
      <geom name="rim_26" type="capsule" fromto="0.090926 -0.219514 0 0.132003 -0.197557 0" size="0.009" material="rim_material"/>
      <geom name="rim_27" type="capsule" fromto="0.132003 -0.197557 0 0.168009 -0.168009 0" size="0.009" material="rim_material"/>
      <geom name="rim_28" type="capsule" fromto="0.168009 -0.168009 0 0.197557 -0.132003 0" size="0.009" material="rim_material"/>
      <geom name="rim_29" type="capsule" fromto="0.197557 -0.132003 0 0.219514 -0.090926 0" size="0.009" material="rim_material"/>
      <geom name="rim_30" type="capsule" fromto="0.219514 -0.090926 0 0.233035 -0.046352 0" size="0.009" material="rim_material"/>
      <geom name="rim_31" type="capsule" fromto="0.233035 -0.046352 0 0.237600 0 0" size="0.009" material="rim_material"/>

      <geom name="backboard" type="box" pos="0.401 0 0.46" size="0.02 0.915 0.61" material="board_material"/>
      <geom name="rim_mount" type="box" pos="0.3115 0 0" size="0.0695 0.055 0.012" material="rim_material"/>
    </body>

    <body name="support" pos="4.48 1.20 0">
      <geom name="support_base" type="box" pos="0 0 0.06" size="0.40 0.40 0.06" material="support_material"/>
      <geom name="support_post" type="box" pos="0 0 1.80" size="0.075 0.075 1.80" material="support_material"/>
      <geom name="support_arm" type="box" pos="0 -0.60 3.60" size="0.075 0.60 0.075" material="support_material"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" time="0" qpos="0 0 0.12 1 0 0 0" qvel="2.666666667 0 9.310833333 0 -6 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
```