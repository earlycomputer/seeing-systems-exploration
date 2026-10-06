The door starts open. A damped hinge spring pulls it against its closed-position stop and keeps it there.

```xml
<mujoco model="self_closing_door">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead_light" pos="1 -2 4" dir="-0.2 0.3 -1"/>
    <camera name="overview" pos="3 -4 2.7" xyaxes="0.8 0.6 0 -0.22 0.29 0.93"/>

    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.68 0.70 0.72 1" friction="1 0.005 0.0001"/>

    <body name="frame" pos="0 0 0">
      <geom name="frame_hinge_jamb" type="box" pos="-0.07 0 1.02" size="0.035 0.075 1.02" rgba="0.24 0.27 0.30 1"/>
      <geom name="frame_latch_jamb" type="box" pos="0.97 0 1.02" size="0.035 0.075 1.02" rgba="0.24 0.27 0.30 1"/>
      <geom name="frame_header" type="box" pos="0.45 0 2.075" size="0.555 0.075 0.035" rgba="0.24 0.27 0.30 1"/>
    </body>

    <body name="door" pos="0 0 0.08">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.6" stiffness="30" springref="-0.15" damping="14" armature="0.02" solreflimit="0.01 1" solimplimit="0.99 0.99 0.001"/>
      <geom name="door_leaf" type="box" pos="0.45 0 0.95" size="0.45 0.025 0.95" mass="9" rgba="0.40 0.22 0.10 1" friction="0.8 0.005 0.0001"/>
      <geom name="door_hinge_barrel" type="cylinder" pos="0 0 0.95" size="0.024 0.92" mass="0.15" contype="0" conaffinity="0" rgba="0.35 0.37 0.40 1"/>
      <geom name="door_upper_panel" type="box" pos="0.45 -0.028 1.40" size="0.34 0.004 0.34" mass="0.05" contype="0" conaffinity="0" rgba="0.50 0.29 0.14 1"/>
      <geom name="door_lower_panel" type="box" pos="0.45 -0.028 0.48" size="0.34 0.004 0.34" mass="0.05" contype="0" conaffinity="0" rgba="0.50 0.29 0.14 1"/>
      <geom name="door_handle_stem" type="capsule" fromto="0.79 -0.025 0.97 0.79 -0.075 0.97" size="0.012" mass="0.03" contype="0" conaffinity="0" rgba="0.75 0.70 0.48 1"/>
      <geom name="door_handle" type="sphere" pos="0.79 -0.085 0.97" size="0.028" mass="0.07" contype="0" conaffinity="0" rgba="0.75 0.70 0.48 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.2" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
```