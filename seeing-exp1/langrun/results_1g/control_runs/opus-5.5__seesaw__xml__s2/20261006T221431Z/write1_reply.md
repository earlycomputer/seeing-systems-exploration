Corrected file below; nothing was run. The ball's surface reached 0.97 m along the plank, but the lip starts at 0.94 m, so they overlapped by 30 mm. I moved the ball inward to 0.89 m along the plank, which leaves a 10 mm gap to the lip. The ball then rolls the last centimetre against the lip once the simulation starts.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="plank_mat" rgba="0.6 0.4 0.2 1"/>
    <material name="weight_mat" rgba="0.2 0.2 0.25 1"/>
    <material name="ball_mat" rgba="0.9 0.2 0.1 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 5" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" material="floor_mat" friction="1 0.005 0.005"/>

    <!-- visual-only fulcrum under the pivot -->
    <geom name="fulcrum" type="box" pos="0 0 0.14" size="0.05 0.12 0.14" rgba="0.4 0.4 0.4 1" contype="0" conaffinity="0"/>

    <!-- seesaw: tilted 15 deg so the +x (ball) end is down, -x (weight) end is up -->
    <body name="seesaw" pos="0 0 0.3" euler="0 15 0">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-30 0" damping="0.5"/>
      <geom name="plank" type="box" size="1.0 0.1 0.02" mass="1.0" material="plank_mat"/>
      <geom name="lip_ball" type="box" pos="0.96 0 0.06" size="0.02 0.1 0.04" mass="0.05" material="plank_mat"/>
      <geom name="lip_weight" type="box" pos="-0.96 0 0.06" size="0.02 0.1 0.04" mass="0.05" material="plank_mat"/>
    </body>

    <!-- 1 kg weight dropped from rest above the raised end -->
    <body name="weight" pos="-0.82 0 3.0">
      <freejoint name="weight_free"/>
      <geom name="weight" type="sphere" size="0.08" mass="1.0" condim="6" friction="1 0.01 0.01" material="weight_mat"/>
    </body>

    <!-- 100 g ball resting in the pocket at the lowered end (plank-local x=0.89, z=0.061) -->
    <body name="ball" pos="0.8755 0 0.1286">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.01 0.01" material="ball_mat"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm converting the ball's world position into the body's local frame by subtracting the body position and applying the inverse rotation, computing the local x and z coordinates using the cosine and sine of the 15-degree angle.

Working through this, the ball actually lands at local 0.93, which overlaps the lip (spanning 0.94–0.98) by 0.03 once the radius is added—so my earlier placement was wrong. I need to pull the ball back to local x=0.89 instead, leaving a small 0.01 gap, then recompute its world coordinates from that corrected local position. I also double-check the weight's position against the lip on the opposite side and confirm it clears fine since it's still airborne at that point.

