The pusher is a heavy 20 kg paddle on a frictionless horizontal slide joint. It starts 0.6 m away from the stack and has a keyframe velocity of 0.6 m/s, so the five 10 cm blocks stand for about 1 s. Then the paddle hits only the bottom block and keeps driving it out from under the stack, and the four blocks above tip over and fall. I haven't run this, so the timing and the exact way the stack falls are estimates.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="block_mat" rgba="0.85 0.55 0.25 1"/>
    <material name="pusher_mat" rgba="0.2 0.3 0.8 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" material="floor_mat" friction="0.6 0.005 0.0001"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" material="block_mat" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" material="block_mat" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" material="block_mat" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" material="block_mat" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" material="block_mat" friction="0.6 0.005 0.0001"/>
    </body>

    <body name="pusher" pos="-0.7 0 0.05">
      <joint name="pusher_slide" type="slide" axis="1 0 0" damping="0"/>
      <geom name="pusher_geom" type="box" size="0.05 0.08 0.03" mass="20" material="pusher_mat" friction="0.6 0.005 0.0001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0.6"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm designing a scene with a stack of five 0.1m cubes and a pusher block that slides along a joint with initial velocity to strike the bottom block, causing the stack to topple.

drag on the upper stack, and since friction can't keep the whole stack accelerating with block1, the top blocks lag behind and topple backward off the moving bottom block. I'll give the pusher a hefty mass like 20 kg and a decent speed around 1 m/s so it yanks block1 out fast enough that the upper blocks can't keep up and tip over.

I'm working out the starting position so the pusher makes contact right around 1 second, factoring in its half-width and a small gap, and deciding whether to cap its travel range or just let it keep sliding — simpler to skip the range limit. Now I'm setting up the block stack with centers positioned so they start in solid contact without overlap issues.

I'm figuring out the keyframe structure: ordering free joints for the five blocks plus the single slide joint for the pusher, deciding to list blocks first in the body order, and working out the qpos/qvel values accordingly, with the slide joint's zero position corresponding to the pusher's starting offset and the velocity entry set to 0.6.

Checking collision geometry — the pusher sits above the floor with no contact, and its height clears the bottom block so it can push into block2 without interference. With that confirmed, I'm ready to write out the full file.

