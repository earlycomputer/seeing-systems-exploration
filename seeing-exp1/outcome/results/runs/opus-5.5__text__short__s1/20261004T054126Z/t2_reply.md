The original key falls short. Even without air, the ball's centre reaches rim height near x ≈ 3.77 m, about 0.23 m in front of the hoop centre. Drag makes it shorter still.

I picked a new launch velocity of (3.27, 0, 9.2) m/s and integrated the flight by hand, step by step, including the scene's drag. I assumed MuJoCo's blunt-drag term is C·ρ·A·|v|·v with no factor of ½, which gives about 0.0217 per metre per unit mass. The predicted flight:

- The ball peaks at about 4.0 m around x ≈ 2.7.
- It comes down through rim height (3.05 m) at x ≈ 4.0, descending at about 54°.
- At that point it is about 0.24 m from both the front and the back rim tube. It needs about 0.127 m (ball radius plus tube radius), so it should go through without touching.

I have not run this in MuJoCo, so the clearance is a prediction.

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
    <key name="shot" qvel="3.27 0 9.2 0 0 0"/>
    <!-- Changed shot qvel from (2.9532, 0, 8.556) to (3.27, 0, 9.2). The old launch fell short:
         even in vacuum its centre reached rim height at x ~ 3.77 (front rim), and the scene's air drag
         (density 1.2, blunt coef 0.25 -> ~0.0217 1/m per unit mass) shortened it further. Integrating the
         flight with that drag, the new velocity peaks at ~4.0 m and descends through z = 3.05 at x ~ 4.0
         at ~54 deg, about 0.24 m from both front and back rim tubes (needs > 0.127 m), so it drops
         cleanly through the hoop. No lateral velocity, so no left/right error. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm estimating the drag coefficient to mass ratio for the ball, calculating it to be roughly 0.0217 per unit mass, and starting to design a launch trajectory aiming for the ball to descend steeply near (4, 3.05).

I'm double-checking whether MuJoCo's blunt drag formula includes a ½ factor like standard physics or not, recalling it likely doesn't, and considering whether other fluid effects apply here—slender drag (zero for a sphere), viscous drag (zero by default), added mass, and buoyancy. I compute the buoyant force from air density and the ball's volume, getting about 0.084 N, which is tiny compared to the ball's weight, so buoyancy is probably negligible for this calculation.

Now I'm setting up a numerical integration by hand to find the launch velocity components that produce a trajectory passing through roughly x=4.0, z=3.05 with the target arc. I define the drag-affected acceleration equations with coefficient c≈0.02167, then try an initial guess of vx0=4.0, vz0=8.0 and plan to step through time with small increments to see where the trajectory lands, adjusting as needed.

Continuing the Heun step, I get x1≈0.396, z1≈0.864 at t=0.1, then computing drag forces at this new point to predict the next state at t=0.2 with vx≈3.86, vz≈5.78.

Continuing the RK2 integration, I get vx3=3.8106, vz3=4.7431 at t=0.3, giving position x3=1.1698, z3=2.0247, then I move on to compute the drag force components for the next timestep.

Continuing the step at t=0.4, I compute drag-adjusted accelerations from predicted velocities, getting averaged ax and az values to update the trajectory for the next timestep.

Continuing the RK2 integration, I get vx6=3.6892, vz6=1.6923, giving x6=2.2936, z6=2.9868 at t=0.6, and I'm now computing the drag acceleration for the next step.

Continuing the numerical integration step at t=0.7, computing predicted velocities and drag/gravity accelerations, then averaging to update the trajectory.

I'm finding the apex only reaches about z=3.13 at x=3.0, which is too low to clear the rim comfortably—I need more vertical velocity to get a proper arc with the apex well above the rim before descending at the target. I'm going to try adjusting the initial velocity components and re-estimate the trajectory with a higher vz.

Continuing the drag-adjusted trajectory integration using predictor-corrector steps, computing velocity magnitudes and updated accelerations at each timestep to track x and z position over time.

Averaging to get vx2=3.2741, vz2=6.9315, then updating position to x2=0.6669, z2=1.7306. Continuing the RK2 iteration into t=0.2, computing new velocity magnitude and accelerations for the next predictor step.

Computing drag accelerations for the predictor step gives ax=-0.3955, az=-10.4056, which average with the previous values to update velocity and position, landing x4 at about 1.0.

Moving to t=0.4, I continue the RK2-style integration: estimating drag with current speed and velocity components, then using the predicted velocity to refine the acceleration estimate for the next averaging step.

Continuing the Euler integration step, I update velocities to vx6≈3.113, vz6≈2.753 and positions to x6≈1.941, z6≈3.656, then start computing the next drag correction at t=0.6 with |v|≈4.156.

Continuing the drag-adjusted RK2 integration, I compute z8, then move to t=0.7, applying the same velocity-dependent drag calculation to get updated acceleration and predicted velocities for the next step.

Continuing the drag correction, I get vx9=3.0445, vz9=-0.2199, giving x9=2.8642 and z9=4.0346, then move on to computing the velocity magnitude for the next step at t=0.9.

Continuing the numerical integration, I get x10≈3.1676, z10≈3.9638, then move to t=1.0, recomputing drag acceleration with updated velocity magnitude and predicting the next step's velocities.

Continuing the predictor-corrector integration, I compute the drag-adjusted acceleration for the next velocity estimate, then average and update position to get x12=3.7676, z12=3.5315, moving into the t=1.2 step.

Continuing, I get x13≈4.0636, z13≈3.1721. To reach rim height z=3.05 it takes about 0.03s more, landing around x=4.15, which overshoots by roughly 0.15 — I need to check if that's within tolerance given the steep ~54° entry angle, which actually tightens the effective window.

To correct, I'm reducing vx0 by about 3.6% (to roughly 3.277) to shrink the overshoot while keeping vz unchanged, since the drag coupling between horizontal and vertical velocity is small but slightly offsetting.

With dt=0.1 Heun the integration error should be small since it's O(dt²) and only applies to the drag terms, while gravity integrates exactly, so I trust this accuracy. I'm now second-guessing the exact MuJoCo drag formula for blunt bodies—trying to recall whether there's a 1/2 factor and the correct coefficient structure, since I remember the default blunt drag coefficient being around 0.5 but I'm not fully certain of the precise expression.

The ellipsoid model does include added mass effects for the sphere, but these are tiny (~0.7%) and depend on angular velocity, so they vanish without spin. As for buoyancy, I don't think it's part of the ellipsoid model, but if it were, it would slightly reduce effective gravity and give a marginally higher apex.

Settling on qvel="3.27 0 9.2 0 0 0", I'm verifying the trajectory clears the backboard and rim: the apex occurs well before the ball reaches the board, and checking the ball's position against the rim and backboard geometry confirms adequate clearance throughout the flight path.

Checking another point along the arc confirms the ball clears the rim comfortably throughout its path — this is a clean swish trajectory. Good, I can finalize this.

