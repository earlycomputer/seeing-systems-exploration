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
    <key name="shot" qvel="3.564 0 8.745 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from (3.5952, 0, 10.416) to (3.564, 0, 8.745).
       Why: the old launch peaked near 5.6 m and crossed x = 4 m about 2.5 m above the rim, so it sailed long.
       How the new values were found: hand-integrated the flight with gravity plus the ellipsoid blunt drag
       (C = 0.25, rho = 1.2, A = pi r^2, so drag/m is about 0.0217 |v| v), using RK2 with dt = 0.1 s.
       Predicted flight:
         - launch at about 9.4 m/s, 68 degrees up;
         - apex about 3.67 m, near x = 2.7 m, so well below the backboard top;
         - ball centre reaches the rim plane (z = 3.05) at t of about 1.2 s, x of about 3.96 m, y = 0;
         - descends there at about 48 degrees, which keeps roughly 4 cm of clearance from both the front and back rim;
         - passes under the backboard's bottom edge.
       Caveats: these are hand estimates, not a MuJoCo run. Buoyancy, if the fluid model applies it, would shift
       the crossing about 8 cm further, to about x = 4.04, which still clears. After dropping through, the ball
       will likely strike the support pole around z = 1.5 m before it first lands. -->
</mujoco>
```

---
thinking (summarized):

I'm working through how MuJoCo's ellipsoid fluid model handles drag, recalling the blunt drag, slender drag, angular drag, and lift coefficients that make up the fluidcoef vector, and trying to pin down the exact drag force formula involving density and projected area.

For a sphere, slender drag and Kutta lift vanish since there's no shape asymmetry, and Magnus lift is zero without spin, so I compute an effective drag coefficient from the blunt term using the ball's radius and air density, arriving at roughly k≈0.0217 per meter for the acceleration term a_drag = k|v|v.

Now I'm thinking through the launch design: I want the ball's trajectory to pass through the rim at x=4, z=3.05 while descending, so I'm picking a launch angle around 50-55° and making sure the arc clears the backboard while centering on the hoop.

I'm working out the required descent angle for clearance given the ball and rim radii — needing more than about 31.5° to fit through the opening, so I'm targeting closer to 45-55° and setting up the projectile equations with drag to solve for the needed launch velocity components.

Checking the math at 55°, I find the ball reaches the hoop almost exactly at the apex of its arc, meaning it's barely descending — that's not steep enough, so I need to adjust the launch angle or velocity to get a proper downward trajectory through the rim.

Trying the slope relation for the entry angle, tanθ around 2.3-2.47 gives entry angles near 66-68°, which seems quite steep for a short 4m shot from low release height, so I'm looking for a value that gives a better margin at the rim.

Without drag, solving for vx and vz gives roughly vx=3.365, vz=8.296, with flight time near 1.19s and apex height around 3.63m, clearing the backboard fine. Now I need to account for drag — the coefficient k≈0.02167 means drag acceleration at launch speed (~8.95 m/s) is about 1.73 m/s², which is non-negligible, so I should numerically integrate the trajectory in small time steps using something like a midpoint method.

I'll set up the drag equations and try integrating starting from the no-drag velocity guess, then iteratively increase vx and vz to compensate for the energy lost to drag until the ball reaches the hoop correctly, starting a step-by-step RK2 integration with dt=0.1s.

Continuing the integration, drag coefficient drops to 0.17116 giving ax=-0.5656, az=-11.0379; using the midpoint values I update position to x=0.6608, z=1.5541 with vx=3.2518, vz=6.0872 at t=0.2, then begin step 3 by computing the new speed magnitude of 6.9013.

Applying the same RK2 midpoint scheme forward: drag coefficient falls to 0.14955 at full step, then 0.13915 at the midpoint, yielding position x=0.9836, z=2.1092 and velocity vx=3.2069, vz=5.0290 at t=0.3; I then start step 4 with speed 5.9645 and drag coefficient 0.12925, giving ax=-0.4145, az=-10.460.

Continuing the numerical integration...

Position updates to x=1.6173, z=2.9080 at t=0.5, with velocities settling to vx=3.1367, vz=2.9777. Moving into step6, computing drag coefficients and accelerations for the next midpoint estimate.

Continuing the midpoint integration into step 8: velocity and drag values settle with vz approaching nearly zero around t=0.8, position reaching roughly x=2.55, z=3.35, suggesting the projectile is nearing its peak or crossing point.

Stepping forward to t=0.9, vz drops to about -0.98 as the object falls, position updates to x≈2.85, z≈3.30, and speed climbs to roughly 3.20 heading into step 10's drag calculation.

Continuing the integration through t=1.0, position reaches x≈3.16, z≈3.16 with vz now near -1.95, and speed rises to about 3.60 entering step 11's drag terms.

At t=1.1 the trajectory lands around x=3.46, z=2.91, well short of the z=3.05 crossing where x comes out near 3.29 instead of the target 4. So I need to figure out how much to boost initial velocity or angle to compensate for this roughly 0.7 m shortfall, probably using a sensitivity/correction approach rather than re-deriving the full no-drag solution from scratch.

So drag losses scale with t² roughly: ~0.21 in x and ~0.35 in z by t=1. I'm trying to pick a target time near 1.2s and back-calculate the needed drag-free launch velocities by adding estimated loss offsets to the real target (4, 3.05), then iterating to refine.

Trying Lx=0.32, Lz=0.50 for T=1.2, I get vx=3.6 and solve vz from the trajectory equation, getting vz≈8.745. Checking the descent angle with these drag-adjusted velocities against the drag-free case to see if the geometry roughly matches.

Now I'm running the RK2 integration with starting velocities (3.6, 8.745) over a 0.1 timestep, computing drag coefficients and accelerations at the midpoint to update position and velocity for this step.

Continuing the RK4 integration, I'm computing step 4's midpoint velocities and drag coefficients as the projectile's trajectory progresses, updating position and velocity through each substep.

Continuing the numerical integration into step 6 and 7, drag is decreasing as velocity drops, with position now near x=2.06, z=3.40 and vertical velocity slowing to about 2.36 m/s.

Continuing the step-by-step numerical integration, updating velocity and position values through steps 8 and 9 using the midpoint method for drag and gravity forces.

Continuing the drag simulation through steps 11 and 12, updating velocity and position using the midpoint method with drag coefficient scaling by speed squared, tracking x and z position reaching about 3.68 and 3.35 respectively.

At t=1.2, the ball crosses x≈3.9975, z≈3.0439 - remarkably close to the rim plane at z=3.05, with a descent angle around 47.9°. I'm checking whether the RK2 integration with dt=0.1 introduces meaningful error given how precisely the crossing aligns with the rim location.

Now I'm calculating actual clearance: the ball's trajectory line near the rim has slope about -1.108, and I need the perpendicular distance from this line to both the front and back rim tube centers to exceed the combined radius (ball radius plus tube radius, ~0.1274). Computing the cross-product distance gives about 0.1721, which clears the 0.1274 threshold.

Checking the path under the backboard: once the ball drops below the bottom edge height, its x-position stays safely clear of the corner, with distance 0.20 versus the 0.1194 radius threshold—so no collision there either.

Continuing the trajectory past the backboard, the ball's path would actually intersect the support pole around x=5.1-5.3 at a height of roughly 1.5 meters, so I need to account for that collision too, though the net itself isn't modeled in this physics.

I'm also double-checking the apex height relative to the backboard position and confirming the ball's starting rest state on the floor before launch. Now I'm verifying the exact form of MuJoCo's blunt drag force formula from the documentation to make sure my drag model matches.

I'm also wondering whether the ellipsoid fluid model includes added mass effects, since the five coefficients cover blunt drag, slender drag, angular drag, Kutta lift, and Magnus lift but I'm not fully certain added mass is part of that set.

Calculating added mass for the ball gives roughly 0.0043 kg, negligible compared to 0.62 kg mass. But buoyancy from density 1.2 is more meaningful—it works out to about 0.084 N, reducing effective gravity to roughly 9.675 m/s², which over 1.2 seconds would raise the trajectory by about 0.097 m compared to the no-buoyancy case.

This matters: at t=1.2s the height would be 3.141 instead of 3.044, which shifts where the ball crosses the rim plane by roughly 0.026s later, moving x forward by about 0.08 to x≈4.08. Checking the front rim clearance with this shift, it's marginal—about 0.120 vs the 0.1274 needed. I need to verify whether MuJoCo actually applies buoyancy for the ellipsoid fluid model or only for the inertia-box model, since that determines if this correction even applies here.

Working out the margin tolerance: the back rim distance needs |offset| ≤ ~0.065 to stay safe, so I'll nudge vx down slightly (about 1%) to shift the no-buoyancy crossing point to ~3.955, landing on vx=3.564, vz=8.745 as a safer compromise for both buoyancy cases.

That gives crossing x≈3.957 without buoyancy and ~4.04 with it — both comfortably within bounds. Final launch parameters: speed 9.44 m/s at 67.8°.

