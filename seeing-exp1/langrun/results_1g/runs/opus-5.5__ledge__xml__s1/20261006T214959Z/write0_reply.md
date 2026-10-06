The ball starts on the table already rolling at 1.67 m/s, set by the `start` keyframe with a matching spin so it does not slip. It leaves the table edge at x = 0 and falls about 0.36 s into a static bucket centred at x = 0.6 m. The bucket floor alone has rolling friction, so the ball settles there and does not roll around forever.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" size="0.6 0.4 0.02" pos="-0.6 0 0.73" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" size="0.025 0.025 0.355" pos="-1.15 0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" size="0.025 0.025 0.355" pos="-1.15 -0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" size="0.025 0.025 0.355" pos="-0.05 0.35 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" size="0.025 0.025 0.355" pos="-0.05 -0.35 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_floor" type="cylinder" size="0.17 0.01" pos="0 0 0.01" condim="6" friction="1 0.005 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" size="0.01 0.045 0.12" pos="0.16 0 0.14" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" size="0.01 0.045 0.12" pos="0.1386 0.08 0.14" euler="0 0 30" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" size="0.01 0.045 0.12" pos="0.08 0.1386 0.14" euler="0 0 60" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" size="0.01 0.045 0.12" pos="0 0.16 0.14" euler="0 0 90" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" size="0.01 0.045 0.12" pos="-0.08 0.1386 0.14" euler="0 0 120" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" size="0.01 0.045 0.12" pos="-0.1386 0.08 0.14" euler="0 0 150" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" size="0.01 0.045 0.12" pos="-0.16 0 0.14" euler="0 0 180" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" size="0.01 0.045 0.12" pos="-0.1386 -0.08 0.14" euler="0 0 210" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall8" type="box" size="0.01 0.045 0.12" pos="-0.08 -0.1386 0.14" euler="0 0 240" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall9" type="box" size="0.01 0.045 0.12" pos="0 -0.16 0.14" euler="0 0 270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall10" type="box" size="0.01 0.045 0.12" pos="0.08 -0.1386 0.14" euler="0 0 300" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall11" type="box" size="0.01 0.045 0.12" pos="0.1386 -0.08 0.14" euler="0 0 330" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.6 0 0.78">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.03" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.6 0 0.78 1 0 0 0" qvel="1.674 0 0 0 55.8 0"/>
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

I'm setting up the physical layout: table height around 0.75m, ball radius 0.03m, bucket positioned at x=0.6 with a rim height of about 0.25m, and working out the trajectory needed so the ball falls from the table edge into the bucket.

Computing the drop time and launch velocity needed to land the ball mid-depth in the bucket, I get roughly 1.67 m/s, then checking that at rim height and floor height the ball's x-position stays safely within the bucket's opening. Since the velocity is high enough that the ball leaves the table edge immediately rather than pivoting around it, I'm now setting the rolling angular velocity to match true rolling motion without slipping, around 55.8 rad/s.

I'm now worried that with zero rolling friction, once the ball settles into the bucket it'll just keep bouncing between the walls indefinitely instead of coming to rest within the simulation window, so I need to add some damping.

I think I'll give the ball a higher condim with a small rolling friction coefficient, and raise the bucket floor's friction values too, since MuJoCo combines contact friction by taking the max across the two geoms.

Checking the physics: with μ≈0.01 rolling friction and radius 0.03, deceleration works out to roughly 2.3 m/s², so the ball stops rolling within about a second—good. I'll keep the table and floor at default condim 3 so they don't apply rolling friction, and only set the bucket bottom to condim 6. Contact elasticity should be fine with default MuJoCo soft contacts.

Tracing the trajectory near the rim: at x=0.45 (t≈0.269s), the ball's height is about 0.425, well clear of the 0.25 rim height. Now I'm working out the bucket geometry—a bottom cylinder of radius 0.17 and the walls built from 12 boxes arranged in a polygon around a 0.15 inner radius, sizing each box's half-dimensions so they overlap properly at the 0.16 radius center with 0.25 height walls.

Computing the angular positions...

I'll keep the bucket body static since it's just resting on the floor, no joint needed. For the table, I'm sizing the tabletop as a box and adding four leg boxes positioned at the corners with appropriate half-dimensions and heights.

Now I'm checking the ball's starting position and trajectory — it begins slightly above the table edge, drops with gravity, and should land inside the bucket where friction settles its motion. I'm setting condim and friction values for the bucket floor and walls so the ball bounces, rolls, and eventually stops due to rolling and torsional friction.

I'll keep expected conditions to "ball touches table_top," "ball touches bucket_floor," and "ball comes to rest in bucket," skipping unrelated hoop-drop conditions. For the keyframe, I'm setting the ball's initial position and velocity (forward motion with spin) and adding a light source for the scene before finalizing the XML.

