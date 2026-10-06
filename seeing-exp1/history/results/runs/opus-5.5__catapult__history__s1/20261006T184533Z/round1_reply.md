The ball is launched but lands short of the bucket. It hits the floor at about x ≈ 1.2 m, bounces into the outside of the bucket's near wall and comes to rest outside the bucket at x = 1.47 m.

**What happens in the run**
- The spring swings the arm from 0° to its 55° stop in 0.53 s. It arrives at 188°/s.
- The ball leaves the cup at about (−0.46, 1.22) m with a velocity of about (2.63, 1.08) m/s. That is roughly 2.8 m/s at about 22° above horizontal.
- The ball peaks at 1.28 m at x = −0.17 m. It first touches the floor at 1.14 s, around x ≈ 1.2 m.
- It bounces against the outside of `bucket_near` and stops outside the bucket.

**Two problems**
- **The throw is too weak.** To reach the bucket floor at x ≈ 2.08 m from that release point and angle, the ball needs about 4.1 m/s at release. It got about 2.84 m/s. At that speed it also clears the 0.4 m near wall with about 0.13 m to spare.
- **The bucket is in the wrong place.** Its centre is at x = 2.0 m, which is 2.92 m from the ball's start, not 3 m.

**Fixes (estimated, not re-run)**
- **Spring stiffness 2.0 → 2.8 N·m/rad.** The arm and its load have about 0.26 kg·m² of inertia. Lifting them to 55° costs about 2.5 J. With stiffness 2.8 the spring stores about 5.7 J over the stroke, leaving about 3 J of kinetic energy. That gives an arm speed of about 4.7 rad/s at the stop and a ball speed of about 4.1 m/s.
- **Bucket centre moved to x = 2.08 m.** That puts it exactly 3.00 m from the ball's start at x = −0.92 m.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.8" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The spring arm swings up to its 55° stop and releases the ball at about 2.8 m/s, 22° above horizontal, from about (-0.46, 1.22) m. The ball peaks at 1.28 m, lands on the floor near x = 1.2 m, bounces against the outside of the bucket's near wall and comes to rest outside the bucket at x = 1.47 m.", "works": false, "problem": "The throw is too weak, so the ball lands short and stays outside the bucket, and the bucket's centre is 2.92 m from the ball's start instead of 3 m."}
```

---
thinking (summarized):

The ball falls short of the bucket, landing around x~1.2 instead of reaching it, so I need to adjust the distance—the bucket should be at x=2.08 to make the total span exactly 3 units from the ball's start at -0.92. I'm recalculating the release velocity components, around vx 2.63 and vz 1.7 at release time ~0.53s, to fix the trajectory so it actually lands in the bucket.

I need more horizontal speed—at current velocity the ball only travels to about x=1.14, far short of the bucket at 2.08, and it must also clear the near wall at x=1.68 with enough height margin above 0.4. I'm working out that with release velocity around (2.6, 1.5) at roughly 30° launch angle from around x=-0.48, I need the horizontal distance to cover about 2.56 units while dropping from height 1.22 to 0.08, so I'm solving the projectile equations to find what speed increase is needed to hit that target.

Checking the clearance height at that near wall point gives 0.606m against the 0.46m threshold, a comfortable 0.15m margin. Now I'm second-guessing whether release angle and speed actually match the arm's physical dynamics — computing the cup's tangential velocity from the arm's angular speed at the 55° stop gives about 3.02 m/s, which aligns with my earlier estimate, so I'm working out the exact release direction by tracking how the arm's rotation about the y-axis transforms the cup's position.

Working through the velocity direction at 55°, I get roughly 35° elevation, close enough to the ~30° I observed earlier. Now I need to verify the angular velocity by computing the spring's energy contribution between 0° and 55° using the torsional stiffness and reference angle, getting about 4.1 J, and I'm starting to account for gravitational losses from the arm and cup masses as they swing up.

Computing potential energy losses from the beam, cup, and ball as they rise, I get about 2.54 J total, leaving roughly 1.56 J of kinetic energy. Working out the moment of inertia contributions from each component gives about 0.263 kg·m², so solving for ω gives 3.45 rad/s versus my observed 3.28 — a reasonably good match accounting for damping. Now I need to find what ω would be required to hit the target value of 4.43 rad/s instead.

That gives a landing window of roughly ±0.33 around 2.08, and range sensitivity is manageable at this speed. I should also check that the ball releases cleanly and that the slight overshoot at the upper stop doesn't cause issues — the critically-damped contact model means minimal bounce, so with a ~4 m/s vertical and ~3.5 m/s horizontal landing velocity, the ball should settle and roll toward the far wall of the bucket rather than bouncing out.

Moving the bucket to x=2.08 puts its center exactly 3.00 from the ball's start position, which should work well given the expected forward roll after landing. I'm also reconsidering the release angle — estimating from the apex timing (around 0.64s) back to release (~0.53s), the vertical velocity at release comes out to roughly 1.08 m/s, so I may want to nudge stiffness slightly to better center the landing.

Recomputing with vx=2.63 and a shallower 22° angle than I first assumed (speed ~2.84), I trace back the release position to about (-0.46, 1.22). Solving the trajectory equations for a target at x=2.08 gives a required launch speed of about v=4.12 m/s at this angle.

With the ball-to-arm speed ratio around 0.94, I derive an angular velocity of roughly 4.76 rad/s, giving a kinetic energy of about 2.98 J, which translates to a needed spring stiffness near 2.77 after accounting for height and friction losses. I'm now checking wall clearance by computing the ball's height at the wall's x-position using these values to make sure it doesn't clip.

Clearance comes out to 0.59, comfortably above the 0.46 threshold, so I settle on a stiffness of 2.8 as a safe working value, acknowledging the 22° angle has a moderate effect on sensitivity.

