## What happened in the run

The arm swings up and hits its 40° stop at 0.16 s, turning at about 503°/s. That is close to the 513°/s I planned. The ball, however, leaves the cup more slowly than planned and on a flatter path.

Working back from the logged state, the ball left the cup at about 4.24 m/s, 33.6° above horizontal. I had planned 4.95 m/s at 45°. The log suggests the ball slipped inward along the arm by about 1.2 m/s at release, which steals forward speed and lowers the launch angle.

The ball peaks at 1.08 m. At 0.84 s it clips the outside of the bucket's near wall (`bucket_wall_180`, at x ≈ 2.65). It then drops to the floor outside the bucket and rolls to rest at x = 2.17 m. So it comes to rest, but short of the bucket.

## The fix

I assumed the release velocity scales with the arm's speed while keeping the 33.6° direction this run showed, but that is not certain at higher speed. I left the release geometry alone and only changed the motor torque.

- **Required speed:** to land the ball's centre about 0.45 m up at x = 3 m, the release point (0.16, 0.80) needs a horizontal speed of about 4.2 m/s. That is 1.19 times the 3.53 m/s observed.
- **Energy:** the kinetic energy must rise by 1.19² ≈ 1.42 times. The gravity work while the arm turns 40° stays the same.
- **New torque:** this gives a motor torque of about 7.40 N·m, up from 5.63.

```json
{"what_happens": "The motor swings the arm to its 40° stop in 0.16 s and the ball is flung off at about 4.2 m/s, 34° up. It peaks at 1.08 m, clips the outside of the bucket's near wall at 0.84 s, falls to the floor outside the bucket and rolls to rest at x = 2.17 m, short of the bucket centred at x = 3 m.", "works": false, "problem": "The ball leaves the cup slower and flatter than planned, so it falls short and lands outside the bucket."}
```

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" pos="0 0 0" rgba="0.8 0.85 0.8 1"/>

    <!-- catapult frame (visual only, non-colliding) -->
    <geom name="catapult_base" type="box" pos="0.55 0 0.02" size="0.3 0.15 0.02" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_post_left" type="box" pos="0.55 0.09 0.2" size="0.02 0.02 0.2" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_post_right" type="box" pos="0.55 -0.09 0.2" size="0.02 0.02 0.2" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0.55 -0.11 0.4 0.55 0.11 0.4" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- throwing arm: pivot at (0.55,0,0.4), arm extends along local -x, ball sits on local +z face -->
    <body name="catapult_arm" pos="0.55 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="-5 40"/>
      <geom name="catapult_arm" type="box" pos="-0.3 0 0" size="0.3 0.04 0.01" mass="0.3" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_wall" type="box" pos="-0.595 0 0.04" size="0.005 0.04 0.03" mass="0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <!-- ball resting in the cup -->
    <body name="ball" pos="0 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.01 0.01" solref="0.005 1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <!-- bucket: octagonal tub, centre 3 m from ball start -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_floor" type="cylinder" pos="0 0 0.02" size="0.39 0.02" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_0" type="box" pos="0.37 0 0.19" size="0.02 0.163 0.19" euler="0 0 0" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_45" type="box" pos="0.26163 0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 45" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_90" type="box" pos="0 0.37 0.19" size="0.02 0.163 0.19" euler="0 0 90" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_135" type="box" pos="-0.26163 0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 135" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_180" type="box" pos="-0.37 0 0.19" size="0.02 0.163 0.19" euler="0 0 180" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_225" type="box" pos="-0.26163 -0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 225" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_270" type="box" pos="0 -0.37 0.19" size="0.02 0.163 0.19" euler="0 0 270" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
      <geom name="bucket_wall_315" type="box" pos="0.26163 -0.26163 0.19" size="0.02 0.163 0.19" euler="0 0 315" solref="0.005 1" rgba="0.2 0.3 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="7.40"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The ball came up short, hitting the near wall and landing at 2.17 instead of the target. Release speed came out around 4.24 at roughly 33.5°, well below the planned 4.95 at 45°, even though the arm's angular velocity of 8.78 rad/s was close to the intended 8.95 — so the shortfall seems to be more about release angle and timing than arm speed itself.

Decomposing the velocity along and perpendicular to the arm, the ball has an unexpectedly large component moving back toward the pivot and less speed along the arm's swing direction than planned. That points to the ball not leaving cleanly at peak arm speed — possibly some give in the contact during the arm's deceleration, where the ball stays pressed against the face a bit longer and bleeds off swing-direction speed while picking up inward motion toward the pivot.

Given the complexity of modeling this precisely, I think the pragmatic approach is to empirically scale: keep the observed release direction (~33.5°) and scale the required launch speed/torque based on that, rather than trying to perfectly predict the contact-release physics.

Solving for required horizontal velocity to hit the target at x=3, z=0.45 gives vx≈4.205, meaning the velocity needs to scale up by about 1.191× from the baseline, which translates to roughly 1.42× more kinetic energy. I need to account for the fact that the actual arm speed (8.78) was slightly below the predicted (8.95), so I'm adjusting the required torque-work calculation using that ratio to find the energy needed to hit the target precisely.

Given the bucket has about ±0.35 m of margin, I'm now checking how sensitive the range is to the launch angle, since a lower angle than planned could shift where the ball lands.

I should keep the release mechanics consistent rather than altering friction, so the empirical scaling stays valid. Checking the trajectory near the wall, I estimate the ball's descent is steep enough (around -0.91 slope) that it clears the top of the wall with margin around 0.80 m clearance before continuing down toward the floor.

The ball then continues to roughly x=3.37 near the far wall at low height before bouncing back with low restitution, which seems fine for the run. With τ=7.40 and ctrlrange 0-10, everything's within acceptable bounds.

