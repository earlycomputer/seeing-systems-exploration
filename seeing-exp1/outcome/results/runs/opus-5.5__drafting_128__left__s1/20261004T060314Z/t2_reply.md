The original key was 3.198, 0.280, 9.3. The new key aims straight at the hoop with a steeper arc.

**Sideways drift.** I set vy to 0. The old 0.28 m/s carried the ball about 0.35 m left by the time it reached the hoop.

**Arc and entry angle.** I raised vz to 9.6 m/s. The ball then peaks at about 4.3 m and comes down at roughly 60° from horizontal. At that angle the 0.457 m ring leaves about ±0.08 m of clearance around the ball. The old flatter, faster shot (about 45°) left only about ±0.04 m and also carried into the backboard.

**Range.** Air drag slows the ball noticeably in this scene. I estimated it from the fluid settings (density 1.2, blunt coefficient 0.25 on the ball's 0.045 m² cross-section). I stepped the flight by hand at 0.1 s. At vx = 2.75 m/s the ball centre came down through rim height at only x ≈ 3.54 m. Horizontal drag scales roughly with vx, so I scaled it up: 2.75 × 4 / 3.54 ≈ 3.11. I used vx = 3.12 m/s, which brings the ball centre down through z = 3.05 m at about x ≈ 4.0 m, about 1.4 s after launch. The ball should pass the rim's centre without touching the backboard, whose face is at x ≈ 4.38 m.

These are hand estimates, not a run of the simulator. Re-render the shot to confirm.

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
    <key name="shot" qvel="3.12 0 9.6 0 0 0"/>
    <!-- Changed qvel from "3.19778 0.27977 9.3 0 0 0" to "3.12 0 9.6 0 0 0".
         Why: the old shot drifted ~0.35 m to the shooter's left (vy = 0.28 m/s) and arrived at x = 4 m about
         1 m above the rim, so it struck the backboard and fell off to the left. Setting vy = 0 aims it straight
         at the hoop. Raising vz to 9.6 m/s gives a higher arc (apex ~4.3 m) and a steep ~60 deg descent, which
         leaves more clearance through the 0.457 m ring. vx = 3.12 m/s was chosen to allow for air drag (fluid
         density 1.2, blunt coefficient 0.25), so the ball centre comes down through z = 3.05 m at x ~ 4.0 m,
         ~1.4 s after launch, in front of the backboard. These figures are hand estimates of the drag;
         re-render the shot to confirm. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to plan a descending trajectory passing through the hoop center at (4,0,3.05), factoring in drag from MuJoCo's fluid model since the ball is treated as an ellipsoid with density 1.2 and blunt drag proportional to projected area and velocity squared.

Testing T=1.2s gives vx=3.33, vz=8.33 without drag for a nice ~46° descent angle. Estimating drag's effect on horizontal displacement, I get roughly a 0.27m shortfall from the undamped trajectory, so I need to boost initial velocity to compensate.

I'm now running a step-by-step numerical simulation with 0.1s increments, tracking velocity decay and position updates under drag to see how far the projectile actually travels compared to the drag-free case.

Continuing through step twelve, the trajectory reaches around x=3.98, z=2.82, which falls short of the rim height needed near x=4 — so the drag-adjusted path clearly loses too much height before reaching the target, meaning I need to reconsider the initial launch parameters.

I'm testing a steeper vertical velocity, around vz=8.9-9.0 m/s with vx near 3.6-3.65, estimating that accounting for drag should shift the crossing point near x=4.0 at the correct rim height, while also checking that the ball's approach angle and size leave enough clearance through the rim opening.

Continuing step-by-step integration...

Continuing the step-by-step integration, velocity is now dropping toward zero vertically as the trajectory peaks and begins descending, with position steadily advancing past x=2.5.

Continuing the trajectory simulation, updating velocity, position, and acceleration through steps 13 and 14 as drag and gravity keep decelerating the motion.

Interpolating between the step 14 and 15 positions at z=3.05, I find x lands around 3.537, which falls about 0.46 m short of the 4.0 target at roughly 1.41 seconds — so I need to increase the initial horizontal velocity to close that gap.

Since drag scales roughly proportional to vx while vertical motion stays largely unaffected, I can approximate the resulting x position by scaling 3.537 by the ratio of new vx to the original 2.75, aiming for something close to 3.10 to compensate for the shortfall.

The Euler step error is minor since the averaged velocity approach is roughly second-order anyway. With vy=0, I should also check where the ball's x-position lands relative to the backboard.

Checking clearance: the ball's far side reaches 4.12, well short of the backboard at 4.381, so it's fine. Settling on a final qvel of "3.12 0 9.6 0 0 0".

