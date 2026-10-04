**What happens.** The ball leaves the floor near x = 0 and climbs to a peak of only about 4.3 m, at about x ≈ 2.3 m. That peak is well short of the hoop. On the way down it is already below rim height at about x ≈ 3.7 m. It then passes under the rim and backboard and lands at about x ≈ 4.3–4.8 m. It never goes down through the hoop.

**Why.** Air is turned on (`density="1.2"`) and the ball has a fluid model with Magnus lift. The keyframe also gives the ball −30 rad/s of backspin. Backspin lift acts at right angles to the velocity. While the ball is rising steeply, that direction points mostly in −x, so the spin pulls the ball backwards by roughly 2.4 N. Drag also slows it. The launch velocity was worked out for a ballistic arc with no air, so the shot falls well short.

**Fix.** I removed air (no `density`, no fluid attributes on the ball) and set the spin to zero. I then solved the arc so the ball's centre is exactly at the rim centre (4, 0, 3.05) while it is falling:
- Apex height is about 4.3 m.
- Launch velocity is vx = 2.801 m/s and vz = 9.057 m/s.
- The ball arrives about 1.43 s after launch, moving down at about 60°.

**Clearance checks.**
- The ball's path stays about 0.21 m from the centre line of both the front and back of the rim. Contact would need 0.127 m, so it touches neither.
- It passes below the backboard (bottom edge at 2.9 m) and below the bracket.
- It reaches the floor after it has gone through the hoop.

```json
{"what_happens": "The ball rises to only ~4.3 m at x≈2.3 m. Backspin Magnus lift and air drag pull it backwards, so it comes down short of the hoop, drops below rim height around x≈3.7 m, passes under the rim and backboard, and lands near x≈4.5 m without going through the hoop.", "works": false, "problem": "Backspin plus air (fluid Magnus and drag) pulls the ball back and slows it, so it falls short and below the rim instead of dropping through the hoop."}
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

  <!-- Ballistic shot (no air): apex ~4.3 m, ball center passes (4, 0, 3.05) descending at ~60 deg after ~1.43 s -->
  <keyframe>
    <key name="start" qpos="0 0 0.1194 1 0 0 0" qvel="2.801 0 9.057 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm calculating the ball's trajectory, checking its height at x=4 using the launch velocities, and finding it comes out above 3.05 at that point—so I'm also computing the apex time and height to verify the full arc.

Comparing this against the backboard geometry, I check whether the ball strikes the backboard rather than the hoop directly, factoring in the backboard's front face position and span. I'm also considering that drag from the fluid and Magnus lift from backspin (negative ω_y producing an upward force) will alter the pure projectile path, so I need to account for those effects when matching against the pixel positions of the dots shown in the image, working out the pixel-to-meter scale to map ball positions accurately.

Tracking the remaining ball dots, it looks like the trajectory peaks lower and earlier than the ideal arc, then descends to around z=2.5 near x=3.67, well below rim height, before landing around x=4.3-4.8 with z dropping toward zero. This suggests the shot falls short and low, landing in front of the hoop rather than going in.

I should model this more rigorously using the drag coefficients given — blunt and slender drag at 0.25, angular drag at 1.5, Kutta lift and Magnus coefficients at 1.0 — applying a quadratic drag force based on the ellipsoid shape to get a more accurate trajectory estimate.

Computing the sphere's cross-sectional area and drag force at v=9.8, I get roughly 0.645 N, which translates to about 1 m/s² of deceleration given the ball's mass. But the Magnus force dominates — with spin at 30 rad/s, I'm getting a force around 2.5 N, roughly 4 m/s² of lateral acceleration, which is huge. I need to work out the direction by computing the cross product of angular velocity and linear velocity vectors.

This reveals that during ascent, the backspin combined with upward velocity pushes the Magnus lift backward, stealing horizontal speed from the ball — that's -2.39 N in the x-direction, about -3.85 m/s² of deceleration, which explains why the trajectory falls short of its expected apex. The fix is to eliminate the spin or fluid effects entirely, either by zeroing out air density or removing the spin term from the keyframe, then recomputing the trajectory with just drag.

Now I'm setting density to zero for pure ballistic motion and solving for the velocity needed to pass through the hoop on a descending path, targeting the ball's center at (4, 3.05) coming down steeply. Starting from z0=0.1194, I need to pick an apex height around 4.3 m and solve the resulting quadratic for the time to reach x=4 with the right vertical velocity.

Working through the numbers, I get vz=9.057, T=1.428, vx=2.801, and an arrival vz of about -4.95, giving a descent angle near 60°, which looks good. Then I'm checking clearance against the backboard and rim — verifying the ball's edge relative to the rim's front edge as it passes through, accounting for the ball radius versus rim inner radius.

I'm now checking the back rim geometry: as the ball descends through the hoop plane at the 60° angle, I'm computing where its back edge would intersect the rim tube's inner edge, and setting up the sphere-rim tangency condition to confirm there's no collision on the far side.

Front rim clearance checks out fine too. Now I'm checking whether the ball clips the backboard support bracket on its way down—the bracket sits around x 4.24-4.38, z 3.028-3.052, and the ball's path stays just below that zone, so it should clear. Then I'm solving for when the ball reaches the floor using the vertical motion equation with vz=-4.95.

With that settled, I'm deciding to strip out the fluid/density attributes entirely since they don't matter without density>0, and setting spin to zero for simplicity rather than adding a small backspin that wouldn't affect anything pre-contact.

Setting qvel to 2.801 and 9.057, then verifying: at x=4 (T=1.428s), z computes to about 3.050, which checks out against my earlier trajectory calculation.

