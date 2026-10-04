**What I expect from the file as written:** the ball does not reach the hoop. It falls about 1.3 m short.

The scene turns on MuJoCo's ellipsoid fluid model (`density="1.2"`, `fluidshape="ellipsoid"`, Magnus coefficient 1.0) and launches with 30 rad/s of backspin. I estimated the result by hand-stepping the flight in 0.1 s steps. Two terms matter:

- **Magnus force.** MuJoCo computes it as ρ·V·ω×v. For this ball that gives an acceleration of about 0.0138·ω·v per unit of spin and speed. With backspin it acts along (−ω·v_z, +ω·v_x). On the way up, while v_z is large, it pushes hard in −x, about 4 m/s² at launch.
- **Blunt drag.** This removes roughly another 2 m/s² early in the flight.

Combined, v_x drops from 3.21 m/s to about 1.35 m/s by the apex. The apex is about 4.5 m high at only x ≈ 1.85 m. On the way down, the Magnus force returns a little forward speed. The ball still crosses rim height at roughly x ≈ 2.7 m, well short of x = 4. It then lands on the floor in front of the hoop.

The tuning also fails without air. In a vacuum the same launch would pass about 1 m above the rim at x = 4.

**Fix.** Remove air effects so the flight is a clean, predictable parabola, and pick the launch velocity from ballistics:

- Flight time to the rim center: T = 1.3 s.
- Horizontal velocity: v_x = 4/1.3 = 3.077 m/s.
- Vertical velocity: v_z = (2.9306 + 4.905·1.3²)/1.3 = 8.631 m/s. I added +0.01 to make up for the lag of MuJoCo's semi-implicit Euler integrator, giving 8.641 m/s.

**Checks on the new shot:**

- The apex is about 3.92 m. The ball enters the rim at about 53° below horizontal.
- Measured perpendicular to the path, the gap from the ball center to the front rim tube and to the back rim tube is each about 0.19 m. The ball radius plus the tube radius is 0.127 m, so there is about 6 cm of clearance on each side. The bracket also clears.
- The ball passes under the backboard: its top is at about 2.78 m when it reaches the board, and the board's bottom edge is at 2.9 m.
- It then strikes the support pole at about 1.2 m height and drops to the floor.

I removed the spin because it has no effect without air.

```json
{"what_happens": "With the fluid model on, Magnus lift from the 30 rad/s backspin plus drag strips most of the forward speed during the climb. The ball peaks about 4.5 m high near x = 1.85 m and comes down through rim height around x = 2.7 m, landing well short of the hoop at x = 4 m.", "works": false, "problem": "The launch velocity and backspin, with air drag and Magnus force enabled, make the ball fall about 1.3 m short of the hoop instead of dropping through it."}
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

  <!-- Ballistic shot: reaches the rim center (4, 0, 3.05) at t = 1.3 s on the way down, apex ~3.92 m, entry angle ~53 deg -->
  <keyframe>
    <key name="start" qpos="0 0 0.1194 1 0 0 0" qvel="3.077 0 8.641 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm setting up the ball's initial position, velocity, and spin, and working out how the backspin's angular velocity translates into surface velocity at the contact point using the cross product of omega and radius.

Then I check what happens without drag or lift: computing the trajectory purely from gravity shows the ball would overshoot the rim by about a meter at x=4, so drag and the Magnus lift from backspin must be what bring it down onto a realistic arc. I'm now thinking through MuJoCo's ellipsoid fluid model—viscous drag, density effects, and the magnus coefficient—to estimate how much those forces would correct the trajectory.

At v~9.8 that drag force is about 1.29 N, giving roughly 0.2g of deceleration. For Magnus lift, I'm computing the ball's volume and using ω×v with ω=(0,-30,0) and v≈(3.21,0,9.3), getting a cross product of about (-279,0,96.3), which gives a force around 2.52 N (≈4 m/s² acceleration) that initially pushes the ball backward.

I should also account for angular drag decaying the spin over time, though it's likely small, and note that a smooth sphere has no Kutta lift asymmetry, and viscosity-based effects are negligible since MuJoCo defaults air viscosity to zero. I'm also considering whether the ellipsoid fluid model includes added mass alongside blunt and slender drag terms.

The added mass contribution is tiny compared to the ball's mass, so I can mostly ignore it. For a sphere the slender-body drag term vanishes due to symmetry, leaving just viscous drag and Magnus-like coupling terms to work with. I'm setting up rough numerical constants—drag coefficient k≈0.0217 and a coupling coefficient m_c≈0.0138—to integrate the equations of motion by hand, including an estimate for angular drag torque causing spin decay.

Working through the angular drag torque formula, I get a rough spin-down rate where angular velocity decays like ω(t)=30/(1+0.366t), suggesting the ball's spin drops from roughly 30 rad/s to about 20 rad/s over 1.3 seconds — though I'm not fully confident in the constant since this estimate involves several uncertain coefficients.

Now I'm working out the Magnus acceleration components. With spin vector ω=(0,-W,0), the cross product ω×v gives acceleration terms where a_x involves -W·vz and a_z involves W·vx, so I'm setting up the x-direction equation combining drag (-k|v|vx) with this Magnus term while the ball is still ascending (vz positive).

Integrating this over the flight, the Magnus term decelerates x-motion on the way up and accelerates it on the way down, but the net effect over a height change of about 2.93 (from launch at 0.12 to rim at 3.05) works out to roughly a 1 m/s drop in vx by the time the ball descends to rim height. For the z-direction, I'm adding gravity (-9.81), drag (-k|v|vz), and the Magnus term (+m_c·W·vx), which comes out to about 0.93 near launch — meaningful enough that I should just integrate this numerically with a small timestep rather than approximate further.

Starting the numerical integration at t=0 with initial state x=0, z=0.119, vx=3.21, vz=9.3, and using a decaying spin rate, I compute acceleration components at each step (getting ax≈-4.54, az≈-10.47 for the first step) and plan to advance using an averaged or semi-implicit scheme for better accuracy.

I'm refining this with a midpoint method: using half-step velocities (vx=2.983, vz=8.777) to recompute the drag and spin accelerations more precisely, giving ax≈-4.17 and continuing to work out az, before updating position and velocity for the next time step.

Correcting an earlier arithmetic slip — z should be 0.997, not 1.116 — and now moving into step 2 (t=0.1 to 0.2), estimating the acceleration at the new starting velocities (2.793, 8.264) to continue the integration.

Updating position to x2≈0.562, z2≈1.773 after this step. I'll continue stepping forward with 0.1 increments, computing the next interval (0.2→0.3s) using the velocity (2.443, 7.247), giving acceleration components ax≈-3.20 and az≈-10 for the next update.

Continuing into the next step (0.3→0.4s), I'm getting velocity around (2.152, 6.248), updating position to x3≈0.792, z3≈2.448, and starting the drag/lift calculation for the following interval with speed near 6.61.

Continuing the midpoint iteration: vx5=1.724, vz5=4.295, giving x5=1.177, z5=3.502. Drag is clearly killing horizontal velocity fast, so I'm estimating the apex occurs around t≈0.94 with vx dropping to roughly 1.2.

Stepping to t=0.6: vx6≈1.577, vz6≈3.337, x6≈1.342, z6≈3.502+0.3... Total horizontal travel is shaping up to be much less than 4 m by the time the ball descends back to 3.05 m height.

Continuing the integration: by t=0.7, velocities drop to roughly (1.469, 2.387) with position (1.494, 4.170); by t=0.8, velocities are around (1.398, 1.444) with position (1.637, 4.362), so the vertical rise is slowing noticeably as drag and gravity dominate.

The ball reaches apex near t≈0.955s at about z≈4.47, x≈1.85, with vx continuing to shrink toward 1.36 and vz dropping to near zero. After the peak, as the ball starts descending and vz goes negative, the Magnus force flips direction and starts pushing x forward again, so I'm estimating how much horizontal velocity gets regained during the fall from 4.47 down to the 3.05m target height, which takes roughly 0.55s and contributes an additional Magnus-driven boost to vx.

Ball radius vs inner rim radius still fits fine. I confirm the Magnus force formula matches MuJoCo's documentation, so my spin analysis holds up. The simplest fix seems to be redesigning a clean trajectory — maybe stripping out fluid effects and spin entirely, computing a pure ballistic launch instead, or keeping just a small amount of backspin.

Since removing fluid density only matters for air drag (rim contacts behave independently), I'll just drop density and fluidshape to simplify. Then I need to design a launch from the floor to the hoop center at (4,0,3.05), descending steeply enough for a clean drop-through, making sure the ball's horizontal position stays within the rim's inner clearance (about ±0.109 after accounting for ball radius) as it crosses the rim plane.

For the descent angle, I'm working out that the effective horizontal opening scales with sin of the descent angle, so I need roughly 31.5° minimum, and I'll pick something steeper like 50°+ for safety. I also need to verify the trajectory clears the near and far rim tube edges with enough margin (over 0.1274 distance) before settling on an apex height and flight time to hit the center precisely.

Trying T=1.3 gives a 53° launch angle with apex near 3.92m, which looks reasonable, so I'll settle on vx=3.0769, vz=8.6313 for the throw. I should also sanity-check that MuJoCo's semi-implicit Euler integration with a small timestep won't introduce meaningful drift from these idealized projectile values.

I'm estimating the integration error is tiny (about 1.3cm low at the rim crossing), and I can compensate by nudging vz up slightly to ~8.641 to offset the lag — this correction is small enough to be negligible for the trajectory, so I'll move on to checking clearance against the front rim position.

Checking the trajectory at the front rim x-coordinate, the ball is about 0.288m above the rim vertically, which translates to roughly 0.19m perpendicular clearance given the velocity angle there — comfortably above the 0.1274m minimum needed, so this looks safe. I still want to verify this is really the closest approach point and check clearance against the back bracket/box structure near the rim too.

Computing perpendicular distance to both rims gives about 0.19, comfortably clearing the required 0.127 margin. Checking the bracket box next (x 4.24–4.381, z 3.028–3.052), the ball's trajectory stays well below its bottom edge with similar clearance, and the backboard's front face at x=4.381 also seems clear as the ball continues past.

So the ball hits the pole around 1.2m height and bounces back after passing through the hoop — that's acceptable, and the support base box shouldn't interfere. I also confirm the ascent path before reaching the rim stays clear, peaking at 3.92m near x≈2.69. For spin, I'll just set angular velocity to zero since it only matters at contact and complicates things unnecessarily.

I'm removing the density attribute entirely rather than setting it to zero, since leaving the fluidshape model active would still apply drag through its box inertia approximation. I'll explicitly add the qpos in the keyframe too, even though it would default to the body's initial position and identity quaternion anyway, just to be safe.

The ball starts exactly touching the floor with zero penetration, so there shouldn't be any significant contact force spike on the first step—it's fine to keep it that way since it's being "launched from the floor." Time to write up the final answer.

