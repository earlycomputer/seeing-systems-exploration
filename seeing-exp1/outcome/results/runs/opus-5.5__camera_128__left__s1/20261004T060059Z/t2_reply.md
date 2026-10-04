```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002" density="1.2"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <!-- Lighting: main overhead directional light plus a softer fill spot above the hoop -->
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: circumference 0.75 m -> radius 0.1194 m, mass ~0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2" fluidshape="ellipsoid" fluidcoef="0.25 0.25 1.5 1.0 1.0"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world (no joint). -->
    <body name="hoop" pos="4 0 3.05">
      <!-- Rim: 16 capsule segments, inner diameter 0.4572 m (18 in), tube radius 0.008 m, tube-center radius 0.2366 m -->
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

      <!-- Bracket joining the back of the rim to the backboard face -->
      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <!-- Backboard: 1.80 x 1.05 m, 0.03 m thick; front face 0.15 m behind the rim's inner edge (x = 0.381); bottom edge 0.15 m below rim -->
      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <!-- Target square painted on the backboard front (thin, visual only) -->
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <!-- Support: floor plate, vertical pole behind the backboard, and horizontal arm to the backboard's back face (x = 4.411) -->
    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="shot" qvel="3.19778 0 9.3 0 0 0"/>
    <!-- Changed qvel y from 0.27977 to 0 m/s; x (3.19778) and z (9.3) are unchanged.
         Why: the sideways velocity carried the ball about 0.35 m to +y (left) by the time it reached
         the rim. To pass cleanly, the ball's centre must stay within about 0.11 m of the rim axis
         (inner radius 0.229 m minus ball radius 0.119 m).
         In x and z the arc already works. I stepped the trajectory by hand using the ball's blunt drag
         (k = 0.25*1.2*pi*0.1194^2/0.62, about 0.022 per metre). Results of that estimate:
         - apex about 4.1 m, near t = 0.9 s;
         - the ball centre descends through z = 3.05 at x of about 3.98 and t of about 1.36 s,
           falling at roughly 58 degrees;
         - the closest approach from the ball path to the front and back rim tubes is about 0.18 m
           and 0.22 m, both more than the 0.127 m (ball radius plus tube radius) needed to clear them.
         So with y = 0 the ball should drop through the hoop without touching the rim or the backboard. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Setting vertical velocity to zero, I'm checking whether the horizontal trajectory still crosses the hoop height near x=4, roughly matching my earlier estimate but with uncertainty about whether it clears the backboard. I want a more rigorous drag calculation using MuJoCo's ellipsoid fluid model to pin down the blunt drag force rather than relying on rough guesses.

Working through the math, I derive an effective drag coefficient k≈0.0217/mass, consistent with a real basketball's drag characteristics, with no slender-drag or Magnus contributions since the ball is a sphere without spin. I'm now running a step-by-step midpoint integration starting from vx=3.198, vz=9.3, computing accelerations from gravity plus drag at each 0.1s interval to trace out the ball's velocity and position over time.

Continuing the numerical integration, I step through t=0.3 and t=0.4, updating velocity and position components using half-step accelerations accounting for drag and gravity, tracking x and z positions as they accumulate toward roughly 1.23 and 2.94 respectively.

Continuing the RK2 integration steps through t=0.7-0.8, updating velocity and position values as drag and gravity decelerate the projectile.

Continuing the trajectory simulation, drag is increasing as velocity grows, pushing the projectile's horizontal position past 3.5 while altitude drops below 3.65 by t=1.2s.

With the altitude now dipping below 3.0 between t=1.3s (z≈3.296) and t=1.4s, I'm setting up to interpolate the exact crossing point at z=3.05 using the fractional time between these two steps.

Working out the interpolation gives x≈3.979, essentially centered on the rim within 0.02 — a clean approach. I'm now checking whether the steep descent angle (around 58° from horizontal) causes the ball to clip the front rim before reaching the hoop plane, computing the distance from the ball's position to the front rim point and confirming it clears by a comfortable margin (0.254 vs the 0.127 rim radius).

Checking the perpendicular distance from the ball's trajectory line to both front and back rim points confirms clearance in both cases (0.183 and 0.219, both exceeding the 0.127 threshold), so the shot should pass cleanly through without touching the rim. Now I'm tracking whether the ball's continued forward motion past the rim plane brings it close to the backboard at x=4.381.

I'll keep vx and vz as computed and just zero out vy, since the margins look acceptable given the rough drag model uncertainty.

