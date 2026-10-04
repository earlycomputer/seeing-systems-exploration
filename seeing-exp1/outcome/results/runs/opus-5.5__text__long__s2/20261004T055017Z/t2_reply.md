The new key is `qvel="3.6 0 8.9 0 0 0"`, a lower and softer arc than the original.

**Air drag model:** I assumed MuJoCo's blunt drag is C·ρ·A_proj·|v|·v with no ½ factor. With C = 0.25 and A = π·0.1194², that gives a deceleration of about 0.022·v² per metre.

**Hand-integrated flight with drag:**
- The apex is about 3.74 m, at x ≈ 2.8 m.
- At x = 4 m, the ball centre is at about 3.10 m, so it crosses the rim plane (z = 3.05) at about x ≈ 4.02 m.
- That is about 0.02 m off the rim's centre. The gap between the ball and the rim's inner edge allows about 0.11 m.
- It is descending at about 48°, steep enough to drop cleanly through the 0.457 m ring.
- The y-velocity stays zero, so there is no left or right error.

**Caveats:**
- I integrated by hand in coarse steps, and the drag formula is my recollection of MuJoCo.
- If the actual drag were about half my estimate, the ball would arrive too high and miss long. So the drag model is the main thing to confirm when you run it.

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
    <key name="shot" qvel="3.6 0 8.9 0 0 0"/>
    <!-- Changed qvel from "3.5952 0 10.416 0 0 0" to "3.6 0 8.9 0 0 0". The old launch peaked near 5 m and
         passed about 1.6 m over the rim, clearing the backboard and missing long. The new, lower arc
         (accounting for air drag at density 1.2, blunt drag coefficient 0.25) peaks at about 3.7 m and
         crosses rim height (3.05 m) at x of about 4.02 m, descending at about 48 degrees, so it drops
         through the hoop. The y-velocity stays 0, so there is no lateral error. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to find a new launch velocity so that with drag the ball passes through the rim descending at a steep enough angle, over 35 degrees. I'll start by working out a vacuum solution with a steep launch angle around 55 degrees, then adjust for the drag coefficient.

Working through the vacuum case, a trajectory with vx around 3.33 and vz around 8.33 gives a descent angle of about 46 degrees at the rim, which looks promising. Now I'm testing this with drag included by simulating step by step with a drag coefficient around 0.0217, trying vx=3.6 and vz=8.9 and tracking how velocity and position evolve over small time increments to see if the trajectory still clears the rim steeply enough.

Continuing the step-by-step velocity and position integration through t=0.8s, with drag decreasing steadily as velocity drops and the z-position approaching its peak near 3.74.

Continuing to x=4, the ball reaches z≈3.10, just slightly above the rim height of 3.05, well within the clearance tolerance given the rim and ball radii. The descent angle checks out around 48°, so the trajectory looks good, though I note the result would shift notably if the drag coefficient formula uses a different constant factor.

Still recalling the drag formula...

Since there's no 1/2 factor in the quadratic drag term and linear viscosity is negligible with default air viscosity, I'll trust the coefficient k=0.0217 and keep the velocity setup as is.

Checking the trajectory at x=4, I'm slightly high by 0.046 — with the steep 48° descent angle, the center crosses z=3.05 near x≈4.02, which is close enough.

