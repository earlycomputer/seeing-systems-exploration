MuJoCo read the joint range in degrees, so the door started outside its limit. I added `<compiler angle="radian"/>`, so the hinge range (0 to 1.65 rad ≈ 95°) and the closer's spring reference (−0.2 rad) now use the same units as the keyframe. The door now starts open at 1.4 rad (about 80°), inside its range. I have not run this version.

```xml
<mujoco model="self_closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.6 0.6 0.6"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <!-- door frame (static) -->
    <geom name="hinge_jamb" type="box" pos="-0.075 0 1.05" size="0.045 0.07 1.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="latch_jamb" type="box" pos="0.985 0 1.05" size="0.045 0.07 1.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="lintel" type="box" pos="0.455 0 2.15" size="0.575 0.07 0.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="door_stop" type="box" pos="0.87 -0.046 1.0" size="0.07 0.025 0.95" rgba="0.35 0.22 0.15 1"/>

    <!-- the door: shut at hinge = 0, opens toward +y for positive angles -->
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" range="0 1.65" limited="true" stiffness="20" springref="-0.2" damping="8" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.47 0 1.02" size="0.45 0.02 1.0" density="500" rgba="0.75 0.55 0.35 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.05 1.0" size="0.03" density="500" contype="0" conaffinity="0" rgba="0.85 0.75 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Since springref for hinge joints is also affected by compiler angle units, I should add compiler angle="radian" to be safe, so both the range and springref are in radians and consistent with the keyframe qpos value of 1.4.

