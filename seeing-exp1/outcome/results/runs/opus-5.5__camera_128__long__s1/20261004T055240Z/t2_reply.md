I set the `shot` key to `qvel="3.63 0 8.36 0 0 0"`. I haven't rendered or simulated the corrected shot; the trajectory below comes from integrating gravity and air drag by hand.

- **Drag-free arc:** a flight time of about 1.15 s to the hoop needs roughly vx = 3.48 and vz = 8.19 m/s. That gives an apex near 3.5 m and an entry angle of about 40° below horizontal.
- **Drag:** the ball's fluid settings act as a pure quadratic drag, about 0.0108·|v|·v per unit mass. It costs roughly 0.15 m of horizontal travel and 0.2 m of height over the flight, so I raised both components to compensate.
- **Hand integration (0.1 s steps):** with vx = 3.61, the ball's centre comes down through z = 3.05 at x ≈ 3.97 m, just short of centre. Raising vx to 3.63 should shift that to about x = 4.00 m.
- **Margins:** the 0.457 m rim leaves the 0.239 m ball about 0.11 m of play each side. Seen along the ~38° descent, the opening is about 0.28 m. The ball should clear the front rim by about 0.15 m and the back rim by about 0.21 m, then fall to the floor under the hoop.

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
    <key name="shot" qvel="3.63 0 8.36 0 0 0"/>
    <!-- Changed shot qvel from (3.5952, 0, 10.416) to (3.63, 0, 8.36). The old launch was far too steep:
         the ball was ~5.6 m high when it crossed x = 4 m and sailed over the backboard (long miss).
         The new velocity targets a ~1.15 s flight with an apex of ~3.5 m and a ~38-40 degree descent.
         Hand-integrating gravity plus the ball's quadratic air drag (~0.0108*|v|*v per unit mass)
         puts the ball centre at x ~ 4.00 m as it descends through rim height z = 3.05 m. That clears
         the front rim by ~0.15 m and the back rim by ~0.21 m, so the ball drops through the hoop and
         falls to the floor. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a velocity so the ball passes through the hoop descending, from near ground level to about 3 meters high over a 4 meter horizontal distance, factoring in gravity and modest drag. I'll pick a flight time T, derive horizontal and vertical velocity components from the displacement equations, and require the vertical velocity at arrival to be less than gravity's contribution so the trajectory is coming down through the hoop rather than still rising.

Testing T=1.0s gives a fairly shallow entry angle around 26°, with apex near 3.25m - a bit too flat given the rim's limited clearance for the ball. Trying T=1.15s instead gives a steeper 41.6° entry angle and an apex around 3.54m, which looks better for threading the hoop cleanly.

I also want to check drag's effect using the ellipsoid fluid model - estimating the sphere's drag force at the relevant speeds shows a deceleration around 0.88 m/s², modest compared to gravity, with negligible lift or Magnus effects since there's no spin.

Now I'm refining that estimate further, averaging drag's effect on horizontal velocity across the trajectory to get a displacement loss of roughly 0.145m, and starting to work out the corresponding vertical displacement loss from drag during ascent.

I need to bump vx up to about 3.61 and raise vz to roughly 8.36 to compensate for the drag-induced height loss, but this increases drag slightly too. I'm checking the rim tolerance: a vertical error of Δz translates to horizontal error at rim height via Δz/tan(angle), roughly Δz/0.89, so I need precision around 0.1 m — my current estimates are rough, so I should redo this with a more careful calculation.

I'm computing the drag coefficient k by working through MuJoCo's ellipsoid blunt drag model, confirming the projected area term for a sphere comes out to k≈0.01084, and noting the slender drag term vanishes for a sphere since the projected area equals the max area. Now I'm stepping through numerical integration with dt=0.1s starting from v=(3.61, 8.36), computing the speed magnitude and acceleration components to trace the trajectory forward in time.

Continuing the trajectory integration through steps 3-5, updating velocity and position using midpoint drag estimates at each stage, with position reaching roughly x=1.419, z=2.630 and velocity around (3.499, 4.235) by step 4, then proceeding into step 5's midpoint calculation.

Continuing the step-by-step integration for steps 8-10, tracking velocity and acceleration updates as gravity and drag adjust, with position reaching roughly (3.49, 3.38) by step 10.

Stepping to step 11, I get velocity around (3.40,-2.66) and position (3.83, 3.17). Checking when x hits 4, I estimate dt≈0.05s, giving z≈3.02, slightly below the rim height of 3.05—so I refine the timing to find x at the exact rim-crossing height.

Nudging vx to about 3.63 brings x closer to 4 at the rim plane. I'm checking clearance against the rim's inner radius versus the ball's radius, accounting for the ~38° descent angle reducing the effective opening—still enough margin for a swish, though tight. I also need to verify the ball clears the front rim, located at x≈3.763.

Checking distances to both the front and back rim tube centers along the trajectory confirms clearance in both cases, so the shot passes cleanly through the hoop and lands on the floor afterward—good, that's the expected outcome.

