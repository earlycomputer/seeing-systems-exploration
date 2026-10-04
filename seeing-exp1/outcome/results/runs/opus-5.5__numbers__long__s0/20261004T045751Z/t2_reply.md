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
    <key name="shot" qvel="3.6 0 8.76 0 0 0"/>
    <!-- Changed shot qvel from "3.5952 0 10.416 0 0 0" to "3.6 0 8.76 0 0 0".
         Why: the old launch was far too strong. The simulated ball crossed x = 4 m about 1.7 m above
         the rim, flew over the backboard, rolled across the top of the support pole and landed near
         x = 6.1 m, a long miss.
         How the new value was found: the logged trajectory fits gravity plus quadratic air drag,
         a = -g z - k|v|v with k ~ 0.022 1/m. A hand integration with that k reproduces the logged
         path to within ~1 cm at t = 0.2 to 1.2 s.
         Predicted result (by that same model, not re-simulated): the ball peaks near 3.68 m and
         reaches the rim center (x = 4.0) at z ~ 3.04-3.05 m, about 1.2 s after launch. It descends
         at ~48 deg, steep enough to clear the front and back rim. y stays 0, so it is centered left/right. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to figure out the launch velocity accounting for drag. Without drag, the apex height would be about 5.65m, but the observed trajectory shows a lower apex around 5.01m, suggesting drag is reducing the ball's height noticeably—I should use that discrepancy to estimate the drag coefficient.

Looking at the early position data, I can back out the effective deceleration in both x and z directions, which come out proportional to the velocity components, consistent with quadratic drag along the velocity direction. Comparing this estimated drag coefficient to the known physical value for a basketball suggests my computed k is larger than expected, so something else may be contributing to the extra deceleration beyond simple drag.

Measuring vx across the finer intervals, I see it actually rises slightly from 3.44 to 3.52 before gradually decreasing to 3.00 by late flight. That early uptick suggests some initial transient, possibly from contact with the floor at launch causing a brief slowdown before the ball frees up.

Setting that aside, I'll focus on fitting the mid-flight vertical velocity data, which shows a steady decline across each interval consistent with gravity's deceleration pattern.

Continuing through the deceleration values across each interval, the per-step change stays fairly consistent, hovering around 9.2 to 11.6 throughout the range down toward the end.

I'm checking whether a simple quadratic drag model with coefficient k≈0.02 reasonably explains these observed decelerations, testing it against both vertical and horizontal velocity changes near the apex and finding the fit roughly consistent, with no need to invoke spin/magnus effects.

But there's an anomaly in the very first interval — the early vz and vx averages come in lower than extrapolation would predict, suggesting something slows the ball more than drag alone right at launch, possibly an added-mass effect in the fluid model that isn't being captured by the simple drag force.

I'm working through the rolling physics: friction at the contact point opposes the forward sliding motion, which creates a torque that spins the ball with positive angular velocity about the perpendicular axis — consistent with the ball transitioning into rolling motion as it moves in +x.

This topspin then interacts with velocity through the Magnus effect, producing a force that pushes the ball forward while adding extra downward deceleration — which matches the observed early drop in vertical velocity. Later, as the ball descends, that Magnus force direction flips, which explains why the horizontal deceleration changes between early and later phases. The initial floor impact with soft contact dynamics also appears to cause an impulsive loss of energy at the very start.

Given this, my practical approach is to scale the launch conditions to compensate: I need to find a new trajectory that crosses the hoop's horizontal position while descending, clearing both the front and back rim edges with enough vertical margin given the ball's radius relative to the hoop's inner radius.

I'll try calibrating using an effective gravity-like constant derived from the observed trajectory, then keep the same steep launch angle (around 71°) but reduce the speed so the arc apex is lower, solving for the angle and velocity needed to pass through the target point.

Comparing to the observed data, I see the no-drag prediction overshoots height notably by x=4, confirming that drag/spin losses are substantial and need to be factored into the final velocity estimate.

Checking the x-deficit matches the z-deficit ratio, it lines up with vz/vx, suggesting about a one-timestep logging delay rather than an actual velocity loss — just a small positional offset. The vx decay from 3.595 to 3.52 over that interval looks consistent with a modest drag coefficient rather than any real discontinuity.

With k≈0.018-0.02, the vertical drag decel of about 2.3 at v=11 matches the observed excess early deceleration, so Magnus force isn't needed to explain it. The 0.9 m vertical deficit at x=4 and the extended travel time to 1.22s instead of 1.113s both seem roughly consistent with this same drag coefficient acting over the horizontal slowdown too.

Checking horizontal velocity decay from 3.595 to 3.0 over the path length gives ln(3.595/3.0)=0.181, and dividing by the estimated arc length of about 7.9 yields k≈0.023, confirming k≈0.022 as a consistent value across both horizontal and vertical motion. Now I want to numerically integrate a new trajectory with this k to pick an appropriate v0, stepping through small time increments manually.

For the drag-free estimate, picking vx0=3.6 and solving for vz0 that reaches the target point gives vz≈8.09, so I'm bumping it up to vz0=8.6 to account for drag, then stepping through time in 0.1s increments tracking position and velocity.

Continuing the midpoint integration to t=0.2: velocity drops to vx=3.471, vz=6.365, with position at x=0.706, z=1.612. Pressing on with the next half-step calculation for drag deceleration.

Continuing the integration, I get vx≈3.339, vz≈3.233 at t=0.5, with position updating to x≈1.726, z≈3.045, as drag continues decelerating the projectile.

Stepping forward further, I compute vx≈3.308, vz≈2.226 at t=0.6, giving x≈2.058, z≈3.318, then continue the half-step integration toward t=0.7 with velocities settling near vx≈3.294, vz≈1.726.

Continuing position/velocity integration...

Continuing the integration through t=1.2, I find x≈3.997, z≈2.884 — meaning the projectile lands short of the target at x=4, falling about 0.17 below the required height of 3.05.

I'm checking whether this trajectory clears the front rim at x=3.763, z=3.05, computing entry angle around 49° and the perpendicular distance from the rim tube to the descending flight path, which comes out to roughly 0.179.

Checking the back rim similarly gives comparable clearance, so I need to bump vz0 up by about 0.17 to raise the apex height at x=4 and reduce vx slightly for drag coupling, landing around vz0≈8.8 — though I should sanity-check this against the original trajectory's observed apex of 5.01 at t≈0.98 to validate my drag coefficient estimate.

Since it's just a time shift of the trajectory, the path stays the same, so I can ignore that. I'll also ignore Magnus/spin effects since y=0.

Trying vz0=8.8 instead, I'm linearizing the vz perturbation decay using the drag coefficient, estimating that over the 1.2s flight the perturbation averages around 0.93 of its initial value, giving δz roughly 0.93*1.2*δ.

The horizontal coupling effect on δx turns out negligible, around -0.03δ. To hit z(4)=3.05 with a small margin, I'm solving δ=0.17/1.12≈0.15, suggesting vz0 should be about 8.75-8.76, though I want to double check the vertical tolerance at x=4 to make sure this choice is robust.

I'm finding that the ball passes if the perpendicular offset stays within about ±0.052, which translates to a z-tolerance near ±0.079 at x=4 — and since sensitivity to vz0 is roughly 1.12 per m/s, that gives me about ±0.07 m/s of margin, meaning model errors could matter. I want to sanity-check my integrator against the original trajectory by running a coarser calculation with vx=3.595, vz=10.416 out to t=1.2 and comparing against x=3.931, z=4.775, so I'm setting up a midpoint integration with dt=0.2 to validate this.

At t=0.2 my integration gives x=0.702, z=1.956, which matches the observed values (0.696, 1.945) closely enough that the small offset is explainable by delay — this confirms my drag model is tracking correctly. I continue stepping forward with the same midpoint method to extend the trajectory further.

At t=0.4 my numbers (1.377, 3.340) still line up well with the observed data (1.373, 3.337), so the model keeps holding. But by t=0.6 I get z=4.103 versus an observed value of 4.301 — a 0.2 discrepancy that's much larger than before, which makes me suspect my coarser step size at this stage is introducing integration error.

Cross-checking against the velocity data directly: observed vz around t=0.4 looks closer to 5.87 rather than my computed 4.86, and the interval from 0.2 to 0.4 implies an average deceleration near 11, which doesn't match what I'm assuming.

Fixing the arithmetic, I recompute vz(0.4) as 5.860 instead and carry this through the velocity, position, and acceleration updates for the next half-step, recalculating speed and drag terms accordingly.

Continuing the integration through t=0.6 and t=0.8, I get x,z positions of roughly (2.033, 4.298) and (2.675, 4.849), which line up closely with the observed values (2.031, 4.301) and (2.674, 4.855), confirming the drag model is tracking well.

At t=1.0 the computed position is (3.307, 5.003) versus observed (3.307, 5.011), still a very tight match. Pushing forward to t=1.2, I'm getting velocities around vx=3.094, vz=-2.155, landing near x=3.931, z≈4.7-ish, continuing to verify against the trajectory data.

Continuing the vz integration through t=1.2, values go negative as expected, then I'm summing the z displacement terms across all the timesteps to get a running total near 3.3.

Now I'm cross-checking the x displacement sums, confirming they land close to 4.0, then running a fresh midpoint integration with dt=0.2 starting from vz0=8.76 to validate the trajectory, computing drag-adjusted accelerations at each half-step.

Continuing the trajectory integration, I'm stepping through the velocity and position updates at each time increment, accounting for drag deceleration as the projectile slows and descends toward its landing point around t=0.6s.

Continuing to x=4, z lands around 3.037-3.047, close to the 3.05 target with entry angle near 48°, which is good. I'm checking the trajectory stays clear of the front rim and confirming the ball passes through the hoop zone between the backboard bounds before reaching the basket.

Checking the rim clearance confirms the ball passes through with enough margin given the inner radius versus ball radius. The pole and backboard are clear too, so I'll settle on qvel="3.6 0 8.76 0 0 0".

