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
    <key name="shot" qvel="3.505 0 8.52 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from (2.9532, 0, 8.556) to (3.505, 0, 8.52). The old launch fell short: even in vacuum
       its centre crossed rim height (descending) at x of about 3.77 m, over the front rim, against the rim centre
       at x = 4.0 m, and the enabled air drag made it shorter still. New aim: a vacuum arc through the rim centre
       (4, 0, 3.05) entering at about 45 degrees down, which needs (3.365, 8.296) and about 1.19 s of flight.
       I then corrected for the ellipsoid fluid drag on a sphere: F = 0.5*rho*0.25*pi*r^2*v^2, about
       0.0108 v^2 per kg of ball. Integrated along the arc, drag costs about 0.15 m in x and 0.25 m in z by the
       hoop, so vx and vz are raised by about deficit/flight time, plus a few percent because drag grows with
       the higher speed. Expected result: the ball clears the front rim by about 0.1 m, drops through the
       centre at roughly 45-50 degrees, and passes under the backboard's bottom edge with about 6 cm to spare.
       After that it may strike the support pole before landing, which is after the make. These figures are
       hand estimates from an integration of the drag, not a run of the simulation. -->
</mujoco>
```

---
thinking (summarized):

I need to account for drag using MuJoCo's ellipsoid fluid model, where the blunt drag force scales with fluid density, velocity squared, and a drag coefficient like F_drag = -½ ρ |v| v.

For a sphere, the projected area equals the max cross-section, giving a drag coefficient per unit mass around k ≈ 0.0108 per meter. I'm checking whether added mass, Kutta lift, Magnus lift, or buoyancy matter here, but since they're all under 2% of the dominant forces (weight and drag), I can safely neglect them for this calculation.

Now I'm working out the launch trajectory to pass through the rim center at (4, 0, 3.05), aiming for a steep descent angle near 45°. I'm setting up the parabolic equations relating launch angle, velocity, and the height/distance constraints to solve for the entry slope at the target.

Solving these gives a launch angle around 67.9°, with horizontal velocity near 3.37 and vertical velocity near 8.3, giving a flight time of about 1.19 seconds.

Now I need a drag correction. Using the no-drag trajectory as a first approximation, I'm computing the speed profile over time and preparing to numerically integrate the drag-induced deficit in both horizontal and vertical displacement using small time steps.

Continuing the table through t=1.1887, then setting up the weighted integrand for the displacement deficit integral, multiplying (T-t) by ax at each sample point to prepare for numerical integration.

Using trapezoid approximation with h=0.2 over the main interval plus a small correction for the leftover segment, getting Δx roughly around -0.15, then starting to tabulate the corresponding integrand values for the z-component.

So with drag, the ball lands short and low relative to the no-drag trajectory, meaning I need to correct the launch velocity by increasing both vx and vz, using the sensitivities ∂x/∂vx = T for the horizontal component.

Roughly bumping vx by about 0.135 and vz by about 0.21 should compensate for the deficit, giving vx≈3.50, vz≈8.506 — with buoyancy and added-mass effects contributing only small corrections on the order of a centimeter.

Since there's no spin, the added-mass gyroscopic terms and Magnus/Kutta lift all vanish for this symmetric sphere, so I don't need to worry about them. The entry angle tolerance of roughly ±2 cm looks comfortable, but I want to double-check the drag integral's accuracy by refining the trapezoid estimate with a midpoint evaluation partway through the fall.

Refining with a smaller step size, I'm getting velocity components and weighted accelerations that confirm the trapezoid approximation is close enough—position changes of about -0.247 in z and -0.154 in x match the coarser estimate within acceptable error. Now I should verify the ball clears the rim and backboard given its steeper-than-45° descent angle caused by drag.

Continuing past the rim, I need to check whether the ball clears the support bracket and pole after the shot — tracing the descending trajectory, it looks like it could get close to a pole positioned around x=5.1–5.3, so I'm working out the fall time from rim height to see if there's a collision there.

Checking the backboard's bottom edge coordinates, I'm calculating whether the ball's trajectory clears it as it passes by—the distance from the ball's center to the edge comes out just over the ball's radius, so it clears by a small margin.

Since the ball bounces off the pole afterward, the simulation would just continue until it actually lands, so that's acceptable behavior. I'll go with the final velocity of 3.50 horizontal and 8.506 vertical, which should give a clean clearance given the drag effects are small at this scale.

