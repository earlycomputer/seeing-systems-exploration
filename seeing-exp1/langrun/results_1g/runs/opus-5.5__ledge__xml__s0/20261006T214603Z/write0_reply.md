The ball starts 40 cm from the table's edge, already rolling at 1.67 m/s. That speed carries it off the 75 cm high table into a 20 cm tall bucket centred 60 cm beyond the edge.

- **Flight path:** The ball's centre drops 0.55 m to reach rim level, which takes about 0.335 s, by which time it has travelled about 0.56 m. It reaches the floor of the bucket at about 0.645 m. The ball's centre can pass anywhere from 0.51 to 0.69 m inside the walls, so both points have room to spare.
- **Bucket floor:** It has rolling friction so the ball stops rolling and settles.
- **Table:** It keeps the default contact, so the ball keeps its speed on the way to the edge.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" pos="-0.5 0 0.73" size="0.5 0.3 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" pos="-0.95 0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" pos="-0.95 -0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" pos="-0.05 0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" pos="-0.05 -0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="ball" pos="-0.4 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.14 0.01" condim="6" friction="1 0.005 0.01" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.13 0 0.11" euler="0 0 0" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.0919 0.0919 0.11" euler="0 0 45" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.13 0.11" euler="0 0 90" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.0919 0.0919 0.11" euler="0 0 135" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.13 0 0.11" euler="0 0 180" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.0919 -0.0919 0.11" euler="0 0 225" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.13 0.11" euler="0 0 270" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.0919 -0.0919 0.11" euler="0 0 315" size="0.01 0.06 0.09" rgba="0.2 0.3 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.4 0 0.78 1 0 0 0" qvel="1.67 0 0 0 55.7 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches table_top
ball touches bucket_bottom
ball comes to rest in bucket
```

---
thinking (summarized):

I'm setting up the physical scene: a table edge at height 0.75m, a ball of radius 0.03m rolling off and launching as a projectile, with a bucket placed 60cm away on the floor to catch it.

I work through the arc time and horizontal distance so the ball passes through the bucket's rim opening and lands near the bottom, solving for a launch speed around 1.67 m/s. I settle on a bucket wall height of 0.2m, giving a fall time of about 0.344s and a landing point around x=0.574, which keeps the ball comfortably within the bucket's inner radius.

I then figure out the rolling kinematics: matching angular velocity to linear velocity via ω_y = v_x/r gives roughly 55.6 rad/s, and I place the ball starting at x=-0.4 on the table so it rolls for about 0.24s before reaching the edge, with friction negligible under the default contact settings.

Once it drops into the bucket, I think through the bounce dynamics — default soft contacts should limit bounce, but the ball could keep rolling indefinitely inside without added resistance. I consider adding rolling friction via a condim 6 setup with small torque-based friction values to let it eventually settle.

Setting bucket bottom friction with rolling coefficient around 0.01 gives faster deceleration so the ball settles quickly, which works well. I also want to check the vertical drop velocity onto the bucket floor is reasonable and that the bucket itself can simply be a static body welded to the world rather than needing a freejoint, since it's resting on the floor anyway.

Now I'm working out the octagonal wall layout for the bucket — placing eight angled boxes around an inner radius to form the sides, sizing their half-lengths for overlap, and positioning each at the right height and rotation angle to close the shape.

I'm also checking the ball's trajectory as it falls into the bucket, verifying it clears the rim and lands within the bottom area with reasonable margin at each stage of the fall.

Now I'm working out the table geometry — the tabletop slab dimensions and leg placements, positioning them so the legs reach from the floor to just under the top surface, and checking whether the ball's path might intersect the legs on its way down.

The ball starts at x=-0.4, z=0.78 with small mass, sitting above the static table body. I expect the simulation to log events like the ball touching the table top and then coming to rest in the bucket, with the default contact solver parameters preventing any noticeable bounce.

I'm setting the keyframe with initial position and velocity so the ball rolls forward, hits the bottom near the far wall, and settles due to friction, then finishing with a light source and floor sizing for the scene.

