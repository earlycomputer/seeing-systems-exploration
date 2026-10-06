**What happened in the run**

- The motor swung the arm to its 45° stop in 0.17 s, at about 517°/s (9.0 rad/s), and the ball left the cup there.
- The release was flatter and slower than I planned. Working back from the flight data, the ball left at about (vx 3.64, vz 1.84) m/s, a 27° launch at 4.1 m/s. I had planned roughly 39° at 4.7 m/s.
- The ball peaked at z ≈ 0.98 m and hit the floor at about x = 2.45 m.
- It bounced into the outside of the bucket's near wall (`bucket_wall_06`, at x ≈ 2.69) and came to rest on the floor at x = 2.62 m, outside the bucket.

**Fix**

I scaled the motor torque from the measured release, assuming the launch stays near 27°.

- Hitting the bucket floor near x = 3.05 from the release point (0.19, 0.81) needs about 4.8 m/s at 27°.
- That is about 1.18× the measured speed, or about 1.38× the kinetic energy.
- After accounting for the losses seen in this run, that means raising the keyframe torque from 5.7 to about 7.2 N·m.

At that speed, my calculation has the ball's centre at z ≈ 0.39 m as it passes over the near rim, which leaves its underside clear of the 0.27 m wall. This assumes the launch angle stays close to 27° at the higher speed, which I haven't confirmed. Nothing else changes.

```json
{"what_happens": "The motor swings the arm to its 45° stop in 0.17 s and the ball is released at about 27° and 4.1 m/s, flatter and slower than planned. It peaks near 1 m, hits the floor at x≈2.45 m, bounces off the outside of the bucket's near wall and comes to rest on the floor at x=2.62 m, outside the bucket.", "works": false, "problem": "The release is too slow and too flat, so the ball lands about 0.5 m short of the bucket and ends up outside it."}
```

```xml
<mujoco model="catapult_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- static catapult frame -->
    <geom name="catapult_base" type="box" pos="0.5 0 0.02" size="0.3 0.2 0.02" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_l" type="box" pos="0.5 0.12 0.21" size="0.03 0.02 0.19" rgba="0.5 0.3 0.1 1"/>
    <geom name="catapult_post_r" type="box" pos="0.5 -0.12 0.21" size="0.03 0.02 0.19" rgba="0.5 0.3 0.1 1"/>

    <!-- throwing arm, pivot at (0.5, 0, 0.4); positive rotation about +y lifts the cup end -->
    <body name="catapult_arm" pos="0.5 0 0.4">
      <inertial pos="-0.26 0 0" mass="0.5" diaginertia="0.0003 0.015 0.015"/>
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-10 45" solreflimit="0.01 1" damping="0"/>
      <geom name="catapult_axle" type="cylinder" pos="0 0 0" euler="90 0 0" size="0.02 0.09" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_beam" type="box" pos="-0.26 0 0" size="0.30 0.03 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_base" type="box" pos="-0.5 0 0" size="0.06 0.062 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.552 0 0.03" size="0.01 0.062 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.455 0 0.018" size="0.01 0.062 0.008" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_side_l" type="box" pos="-0.5 0.052 0.03" size="0.06 0.01 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_side_r" type="box" pos="-0.5 -0.052 0.03" size="0.06 0.01 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <!-- bucket, centre 3 m from the ball's start (0,0,0.45) -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.32 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0.145" euler="0 0 0" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2685 0.155 0.145" euler="0 0 30" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.155 0.2685 0.145" euler="0 0 60" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.31 0.145" euler="0 0 90" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.155 0.2685 0.145" euler="0 0 120" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.2685 0.155 0.145" euler="0 0 150" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.31 0 0.145" euler="0 0 180" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2685 -0.155 0.145" euler="0 0 210" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.155 -0.2685 0.145" euler="0 0 240" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.31 0.145" euler="0 0 270" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.155 -0.2685 0.145" euler="0 0 300" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.2685 -0.155 0.145" euler="0 0 330" size="0.01 0.085 0.125" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- ball resting in the catapult cup -->
    <body name="ball" pos="0 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="0.8 0.01 0.01" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="7.2"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The ball landed short at x≈2.6, bouncing off the outside of wall 06 instead of going through, settling at 2.62. The arm speed was close to planned at 9.02 rad/s vs 9.3, but checking the launch angle more carefully—with vz around 1.8 and vx at 3.64 at release—suggests the trajectory was too shallow to clear the gap.

The actual release angle comes out to about 26°, way under the intended 39°, and speed is around 4.06 instead of 4.68. This gap is likely from the ball sliding along the outer lip during the deceleration phase when the arm overshoots its soft limit before settling back. I need roughly 0.6 m more range to hit the target, so I'm considering whether to increase the drive torque or adjust the limit angle to get more vertical launch component, since the outer lip contact seems to be flattening the trajectory compared to what a clean release would produce.

Checking the apex time confirms vz=0 at t≈0.363, with z-top at 0.98, and I verify the trajectory matches at τ=0.387 and τ=0.75. Back-tracking to release gives x≈0.186, z≈0.807, consistent with the planned release point, so the launch vector is vx=3.64, vz=1.84 — angle 26.8°, speed 4.08. I'm now tracing this back to the arm's angular speed of 9.02 rad/s to see what's driving it.

Expected speed is around 4.53 and velocity components (3.51, 2.87), but I got (3.64, 1.84), meaning vz is losing about 1 m/s somewhere. This could be from the arm overshooting to 46.7° or some contact softness during deceleration causing the ball to separate early — I'll set this aside and empirically try increasing torque while keeping the launch angle near 27°.

Working through the geometry, I calculate that reaching the target point from the current position requires a speed of about 4.80 m/s, a ratio of 1.176 over the current 4.08 m/s. That means the angular velocity needs to scale by 1.176, which translates to roughly 1.383x more kinetic energy needed — I'm now checking that against the current energy budget of about 3.015 J kinetic plus 1.234 J potential.

Accounting for torque losses, I'm refining the required torque to around 7.25, though I note the launch angle could shift with speed, making a steeper trajectory potentially more reliable. I check clearance at the rim with the new 26.8° angle and 4.80 m/s velocity — computing the ball's position at x=2.70 gives a height of 0.389, comfortably above the 0.27 wall, so that clears.

Now I'm thinking through the landing dynamics: the ball descends steeply, hits the bottom with a fast downward velocity around 4.39 m/s, then moves horizontally into the far wall at roughly 4 m/s. Given MuJoCo's fairly inelastic contacts, I expect the bounce back to be mild and the ball to settle quickly, similar to the prior run. I consider raising the wall height for safety, but that creates a conflict with clearance at x=2.70, so I'll keep it at 0.27 and look for another adjustment.

Checking sensitivity, a 3% speed variation shifts the range by about ±0.17, putting the landing zone between roughly 2.88 and 3.22 — close to the inner radius of 0.30, which seems acceptable near the rim. I'll aim for a landing point slightly nearer the center, around 3.0, and settle on τ=7.2, while noting the angle still carries some uncertainty and the ctrlrange of 0-10 is fine to keep as is.

