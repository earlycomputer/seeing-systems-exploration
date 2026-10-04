The ball flies too high, passes over the rim, and never drops through the hoop.

**What the picture shows.** In the side view the ball's copies climb in a tall arc. The highest copies sit well above the backboard top, around 4.5 m. The ball crosses above the hoop and comes down near the backboard. It ends on the floor near the support base. No copy drops through the rim.

**Why it misses.** With the keyframe velocity (3.21, 9.3), the flight works out like this:
- The ball reaches x = 4 m after about 1.25 s, with its center at about 4.1 m. That is roughly 1 m above the rim.
- Its apex is about 4.5 m.
- It then strikes the backboard face at about 3.8 m height.

**The fix.** I re-solved the launch so the ball's center passes through the rim center (4, 3.05) descending at 45°:
- Time of flight T ≈ 1.189 s.
- Launch velocity vx = 3.365 m/s, vz = 8.296 m/s.
- Apex is 3.63 m, at x ≈ 2.85 m.

Clearances along that path:
- Front and back rim: about 0.167 m from the ball center, against the 0.127 m needed.
- Bracket and backboard bottom edge: about 0.16–0.18 m, against the 0.119 m ball radius.

I also removed air density and fluid drag so the flight is the exact ballistic path. Drag, and the Magnus lift from the backspin, would bend the ball off that solved path.

```json
{"what_happens": "The ball launches in a very tall arc (apex about 4.5 m), passes about 1 m above the rim at x = 4 m, strikes the backboard and falls to the floor near the support. It never goes through the hoop.", "works": false, "problem": "The keyframe launch velocity (3.21, 9.3) puts the ball about 1 m above the rim when it reaches the hoop, so it overshoots into the backboard instead of dropping through."}
```

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
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

      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Ballistic shot: center passes (4, 3.05) at t = 1.189 s descending at 45 deg; apex 3.63 m -->
    <key name="start" qvel="3.365 0 8.296 0 -20 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Computing the ball's trajectory: it reaches x=4 at about t=1.246s, giving z≈4.09m, while the apex occurs at t=0.948s with z≈4.53m.

At x=4 the ball passes 1 m above the rim while descending, which looks like a miss given the hoop at z=3.05 and backboard front face at x=4.381. Checking the backboard collision math and factoring in fluid drag, I realize the launch velocity needs adjusting so the ball actually descends through the hoop rather than sailing over it.

I decide to drop the fluid density to zero so the trajectory stays clean ballistic motion, then set up the geometry: start at (0, 0.1194), target the rim center at (4, 3.05) with a steep ~45° descent angle. Solving for time of flight by equating the descent velocity to match the horizontal component, I get T² ≈ 1.413, so T ≈ 1.1887 seconds.

Working through the velocity components, I find vx ≈ 3.365 and vz ≈ 8.296, giving an apex height around 3.627m at x ≈ 2.846m. I check the clearance through the rim opening at a 45° approach angle — the effective gap versus ball diameter looks fine — and start verifying the front rim's inner edge position for tube clearance.

Checking both front and back rim clearances along the 45° trajectory line, the perpendicular distances (about 0.167m) comfortably exceed the required margin (ball radius plus tube radius, ~0.127m), so the shot clears both sides. I'm also estimating the trajectory's radius of curvature near the rim to confirm the straight-line approximation holds.

Now I'm checking whether the ball could clip the support bracket after passing through—comparing the ball's falling z-position against the bracket's physical bounds as it travels past x=4.24, since the ball's top edge might be right at the bracket's bottom threshold.

Continuing the fall trajectory past the backboard bottom edge, I'm checking if the ball clears it before computing where it eventually lands—working out it reaches the floor around x=5.69, landing near the support pole and base rather than clipping the board.

Margin is fine at 0.119. For the spin, backspin with forward motion along +x should correspond to negative wy, so I'll keep that sign convention. I'll drop the fluid/density attribute entirely so there's no drag or Magnus force acting on the ball, leaving it resting at z=0.1194 on the floor initially.

Picturing the trajectory: the ball arcs upward to an apex around 4.5 m, clears the hoop, and comes down near the backboard base — I'll describe this in the final answer.

