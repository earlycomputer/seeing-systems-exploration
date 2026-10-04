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
    <key name="shot" qvel="3.62 0 8.75 0 0 0"/>
    <!-- Changed shot qvel from (3.21, 0, 9.3) to (3.62, 0, 8.75).
         Why: the old launch was too steep. Its apex was ~4.5 m and it was still ~1 m above the rim at x = 4.
         It only came down to rim height near x = 4.8, past the backboard face (x = 4.38), so the shot went long.
         New shot, integrated with the scene's quadratic air drag
         (fluidcoef blunt 0.25, rho 1.2, A = pi r^2, k ~ 0.0217 /m):
         - apex ~3.67 m near x ~ 2.8
         - descends through z = 3.05 at x ~ 4.0, about 1.1 s after launch
         - entry angle ~48 deg below horizontal
         - clears the front rim by ~0.25 m vertically and keeps ~0.2 m from the back rim and bracket.
         These numbers are hand-integrated (0.1 s steps) and assume MuJoCo's blunt drag has no extra 1/2 factor.
         Re-run the simulation to confirm; if the ball still clips the back rim, reduce vx slightly. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to find the launch velocity so the ball reaches the rim at x=4, z=3.05 while descending, ignoring drag for now. With height difference of about 2.93 and horizontal distance of 4, I'm testing a time of 1.1 seconds, which gives roughly vx=3.64 and vz=8.06.

Checking t=1.1s, the ball descends at a 37° entry angle — close to the minimum needed for the ball to clear the rim opening given its radius versus the rim's inner radius, but marginal. Trying t=1.2s instead gives vx=3.33, vz=8.33, descending at about 46°, which clears comfortably with an apex height near 3.65m.

Now I need to account for drag using MuJoCo's ellipsoid fluid model — recalling the blunt and slender drag force formulas with the given coefficients (0.25 for blunt, implying an effective Cd of 0.5, and slender drag contributing nothing for a sphere since projected area difference is zero), plus angular drag and Kutta lift terms.

I'm computing the drag coefficient k using the ball's mass, air density, and cross-sectional area, getting roughly 0.0217 per meter, which at a 9 m/s velocity gives a deceleration around 1.76 m/s² — significant enough that I need to numerically integrate the trajectory with drag included rather than rely on the vacuum parabola, starting with initial velocity guesses around vx=3.45, vz=8.65 and refining from there.

Now I'm stepping through the integration with a smaller timestep, computing speed magnitude and the resulting drag accelerations on each axis, then comparing against the simpler no-drag estimate to see how much the launch angle and speed need adjusting to still hit the target.

Continuing the integration through t=0.3, I'm tracking position and velocity decay from drag and gravity, now at x≈1.29, z≈2.57 with velocity around (3.14, 4.02).

Continuing the step-by-step integration, I find the velocity peaking near zero vertical speed around t=0.7-0.8, with horizontal position reaching about x=2.5-3.0 and height stabilizing near z=3.3-3.4, as drag continues to taper off.

I'm getting x=3.4239, z=2.9445, falling short of the target landing point by about 0.7 m, so I need to increase the initial velocity. Let me reconsider the sensitivity between speed and landing distance, but I'm noticing a discrepancy in my x-position calculations that suggests I made an arithmetic error somewhere in the step-by-step integration—I should recheck the numbers from the earlier steps.

Crossing happens around t≈1.056, giving x≈3.29, which is about 0.71 short of the target. I need larger velocities — drag cost roughly 0.1s of flight time and slowed horizontal distance, so let me try vx=3.8, vz=9.0 and re-integrate with the drag coefficient.

Stepping through the RK2 integration, x reaches about 0.376 and z about 0.961 at the second step, with velocity decaying to roughly (3.69, 7.29) by the next half-step as drag continues reducing both components.

Continuing the step-by-step numerical integration through timesteps 4 through 6, updating velocity, drag-adjusted acceleration, and position values each half-step as the object's speed decays and its trajectory curves downward.

Continuing the step-by-step integration, I'm tracking position and velocity through t=0.9 and into t=1.0, with drag decelerating the x-velocity and gravity minus drag adjustments shifting the z-acceleration from negative to positive as the vertical velocity turns downward.

By t=1.2, x reaches about 4.2 and z about 3.31, overshooting the target of z=3.05 at x=4, so I need to interpolate between two trial trajectories to find the throw velocity that lands precisely at the desired crossing point.

I should also verify the ball clears the rim's front edge, not just reaches the hoop center, so I'm checking the inner boundary at x≈3.77. Running the trajectory forward with initial velocity (3.624, 8.747), I'm stepping through drag-adjusted acceleration terms to track position and speed decay over successive small time increments.

Continuing the step-by-step velocity and position integration through timesteps 4 and 5, tracking the decreasing drag deceleration as speed drops toward roughly 4.4 units.

Continuing the trajectory integration, I track velocity peaking around t=0.8 before gravity pulls it downward, reaching x≈3.38, z≈3.55 by t=0.9 with vertical velocity now swinging negative.

Pushing further to t=1.1, the position settles near x≈4.02, z≈3.05 with velocity around (3.17, -3.49), giving me a landing estimate near this point.

Checking entry angle: atan(3.49/3.17) comes out to about 48°. Now verifying clearance against the rim tubes—front rim at x≈3.76 and back rim at x≈4.24, both with small tube radius—to confirm the ball's trajectory passes safely through without clipping either side.

Checking the backboard bracket clearance too — the ball's edge stays far enough from the bracket corner and backboard face throughout the trajectory, with enough margin to absorb small integration errors from the dt=0.1 midpoint step.

I'm now second-guessing my drag coefficient assumption, since if MuJoCo's blunt drag formula omits the ½ factor I used, the ball would travel noticeably farther and potentially hit the backboard instead of clearing it. I'm trying to recall the exact MuJoCo documentation formula for blunt drag force to pin down whether my calculation used the right constant.

