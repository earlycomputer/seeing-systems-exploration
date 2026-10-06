You're right: MuJoCo read the range `0 1.7` as degrees, so the door started 80° outside it. I've added `<compiler angle="radian"/>`, so the range now runs 0 to 1.7 rad (about 97°), and the keyframe start of 1.4 rad sits inside it. The spring rest angle of -0.1 rad is also read in radians now.

```xml
<mujoco model="door_swings_shut">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 -3 4" dir="0 0.6 -0.8" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <geom name="wall_hinge_side" type="box" pos="-0.55 0 1.1" size="0.5 0.05 1.1" rgba="0.85 0.82 0.75 1"/>
    <geom name="wall_latch_side" type="box" pos="1.45 0 1.1" size="0.5 0.05 1.1" rgba="0.85 0.82 0.75 1"/>
    <geom name="lintel" type="box" pos="0.45 0 2.15" size="0.5 0.05 0.05" rgba="0.85 0.82 0.75 1"/>
    <geom name="door_stop" type="box" pos="0.87 -0.036 1.01" size="0.03 0.015 0.95" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.7" stiffness="20" springref="-0.1" damping="12"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.01" size="0.45 0.02 1.0" mass="30" rgba="0.55 0.35 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" mass="0.2" rgba="0.9 0.8 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The range is interpreted in degrees by default, so I should add compiler angle="radian" to keep units consistent — this should also resolve springref since it's tied to the same angle convention.

