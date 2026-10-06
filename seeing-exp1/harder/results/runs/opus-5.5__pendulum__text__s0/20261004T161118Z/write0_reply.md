The pendulum starts 25° back and is released by gravity. Its dense bob reaches the bottom of its arc just as it meets the ball, so the strike is nearly horizontal.

The ball rolls along +x toward the cup centred at x = 1 m. The cup is a U-shaped pocket with a 12 cm mouth facing the ball and a tall back wall that stops it. A small rolling friction on the ball soaks up any rebound so it stays inside.

I haven't run this. The ball speed and the rebound depend on MuJoCo's contact behaviour, so they are estimates. The ball should reach the cup within about 2 s.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="stand_post" type="box" pos="-0.061 0.15 0.28" size="0.01 0.01 0.28" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    <geom name="stand_arm" type="capsule" fromto="-0.061 0.15 0.535 -0.061 0 0.535" size="0.008" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    <body name="pendulum" pos="-0.061 0 0.535">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.465" size="0.006" density="1000" rgba="0.6 0.6 0.7 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.03" density="8000" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" condim="6" friction="0.8 0.005 0.0003" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="cup" pos="1 0 0">
      <geom name="cup_back" type="box" pos="0.11 0 0.05" size="0.01 0.12 0.05" rgba="0.2 0.7 0.3 1"/>
      <geom name="cup_left" type="box" pos="0 0.11 0.05" size="0.12 0.01 0.05" rgba="0.2 0.7 0.3 1"/>
      <geom name="cup_right" type="box" pos="0 -0.11 0.05" size="0.12 0.01 0.05" rgba="0.2 0.7 0.3 1"/>
      <geom name="cup_front_left" type="box" pos="-0.11 0.09 0.05" size="0.01 0.03 0.05" rgba="0.2 0.7 0.3 1"/>
      <geom name="cup_front_right" type="box" pos="-0.11 -0.09 0.05" size="0.01 0.03 0.05" rgba="0.2 0.7 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.4363 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics layout for the scene — placing the ball on the floor and figuring out how the cup should be positioned so the ball can realistically roll into it, since the floor is flat and can't have a sunken hole.

A better design: make the cup an open structure with a gap facing the ball so it rolls in and stops against the back wall, relying on MuJoCo's default contact damping to absorb most of the bounce. I'm weighing whether the ball might bounce back out through the gap, and considering that without rolling friction, a ball on a flat plane with condim 3 will keep rolling indefinitely unless something slows it down.

I'm deciding to skip giving the cup a base plate entirely, so it's just walls sitting on the floor — simpler and avoids the ball having to climb a lip, since any small step (even a few millimeters versus the 30mm ball radius) could still risk deflecting it rather than let it settle naturally inside.

Now I'm designing the cup itself as a static body with eight wall segments spaced around a 0.08 radius circle at 45° apart, each 0.06 tall to match the ball's diameter, leaving out the segment facing the ball's approach direction to form the entry gap. I'm calculating the gap width using the chord length formula for that segment spacing.

Actually, I'm pivoting to a simpler square U-shaped design instead: a back wall and two side walls forming a box around the cup center, with a front opening wide enough for the 0.06 ball to enter, built from basic box geoms rather than a circular arrangement.

For the pendulum strike, I'm positioning the bob so it touches the ball when hanging vertically, with pivot located above at the end of a 0.5-length rod, matching heights so impulse transfers horizontally through the ball's center, then releasing it from an angled start via keyframe qpos.

Working through the physics: at 60° release the bob reaches about 2.21 m/s at the bottom, then transfers momentum to the ball depending on mass ratio. The ball rolls roughly a meter to the back wall, and I'm checking whether the impact speed could cause bouncing given MuJoCo's default contact stiffness, which is fairly inelastic but not fully so.

Trying a gentler release angle of 30° instead gives a bob speed near 1.15 m/s, so the ball ends up moving around 1 m/s after collision and rolling (with friction converting slide to roll) over roughly a second to reach the cup. But then the back-wall bounce could send it back out through the front gap, which is a problem I need to solve — maybe by adjusting geometry so the ball settles instead of escaping.

Rather than fine-tuning friction coefficients and condim settings to tune deceleration precisely, a more robust fix is giving the cup a ramped entrance: the ball rolls up a short ramp to rim height and tips over into a walled interior it can't climb back out of, so only balls with enough speed to climb the ramp (roughly v² > (10/7)gh) make it in and stay trapped.

With a 0.15 length ramp at 0.03 height, slope is roughly 11°, leading up to the front wall where the ball would drop into the cup — falling 0.03m at 1 m/s takes about 0.08s, landing well within the 0.2m cup interior. I'm debating whether this ramp should just be part of the cup body itself, which seems fine to keep simple. I'm also second-guessing the bounce-back behavior, wondering about MuJoCo's default contact damping and whether a critically damped soft contact actually produces near-zero restitution.

That seems right: the ball shouldn't rebound much since the contact force vanishes only as penetration approaches zero, meaning it exits with just a small residual velocity rather than bouncing cleanly. But now I'm realizing the ball's topspin complicates things — if it hits the wall while spinning forward, friction at the contact point could cause it to climb rather than just stop.

Working through the cross product, with spin about the y-axis from forward rolling, the contact point's surface velocity points downward, so friction reacts upward on the ball — meaning it could ride up the wall slightly, though the 0.08 wall height should still contain it. After the near-zero bounce, the ball would likely settle near the back wall around x≈1.07, still within the cup, though I'm a little uneasy about whether the soft contact solver's damping is really enough to prevent any noticeable bounce-back.

Considering the pendulum's follow-through, after striking the ball it continues swinging through to its return arc and back to roughly -30°, by which point the ball has already moved away — so no secondary collision, but I'll add slight hinge damping to settle it faster. For masses, a 0.03 radius ball at default density gives about 0.113 kg, while making the bob heavier with a 0.04 radius sphere plus rod gives roughly 0.268 kg, which seems like a better balance for a convincing strike.

Estimating post-collision speeds: with restitution around 0.2 and the pendulum's effective mass advantage, the ball likely ends up sliding at roughly 0.8-1.2 m/s, settling into rolling around 0.6-0.9 m/s once floor friction kicks in, which should cover a 1 m distance in about 1.5 seconds — comfortably within the 6 second window.

For the collision geometry, I'm checking exactly where the bob first touches the ball: since the bob swings back along an arc, its distance to the ball center only equals the sum of radii right at the vertical position (φ=0), so contact happens there with a purely horizontal impulse. I'll offset the bob's resting x-position slightly to avoid any initial overlap.

Working out the hinge rotation convention about the y-axis, a positive angle swings the bob toward -x, so starting at 30° deflection puts the bob correctly on the -x side before it swings through. I'll bump the start angle up to 40° for extra margin, giving an impact speed around 1.52 m/s from energy conservation.

Checking impact speeds against the ball's expected rolling speed — around 1.2-1.8 m/s seems right to clear the back wall without the ball climbing it via spin friction, so I'll settle on 35° giving v≈1.33 m/s. Now setting up the pendulum body geometry — rod and bob placement relative to the pivot.

I need a support structure for the pivot: a world-body stand with a crossbar at pivot height, positioned beside the ball so it doesn't overlap. I'm checking whether contacts between the pendulum and its parent world body get excluded by default in MuJoCo's parent-filtering, since the crossbar sits right where the rod pivots.

Actually I realize the bob is penetrating the floor at the bottom of its swing — with bob radius 0.04 and center at z=0.03, the bottom reaches -0.01, below ground. I need to shrink the bob radius or raise its resting center so it just clears the floor.

I'm also weighing mass and density choices: a dense steel-like bob versus a lighter ball, checking whether a reasonable swing angle gives a sensible impact velocity on the ball without it flying off too fast. I'll settle pivot height and bob radius so the bob clears the floor and set densities so the handoff velocity to the ball is reasonable.

Working through the collision dynamics: mass ratio ball-to-bob is about 8, so after impact the ball exits near or above the pendulum's speed. Factoring in sliding-to-rolling friction loss (final rolling speed is 5/7 of initial), I want a final rolling speed around 0.7 m/s, which means I need roughly 1 m/s off the bob, giving a pendulum swing angle of about 23°.

Rounding to 25° gives bob speed ~0.96 m/s, and since there's no rolling friction over the travel distance, any launch speed eventually reaches the cup — so slower is actually safer and more forgiving. The strike stays symmetric in the plane so there's no lateral drift to worry about. Now I'm thinking about the cup design itself: the ball hits the back wall with low restitution, which should keep it contained, though I'm considering whether to add extra damping to the cup floor to prevent any rebound escape.

Adding rolling friction around 0.0005 gives a deceleration of roughly 0.12 m/s², enough to let the ball travel the couple meters to the cup while slowing naturally, and any rebound at low speed would stop within centimeters, which seems like solid robustness. I'll set condim appropriately so friction applies correctly between the two geoms.

But checking a worst-case lower bound of 0.5 m/s, the travel distance becomes marginal against the needed 0.9m, so I should tune μ_r down to around 0.0002 to keep enough margin even in that slower scenario.

Then I'm worried about rebound overshoot: with the cup's inner depth of 0.2m, the ball must not bounce back past x=0.93, which caps allowable rebound speed to about 0.11-0.14 m/s depending on friction choice. That means restitution needs to stay quite low, so I'm considering tuning solref parameters for the cup contacts to add damping and avoid excessive bounce.

Checking the pendulum timing: it swings a quarter period of about 0.35s to reach the ball, while the ball takes roughly 1.3s to travel, totaling around 2s for the whole sequence. After the strike, the pendulum continues forward with reduced speed, swinging past and oscillating back through the bottom near x=-0.061 once the ball is gone — I'll add minor joint damping (around 0.002) to slightly slow the swing but otherwise keep it simple.

For the cup geometry at (1,0,0), I'm skipping a base plate since the floor serves that purpose, and placing a back wall and side walls as thin boxes sized to form the cup's inner cavity, letting the left wall overlap the back wall slightly since that's fine structurally.

For the front opening, I'm computing wall segments on either side leaving a 0.12-wide gap (0.06..0.12 in relative y), giving 0.03 clearance on each side of the 0.06-diameter ball so it can pass through without getting stuck, relying on rolling friction to settle it once inside the inner region spanning roughly x∈[0.9,1.1].

I'm adding visual-only stand geometry (contype/conaffinity 0) for a post and arm that overlap the pendulum pivot harmlessly, then setting up the keyframe qpos ordering the pendulum hinge angle followed by the ball's free-joint position and orientation, making sure the ordering matches how the bodies are defined in the tree.

Checking the pendulum bob's position at 25° confirms it doesn't overlap the ball, and I verify the combined friction coefficients between floor and ball settle at reasonable values (max friction, low rolling/torsional terms) since the ball won't spin about the normal axis in this setup.

