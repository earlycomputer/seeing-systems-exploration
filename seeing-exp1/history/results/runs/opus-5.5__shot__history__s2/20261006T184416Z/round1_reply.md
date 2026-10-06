**What happens in the run.** The ball leaves the floor at 9.84 m/s, with a backspin of −30 rad/s about y. It peaks at (2.30, 0, 4.31) m. Its forward speed then bleeds away from 3.21 to about 2.1 m/s. That loss comes from the fluid model in the file, which turns on air drag through `density="1.2"` and Magnus lift through `fluidcoef`. As a result the ball falls short of the hoop. At 1.47 s it passes the front of the rim at x ≈ 3.59 m, 0.18 m away from `rim_07`, and never enters the opening. It lands near the base of the support, bounces once on `support_base`, and rolls back toward the start.

**What I changed.** I removed the fluid drag and the spin, so the flight is plain ballistic and easy to aim. The new launch velocity is (2.80, 0, 9.06) m/s.
- The apex is at about 4.3 m.
- The ball reaches x = 4 m with its centre at the rim plane z = 3.05 m after about 1.43 s.
- It is descending at about 60° at that point, which gives roughly 0.08 m of clearance to the rim tube on each side.
- Afterwards it passes below the backboard and hits the support pole low down.

```json
{"what_happens": "The ball is launched with backspin and air drag on, peaks at 4.31 m around x = 2.3 m, slows horizontally, and passes 0.18 m in front of the rim at x ≈ 3.6 m without going through the hoop. It then lands near the support base, bounces, and rolls back toward x ≈ 2.7 m.", "works": false, "problem": "Fluid drag and backspin slow the ball's forward motion so much that it falls short of the hoop and never drops through the rim."}
```

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002"/>

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
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2"/>
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

  <!-- Ballistic shot: apex ~4.3 m, reaches x = 4 m at z = 3.05 m after ~1.43 s, descending at ~60 deg -->
  <keyframe>
    <key name="start" qvel="2.80 0 9.057 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The ball misses the hoop, passing 0.18m short of rim_07 at the 1.47s mark. I'm checking whether fluid drag and the backspin-driven Magnus effect (with angular velocity around the y-axis at -30) caused it to fall short of the rim.

The safest fix is to strip out fluid density and spin effects entirely and just compute clean ballistics instead of tuning the drag/Magnus parameters. I need to redesign the trajectory from launch point to the hoop center, accounting for ball radius versus rim opening — since the entry angle matters a lot, I should aim for roughly 50° to ensure enough clearance through the rim given the ball's diameter relative to the inner rim diameter. Now I'm working out the launch velocities needed to hit that target height and angle.

The timestep-induced position error is negligible, around 0.014 m. Checking clearance at the rim: the ball center's horizontal distance from the front rim tube needs to exceed the sum of radii (about 0.1274 m), and at z=3.05 the ball's x-position roughly aligns with the front tube center, so I need to verify the trajectory actually clears it rather than clipping.

Computing the perpendicular distance from the trajectory line to both front and back rim centers, I get about 0.206 m for the front rim, which comfortably clears the 0.1274 m threshold. The back rim at x=4.2366 gives a similar clearance distance, so the ball should pass through without touching either side of the rim.

Fine, safe distance there. Checking where the ball eventually lands, I calculate it hits the floor around x=5.17, which is concerning because that overlaps with the support base and pole region—so I need to check if the ball actually collides with the pole face at x=5.1 before reaching the floor.

I'm deciding to remove the angular velocity and fluid properties, setting density to zero and dropping the fluidshape element, while keeping damping on the ball. I'm setting the initial velocity state and double-checking whether starting the ball in contact with the floor at t=0 could create an unwanted impulse from the contact constraint.

Since the ball is separating upward with no penetration, the contact force should be negligible, so I'll leave the starting height as-is rather than adding a gap. I'm also accounting for the small numerical integration error from MuJoCo's semi-implicit Euler scheme, which causes the ball's trajectory to sit slightly lower than the analytic parabola — roughly 0.014m by the time it reaches x=4, which is acceptable for this setup.

