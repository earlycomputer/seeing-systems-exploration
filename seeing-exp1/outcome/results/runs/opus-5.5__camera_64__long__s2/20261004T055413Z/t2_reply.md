I changed only the `shot` key's `qvel`, from (3.5952, 0, 10.416) to (3.57, 0, 8.8).

**Why the old shot missed.** It was launched far too steeply and fast. It peaked near 5.6 m and was still above 5 m when it passed over the rim, so it overshot.

**How I chose the new velocity.**
- **Path:** I stepped the flight numerically (0.1 s steps), including the scene's air drag. The ball peaks at about 3.71 m, about 0.85 s in. It comes down through the rim plane (z = 3.05 m) about 1.2 s after launch, at x ≈ 4.0 m, near the rim centre.
- **Entry:** it is falling at roughly 47°, at about 3.4 m/s down and 3.15 m/s forward.
- **Clearance:** it misses the front rim by about 0.1 m and the back rim by about 0.03 m. Its y velocity is zero, so it stays on the rim's centreline.

**One assumption the result depends on.** I took MuJoCo's blunt-drag force to have no factor of ½. If the factor is really ½, drag is half what I modelled, and the ball would come down about 0.3 m farther on, probably clipping the back rim. I have not run this in MuJoCo, so the drop through the hoop still needs confirming by simulation.

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
    <key name="shot" qvel="3.57 0 8.8 0 0 0"/>
    <!-- Changed shot qvel from (3.5952, 0, 10.416) to (3.57, 0, 8.8). The old launch was far too steep and fast:
         the ball peaked near 5.6 m and passed over the rim more than 2 m high, a long miss.
         The new velocity was found by stepping the flight numerically with the scene's quadratic blunt drag,
         taken as F = -rho * 0.25 * pi r^2 * |v| v (no factor of 1/2).
         Result: apex ~3.71 m at ~0.85 s; the ball descends through the rim plane (z = 3.05) at ~1.2 s,
         at x ~ 4.0 m, near the rim centre, falling at roughly 47 degrees. It clears the front rim by ~0.1 m
         and the back rim by ~0.03 m. Zero y-velocity keeps it on the rim centreline.
         If MuJoCo's drag actually carries a 1/2 factor, the ball lands ~0.3 m farther and may clip the back rim;
         this has not been checked in simulation. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to figure out a launch velocity that gets the ball to x=4, z=3.05 while descending, accounting for drag. Starting from z=0.1194 and needing to rise 2.93 m, I'm testing a trajectory with roughly a 55° angle, picking a flight time of T=1.1s and solving for vx and vz components to see if the descent condition holds at the hoop.

Checking T=1.1s, the vertical speed at the hoop comes out only moderately steep (37° entry angle), so I try T=1.2s instead, giving a steeper 46° entry angle and an apex height around 3.65 m, which looks promising.

Now I need to account for drag using MuJoCo's blunt drag model, working out a drag coefficient k from the ball's radius, air density, and the blunt coefficient, then estimating how much this slows the ball down at typical speeds around 9 m/s to figure out how much I need to compensate the initial velocity.

I'm roughly integrating the drag's effect on horizontal and vertical displacement by averaging the deceleration over the flight, weighting it more heavily early in the trajectory where speed is highest, and estimating the horizontal position shift comes out to around -0.15 to -0.18 m.

Now I'm doing a step-by-step numerical integration at 0.2s intervals, computing the no-drag velocity components, speed magnitude, and resulting drag accelerations in both x and z directions at each timestep to get a more accurate correction.

Finishing the Simpson's rule sum, I get Δx ≈ -0.154 m, and now I'm computing the corresponding Δz sum using the same weighted terms.

With drag, the ball lands short at t=1.2 (x≈3.846, z≈2.81 instead of the target), so I need to boost the initial velocities—roughly vx to 3.47 and vz to 8.53 to compensate for the drag losses. I should also double-check the vertical velocity at the hoop by integrating the acceleration profile with Simpson's rule to make sure the timing still works out correctly.

Continuing the position calculation, the ball reaches x≈4.02 at the rim plane height of 3.05, with enough clearance against the rim's inner radius given the ball's size. Checking the front rim edge near x=3.77 confirms the trajectory clears comfortably as the ball descends through the hoop.

Then I trace the back rim concern more closely: at z=3.05 the center sits at x=4.02, and I'm checking distance from the ball's surface to the back rim tube (centered near x=4.2366) to see if it clips as the ball falls at roughly a -1.05 slope, since the tube has such a small radius that any near-miss matters.

Working through the quadratic, the discriminant comes out negative, so there's no contact, and the closest approach gives a distance of about 0.157, comfortably clearing the 0.127 threshold. To stay safely away from that margin, I decide to aim the shot so it crosses slightly shorter, around x=3.98, rather than right at the rim's edge.

Given roughly ±0.05m uncertainty in my drag modeling, I pick vx=3.46 and vz=8.55, which puts the ball at x≈3.99 at t=1.2s — close enough to target. I also double check the trajectory clears the front rim and backboard area without issue, since the ball's height at x=3.77 is well above rim level.

Then I turn to nailing down MuJoCo's exact blunt drag formula, trying to recall whether it's written as a half-factor times drag coefficient, density, area, and velocity squared, to make sure my force calculations match the simulator's actual physics model.

The default blunt coefficient of 0.5 makes me lean toward no extra ½ factor in the formula, which would double the drag coefficient to about k=0.0217, shifting the estimate to roughly Δx≈-0.31, Δz≈-0.48. That's a meaningful uncertainty of about 0.15 m in x, so I need to pin down the exact formula MuJoCo uses before trusting this.

With this drag coefficient, I'll iterate numerically using midpoint integration with a 0.1 timestep, starting from guessed launch velocities vx=3.6, vz=8.8, tracking position and velocity through each acceleration update to see where the trajectory crosses the target point.

Continuing the step-by-step integration, I compute the next iteration's velocity and drag terms, updating position and velocity values to vx≈3.4985, vz≈7.0990, with new x and z estimates around 0.7062.

Continuing the RK2 integration into step 4: updating position to x=1.0505, z=2.2526 with velocities vx=3.4191, vz=5.4855 at t=0.3, then computing midpoint accelerations using drag proportional to speed for the next step.

Continuing the RK4 integration, I'm updating position and velocity at t=0.5s, then computing the next midpoint drag forces for step 6 of the trajectory simulation.

Continuing the RK4 integration, position updates to x=2.3866, z=3.6218 at t=0.7, with velocity dropping to vx=3.2786, vz=1.4096 as drag continues decelerating the projectile.

Continuing the midpoint integration for step 10, updating position to x=3.0375, z=3.7062 with velocities vx=3.2318, vz=-0.5586 at t=0.9, then computing step 10's acceleration terms using drag proportional to speed.

Continuing the trajectory simulation, I update position to x=3.6791, z=3.3999 with velocities vx=3.1820, vz=-2.4964 at t=1.1, then begin computing the next midpoint step with updated drag forces.

Checking where z=3.05 lands, I estimate x reaches about 4.04, slightly past my target center around 3.98-4.0. I'm considering trimming vx slightly to shift the crossing point closer to 4.005, which looks acceptable, then returning to the entry angle analysis from the earlier ~45° clearance check.

I'm now worried about whether the drag formula actually includes a ½ factor — if it does, the crossing point would drift significantly farther, maybe out to x≈4.37, which risks hitting the back rim or backboard. I'm trying to recall MuJoCo's documented drag force formula to settle whether that ½ is included, since this materially changes my trajectory predictions.

Settling on qvel="3.57 0 8.8 0 0 0" as the final answer, giving an apex around 3.71 m, safely under the backboard's 3.95 m top — so it shouldn't interfere. Time to write up the explanatory comment.

