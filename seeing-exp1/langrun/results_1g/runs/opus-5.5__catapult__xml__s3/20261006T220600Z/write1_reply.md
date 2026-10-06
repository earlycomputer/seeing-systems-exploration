The full-length axle passed through the beam, so I split it into two short stubs. Each stub runs from just outside the beam's side face (y = ±0.052) to the inner face of its post (y = ±0.10). Nothing else changed, and the file still hasn't been run.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="0 0.4 -1"/>
    <geom name="floor" type="plane" size="6 3 0.1" pos="0 0 0"/>
    <body name="catapult_base" pos="0 0 0">
      <geom name="catapult_baseplate" type="box" size="0.25 0.18 0.01" pos="0 0 0.01"/>
      <geom name="catapult_post_left" type="box" size="0.02 0.02 0.19" pos="0 0.12 0.21"/>
      <geom name="catapult_post_right" type="box" size="0.02 0.02 0.19" pos="0 -0.12 0.21"/>
      <geom name="catapult_axle_left" type="cylinder" size="0.012 0.024" pos="0 0.076 0.4" euler="90 0 0"/>
      <geom name="catapult_axle_right" type="cylinder" size="0.012 0.024" pos="0 -0.076 0.4" euler="90 0 0"/>
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" limited="true" solreflimit="0.005 1" damping="0"/>
        <geom name="catapult_beam" type="box" size="0.38 0.05 0.01" pos="-0.28 0 0" mass="0.2"/>
        <geom name="catapult_cup_outer" type="box" size="0.01 0.055 0.03" pos="-0.651 0 0.04" mass="0.03"/>
        <geom name="catapult_cup_inner" type="box" size="0.01 0.055 0.015" pos="-0.55 0 0.025" mass="0.02"/>
        <geom name="catapult_cup_side_left" type="box" size="0.04 0.005 0.02" pos="-0.6 0.05 0.03" mass="0.015"/>
        <geom name="catapult_cup_side_right" type="box" size="0.04 0.005 0.02" pos="-0.6 -0.05 0.03" mass="0.015"/>
      </body>
    </body>
    <body name="ball" pos="-0.6 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.005 0.001"/>
    </body>
    <body name="bucket" pos="2.4 0 0">
      <geom name="bucket_floor" type="box" size="0.32 0.32 0.01" pos="0 0 0.01"/>
      <geom name="bucket_wall_far" type="box" size="0.01 0.32 0.125" pos="0.31 0 0.135"/>
      <geom name="bucket_wall_near" type="box" size="0.01 0.32 0.125" pos="-0.31 0 0.135"/>
      <geom name="bucket_wall_left" type="box" size="0.3 0.01 0.125" pos="0 0.31 0.135"/>
      <geom name="bucket_wall_right" type="box" size="0.3 0.01 0.125" pos="0 -0.31 0.135"/>
    </body>
  </worldbody>
  <actuator>
    <velocity name="catapult_drive" joint="catapult_hinge" kv="30" forcelimited="true" forcerange="-15 15"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 -0.6 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="7.84"/>
  </keyframe>
</mujoco>
```

```expect
catapult_arm reaches its upper stop
ball touches bucket_floor
ball comes to rest in bucket
```

---
thinking (summarized):

I'm noticing the axle overlaps the beam despite parent-child filtering, so I need to split it into two shorter stubs positioned between the posts and the beam's sides, keeping them just touching the beam edge rather than passing through it.

Checking the rest of the geometry, the cup sides, posts, and beam are all properly spaced in y and z with no overlaps, so the layout looks clean aside from the axle fix.

