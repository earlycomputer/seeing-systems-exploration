The hinge range was read in degrees, so it allowed only ±0.3°. The file now declares `<compiler angle="radian"/>`, which makes the range ±0.3 rad. The keyframe start of 0.3 rad (ball end down) then sits at the lower stop instead of far outside it.

```xml
<mujoco model="seesaw_catapult">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="fulcrum" type="box" pos="0 0 0.1" size="0.03 0.08 0.1" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="seesaw" pos="0 0 0.25">
      <joint name="pivot" type="hinge" axis="0 1 0" limited="true" range="-0.3 0.3"/>
      <geom name="plank" type="box" size="0.75 0.06 0.02" mass="0.3" rgba="0.7 0.5 0.3 1"/>
      <geom name="lip" type="box" pos="0.73 0 0.05" size="0.02 0.06 0.03" mass="0.01" rgba="0.5 0.3 0.2 1"/>
    </body>
    <body name="weight" pos="-0.615 0 1.6">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.06" mass="1.0" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="0.6578 0 0.110">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.3 -0.615 0 1.6 1 0 0 0 0.6578 0 0.110 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I should add a compiler angle="radian" setting to fix this, and reconsider whether starting exactly at the joint limit of 0.3 is a problem—it's technically at the boundary but should still work, though I could widen the range slightly to be safe.

