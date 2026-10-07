The seesaw range was meant in radians but MuJoCo read it as degrees. I added `<compiler angle="radian"/>` so it is now read as radians. This also corrects the seesaw axle's `euler` rotation, which had the same problem.

I also widened the seesaw's upper limit very slightly, from 0.36 to 0.361. The seesaw now starts just inside its range, still resting against that limit with its ball end down. Like the earlier version, this has not been run.

```xml
<mujoco model="pendulum_cart_seesaw_cup">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0.6 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="frame_post" type="box" pos="0 -0.2 0.6" size="0.02 0.02 0.6" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="frame_beam" type="box" pos="0 -0.1 1.2" size="0.015 0.1 0.015" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="shelf" type="box" pos="0.235 0 0.2725" size="0.165 0.1 0.2725" rgba="0.6 0.45 0.3 1"/>
    <geom name="lower_stop" type="box" pos="0.435 0 0.155" size="0.02 0.05 0.155" rgba="0.7 0.2 0.2 1"/>
    <geom name="seesaw_stand" type="box" pos="0.75 0 0.15" size="0.02 0.08 0.15" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>

    <body name="pendulum" pos="0 0 1.2">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.55" size="0.01" mass="0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.6" size="0.05" mass="1" rgba="0.2 0.2 0.8 1"/>
    </body>

    <body name="cart" pos="0.115 0 0.6">
      <joint name="cart_slide" type="slide" axis="1 0 0" limited="true" range="-0.01 0.10"/>
      <geom name="cart_body" type="box" size="0.06 0.06 0.05" mass="3" rgba="0.9 0.6 0.1 1"/>
    </body>

    <body name="weight" pos="0.245 0 0.585">
      <freejoint name="weight_free"/>
      <geom name="weight_geom" type="sphere" size="0.04" mass="1" rgba="0.2 0.2 0.2 1"/>
    </body>

    <body name="seesaw" pos="0.75 0 0.32">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-0.1 0.361"/>
      <geom name="seesaw_axle" type="cylinder" pos="0 0 0" size="0.015 0.07" euler="1.5708 0 0" contype="0" conaffinity="0" mass="0.01" rgba="0.3 0.3 0.3 1"/>
      <geom name="seesaw_plank" type="box" pos="0.04 0 0" size="0.40 0.06 0.01" mass="0.2" rgba="0.2 0.7 0.3 1"/>
      <geom name="seesaw_tray_wall" type="box" pos="-0.185 0 0.03" size="0.005 0.06 0.02" mass="0.02" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_a" type="box" pos="-0.275 0.055 0.02" size="0.085 0.005 0.01" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_b" type="box" pos="-0.275 -0.055 0.02" size="0.085 0.005 0.01" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_post" type="box" pos="0.40 0 0.03" size="0.008 0.008 0.02" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_pad" type="box" pos="0.40 0 0.055" size="0.033 0.03 0.005" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_lip" type="box" pos="0.430 0 0.066" size="0.003 0.03 0.006" mass="0.002" rgba="0.2 0.5 0.3 1"/>
    </body>

    <body name="ball" pos="1.1611 0 0.2518">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.02" mass="0.02" condim="6" friction="0.8 0.01 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="cup" pos="1.425 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.19 0.15 0.01" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.18 0 0.16" size="0.005 0.15 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_far" type="box" pos="0.18 0 0.16" size="0.005 0.15 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.145 0.16" size="0.175 0.005 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.145 0.16" size="0.175 0.005 0.14" rgba="0.3 0.6 0.9 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5708 0 0.245 0 0.585 1 0 0 0 0.36 1.1611 0 0.2518 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I realize I need to add a radian angle compiler setting, which fixes the axle euler interpretation without other changes. I'm also reconsidering whether the range's upper bound matching the initial value exactly could cause it to start right at the joint limit, so I might widen it slightly to avoid starting at the boundary.

