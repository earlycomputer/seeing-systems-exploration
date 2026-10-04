**Change:** I raised the `shot` launch velocity to vx = 3.58 m/s, vz = 8.775 m/s (vy stays 0). The ball still starts at rest at (0, 0, 0.1194). These numbers come from a hand integration with assumed drag, not a simulation run, so they need confirming in MuJoCo.

**Fixing the miss**
- The original shot came down through rim height about 0.23 m short even without air, so it hit or fell in front of the front rim.
- I first chose a launch that would pass through the rim centre on the way down at about 46° in a vacuum.
- I then corrected for air drag. With the fluid settings in the file, drag works out to about 0.022 per metre of flight times speed squared.
- Drag costs roughly 0.3 m of reach and 0.5 m of height over the flight, so the corrected launch is faster.

**Predicted flight with drag**
- The ball peaks near 3.70 m at about t ≈ 0.85 s.
- It crosses the rim plane at about x ≈ 4.00, at t ≈ 1.21 s.
- It drops at about 48° below horizontal.

**Clearances**
- The closest approach of the ball's centre to the front rim tube is about 0.2 m. Contact would need under 0.127 m.
- The closest approach to the back rim tube is about 0.145 m.
- The backboard and bracket are not reached.

**Limits of this estimate**
- My integration used 0.1 s steps, so the real path could differ by a few centimetres.
- I assumed MuJoCo's blunt-drag force has no factor of ½. If it does, drag is half as strong and the shot would carry past the centre, possibly into the back rim. That clearance is only about 18 mm.
- A quick run in MuJoCo would settle both points.

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
    <key name="shot" qvel="3.58 0 8.775 0 0 0"/>
    <!-- Changed shot qvel from (2.9532, 0, 8.556) to (3.58, 0, 8.775). The old launch reached rim
         height about 0.23 m short even in vacuum, onto the front rim, and air drag made it shorter.
         The new launch, hand-integrated with the scene's air drag (density 1.2, blunt coefficient
         0.25, roughly 0.022 per metre times speed squared), peaks near z = 3.7 m. It descends
         through the rim plane at about x = 4.00 (rim centre), about 48 degrees below horizontal,
         and stays clear of the front rim, back rim, bracket and backboard.
         Not verified in simulation. If MuJoCo's drag formula includes a factor of 1/2, the shot
         carries long and the back-rim clearance (about 18 mm) is at risk. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to pick a velocity that accounts for drag, so I'm recalling how MuJoCo's ellipsoid fluid model computes drag force—combining blunt and slender body coefficients weighted by projected versus max cross-sectional area, scaled by density and velocity squared.

Using the default fluidcoef values (blunt=0.25), I estimate the drag coefficient as roughly 0.25*1.2*A, giving a drag constant k ≈ 0.0217 per meter, which is comparable to a real-world Cd~0.47 with the standard 1/2 factor. I'll ignore angular drag, Kutta lift, and Magnus effects since the sphere isn't spinning and these terms vanish or are negligible for this case, and I'll skip added mass effects since I'm not certain MuJoCo's current model accounts for them.

Now I'm working out the launch trajectory: I need the ball to descend steeply through the rim center at x=4, z≈3.05, avoiding the backboard and front rim. Testing a 55° launch angle in vacuum conditions with Δz=2.9306 and Δx=4, I compute tan(55°)=1.4281, giving x·tanθ - Δz = 2.7819, and solving for v² using the projectile range equation yields v² ≈ 85.75.

Checking this result, the ball arrives at the hoop with vz slightly positive — meaning it's still rising rather than descending, so 55° is too shallow and I need a steeper angle to get a proper descending entry into the rim.

Computing the apex height at about 3.42, only 0.37 above the rim, with an entry angle near 36° — checking the rim clearance rule, sin(36°) times rim diameter barely exceeds the ball diameter, so it's marginal. I should try a steeper angle, tanθ=2.5, to get safer clearance.

Recalculating velocity gives v≈8.97 with vx≈3.33 and vz≈8.33, time of flight about 1.2s, entry angle now 46° and apex height around 3.66 — much better margin. Now I want to account for drag, since the drag coefficient k=0.0217 produces a meaningful deceleration (~1.6 m/s² at launch speeds), so I need to perturbatively correct the trajectory for this effect.

I'll estimate the deficits by sampling the vacuum trajectory at several time steps (0, 0.3, 0.6, 0.9, 1.2s), computing the speed at each point, and using those to approximate the cumulative drag-induced position error in both horizontal and vertical directions.

Computing the final drag term at t=1.2, then applying Simpson's rule with these weighted integrand values to get δx≈0.31 m, and now setting up the same integration approach for δz.

That gives δz≈0.48 m, a fairly large drag correction. Since the deficits are nonlinear in speed, I'll try an iterative fix: re-aim the vacuum trajectory toward a shifted target (adding the drag deficits to the original offsets) and recompute, rather than trying to solve this analytically in one shot.

Since the vacuum velocities are higher than real ones, using them overestimates drag, so my estimate is probably shooting slightly long — that should be fine given the backboard sits at 0.381 from center. I want to verify this more rigorously with numerical integration using the candidate velocities vx=3.615, vz=8.775, stepping with a midpoint-style method and double-checking the drag coefficient calculation from the ball's cross-sectional area and density.

Checking the MuJoCo fluid drag formula against the documentation, I confirm there's no factor of 1/2 — the force is just density times the blunt drag coefficient times projected area times velocity squared, with the slender term vanishing for a sphere since max and projected areas are equal. That confirms my k value of 0.02167.

Added mass and spin effects don't apply here since there's no rotation. Now I'm setting up the Heun (RK2) integration with a 0.1 second timestep, computing the initial velocity magnitude and the resulting drag-adjusted accelerations in both x and z directions at t=0.

I'm predicting the velocities at the next step, recalculating drag with the new speed, then averaging the predictor and corrector accelerations to update vx and vz, and I'm about to update the position using the averaged velocity.

Continuing the numerical integration, I update velocity and position at t=0.2 using the corrector step, then begin computing the new acceleration values for the next iteration.

Continuing the predictor-corrector integration into t=0.3, computing drag-adjusted accelerations and updated velocity/position predictions through another RK-style step.

Continuing the predictor-corrector integration, I get updated velocities and accelerations for this step, landing on new position estimates x≈1.7336 and z≈2.7805.

Continuing the corrector step, I get vx=3.3194, vz=2.3806, updating position to x=2.0671, z=3.4202. Moving to t=0.6, I compute the new acceleration values and begin the predictor step again.

Continuing the predictor-corrector iteration for drag and gravity acceleration, updating velocity and speed values at t=0.7 to refine the trajectory estimate.

Continuing the correction step, I get updated velocity and position values, then move into the t=0.9 iteration with fresh acceleration calculations.

Continuing the predictor-corrector integration into t=1.0, computing updated velocities, drag magnitude, and acceleration components for the next timestep.

Continuing the predictor-corrector step, I get az≈-9.5877, then predict and correct vx and vz for the next iteration, landing on vx≈3.1635, vz≈-3.4733, and I'm starting to update the position x using these corrected velocities.

At t=1.2 the ball is at x≈4.013, z≈3.077, so interpolating to find where it crosses x=4, z comes out to roughly 3.09 - just slightly above the rim plane, meaning the trajectory passes within a few centimeters of center, which looks fine.

Checking the entry angle (~48°) and clearance against the front rim tube at several points along the path, the distance from ball center to the rim tube stays safely above the collision threshold of 0.127 throughout the approach.

Checking a few more intermediate heights along the ball's path, the clearance stays above the 0.127 threshold, bottoming out around 0.145 — tight but clean. I'm also comparing against the backboard bracket box position, which sits near the rim bracket coordinates, and noting the backboard front face x-position for the next clearance check.

To center the shot better, I'm nudging vx down slightly (to about 3.58) so the trajectory crosses the rim plane closer to x=4.00 instead of 4.04, accounting for the small Heun integration error with dt=0.1. I should also verify how MuJoCo's ellipsoid fluid model handles drag for this adjustment.

Checking whether added mass matters for the ellipsoid fluid model, I estimate it's around 0.0043 kg for a sphere this size versus the ball's 0.62 kg mass — completely negligible, so I can ignore it. The flight path should be fine; now I'll write the final file with the trajectory parameters and comments.

