The ball starts at rest near the top of a 20° ramp and gravity rolls it down. It leaves the ramp's lower edge just above the low near wall of a square open-top cup and drops in. The taller far and side walls catch it. Rolling friction on the ball (`condim="6"`) bleeds off its energy so it settles on the cup floor well within the 6 s.

The numbers below are hand estimates from the geometry; I have not run this file in MuJoCo.

- **Ramp roll:** the ball rolls about 0.45 m and leaves the edge at roughly 1.3–1.5 m/s, about 0.7 s after release.
- **Clearing the near wall:** the ball's centre leaves the edge at z ≈ 0.128, so its underside clears the 0.08 m near-wall top by about 2 cm.
- **Landing:** it touches down near the middle of the 0.24 m-wide cup floor.
- **Catching the bounce:** the far wall is 0.15 m tall, which gives margin if the landing bounces.
- **Coming to rest:** rolling friction should stop the ball after a few wall contacts. I expect it to be still by about 3–4 s.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 2" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="ramp_board" type="box" pos="0 0 0.176" euler="0 20 0" size="0.25 0.08 0.01" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_leg" type="box" pos="-0.2 0 0.119" size="0.01 0.06 0.119" rgba="0.5 0.3 0.15 1"/>

    <body name="cup" pos="0.38 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.005" size="0.13 0.13 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.125 0 0.04" size="0.005 0.13 0.04" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_far" type="box" pos="0.125 0 0.075" size="0.005 0.13 0.075" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.125 0.06" size="0.12 0.005 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.125 0.06" size="0.12 0.005 0.06" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.1743 0 0.282">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" condim="6" friction="1 0.005 0.003" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="-0.1743 0 0.282 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm designing a scene where a ball rolls down a ramp and settles into a cup, needing it to work reliably within 6 seconds. I'm thinking through how to build the cup itself, considering using a ring of angled boxes around the base to approximate cylindrical walls since a true hollow cylinder isn't directly available.

I'm also working out the physics so the ball doesn't roll forever inside the cup — adding rolling friction via the contact parameters so the ball's motion dissipates naturally against the cup walls and floor, estimating how the friction coefficient translates into a deceleration rate for the sphere.

Now I'm figuring out the ramp geometry: a tilted box at roughly 20° so gravity provides enough acceleration to overcome rolling resistance, sized so the ball launches off the end and arcs into the cup rather than needing the cup sunk below floor level, which isn't feasible with a flat plane.

Computing the upper end position, I find the top surface reaches z≈0.271 while the lower end sits at z=0.10 to match the cup rim height, giving zc=0.176. Since the ramp is a floating static geom with no physical support needed, I consider adding an optional support leg underneath for visual grounding, though it's not strictly necessary.

Calculating the leg's position under the ramp, confirming a height of about 0.238 with half-height 0.119 and center 0.119, and noting that since the leg and ramp are part of the same static body they won't collide with each other, so the slight overlap is harmless. Now I'm positioning the ball's starting point on the ramp's upper surface near the top, computing its world coordinates from the local offset.

Working out how far the ball rolls down the 0.45m incline and estimating its final speed using energy methods, accounting for rolling friction effects from the contact model — getting roughly 1.3-1.5 m/s depending on how much rolling resistance slows it down.

Then I'm tracking the ball's exit position and velocity components as it leaves the ramp edge, and computing the projectile fall time until it reaches the cup floor, solving the quadratic for drop time given the initial downward velocity component.

Then I'm checking clearance over the near wall of the cup: figuring out how much the ball center drops before reaching the wall's x-position, to make sure the ball's underside clears the wall top, and using that to decide where to place the near wall relative to the ramp edge.

The ramp's lower corner ends up near x=0.23, z=0.081, close to the wall edge but not colliding since it's static geometry. I'm considering enlarging the cup for safety—widening the inner region and reconsidering wall height, since raising it to 0.10 would clash with the ball's exit height, so I may need to raise the ramp instead and recompute the center height.

Checking the landing trajectory, the ball lands around x=0.38 still moving fast horizontally and could bounce off the far wall at 0.08 height since its center sits below the wall top—soft contact dynamics might let it hop or bounce unpredictably, so I should make that far wall taller, maybe 0.15, to reliably catch it.

With default solref values MuJoCo contacts are nearly critically damped so bounce should be minimal, letting rolling friction decelerate the ball between wall impacts (roughly 0.5 m/s² deceleration) until it settles within a few seconds given the cup's 0.24m width.

Bumping rolling friction to 0.003 still keeps the ramp resistance comfortably below gravity's pull on the incline, so the ball should still roll freely down. I'm now working out the cup's position, aligning the bottom plate so its center sits at x=0.38 to match the inner span from 0.26 to 0.50.

Defining the wall geometries...

Checking that the floor gap between ramp and cup never gets contacted, then working through contact friction values—ball radius 0.03 with default density gives about 0.113 kg mass, and I'm reasoning through how friction parameters combine across ramp, cup, and ball surfaces.

Estimating the rolling time from ramp to cup end (roughly 0.7s to reach it, settling by 3-4s), then computing the exact starting qpos for the ball so it sits correctly on the ramp without penetrating—working out the z-height using the ramp's slope and offset to get z ≈ 0.282, matching the body's initial position and orientation in the keyframe.

