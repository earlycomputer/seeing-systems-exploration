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
    <key name="shot" qvel="3.35 0 8.67 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from (3.5952, 0, 10.416) to (3.35, 0, 8.67).
       Why: the old launch sent the ball to an apex near 5.6 m, so it sailed over the hoop and backboard and missed long.
       How the new value was found: I integrated the flight by hand with the scene's quadratic blunt drag
       (k = 0.5*1.2*0.25*pi*0.1194^2/0.62, about 0.0108 per m). It has not been confirmed by running MuJoCo.
       Expected flight from that hand integration:
       - apex about 3.8 m at x about 2.9 m;
       - descends through rim height (z = 3.05) at x about 4.0 m, about 1.25 s after launch;
       - entry angle about 50 degrees below horizontal;
       - clears the front and back rim tubes by about 5 cm;
       - passes under the backboard's bottom edge after dropping through. -->
</mujoco>
```

---
thinking (summarized):

I need to figure out the right launch velocity so the ball arcs through the rim center at x=4, z=3.05, clearing the front rim at x=3.763, accounting for drag (k≈0.0108/m) and a bit of Kutta lift, aiming for roughly a 45° descending entry angle.

Trying different launch angles without drag first: tanθ=1.5 gives vx=5.06, vz=7.58 but descent angle is nearly flat (bad). Tanθ=2 gives vx=3.93, vz=7.87 with ~28° descent. Settling on tanθ=2.5, which gives vx≈3.33, vz≈8.33, producing a ~46° descent angle through the hoop — this looks like the right trajectory shape to refine with drag.

Now estimating drag effects: speeds range roughly 9 m/s at launch down to ~5 m/s at the end, with drag deceleration on the order of 0.4-0.9 m/s². Working through how much horizontal distance is lost to drag over the ~1.2s flight, getting a correction factor to adjust the launch velocity.

I should also check whether MuJoCo's ellipsoid aerodynamic model includes viscous drag by default — it doesn't, since viscosity is zero unless explicitly set, so only blunt/slender drag, angular drag, Kutta lift, and Magnus effects apply here.

For a sphere, the slender-body term and Kutta lift vanish since they depend on the difference between projected areas or cross terms that are zero for a symmetric sphere, leaving just the blunt drag coefficient to compute using the standard drag equation with projected area based on the sphere's radius.

I'm now trying a numerical simulation with a starting guess of vx=3.55, vz=8.75, stepping forward in time with dt=0.1 using an improved Euler method, computing drag-adjusted accelerations at each step to see where the trajectory lands.

Continuing the predictor-corrector integration, I get v2 values and update position to x2=0.7034, z2=1.6582, then move into step 3 of the trajectory calculation.

Continuing the drag integration, z3 comes out to 2.2714. I continue to step 4, computing speed and drag-adjusted accelerations at the current and predicted points, averaging them, then updating velocity to vx=3.4360, vz=4.6024.

Updating position: x4=1.3954, z4=2.7824. Now stepping into step 5, I'm recomputing speed magnitude and drag acceleration at this point, then predicting the next velocity (vx=3.4146, vz=3.5928) to average the accelerations again.

Continuing the averaged values give v6 with vx≈3.399, vz≈2.601, updating position to x6=2.0788, z6=3.5023. Moving to step 7, I compute drag forces again and get predicted velocities vx≈3.383, vz≈1.608 with reduced speed magnitude around 3.746.

Continuing the drag integration into step 9, computing velocity magnitude, drag accelerations, and updating position via averaged trapezoidal steps for x and z.

Continuing the drag integration, I compute step 10's velocity and position: vx10≈3.346, vz10≈-1.334, giving x10≈3.4275 and z10≈3.8381, applying the same predictor-corrector approach with drag deceleration dominating the downward velocity component.

Moving to step 11, I compute the velocity magnitude ~3.602, derive drag accelerations ax≈-0.1307, az≈-9.758, then predict forward and correct using averaged values, landing on vx11≈3.332, vz11≈-2.308, with x11 staying near 3.4275 as horizontal motion stabilizes.

Continuing to step 12, I recompute speed ~4.053, get ax≈-0.1464 and az≈-9.709, then predict new velocities and recheck magnitude ~4.664, giving refined accelerations ax≈-0.1677, az≈-9.644 for the next averaging pass.

Now I'm averaging to get ax=-0.157, az=-9.6765, updating position to x≈4.094, z≈3.292, and checking when x reaches 4.0 to see if z lands near the target 3.05, interpolating velocity and curvature between t=1.1 and 1.2 to estimate z at that point.

That gives z≈3.38, about 0.33 m too high. I'm considering the front rim constraint (x≈3.763-3.771, z must clear roughly 3.18) and estimating the descent angle (~38°), then adjusting vz downward by about δ≈0.28 to bring vz to roughly 8.47, lowering the trajectory to hit the target height while checking how this affects the entry angle.

Actually I'm weighing whether a steeper ~45° entry is safer given the rim-to-ball clearance (0.457 m opening vs 0.239 m ball, with only ~0.04 m margin at 38°), so I'm testing an alternative with vx=3.25 and recomputing vz, accounting for drag decay over the flight time to x=4.

Working through this, I get vz≈8.785 at launch, giving entry vz around -3.7 and vx around 3.1, so roughly a 50° angle — though my estimates feel shaky. Rather than trust this rough algebra fully, I think it's safer to adjust the existing simulation incrementally, tweaking vz slightly while keeping vx near 3.55, since reduced vz means slightly less drag and earlier arrival in x.

Running the simulation with vx=3.35, vz=8.70...

Continuing the RK2 integration for step 2, computing drag-adjusted acceleration with the new speed magnitude, then averaging predictor and corrector values to get vx2=3.29001, vz2=6.59881, and starting the x2 position update.

Averaging the predictor-corrector values gives x3=0.99159, z3=2.25694 for this step, and I'm continuing into step 4 with the drag-adjusted acceleration terms to find the next velocity and position estimates.

Continuing the integration, I compute step 5 giving vx≈3.226, vz≈3.554, position x5≈1.641, z5≈3.169, then begin step 6 with updated speed and drag calculations.

Continuing the predictor-corrector integration for step 7, computing drag-adjusted acceleration and updating velocity to vx=3.19714, vz=1.56802, with x7 landing at 2.28278 and z7 next to compute.

Now I'm moving to step 8, applying the same averaging scheme: computing speed magnitude, drag-based ax and az, predicting velocity, then recomputing drag at the predicted state to get averaged accelerations, which are coming out to roughly ax=-0.11759 and az still being worked out.

Continuing the step-by-step velocity integration, I compute averaged accelerations to update vx and vz at step 9, then propagate x9 and z9 from those averaged velocities before starting the same prediction-correction cycle for step 10.

Continuing the drag-adjusted projectile integration, I compute step 11's predictor-corrector velocities and positions, getting vx≈3.150, vz≈-2.350, with updated position x11≈3.552, z11≈3.523, then move into step 12's speed calculation.

Continuing to step 13, I check when x reaches 4: the height comes out about 0.039 above target, with velocity angle around 50°, which looks good. I also check the front rim position at x=3.763 and find the corresponding height.

Now I'm verifying the ball clears both rim edges. Treating the trajectory as a straight line locally, I compute the perpendicular distance from the front rim point to the ball's path — about 0.1815, which exceeds the 0.1274 clearance needed, so it's safe. The back rim at x=4.237 gives the same distance, so it also clears.

I'm adjusting for the small vertical offset at x=4.0, which shifts where the ball crosses the rim's z-plane slightly forward to about x=4.033. This reduces the back-side clearance margin to about 0.156, still above the 0.127 threshold, so I'll tune vz down slightly to around 8.67 and use qvel "3.35 0 8.67 0 0 0" to center the crossing near x=4.0. Now I'm checking the backboard position at x=4.381 to make sure the ball passes through the rim before it could reach that face.

Checking the bracket clearance again confirms the trajectory stays safely clear by about 0.17m, well past the 0.119m threshold needed. After passing through the hoop, the ball falls toward the floor—with the given velocities, it lands around x≈5.45m, which would hit the support base located between x=4.8 and 5.6.

Looking more carefully, the ball actually passes under the backboard (which spans z 2.9 and up) since the ball's position stays around z≈2.58-2.72 at that x-range, clearing it safely. It then likely strikes the pole near x=5.1 at roughly z≈1.5, but since that happens after the ball has already gone through the hoop, this collision is acceptable for the "first landing" requirement—in a real setup the net would catch it, but this approximation is fine.

