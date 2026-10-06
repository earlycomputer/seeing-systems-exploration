**What happened in the run.** The arm swung up and hit its 45° stop at 0.13 s, turning at 447°/s (7.8 rad/s), which is the speed I designed for. The ball left with almost exactly the horizontal speed I predicted, 3.60 m/s. Its vertical speed was only about 0.6 m/s instead of about 3.0 m/s. So it flew low, landed on the floor near x ≈ 1.4 m at 0.61 s, rolled into the bucket's near wall, bounced back, and rolled to a stop outside the bucket at x = 1.62 m.

**Why the throw went low.** The missing velocity is purely vertical, about 2.4 m/s. Split along the arm, it is two equal parts: a push inward, and a drag against the ball's upward slide. Equal normal and friction pushes (the friction coefficient is 1) point to the outer cup wall. During the swing that wall was pressed hard against the ball to keep it moving in a circle. When the arm stopped, the ball slid up along the wall face, and friction there ate most of its upward speed.

**The fix.** I made every cup geom frictionless (`condim="1"`) and gave them `priority="1"`, so that setting governs their contacts with the ball. I also stiffened those contacts, so the ball sinks less into the wall during the swing. The ball can now slide off the wall freely. The floor and bucket keep their normal friction and rolling friction, so the ball still settles in the bucket. Nothing else changed: the drive speed of 7.84 rad/s already gave the right arm speed.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="0 0.4 -1"/>
    <geom name="floor" type="plane" size="6 3 0.1" pos="0 0 0"/>
    <body name="catapult_base" pos="0 0 0">
      <geom name="catapult_baseplate" type="box" size="0.25 0.18 0.01" pos="0 0 0.01"/>
      <geom name="catapult_post_left" type="box" size="0.02 0.02 0.19" pos="0 0.12 0.21"/>
      <geom name="catapult_post_right" type="box" size="0.02 0.02 0.19" pos="0 -0.12 0.21"/>
      <geom name="catapult_axle_left" type="cylinder" size="0.012 0.024" pos="0 0.076 0.4" euler="90 0 0"/>
      <geom name="catapult_axle_right" type="cylinder" size="0.012 0.024" pos="0 -0.076 0.4" euler="90 0 0"/>
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" limited="true" solreflimit="0.005 1" damping="0"/>
        <geom name="catapult_beam" type="box" size="0.38 0.05 0.01" pos="-0.28 0 0" mass="0.2" priority="1" condim="1" solref="0.005 1"/>
        <geom name="catapult_cup_outer" type="box" size="0.01 0.055 0.03" pos="-0.651 0 0.04" mass="0.03" priority="1" condim="1" solref="0.005 1"/>
        <geom name="catapult_cup_inner" type="box" size="0.01 0.055 0.015" pos="-0.55 0 0.025" mass="0.02" priority="1" condim="1" solref="0.005 1"/>
        <geom name="catapult_cup_side_left" type="box" size="0.04 0.005 0.02" pos="-0.6 0.05 0.03" mass="0.015" priority="1" condim="1" solref="0.005 1"/>
        <geom name="catapult_cup_side_right" type="box" size="0.04 0.005 0.02" pos="-0.6 -0.05 0.03" mass="0.015" priority="1" condim="1" solref="0.005 1"/>
      </body>
    </body>
    <body name="ball" pos="-0.6 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.005 0.001"/>
    </body>
    <body name="bucket" pos="2.4 0 0">
      <geom name="bucket_floor" type="box" size="0.32 0.32 0.01" pos="0 0 0.01"/>
      <geom name="bucket_wall_far" type="box" size="0.01 0.32 0.125" pos="0.31 0 0.135"/>
      <geom name="bucket_wall_near" type="box" size="0.01 0.32 0.125" pos="-0.31 0 0.135"/>
      <geom name="bucket_wall_left" type="box" size="0.3 0.01 0.125" pos="0 0.31 0.135"/>
      <geom name="bucket_wall_right" type="box" size="0.3 0.01 0.125" pos="0 -0.31 0.135"/>
    </body>
  </worldbody>
  <actuator>
    <velocity name="catapult_drive" joint="catapult_hinge" kv="30" forcelimited="true" forcerange="-15 15"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 -0.6 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="7.84"/>
  </keyframe>
</mujoco>
```

```expect
catapult_arm reaches its upper stop
ball touches bucket_floor
ball comes to rest in bucket
```

```json
{"what_happens": "The arm swings to its 45° stop at 0.13 s at the intended 7.8 rad/s and the ball leaves with the right horizontal speed (3.6 m/s) but only about 0.6 m/s upward instead of about 3 m/s. It flies low, lands on the floor near x = 1.4 m, rolls into the outside of the bucket's near wall, bounces back and stops on the floor at x = 1.62 m, outside the bucket.", "works": false, "problem": "Friction between the ball and the outer cup wall at release strips most of the ball's upward velocity, so the throw falls about 1 m short of the bucket."}
```

---
thinking (summarized):

The ball seems to land short, touching the floor around x≈1.4 based on the trajectory I'm tracking. The release vx of 3.60 matches my prediction of 3.61, but vz at release appears much smaller than I initially assumed—working backward from the peak at 0.19s with z=0.89, I estimate vz near 0.59 at the moment of release.

This is way off from the predicted 3.06, meaning vertical velocity is being lost somewhere. The arm's angular velocity of 447°/s checks out, and vx matches, but the expected perpendicular velocity (3.6, 3.05) doesn't match what the ball actually shows (3.6, 0.6)—there's a missing component of about -2.45 in the vertical direction. I'm wondering if the ball wasn't rigidly moving with the arm the whole time, and may have been rolling against the outer cup wall or floor during the acceleration phase before release, which could explain the discrepancy.

Checking the position consistency: working backward from x=0.04 at 0.25s with vx=3.6 gives x≈-0.39 at release, which lines up. The z-position also matches the predicted trajectory at release (~0.86-0.87). So the release position is right, but the vertical velocity is suspiciously low. I'm trying to figure out why the arm's deceleration would kill the ball's velocity component away from the wall—normally the ball should be moving inward along the arm direction, away from the outer wall, so nothing should be stopping that motion. Unless ball spin is somehow involved in reducing that velocity component.

The key realization is the ball's spin about the y-axis persists even as the arm stops rotating. Computing how spin interacts with the contact point at the outer wall, the spin creates a surface velocity equal to ωr along the outward normal direction relative to the now-stationary wall. This means friction at the contact point from this spin-induced slip could generate a force that affects the ball's velocity component in that direction.

But there's a complication: the arm overshoots its stop, moves back 1.2° then bounces with -76°/s, so the outer wall's motion relative to the ball flips direction too during that bounce, which changes the contact dynamics unpredictably. I'm also considering whether the beam contact point experiences similar spin-induced sliding, and whether rolling friction at the beam contact matters during deceleration, though that depends on whether there's still normal force there once the arm starts decelerating away from the ball.

Trying to decompose the velocity loss into components along n and e directions, I get numbers that don't cleanly match a simple friction story — the ball seems to lose speed in n but also shift inward along e, which is confusing given the arm's outward motion. Since isolating the exact mechanism is getting complicated, I think the better path is to just apply a direct correction: the release vz is consistently low by about 2.45 relative to prediction while vx checks out, so I should account for that discrepancy empirically rather than fully resolve the underlying physics.

When the arm hits its limit, the soft stop decelerates it over some milliseconds, meaning the wall itself is decelerating tangentially during that window, which could be contributing to the unexpected force spike rather than the steady-state centripetal effect I was assuming.

I'm wondering if the beam separated from the ball once it decelerated, with the ball continuing on its own path rather than staying in contact. The large velocity deficit makes me suspect the ball picked up spin or rolled differently than expected, or that the joint's soft limit constraint is behaving unexpectedly rather than a clean rigid contact.

I'm struggling to pin down the exact friction/normal-force mechanism causing the velocity loss, so I'll take a pragmatic route instead: lower the friction coefficient on the cup geoms to near zero and switch the ball's condim from 6 to 3, since rolling friction torque under a strong normal force could be the thing killing spin and velocity.

Working through the contact point velocity algebra, the tangential slip component stays small while the normal component grows, meaning the ball separates cleanly from the beam rather than sliding. So with the ball rigidly attached during rotation nothing problematic happens — the issue must instead arise from contact forces during the arm's deceleration phase, since the ball tends to continue forward relative to the decelerating beam, causing separation.

Now I'm checking the numbers: the release velocity of 447°/s converts to 7.80 rad/s, giving vz=0.6, vx=3.6, magnitude 3.65 at 9.5°, versus a predicted magnitude of 4.73. The vx match seems suspicious — I'm wondering if this is coincidence or if it points to the ball not rotating purely rigidly, perhaps sliding outward along the outer wall instead.

I'm considering whether the ball left the beam earlier than 0.13s due to tangential forces or gravity components along the normal versus centripetal directions, but that would produce a steeper, not flatter, trajectory, so that doesn't fit. I also rule out inward/outward sliding and confirm the cup side walls (±0.045) comfortably clear the 0.04 ball radius. Back-calculating from the 0.25s state (z=0.88, vz=-0.59) and the 0.19s peak (z=0.89), I'm working out that the release vz around t=0.13-0.14 should be about 0.59 from gravity deceleration.

Now I'm checking whether friction against the outer wall during arm rebound could explain the discrepancy — tracing the wall's geometry (top at local z=0.07, ball center needing to clear by about 0.06) and estimating a 13ms sliding contact period as the arm rebounds backward at roughly 1.3 rad/s, trying to work out the wall's point velocity and resulting friction force on the ball during that contact.

That friction impulse estimate only gives 0.36 m/s, far short of 2.4, so the normal force must be larger than I assumed. I wonder if the ball had rolled up against the outer wall with extra force from the arm's deceleration itself, or if its position wasn't quite at the radius I used—something about my rigid-contact assumption seems off.

Maybe I should abandon trying to predict the exact unknown loss and instead redesign to avoid it entirely, or just accept guesswork retuning. I'm recomputing the ball's position relative to the pivot at 45°, breaking it into radial and normal unit vector components.

Checking the velocity derivation, the x-component matches perfectly at 3.58 against the observed 3.60, but the z-component drops to 0.6 from an expected 3.03 — so the loss is purely vertical, roughly -2.43. That's strange because nothing in the arm's frame at that angle should produce a purely vertical impulse like that.

I'm thinking the inner wall corner might be the culprit: if the ball's local position is close to that corner (within 0.041 vs. a 0.04 threshold) and moving inward and upward, contact there could explain the vertical velocity loss, especially if the ball is being pressed against the outer wall due to centripetal effects.

Checking the actual displacement vector from corner to center dotted with the velocity vector, though, shows the ball is separating from that corner, not approaching—so that's not it. I'm now reconsidering whether the beam itself or another geometry (floor, cup_outer wall) might be the real contact responsible for the timing discrepancies I noticed earlier.

Nothing touches the ball between 0.14 and 0.19s, so the small vz at release checks out mathematically. Ruling out pivot contact and radial wall motion, I suspect residual friction on the cup geoms during the stop is dragging the ball down—so the practical fix is just zeroing out friction on those cup surfaces to get a cleaner release.

If friction were the cause, eliminating it should fix the discrepancy, but if not, something else is wrong. I'm also considering whether rolling friction could be the culprit — with soft constraints coupling relative angular velocity, the torque is bounded by μ_r*N, which seems too small to explain a 2.4 m/s loss. I'm also checking whether contact depth with the beam during the swing matters, but since tangential acceleration is zero at constant ω, that seems fine too.

I briefly consider the servo's force limit pushing on the arm, but that seems irrelevant to the ball itself. Instead, I'm trying to work out what impulse could remove only vertical momentum — setting up the equations to solve for the normal and tangential impulse components that would produce a pure -z velocity change of 0.243 Ns.

Solving gives a=b=-1.72, meaning the impulse has to come from the outer wall pushing inward (-e) combined with a friction impulse acting along -n, and with μ=1 the friction equals the normal force, saturating. So the outer wall must be delivering a large inward normal impulse plus matching friction — I'm trying to understand why the outer wall's radial normal direction would produce this given the wall's height and radius geometry.

Now I'm estimating the contact penetration depth: the ball's centripetal acceleration during the swing is roughly 36 m/s² (about 3.7g), and with MuJoCo's default soft-contact solref timeconstant of 0.02s, I'm working out the implied spring stiffness and resulting penetration depth to see if it's large enough to explain the force magnitude.

When the arm suddenly stops, I'm checking whether the stored contact spring energy releasing radially could produce the observed velocity jump—computing sqrt(a·x) for a plausible penetration depth, but getting only about 0.42 m/s, far short of the 1.72 m/s I need to explain. I'm also considering whether the arm's angular position, the beam's contact normal direction, or the ball's own spin relative to the arm's rotation could be contributing an impulse I haven't accounted for yet.

Tracking the spin contribution, I work out that the ball's rotation combined with the arm's angular velocity gives the contact point on the wall a sliding velocity—computing the cross product of spin and radius to get a component along the normal direction, then combining it with the center's velocity to find the total rigid-body velocity at the contact point just before the arm halts. This works out to roughly 5 m/s of relative sliding along the wall once the arm stops, which seems like a much more promising lead than the spring-release idea.

The fix would be making the outer wall contact frictionless so the ball slides along it unimpeded without spurious normal force coupling. On the frictionless beam, gravity's tangential component along e pulls the ball inward at angle θ, with magnitude -g sinθ relative to the pivot direction.

Checking centripetal requirement: ω²R=36 exceeds g sin45≈7, so the ball stays pressed against the outer wall even early in the swing, which is good. For implementation, I'd set cup geoms to priority 1 with condim 1 (frictionless), while the ball keeps condim 6 for floor/bucket contacts—MuJoCo's priority system means the higher-priority geom's condim and friction win. I'm also worried about soft penetration giving an unwanted inward kick (~0.4 m/s along -e), which might require stiffening the cup contacts with a tighter solref to avoid that spurious velocity change.

With frictionless walls, the predicted release velocity (3.58, 3.03 m/s at ω=7.8) matched the servo output well (3.60 vs 3.58), so the trajectory should land the ball near the bucket center at rim height. If there's still a discrepancy I'll iterate further, and I'm considering making the bucket deeper to add margin for error.

