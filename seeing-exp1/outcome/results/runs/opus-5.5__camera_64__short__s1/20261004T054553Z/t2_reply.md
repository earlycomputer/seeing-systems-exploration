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
    <key name="shot" qvel="3.445 0 8.9 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from (2.9532, 0, 8.556) to (3.445, 0, 8.9).
       Why: the old velocity was a drag-free solution, and even without drag it brought the
       ball centre down to rim height at x ~ 3.77 m, right over the front rim. The air drag
       in this scene (density 1.2, blunt coefficient 0.25 -> ~0.0217 v^2 per metre) only made
       it fall shorter.
       The new velocity comes from integrating the trajectory with that quadratic drag included.
       The apex is ~3.79 m at t ~ 0.8 s. The ball centre comes down through z = 3.05 m at
       x ~ 3.96-4.0 m, y = 0, about 1.24 s after launch, descending at ~51 degrees. Clearance
       between the ball (r = 0.119 m) and the inner rim (r = 0.229 m) is ~0.11 m.
       The aim is ~1% short of dead centre to hedge against uncertainty in whether a small
       buoyancy force (~0.14 m/s^2) is applied. If it is, the ball arrives slightly long
       (~4.05 m), which is still inside the rim. -->
</mujoco>
```

---
thinking (summarized):

I need to account for drag in the velocity design, using MuJoCo's ellipsoid fluid drag model with its blunt, slender, angular, Kutta, and Magnus coefficients to estimate the force on a sphere-like shape moving through the fluid.

Buoyancy seems negligible here, contributing maybe 0.14 m/s², so I'll set it aside. Computing the drag deceleration constant gives roughly 0.0217 per meter, meaning at 9 m/s the drag decelerates the ball by about 1.76 m/s². Now I need to work through the trajectory numerically to see the ball's center passing through the rim at (4, 0, 3.05) while descending.

I'll try a perturbative approach: start from the drag-free parabolic trajectory with a guessed launch velocity around (3.2, 8.8), then estimate how much drag pulls the horizontal distance short, and adjust the initial velocity to compensate.

Let me set up a step-by-step RK2 integration with dt=0.1, tracking position and velocity under gravity plus quadratic drag, starting with trial values vx=3.2, vz=8.9, computing the speed and acceleration components at each step to trace out the actual trajectory.

Continuing the integration step through t=0.2, tracking velocity decay from drag and updating position: x reaches 0.6278, z reaches 1.6709, with speed dropping to about 7.336 before computing the next midpoint acceleration for the following step.

Continuing the numerical integration, I get v5=(2.9696, 3.5123) with position x=1.5343, z=3.1895 at t=0.4, tracking the drag-affected trajectory step by step.

Continuing the numerical integration, I get v7=(2.9200, 1.5074), with position updating to x=2.1228, z=3.6902 at t=0.7, then computing the drag force components for the next step.

Still computing the trajectory steps...

Continuing the numerical integration, computing velocity and position at t=1.1 using midpoint drag and gravity updates, with x approaching 3.5 and z around 3.5.

At t=1.2 I'm getting x≈3.84 and z≈2.84, so I can see the trajectory is crossing z=3.05 somewhere in this interval—I'll need to interpolate to pin down the exact crossing point.

At the crossing, x only reaches about 3.68 against a target of 4, so I'm short by roughly 0.32m with a descent angle near 53°. To correct, I'm considering scaling up the initial horizontal velocity by about 8.6% and checking how that ratio of achieved distance to ideal distance holds given drag effects.

Now I'm re-simulating with vx=3.48 and vz=8.9, stepping through the trajectory and recomputing drag-adjusted accelerations at each timestep to see where this new combination lands.

Continuing the RK4-style integration, I get t=0.2 with v3=(3.3042, 5.5782), updating position to x=1.01525, z=2.28128 and moving to the next timestep.

Continuing the RK4 integration: computing drag acceleration at t=0.4 gives v5=(3.2250, 3.5053) with position updates x=1.6675, z=3.18746. Now stepping into t=0.5, calculating the speed magnitude and starting the acceleration components for the next midpoint estimate.

Continuing the step-by-step velocity Verlet integration, I'm computing drag-adjusted accelerations and updating position/velocity through t=0.7, tracking the midpoint speed estimates for the next half-step.

Continuing the RK4 integration step for t=0.9, computing drag acceleration and updating velocity and position with midpoint estimates for the next timestep.

Continuing the RK4 integration step, computing the drag acceleration terms at t=1.1 and the midpoint, then updating velocity and position for the next step.

Since z is now close to crossing zero, I'm estimating the small remaining time to impact by linearizing the velocity near this point, getting Δt ≈ 0.0449s and using it to extrapolate the final x position.

At crossing, x ≈ 3.999, z ≈ 3.05, with descent angle around 51° given vz ≈ -3.79 and vx ≈ 3.04. I'm checking whether the integration error from RK2 with dt=0.1 is negligible (likely just millimeters), but I want to verify the exact drag force formula MuJoCo uses for its ellipsoid fluid model, particularly whether there's a ½ factor in the blunt drag coefficient term.

I recall the formula doesn't include a ½, and since a sphere has A_max equal to A_proj, the slender drag term vanishes, leaving just the blunt term — consistent with how I've been computing k. For added mass, the ellipsoid model's cross-term forces only appear with rotation (ω×v), so they're zero here. I'm now thinking through whether buoyancy is also applied in this model.

Checking the vertical shift from buoyancy: if present, roughly 0.107 m upward over the fall, shifting the crossing point by about 0.085 m longitudinally. Comparing this against the hoop's geometry — rim inner radius 0.2286 m, ball radius 0.1194 m — there's about 0.109 m of horizontal margin, so I need to check whether this offset still keeps the shot within tolerance at the steep descent angle.

I'm not confident whether MuJoCo's ellipsoid fluid model includes buoyancy the way the inertia-box model does, so I'll hedge between the two possible landing points (around 3.96 vs 4.045) by nudging vx down about 1%, landing on vx=3.445, vz=8.9 as a compromise that should work whether or not buoyancy is active.

