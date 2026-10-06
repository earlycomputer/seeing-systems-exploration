**What happens in the run.** The ball leaves the floor at 9.84 m/s and climbs to 4.31 m at x = 2.30 m. On the way down it crosses the rim height (z = 3.05 m) at about x ≈ 3.45 m. That is more than half a metre short of the hoop centre at x = 4 m. It misses the rim by 0.18 m and never touches it. It lands at x ≈ 4.1 m, bounces off the support base, and rolls back along the floor.

**Why it falls short.** Two settings shape the flight:
- **Fluid drag.** `density="1.2"` together with the ball's `fluidshape` makes the air drag on the ball fairly strong. vx drops from 3.21 to 2.14 m/s by the apex.
- **Spin lift.** The backspin of −30 rad/s adds Magnus lift and pushes vx back up on the descent.

The launch velocity was not chosen with either effect in mind, so the ball misses.

**Fix.**
- Remove the fluid model, which makes the flight a plain ballistic arc.
- Start the ball 0.6 mm above the floor, so the spinning ball gets no frictional kick from the floor on the first step.
- Choose the launch velocity so the ball's centre passes through the rim centre.

**Launch calculation.** The ball needs to go from (0, 0.12) to (4, 3.05). With vx = 3.0 m/s, it reaches x = 4 at t = 4/3 s. That requires vz·t − 4.905t² = 2.93, so vz ≈ 8.74 m/s. I raised this slightly to 8.75 to offset the semi-implicit Euler drift of about 1 cm. The resulting flight:
- **Apex.** About 4.0 m.
- **Entry.** The ball crosses the rim plane descending at about −4.33 m/s, an entry angle of about 55°. At that angle the effective opening is 0.4572·sin55° ≈ 0.37 m, against the ball's 0.24 m diameter.
- **Rim clearance.** The centre line of the path passes about 0.195 m from the front and back rim tubes. That leaves roughly 0.07 m to spare after subtracting the ball radius and the tube radius.
- **Bracket and backboard clearance.** Below the rim, the bracket is cleared by about 0.08 m. The ball is below the backboard's bottom edge before it reaches the backboard face.

Spin no longer affects the flight, so I left a small backspin for looks.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg (hollow shell inertia 2/3 m r^2). Starts just above the floor. -->
    <body name="ball" pos="0 0 0.12">
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
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.0 0 8.75 0 -10 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The ball is launched at 9.84 m/s, peaks at 4.31 m at x=2.30, and with air drag and Magnus lift slowing and bending its path it crosses rim height near x=3.45, passing 0.18 m short of the rim without touching it. It lands near x=4.1, bounces off the support base and rolls back along the floor.", "works": false, "problem": "The fluid drag and spin lift were not accounted for in the launch velocity, so the ball falls about half a metre short of the hoop and never goes through the rim."}
```

---
thinking (summarized):

Checking the trajectory against the rim position, the ball passes 0.18 m short of rim_07 — at 1.50 s it's at x=3.55, z=2.78, and crosses z=3.05 around x≈3.45, missing the hoop at x=4. I'm also factoring in air drag from the ellipsoid fluidshape and considering whether the -30 rad/s spin about y introduces a Magnus effect on the trajectory.

Working through the Magnus force, the backspin should produce upward lift, which roughly matches the vx behavior in the data — dropping then rising again during descent. But given the ball's trajectory still falls short and peaks too high at 4.31 m, drag doesn't seem to be the main issue. I'm leaning toward removing the drag entirely and adjusting the initial z-position slightly above the floor (around 0.12 m) to avoid any penetration artifacts at the start.

Now I need to design the ballistic path so the ball's center passes cleanly through the hoop at (4, 0, 3.05) while descending without clipping the rim or backboard. With a horizontal drop of 4 m and vertical rise of about 2.93 m, and the rim's inner clearance versus ball diameter, I calculate the minimum descent angle needs to exceed roughly 31.5° for the ball to fit through — so I'll aim for something steeper, around 55°, to ensure safe clearance.

Working through the physics with an initial horizontal velocity of 3.0 m/s gives a flight time of about 1.333 s to cover the 4 m distance. Solving for the needed vertical velocity to hit the correct height at that time, I get vz ≈ 8.738 m/s, and checking the velocity at impact shows a descent angle of about 55.4° — right in the target range, confirming this trajectory should clear the rim properly.

Now I'm checking whether the ball clips the backboard after passing through the hoop — tracking the ball's center position as it descends past the rim plane, comparing against the backboard's bottom edge at z=2.9 m, to see if the ball's sphere intersects that structure given its downward velocity of about 4.34 m/s.

Checking distance from the ball's front edge to the bracket box corner — it comes out around 0.199, safely clear of the 0.1194 collision radius. I'm also checking clearance against the back rim tube, computing the perpendicular distance from the ball's travel line to the tube's position.

Nothing else interferes before the front rim crossing, so the line approximation holds given the parabola's gentle curvature there. I'll simplify by setting fluid density to zero and removing drag effects entirely, since spin doesn't matter without fluid interaction—I'll keep a modest backspin value like -15 just for realism even though it has no physical effect in flight.

To avoid contact-impulse artifacts at t=0, I'll start the ball slightly above the floor (z=0.125) rather than exactly at its resting radius, which avoids any solver-induced force from zero-penetration contact. Recomputing the vertical velocity for this adjusted height gives vz≈8.734, keeping the ball clear of accidental floor contact at launch.

Semi-implicit Euler causes the position to fall slightly faster than exact, about 0.013 m low given my timestep — small enough relative to my clearance margin, so I'll just nudge vz up slightly to compensate. After landing, the ball continues past the floor and may interact with the support base or pole nearby, but that should bounce fine without issue.

I've confirmed the ball's apex and trajectory clear the backboard and any other obstacles, so the setup is solid enough to write the final answer.

