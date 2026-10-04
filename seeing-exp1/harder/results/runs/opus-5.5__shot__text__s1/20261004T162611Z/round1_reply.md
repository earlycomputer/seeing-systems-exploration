**Expected behavior of the scene as written.** The scene does not do what the brief says. The cause is the air model, not the launch numbers. The ball does have the right size and mass and starts on the floor. Then:

- `density="1.2"` turns on MuJoCo's ellipsoid fluid model. The ball has a Magnus coefficient of 1.0, and the keyframe gives it a 30 rad/s backspin (ω_y = −30).
- On the way up, the Magnus force ρ·V·(ω×v) points mostly backwards. At launch it is about −2.4 N, roughly −3.9 m/s² on a 0.62 kg ball. Blunt drag adds to this.
- Estimating by hand, the horizontal speed falls from 3.2 m/s to about 1.3 m/s by the apex. The apex is about 4.4 m high, at only about x ≈ 1.8 m.
- The ball comes back down through rim height at about x ≈ 2.4 m. That is roughly 1.5 m short of the hoop, so it lands on the floor in front of the basket.
- Without the air, these launch numbers would be about 1 m too high over the hoop and would rely on a backboard bank. So the velocities were not tuned for this air model either way.

**Fix.** I removed the air (the density defaults to 0 and the fluid attributes are gone) and dropped the spin. I then chose a clean swish in a vacuum:

- Apex at 4.30 m, so v_z = √(2·9.81·(4.30−0.1194)) = 9.057 m/s.
- Time to apex is 0.923 s, and the fall to 3.05 m takes 0.505 s, so T = 1.428 s.
- v_x = 4/1.428 = 2.801 m/s.

Checks on this path:

- The ball enters about 60° from horizontal at about 4.95 m/s downward.
- At the front rim (x = 3.763) the ball's center is at 3.43 m, about 0.38 m above the rim.
- The path passes 0.206 m from both the front and back rim tubes and 0.198 m from the bracket. The ball radius is 0.119 m and the rim tube adds 0.008 m, so every clearance holds.
- It drops under the backboard's bottom edge (2.90 m) and hits the support pole at about z ≈ 0.7 m after scoring.

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

  <!-- Vacuum ballistic swish: apex 4.30 m, reaches x = 4 m at z = 3.05 m descending at ~60 deg after 1.428 s -->
  <keyframe>
    <key name="start" qvel="2.801 0 9.057 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "With air density 1.2 and a 30 rad/s backspin, Magnus lift and drag strip the ball's forward speed on the way up. It peaks near 4.4 m at about x = 1.8 m and falls back through rim height around x = 2.4 m, landing well short of the hoop at x = 4 m without touching the rim.", "works": false, "problem": "The fluid model (density 1.2 with Magnus coefficient 1.0) acting on the large keyframe backspin pushes the ball strongly backwards, so it falls about 1.5 m short of the hoop instead of dropping through it."}
```

---
thinking (summarized):

I'm setting up the ball's initial position and velocity, noting the angular velocity suggests backspin since the ball moves in +x but has negative wy, and factoring in fluid drag with ellipsoid shape which brings Magnus lift into play.

Checking the no-drag case first: reaching x=4 takes about 1.246s, giving a height around 4.09m — well above the rim at 3.05m, with the ball still descending from its apex near 4.53m. This tells me drag must be significant enough to pull the trajectory down closer to the rim, so I'm trying to estimate the drag force using the ball's mass, cross-sectional area, and MuJoCo's blunt drag formula with the given coefficient, density, and velocity to see how much it reduces the height at that point.

Now I'm computing the Magnus force from the spin, taking the cross product of angular velocity and velocity vectors to get the lift force components, then converting to acceleration to see how much it curves the trajectory sideways and upward.

I should check whether the designer actually ran drag-free numbers or included Magnus effects, since without drag the ball ends up way too high at x=4. I need to recall MuJoCo's ellipsoid fluid model formulas for blunt drag force to integrate this properly.

For a sphere, the slender drag term vanishes since the projected area difference is zero, so I'm left with just blunt drag, angular drag, and Magnus lift to account for.

For angular drag I'm working out I_D ≈ (8π/15)r^5 for a sphere, giving torque around 0.066 N·m and angular deceleration governed by dω/dt = -kω² with k≈0.01244, so ω decays from 30 to about 20.7 rad/s by t=1.2s — though I'm not fully confident in that I_D formula.

Checking the documented formula more carefully, it looks like I_D=(8/15)π d_x(d_y^4+d_z^4), which for a sphere doubles my earlier estimate to k≈0.0249, giving ω(t)=30/(1+0.746t) and ω≈15.8 at t=1.2 — still uncertain. I'm also considering the Kutta lift term, which should vanish for a sphere due to its symmetry.

For Magnus force, F_M = C_M ρ V ω × v makes sense. I'm trying to recall whether MuJoCo's ellipsoid fluid model also includes an added-mass term alongside viscous drag, Magnus, Kutta, blunt/slender drag, and angular drag — if so, added mass for a sphere (~0.5ρV ≈ 0.004 kg) would be negligible compared to the object's mass of 0.62 kg, so I can likely ignore it and move on to integrating the drag acceleration.

Working out numbers: drag acceleration coefficient comes to about 0.02168·|v|v, and Magnus acceleration coefficient works out to 0.0138·(ω×v), with ω = (0, -w, 0) giving the cross product as (-w·vz, 0, w·vx). Starting with w=30 gives a factor of 0.414.

Now I'm considering spin decay — whether to model dω/dt = -kω² with some coefficient k around 0.0249 or 0.0124 — then stepping through the trajectory numerically with dt=0.1. At t=0, with v=(3.21,9.3) and |v|=9.84, I compute ax ≈ -4.53 and az ≈ -9.81 -1.984 +1, combining gravity, drag, and Magnus contributions.

I'm continuing the Euler stepping: at t=0.1, velocity becomes roughly (2.757, 8.253) with position updated accordingly, spin decaying to ω≈27.9 giving f≈0.385, and the new accelerations ax≈-3.70, az≈-10.31. I'm now moving to t=0.2 with velocity dropping further to around (2.387,...).

Continuing the numerical integration through t=0.4 and t=0.5, tracking velocity decaying further (down to about 5.53 then 4.5 m/s) while position continues accumulating toward x≈1.15, z≈3.0 and beyond.

Continuing the step-by-step integration: at t=0.7, velocity is roughly (1.41,2.29) with position x=1.457, z=4.137; by t=0.8 velocity drops further to about (1.34,1.33) with x near 1.595, as drag and Magnus forces keep decelerating the horizontal and vertical components.

By t=0.9 the velocity is near (1.30,0.38), position x=1.727, z=4.318, and at t=1.0 the vertical velocity turns negative (-0.57), meaning the trajectory peaks around z≈4.40 and starts descending, with x reaching about 1.857.

Continuing to t=1.1, velocity is roughly (1.30,-1.52) and position drops to x=1.986, z=4.29. Estimating the remaining fall to rim height (~3.05) suggests only about 0.5 m more horizontal travel, landing the ball around x≈2.5 — well short of the x=4 target, so the shot looks like a clear miss.

Even checking the non-fluid case, the ball would end up near x=4 at a height well above the rim, likely clipping the backboard around z≈3.81 (within the board's top limit of 3.95) before bouncing back with reversed horizontal velocity — a bank attempt that's uncertain to drop in.

The real fix is to remove the fluid/density setting entirely so it stops affecting the trajectory.

Then I'll design a clean arcing shot instead: starting near the floor and rising to an apex around 4.3m before descending into the hoop at a steep ~60° entry angle, which gives a nice swish without needing spin or drag effects.

Now I'm checking the backboard and rim clearances to confirm the ball actually passes cleanly through the hoop opening rather than clipping the rim or backboard, comparing the ball's horizontal extent against the rim's inner radius at the moment it crosses the rim plane.

Perpendicular distance to both rims checks out at 0.206, clearing the 0.1274 radius with margin, and the y-direction clearance at the sides is also fine at 0.2366. I'm also verifying the ball clears the front rim height while ascending before the hoop, finding it passes about 0.38 above the rim at that point — plenty of margin.

Now I'm tracking the ball after it falls through the net toward the floor, calculating landing position around x=5.17, then checking whether it might clip the support pole structure near x=5.1-5.3 — computing the timing and height at that x to see if there's a collision with the pole face.

I'm also double-checking the backboard clearance: as the ball passes beneath the backboard's lower edge, I'm computing its height at that x-position (around 2.544) versus the backboard bottom at 2.90, confirming the ball's top stays below it so there's no collision there.

Now I'm checking the mounting bracket geometry near the rim, verifying the ball's trajectory distance from the bracket's bottom-front corner to make sure it doesn't clip it after passing through the net.

I'll simplify the physics by removing fluid density entirely since there's no air drag needed, and set initial velocity directly via qvel="2.801 0 9.057 0 0 0" with zero spin. I'm now computing precise timing values for the trajectory.

T = 0.9232+0.5048=1.4280, giving vx=2.8011, which checks out. The ball starts resting on the floor at the correct height, so I'm ready to write the corrected file.

