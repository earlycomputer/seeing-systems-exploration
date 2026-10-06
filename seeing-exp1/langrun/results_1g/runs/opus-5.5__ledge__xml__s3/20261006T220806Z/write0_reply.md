The ball starts 0.5 m from the table edge, already rolling at 1.52 m/s. It leaves the 0.75 m high table and falls for about 0.39 s. That carries it about 0.59 m forward, to the middle of the bucket's floor. The bucket's base has rolling friction so the ball settles there instead of rolling around for ever.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" size="0.5 0.4 0.02" pos="-0.5 0 0.73" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" size="0.03 0.03 0.355" pos="-0.06 0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" size="0.03 0.03 0.355" pos="-0.06 -0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" size="0.03 0.03 0.355" pos="-0.94 0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" size="0.03 0.03 0.355" pos="-0.94 -0.35 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_base" type="cylinder" size="0.17 0.01" pos="0 0 0.01" condim="6" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" size="0.01 0.068 0.1" pos="0.155 0 0.11" euler="0 0 0" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall1" type="box" size="0.01 0.068 0.1" pos="0.1096 0.1096 0.11" euler="0 0 45" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall2" type="box" size="0.01 0.068 0.1" pos="0 0.155 0.11" euler="0 0 90" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall3" type="box" size="0.01 0.068 0.1" pos="-0.1096 0.1096 0.11" euler="0 0 135" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall4" type="box" size="0.01 0.068 0.1" pos="-0.155 0 0.11" euler="0 0 180" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall5" type="box" size="0.01 0.068 0.1" pos="-0.1096 -0.1096 0.11" euler="0 0 225" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall6" type="box" size="0.01 0.068 0.1" pos="0 -0.155 0.11" euler="0 0 270" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="bucket_wall7" type="box" size="0.01 0.068 0.1" pos="0.1096 -0.1096 0.11" euler="0 0 315" rgba="0.2 0.4 0.8 0.6"/>
    </body>

    <body name="ball" pos="-0.5 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.5 0 0.78 1 0 0 0" qvel="1.52 0 0 0 50.667 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches table_top
ball touches bucket_base
ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the physics for the ball drop: table height, edge position, bucket location, and the fall trajectory so the ball lands inside the bucket, including walls built from box shapes.

I'm computing the fall time and required horizontal velocity, then checking the trajectory clears the near rim and lands properly inside the bucket. Now I'm setting consistent linear and angular velocity so the ball rolls naturally off the table edge.

Building the bucket shape...

I'm thinking through the physics: the ball enters moving fast toward the far wall, bounces off with some energy loss from the default contact damping, but keeps rolling and spinning inside the enclosure rather than settling quickly. I should consider adding higher condim or friction to help it actually come to rest within the simulation time.

Since condim combines as max, setting it on the base geom alone suffices, and with rolling friction 0.005 the deceleration works out to roughly 1.17 m/s², stopping the ball in about 1.3 seconds. For the vertical impact at ~3.9 m/s, default solref should keep it critically damped with minimal bounce, and even though the ball moves ~8mm per timestep, its 30mm radius means it won't tunnel through the thin base.

I'm now checking the bucket geometry: the far wall is tall enough to contain the ball moving at 1.5 m/s, and the ball's trajectory (starting at x=-0.5, z=0.78, launched with keyframe velocities) lands around x=0.586 at the base height of 0.05, well clear of the walls. The bucket itself is static with no joint, so the keyframe only needs to specify the ball's qpos and qvel, and I should verify this satisfies expectations like the ball touching the table and settling at rest in the bucket.

I'm settling on using "ball touches table_top" for the contact check, confirming geom names, and noting the ball's default density gives a reasonable mass. I also want to make sure the ball clears the table legs, which sit near x=-0.05 under the tabletop, so the ball's path passing above them should be fine.

