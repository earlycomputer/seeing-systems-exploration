The pusher is a paddle on a horizontal slide joint, driven by a velocity motor at a constant 0.3 m/s. It starts 0.3 m from the stack, so the five blocks stand untouched for about one second. Then the paddle reaches `block1`, which is the only block at its height, and keeps driving it out from under the stack. Friction drags `block2` forward at its base while the blocks above lag behind, so the column tips back and falls.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <camera name="side" pos="0.2 -1.6 0.5" xyaxes="1 0 0 0 0.3 1"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.38 0 0.05">
      <joint name="pusher_slide" type="slide" axis="1 0 0" damping="0"/>
      <geom name="pusher_paddle" type="box" size="0.03 0.08 0.03" density="2000" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.2 0.8 0.3 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.9 0.8 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.9 0.5 0.1 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.6 0.2 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="pusher_motor" joint="pusher_slide" kv="500" forcelimited="true" forcerange="-200 200"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.3  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.3"/>
  </keyframe>
</mujoco>
```

```expect
pusher touches block1
block2 touches floor
block5 touches floor
```

---
thinking (summarized):

I'm designing a scene with a stack of five 0.1m cube blocks and a pusher mechanism that strikes the bottom block to topple the tower, considering whether to use a sliding body or swinging pendulum for the impact.

e the stack via friction, and the upper blocks could tip backward from the sudden push. I'll check "block touches floor" as a clear toppling signal, along with "pusher touches block1" for contact confirmation, formatted as "X touches Y" pairs. For reliable toppling, I'll make the pusher velocity-controlled at 0.3 m/s over a long travel range, sizing the actuator force to overcome friction from the stacked blocks' combined weight.

Without friction, blocks 2-5 would just drop 0.1 m straight down into a new stack, never touching the floor directly. But with friction, block2 gets dragged partially along with block1, so the base of the stack shifts while the top lags behind, causing it to tip backward and topple—making it likely block5 ends up touching the floor. I should also consider events like the pusher contacting block1, and note the setup where the pusher starts 0.3 m away moving at 0.3 m/s before any contact occurs.

Setting up the pusher geometry and velocity actuator...

Writing MJCF XML file...

