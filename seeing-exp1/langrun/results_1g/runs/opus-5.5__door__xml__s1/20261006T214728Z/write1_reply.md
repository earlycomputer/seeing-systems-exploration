MuJoCo read the joint range as degrees, so the 1.4 rad start sat outside it. I've added `<compiler angle="radian"/>`, which makes the range (0 to 1.7 rad) and the spring reference (−0.3 rad) both read as radians, matching the keyframe.

```xml
<mujoco model="closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="4 4 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="frame_hinge_post" type="box" pos="-0.04 0 1.03" size="0.03 0.05 1.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_latch_post" type="box" pos="0.94 0 1.03" size="0.03 0.05 1.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_header" type="box" pos="0.45 0 2.09" size="0.52 0.05 0.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0.03">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="20" springref="-0.3" damping="12" armature="0.1"/>
      <geom name="door_slab" type="box" pos="0.45 0 1.0" size="0.44 0.02 1.0" density="600" rgba="0.6 0.4 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" density="600" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
```

---
thinking (summarized):

I should set the compiler angle to radians, since springref for the hinge is also interpreted under that same compiler setting, so -0.3 rad will work correctly.

