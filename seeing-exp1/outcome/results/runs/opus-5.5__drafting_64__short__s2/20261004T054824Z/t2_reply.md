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
    <key name="shot" qvel="3.19 0 9.36 0 0 0"/>
    <!-- Changed qvel from "2.9532 0 8.556 0 0 0" to "3.19 0 9.36 0 0 0".
         Why: the old launch fell short. Even ignoring air, the ball came back down to rim height
         at about x = 3.77 m, which is on the front rim, and air drag pulled it shorter still.
         How: I hand-integrated the flight (midpoint steps of 0.1 s) with gravity and the scene's
         blunt drag. I assumed MuJoCo's drag force is C * rho * A * |v| * v with no factor of 1/2,
         giving 0.25 * 1.2 * 0.0448 / 0.62 ~= 0.0217 per metre.
         Result: the apex is about 4.15 m. The ball's centre comes down through rim height
         (3.05 m) near x ~= 4.0 m at about 1.37 s, falling at about 55 degrees. The ball's
         bottom clears the front rim by about 0.17 m.
         Uncertainty: if the drag actually includes a factor of 1/2, the ball would cross rim
         height roughly 0.15-0.2 m long. That is close to the ball's ~0.11 m clearance inside
         the rim, so it could touch the back rim. Simulating the shot would confirm.
         The ball has no sideways velocity and no spin, so there is no left/right drift. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to figure out the initial velocity so that, accounting for drag, the trajectory passes through the rim center while descending. I'm considering MuJoCo's fluid drag model, which combines blunt and slender drag coefficients based on projected area versus maximum cross-sectional area, scaled by air density and velocity squared.

For a sphere, the slender term vanishes since max area equals projected area. Working through the default blunt drag coefficient and radius, I estimate a drag constant k ≈ 0.0217/m. Then I set up the target displacement of 4m horizontally and 2.93m vertically, and start with a drag-free approximation to estimate launch velocity before correcting for drag, picking a trial flight time around 1.35s to compute initial velocity components.

Now I'm manually stepping through the trajectory with drag included, tracking how speed and vertical velocity decay over 0.3s intervals to approximate the perturbation effect on the drag-free path.

Integrating this via trapezoid rule across the time segments gives a total displacement deficit of about -0.348, so I'm tallying up these pieces to get the drag-induced shortfall in horizontal travel.

Now I'm computing the vertical acceleration contribution, combining the drag term with gravity over each timestep, then weighting by the remaining time (T-t) to build the numerator for the sensitivity integral.

Summing the trapezoid segments gives a rough estimate of roughly -0.67, though I note the trapezoid overestimates for a convex decaying function, so the true value is probably closer to -0.62. I'll estimate the overall position corrections as roughly Δz≈-0.64 and Δx≈-0.33.

To correct for these offsets, I'm computing first-order adjustments to the initial velocity components needed to compensate, factoring in that higher speeds will themselves increase drag and alter the effective flight time.

Rather than relying on approximations, I decide to just numerically integrate the trajectory for a candidate velocity using small time steps with a midpoint (RK2) method, tracking position and velocity under drag deceleration proportional to speed squared.

Continuing the integration through steps 3 and 4, updating position and velocity with drag decreasing as speed drops, now around x=0.94, z=2.29 and still iterating forward.

Continuing the step-by-step integration through steps 7 and 8, tracking velocity decay from drag and gravity as position climbs past x=2.14, z=3.86.

Continuing the step-by-step integration, I'm computing steps 10 and 11, updating velocity and position with drag-adjusted acceleration each time.

Continuing step14: z drops to 2.7886, past target 2.9306, so I need to find the crossing fraction within this interval to pinpoint when z actually hits 2.9306.

Solving the small quadratic gives τ≈0.07, placing x at roughly 4.069 when the ball crosses rim height — about 6.9 cm off center. Given rim inner radius 0.2286 and ball radius 0.1194, clearance is about 0.109, so it's within bounds but aiming for center is still ideal.

To center the shot I need to reduce vx slightly: with dx/dvx roughly 1.3-1.37, trimming vx by about 0.053 brings vx to roughly 3.19 while keeping vz at 9.36. I should also verify the ball clears the backboard (front face at 4.381, which it does) and check its position near the front rim at x=3.77.

Checking the ball's height when it's near the front rim, it's well clear of rim height, and after passing through there's no obstruction to worry about on the way down. I'm fairly confident in the drag coefficient formula (MuJoCo's blunt drag model without an extra 1/2 factor, default C_blunt=0.5), and the inertia calculation checks out with no spin needed, so I'll set the velocity to vx=3.19, vz=9.36.

