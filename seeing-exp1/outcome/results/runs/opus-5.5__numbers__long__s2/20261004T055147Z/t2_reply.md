I lowered the launch speed and kept the original direction (about 71° above horizontal; I used 70°). The old shot was about 1.7 m too high at the rim and flew over the backboard.

To set the new speed, I estimated the air drag from the logged trajectory: the horizontal speed falls from 3.45 to 3.05 m/s, which gives a drag constant of about 0.022 per metre. I then integrated the new shot by hand with that drag. I have not run it in MuJoCo, so the result is a prediction from that calculation.

At 9.73 m/s, the ball's centre is predicted to cross the rim height at x ≈ 3.99–4.01 m, coming down at about 55°. At that angle the ball can pass between the front and back of the rim if its centre crosses anywhere from about 3.92 to 4.08 m. That leaves roughly 8 cm of margin either way, which is larger than the uncertainty in the drag estimate.

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
    <key name="shot" qvel="3.3279 0 9.1432 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from "3.5952 0 10.416 0 0 0" to "3.3279 0 9.1432 0 0 0".
       Old shot: ~11.0 m/s at ~71 deg. Its centre passed x = 4 m at z ~ 4.72 m, about 1.7 m above
       the 3.05 m rim. It cleared the backboard and hit the support, a long miss.
       New shot: 9.73 m/s at 70 deg above +x, still launched from rest on the floor, with no
       sideways (y) velocity and no spin. Speed was chosen using the quadratic air drag measured
       from the logged flight (k ~ 0.022 per metre, from the decay of horizontal speed). With that
       drag, the centre should peak near z ~ 3.98 m at x ~ 2.7 m and come back down through the
       rim height at x ~ 3.99-4.01 m, descending at ~55 deg. At that angle the clean window for the
       centre is roughly x = 3.92-4.08 m, so the ball should drop through the hoop without touching
       the rim, bracket or backboard. This is a hand-integrated prediction, not yet confirmed by a
       MuJoCo run. -->
</mujoco>
```

---
thinking (summarized):

I need to figure out a new launch velocity accounting for drag, since the ball is an ellipsoid with density 1.2 and must pass through (4,0,3.05) while descending, starting from (0,0,0.1194). I'm checking the original no-drag trajectory's apex time and height to see how far off it is from what's needed.

Comparing observed positions against no-drag predictions, drag is clearly significant—apex height and horizontal reach are both notably lower than the no-drag case. I'm estimating the drag deceleration from early velocity data, solving for the drag coefficient k in ax = -k·v·vx, but the resulting k seems too large compared to a typical basketball's physical drag coefficient, so I'm now considering whether MuJoCo's ellipsoid fluid model includes added mass or other effects (blunt/slender drag, angular drag, Kutta and Magnus terms) that could explain the larger deceleration.

Checking k using velocity data near the apex gives a much smaller value than the early-trajectory estimate, suggesting the deceleration isn't purely quadratic in speed—maybe there's a combination of linear and quadratic drag terms, so I'm pulling more velocity samples from the start of the trajectory to pin this down.

The first interval looks oddly lower than the second, which could be an artifact of initial floor contact or rounding rather than true drag behavior, so I'm tracking vx across a mid-range window to get a cleaner decay estimate.

Computing deceleration from the mid-segment gives roughly 0.64 m/s², and solving k*v*vx = 0.64 yields k ≈ 0.0195, consistent with realistic quadratic drag coefficients around 0.02. The apex calculation gives a rougher match, so I'll settle on k somewhere in the 0.02–0.025 range.

Looking at vz, gravity alone predicts about 0.49 m/s decrease per 0.05s interval, but the observed drops (0.60, then 0.56) suggest some extra deceleration beyond pure gravity, pointing to drag affecting the vertical component too.

Checking that extra vz loss against k*v*vz gives k≈0.019, which matches nicely. But the initial horizontal and vertical velocities both seem to drop more than expected right at launch, which doesn't fit drag alone — maybe there's floor contact or penetration at the start, though that should push the ball up rather than slow it down. I'm now wondering if the ellipsoid collision model in MuJoCo is missing added mass effects that would explain this discrepancy.

I wonder if contact damping or the unilateral nature of MuJoCo's constraint forces could explain an initial velocity loss that isn't pure friction—maybe the launch effectively delivers only ~95-96% of commanded velocity before settling into consistent behavior, which would explain why interval 2's vx is actually higher than interval 1's.

Let me calibrate empirically instead: using central differences at t=0.10, I get vx≈3.51 and vz≈9.22, compared to the no-drag prediction of vz=9.435 at that time. That's roughly a 2.3-2.4% loss in both components—consistent with drag decelerating velocity by about that amount over the first tenth of a second given k=0.02 and v~10.5.

So k≈0.02 for quadratic drag along the velocity direction seems right, and the earlier anomaly at the very first interval is probably just a position-tracking artifact. Checking this against the full trajectory, though, the apex height of 5.01 vs the no-drag value of 5.65 is a big gap—I'm computing the vertical rise reduction using the drag formula for height under quadratic resistance.

Now I need to design the actual shot: from the release point to the hoop, accounting for the rim's inner radius, the tube thickness, and the ball's own radius to figure out how much clearance the ball's center needs as it passes through.

Trying a no-drag estimate first: at 60° launch angle, solving for v0 gives about 8.86 m/s, but when I check the resulting entry angle at the hoop it comes out around 15°, which is way too shallow for a clean shot—something's off since the trajectory needs a steeper descent into the basket.

Let me try steeper launch angles instead. At 65°, I get v0≈8.82 and an entry angle of about 34°, still fairly shallow. Pushing to 70° to see if the entry angle steepens enough for a realistic shot.

Working through the 70° case, I land on v0≈9.12 with an entry angle around 52°, which looks much better — so roughly 70° seems like the right launch angle. Comparing to the original shot's angle of about 71°, it seems the original speed was just too strong; I should keep a similar angle but reduce the speed. Now I need to bring drag (k=0.02) into the simulation and calibrate against the original trajectory's known point at x=4, z=4.72 to find the right lower speed, probably simulating manually around v0≈9.6 and adjusting from there.

Simulating the drag trajectory numerically...

Continuing the RK2 integration into step 2, updating velocity and position with the new drag-adjusted accelerations, giving x≈0.645, z≈1.697.

Moving into step 3, computing speed magnitude and drag accelerations again, then the midpoint estimates for velocity before refining the next update.

Continuing the midpoint update to position and velocity, I move to t=0.4 and begin step 5 with new drag calculations, then start computing the mid-step velocities for the next iteration.

Continuing the midpoint integration, I compute drag deceleration terms and update velocity and position at t=0.6, getting x=1.8826, z=3.5714, vx=3.0329, vz=2.6442, then move into step 7 with the new speed calculation.

Continuing the RK2 integration into step 8, updating velocities and accelerations with drag as t reaches 0.7, computing midpoint estimates for the next position update.

Continuing the midpoint update for step 9, then moving into step 10 at t=0.9, recomputing velocity magnitude, drag accelerations, and the midpoint estimates for vx and vz.

Continuing the midpoint integration into step 11, I update drag forces with the new velocity, then advance position and velocity to t=1.1, getting x≈3.374, z≈3.658, vx≈2.935, vz≈-2.268, before starting step 12's velocity magnitude calculation.

Continuing the drag simulation into step 13 at t=1.2, I'm computing velocity magnitude and the resulting drag-adjusted accelerations, then applying the midpoint update to refine vx and vz further.

Checking the target height of z=3.05, I find it falls between t=1.2 (z=3.38) and t=1.3 (z=3.01), so I interpolate the crossing fraction and get x≈3.927, which lands about 0.073 m short of the target—still within the acceptable window, though I note the steep descent angle matters for the approach.

To correct that shortfall, I estimate how sensitive the landing x-position is to small changes in launch speed, working through the time-to-crossing derivative and combining it with the horizontal/vertical velocity relationship to get a rough dx/dv0 ≈ 1.4.

That tells me I need v0 ≈ 9.65 m/s to hit the target, so I compute the resulting horizontal and vertical velocity components. Then I pause to sanity-check this whole approach against the original data's apex height and angle, since the early anomaly in the dataset made me want to verify my calibration independently.

I check whether drag on the vertical component is amplified near apex by the horizontal speed contribution, then try cross-checking k using the observed horizontal velocity decay near apex instead. I also look at the late descent velocities to estimate acceleration directly from consecutive data points.

Solving for k from that acceleration difference gives a much larger value than before, around 0.04, which is inconsistent with the earlier estimate—likely because position rounding to three decimals makes second differences noisy, with error bars on the order of ±0.8 m/s². I decide to use wider time intervals to reduce that noise instead.

Continuing the ascent calc: drag deceleration comes out to about 0.86, and averaging v·vz across the velocity range gives roughly 36.9, so k ≈ 0.0233, consistent with the earlier descent estimate around 0.02-0.024.

I'm also puzzling over the discrepancy in the first 0.05s interval—observed x and z positions fall short of what the launch velocity predicts, losing about 0.006 in x and 0.02 in z. This makes me think about whether the ball's initial contact with the floor, using MuJoCo's soft constraint solver with reference acceleration terms, is absorbing some of that early momentum.

Checking the drag model at t=0.1 with k=0.023 against observed values, the predicted x and z both come up short by similar amounts to the losses seen at t=0.05, suggesting a consistent one-time offset introduced early on rather than an error that grows over time.

Comparing interval velocities from 0.05 to 0.10, both observed and modeled x- and z-velocities match well, confirming the discrepancy is purely positional, confined to the first interval, and doesn't propagate. I'm now considering whether increasing k from 0.02 to 0.023 shortens the trajectory enough to matter at the crossing point.

Testing the no-drag case for comparison: solving for time to reach z=3.05 gives t≈1.418s and x≈4.654m, versus 3.927m with k=0.02, so drag costs about 0.727m of range. Scaling that effect to k=0.023 suggests an extra 0.109m reduction, meaning I'd need roughly 0.18m more adjustment than the 0.073m I'd estimated — the numbers aren't quite reconciling yet.

I think a cleaner approach is to calibrate k directly from the original trajectory rather than guessing, perhaps using the apex height (observed max z around 5.011 at t=1.00, adjusted for the initial offset) or the decay of vx over known time intervals to pin down the true drag coefficient.

Continuing to sum segment lengths across each time interval to build up the total path length.

I'm continuing to compute values out to 1.50 and running a cumulative sum of these terms, tallying the running total step by step to track where it's converging.

Dividing to get k gives roughly 0.0217, though I want to sanity-check this since rounding the vx values to three decimals introduces some uncertainty in the ratio used for the log calculation, which propagates to an error of about ±0.001 in k. I should try a more robust estimate using the early vx span from 0.05 to 0.35 instead.

Assuming purely quadratic drag per MuJoCo's ellipsoid model—blunt drag scaling with v², with slender drag and Kutta lift vanishing for a sphere—k≈0.022 seems right. Since the sphere starts with zero angular velocity and drag on a sphere produces no torque or Magnus effect, I can treat this as a simple translational drag problem and proceed with k≈0.022 to check against my earlier estimate.

Scaling the drag effect to k=0.022 shifts the crossing point to around x≈3.834, accounting for the small initial offset anomaly that nudges things further. To hit the target I'd need roughly dv0≈0.118 more speed, though drag likely dampens that sensitivity somewhat—better to just rerun the simulation directly with k=0.022 and v0=9.72 for an accurate answer.

Running the midpoint RK2 integration step by step with these new velocity components, computing drag force and acceleration at each timestep...

Continuing the RK2 integration for step 2, computing drag coefficients and updating velocity and position, then moving into step 3's midpoint calculations.

Continuing the RK4 integration into step 4, updating position to about (1.28, 2.87) with velocity around (3.11, 4.74) as drag decelerates the motion, then moving into step 5's velocity magnitude calculation.

Continuing the numerical integration, I get updated position x=1.89661, z=3.61439 with velocities vx=3.04394, vz=2.69508 after this step, moving on to step 7.

Continuing the numerical integration for step 8, computing velocity magnitude, drag coefficient, and accelerations, then using a midpoint method to update position and velocity values for x and z.

Continuing the numerical integration for step 10, computing velocity, drag coefficient, and acceleration at the midpoint, then updating position and velocity values for the next iteration.

Continuing the midpoint integration into step 12, computing updated velocities and drag coefficients, then advancing position estimates for x and z.

Continuing to t=1.3, I find the trajectory crosses z=3.05 with x landing around 3.97-4.00. Factoring in the small initial offset anomaly shifts the crossing to about 3.98, roughly 2cm short of center but well within acceptable margin, so a tiny v0 adjustment could fine-tune it if needed.

Now I'm checking clearance against the front rim tube. With a 55° descent angle, I need the horizontal distance between the ball's path and the rim's inner edge (at x≈3.7634) to produce enough perpendicular clearance—at least 0.1274—accounting for the tube radius, which sets a minimum threshold on where the trajectory's crossing point must be.

Checking the bracket and backboard clearance, the distance from ball center to the bracket box stays safely above the minimum needed, and the ball clears the backboard bottom edge as it continues past x=4.0 while still descending, confirming the trajectory stays clear of these structures.

Wait, the support structure actually has a pole at x 5.1-5.3 that the ball would hit around z≈1.1 — but that's fine since hitting the pole isn't "landing," it'll just bounce and eventually land on the floor after already passing through the hoop. That satisfies the goal, so I'll go with v0=9.73 at 70° and compute the velocity components.

So vx≈3.3279, vz≈9.1432, giving qvel="3.3279 0 9.1432 0 0 0". Checking sensitivity, a 0.01 change in v0 shifts x by about 0.0135, which keeps me within tolerance even accounting for the anomaly.

