Two fixes:

- **Angle units:** I added `<compiler angle="radian"/>`, so the hinge range of 0 to 1.7 is read in radians. The keyframe start of 1.3 rad is now inside it.
- **Overlap:** I moved the hinge post back. When the door is swung open, its back edge pokes about 2 cm behind the hinge line, and the post now starts 4 cm behind it.

```xml
<mujoco model="closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.3 0.5 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="view" pos="2.2 -2.6 1.8" xyaxes="0.76 0.65 0 -0.3 0.35 0.89"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="frame_hingepost" type="box" pos="-0.06 0 1.05" size="0.02 0.05 1.05" rgba="0.4 0.3 0.2 1"/>
      <geom name="frame_jamb" type="box" pos="0.95 -0.031 1.05" size="0.05 0.01 1.05" rgba="0.4 0.3 0.2 1" contype="0" conaffinity="0"/>
      <geom name="frame_latchpost" type="box" pos="0.97 0.02 1.05" size="0.03 0.04 1.05" rgba="0.4 0.3 0.2 1" contype="0" conaffinity="0"/>
      <geom name="frame_lintel" type="box" pos="0.46 0 2.13" size="0.54 0.05 0.03" rgba="0.4 0.3 0.2 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="40" springref="-0.3" damping="15" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.02" size="0.45 0.02 1.0" density="500" rgba="0.7 0.5 0.3 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.06 1.0" size="0.03" density="500" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.3" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
```

---
thinking (summarized):

I need to set the compiler angle unit to radians, then check whether the rotated door panel overlaps the hinge point by working out where its corner lands after rotating by 1.3 radians.

I'm finding the panel's corner only reaches about -0.02 at maximum rotation, so moving the hinge post back so it spans -0.08 to -0.04 avoids collision. I'm also confirming the jamb, latchpost, and lintel positions don't collide with anything else in the frame.

