**What happens in the run.** The ball leaves the floor at (0, 0, 0.12) m with vx +3.21 and vz +9.30 m/s, plus 30 rad/s of backspin. It peaks at about 4.31 m at x = 2.30 m. The air in the scene (`density="1.2"` with the ellipsoid fluid model on the ball) slows it sharply. Its horizontal speed falls from 3.21 to about 2.2 m/s. So when it comes back down through rim height (3.05 m), it is only at x ≈ 3.59 m. It passes 0.18 m short of the near side of the rim without touching it. It then lands on the floor near the base of the pole, bounces off the support base, and rolls slowly back toward the start. It never goes through the hoop.

**Fix.** I removed the air drag and lift (air density 0, no fluid shape on the ball) and the spin. Without them the flight is a plain parabola that can be aimed exactly. I also lifted the ball 5 mm off the floor so the first step has no floor contact. Its center then starts at z = 0.125 m.

The launch velocity comes from the flight equations:
- With vz = 9.0 m/s, the ball's center comes back down to 3.05 m at t = 1.413 s. That run of the flight climbs 2.925 m.
- vx = 4 / 1.413 = 2.831 m/s puts it at x = 4 m at that moment.
- The peak is about 4.25 m.
- It arrives falling at 4.85 m/s, which is about 60° below horizontal.

These numbers give the clearances:
- The straight line through the rim center at that slope passes 0.204 m from both the near and far rim tubes. The ball needs 0.127 m (ball radius 0.1194 m plus tube radius 0.008 m), so it clears both.
- Under the rim plane the ball's front edge stays near x ≈ 4.27 m, short of the backboard face at 4.381 m.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002" density="0"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg (hollow shell inertia 2/3 m r^2). Starts 5 mm above the floor. -->
    <body name="ball" pos="0 0 0.125">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world. -->
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
    <key name="start" qvel="2.831 0 9.0 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The ball is launched at 9.84 m/s with backspin and peaks at 4.31 m. Air drag cuts its horizontal speed from 3.21 to about 2.2 m/s, so it comes down through rim height at x = 3.59 m, 0.18 m short of the rim without touching it. It lands near the support base, bounces off it, and rolls back across the floor; it never passes through the hoop.", "works": false, "problem": "The launch velocity ignores the strong fluid drag on the ball, so the ball falls short of the hoop instead of dropping through it."}
```

---
thinking (summarized):

Checking the trajectory, the ball misses the hoop—passing at x=3.59 when it reaches z=2.98, while the rim center sits at x=4. Drag is clearly a factor, pulling vx down from 3.21 to around 2.2, and I'm also accounting for a Magnus lift effect from the backspin pushing the ball upward.

The simplest fix is to strip out the fluid effects and spin entirely and solve for a clean ballistic trajectory instead. I need the ball to land at x=4, z=3.05 with a steep enough entry angle—above roughly 32°, so I'm targeting around 50-60°—to clear the rim given the ball and hoop dimensions. Solving with vz0=9.0 gives a descent time of about 1.41s, vx≈2.83, arrival angle near 59.7°, and an apex height around 4.25, which looks workable—now I just need to check whether this path would clip the backboard.

I'm checking the geometry near the backboard: the ball passes the rim plane at x=4, then continues falling about 0.27m further before its front edge could reach the backboard's bottom edge at x=4.381, and the numbers suggest it clears with room to spare (front edge around 4.27). I'm also double-checking the ball's clearance against the rim's inner radius right at the rim plane to make sure the edge doesn't clip there either.

Checking the far rim clearance gives the same 0.204 margin, comfortably above the required 0.127, and the bracket region near the backboard also checks out fine with similar spacing. The backboard front face clearance at lower z also looks safe based on the trajectory's position there.

The trajectory stays clear of the rim on the ascent since that happens at a small x value, and it never passes above the backboard's top edge since x never exceeds 4 at that height. For simplifying physics, I'm considering zeroing out drag by setting density to zero and removing the fluid shape and spin to keep things clean, though I need to watch out for the initial floor contact at t=0 — if spin is nonzero there, friction could alter the ball's velocity unexpectedly.

To avoid that complication, I'll lift the ball's starting height slightly to 0.125 and set spin to zero, then recompute the fall time and corresponding horizontal velocity using the quadratic drop equation — landing on vx≈2.831, vz=9.0, with the integration error from semi-implicit Euler small enough to ignore.

With no fluid shape and density set to zero, there are no drag forces to worry about, so I'll just drop that option from the file and write it out.

