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
    <key name="shot" qvel="3.25 0 9.35 0 0 0"/>
    <!-- Changed qvel from (2.9532, 0, 8.556) to (3.25, 0, 9.35).

         Why the old shot missed: even with no drag it crossed rim height (z = 3.05) on the way
         down at x ~ 3.77. That is about 0.23 m short of the rim centre and right on the front
         rim tube. Air drag (density 1.2, blunt coefficient 0.25, so k = C*rho*pi*r^2/m
         ~ 0.0217 /m) makes it shorter still.

         How the new values were set:
         - Drag-free target: vx = 2.96, vz = 8.8 reaches x = 4.0 at z = 3.05 while descending,
           at t ~ 1.35 s, entering at roughly 55 deg.
         - Estimated drag loss over that flight: ~0.35-0.40 m in x and ~0.67-0.75 m in z.
         - Each loss is made up by adding (loss / t) to the matching velocity component.
         - Lateral velocity stays 0. No spin, so no Magnus force.

         The required accuracy is about +/-0.11 m of ball-centre offset at the rim. Expected
         clearance from the front rim during descent is ~0.19 m against a needed 0.127 m.

         These drag figures are a hand estimate, not a re-run simulation. If a re-render still
         shows the ball short or long, adjust vx by roughly 0.07 m/s per 0.1 m of miss. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working through how MuJoCo's ellipsoid fluid model computes drag, using the blunt drag coefficient along with the fluid density and cross-sectional area to estimate the force from velocity.

I'm designing a drag-free trajectory to pass through the target point at (4,0,3.05) while descending, solving for the required vertical and horizontal velocity components using time-of-flight equations. Then I'm estimating how drag would perturb this trajectory by tracking how speed decreases from launch to apex to the target point, to correct the initial velocity accordingly.

Computing the deceleration-weighted integral numerically, plugging in the acceleration values at each time step and applying trapezoidal integration over the 0 to 1.35s interval to estimate the horizontal velocity loss.

I get roughly 0.354 m for this displacement component, but now I'm second-guessing my drag coefficient formula—trying to recall whether MuJoCo's blunt drag model includes a factor of one-half like standard aerodynamic drag equations or omits it entirely.

With C=0.25 giving an effective Cd of 0.5, that matches typical drag coefficients, so I compute k ≈ 0.0217 using the projected area and density values. Now I'm working through the vertical drag deficit integral, estimating the drag-induced acceleration terms at several time points (t=0, 0.3, 0.6, 0.9s) to see how much they diminish as velocity decreases toward apex.

I'm continuing the integral at later time points (t=1.2, 1.35s) where vz goes negative during descent, weighting each term by (T-t) and applying trapezoidal integration to get a cumulative z deficit around 0.67 m — a substantial perturbation, though I accept the approximation has limits and plan to compensate for it. Now I'm thinking about how to adjust the initial vx and vz by estimating the linear sensitivity of landing position to launch velocity over the time T.

At the actual crossing time (around T=1.352s, when z=3.05m descending), accounting for drag the trajectory undershoots to roughly x=3.646 and z=2.38 with a reduced descent speed of about -4.2 m/s, meaning the real crossing happens earlier than expected. To correct this I want to add velocity boosts Δvz≈0.50 and Δvx≈0.262 so the trajectory lands at x=4, z=3.05 at time T, though I recognize these increased speeds will themselves raise drag losses proportionally, so the correction isn't perfectly clean.

Iterating on this, I estimate the drag losses scale roughly with v², so bumping vz by about 11% relative and vx effects by about 14% gives refined corrections of Δvz≈0.555 and Δvx≈0.296, landing on vz≈9.355 and vx≈3.254 — keeping in mind there's roughly ±0.1m of uncertainty at the rim given the approximations in this iterative estimate.

Checking clearance on descent: at a steep entry angle near 54°, the ball's path over the front rim keeps about 0.19m distance from the rim tube, comfortably clearing the required 0.127m, and the back rim/backboard side looks fine too.

Refining the drag integral with Simpson's rule instead of trapezoid gives 0.464 vs 0.49, a small correction. Using constant vx slightly overestimates drag since real vx decays during flight, but the effect is minor enough to ignore.

I'll settle on an initial velocity of 3.25 in x and 9.35 in z, though I can't fully verify this without running the simulation directly.

