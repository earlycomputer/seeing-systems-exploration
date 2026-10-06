The ball starts resting on the floor at x = 0 and is launched by a keyframe velocity of (2.865, 0, 8.947) m/s. Under default gravity this puts its peak at 4.2 m. It comes down through the rim center (4, 0, 3.05) about 1.40 s after launch, travelling at roughly 59° below horizontal. Rolling friction then brings it to rest on the floor beyond the hoop.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="12 12 0.1" rgba="0.75 0.6 0.4 1"/>

    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005952 0.005952 0.005952"/>
      <geom name="ball" type="sphere" size="0.12" condim="6" friction="0.8 0.02 0.04" rgba="0.9 0.45 0.1 1"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim00" type="capsule" size="0.01" fromto="0.2386 0 0 0.22044 0.09131 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim01" type="capsule" size="0.01" fromto="0.22044 0.09131 0 0.16872 0.16872 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim02" type="capsule" size="0.01" fromto="0.16872 0.16872 0 0.09131 0.22044 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim03" type="capsule" size="0.01" fromto="0.09131 0.22044 0 0 0.2386 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim04" type="capsule" size="0.01" fromto="0 0.2386 0 -0.09131 0.22044 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim05" type="capsule" size="0.01" fromto="-0.09131 0.22044 0 -0.16872 0.16872 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim06" type="capsule" size="0.01" fromto="-0.16872 0.16872 0 -0.22044 0.09131 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim07" type="capsule" size="0.01" fromto="-0.22044 0.09131 0 -0.2386 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim08" type="capsule" size="0.01" fromto="-0.2386 0 0 -0.22044 -0.09131 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim09" type="capsule" size="0.01" fromto="-0.22044 -0.09131 0 -0.16872 -0.16872 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim10" type="capsule" size="0.01" fromto="-0.16872 -0.16872 0 -0.09131 -0.22044 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim11" type="capsule" size="0.01" fromto="-0.09131 -0.22044 0 0 -0.2386 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim12" type="capsule" size="0.01" fromto="0 -0.2386 0 0.09131 -0.22044 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim13" type="capsule" size="0.01" fromto="0.09131 -0.22044 0 0.16872 -0.16872 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim14" type="capsule" size="0.01" fromto="0.16872 -0.16872 0 0.22044 -0.09131 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim15" type="capsule" size="0.01" fromto="0.22044 -0.09131 0 0.2386 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="bracket" type="box" pos="0.3093 0 0" size="0.0707 0.03 0.01" rgba="0.9 0.2 0.05 1"/>
      <geom name="backboard" type="box" pos="0.405 0 0.375" size="0.025 0.9 0.525" rgba="0.95 0.95 0.95 0.6"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="2.865 0 8.947 0 0 0"/>
  </keyframe>
</mujoco>
```

Geometry and clearances:
- **Ball:** regulation size, radius 0.12 m and 0.62 kg. It is modelled as a hollow shell, with I = ⅔mr².
- **Rim:** a ring of 16 capsules with an inner diameter of 0.457 m. The backboard face is 0.151 m behind the rim's inner edge, and the board's bottom edge is 0.15 m below the rim.
- **Clearance at the rim:** at the ball's 59° descent, its center passes about 0.196 m from the near and far rim edges. That leaves about 6.6 cm of clearance against the ball radius plus the rim tube.
- **Clearance past the rim:** the ball also misses the backboard's bottom edge (about 0.25 m from its center line) and the bracket.

How the ball settles:
- **Landing:** it hits the floor about 1.2 m past the hoop, near x ≈ 5.2. Default contacts are critically damped, so it doesn't bounce back toward the rim.
- **Stopping:** the ball's contacts use `condim="6"`, and its rolling-friction coefficient is 0.02. With rolling decelerating it at about 1 m/s², I estimate it stops within about 2 s of landing, near x ≈ 7. I haven't run the simulation to confirm this.
- **Simplifications:** the rolling friction is higher than a real basketball's, so the ball comes to rest within the 6 s run. There is no net, and no support pole holding up the backboard.

---
thinking (summarized):

I'm working out the physical dimensions for a basketball shot simulation - standard ball size, hoop height of 3.05m, rim diameter, and setting up a launch trajectory from the floor to arc through the hoop roughly 4 meters away.

With an apex of 4.2m, I calculate the initial vertical velocity needed using kinematics (~8.95 m/s), giving a time to apex of about 0.91s, then a descent phase of 0.48s to reach rim height, yielding a total flight time near 1.4s and a horizontal velocity of about 2.87 m/s. This produces a steep ~59° entry angle through the rim, which should clear the torus-shaped hoop geometry with reasonable margin given the rim's tube radius and inner clearance.

After landing, the ball would keep rolling indefinitely with no friction to stop it, so I need some way to decelerate it within the time limit—maybe by adding rolling friction via contact parameters like condim 6 and a friction coefficient, estimating that a mu_roll around 0.02 could provide enough deceleration relative to gravity and the ball's radius to bring it to rest in time.

After the ball passes through, checking whether it would bounce back up into the rim from below — but with MuJoCo's default contact damping being nearly critically damped, bounces should be minimal, and the ball's trajectory carries it past the rim's x-extent anyway, so no collision risk there.

Now I want to verify the ball clears the rim on its way up too, before reaching the apex. Tracing the ball's position near the front edge of the rim at x≈3.77, computing the time and height at that point, and comparing the ball's bottom surface against the rim height to confirm there's clearance — then checking the exact distance from the ball center to the nearest rim point to make sure it exceeds the ball's radius.

Now I'm checking whether a backboard placed near x=4.38 would actually intersect the ball's path after it passes through the rim, computing the ball's position at that x-coordinate and comparing against the board's bottom edge height to see if there's a collision.

I'll skip the pole since it would make the trajectory too messy and unpredictable, keeping the hoop body fixed without that extra support. For the landing physics, I'm working out how the ball's forward velocity converts to rolling motion via friction during impact, then applying rolling resistance deceleration using the rolling friction coefficient to figure out how far it travels before stopping.

With μr=0.05, deceleration comes to about 2.92 m/s², bringing the ball to rest within roughly 0.7 seconds and 0.72 meters, settling by around 2.6 seconds total. I need to double check how MuJoCo handles near-zero velocity friction constraints and condim settings for the ball-floor contact, making sure rolling friction only applies during actual contact and doesn't interfere with the rim pass-through. I'm noting that μr=0.05 is higher than realistic values but acceptable for getting the ball to rest convincingly.

Actually 0.05 might be too aggressive causing unrealistic quick stopping, while fully realistic values would have the ball rolling for 6+ seconds — I'll settle on a moderate 0.03-0.04 range, giving a stop time around 1.17s and travel distance of about 1.2m, landing the ball near x=6.5, which seems reasonable. I also want to enlarge the floor plane size for visual clarity, and I should verify the solref/timeconst settings handle the impact velocity without excessive penetration.

With a vertical impact speed near 9 m/s and timeconst 0.02, penetration should stay to just a few centimeters, which is acceptable without adding bounce complexity — a critically damped contact avoids rebound, which keeps the ball moving forward away from the hoop as intended. I'm now setting the keyframe initial position at z=0.12 resting on the floor with qvel roughly 2.865 in x and 8.947 in z, and refining these velocity components more precisely.

Computing vz0 gives about 8.9471, with fall time t1≈0.912s and rise time t2≈0.484s, so total flight time T≈1.396s and vx≈2.865. I'm checking whether starting the ball exactly at floor contact with zero penetration might trigger a spurious unilateral contact force, but since the velocity is separating, the solver shouldn't apply any impulse — so z=0.12 should be safe, though I could nudge it slightly if needed.

Now I'm working out the hoop's rim geometry using 16 capsule segments forming a ring, computing the tube center radius (0.2386) and the chord half-length per segment, then starting to compute the angular coordinates for each capsule's endpoints around the ring.

For the backboard, I'm positioning it in the hoop's local frame: box center placed behind the rim with a half-size of roughly 0.025 x 0.9 x 0.525, and checking the vertical center so the board bottom aligns at the correct world height of 2.9, then verifying the face distance from the rim.

I'm also checking a bracket connecting rim to board, computing its perpendicular distance from the ball's path to ensure clearance, naming it distinctly so it isn't confused with rim parts, and deciding to skip adding a net mesh for simplicity. For the ball's physical properties, I'm considering setting an explicit diagonal inertia reflecting a hollow shell (2/3 m r²) rather than the default solid-sphere inertia, since a basketball is hollow.

I'm then working out rolling friction dynamics using this inertia value, confirming the deceleration rate from rolling friction, and setting the inertial element directly so the geom's mass doesn't override it. I'm also reasoning through contact friction parameters between the ball and floor, noting that MuJoCo takes the max across combined friction coefficients and that condim needs to be set high enough (6) to capture torsional and rolling friction during impact.

