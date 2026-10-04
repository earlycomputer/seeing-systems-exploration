The original launch (vx 2.9532, vz 8.556) brings the ball down through rim height about 0.23 m short even without air, and air drag makes it shorter still. I changed only the `shot` key's `qvel` to launch harder and on a steeper arc. The result comes from a hand integration of the ball's flight with air drag, not from running the scene, so it should be checked in MuJoCo.

**Air drag.** I assumed MuJoCo's ellipsoid-model drag force has the form C·ρ·A·|v|·v with no ½ factor; I'm fairly but not fully sure of that. With this ball's coefficient 0.25 and its size and mass, drag slows it by about 0.0217·v² m/s². That is roughly 2 m/s² at launch.

**New launch velocity:** vx = 3.307 m/s, vz = 9.16 m/s.
- The ball peaks at about 4.0 m near x ≈ 2.8.
- It comes down through rim height (3.05 m) at x ≈ 4.00, about 1.32 s after launch.
- It is falling at about 53° below horizontal there.
- Its path clears the front and back of the rim by about 0.065 m each.
- The flight is well clear of the backboard and bracket, and there is no sideways component.

**How sensitive this is.**
- If the drag force actually includes the ½ factor, the ball would cross about 0.2 m long. It would hit the back of the rim or the backboard, so it might not go in.
- With my drag assumption, a 0.06 m/s error in vx moves the crossing point about 0.08 m. The clean-entry margin is ±0.11 m.

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
    <key name="shot" qvel="3.307 0 9.16 0 0 0"/>
    <!-- Changed qvel from "2.9532 0 8.556 0 0 0" to "3.307 0 9.16 0 0 0".
         The old launch descended through rim height (z=3.05) at x~3.77 even without air,
         i.e. onto the front rim; with the air drag in this scene (density 1.2, blunt coef 0.25)
         it fell further short (~x 3.4-3.6). The new launch is hand-integrated with drag
         assumed as F = 0.25*rho*pi*r^2*|v|*v (decel ~0.0217*v^2), not run in MuJoCo.
         It peaks near z~4.0 at x~2.8 and comes down through rim height at x~4.00
         (t~1.32 s) at ~53 deg below horizontal, clearing front and back rim by ~0.065 m.
         If MuJoCo's drag includes a 1/2 factor, the shot lands ~0.2 m long (back rim/backboard).
         No lateral velocity, so no left/right error. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a new velocity that reaches x=4 at z=3.05 while descending, factoring in drag. I'll design a steeper no-drag trajectory first, picking a flight time and solving for vx and vz, then adjust for drag's effect on the descent angle.

Now I'm trying to recall the exact MuJoCo drag force formula for blunt bodies—whether it includes a factor of ½ or not—since I need this to properly correct the trajectory for air resistance. Given the default viscosity is zero, I'm leaning toward treating the drag coefficient as negligible for this calculation.

I need a target horizontal tolerance of about ±0.1 m at rim height, so I'm estimating the drag-induced deficit by approximating the trajectory with vx held constant and vz decreasing under gravity, then integrating the drag deceleration terms over time to see how much the range shrinks compared to the no-drag case.

Using trapezoidal integration, the horizontal deficit comes out to about 15.4k and the vertical deficit about 28k downward. Scaling this for k=0.0162 gives roughly 0.25 short and 0.45 low, while k=0.0217 gives about 0.33 short and 0.61 low.

I need to compensate by increasing velocity, since both x and z deficits respond directly to added speed with sensitivity T=1.3. But rather than treating x and z independently, what actually matters is the ball crossing z=3.05 while x sits between 3.89 and 4.11 — given the trajectory's descending slope of about -1.34, a height deficit at x=4 effectively shifts the crossing point backward horizontally by Δz/1.34.

For the higher drag case (k=0.0162), the combined shortfall works out to about 0.6 m past where it needs to land, so I need velocity corrections — roughly δvx = Δx/T and δvz = Δz/T — to shift the first-order landing position to match the target, while keeping in mind drag will slightly curve the slope too.

With second-order corrections for the extra drag from the boosted speed, I land on vx≈3.29, vz≈9.01. Then I check sensitivity: if the true drag coefficient is lower or higher than my assumed 0.0162, the shot overshoots or falls short by about 0.20 m, which is within the roughly ±0.11 m tolerance only loosely — I still need to nail down the actual drag coefficient more precisely.

I recall MuJoCo's fluid drag model uses a combination of blunt and slender drag coefficients weighted by projected area, so I'm trying to recall the exact formula to make sure my coefficient assumption matches the simulator's physics.

Confirming sphere projected area equals πr² and no viscous term applies since viscosity defaults to zero. Recomputing with k=0.0217 gives position deltas and velocity sensitivities, then adjusting upward roughly 10% to account for drag scaling with v² at the higher speed, though I note this linearization still ignores how the corrected velocities themselves alter drag over the flight.

Now I'm numerically integrating the trajectory with the adjusted initial velocities using an RK2-style stepping scheme, computing speed and drag-based accelerations at each timestep to verify the target is actually reached.

Continuing the RK2 integration step to t=0.2, updating position to roughly (0.660, 1.721) with velocity components around vx=3.243, vz=6.896, then starting the next step's midpoint velocity calculation.

Continuing the numerical integration for the next timestep, computing drag-adjusted acceleration and updating velocity and position values through the midpoint method.

Continuing the RK4 integration step, updating position to x=1.6118, z=3.3085 at t=0.5, then computing drag acceleration terms for the next midpoint velocity estimate.

Continuing the integration step, I update position and velocity to t=0.7, then begin computing drag forces for the next step at t=0.7 with the new speed around 3.512.

Continuing the trajectory integration into t=0.9, updating position and velocity with drag and gravity, now approaching z near 4 as the projectile nears its apex.

Continuing the drag integration, I compute the updated speed and accelerations, then advance position to x=3.4359, z=3.7549 with velocities vx=2.9753, vz approaching -2.0 at the next step.

Continuing the numerical integration, updating velocity and position through t=1.2, applying drag deceleration with the midpoint method for each half-step.

At t=1.3, position reaches x=4.026, z=3.125 and is descending through the target height. Crossing z=3.05 happens around x=4.08, slightly beyond the 4.0 m aim point but just within tolerance, so I'm looking at trimming vx a touch to pull the landing spot back to roughly 4.0.

Reducing vx0 to about 3.307 shifts crossing time to ~1.318 and brings the crossing x down to about 4.0, accounting for drag. I should also verify the trajectory doesn't clip the backboard or rim on the way up, checking the apex position around x≈2.8.

Checking clearances through the hoop: front rim at 3.7634, back rim at 4.2366, and factoring in ball radius, the trajectory passes with roughly 0.11m clearance at the back rim and stays comfortably above the rim tube near the front. As the ball continues descending through the ring, I'm tracking how x shifts with z to confirm it clears the back rim edge during the drop.

Front rim distance checks out the same, 0.192, so the shot is centered through the hoop with clearance at the bracket. I'll finalize the velocity as qvel="3.307 0 9.16 0 0 0" and note it in a comment.

