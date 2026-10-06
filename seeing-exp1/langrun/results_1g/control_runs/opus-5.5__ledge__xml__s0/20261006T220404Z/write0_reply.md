The ball starts 0.4 m from the table's edge, rolling at 1.6 m/s. It falls about 0.73 m to the bucket floor, which takes about 0.39 s, so it lands about 0.62 m beyond the edge. That is near the centre of the bucket, which sits 0.60 m out with a 0.15 m inner radius. The bucket floor has high rolling friction so the ball comes to rest there.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Table: top surface at z = 0.75, edge at x = 0 -->
    <geom name="table_top" type="box" pos="-0.5 0 0.73" size="0.5 0.4 0.02" friction="0.8 0.005 0.0001" condim="6" rgba="0.6 0.4 0.2 1"/>
    <geom name="table_leg1" type="box" pos="-0.05 0.35 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
    <geom name="table_leg2" type="box" pos="-0.05 -0.35 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
    <geom name="table_leg3" type="box" pos="-0.95 0.35 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
    <geom name="table_leg4" type="box" pos="-0.95 -0.35 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>

    <!-- Bucket: centre 0.6 m beyond the table edge, inner radius 0.15, rim at 0.27 -->
    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.17 0.01" friction="1 0.05 0.03" condim="6" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.155 0 0.135" euler="0 0 0" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1096 0.1096 0.135" euler="0 0 45" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.155 0.135" euler="0 0 90" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.1096 0.1096 0.135" euler="0 0 135" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.155 0 0.135" euler="0 0 180" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1096 -0.1096 0.135" euler="0 0 225" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.155 0.135" euler="0 0 270" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.1096 -0.1096 0.135" euler="0 0 315" size="0.005 0.068 0.135" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- Ball: radius 0.03, resting on the table top -->
    <body name="ball" pos="-0.4 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" friction="0.8 0.005 0.0001" condim="6" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.4 0 0.78 1 0 0 0" qvel="1.6 0 0 0 53.333 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics for a ball rolling off a table and landing in a bucket: calculating the fall time based on table height and gravity, then setting the ball's horizontal velocity so the travel distance matches the bucket's 0.6 m offset from the edge.

I'm checking that the ball clears the bucket's rim height and inner radius without clipping the wall, verifying it leaves the table edge cleanly since its centripetal acceleration exceeds gravity at that speed. I still need to account for how MuJoCo's contact physics will handle the ball settling once it lands inside the bucket.

Since a flat-bottom bucket gives no natural rolling friction, I'm adding a small rolling friction coefficient via condim 6 so the ball eventually stops instead of oscillating forever, estimating the deceleration from the torque balance for a solid sphere comes out to roughly 0.12 m/s².

With mu=0.0005, the ball would take way too long to settle in the bucket since collisions with walls are the real dissipation mechanism. I'm considering giving the bucket floor geom its own higher rolling friction coefficient (since contact friction parameters combine by taking the max between geoms), while keeping the table's rolling friction low so the ball still travels well before falling off — working out that a bucket floor friction of 0.02 gives a deceleration around 4.7 m/s², which would settle the ball quickly once it's inside.

For the keyframe, I'll set the ball's initial velocity and matching angular velocity for rolling, starting it a bit before the table edge; with the table's very low rolling friction, the speed loss over that distance is negligible, keeping it near the target 1.56 m/s. I also need to account for the ball hitting the bucket floor at a decent vertical speed, where default contact solver parameters should keep the bounce small.

With density 1000 the ball comes out around 0.113 kg, fine. For the table I'm setting up a static top box plus leg boxes at the right height, and for the bucket I'm placing a cylindrical bottom with wall boxes arranged around it, considering whether a square or octagonal arrangement looks more like a bucket.

Now I'm working out the octagon wall geometry—apothem, side length, wall thickness and height—and cross-checking that the rim height and position will actually catch the ball given its projectile trajectory from the earlier velocity calculation.

I'm recalculating with v=1.6, giving the ball center landing around x=0.617 at the bucket floor and clearing the near wall at x=0.501 when passing z=0.30, with good clearance from the far wall too. I'm also considering whether the bucket itself should be a dynamic rigid body or just treated as a fixed static structure sitting on the floor.

For the octagon walls, I'm computing the eight positions around a circle of radius 0.155 at 45-degree intervals, using thin angled box geoms rotated to match each wall segment's orientation.

Bumping the ball's condim to 6 to match the walls, and setting its initial keyframe at x=-0.4, z=0.78 with a forward velocity of 1.6 m/s and angular velocity of about 53.3 rad/s so it lands in the bucket and settles to rest well before the 6-second mark.

Now I'm finishing up the scene geometry - sizing the floor plane, adding four leg boxes for the table, placing a light source, and writing out the final model.

