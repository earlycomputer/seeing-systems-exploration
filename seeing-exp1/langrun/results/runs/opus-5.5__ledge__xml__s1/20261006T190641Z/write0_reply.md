The ball rolls without slipping at 1.555 m/s along a 0.75 m high table and leaves the edge at x = 0. Ignoring drag, it falls about 0.39 s to the bucket floor and lands near x = 0.60 m, the bucket's centre. It clears the near rim with roughly 6 cm to spare.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" pos="-0.75 0 0.725" size="0.75 0.4 0.025" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" pos="-0.05 0.35 0.35" size="0.02 0.02 0.35" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" pos="-0.05 -0.35 0.35" size="0.02 0.02 0.35" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" pos="-1.45 0.35 0.35" size="0.02 0.02 0.35" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" pos="-1.45 -0.35 0.35" size="0.02 0.02 0.35" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="box" pos="0 0 0.005" size="0.16 0.16 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_px" type="box" pos="0.155 0 0.085" size="0.005 0.16 0.075" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_nx" type="box" pos="-0.155 0 0.085" size="0.005 0.16 0.075" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_py" type="box" pos="0 0.155 0.085" size="0.15 0.005 0.075" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_ny" type="box" pos="0 -0.155 0.085" size="0.15 0.005 0.075" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-1.0 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" friction="1 0.005 0.0001" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-1.0 0 0.78 1 0 0 0" qvel="1.555 0 0 0 51.833 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to work out the geometry: the ball rolls off the table edge with some velocity, becomes a projectile, and must land 0.6 m horizontally into the bucket, accounting for the ball's radius affecting the effective drop height and launch point.

Computing the fall times: dropping from the table surface at 0.78 to the bucket rim height takes about 0.32 s, requiring a launch speed near 1.88 m/s, but continuing the trajectory down to the bucket floor overshoots the inner radius slightly, so I need to tune the velocity to land more centrally rather than near the rim.

The ball's leftmost point sits at 0.514, well clear of the 0.45 wall, so keeping the inner half-width at 0.15 works fine rather than widening it. Checking the edge-release condition, with v²/(gr) coming out around 8, well above 1, the ball leaves the edge right as its center passes it, confirming the trajectory assumption holds.

For the rolling setup, I'm computing the ball's starting position resting on the table and deriving the angular velocity needed for pure rolling toward the edge, working out that ωy = v/r keeps the contact point stationary. Now I need to figure out how MuJoCo's free joint represents angular velocity components to set qvel correctly.

For the bucket, I'm deciding to keep it simple—building a static body from a bottom disc and a few wall boxes arranged in a square rather than a full cylindrical ring, placing it off to one side on the table and working out wall thickness and positioning so the ball can land inside.

I'm recomputing the landing trajectory with the updated bucket height, confirming the drop time and landing x-position still match up, and reasoning that default contact dynamics should give a reasonably believable bounce without extra tuning. I'm also sketching the table itself as a top slab with corner legs, making sure the legs sit far enough from the ball's path that they don't interfere with the drop.

Legs sit well behind the ball's starting position so there's no collision risk, and default friction should keep the ball rolling naturally without unwanted drift. I'm checking the bounce dynamics in the bucket—impact velocity from the drop height versus the default solver damping suggests minimal rebound, while the horizontal walls should contain the sideways motion. Now I'm writing the keyframe with the ball's position and velocity values.

