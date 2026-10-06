**What happened in the run**

- **Launch.** The motor swung the arm to its 40° stop in 0.15 s, arriving at 9.46 rad/s (542°/s).
- **Bad release.** The ball left at about 4.0 m/s and only about 27° above horizontal. It should have been about 4.8 m/s at 44°.
  - Back-tracking from the 0.25 s state puts the release point where intended, so only the velocity was wrong.
  - Compared with the arm-tip velocity, the ball lost about 1 m/s perpendicular to the arm.
  - It also gained about 1 m/s directed back toward the hinge.
- **Landing.** It peaked at only 0.85 m and landed on the floor at x ≈ 2.3 m. It rolled into the bucket's near outside wall and stopped outside it at x = 2.64 m.

**Likely cause**

My best explanation is the outer cup wall. During the swing the ball sinks into it under centripetal load, about 2.2 N against fairly soft contacts. At release that wall contact springs back and kicks the ball toward the hinge. Its 0.8 friction also drags on the ball as it slides up the wall face. I haven't confirmed this. The beam contact springing back could also contribute.

**Fixes in the corrected file**

- **Frictionless, stiff cup walls.** The cup walls now touch the ball only through explicit frictionless contact pairs with stiff contacts. This removes the friction drag and shrinks the spring-back.
- **Stiffer beam contact.** The beam contact is also an explicit, stiffer pair, still with friction.
- **More torque.** I raised the motor torque from 5.51 to 5.65 N·m. The arm reached the stop about 2% slower than calculated, and the extra torque should bring the release up to the 4.85 m/s the aim needs.

```json
{"what_happens": "The motor swings the arm to its 40° stop in 0.15 s, but the ball leaves at only ~4.0 m/s and ~27° elevation instead of ~4.8 m/s at 44°. It flies to a 0.85 m peak, lands on the floor at x≈2.3 m, rolls into the outside of the bucket's near wall and stops at x=2.64 m, outside the bucket.", "works": false, "problem": "The ball is mis-launched (too flat and too slow), most likely by the frictional, soft outer cup wall kicking it toward the hinge and dragging on it at release, so it falls short of the bucket."}
```

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" pos="0.35 0 0.025" size="0.4 0.18 0.025" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_upright_left" type="box" pos="0.5 0.12 0.185" size="0.02 0.015 0.135" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_upright_right" type="box" pos="0.5 -0.12 0.185" size="0.02 0.015 0.135" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" pos="0.5 0 0.3" euler="90 0 0" size="0.012 0.135" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="catapult_stop_post_left" type="box" pos="0.331 0.12 0.27" size="0.015 0.015 0.22" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_stop_post_right" type="box" pos="0.331 -0.12 0.27" size="0.015 0.015 0.22" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_stop_bar" type="cylinder" pos="0.331 0 0.4875" euler="90 0 0" size="0.02 0.135" contype="0" conaffinity="0" rgba="0.6 0.1 0.1 1"/>
    </body>

    <body name="catapult_arm" pos="0.5 0 0.3">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 40" limited="true" solreflimit="0.005 1"/>
      <geom name="catapult_arm_beam" type="box" pos="-0.275 0 0" size="0.275 0.03 0.015" mass="0.3" contype="0" conaffinity="0" rgba="0.6 0.45 0.25 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.55 0 0.045" size="0.01 0.065 0.03" mass="0.02" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.44 0 0.045" size="0.01 0.065 0.03" mass="0.02" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_side_left" type="box" pos="-0.495 0.055 0.045" size="0.045 0.01 0.03" mass="0.02" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="catapult_cup_side_right" type="box" pos="-0.495 -0.055 0.045" size="0.045 0.01 0.03" mass="0.02" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.355">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.05" condim="6" friction="0.8 0.005 0.002" solref="0.005 1" rgba="0.9 0.2 0.1 1"/>
    </body>

    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 -0.03" size="0.3 0.05" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.29 0 0.17" euler="0 0 0" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2511 0.145 0.17" euler="0 0 30" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.145 0.2511 0.17" euler="0 0 60" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.29 0.17" euler="0 0 90" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.145 0.2511 0.17" euler="0 0 120" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.2511 0.145 0.17" euler="0 0 150" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.29 0 0.17" euler="0 0 180" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2511 -0.145 0.17" euler="0 0 210" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.145 -0.2511 0.17" euler="0 0 240" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.29 0.17" euler="0 0 270" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.145 -0.2511 0.17" euler="0 0 300" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.2511 -0.145 0.17" euler="0 0 330" size="0.01 0.08 0.15" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="pair_ball_beam" geom1="ball" geom2="catapult_arm_beam" condim="3" friction="0.8 0.8 0.005 0.0001 0.0001" solref="0.004 1"/>
    <pair name="pair_ball_cup_outer" geom1="ball" geom2="catapult_cup_outer" condim="1" solref="0.004 1"/>
    <pair name="pair_ball_cup_inner" geom1="ball" geom2="catapult_cup_inner" condim="1" solref="0.004 1"/>
    <pair name="pair_ball_cup_left" geom1="ball" geom2="catapult_cup_side_left" condim="1" solref="0.004 1"/>
    <pair name="pair_ball_cup_right" geom1="ball" geom2="catapult_cup_side_right" condim="1" solref="0.004 1"/>
  </contact>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="5.65"/>
  </keyframe>
</mujoco>
```

```expect
catapult_arm reaches its upper stop
ball touches bucket
ball comes to rest in bucket
```

---
thinking (summarized):

Checking the arm stop speed against expectations, I find it close at 9.46 rad/s versus 9.64. But backtracking the ball's velocity at release from the 0.25s sample gives roughly (3.58, 1.83) m/s, an elevation of 27° and speed 4.02 m/s—falling short of the expected (3.51, 3.35), suggesting the vertical component is off.

I'm puzzled why vx matches but vz is deficient by about 1.5 m/s. I consider whether the ball stayed in contact with the arm or wall longer than expected, possibly with friction along the local z-direction reducing velocity—but that would affect both components proportionally, not matching the asymmetric deficit I'm seeing. I'm now looking at whether the ball lagged behind the arm during the swing, checking the peak height of 0.85m at x=0.83 for clues.

Back-propagating from the release position at (0.52, 0.81) by 0.1s, I get an estimated release point near (0.152, 0.663), which lines up reasonably with expectations—so the position seems right, but the velocity angle is off, coming out around 27° instead of the expected 44°. Comparing components: expected velocity is about (3.44, 3.29) but actual is (3.58, 1.83), giving a difference of (0.14, -1.46). When I decompose this along the local beam axes—normal direction (0.643, 0.766) and the direction toward the hinge (0.766, -0.643)—the normal component comes out to about 3.70 versus an ideal of 4.73, suggesting the discrepancy is concentrated along the beam's normal direction rather than spread evenly.

The tangential component toward the hinge jumps from an expected ~0.52 to an actual ~1.57, meaning the ball picked up roughly 1 m/s toward the hinge while losing about 1 m/s in the normal direction. This pattern suggests something like rolling contact or spin effects—possibly the ball is pressed into the outer wall by centripetal force with deep soft-contact penetration, and when released, the contact spring pushes it inward toward the hinge, or friction with the beam surface during deceleration is imparting this extra tangential velocity.

I'm estimating the centripetal force at about 2.24 N, then trying to work out the contact stiffness from the solver reference parameters to figure out how much penetration depth that would cause.

Then I consider friction along the outer wall: as the normal force decays over roughly 12ms, friction at 0.8 times normal could produce a tangential impulse that decelerates and spins the ball by something like 0.8 m/s.

That roughly matches the observed 1 m/s inward gain with equivalent normal loss, though rolling instead of sliding would change the spin-induced reduction. But the magnitude still seems off given the arm's small 0.5° overshoot, since deceleration of the arm's rotation shouldn't itself push the ball inward through the outer wall.

Rather than chase the friction math further, I should just address the root cause: either make the cup walls frictionless or use an explicit contact pair between the ball and the outer wall with zero friction, since MuJoCo normally takes the max friction of the two contacting geoms.

Alternatively, I could just redesign the cup geometry or simply retune the torque empirically against whatever launch result the simulation actually produces, rather than trying to perfectly model friction effects.

With frictionless pair contact and a stiffer solref, penetration and the resulting velocity error should shrink roughly proportional to the time constant, so the release velocity should land closer to ideal. There's also friction between the ball and beam surface during the swing, which should prevent the ball from sliding outward along the beam before release, and I need to double check whether the outer wall geom is really the one releasing the ball at that same 0.15s mark.

This gives 4.76 m/s versus the needed 4.85, about 0.1 m short given the sensitivity of ~1.18 m per m/s. The shortfall suggests either extra losses or a slightly larger effective inertia than modeled, so I need to bump up the driving torque or reduce friction losses slightly to close that 2% gap and hit the target angular velocity of 9.64 rad/s.

Given uncertainty about where exactly losses come from (soft contact compression, ball offset, or sampling timing at the upper stop), I'll just settle on a torque of 5.65 as a reasonable compromise rather than over-fitting. I'm also double-checking the bucket geometry and release speed don't need further adjustment.

For contact pair definitions, I'm setting the outer cup wall as frictionless while the beam pair uses friction with solver reference parameters for stability, with beam/wall geoms excluded from standard collision affinity. I'm now reconsidering whether a frictionless outer wall could let the ball roll along the beam during the swing, since the beam friction alone might not properly resist the centripetal radial force while the ball is held between the beam and outer wall.

