**What I see:** In the side elevation, the ball now rises in a clean, high arc. It peaks around x ≈ 2.9–3.0 m, near 4.2–4.3 m up, and stays in line with the hoop. In the plan view, the trail runs straight along y ≈ 0, so the left/right error is fixed. But the ball comes down at the backboard, not through the ring. At x = 4 m it is still near 4 m high, and its descending copies lie at x ≈ 4.4 m and beyond. It drops to the floor behind the hoop, near the support. The shot goes long.

**Why:** The apex sits almost where a drag-free throw would put it: 3.12 m/s × 0.98 s ≈ 3.05 m. So air drag in this scene is much weaker than I estimated, roughly a few percent of range rather than about 18%. Without that loss, vx = 3.12 m/s carries the ball to about x ≈ 4.9 m by the time it falls to rim height. That puts it into the backboard instead.

**Fix:** I keep vy = 0 and the steep arc (vz = 9.6 m/s). I reduce vx so the ball reaches rim height over the hoop's centre:
- Falling back to z = 3.05 m takes about 1.58 s without drag, so vx ≈ 4.0 / 1.58 ≈ 2.53 m/s.
- I allow about 4% for the weak drag seen in the picture, which gives vx ≈ 2.62 m/s.
- The ball should then enter at about 65° and pass the ring centre around x ≈ 4.0 m, clear of the backboard.

```json
{"description": "The ball rises in a high arc peaking near x≈3 m, z≈4.3 m, and tracks straight along y≈0 in plan, so the sideways error is gone. It reaches the hoop's x still well above the rim, comes down at the backboard around x≈4.4 m and beyond, and falls to the floor behind the hoop instead of through the ring: the shot is long.", "goes_in": false, "miss": "long", "evidence": "both"}
```

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
    <key name="shot" qvel="2.62 0 9.6 0 0 0"/>
    <!-- Changed qvel from "3.12 0 9.6 0 0 0" to "2.62 0 9.6 0 0 0" (originally "3.19778 0.27977 9.3 0 0 0").
         Why: with vy = 0 the shot was on line but went long. The readback put the apex near x = 3 m, almost
         where a drag-free throw would, so drag here is far weaker than first assumed. At vx = 3.12 m/s the ball
         reached the backboard before falling to rim height. With vz = 9.6 m/s the ball falls back to
         z = 3.05 m about 1.58 s after launch. vx = 4.0 / 1.58 = 2.53 m/s, raised to 2.62 m/s to cover a
         few percent of drag loss, should bring the ball centre down through the ring centre at x ~ 4.0 m at a
         steep ~65 deg entry, clear of the backboard. This is an estimate; re-render to confirm. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm mapping the pixel positions in the side view image to estimate where the arc peaks, descends to the hoop, and where the ball's trajectory copies fall near the backboard and floor.

Comparing my simulated apex position against the apparent image apex suggests the ball actually flew longer than predicted, meaning my drag estimate is probably too strong—the real drag coefficient in MuJoCo's blunt-body model is likely smaller than I assumed.

Rerunning the trajectory with little to no drag, I find the ball would reach the backboard around t≈1.37, with the ball's height landing right near the top edge of the backboard—so it's plausible the ball clips the top of the board rather than striking it squarely.

The picture's apex loss is much smaller than my simulation suggested, so I'll scale down my drag estimate to roughly 4% loss at crossing rather than the larger value. With vz=9.6 giving crossing time near 1.56s and target x=4.0, I calculate vx should be about 2.64 after accounting for that reduced drag effect.

