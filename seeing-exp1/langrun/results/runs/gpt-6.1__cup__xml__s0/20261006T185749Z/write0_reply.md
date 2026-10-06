```xml
<mujoco model="ball_rolls_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size njmax="500" nconmax="100"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
    <rgba haze="0.85 0.9 0.95 1"/>
  </visual>

  <worldbody>
    <light name="main_light" pos="-1 -2 4" dir="0.2 0.3 -1" directional="true"/>
    <camera name="overview" pos="0 -4.3 2.8" xyaxes="1 0 0 0 0.487 0.873" fovy="50"/>

    <geom name="floor" type="plane" pos="0 0 0" size="4 3 0.1" rgba="0.83 0.86 0.89 1" friction="0.8 0.005 0.001"/>

    <body name="ramp">
      <geom name="ramp_deck" type="box" pos="-0.912649 0 0.812053" euler="0 18.434949 0" size="0.948683 0.24 0.04" rgba="0.38 0.55 0.68 1" condim="3" friction="0.7 0.003 0.0001" solref="0.015 1" solimp="0.95 0.99 0.001"/>
      <geom name="ramp_rail_left" type="box" pos="-0.888932 0.225 0.883204" euler="0 18.434949 0" size="0.948683 0.015 0.035" rgba="0.25 0.38 0.49 1" condim="3" friction="0.7 0.003 0.0001"/>
      <geom name="ramp_rail_right" type="box" pos="-0.888932 -0.225 0.883204" euler="0 18.434949 0" size="0.948683 0.015 0.035" rgba="0.25 0.38 0.49 1" condim="3" friction="0.7 0.003 0.0001"/>
      <geom name="ramp_support_high" type="box" pos="-1.65 0 0.5" size="0.04 0.18 0.5" rgba="0.3 0.34 0.38 1"/>
      <geom name="ramp_support_low" type="box" pos="-0.15 0 0.24" size="0.04 0.18 0.24" rgba="0.3 0.34 0.38 1"/>
    </body>

    <body name="cup" pos="0.75 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.03" size="0.75 0.5 0.03" rgba="0.76 0.48 0.24 1" condim="6" friction="1 0.02 0.035" solref="0.015 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_wall_entry" type="box" pos="-0.71 0 0.27" size="0.04 0.5 0.21" rgba="0.88 0.61 0.32 1" condim="6" friction="1 0.02 0.035" solref="0.015 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_wall_far" type="box" pos="0.71 0 0.27" size="0.04 0.5 0.21" rgba="0.88 0.61 0.32 1" condim="6" friction="1 0.02 0.035" solref="0.015 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_wall_left" type="box" pos="0 0.46 0.27" size="0.67 0.04 0.21" rgba="0.88 0.61 0.32 1" condim="6" friction="1 0.02 0.035" solref="0.015 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.46 0.27" size="0.67 0.04 0.21" rgba="0.88 0.61 0.32 1" condim="6" friction="1 0.02 0.035" solref="0.015 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="-1.631026 0 1.156921">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.06" mass="0.12" rgba="0.9 0.16 0.1 1" condim="3" friction="0.7 0.003 0.0001" solref="0.015 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" time="0" qpos="-1.631026 0 1.156921 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Considering design for a scene**

I'm thinking about designing a scene where we need to verify that tools are functioning honestly. Right now, it seems we don’t have those tools available. We can reason through using robust geometry for a ramp leading to a cup. The ball should roll down the ramp and land in the cup after about 6 seconds. I'm considering the dimensions for a robust cup and ramp setup, including the incline and openings. It needs to be straightforward and effective!

**Designing ramp and cup setup**

I'm sketching out a ramp that extends from x = -1.8 to -0.05, with a height descent from 1.05 to 0.45. The ball will roll into the cup at x = 0.35, reaching a velocity of about 2.7. The cup should have a width of 1.0, with walls at a height of 0.4. I also need to ensure that the ball rolls smoothly down the ramp and doesn’t get stuck, considering factors like friction and rolling coefficients. It’s all about creating an effective setup!

**Refining ramp and cup design**

I’m considering using different configurations for the ramp and cup dimensions. I might go with a ramp of condition 3 and a sphere of condition 3, while the cup can be set to condition 6, which will help with rolling friction at around 0.03. The ramp’s slope should be 20 degrees, starting at a height of 1.0 and extending approximately 1.8. I’ll ensure there's enough clearance between the ramp's left end and the cup. It’s all about making sure everything fits and works smoothly!

**Calculating ramp and ball parameters**

I'm contemplating how to simplify the velocity calculations. The ramp length is about 1.897, with the ball at a relative height of -1.65—enough since the ramp's high side is 1.8. The top endpoints of the ramp match up nicely. The ball is landing at the bottom with coordinates x = .67 and z = .12. If I consider the cup's conditions, it rolls with a stopping distance of .035 within .6m. The total time is approximately 2.5. I'll make the cup bottom larger for consistency. Everything seems to check out!