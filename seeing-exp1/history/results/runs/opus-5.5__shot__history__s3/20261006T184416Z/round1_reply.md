**What happens in the run**

The ball leaves the floor at 9.84 m/s and climbs to a peak of 4.31 m at x = 2.30 m. Drag from the fluid model (`density="1.2"` with `fluidshape="ellipsoid"`) bleeds off its horizontal speed, from 3.21 down to about 2.14 m/s. The lift and Magnus terms in `fluidcoef`, acting on the −30 rad/s spin, also bend the path.

At 1.47 s the ball comes down through rim height at about x = 3.55 m. That is roughly 0.2 m in front of the rim's front edge, and it passes 0.18 m from `rim_07` without touching it. It never goes through the hoop. It hits the floor near x = 4.1 m, bounces once off the support base, and rolls back toward the start.

**Fix**

I removed the fluid model and the spin, so the flight is a plain parabola, and computed a launch that goes through the rim center:

- Launch velocity: vx = 3.013 m/s, vz = 8.719 m/s.
- Timing and peak: the ball reaches rim height (3.05 m) at x = 4.0 m after 1.33 s. It peaks near 3.99 m.
- Entry angle: it descends at about 55°, steeper than the roughly 32° a ball of this size needs to fit through an 18-inch rim.

Clearances along the path:

- **Rim:** the ball's center stays about 0.19 m from both the front and back rim tubes. That is more than the 0.127 m contact distance.
- **Bracket:** it clears the bracket by more than 0.06 m.
- **Backboard:** it passes under the backboard's lower edge before reaching x = 4.26 m.

The timestep drops the ball only about 1 cm below the ideal parabola, so these clearances still hold.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg, hollow shell inertia 2/3 m r^2 -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world. -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="0.9 0.3 0.05 1"/>

      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Ballistic shot: reaches rim plane (z = 3.05) at x = 4.0 after 1.33 s, descending at ~55 deg; apex ~3.99 m -->
    <key name="start" qvel="3.013 0 8.719 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The ball launches at 9.84 m/s and peaks at 4.31 m, but air drag and lift from the fluid model slow and bend its flight. It comes down through rim height at x≈3.55 m, about 0.2 m short of the front rim, passing 0.18 m from rim_07 without touching. It then hits the floor, bounces off the support base and rolls back toward the start. It never goes through the hoop.", "works": false, "problem": "The ball falls short of the hoop because the fluid drag and lift on the ball (density 1.2, ellipsoid fluid model, spin) were not accounted for in the launch velocity."}
```

---
thinking (summarized):

I'm tracking the ball's trajectory and realizing it missed the hoop — at 1.47s it passed 0.18m from rim_07, falling short due to significant drag effects slowing its horizontal velocity from 3.21 down to about 2.14. I'm checking whether it still passed near the hoop region at a later timestamp around 1.75s.

To fix this, I'll simplify by removing drag entirely (setting density to 0 and dropping the fluidshape) rather than tuning drag parameters, since I can't simulate iteratively. I'm working out the geometry for a clean shot: with rim inner radius 0.2286 and ball radius 0.1194, I need the descent angle steep enough — above about 31.5° — for the ball to fit through the opening, so I'm aiming for something around 50° and recalculating the ballistic path from the start position to the rim center.

I'm also checking whether the ball clears the backboard and support bracket after passing through the rim — tracing the ball's position as it continues forward and downward to see if it collides with the bracket structure sitting just under the rim.

I'm now estimating a steep descent angle around 55° so the ball clears the front rim edge before dropping toward the bracket, and setting up the horizontal and vertical motion equations to solve for the velocity components needed at that angle.

Apex height comes to about 3.99 m, which checks out. I'm also considering the small numerical error from discretization timesteps in MuJoCo's semi-implicit Euler integration — it's negligible, around 0.013 m. I'm also confirming the ball's initial position clears the floor properly, and starting to check clearance against the front rim tube near x=3.7.

Computing the distance from the ball's path to the front rim center, I get about 0.194 m, comfortably above the 0.127 m clearance needed — good. Now checking the back rim side of the hoop at the symmetric point to make sure the trajectory clears there too.

I'm parameterizing the parabola relative to the crossing point and sampling several nearby x-values to compute the distance to the rim corner, trying to find the closest approach point numerically.

Checking distances from the bracket corner at various x' points, they stay around 0.19-0.22, so clearance looks fine there too. Now I'm tracking the ball past the backboard as it continues its drop toward the floor, solving for the time to fall the remaining height using the vertical velocity at the rim.

I find it reaches the backboard's x-position with the ball's edge just clearing under the bottom of the board since the computed top of the ball is below the board's lower edge, so it passes safely underneath. Continuing the trajectory further, I check whether it collides with the support pole and find it does hit the pole, but only after already passing through the hoop, so that's not a problem for scoring purposes.

I decide to skip modeling fluid effects entirely, keeping density at default and omitting fluidshape/fluidcoef, while leaving solref as is. For angular velocity I consider adding backspin but conclude it's unnecessary since spin won't affect the flight without fluid drag, so I set it to zero for simplicity. I don't think a keyframe qpos is needed, and I settle on a qvel vector giving the ball forward and upward velocity components.

