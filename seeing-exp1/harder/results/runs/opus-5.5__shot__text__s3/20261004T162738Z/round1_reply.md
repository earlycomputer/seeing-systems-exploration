**Expected behaviour of the submitted file**

- The ball starts at the floor with velocity (3.21, 0, 9.3) m/s and backspin ω_y = −30 rad/s.
- Air is on: `density="1.2"`, and the ball has `fluidshape="ellipsoid"` with a Magnus coefficient of 1.
- MuJoCo's Magnus force is ρ·V·(ω×v). At launch that is about (−2.4, 0, +0.8) N on a 0.62 kg ball. That is a backward pull of roughly 3.9 m/s², about five times what a real basketball sees. Blunt drag adds about 0.7 m/s² more.

Integrating by hand:

| t (s) | v_x (m/s) | position |
|---|---|---|
| 0.5 | ~1.7 | — |
| ~0.95 (apex) | — | x ≈ 1.85 m, z ≈ 4.47 m |
| ~1.5 (falling through z = 3.05) | — | x ≈ 2.7 m |

So the ball lands about 1.3 m short of the hoop.

Without air the same launch would also fail. It would be about 1 m above the rim at x = 4 and come down through rim height near x ≈ 4.8, which is into the backboard.

**Fix**

- Remove the fluid model so the flight is purely ballistic and predictable.
- Lift the ball 6 mm off the floor so no floor contact acts on the first step.
- Retune the launch for a 1.3 s flight through the rim center (4, 3.05):
  - v_x = 4/1.3 = 3.077 m/s.
  - v_z = (2.925 + 4.905·1.3²)/1.3 = 8.627 m/s.
- Resulting flight:
  - Apex is about 3.92 m.
  - Entry is about 53° below horizontal, with velocity (3.08, −4.12) m/s at the rim.
  - The perpendicular distance from the ball path to the rim tube centers is about 0.19 m on both near and far sides. Contact would need less than 0.127 m, so it clears with about 6 cm to spare.
- After the rim:
  - It clears the bracket top edge (perpendicular distance about 0.19 m against a radius of 0.119 m).
  - It clears the backboard's bottom edge: when the ball is fully below z = 2.9, its front is at x ≈ 4.30, short of the face at 4.381.
  - It then falls and strikes the support pole near z ≈ 1.2 m, which is after the basket.

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

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg (hollow shell inertia 2/3 m r^2); starts 6 mm above the floor -->
    <body name="ball" pos="0 0 0.125">
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

  <!-- Ballistic shot: 1.3 s flight, apex ~3.92 m, enters rim center at ~53 deg descent -->
  <keyframe>
    <key name="start" qvel="3.077 0 8.627 0 -20 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "With the given file, MuJoCo's strong Magnus force from the -30 rad/s backspin plus drag kills the forward speed: the ball peaks near x 1.85 m, z 4.47 m and drops back through rim height around x 2.7 m, falling about 1.3 m short of the hoop.", "works": false, "problem": "The fluid model's Magnus force (coefficient 1 at 30 rad/s backspin) and drag decelerate the ball so it lands about 1.3 m short of the hoop at x = 4 m; without air the same launch would overshoot into the backboard."}
```

---
thinking (summarized):

I'm working out the ball's trajectory starting at a small height with forward and upward velocity, considering that the spin direction (wy=-30) actually represents backspin given the positive x-motion, and factoring in fluid drag with the ellipsoid shape enabling the Magnus effect.

Checking the no-drag ballistic path, I find the ball would reach around 4.09 m height at x=4 instead of the target rim height of 3.05 m, meaning it overshoots unless drag and Magnus lift pull it down and shorten the range—so the apex and fall calculations without drag land the ball around x=4.80, confirming drag effects must be doing real work here. Now I'm setting up the blunt drag force equation to quantify that effect.

This gives acceleration around 0.0217/m per unit velocity squared, so with v≈9.8 m/s the deceleration from drag is about 2 m/s², which is meaningful. Working through the Magnus force next, with V≈0.00713 for the ball's volume and C_M=1, I compute ω×v using the spin vector (0,-30,0) and velocity (3.21,0,9.3), giving a cross product of roughly (-279,0,96.3), which scales to a Magnus force near (-2.39, 0, 0.82) N.

Converting that to acceleration gives roughly (-3.85, 0, 1.33) m/s² — a large backward component. This makes sense physically: backspin on a ball moving up and forward produces lift that's perpendicular to the velocity, which effectively points back and up relative to the trajectory. I still need to account for angular drag decaying the spin over time, so I'm estimating that decay rate next.

Working through the angular drag torque, I get roughly 0.066 N·m initially, which with the sphere's rotational inertia gives an angular deceleration constant k ≈ 0.01244, leading to ω(t) ≈ 30/(1+0.373t) as the spin decays over the flight.

Checking Kutta lift, I realize it should vanish for a sphere since the projected area is symmetric and doesn't depend on orientation, so that force term drops out entirely. Now I need to set up a numerical integration starting from the initial state (position, velocity, spin) and step through the drag and gravity accelerations over time.

At the first timestep I compute the drag coefficient term and the Magnus coefficient from spin, finding the x-acceleration comes out negative (slowing the forward velocity) and the z-acceleration is dominated by gravity minus drag plus a smaller Magnus contribution, giving a steep downward acceleration overall. I'm proceeding with a small timestep to integrate forward.

Using this to get x1=0.300, z1=0.998 after the first step. I'm also tracking how the angular spin decays over time with a simple decreasing function, computing values at several time points for later reference, though I'm not fully certain about the drag torque coefficient I'm using. Moving on to the second integration step from t=0.1.

Continuing the step-by-step integration: for step 3 (t=0.2→0.3) I get v3=(2.154, 6.249), landing at x3=0.792, z3=2.449. Moving into step 4 (0.3→0.4) with ω=26 now.

v5 comes out to about (1.73, 4.30), giving x5=1.178, z5=3.503. The horizontal speed is dropping fast, and I still need to reach x=4, so I keep iterating. For step 6 (0.5→0.6) with ω=24.9, using mid velocity (1.64,3.81), I compute ax≈-1.456 and start working out az.

Continuing the integration, v6 ends up (1.583,3.337), x6=1.344, z6=3.885. Moving to step 7 (0.6→0.7) with ω=24.1, mid velocity (1.52,2.86), I get ax≈-1.058 and az≈-9.505, yielding v7=(1.477,2.387) and x7=1.497, with z7 still to be computed.

Working through step 7's z-position: z7=4.171. Then step 8 (0.7→0.8) with ω=23.4 gives ax≈-0.691, az≈-9.447, so v8=(1.408,1.442), x8=1.641, z8=4.362. Now moving into step 9 (0.8→0.9) with ω=22.8, computing the acceleration components from the midpoint velocity (1.39,0.97).

The trajectory reaches apex around t≈0.95 with z≈4.47, x≈1.85, then starts descending — at this point the Magnus force's x-component flips sign to positive since vz becomes negative, pushing the trajectory forward. Continuing into step 10 (0.9→1.0) with ω=22.2, I compute ax≈-0.050 and az≈-9.391, giving the updated velocity components for that step.

Stepping into step11 (1.0→1.1) with ω=21.6, I get ax≈0.222, az≈-9.366, giving v11≈(1.389,-1.375) and position x11≈2.055, z11≈4.371, confirming the descent has begun. Moving into step12 (1.1→1.2) with ω=21.0...

Continuing to z12=4.187, x12=2.196, I'm now estimating the remaining trajectory: the ball needs to cover the gap to x=4 while z drops to 3.05 (1.14 m), and given the current vz trend, it looks like the ball lands around x≈2.7, falling about 1.3 m short of the hoop — so this trajectory misses. I'm second-guessing whether my Magnus force model is accurate enough to trust that conclusion.

Comparing real-world Magnus lift to MuJoCo's computed force, I find MuJoCo's coefficient makes the effect roughly 5x stronger than physically realistic—this is just a quirk of the scene setup. The simplest fix is to zero out the fluid density and instead pick a launch velocity that produces a clean ballistic trajectory to the target.

Keeping backspin for visual realism is fine since without fluid dynamics it won't actually affect the flight path, though rim contact could still matter. Now I'm working out the geometry needed for the ball to pass cleanly through the hoop: given the ball radius and inner rim radius, I need to calculate the minimum descent angle that provides enough clearance for the ball to fit through without touching the rim.

I also need to check that the ball won't clip the backboard — since there's no net, after passing through the rim plane the ball continues forward and down, so I need to verify its trajectory clears the backboard's bottom edge and bracket before settling on an apex height for the shot.

Trying T=1.2s with vx=3.333 m/s gives vz≈8.328 m/s at launch, landing angle around 46° at the rim, with apex height roughly 3.65 m — close to the steep entry I wanted.

Bumping to T=1.3s gives a better fit: vx=3.077, vz=8.631, launch speed ~9.16 m/s, entry angle ~53°, apex height ~3.92 m. Now I need to verify clearance near the rim at x≈3.76 (tube center), z=3.05, checking the ball doesn't clip the tube given its radius of 0.008 m and the 0.1274 m combined clearance threshold.

Approximating the trajectory as a straight line near the rim, I compute perpendicular distances from the near and far rim points to the ball's path, getting about 0.1895 m on both sides — comfortably above the 0.1274 m threshold, so clearance is roughly 6 cm. Curvature over that short span should be negligible, so this trajectory looks safe.

Both rim deviations are tiny (under 4mm), confirming the ball clears both sides safely. Now I'm checking the bracket position after the ball passes the rim, working out its coordinates and clearances.

Checking the near top corner of the bracket—the perpendicular distance comes out around 0.193m, well clear of the ball's radius, so the ball misses it too. Now I'm locating the backboard's bottom edge and front face to see where the ball's path intersects them.

I'm computing when the ball drops fully below the backboard (around s≈0.0597s, x≈4.184), confirming it clears the backboard since its front face x stays under the backboard's x position. Continuing the trajectory down to the floor, I solve the quadratic for fall time (s≈0.4596) giving x≈5.414, which I need to check against the support pole's footprint spanning x from 5.1 to 5.3 and base width 4.8 to 5.6.

Checking further, the ball actually collides with the support pole around z≈1.24 after already passing through the hoop, so I decide that's acceptable since the score already happened — the ball would just bounce off afterward, which is physically fine to leave as is. I'm also reconsidering whether to simplify drag modeling, keeping Magnus effect at zero and using a blunt drag coefficient around 0.25 for simplicity.

Since recomputing trajectories with full drag is complex, I decide to drop the fluid interaction entirely by removing the density and fluidshape attributes, accepting that the resulting air drag omission is a minor inaccuracy over the roughly 1.3 second flight. I also want to double check the ball's starting contact with the floor — it touches at z=0.1194 with zero distance, so friction from the initial spin of -30 could slightly perturb the launch velocity during the first simulation step since MuJoCo registers contacts at zero margin.

Instead I decide to start the ball slightly above the floor at z=0.125 for a small 6mm gap, avoiding that initial contact ambiguity. Recomputing with this new z0 gives a height difference of 2.925, so vz becomes 8.627 while vx stays at 3.077. Since there's no fluid drag, spin won't affect flight physics, so I settle on a modest backspin of wy=-20 just for visual realism when it eventually contacts the floor or pole.

For the solver reference parameters I'll use 0.01 0.2, which should work fine for bounce behavior. The freejoint velocity is linear in world coordinates and angular in the local frame, which is correct for this setup. I also confirm that density isn't needed and the timestep option is sufficient, so I'm ready to write up the final answer.

