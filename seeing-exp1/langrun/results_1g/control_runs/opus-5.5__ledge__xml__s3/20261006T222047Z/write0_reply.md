The table top is at z = 0.75 m and its edge at x = 0. The ball (r = 3 cm) is launched rolling at 1.555 m/s, so its fall from a centre height of 0.78 m to the bucket floor (centre at z = 0.05) carries it about 0.60 m beyond the edge. That puts the landing at the bucket's centre, x = 0.6. The bucket's floor has rolling friction so the ball stops inside it.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" pos="-0.5 0 0.73" size="0.5 0.3 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" pos="-0.95 0.25 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" pos="-0.95 -0.25 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" pos="-0.05 0.25 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" pos="-0.05 -0.25 0.355" size="0.025 0.025 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.2 0.01" condim="6" friction="1 0.02 0.02" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.19 0 0.11" euler="0 0 0" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1344 0.1344 0.11" euler="0 0 45" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.19 0.11" euler="0 0 90" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.1344 0.1344 0.11" euler="0 0 135" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.19 0 0.11" euler="0 0 180" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1344 -0.1344 0.11" euler="0 0 225" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.19 0.11" euler="0 0 270" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.1344 -0.1344 0.11" euler="0 0 315" size="0.01 0.08 0.1" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.8 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.8 0 0.78 1 0 0 0" qvel="1.555 0 0 0 51.83 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical setup: table height 0.75m, ball radius 0.03m rolling off the edge, with the bucket centered 0.6m beyond the table and needing to calculate the fall height from the ball's center to the bucket.

I calculate the fall time as roughly 0.386s giving a launch velocity near 1.56 m/s, then double-check the trajectory clears the bucket's rim before landing near its center. I decide to widen the bucket's inner radius to 0.18m for better margin and lower the wall height slightly, then move to setting up consistent rolling motion by relating the ball's linear velocity to its angular velocity so the contact point has zero slip.

With condim 3 and no rolling friction, the ball should maintain its speed as it rolls toward the table edge, and I check that it leaves the edge immediately rather than pivoting around it since the velocity-squared-to-gravity-radius ratio is well above 1. I note that for MuJoCo free joints, the angular velocity component of qvel is expressed in the body's local frame rather than world frame, which matters since the body starts in an identity orientation.

Now I'm thinking about what happens after the ball lands in the bucket—it'll hit with significant vertical velocity and some residual horizontal speed, bounce with default soft contacts and small restitution, then potentially roll back and forth between the bucket walls. Since there's no rolling friction, the ball could keep bouncing around without settling, so I'm considering adding rolling friction via condim="6" with a specific friction tuple, though that would also slow the ball down on the table before it reaches the edge, which isn't ideal.

I'll just make the bucket static on the floor, that's simplest. For the bucket walls, I'll approximate the cylindrical ring with 8 boxes arranged in an octagon, sizing each box's half-length and thickness based on the inner radius to keep them snug against each other.

Working through the bottom thickness and rim height, I'm recalculating when the ball crosses into the bucket opening and confirming its trajectory clears the rim before landing near the bottom. I'll place the wall boxes at 45-degree angle increments around the circle.

Now I'm setting up the table surface and leg geometry, positioning each leg box near the corners with enough clearance so the ball passes beyond the table edge before falling, and placing the ball's starting x-coordinate.

I'm working out the ball's keyframe state, giving it an initial velocity so it rolls across and off the table edge, checking that friction and contact softness won't meaningfully slow it before launch. After landing in the bucket, friction will handle killing its spin and settling it, so I'm setting condim 6 with appropriate friction on the bucket's bottom surface to ensure it stops rather than sliding around.

