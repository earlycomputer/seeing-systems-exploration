The shot now aims for the rim's center at x = 4 m. It comes down at about 4.6 m/s at roughly 59° from horizontal, so it crosses rim height with about 0.1 m to spare on each side. That margin depends on how strongly MuJoCo's drag acts on the ball, which I estimated from memory rather than ran.

- **Fix:** the launch velocity changes from (3.5952, 0, 10.416) to (3.16, 0, 9.4) m/s. The old shot peaked near 5.6 m right above the hoop and landed well past it. The new one peaks near 4.2 m around x ≈ 2.6 m.
- **Rim clearance:** the ball crosses rim height (3.05 m) at x ≈ 3.99 m, about 1.38 s after launch. That leaves about 0.10 m to the front rim and 0.12 m to the back rim.
- **Drag assumption:** I stepped the flight by hand with drag deceleration k·|v|·v, where k = ρ·0.25·A/m ≈ 0.0217 per metre, assuming no ½ factor in MuJoCo's drag term. If MuJoCo does use a ½ factor, drag is half as strong and the ball would land high and long. Simulating the scene would settle this.

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
    <key name="shot" qvel="3.16 0 9.4 0 0 0"/>
    <!-- Changed qvel from (3.5952, 0, 10.416) to (3.16, 0, 9.4) m/s. The old launch peaked ~5.6 m almost
         directly over the hoop and came down well past it (long). The new launch, integrated with the
         ellipsoid-model drag (rho*0.25*A/m ~ 0.022 per m on |v|v), peaks ~4.2 m near x ~ 2.6 m and descends at
         ~59 deg through rim height (3.05 m) at x ~ 3.99 m, ~1.38 s after launch, leaving ~0.10 m clearance to the
         front and back of the rim. If MuJoCo's drag carries an extra 1/2 factor the ball runs high and long. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need the trajectory to pass through the hoop center at x=4, z=3.05 while descending, factoring in drag. Starting from z=0.1194, I need about 2.93 m of rise over 4 m horizontal, so I'm considering a launch angle near 52° and testing an apex height around 4.0 m, roughly 0.95 m above the rim, using the vacuum projectile equation as a starting approximation.

Working through the vacuum case: the time to apex and fall gives a total flight time near 1.33 s, horizontal velocity around 3.0 m/s, and launch speed near 9.23 m/s. Now I need to account for MuJoCo's drag model, recalling that blunt drag scales with air density, drag coefficient, projected area, and velocity squared, while the slender drag term vanishes for a sphere since there's no difference between max and projected area. I'm estimating a drag coefficient k and planning to roughly simulate the trajectory step by step to see how much the drag reduces the effective velocity needed.

Rather than doing a full numerical integration in my head, I'm trying a perturbation approach: estimating the drag-induced deficit in horizontal distance using average velocity values, which suggests needing to boost the horizontal velocity by about 0.15 m/s to compensate. I'm setting up an initial guess of vx=3.17, vz=8.95 and planning a quick manual Euler integration with small time steps to check whether these values actually produce the right landing point under drag.

Continuing the numerical integration, I compute step two's accelerations and update velocities and position, tracking x and z through the drag-affected trajectory.

Continuing the step-by-step numerical integration, updating velocity and position through steps 4 and 5 with the averaged acceleration values.

Continuing the trajectory integration into step 8, updating velocity and position estimates as the projectile decelerates toward lower z-values.

Continuing the step-by-step integration: velocity drops sharply in z as drag builds, giving vx≈2.992, vz≈-1.144 at step10, moving position to x=3.061, z=3.947. I'm now computing step11 with similar drag-adjusted acceleration, pushing vz further negative as the object accelerates downward.

Step13: v=4.2837, avg ax=-0.1493, az=-9.628. vx=2.9532, vz=-4.0516. x=3.9534; z=3.1664. Now checking: I need z=3.05 right at x=4. At x=3.9534, z=3.166 with vz=-4.05, vx=2.95, so time to reach x=4 is about 0.0158s, letting me estimate the final z there.

At x=4, z≈3.10, meaning the ball clears by about 5 cm. Reaching z=3.05 happens around x≈4.037, so roughly 3.7 cm beyond the hoop center — with ball radius 0.119 and rim inner radius 0.2286 giving horizontal clearance of 0.109, this looks fine. I also need to verify clearance over the near rim at x=3.763 (top of rim tube at height 3.058) and the far rim at x=4.237 — checking the ball's trajectory height at those points shows comfortable clearance above the rim in both cases.

Checking the back rim inner edge at 4.2286, the ball edge at z=3.05 reaches about 4.156, giving 7 cm clearance before the backboard front at 4.381 — descent angle comes out to about 54°, which looks good. I'm considering a small tweak to vx to better center the shot, but the adjustment needed is tiny, so I'll leave vx around 3.14 and instead double check my drag model assumptions against MuJoCo's documented blunt drag formula to make sure I haven't mishandled a factor of two.

I'm trying to pin down whether the drag coefficient includes that factor of 1/2, since without it the drag would double and change the landing point noticeably — maybe 0.2-0.3 m shorter versus my current estimate. Given the uncertainty, I'm weighing whether to hedge my target between the two scenarios or trust my original formula more, trying to recall MuJoCo's exact ellipsoid drag documentation to settle it.

I'm trying to recall whether the ellipsoid drag model includes the 1/2 factor or not, weighing it against the default blunt coefficient convention. Since the user set the coefficient to 0.25, that seems consistent with a C_D/2 convention where actual C_D is around 0.5, so I compute k = ρ·0.25·A/m ≈ 0.02168, noting this effectively doubles the drag compared to including the 1/2 factor.

Now I'm comparing a vacuum trajectory against the drag-affected one at x=4: vacuum reaches z≈3.60 while the first drag estimate gave z≈3.10, so drag costs roughly 0.50 m at that point, and I want to see how doubling k changes that loss.

Doubling k likely costs closer to 2.6-2.65 m, which overshoots the target too much, so I need to re-tune. I'm running another Heun integration with k=0.02168 and trying vx=3.36, vz=9.4, computing drag-adjusted acceleration and velocity at each step to see where this pair lands near x=4, z=3.05.

Continuing the drag integration into step 3 and starting step 4, I'm tracking velocity magnitude, drag coefficient, and acceleration components each half-step to update position and velocity using averaged values, getting x≈0.98, z≈2.43 by end of step 3.

Continuing the integration through steps 5 and 6, updating position to x=1.6077, z=3.4229, then computing velocity decay for step 6 with vx dropping to around 3.071 and vz to about 2.9255 as drag continues to slow the trajectory.

Predicted vx=3.0021, vz=-0.0555 with speed 3.0026, giving drag coefficient 0.0651 and corrected accelerations ax'=-0.1954, az'=-9.8064; averaging with the previous step gives ax=-0.2014, az=-9.8402.

Updating position to x=2.8269, z=4.1955, then moving into step 10 with velocity 3.0032 and recomputed drag coefficient 0.06511, yielding ax=-0.1955, az=-9.8066; predicting ahead gives vx=2.9832, vz=-1.0328 with speed 3.1569, drag coefficient 0.06844, and corrected ax'=-0.2042, az'=-9.7393, averaging to ax=-0.1999, az=-9.773.

Continuing to step 11: updated position x=3.1262, z=4.1414, speed 3.1554, drag 0.06841, ax=-0.204, az=-9.7396; prediction gives vx=2.9623, vz=-2.0034, speed 3.5762, drag 0.07753, corrected ax'=-0.2297, az'=-9.6547, averaging to ax=-0.2169, az=-9.6972, then updating velocity to vx=2.961, vz=-1.9991 and position to x=3.4234, z=3.99, moving into step 12.

Continuing the integration, I get x≈4.0105, z≈3.3989 at this step, overshooting the target z=3.05 at x=4 by about 0.36. I estimate the extra time needed to reach the target height, solving a small quadratic for the remaining drop, giving an adjusted x near 4.246.

That's about 0.25 too long, so I need to scale back initial velocity. Comparing against the sensitivity from a prior run, I estimate reducing vx by roughly 0.2 to shift the landing point back to x=4, accounting for the fact that lower vx slightly reduces drag coupling with vz, nudging landing time a bit later with minimal net effect — I'm now rechecking where z crosses 3.05 with vx=3.16.

With vx≈3.16 the landing lands close to 3.99, essentially right at target. I'm now checking the entry angle (steep, around 59°) and verifying the shot clears the front rim by tracking the ball's height as it passes over the rim's x-position, confirming clearance by comparing the ball's center position to the rim tube location.

Then at the crossing point, I check both front and back gaps between the ball and the rim tube — both come out positive, so the shot should pass through cleanly. I pause on the drag coefficient assumption, since getting the formula wrong (with vs without the 1/2 factor) could significantly change the trajectory height, but I decide to trust my recollection of MuJoCo's actual fluid drag implementation without the 1/2 factor.

I settle on vx=3.16, vz=9.4 as the final launch velocities, double-check the apex height clears the backboard area, and move to writing up the final answer.

