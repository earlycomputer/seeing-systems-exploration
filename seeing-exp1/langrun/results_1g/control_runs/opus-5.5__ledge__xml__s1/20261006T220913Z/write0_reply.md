The ball starts on a 0.75 m high table, rolling without slip at about 1.56 m/s. It leaves the table edge at x = 0 and falls into a bucket centred at x = 0.6 m. The bucket floor has rolling friction, so the ball stops inside the bucket.

```xml
<mujoco model="ball_table_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.6 0.6 0.65 1"/>
    <material name="wood" rgba="0.55 0.35 0.2 1"/>
    <material name="bucket_mat" rgba="0.2 0.4 0.8 1"/>
    <material name="ball_mat" rgba="0.9 0.2 0.1 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0.3 -1 3" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="0.1 -2.2 0.7" xyaxes="1 0 0 0 0.3 1"/>

    <geom name="floor" type="plane" size="5 5 0.1" material="floor_mat"/>

    <!-- Table: top surface at z = 0.75, edge at x = 0 -->
    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" size="0.5 0.3 0.02" pos="-0.5 0 0.73" material="wood" friction="1 0.005 0.0001"/>
      <geom name="table_leg1" type="box" size="0.025 0.025 0.355" pos="-0.05 0.25 0.355" material="wood"/>
      <geom name="table_leg2" type="box" size="0.025 0.025 0.355" pos="-0.05 -0.25 0.355" material="wood"/>
      <geom name="table_leg3" type="box" size="0.025 0.025 0.355" pos="-0.95 0.25 0.355" material="wood"/>
      <geom name="table_leg4" type="box" size="0.025 0.025 0.355" pos="-0.95 -0.25 0.355" material="wood"/>
    </body>

    <!-- Bucket: centre 0.6 m beyond the table edge, inner radius ~0.15 m, rim at z = 0.27 -->
    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.17 0.01" pos="0 0 0.01" material="bucket_mat" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall00" type="box" size="0.01 0.044 0.125" pos="0.16 0 0.145" euler="0 0 0" material="bucket_mat"/>
      <geom name="bucket_wall01" type="box" size="0.01 0.044 0.125" pos="0.1386 0.08 0.145" euler="0 0 30" material="bucket_mat"/>
      <geom name="bucket_wall02" type="box" size="0.01 0.044 0.125" pos="0.08 0.1386 0.145" euler="0 0 60" material="bucket_mat"/>
      <geom name="bucket_wall03" type="box" size="0.01 0.044 0.125" pos="0 0.16 0.145" euler="0 0 90" material="bucket_mat"/>
      <geom name="bucket_wall04" type="box" size="0.01 0.044 0.125" pos="-0.08 0.1386 0.145" euler="0 0 120" material="bucket_mat"/>
      <geom name="bucket_wall05" type="box" size="0.01 0.044 0.125" pos="-0.1386 0.08 0.145" euler="0 0 150" material="bucket_mat"/>
      <geom name="bucket_wall06" type="box" size="0.01 0.044 0.125" pos="-0.16 0 0.145" euler="0 0 180" material="bucket_mat"/>
      <geom name="bucket_wall07" type="box" size="0.01 0.044 0.125" pos="-0.1386 -0.08 0.145" euler="0 0 210" material="bucket_mat"/>
      <geom name="bucket_wall08" type="box" size="0.01 0.044 0.125" pos="-0.08 -0.1386 0.145" euler="0 0 240" material="bucket_mat"/>
      <geom name="bucket_wall09" type="box" size="0.01 0.044 0.125" pos="0 -0.16 0.145" euler="0 0 270" material="bucket_mat"/>
      <geom name="bucket_wall10" type="box" size="0.01 0.044 0.125" pos="0.08 -0.1386 0.145" euler="0 0 300" material="bucket_mat"/>
      <geom name="bucket_wall11" type="box" size="0.01 0.044 0.125" pos="0.1386 -0.08 0.145" euler="0 0 330" material="bucket_mat"/>
    </body>

    <!-- Ball: radius 3 cm, resting on the table top -->
    <body name="ball" pos="-0.4 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" material="ball_mat"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Rolling without slip: vx = 1.555 m/s, wy = vx / r = 51.83 rad/s -->
    <key name="start" qpos="-0.4 0 0.78 1 0 0 0" qvel="1.555 0 0 0 51.83 0 0"/>
  </keyframe>
</mujoco>
```

**Checks I worked by hand (not simulated):**

- **Landing point:** The ball centre falls 0.73 m, from z = 0.78 to resting on the bucket floor at z = 0.05. That takes about 0.386 s, which carries it 1.555 × 0.386 ≈ 0.60 m past the edge, so it lands at the bucket's centre.
- **Clearing the edge:** v²/r ≈ 80 m/s², which is greater than g. So the ball leaves the table edge cleanly instead of pivoting around it.
- **Clearing the rim:** At the near wall (x ≈ 0.43 m), the bottom of the ball is at z ≈ 0.34. The rim is at 0.27, so the ball clears it.
- **Coming to rest:** Rolling and torsional friction on the bucket floor (0.02) slow the ball at about 4.7 m/s². After at most one bounce off the far wall, it stops well before 6 s.
- **Table friction:** The table contact uses condim 3, so there is no rolling resistance there. The ball keeps its speed until it reaches the edge.

---
thinking (summarized):

I'm working out the physics of a ball rolling off a table and landing in a bucket positioned 0.6 m beyond the edge, figuring out table height and launch velocity so the fall time and horizontal distance match up.

Ball center at 0.78 m, bucket floor contact around 0.05 m, giving a 0.73 m drop and a required launch speed of about 1.56 m/s to cover the 0.6 m gap. I'm also considering how the ball's rolling motion carries over as it leaves the table edge, since friction should preserve its rotation into the fall.

Checking clearance, the ball passes safely over the near rim and lands on the bucket floor before reaching the far wall, so it'll bounce around inside the bucket. Without rolling friction, the ball could keep oscillating back and forth off the walls, so I need to make sure it settles below 5 cm/s by 6 seconds through wall collisions and damping.

I'm estimating how much rolling resistance to add so the ball slows down naturally on the table before it even reaches the edge, working out the deceleration from a rolling-friction coefficient and the sphere's moment of inertia.

Since contact friction parameters combine by taking the max of the two geoms involved, I realize I can give the table zero rolling friction and the bucket floor a high rolling-friction value with higher condim, so the ball only decelerates once it lands in the bucket rather than on the table itself.

I'm checking that contact penetration stays small given the ball's speed and soft-contact timing, which seems fine. For the bucket geometry, I'm working out how to approximate a cylindrical rim using a ring of 12 boxes, sizing each box's radial thickness, tangential width, and height so they fit around the 0.16 m radius.

Computing box positions around the ring...

I'm checking clearance between the rim and ball placement, then moving to design the table: a flat top surface with four legs, positioning the ball to start resting on top of it.

Working through the bucket landing physics, I confirm the ball loses contact at the table edge and begins free-fall from x=0 with v≈1.555 m/s, giving angular velocity ω_y≈51.83 rad/s for forward rolling, and I'm verifying the sign convention via contact-point velocity (v plus ω cross the contact radius vector).

Now I'm setting up the free joint state for the ball: position and quaternion in qpos, linear and angular velocity in qvel, noting the bucket itself stays fixed so only the ball's six degrees of freedom matter. I still need to compute the ball's mass from its radius and density for completeness.

Checking whether the ball lands and settles within the bucket's inner radius, I estimate rolling deceleration from friction and find the ball travels roughly 0.26 m before stopping—farther than the 0.15 m to the bucket wall, so it bumps the wall around 1 m/s, bounces slightly, then comes to rest inside. That satisfies the landing tolerance.

Now I'm setting up the MuJoCo XML structure: naming floor, table, and ball bodies/geoms appropriately, confirming default contact and torsional friction settings are adequate, and wrapping the table geoms into a dedicated "table" body for clarity.

