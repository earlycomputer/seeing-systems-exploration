The original launch (vx = 3.595, vz = 10.416 m/s) peaks around 5.6 m, about 2.6 m above the rim, and lands near x ≈ 6 m. That is long.

**How I chose the new launch.** I estimated air drag from the ball's fluid settings (blunt drag on a sphere of radius 0.1194 m in air of density 1.2). That works out to a drag deceleration of about 0.022·|v|·v. With that drag, I hand-integrated the flight for a few trial launches:

| Launch (vx, vz) in m/s | Height where x = 4 m | Where it falls through z = 3.05 m |
|---|---|---|
| 2.92, 8.86 | — | x ≈ 3.28 m (short) |
| 3.40, 9.60 | z ≈ 3.5 m | x ≈ 4.34 m (long) |
| **3.15, 9.60** | — | x ≈ 4.03 m |

**Result for 3.15, 9.60.**
- The apex is about 4.3 m at x ≈ 2.6 m.
- The ball comes down at roughly 60° and passes within about 3 cm of the rim centre.
- Clearance from the front rim, back rim and backboard is about 0.18–0.23 m, centre to tube. The minimum allowed is 0.127 m.
- The margin for error is about ±0.1 m.

These figures come from my own step-by-step integration, not a MuJoCo run. Re-rendering would confirm them.

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
    <key name="shot" qvel="3.15 0 9.6 0 0 0"/>
    <!-- Changed shot qvel from "3.5952 0 10.416 0 0 0" to "3.15 0 9.6 0 0 0".
         The old launch was far too strong: it peaked ~5.6 m, flew over the rim and backboard,
         and landed long near x = 6 m. Re-aimed including blunt air drag (~0.022*|v|*v for this
         ball in rho = 1.2 air): hand-integrated flight peaks ~4.3 m near x = 2.6 m and descends
         at ~60 deg through z = 3.05 m at x ~ 4.03 m (rim centre x = 4.0). Clearances to the front
         rim, back rim and backboard are about 0.18-0.23 m against 0.127 m needed. Not yet
         confirmed by a MuJoCo run. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the launch velocity needed for the ball to arc into the hoop, factoring in drag—starting from the shooter's release point at roughly 1.19m high to the hoop at 4m distance and 3.05m height. I'm setting up the projectile equations for horizontal and vertical motion to solve for the right angle and speed, considering an apex height around 4.2m.

Now I'm trying to estimate MuJoCo's drag model for the sphere, using the blunt drag coefficient and projected area to compute a drag constant per unit mass, while checking whether slender drag and Magnus effects contribute anything for a non-spinning sphere.

With no drag the shot lands around 7.6, and adding drag with k≈0.0217 at speed 11 gives roughly a=2.6 deceleration, bringing landing closer to 6, which seems plausible. I want to numerically integrate with drag using 0.1s steps, starting with a guess of (3.1, 9.4) and checking against (2.92, 8.86) to measure the drag effect before scaling up the initial velocity to compensate.

Stepping through the simulation by hand: at t=0 I start at height 0.1194 with vx=2.92, vz=8.86, compute drag accelerations, then update velocity and average position each step — after one step I'm at roughly x=0.289, z=0.947 with vx=2.861, vz=7.70, and I continue this process for the next step evaluating the new speed and drag coefficient.

Continuing step by step: by step 4 I'm around x=1.126 with vx=2.729, vz=4.445, still tracking z, iterating forward with recalculated drag at each stage.

Steps 5-7: as velocity and height change, drag coefficient ks keeps shrinking (0.1132→0.0944→0.078) while horizontal velocity stays nearly steady around 2.7, with x climbing to about 1.666 and z peaking near 3.446 before starting to come down.

Continuing through steps 8-9, vz flips negative as the projectile crests and begins falling, with z reaching roughly 3.727 then 3.719, and ks continuing to decay toward 0.058 as drag weakens.

Continuing the step-by-step integration, I find at step13 the trajectory reaches x≈3.277 when z crosses 3.05, falling short of the target by about 0.72 m with a time of roughly 1.215 s. This means I need to correct the initial conditions, so I'm considering sensitivity of landing position to vx and vz and estimating that drag reduces average vx to around 2.7, which I'll use to adjust my guess for new initial values.

Trying vx=3.4, vz=9.6 and simulating forward: after two steps, drag and gravity reduce velocities to around vx≈3.26, vz≈7.26, with position reaching roughly x=0.666, z=1.02 so far.

I'm continuing the step-by-step integration through several more intervals, tracking speed, drag deceleration, and updated x/z positions each time—after five steps the trajectory reaches around x=1.31, z=3.04 with velocity settling near vx=3.16, vz=5.08, then starting the next step's drag calculation.

Continuing the step-by-step velocity and position integration through steps 8-10, drag is dropping off as speed decreases, with vz approaching zero then going negative as the object nears peak height around z≈4.3.

Continuing the trajectory steps, I find the ball crosses z=3.05 at x≈4.32, overshooting the target by roughly 0.34 m — so I need to check how sensitive the landing position is to small changes in initial velocity components.

I'll go with vx=3.15, vz=9.6 and step through the simulation to verify the trajectory, tracking drag deceleration and position updates across successive timesteps to see where it lands.

Continuing through steps S6 and S7, drag keeps decreasing as velocity drops, and position creeps forward to roughly x=2.07, z=4.0 — close to the target altitude, so I'm tracking when it crosses zero.

Continuing the drag simulation through steps 11-13, tracking velocity decay and position updates as the projectile's speed and height decrease with each iteration.

So crossing happens around x≈4.03, well within the rim's 3cm margin. Checking clearance: the ball's distance to the front rim at entry is about 0.228m and to the back rim about 0.206m, both comfortably exceeding the 0.127m combined radius needed, so the shot clears both sides of the rim.

With semi-implicit Euler at 0.1 step and small drag, the simulation should be accurate enough. I'll set the initial velocity to qvel="3.15 0 9.6 0 0 0".

