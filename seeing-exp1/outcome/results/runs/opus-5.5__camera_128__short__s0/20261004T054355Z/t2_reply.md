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
    <key name="shot" qvel="3.27 0 8.79 0 0 0"/>
    <!-- Changed qvel from (2.9532, 0, 8.556) to (3.27, 0, 8.79), with y and spin still zero.
         The old launch came down through rim height (3.05 m) at x = 3.77 m even without air.
         That is right on the front rim, and drag (density 1.2, blunt coefficient 0.25,
         about 0.011*v^2 m/s^2) pulled it shorter still.
         First I set vx to 3.134 so the ball, ignoring air, crosses z = 3.05 on the way down
         at x = 4.0 (t = 1.276 s).
         I then estimated the drag losses along that path: about 0.16 m in x and 0.28 m in z.
         Adding about 0.136 m/s to vx and 0.236 m/s to vz makes up for these, including the
         slightly higher drag at the higher speed.
         The ball centre should now pass within a few cm of the rim centre, descending at
         about 53 degrees. At that angle it clears the front and back rim by about 0.06 m
         (perpendicular to its path), so it drops through. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for drag in my velocity estimates, using MuJoCo's ellipsoid fluid model with blunt drag coefficient 0.25 and projected area for a sphere of radius giving about 0.0448 m².

For the slender drag and Magnus/Kutta lift terms, these vanish for a sphere since there's no spin or area asymmetry, leaving just the blunt drag coefficient k≈0.01084 v². At launch speeds around 9 m/s, this gives a deceleration near 0.88 m/s², which is meaningful enough that I need to adjust my no-drag trajectory calculation to hit the hoop target, aiming for a steep descending angle around 55-60°.

Without drag, solving for the trajectory that passes through the hoop center at x=4, z=3.05 while descending gives vx≈3.134 with vz=8.556, for a speed near 9.112 m/s. Now I need to correct this for drag by roughly integrating the deceleration effect, estimating how much the horizontal distance falls short due to the velocity-squared drag term.

I'm sampling the no-drag trajectory at several time points to compute speed and drag deceleration along x, using these to estimate the correction to the straight-line path from drag forces.

Applying trapezoid integration to the x-deficit terms gives Δx≈-0.163, and now I'm doing the same weighted sum for the z-component terms to get Δz.

This puts the ball at approximately x≈3.837, z≈2.766 at T=1.276 with drag included, still descending, so I need a correction. Using linear sensitivity where small velocity changes scale roughly by T, I need about +0.163 in x and +0.284 in z to hit the target crossing point of x=4, z=3.05.

Computing δvx≈0.128 and δvz≈0.223 for first order, then adjusting for drag's quadratic dependence on speed—since drag increases slightly with higher velocity, I add a bit more: δvx≈0.136, δvz≈0.236, giving new launch velocities vx=3.270, vz=8.792. Now I need to check whether this trajectory stays within tolerance (0.11 m) at the rim height, considering the descent angle is roughly 53° with vz≈-3.96 and vx≈3.0, and whether the slanted path clears the front rim properly.

I'm working out the geometry of the front rim—its inner edge sits at x=3.7714, and I'm computing the perpendicular distance from the rim tube center to the ball's path line using the descent slope, finding a clearance distance of about 0.189 m.

Checking further trajectory, the ball might graze the support pole near x=5.1, but that shouldn't count as "landing" so it should still go in. I'm confident enough in the result now, so I'll settle on qvel="3.27 0 8.79 0 0 0".

