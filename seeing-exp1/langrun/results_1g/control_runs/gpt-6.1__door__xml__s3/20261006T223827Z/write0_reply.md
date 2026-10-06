```xml
<mujoco model="self_closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead_light" pos="0 -2 4" dir="0 0.4 -1"/>
    <camera name="overview" pos="3 -4 2.8" xyaxes="0.8 0.6 0 -0.24 0.32 0.9165"/>

    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.65 0.68 0.70 1"/>
    <geom name="left_jamb" type="box" pos="-0.57 0 1.07" size="0.06 0.08 1.07" rgba="0.25 0.28 0.31 1"/>
    <geom name="right_jamb" type="box" pos="0.57 0 1.07" size="0.06 0.08 1.07" rgba="0.25 0.28 0.31 1"/>
    <geom name="lintel" type="box" pos="0 0 2.20" size="0.63 0.08 0.06" rgba="0.25 0.28 0.31 1"/>

    <!-- A passive hinge spring closes the door; near-critical damping prevents rebound. -->
    <body name="door" pos="-0.5 0 0.07">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.65" stiffness="30" springref="0" damping="18.2" armature="0.02"/>
      <geom name="door_panel" type="box" pos="0.5 0 1" size="0.5 0.03 1" mass="8" rgba="0.48 0.25 0.12 1"/>
      <geom name="door_knob" type="sphere" pos="0.9 -0.065 1" size="0.035" mass="0.08" rgba="0.85 0.67 0.22 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.25" qvel="0"/>
  </keyframe>
</mujoco>
```