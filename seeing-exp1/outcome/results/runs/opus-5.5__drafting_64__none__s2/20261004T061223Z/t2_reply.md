Changed only `qvel` from `3.21 0 9.3` to `3.4 0 9.0`, so the ball now comes down through the rim instead of carrying into the backboard. The result comes from my hand-integration of the trajectory, not from running MuJoCo.

**How the new velocity was found.** I stepped the flight by hand in 0.1 s steps, using a midpoint evaluation of the acceleration in each step.

- **Drag.** I assumed MuJoCo's ellipsoid blunt-drag law, F = C·ρ·A·|v|·v. With the scene's blunt coefficient 0.25, ρ = 1.2 and r = 0.1194, that gives a deceleration of about 0.0217·|v|·v per unit mass. I am not certain MuJoCo's formula has no ½ factor; if it does, drag is half this.
- **Buoyancy.** I ignored it; it would reduce gravity by only about 1.4%.

**Predicted flight.**
- The apex is about 3.87 m at x ≈ 2.9 m, t ≈ 0.81 s.
- The ball crosses rim height (3.05 m) on the way down at t ≈ 1.27 s.
  - Its centre is then at x ≈ 3.99, against the rim centre at x = 4.
  - It is moving at about (2.95, −3.98) m/s, a steep entry of about 53° below horizontal.

**Clearance at the rim.**
- Along that entry line, each side of the rim tube sits about 0.18 m from the ball's path, against a ball radius of 0.119 m. That leaves about 6 cm of margin each side, or about ±8 cm of tolerance in where the ball crosses.
- It then passes under the backboard: the top of the ball is at about 2.76 m where the board's bottom edge is at 2.9 m.

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
    <key name="shot" qvel="3.4 0 9.0 0 0 0"/>
    <!-- Changed qvel from "3.21 0 9.3 0 0 0" to "3.4 0 9.0 0 0 0". The old launch was still about 1 m
         above the rim (and rising) when it reached x = 4, so it carried long into the backboard.
         Estimated by hand-integrating gravity plus the ellipsoid blunt drag (~0.0217*|v|*v per kg,
         assuming F = C*rho*A*|v|*v with C = 0.25; buoyancy ignored), not by running MuJoCo.
         The new launch peaks near 3.87 m at x ~ 2.9 m and descends through z = 3.05 at x ~ 3.99 m
         (rim centre x = 4) at about 53 deg below horizontal. That leaves ~6 cm clearance to the rim
         on each side, and the ball then passes under the backboard's bottom edge. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to figure out the right launch velocity so the ball arrives at the rim center (x=4, z=3.05) accounting for drag and gravity, starting from z≈0.119. I'm testing different flight times to get a steep, descending trajectory through the hoop rather than a flat one.

Trying T=1.2s: horizontal velocity 3.333, vertical velocity 8.33, giving an apex around 3.66m and a rim entry angle near 46°, which looks like a good steep shot.

Now I need to account for air drag using MuJoCo's fluid model. Since this is a sphere, the slender drag and Kutta lift terms vanish by symmetry, leaving only blunt drag proportional to density, cross-sectional area, and velocity squared, and I'm computing that coefficient now.

There's also a small buoyancy correction from air density reducing effective weight by about 1.4%, though I'm unsure whether MuJoCo applies buoyancy identically for the ellipsoid fluid model versus the inertia-box model — likely a minor effect either way.

Now I need to numerically integrate the trajectory with drag coefficient k/m≈0.0217, using roughly 0.1s steps, trying initial velocity guesses like vx0=3.6, vz0=8.6, and adjusting until the projectile reaches x=4 at z=3.05 while descending. I'm weighing whether to use g=9.81 or a slightly reduced value near 9.75 to account for buoyancy.

Computing drag deceleration from velocity magnitude and stepping forward with simple Euler updates, I'm tracking how x and z evolve over successive 0.1s intervals as speed and acceleration decrease each step.

Continuing the step-by-step integration: by step 5 the velocity drops to around vx=3.325, vz=3.169, with position reaching roughly x=1.723, z=3.030, as drag continues to shrink both the horizontal and vertical acceleration terms each iteration.

Pushing through steps 6 through 8, the drag force keeps weakening as speed decreases, with vz dropping to near zero (0.167) while vx stabilizes around 3.24, and the trajectory reaches approximately x=2.707, z=3.528 at t=0.8.

Continuing the iteration, I'm computing drag-adjusted acceleration and updating velocity and position through steps 10 and 11, with vx decreasing and vz becoming more negative as the projectile falls further, reaching about x=3.35, z=3.37 at t=1.0.

At step 12, I find the trajectory crosses z=3.05 around x=3.755, meaning the ball falls short of the target rim by roughly 0.25 meters.

I need to boost vx by about 0.23 m/s to add that missing range, since the trajectory to reach z=3.05 at x=4 takes about 1.13 seconds, though drag will complicate the scaling since a faster vx also decays differently.

Scaling up the drag loss estimate with higher velocity, I estimate the average horizontal velocity would drop to around 3.52 for vx0=3.85, giving roughly 3.97 m distance in 1.128 s — slightly short of the 4.0 target, so I'm nudging up to vx0=3.9 to compensate.

Now I need to verify rim clearance geometrically: I'm checking whether the ball's trajectory clears the front rim tube by computing the distance from the ball's center to the front rim point at the moment it crosses that height, requiring it to exceed the sum of their radii.

At a descent angle of roughly 41°, the effective horizontal opening works out to about 0.30m against a ball diameter near 0.24m, which is a tight but passable margin, so I'd prefer a steeper entry angle for safety. Checking the back rim similarly, the ball's edge stays comfortably inside the rim's inner boundary at the critical height, so that side looks fine.

That's too tight given my integration accuracy, so I should try a steeper trajectory instead — more vertical velocity, less horizontal. I'm redoing the integration with vx0=3.0, vz0=9.2 using drag coefficients, computing acceleration components and stepping forward with a predictor-corrector method.

There's a bigger worry here though: I'm not even sure whether MuJoCo's drag formula includes the one-half factor, which would significantly change the drag magnitude and matters more than my integration method's accuracy.

Viscosity defaults to zero, so that term drops out. I'm checking the accuracy of my simple Euler integration scheme—since drag decreases over time, this method tends to slightly overestimate drag early on, leading to a small systematic underestimate of velocity and a resulting position error of maybe a few centimeters over one second, which could matter here.

So instead I'll switch to a midpoint method: estimate velocity at the half-step, compute acceleration there, then use that to advance the full step—two evaluations per step but much better accuracy for a steep trajectory. I'm testing this with an initial velocity of (3.4, 9.0) m/s under drag, working through the acceleration components (drag proportional to speed times velocity component, plus gravity) at t=0 to get the midpoint velocity estimate before advancing further.

Continuing the step-by-step numerical integration, updating position and velocity through each timestep as drag decreases with speed, tracking x and z coordinates up to t=0.2s and beyond.

Continuing the projectile integration, I'm stepping through drag-adjusted velocities and positions across t=0.3 to 0.4, computing midpoint accelerations each step to update x and z coordinates.

Continuing the RK4 integration step to t=0.6, updating position to x=2.2527, z=3.5426 with velocities trending toward vx=3.094, vz=1.587.

Continuing the trajectory integration, I get x≈2.8672, z≈3.8705 at t=0.9, with velocity dropping to around 3.08 as drag keeps decelerating the projectile.

Continuing the numerical integration, I'm stepping through velocity and position updates at t=1.1, tracking drag-adjusted acceleration components as the trajectory curves downward.

Continuing the integration step, I find x≈4.0677, z≈2.9425 at t=1.2, so the projectile has dropped below z=3.05. Now I'm setting up the quadratic equation to solve for the exact crossing time within this interval.

That gives margin of 0.063m, tolerance ~0.078m in x, which is comfortable. Checking the backboard and bracket clearance too — the ball's x-position stays well below the bracket's edge (4.24) at that height, so it clears both obstacles safely while continuing to fall.

Now I'm tracing the ball's fall to the floor: it reaches z=0.12 at about t=0.466s, landing near x=5.32, which actually puts it right around the support pole's x-range (5.1-5.3). So the ball might graze or hit the pole/base near the bottom, but since the simulation only needs to confirm it drops through the hoop, this later collision likely doesn't matter for the core requirement.

Checking clearance under the backboard: the ball passes below it (bottom at 2.9) with top of ball around 2.76, so it clears fine. I'll go with the velocity setting qvel="3.4 0 9.0 0 0 0", noting that buoyancy effects would only shift the apex and crossing time slightly.

