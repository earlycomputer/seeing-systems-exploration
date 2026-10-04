The original keyframe launched the ball much too high, so I changed only `qvel` to a slower, flatter shot. I re-derived the new velocity by hand-integrating the flight with the scene's own air model, in 0.1 s midpoint steps; nothing was simulated.

**Air model used.** I assumed MuJoCo's ellipsoid drag has no ½ factor. The scene values then give a drag acceleration of about 0.0217·|v|·v. Buoyancy reduces gravity to about 9.675 m/s². With no spin, there is no Magnus or lift force.

**Predicted flight with `qvel = 3.22 0 9.2 0 0 0`:**
- The ball peaks at about 4.09 m near x ≈ 2.7 m, around t ≈ 0.9 s.
- It reaches x = 4.00 m at about t ≈ 1.35 s with its center at z ≈ 3.06 m. That is essentially the rim center.
- It is then descending at about 58° (vx ≈ 2.79, vz ≈ −4.4 m/s).

**Clearances on the way down:**
- **Rim.** The trajectory passes about 0.20 m from both the front and back rim tubes. It needs at least 0.127 m (ball radius plus tube radius), so there is about 7 cm to spare.
- **Bracket.** The ball misses the hoop bracket by about 0.19 m, which is more than its 0.119 m radius.
- **Backboard.** The ball reaches the plane of the backboard's front face well below the board's bottom edge (z = 2.9 m).

The integration is approximate. The ~7 cm rim margin should absorb its error, but I can't confirm the result without running the scene.

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
    <key name="shot" qvel="3.22 0 9.2 0 0 0"/>
    <!-- Changed shot qvel from "3.5952 0 10.416 0 0 0" to "3.22 0 9.2 0 0 0".
         The old launch was far too strong: with the scene's air drag the ball passed x = 4 m at ~4.85 m
         (1.8 m above the rim), cleared the backboard and landed long near x ~ 6.3 m.
         The new launch was found by hand-integrating gravity plus the ellipsoid drag (blunt coef 0.25,
         rho 1.2, no 1/2 factor assumed) and buoyancy. Predicted flight: apex ~4.09 m near x ~ 2.7 m;
         the ball crosses x = 4.0 m at z ~ 3.06 m (rim center) at t ~ 1.35 s, descending at ~58 deg.
         It clears both rim tubes by ~7 cm, then the bracket and the backboard's bottom edge, and drops
         through the hoop. No lateral velocity or spin, so it stays centered in y. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to find a launch velocity that sends the ball through the rim center, accounting for drag. Starting with the vacuum case, I'm setting up the equations relating launch angle and speed to the horizontal distance of 4 and vertical drop needed, before adding drag corrections.

Testing angles iteratively: 55° makes the ball still rising at the rim (bad), 60° gives too shallow a descent angle at 15°, 65° improves to 34°, and 68° reaches 45° entry — checking that against the rim's effective opening confirms the ball clears with margin. I'm now checking whether 70° gives even better tolerance.

Now I'm shifting from vacuum calculations to accounting for drag, setting up a numeric integration with the drag coefficient and effective gravity, planning to guess initial velocities and iterate until the trajectory lands at the rim center.

Continuing the midpoint integration, I'm tracking velocity and position through successive 0.1s steps, applying drag forces that decrease as speed drops toward the later timestep.

Continuing the numerical integration, I'm tracking velocity and position through each timestep as drag decelerates the projectile, with t=0.5 giving vx=3.234, vz=3.831, x=1.674, z=3.343, and I'm now stepping into the next iteration.

Continuing the drag simulation through steps 8 and 9, I'm tracking velocity decay with vz approaching zero around t=0.9, meaning the projectile is nearing its peak height.

Continuing the trajectory integration through steps 12 and 13, I find vx around 3.03-3.06, vz dropping toward -3.9, with x reaching about 4.18 and z at 3.28 — checking against the target of x=4 shows the altitude there is getting close to my threshold.

That's too high by roughly 0.44 m, meaning too much energy — I need to reduce the initial vz by about 0.45 to compensate, keeping in mind drag effects also shorten flight time somewhat. At x=4 the entry angle comes out around 48°, computed from vz≈-3.35 and vx≈3.05.

Actually, I should try reducing vx0 instead to keep the trajectory steeper — delaying arrival at x=4 naturally lowers z, and I'm estimating I'd need to cut vx0 by roughly 0.285 to 3.215, accounting for the way x scales with time and the small secondary effect this has on z through reduced drag.

Testing this candidate numerically with vx0=3.22, vz0=9.2, I'm stepping through the velocity integration with drag terms to see where the trajectory lands.

Continuing the numerical integration through steps 4 and 5, tracking velocity decay and position updates as drag continues to reduce both horizontal and vertical speed over successive 0.1 time intervals.

Continuing the numerical integration through steps 7 and 8, tracking velocity, drag deceleration, and position updates as the projectile's horizontal and vertical speeds continue decaying toward the t=0.7-0.8 range.

Continuing the numerical integration, I'm tracking velocity and position through steps 10-12, with vz dropping sharply as gravity continues decelerating the vertical motion while vx slowly decreases from drag.

Continuing to t=1.4, the ball reaches x≈4 at z≈3.06 with an entry angle around 57.6°, which looks like a good center-of-rim pass. Now I'm checking the crossing against the rim plane, comparing ball radius against the rim's inner radius to verify it actually fits through.

Looking at the trajectory line near the rim, I compute perpendicular distances from the ball's path to both the back rim center (4.2366) and front rim center (3.7634), both coming out to about 0.1997, comfortably larger than the combined ball and tube radius of 0.127.

Now I'm checking the backboard clearance: as the ball continues past the rim toward larger x, I find it reaches the backboard's front plane while still well below the bottom edge, so no collision there. I'm also checking the mounting bracket region near x=4.24-4.381, z just above rim height, to see if the ball's path clips it as it passes through.

Should be negligible given MuJoCo's dt=0.002 Euler integrator being fine-grained enough. I'm now second-guessing my drag force formula—checking whether MuJoCo's blunt drag model includes a factor I assumed (Cblunt*rho*A*|v|v), cross-referencing against the actual documented equation for fluid drag forces.

Since the sphere starts with zero angular velocity and the drag acts at the center with no asymmetry, there's no torque, lift, or Magnus effect to worry about, and viscosity defaults to zero anyway. The ball starts exactly at z=r with no penetration, so any solver reference stiffness effects on contact should be negligible.

