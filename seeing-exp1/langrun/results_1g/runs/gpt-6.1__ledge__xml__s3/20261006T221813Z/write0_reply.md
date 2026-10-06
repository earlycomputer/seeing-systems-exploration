```xml
<mujoco model="ball_table_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="50"/>
  <statistic center="0 0 0.5" extent="2"/>

  <worldbody>
    <light name="overhead" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.72 0.75 0.78 1" friction="0.8 0.01 0.005" condim="6"/>

    <!-- The tabletop ends at x = 0 and its upper surface is at z = 1. -->
    <body name="table">
      <geom name="table_top" type="box" pos="-0.6 0 0.97" size="0.6 0.4 0.03" rgba="0.50 0.30 0.15 1" friction="0.8 0.005 0.00005" condim="6" solref="0.01 1"/>
      <geom name="table_leg_1" type="box" pos="-1.08 -0.31 0.47" size="0.035 0.035 0.47" rgba="0.35 0.20 0.10 1"/>
      <geom name="table_leg_2" type="box" pos="-1.08 0.31 0.47" size="0.035 0.035 0.47" rgba="0.35 0.20 0.10 1"/>
      <geom name="table_leg_3" type="box" pos="-0.12 -0.31 0.47" size="0.035 0.035 0.47" rgba="0.35 0.20 0.10 1"/>
      <geom name="table_leg_4" type="box" pos="-0.12 0.31 0.47" size="0.035 0.035 0.47" rgba="0.35 0.20 0.10 1"/>
    </body>

    <!-- An open, watertight polygonal bucket centered 0.60 m beyond the edge. -->
    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.02" size="0.25 0.02" rgba="0.15 0.42 0.65 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.22 0 0.19" size="0.02 0.065 0.15" euler="0 0 0" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.190526 0.11 0.19" size="0.02 0.065 0.15" euler="0 0 30" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_03" type="box" pos="0.11 0.190526 0.19" size="0.02 0.065 0.15" euler="0 0 60" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_04" type="box" pos="0 0.22 0.19" size="0.02 0.065 0.15" euler="0 0 90" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.11 0.190526 0.19" size="0.02 0.065 0.15" euler="0 0 120" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.190526 0.11 0.19" size="0.02 0.065 0.15" euler="0 0 150" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.22 0 0.19" size="0.02 0.065 0.15" euler="0 0 180" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.190526 -0.11 0.19" size="0.02 0.065 0.15" euler="0 0 210" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_09" type="box" pos="-0.11 -0.190526 0.19" size="0.02 0.065 0.15" euler="0 0 240" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_10" type="box" pos="0 -0.22 0.19" size="0.02 0.065 0.15" euler="0 0 270" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.11 -0.190526 0.19" size="0.02 0.065 0.15" euler="0 0 300" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
      <geom name="bucket_wall_12" type="box" pos="0.190526 -0.11 0.19" size="0.02 0.065 0.15" euler="0 0 330" rgba="0.18 0.48 0.72 1" friction="0.9 0.02 0.01" condim="6" solref="0.01 1"/>
    </body>

    <body name="ball" pos="-0.8 0 1.04">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" density="800" rgba="0.95 0.25 0.12 1" friction="0.8 0.005 0.00005" condim="6" solref="0.01 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Initial translation and rotation give rolling without slipping: v = radius * omega. -->
    <key name="start" qpos="-0.8 0 1.04 1 0 0 0" qvel="1.4 0 0 0 35 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches table_top
ball touches bucket
ball comes to rest in bucket
```

---
thinking (summarized):

**Considering ball roll friction**

I'm trying to think through the ball's roll friction and how it could impact its movement. The coefficient of rolling friction I’ve noted is 0.0001, which might mean the ball slows down before reaching the edge of the table. I wonder how strong that effect really is. I should consider the surface it's rolling on and how that might change the behavior of the ball as it approaches the edge. It's an interesting thought!

**Considering ball impact dynamics**

I'm thinking about how the ball's impact might cause it to bounce between 0.04m and 0.01m, especially when critically damped enough to come to rest. That sounds good! I also need to consider factors like drop edge rolling and the pivot point when the edge is centered at x=0 and z=1.04, with gravity pulling down after the impact. It’s interesting how these aspects interact!

**Evaluating simulation details**

I’m working on the ball simulation, expecting it to contact the rear wall at around x.8, maybe starting at x.62. I think slip damping might stop it quickly before reaching x.63. I need to keep it realistically minimal. I’m considering using condim6 for all three components: the table, ball, and bucket. For the floor, it seems .005 should work. I need to check the table legs with condim3. Reducing defaults could help, but I want to be cautious.

**Setting up simulation environment**

I’m applying geom friction condim6 and setting solref to .01 for all bucket components. The density on static is irrelevant for my purposes. For camera orientation, I have specific xy axes values, and while I don’t need the camera, I can create a position if necessary. I could also optimize by focusing on stats with a center at "0 0 .5" and a visual headlight. The floor size is "3 3 .1," and the walls will be orange for clarity.