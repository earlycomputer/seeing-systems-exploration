**What I see:** The ball now rises in a lower arc that peaks at about 3.5 m, around x ≈ 2.4–2.6 m. It comes down toward the hoop but is still descending in front of it. It does not travel through to x = 4 m. Instead, the descending copies drop almost vertically at about x ≈ 3.0–3.3 m and land there, short of the hoop. That abrupt near-vertical drop just in front of the rim looks like a hit on the front of the rim followed by a bounce back. In plan, all copies stay on y ≈ 0, so there is still no sideways error.

**Why it fell short:** I re-fitted the air drag to this shot. An effective drag rate of about 0.2 /s reproduces the observed peak of about 3.5 m. With that drag, the ball centre reaches rim height (descending) at only x ≈ 3.5 m. That is about 0.5 m short of the rim centre and makes it clip the front rim at x ≈ 3.76 m.

My earlier correction raised vx by only about 5%, which was not enough. The vz I gave also set a peak that drag pulls down too early in x. The first shot in this scene also landed short of its no-drag range, which is consistent with this drag level.

**New launch:** I re-solved the shot with that drag for a 1.15 s flight from the rest position to the rim centre (4, 3.05). This gives vx ≈ 3.89 and vz ≈ 8.71:
- **Peak:** about 3.57 m.
- **Entry:** descending at about 46°.
- **Rim clearance:** the path passes about 0.17 m from both the front and back rim tubes. The ball radius plus the tube radius is 0.127 m, so the ball clears them.

```json
{"description": "The ball rises to about 3.5 m near x≈2.5 m, then comes down in front of the hoop. It appears to clip the front of the rim and drops nearly vertically, landing around x≈3.0–3.3 m, short of the hoop. The plan view shows it on y≈0 throughout.", "goes_in": false, "miss": "short", "evidence": "both"}
```

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
    <key name="shot" qvel="3.89 0 8.71 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from "3.52 0 8.58 0 0 0" to "3.89 0 8.71 0 0 0".
       The previous launch peaked near 3.5 m and fell short: its centre reached rim height around x = 3.5 m, so it clipped the front rim and dropped in front of the hoop.
       I fitted an effective air-drag rate of about 0.2 /s to that readback; this matches its observed peak.
       With that drag, I re-solved for a 1.15 s flight from the rest position (0, 0.1194) to the rim centre (4, 3.05).
       The result peaks near 3.57 m and enters descending at about 46 degrees.
       It passes about 0.17 m from the front and back rim tubes, which is more than the ball radius plus tube radius of 0.127 m.
       The drag fit comes from reading the picture, so a residual error of roughly 0.1 m at the rim is possible. -->
</mujoco>
```

---
thinking (summarized):

I'm mapping out the trajectory of the arc as it rises and falls, trying to pin down where the balls land relative to the hoop position and converting between the image's pixel coordinates and real-world meters.

This shows the descent is much steeper than expected, landing around x≈3.1-3.2 m instead of the no-drag estimate of 4.22 m, which tells me air resistance is playing a significant role and I need to factor in a noticeable drag coefficient.

Solving numerically, c≈0.73/s fits the drag decay, implying an effective k≈0.12 — about 6x higher than my rough estimate, so the actual blunt-body drag model must be stronger than anticipated. I should just treat this empirically rather than derive it theoretically, and start counting the dot spacing in the picture to check timing against the arc shape.

Now I'm working out a new trajectory using the linear-drag approximation (since the quadratic model is messy), setting up the position equations for x and z with a decay constant c, and testing c=0.7 for a 1.2-second flight time to see if it matches the target arc.

Continuing the trajectory math, the descent angle looks steep (around 59°) and the apex height comes out to about 3.81 m, which seems reasonable. But I'm worried the result is too sensitive to my estimate of c, so I want to try calibrating the quadratic drag coefficient k against the actual observed shot data instead — looking at shot 2's initial velocity and its observed peak height and landing distance to back out a better k value numerically.

Trying a crude Euler simulation with k=0.1 and small timesteps to step through velocity and position, computing drag-adjusted accelerations at each stage and using midpoint averaging to improve accuracy.

Continuing the integration, I get x2=0.647, z2=1.509 after step 2, then step 3 gives vx3=2.856, vz3=4.284 with x3=0.940, z3=1.997, and step 4 yields vx4=2.728, vz4=3.133 with x4=1.218, z4=2.365. I'm now starting step 5's velocity calculation.

Step7 finishes with vx7=2.486, vz7=0.0345, giving peak around x7=1.996, z7=2.828 — but that's lower than the observed peak of roughly 3.5 at x~2.3, suggesting k=0.1 is too large. I should double-check my pixel reading: estimating the top ball's position in the 128px image, the band spans z -0.2 to 5.35, giving a scale of about 16.41 px per unit, so a pixel y of ~30 corresponds to z≈3.52, with the rim at z≈3.05 around pixel 2.3.

Looking more carefully, the rim appears near y~37, x~70-78px, while peak balls sit slightly above at y~30, consistent with peak height ≈3.5 at x≈2.35m. The landing ball near the bottom darkens around x~60px, y~85, giving z≈0.12 and x≈2.96, so the trajectory descends nearly vertically around x≈2.9-3.1m.

Comparing to the no-drag case (peak 3.87 at x=3.08), the observed peak is lower and shifted left, so I'm trying a smaller drag coefficient, k=0.04, to see if it better matches the 0.35m drop and leftward shift in peak position.

I'm testing a linear drag model, solving for the time at peak height and then plugging back in to estimate the horizontal distance to compare against the observed peak at x=2.35, z=3.52, and landing near x=3.0.

The height for c≈0.2 matches better but the x-value doesn't quite fit the observed horizontal distance, so I'm suspecting measurement uncertainty. I'm now solving for the landing time by iterating toward where z(t)=0, narrowing in between t=1.6 and 1.68.

Getting x≈5.01m at landing, but that's way off from the observed ~3.0m, so something's wrong with my pixel reading of the trajectory. Let me re-examine the ball positions in the image more carefully — the descending portion looks like it drops almost vertically around x≈60px (about 2.96m), while the ascending portion has balls spaced roughly 5-6px apart horizontally, suggesting about 0.33m per 0.1s interval.

That abrupt vertical drop near x≈60-63px makes me suspect the ball actually struck something there rather than following free-fall trajectory — possibly the front of the rim, which I'd placed around x≈3.6-3.8m. If the ball hit the rim front and bounced back, that would explain the sudden change in its path near that location.

Reconsidering with a lower drag coefficient around c≈0.15-0.2 feels more consistent — a slightly short shot hitting the rim and bouncing back rather than a clean trajectory. I'm cross-checking this against the earlier no-drag shot, which overshot the observed landing point, and trying to solve for when z reaches about 3.05m on the way down using this damping value.

My calculations put the ball's horizontal position at roughly x≈3.49 when it crosses rim height, about half a meter short of center — meaning the trajectory actually clips the front rim tube rather than reaching it cleanly, which matches the short bounce-back behavior. Now I'm using this same drag coefficient to work out what launch parameters would land the ball cleanly at x=4, z=3.05 around t=1.15s.

Solving for the initial velocities gives vx0≈3.89 and vz0≈8.71, and checking the descending velocity at impact shows the ball comes down at about 45.6° — a reasonable shot angle. I also computed the apex of this trajectory, landing around z≈3.57 near t≈0.82s, which seems like a sensible peak height for this shot.

Checking rim clearance confirms the trajectory passes safely over both the front and back rim with margin of about 0.168 vs the required 0.127, so the shot geometry checks out on both sides.

Given similar shot speed to the prior attempt (9.53 vs 9.27), the c=0.2 drag model remains a good match since it correctly predicted the observed peak of 3.5. I'll go with qvel="3.89 0 8.71 0 0 0".

