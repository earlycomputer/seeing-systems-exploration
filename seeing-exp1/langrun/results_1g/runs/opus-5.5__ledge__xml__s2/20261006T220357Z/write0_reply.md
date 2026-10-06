The table top is at 0.75 m and its edge is at x = 0. The ball starts rolling at 1.7 m/s with matching spin. Leaving the edge at that speed, it clears the near rim of a 15 cm-radius bucket centred at x = 0.6 m and lands on the bucket floor at about x = 0.66 m. The bucket floor has rolling friction so the ball settles inside.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" pos="-0.5 0 0.73" size="0.5 0.4 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" pos="-0.95 0.35 0.365" size="0.02 0.02 0.365" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" pos="-0.95 -0.35 0.365" size="0.02 0.02 0.365" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" pos="-0.05 0.35 0.365" size="0.02 0.02 0.365" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" pos="-0.05 -0.35 0.365" size="0.02 0.02 0.365" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_floor" type="cylinder" pos="0 0 0.005" size="0.17 0.005" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.155 0 0.135" euler="0 0 0" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1342 0.0775 0.135" euler="0 0 30" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0.0775 0.1342 0.135" euler="0 0 60" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="0 0.155 0.135" euler="0 0 90" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.0775 0.1342 0.135" euler="0 0 120" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1342 0.0775 0.135" euler="0 0 150" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="-0.155 0 0.135" euler="0 0 180" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="-0.1342 -0.0775 0.135" euler="0 0 210" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall8" type="box" pos="-0.0775 -0.1342 0.135" euler="0 0 240" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall9" type="box" pos="0 -0.155 0.135" euler="0 0 270" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall10" type="box" pos="0.0775 -0.1342 0.135" euler="0 0 300" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall11" type="box" pos="0.1342 -0.0775 0.135" euler="0 0 330" size="0.005 0.042 0.125" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.3 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.3 0 0.78 1 0 0 0" qvel="1.7 0 0 0 56.667 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches table_top
ball touches bucket_floor
ball comes to rest in bucket
```

---
thinking (summarized):

I'm setting up the physics scene: a table edge at height 0.75m, with a ball rolling off and landing in a bucket 0.6m away, accounting for the ball's radius of 0.03m in positioning its center.

Since the roll speed gives centripetal force far exceeding gravity, the ball leaves the edge essentially immediately rather than pivoting around it. For the bucket (height 0.25m, inner radius 0.12m), I'm calculating the fall times to reach rim height versus bucket floor, then solving for a launch velocity around 1.5 m/s that lands the ball near the bucket's center while clearing the rim on entry.

I settle on v=1.7 as a reasonable compromise between clearing the near rim and staying within the far wall, and decide to size the bucket with inner radius 0.15 and height 0.25. Now I'm working out the rolling kinematics on the table — setting the angular velocity consistent with pure rolling (ω = v/r) so the contact point has zero velocity relative to the floor.

I'm figuring out table dimensions and leg placement, then thinking through how the freejoint's qpos/qvel are structured — position and quaternion for qpos, linear plus local-frame angular velocity for qvel — so I can set up the keyframe for the ball's starting position correctly.

Now I'm designing the bucket itself: a fixed body with a cylindrical floor and walls made from a ring of angled boxes, working out the radius, wall thickness, height, and segment count needed so the box positions and rotation angles form a closed circular enclosure for the ball to settle into.

Good, that lands safely on the floor. But then I need to think about damping so the ball actually settles instead of bouncing endlessly between walls—without rolling friction it'll just keep rolling back and forth within the 5.6 second window. I'm considering adding a rolling friction coefficient to the ball's contact properties to decelerate it realistically.

Actually, a better approach is to apply the rolling friction specifically on the bucket floor geom rather than the ball, since MuJoCo combines contact friction by taking the max across both geoms. Setting the bucket floor to condim 6 with a small rolling friction value should decelerate the ball enough to stop within a second or two, while the table keeps default friction and condim 3 for normal behavior elsewhere.

Default MuJoCo contacts are mostly inelastic, so there shouldn't be meaningful bounce when the ball lands with roughly 3.8 m/s vertical velocity. I'm also checking that the ball leaves the table edge cleanly and setting a reasonable default density for the ball mass, then computing the twelve wall positions around the bucket circumference at 30-degree increments with radius 0.155 to place the wall segments correctly.

I'm also sizing the radial and tangential half-extents for each wall box and checking the table leg placements relative to the tabletop edges and width to make sure nothing collides improperly.

The leg under the table won't interfere since the ball's trajectory stays at x>0. For success conditions, I'll keep it simple: the ball should touch the table top, then land and rest in the bucket, touching the bucket floor. Lighting and visual details are optional extras I can add at the end.

