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
    <key name="shot" qvel="3.45 0 9.05 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from "2.9532 0 8.556 0 0 0" to "3.45 0 9.05 0 0 0".
       The old launch speed was solved without air. With density 1.2 and blunt drag 0.25 on the ball's
       ellipsoid fluid model, the drag is about k = 0.25*1.2*pi*0.1194^2/0.62 = 0.0217 per metre, roughly
       1 N at launch. That pulled the ball below rim height before the front rim, so it fell short under
       the hoop. Hand-integrating with this drag, the new velocity peaks near z = 3.86 m. The ball centre
       comes down through z = 3.05 m at about x = 3.99 m, descending at about 53 degrees. It clears the
       front rim by about 0.18 m and the back rim by about 0.19 m, against a needed 0.127 m. The ball
       still starts at rest on the floor at the origin, with no spin. -->
</mujoco>
```

---
thinking (summarized):

I need to figure out the velocity accounting for drag, recalling MuJoCo's ellipsoid fluid model where drag coefficients govern blunt, slender, and angular drag along with lift terms, and working out how the quadratic drag force applies to a sphere's projected area.

Estimating the drag constant k by computing cross-sectional area and dividing by mass, I get something in the range of 0.01-0.02 per meter, though the exact formula (with or without the 1/2 factor) is uncertain. I'm trying to use this to figure out how much the projectile's range shrinks compared to the no-drag case, aiming to roughly match a target landing position near the hoop by adjusting the launch velocity accordingly.

Settling on k≈0.0217 as the drag coefficient. Now I'm trying to find a launch velocity that lands through the rim at (4, 3.05) with a steep descending angle by trial, starting with vx=3.3, vz=8.7 and checking the no-drag apex and rim-crossing time against the target.

I'm manually stepping through the trajectory with drag using small time increments, computing speed-dependent acceleration at each step and updating velocity and position to see where the ball actually lands with air resistance factored in.

Continuing the numerical integration through t=0.6, tracking velocity decay and position updates as drag force diminishes with speed—vx stabilizing near 3.0 while vz drops rapidly as gravity dominates, with x and z positions steadily accumulating.

Continuing the trajectory to t=1.1, the ball apexes around z=3.6 but falls short of the rim crossing near x≈3.52 — the drag is too strong with these initial conditions. I need to boost the launch speed, trying something like vx=3.6, vz=9.4, to get the ball to reach x=4 at z=3.05.

Redoing the full numerical integration from t=0 with the new higher initial velocity, tracking drag-adjusted acceleration, velocity, and position at each 0.1s step through t=0.3, watching how the trajectory develops with the stronger drag coefficient from the higher speed.

Continuing the step-by-step integration, I see the projectile's height peaking around t=0.8 near z=4.13 before starting to descend, with horizontal distance steadily increasing past x=3.3 by t=0.9 as drag continues reducing velocity.

Tracking further steps, the trajectory keeps descending and crosses z=3.05 at roughly t=1.27, landing around x=4.48.

Interpolating between crossing points, I pick a target midpoint of x≈4.0 with vx≈3.45, vz≈9.05, but I'm wary of accumulated integration error from the coarse timestep and genuine uncertainty about the drag coefficient k—if it's actually half what I assumed, the shot would overshoot. Given the rim's tight clearance relative to the ball radius, I need to pin down MuJoCo's actual blunt-body drag formula to trust these numbers.

I recall the ellipsoid model uses force = -C_D,blunt·ρ·A_proj·|v|·v with no extra half factor since C_D,blunt already absorbs it, and with the default coefficient of 0.5 and projected sphere area, my computed k of about 0.02167 matches what I used—so the landing prediction should be sound. I also confirm linear viscosity defaults to zero and the inertia-based model isn't active here since fluidshape is set to ellipsoid.

Checking the added mass contribution for a sphere (half the fluid density times volume) gives roughly 0.0043 kg, which is negligible next to the object's mass of 0.62 kg, so I can ignore it.

Now I'm setting up the numerical integration with vx and vz components, using an Euler step with dt=0.1, acknowledging the drag is estimated using the velocity at the start of each interval which slightly overestimates drag early on but should be close enough—starting the first speed calculation now.

Stepping through the Euler integration, I'm computing speed, drag coefficient, acceleration, updated velocities and positions across t=0.1 and t=0.2, tracking how velocity and height evolve as drag decreases with speed.

Continuing the velocity integration through t=0.6 and t=0.7, drag keeps decreasing as speed drops, with vertical velocity settling toward terminal fall rate while horizontal position creeps forward to about x=2.588.

Continuing the trajectory through t=1.1 and t=1.2, the height keeps dropping as speed increases, and I find it crosses z=3.05 between these two points by interpolating the fraction where z passes that threshold.

Now I'm checking whether the ball actually clears the rim at this crossing point - computing the descent angle (about 53° from horizontal) and measuring the perpendicular distance from the trajectory line to the front rim's tube surface to confirm clearance.

Front rim gives about 0.184 m clearance versus the required 0.127 m radius, and the back rim gives about 0.193 m, so both pass comfortably given the small trajectory curvature and expected Euler integration error. The margin suggests the shot is reasonably centered with roughly ±0.07 m of slack in x, and I'm now checking whether the ball could clip the bracket or support base after passing through, but it looks like it stays clear of both since it's below those structures by the time it reaches them.

Tracking the fall further though, I'm now worried the ball's landing trajectory after passing z=2.906 might actually intersect the pole structure located at x=5.1 to 5.3 extending up to 3.4 m high — recomputing the time and x-position at that height to check for a collision there.

I also need to double-check whether the ball clears the backboard's bottom edge, comparing the ball's z-height and x-extent against the backboard bottom at z=2.9, x=4.381 to see if they overlap at the critical point.

Checking the bracket corner distance at the crossing point confirms clearance is fine, so I'll set the initial velocity to 3.45 along x and 9.05 along z with no rotation.

