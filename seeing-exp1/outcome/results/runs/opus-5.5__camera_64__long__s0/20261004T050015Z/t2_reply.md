The ball now drops through the rim. I lowered the launch from 3.5952 m/s horizontal and 10.416 m/s vertical to 3.40 and 9.00.

**How I chose it:** I stepped the flight through by hand in 0.1 s steps, including the scene's air drag on a sphere.
- The drag is significant. At launch speed it adds about 2 m/s² of deceleration, so a drag-free calculation is not accurate enough here.
- The ball peaks at about 3.87 m, roughly 0.8 m above the rim.
- On the way down it reaches rim height (3.05 m) at x ≈ 3.995, at t ≈ 1.27 s. That is within about 5 mm of the rim centre.
- It enters at about 53° below horizontal. At that angle the 0.457 m rim shows an opening of about 0.36 m. The ball is 0.239 m across, which leaves about 7 cm of slack along x.

**Clearances I checked:**
- The front and back of the rim stay about 0.18 m from the ball's centre line. The ball's radius plus the rim tube is 0.127 m.
- The bracket and the bottom front corner of the backboard stay at least 0.18 m from the centre line.
- After passing through, the ball lands at roughly x ≈ 4.7–4.9 m, short of the support pole.

**What I could not confirm:** These figures come from my own integration, not from running MuJoCo. A few centimetres of difference from the real simulation would still go in.

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
    <key name="shot" qvel="3.40 0 9.00 0 0 0"/>
    <!-- Changed qvel from "3.5952 0 10.416 0 0 0" to "3.40 0 9.00 0 0 0".
         The old launch was far too steep and fast: the ball peaked about 5.6 m high,
         right above the hoop, sailed over the backboard and landed metres behind (miss: long).
         The new launch was checked by stepping the flight by hand in 0.1 s steps, including
         the scene's air drag (blunt drag coefficient 0.25, air density 1.2; about 2 m/s^2 of
         deceleration at launch speed).
         The ball peaks at about 3.87 m, about 0.8 m above the rim. It reaches rim height
         (z = 3.05) at x ~ 3.995, t ~ 1.27 s, within about 5 mm of the rim centre.
         It enters at ~53 deg below horizontal, so the 0.457 m rim shows an opening of
         about 0.36 m against the 0.239 m ball, leaving about 7 cm of slack along x.
         The rim front/back, bracket and backboard corner all stay at least 0.18 m from the
         ball's centre line. The ball then lands at roughly x ~ 4.7-4.9 m, short of the
         support pole. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for drag in the velocity calculation, recalling MuJoCo's ellipsoid fluid model where the blunt drag force on a sphere scales with the fluid density, projected area, and velocity squared.

Computing k/m yields a meaningful deceleration term, roughly 2.17 m/s² at 10 m/s, which is substantial relative to gravity, so I can't ignore drag. Since the sphere's slender drag and lift terms vanish and angular drag only affects rotation, I just need to integrate the equations numerically to find a trajectory where the ball's center passes through the rim center while descending.

Checking the geometry: rim inner radius 0.2286 versus ball radius 0.1194 gives margin, but the effective opening shrinks with entry angle — I need sinθ > 0.52, so θ > 31°, and aiming for a steeper 45-50° descent gives more clearance (~±0.042 m). I also need to confirm the ball clears the backboard and lands centered on the rim at z=3.05.

Now I'm setting up a drag-free parabolic trajectory as a baseline: solving for launch angle and speed using the horizontal/vertical displacement (Δx=4, Δz=2.9306) and requiring a -1 slope (45° descent) at the hoop, deriving tanα in terms of the coefficient A = g/(2v²cos²α), then I'll refine this with full numerical integration including drag (c=0.02167) to get the actual trajectory, continuing the ball's fall to the floor after it passes through the hoop.

Since drag complicates things analytically, I'll switch to numerical integration with small time steps, estimating initial speeds around vx=3.9, vz=8.6 to compensate for drag, then using a midpoint method to update velocity and position each step based on drag force proportional to speed squared.

Continuing the position updates: z reaches 0.9216 at t=0.1, then recomputing drag-adjusted acceleration gives new velocities vx=3.7608, vz=6.3654, pushing position to x=0.7651, z=1.6122 at t=0.2, and I'm continuing the iteration into the next step.

Continuing the RK4 integration, I update velocities and positions through t=0.4, tracking drag-adjusted acceleration each half-step as speed decreases.

Continuing the integration: at t=0.6, x=2.2293, z=3.3176, with drag coefficient and acceleration updating each half-step as velocity decreases toward vx=3.5500, vz=1.2272.

Stepping to t=0.7, I compute the new velocity magnitude, drag coefficient, and accelerations through the half-step, converging on vx=3.5223, vz=0.2405, with position updating to x=2.9393, z approaching roughly 3.56.

Continuing to t=0.8 and t=0.9, I repeat the same RK2-style velocity and drag calculations, tracking x advancing to about 3.29, z dropping toward 3.54, and velocities shifting as drag and gravity pull the trajectory downward.

Continuing the integration step, x reaches 3.984 with z at 3.196 just past t=1, close to the target of z=3.05 at x=4 but slightly long—extrapolating further suggests the ball overshoots to about x=4.16 when it drops to rim height, meaning it would strike the back rim rather than land cleanly.

This tells me the current 38° entry angle is too shallow, so I need a steeper trajectory. I'm trying a redesigned launch with higher apex and smaller vx, testing values like vx=3.9, vz=8.6 and setting up the drag-free quadratic to solve for the time when z=3.05.

Comparing the drag-free solution (x≈5.03, t≈1.29) against the drag-included version (x≈4.16, t≈1.05) shows drag shortens the landing distance by roughly 0.87m, which is substantial. I'm now setting up another numerical integration pass with vx=3.6, vz=9.0 to see if this gets closer to landing near x=4 with a steeper angle, initializing the velocity components for the first timestep.

Working through the midpoint integration, computing speed magnitude, drag coefficient, and accelerations at each half-step to update velocities and positions, then continuing to the next timestep with updated speed and drag values.

Continuing the RK2 integration, I'm advancing velocity and position through t=0.2 and into t=0.3, updating drag coefficients and accelerations at each half-step as the projectile decelerates.

Continuing the RK2 integration steps, I'm tracking position and velocity updates through t0.5 and into t0.6, with drag coefficient and acceleration recalculated at each half-step.

Continuing the half-step RK integration through t=0.8, drag and gravity are steadily reducing vertical velocity toward near-zero while horizontal velocity decays only slightly, with position updating to roughly x=2.71, z=3.86.

Continuing the RK2 integration step through t1.0, updating velocity and position components as drag and gravity forces evolve with each half-step.

Still overshooting with this trajectory, so I'm trying to tune the initial velocities down. Since the landing x-position scales roughly with vx while the time of flight is mostly set by vz, I'll try scaling vx down proportionally to reduce the overshoot while keeping vz near 8.6 to hit the target height.

Computing the entry angle now gives about 40°, which gives a tighter but still workable clearance margin — maybe 4cm horizontally — assuming my numerical integration error stays within a few millimeters.

Let me try a steeper trajectory instead: with vz=9.0 and scaling vx to about 3.40, the entry angle rises to roughly 49°, widening the effective window and giving a more comfortable 7cm margin. I should double-check this by actually integrating vx=3.40, vz=9.0 to confirm.

Working through the numerical integration step by step, tracking velocity, drag coefficient, and position at each small time increment to trace the full trajectory.

Continuing the half-step RK4 integration, I update velocities and drag coefficients through t=0.3, tracking position as x grows to 0.9918 and z to 2.3102 while vz continues decaying under gravity and drag.

Continuing the drag integration, I'm stepping through t=0.5, updating velocities and positions with the quadratic drag coefficient recalculated each half-step.

Continuing the half-step integration through t=0.8, velocity drops to near zero vertically while horizontal speed decays slightly, pushing position to roughly x=2.87, z=3.87 as drag continues easing with lower speed.

By t=0.9 vertical velocity turns negative as the projectile starts descending, with drag coefficient staying near 0.068-0.069 and position advancing to x=3.17, z=3.78, setting up the next step at t=1.0.

Continuing the drag calculation, computing the new velocity magnitude and drag coefficient, then updating the half-step acceleration components for the next integration step.

Since z still needs to drop further to reach 3.05, I'm solving the quadratic for the small time increment needed, then updating x accordingly.

x ends up near 4.0 with entry velocity vz≈-3.97, vx≈2.95, giving roughly a 53° angle—so I'm setting the initial velocity to 3.40 0 9.00 0 0 0.

Now I need to verify clearance against the rim and backboard along the trajectory, checking the ball's position relative to the front rim's inner edge and tube radius to make sure it doesn't clip anything on the way up or down.

Computing the perpendicular distance from the trajectory line to the front rim tube center gives about 0.185, comfortably clearing the required 0.127 margin—so that's fine. Now checking the back rim position similarly.

Below the rim, I need to verify clearance against the backboard's bottom edge. Tracing the descending ball path at its 53° slope, it appears to dip below the backboard's bottom edge height near x≈4.26, so I need to examine the corner case more carefully.

I check perpendicular distances from the ball's trajectory to the backboard's bottom-front corner and to the mounting bracket box's near corner, and both clear the 0.12 radius threshold with margin (0.219 and 0.183 respectively), so no collision there.

Looking at the falling trajectory, it curves steeper as it descends, moving further from the backboard, and the ball likely lands near x≈4.7-4.9 relative to the support base and pole positions, which seems fine either way. The rim tube capsule check at y=0 also looks clear, so I'm ready to write up the final comment.

