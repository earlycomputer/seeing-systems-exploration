The shot was going long. It has to cross x = 4 m and then come back down to rim height there, so I lowered the launch speed. I worked the corrected flight out by hand, including the scene's air drag, and it has not been re-simulated in MuJoCo.

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
    <key name="shot" qvel="3.275 0 9.2 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from (3.5952, 0, 10.416) to (3.275, 0, 9.2).
       Why: the old launch was far too strong. It carried the ball about 2 m above the rim at x = 4 m,
       so it sailed over the backboard and landed long.
       How the new values were found: integrated the flight by hand, including the ellipsoid blunt drag
       (Cd 0.25, air density 1.2, ball area 0.0448 m^2, mass 0.62 kg, about 0.0217*|v|*v per unit mass).
       Expected flight: apex about 4.03 m near x = 2.7 m. The ball comes back down to rim height (3.05 m)
       at about t = 1.33 s, with its center about 0.01 m beyond the rim center. The descent angle there is
       about 55 degrees.
       Clearances: about 0.21 m from the front rim and about 0.18 m from the back rim, against 0.127 m
       needed to avoid touching. It also clears the bottom edge of the backboard by about 0.08 m.
       The y velocity stays 0 and there is no spin, so there is no sideways error or Magnus force.
       Not checked in MuJoCo: the result has not been re-run in simulation. -->
</mujoco>
```

---
thinking (summarized):

I need to find a launch velocity that carries the ball through the hoop while accounting for drag, moving from its start position to the hoop location while descending. I'm trying to recall MuJoCo's ellipsoid fluid model formula for blunt drag force, which depends on the drag coefficient, fluid density, and projected area times velocity squared.

Since the ball is a sphere, the slender drag term vanishes (max and projected area are equal), and with no spin the Magnus and Kutta lift terms also drop out, leaving just blunt drag as the dominant force. I'm checking whether added mass effects matter here, but computing it for a sphere gives a tiny value compared to the ball's mass, so it's negligible and I can ignore buoyancy and added-mass corrections.

I'm estimating buoyancy's contribution and finding it's only about 1.4% of gravity, small enough to ignore given the hoop's margin for error, then computing the drag coefficient k = CρA/m using the ball's cross-sectional area and mass to get a numeric decay rate for the trajectory.

Now I'm working out a flight strategy: pick a launch angle around 45°, estimate the vacuum trajectory parameters (horizontal and vertical displacement), then try a specific initial vertical velocity to see where the apex lands and how long it takes to fall back to rim height, planning to correct for drag afterward.

With drag at these speeds, the deceleration from air resistance is significant (around 1.75 m/s² at 9 m/s), so I need to actually integrate the motion numerically rather than rely on the vacuum approximation. I'm setting up to step through the trajectory by hand using small time increments, starting with a guess of initial horizontal and vertical velocities and refining from there.

I'm also checking whether MuJoCo's ellipsoid fluid model includes buoyancy — recalling that the inertia-box model does add a buoyancy term, but I believe the ellipsoid model only accounts for added mass and viscous resistance without buoyancy, so I'll leave that out of the calculation.

With viscosity set to zero by default there's no viscous drag term, so the blunt drag force reduces to the standard quadratic form with the drag coefficient times projected area times speed times velocity, no factor of one-half. Angular drag and added-mass gyroscopic terms vanish here since there's no spin, so for pure translation the added-mass contribution simplifies considerably.

I'll numerically integrate the trajectory using a midpoint RK2 scheme with a 0.1 timestep, starting from a guessed initial velocity around vx=3.5, vz=9.2, computing acceleration at the start, taking a half-step, evaluating acceleration at the midpoint, then updating position and velocity for the full step.

Continuing the RK2 integration, I compute drag and gravity accelerations at t=0.2s, then advance position to x2=0.68606, z2=1.72845, and start the midpoint calculation for the next step.

Continuing the RK4 integration, I compute v4 and update position to x4≈1.350, z4≈2.899 at t=0.4, then keep stepping through drag deceleration with midpoint estimates for the next interval.

Continuing the RK2 integration step by step, updating position and velocity values as drag and gravity forces evolve through each timestep.

Continuing the RK4 integration step, I get v9=(3.1315,-0.2194) with position x9=2.94605, z9=4.02966, then start the t=0.9 step computing new acceleration and midpoint values.

Continuing the step-by-step velocity and position integration through t=1.1, tracking drag deceleration as speed decreases and air resistance force updates each substep.

By x≈4, the ball is roughly 0.34 m above the rim, so I need to keep integrating forward to find exactly when z drops to rim height (3.05 m), recomputing speed and acceleration at t=1.2 to continue the trajectory.

Continuing the step to t=1.3 gives x≈4.18, z≈3.17, and extrapolating further, z reaches 3.05 around t≈1.327 with x≈4.26 — so I need to check whether that horizontal position falls within the rim's bounds (roughly x between 3.89 and 4.11) to determine if the shot actually goes in.

Lower speed means slightly less drag, so vertical velocity decays a bit less and flight time stretches, but that effect is minor near the trajectory's arc. I'll redo the numerical integration with vx0=3.29, vz0=9.2 using the same drag model to check where it lands.

Continuing the RK4 integration step by step, tracking velocity and position through each substep as drag forces decrease with falling speed.

Continuing the trajectory integration, I get v5=(3.0441,3.7730) with position x5=1.57505, z5=3.32785, then start the t0.5 step computing speed and drag deceleration again.

Still computing trajectory steps...

Continuing the step-by-step velocity integration, I get x10≈3.06601, z10≈3.96397 at t=1.0, and I'm starting the next drag calculation with the updated speed.

Still computing trajectory steps...

Checking when the ball reaches rim height (z=3.05), I'm estimating about 0.03s more, landing x near 4.02 — close to the rim center, so it should clear. Now I need to verify the ball also clears the front rim tube as it passes x≈3.763 on the way down.

Checking the back rim clearance too: the perpendicular distance comes out to about 0.176, still safely above the required 0.127, so the ball clears both rims along this trajectory.

Checking whether the ball might clip the backboard's bottom edge before reaching the floor — tracing the trajectory near x≈4.2-4.38, z≈2.7-2.94 to see if it passes clear of that corner or grazes it.

Landing might clip the support base plate but that's acceptable since we just need first contact. With no spin there's no Magnus effect to worry about, so I'll set the velocity to roughly 3.275 m/s horizontal and 9.2 vertical, nudging slightly to better center the trajectory through the gap.

