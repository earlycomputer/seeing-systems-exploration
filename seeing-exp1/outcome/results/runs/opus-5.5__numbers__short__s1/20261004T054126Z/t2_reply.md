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
    <key name="shot" qvel="2.975 0 9.8 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from "2.9532 0 8.556 0 0 0" to "2.975 0 9.8 0 0 0".
       Why: the old launch was too flat. It peaked at ~3.54 m and came down through rim height
       (3.05 m) at x ~ 3.14 m. That is ~0.86 m short of the rim centre (x = 4.0), so the ball
       passed under the hoop.

       How the new values were chosen:
       - The logged trajectory fits gravity plus quadratic air drag with
         |a_drag| ~ 0.022 * |v| * v (1/m).
       - Under that model, raising vz to 9.8 m/s gives an apex of ~4.5 m.
       - At vx = 3.2 m/s that steeper arc reached rim height at x ~ 4.29 m (long), so vx was
         scaled down to 2.975 m/s, plus a small correction for the reduced drag.
       - The ball should then descend through z = 3.05 m at x ~ 4.0 m. It comes down steeply
         (~60 deg), with ~0.1 m of clearance to both the front and back of the rim.
       - It then falls under the backboard's bottom edge.

       The y and angular components stay zero, so there is no left/right error.
       Not yet confirmed: these values come from a hand-integrated drag model, not a re-run
       of MuJoCo. Re-simulate to check the ball crosses rim height near x = 4.0. -->
</mujoco>
```

---
thinking (summarized):

I need to figure out the velocity so the ball passes through the rim center, accounting for air drag slowing it down over time. Looking at the trajectory data, the horizontal velocity appears to decay noticeably from around 2.82 early on to about 2.46 later, so I need to account for that drag effect rather than assuming constant velocity.

Checking the vertical motion too: without drag, the apex would be at t=0.872 reaching about 3.85m, but the actual apex is only 3.54m, showing drag is substantial. I'm trying to empirically estimate a drag coefficient k from the deceleration pattern, roughly solving k*|v|*vx for the observed slowdown, getting k≈0.2, which seems much larger than a typical basketball's physical drag coefficient (~0.02) -- MuJoCo's fluid model must be including extra viscous and Kutta lift terms beyond simple quadratic drag. I'm now cross-checking this against the vertical motion data to see if it's consistent.

Trying to back out the effective drag area from the sphere's projected cross-section doesn't match cleanly against the empirical k value, so the slender drag term must be contributing too. I decide to just trust the empirical fit rather than fully decompose the coefficients, and move to checking velocity near the apex of the flight to cross-validate.

I'm comparing deceleration rates at different points in the trajectory — near launch versus near the apex — and getting inconsistent values for the drag coefficient, which suggests my velocity estimates from position differences are too noisy to pin down precisely. I need a cleaner way to estimate instantaneous velocity instead of these rough finite differences.

Estimating drag coefficient from the velocity decay: vx drops from 2.92 to 2.68 over 0.75s, giving roughly 0.32 m/s² deceleration, which fits k≈0.02 for quadratic drag—consistent with realistic basketball physics. The anomalous first interval is likely a contact/initial condition artifact, so I'm now double-checking the vertical motion trajectory for consistency.

But comparing actual vz against the no-drag prediction, I'm seeing the ball lose more speed than expected in just the first 0.05s—about 0.37 m/s extra in vz and some in vx too. This is puzzling since drag alone shouldn't cause this much loss right at the start; I wonder if it's related to the initial contact solver settings (solref) causing a penetration impulse, or possibly some other force term like Kutta lift being included unintentionally. I want to isolate what's happening specifically after t=0.05 to see if the model behaves normally from that point onward.

That gives rise height around 3.12, but actual is 3.02, suggesting drag coefficient closer to 0.03 rather than 0.02. Trying another angle, I should fit empirically instead: the trajectory needs to land at rim height at x=4.0 rather than 3.14, and comparing the velocity at t=0.05 to the given initial values shows an unexplained loss of about 0.5 m/s in vz, equivalent to 10 m/s² of extra deceleration — maybe MuJoCo's ellipsoid collision/drag model behaves differently than my simple quadratic drag assumption at higher speeds.

But since the ball is moving away from the floor, that contact constraint shouldn't really apply, so friction isn't the culprit there. Maybe the keyframe's starting z is just qpos0's default body position, 0.1194, which seems fine. I try plugging k=0.022 straight into the integration to check x at t=0.05, getting about 0.1469 versus the data's 0.141, so there's still a gap of roughly 0.006 I need to account for.

Checking z the same way gives about 0.533 versus 0.516, a gap of 0.017 — and that ratio of z-diff to x-diff (~2.9) matches vz/vx closely, suggesting the discrepancy behaves like an overall velocity scaling of about 4% rather than a position-independent effect. That points toward something like added mass in MuJoCo's fluid/ellipsoid model, which includes blunt and slender drag, angular drag, and lift coefficients — added mass would show up in the effective inertia.

But computing added mass for a sphere of this size gives only ~0.0043 kg, negligible against the object's 0.62 kg mass, so that doesn't explain a 4% effect. I'm now reconsidering whether the data reflects some different timing offset, and checking the second differences in z across the later rows to see if gravity alone accounts for the pattern.

Looking at the numbers, the accelerations from second differences come out around -11 to -10.8 m/s², noticeably more than pure gravity's -9.8, implying extra drag around 1.2-1.4 m/s² at the given speeds. Solving for a drag coefficient from that gives k≈0.022-0.023, matching my earlier estimate well. So the quadratic drag model with k≈0.022 fits consistently, and I'm left wondering if the roughly 4% velocity loss in that very first interval comes from something else entirely — maybe a contact-related effect at t=0 rather than the fluid model itself.

Let me test this against the x and z data directly: computing velocities between t=0.05 and t=0.10 shows vx stays near 2.9, almost unchanged from initial, which contradicts a uniform velocity-loss model — so the discrepancy at t=0.05 looks more like a position offset than a velocity reduction. The z data similarly shows average vz around 7.72 versus an expected 8.56 without drag, reinforcing that something other than simple drag is shifting the early position.

This actually fits a one-timestep logging offset (~0.002s), since multiplying that interval by the velocities gives exactly the observed discrepancies (-0.006 in x, -0.017 in z) — so this is just an artifact, not a physical effect, and I can treat the real dynamics as pure quadratic drag with k≈0.022. Now I want to simulate this model forward to check it against the rim-crossing data.

Rather than doing a full numerical integration by hand, I'm trying a scaling approach: I want a new trajectory passing through roughly (4.0, 3.05 descending), so I'm testing a launch angle near 55° and sketching out the no-drag approximation first — picking a vz around 9.5 and working out what vx and apex height would be needed to land near that point.

Solving the no-drag equation gives T≈1.552s, vx≈2.58, with a steep descent angle around 65°, which looks like it has reasonable margins. Now I want to layer in the drag correction, so I'm comparing against the original calibrated data (v0 ≈ 2.953, 8.556) to see where the no-drag trajectory would cross z=3.05 while descending, as a way to sanity-check the drag-adjusted result.

Comparing the predicted no-drag x≈3.767 against the actual observed x≈3.14 at t≈1.14, drag has shortened the range by about 0.63 m — roughly 17%, which is substantial enough that I need to integrate the equations of motion properly rather than approximate. I'm setting up the drag acceleration equations with k=0.022 and planning to numerically integrate using improved Euler (Heun's method) with dt=0.1, starting by validating k against the original trajectory before applying it to the new candidate.

Stepping through the Heun integration: computing the speed magnitude and drag acceleration at the initial state, using that to predict the next velocity, then averaging the predictor and corrector accelerations to update velocity and position incrementally.

Matches at 0.574, 1.591, confirming the consistent offset and validating my k value. The offset seems like the simulation running one step behind, but that shouldn't affect the path shape itself, just timing—so it's fine for design purposes.

Now I need a candidate initial velocity that accounts for drag loss, which costs roughly 17% of the x-distance in the original case, with larger vz increasing flight time and thus drag. I'll try v0=(3.2, 9.8) with k=0.022 and integrate forward with dt=0.1 until z descends back through 3.05, starting from x=0, z=0.119.

Continuing the velocity integration...

Continuing the RK2 integration steps, updating velocity and position through t0.4 and into t0.5 with drag deceleration gradually tapering as speed decreases.

Continuing to step through the drag-affected trajectory, computing velocity and position updates at each half-second interval using the predictor-corrector averaging scheme.

At t=0.9, v10=(2.8267,-0.7042), giving x≈2.9666, z≈4.4898. I'm noting the apex occurred around z≈4.51 near x≈2.75, and now I need to figure out how much farther horizontally the object travels while falling the remaining 1.44 units to reach z=3.05.

Continuing to step forward: at t=1.0, v11≈(2.8076,-1.6769), updating position to x≈3.2483, z≈4.3707. I'm iterating through these small time steps to pin down exactly when the descent reaches the target height.

Continuing the drag simulation iterations, updating velocity and position through t1.3 and into t1.4, tracking acceleration from drag forces as speed decreases each step.

Checking where the trajectory crosses z=3.05 between t=1.4 and 1.5, I find it lands around x=4.29, which overshoots the target by about 0.29 m. To correct this, I need to scale down the initial horizontal velocity by roughly a factor of 0.9324, adjusting vx from 3.2 downward and preparing to rerun the simulation with the corrected value.

Checking feasibility with rim clearance: inner radius 0.2286, ball radius 0.1194 leaves about 0.109 m margin for the center. At crossing the trajectory is steep, around 64°, so the ball should clear the rim without grazing front or back, and my numerical integration error from using Heun's method with dt=0.1 should be small given the smoothness of drag and gravity.

Still, I want to redo the integration with vx=2.98 to pin down x more precisely — with less drag, both the horizontal decay and the flight time increase slightly, pushing x somewhat higher than a naive linear scaling would suggest, so I should reintegrate carefully rather than estimate.

Vertical drag reduction adds a tiny bit more, pushing distance up by about 0.01m total. Testing vx=2.975 gives x≈3.998, close enough to the target of 4. Setting qvel to "2.975 0 9.8 0 0 0" and checking the apex trajectory clears any obstacles near the backboard.

Tracing the descent after the rim plane, the ball's edge passes safely under the backboard bottom at z=2.9 as x increases past 4.26, so it clears the bracket region without collision.

Now checking the far rim clearance: as the center drops 0.1 below rim height while x shifts to 4.05, the distance from the ball surface to the rim tube comes out to 0.212, well clear of the 0.127 combined radius threshold. I'm now checking the front rim at x=3.763, z=3.05, tracking where the ball's center sits as it approaches from the left on its steep descent.

