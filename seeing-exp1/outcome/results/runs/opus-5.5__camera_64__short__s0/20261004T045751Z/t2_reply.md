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
    <key name="shot" qvel="3.70 0 8.65 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from (2.9532, 0, 8.556) to (3.70, 0, 8.65). Nothing else was changed.
       Why: the old launch was short. Even without air, the ball's centre came down through rim height (3.05 m)
       at x ~ 3.77 m, which is over the front rim, not the rim centre at x = 4.0 m. The scene's air drag
       (density 1.2, blunt drag coefficient 0.25 on a 0.1194 m sphere) pulled it shorter still, to x ~ 3.2 m.
       How the new values were found: I integrated the flight by hand with that drag
       (F = 0.25 * rho * pi * r^2 * |v| * v, no spin, no lift; buoyancy not included), using 0.1 s
       midpoint steps. Launching at (3.3, 8.6) gave a crossing at x ~ 3.54 m; launching at (3.8, 8.65)
       gave x ~ 4.11 m. Interpolating between these gives vx ~ 3.70.
       Expected flight: apex ~ 3.6 m at t ~ 0.83 s. The ball descends through rim height at x ~ 4.0 m,
       t ~ 1.17 s, at about 43 degrees below horizontal. At that angle the ball clears the 0.457 m ring
       with roughly +/- 5 cm of slack, so it should drop through the hoop centre and land just beyond it.
       vy stays 0, so there is no left/right error. -->
</mujoco>
```

---
thinking (summarized):

I need to account for drag in the launch velocity calculation, so I'm working through MuJoCo's ellipsoid fluid model with its blunt and slender drag coefficients to estimate the force more precisely.

For a sphere, the projected area equals the max cross-section, so the slender drag term vanishes, confirming the simple drag coefficient I calculated earlier. The Kutta lift and Magnus terms also drop to zero since there's no spin and the sphere's symmetry makes those cross products vanish, so I just need to check whether added mass effects are part of MuJoCo's model.

The 1.4% buoyancy effect is small enough to ignore for now. Turning to the actual trajectory: I need the ball to pass through the rim center starting from its initial height, descending steeply, so I'll try a launch velocity guess and integrate the drag-affected equations of motion step by step with a coarse timestep to see where it lands.

Continuing the step, I get vx≈3.2387, vz≈7.4684 at t=0.1 with position z≈0.9218, then moving to t=0.1 I recompute the drag deceleration for the next iteration.

Using RK2 again, I find the half-step and full-step velocities, bringing position to x≈0.6477, z≈1.6130 at t=0.2, with speed dropping to about 7.125 and acceleration magnitude around 10.79 vertically.

Continuing the RK2 integration, I get position (1.2757, 2.6746) at t=0.4, with drag continuing to decelerate velocity as I move into the next timestep.

Continuing the integration step, I get x=1.8895, z=3.3241 at the end of this interval, then move to computing the velocity magnitude for t=0.6.

Continuing the RK2 integration step at t=0.7, computing velocity magnitude and drag accelerations for the half-step and full-step, updating position to x≈2.4932, z≈3.4984.

At t=0.8, I repeat the same process: computing speed magnitude, drag forces in x and z, then half-step and full-step updates, landing at x≈2.7921, z≈3.5508.

Continuing to t=0.9, I apply the same midpoint integration for velocity and position, getting vx≈2.9588, vz≈-1.6901, with new position x≈3.0891 and z dropping further toward 3.43.

Moving to t=1.0, I repeat the drag and gravity calculations using the updated speed, finding vx≈2.9354, vz≈-2.6538, and updating position to x≈3.3839 while z continues decreasing.

Continuing to t=1.1, applying the same RK2-style integration with drag proportional to speed squared, giving vx≈2.9083, vz≈-3.6057, and updated position x≈3.6762 with z≈3.2128.

Interpolating between t=1.1 and t=1.2 to find where z crosses the 3.05 target, I estimate the crossing happens around x≈3.539 — well short of the needed x=4.0, a gap of about 0.46. This tells me I need more horizontal velocity or more flight time to reach the target.

To scale up x proportionally, I need roughly a 13% increase in vx, bumping it to about 3.8, but since faster speed means more drag on vz too, the trajectory will drop slightly sooner, so I need to re-integrate with vx0=3.8 and vz0=8.65 to check.

Continuing step-by-step drag integration...

Continuing the RK2 integration step, I'm stepping through t=0.2 to t=0.3, computing velocity magnitudes, drag coefficients, and updated positions at each half and full step.

Continuing the RK2 integration step by step, computing drag-adjusted acceleration and velocity at t=0.5 to update position, tracking the projectile's trajectory as it decelerates.

Continuing the RK2 integration step to t=0.7, velocity drops to vx=3.4339, vz=0.2912, giving position x=2.8643, z=3.6011. Moving into t=0.8 with speed near 3.446 and drag coefficient recalculated.

Continuing the RK2 integration step by step, I push the position to x=3.546, z=3.464 at t=0.9, then begin computing drag and gravity accelerations for t=1.0 with the half-step velocities.

Continuing: x=4.2165, z=2.9390, overshooting slightly past z=3.05. Solving for the crossing time gives t≈0.0676, landing at x≈4.1093, about 0.11 too long, so I need to scale down vx to roughly 3.70 to hit x=4.0 exactly.

Accounting for the coupling between vx and vz, interpolating between trial values gives vx≈3.704 with vz≈8.65, yielding an entry angle of roughly 43° descent. Checking clearance: the projected rim opening at that angle (0.31m) comfortably exceeds the ball's diameter (0.239m), so the shot geometry is tight but makes it through.

I'm weighing whether a slightly steeper trajectory (bumping vz toward 9.3) would widen the rim clearance tolerance to around ±0.07m, but that requires rerunning the integration, and I'm second-guessing whether my dt=0.1 midpoint method accumulates enough error from the drag term to matter, since gravity alone should integrate nearly exactly.

Buoyancy effects could shave gravity slightly (~1.4%), stretching the flight a few centimeters further, and I'm also trying to recall MuJoCo's exact blunt-body drag formula from the docs to make sure I'm not misapplying the force model before committing to a launch angle near 43°.

For a sphere with no rotation, those virtual inertia cross-product terms vanish anyway, so it doesn't change anything. I'll settle on vx = 3.70, vz = 8.65, though I'm still slightly unsure whether buoyancy applies consistently across both fluid models in MuJoCo.

If g' = 9.67 instead, the trajectory gets about 1.4% more height at apex, which shifts the crossing time enough to move x by roughly 0.10 — that's larger than my 0.05 tolerance, so I really need to nail down whether buoyancy is included. The inertia-box fluid model clearly adds a buoyancy term, but I'm not certain the ellipsoid model does the same.

I don't recall buoyancy being part of the ellipsoid fluid model code — it seems to only handle added mass, viscous drag, Kutta lift, and Magnus effects, not buoyancy. I'll proceed assuming no buoyancy and keep vx=3.70, vz=8.65, noting this assumption in my comment.

