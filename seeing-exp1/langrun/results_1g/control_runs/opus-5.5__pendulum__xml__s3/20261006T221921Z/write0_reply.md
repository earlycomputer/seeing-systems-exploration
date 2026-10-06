The pendulum drops from 50° and strikes the ball at the bottom of its swing. The ball then rolls 1 m, climbs a shallow ramp over the cup's front lip, and is caught by tall back and side walls. I worked out the geometry and speeds by hand but have not run the simulation, so the final position and the at-rest check are predictions.

- **Strike:** the 1 kg bob on a 0.5 m arm reaches about 1.87 m/s at the bottom.
- **Ball speed:** the ball is 0.05 kg. Assuming the default contact barely bounces, it should leave at about 1.78 m/s and slow to about 1.27 m/s once rolling.
- **Ramp:** climbing the 2.5 cm ramp needs at least about 0.6 m/s, so there is a good margin.
- **Settling:** the default soft contacts absorb nearly all of each impact. The ball should come to rest against the back wall, about 3 cm past the cup centre at x ≈ 1.03, well inside the 6 s.
- **Walls:** the back and side walls are 10 cm tall in case the ball comes in faster than expected.
- **Friction:** I set it to 0.6 rather than the default 1. A ball still spinning against the back wall can then no longer climb it.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" friction="0.6 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.0548 0 0.535">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.006" mass="0.05" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="1" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.11796 0 0.00271" euler="0 -11.768 0" size="0.061288 0.07 0.01" friction="0.6 0.005 0.0001" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_back" type="box" pos="0.065 0 0.05" size="0.005 0.07 0.05" friction="0.6 0.005 0.0001" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_left" type="box" pos="0 0.065 0.05" size="0.07 0.005 0.05" friction="0.6 0.005 0.0001" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_right" type="box" pos="0 -0.065 0.05" size="0.07 0.005 0.05" friction="0.6 0.005 0.0001" rgba="0.6 0.5 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.872665 0 0 0.03 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the scene layout: positioning the ball and a pendulum so that at the bottom of its swing it strikes the ball moving in the +x direction toward a cup, and I'm considering whether a flat-floor cup setup actually works physically or if a ramp is needed for the ball to roll up into it.

Since MuJoCo's default contacts are mostly inelastic, the ball hitting a back wall should mostly stop rather than bounce out, which helps it settle in the cup. But I'm also considering whether leftover spin from rolling friction against the wall could push it back out, which I need to account for.

I think a simpler, more robust design is a cup made from a U-shaped arrangement of walls (back wall plus two side walls), letting the ball enter from an open front and settle against the back wall. I can calculate the required entry speed if there's a small lip to climb, using rolling dynamics (v² > (10/7)gh), but since condim 3 gives no rolling resistance by default, the ball's speed stays predictable as it crosses the lip.

I'm leaning toward making the walls tall enough (around 0.04, taller than the ball's radius) so the ball can't hop back out once inside, keeping the base as a flat plane rather than adding an extra floor plate to avoid unnecessary complexity.

Now I'm designing a low front lip (~0.025 height) with a short ramp leading up to it, so the ball rolls up the incline, over the lip edge, and drops back down onto the floor before rolling toward the back wall and stopping inelastically. Since the cup geometry is static with no joints, I don't need to worry about ramp-floor collisions, just the ball contacting the ramp surface as it's rotated at a small angle.

I'm now sizing the cup itself — centering it around x=1.0 with thin walls, checking that the ball settles close enough to the back wall to count as "in the cup," and adjusting the inner width smaller so the resting position is within an acceptable radius, while making sure the ball (0.06 diameter) still clears the lip drop and fits the inner cup length afterward.

Rather than relying on the ball bouncing cleanly off the back wall, I'm thinking it's fine if it just loses energy bouncing between the lip and back wall and settles somewhere inside — that's acceptable. I'm also reconsidering whether I even need a ramp: hitting the front lip directly at its height (0.025, less than the ball radius 0.03) risks an unpredictable inelastic collision in MuJoCo, so a ramp leading smoothly up to the lip height is the safer choice, with the ramp's top edge aligned with the lip's top surface at the front wall's outer face.

Working out the rotation math for the ramp: rotating about the y-axis by angle φ maps the local x-axis appropriately, so I need a negative angle for the ramp to rise toward +x. I calculate θ ≈ 11.77° from the rise/run, giving a slope length of about 0.1226 m, so the half-length is roughly 0.0613 m, with the top surface centered at z=0.0125.

I'm computing the box center by offsetting from the top surface along the local normal direction, using sinθ≈0.204 and cosθ≈0.979, landing on a center near (0.872, 0, 0.0027). I check the low end doesn't dip through the floor and start tracing the high-end corner position along the negated normal direction.

Checking the ramp's low front edge, it meets the floor smoothly at x≈0.81 where the ball transitions from flat ground onto the incline — this looks fine as is, maybe extending the ramp slightly lower is unnecessary. I'll set the ramp width with a y half-extent of 0.06.

Now I'm laying out the cup geometry: an inner region from x=0.93 to 1.07 with y from -0.06 to 0.06, a back wall around x=1.07-1.08, and side walls bounding the interior near x=0.93-1.08 at height 0.05. I'm checking whether the ball, after dropping from the lip, lands against the back wall or settles somewhere off-center, but since the setup is symmetric there's no lateral drift to worry about — y stays at zero.

I need enough speed for the ball to climb the ramp, requiring v² greater than roughly 0.35 (v>0.59 m/s), but some energy is lost at the floor-to-ramp transition due to the impact angle and spin mismatch, so I'm picking an initial ball speed around 1.2 m/s. After the lip, the ball travels into the cup and strikes the back wall at roughly 1 m/s — this collision is mostly inelastic in the normal direction given the soft contact damping, though some restitution may occur. I'm also working through what happens to the ball's spin after translational motion is stopped: the floor friction keeps pushing the still-spinning ball into the wall, so I need to trace how wall friction interacts with that remaining angular momentum.

With default friction of 1, the upward wall force barely balances gravity — too marginal, so I should explicitly set friction lower, like 0.6, on the relevant surfaces so the spin properly decays and the ball settles at rest. I also need to check what happens if the ball bounces back toward the ramp's lip, since that inner face is short and the contact geometry there could behave oddly.

Adding rolling friction could help dampen motion more gradually, but condim 3 contacts should already be inelastic enough to kill normal velocity on each wall hit. I'm estimating whether a small rolling resistance coefficient would meaningfully slow the ball without over-damping its approach.

Actually there's a subtlety I missed: the ball slides before rolling kicks in, so friction converts initial velocity to 5/7 for rolling. So launching at 1.2 m/s only gives rolling speed around 0.86 m/s, meaning I should aim for a higher launch speed, maybe 1.8 m/s giving rolling speed near 1.29 m/s. Checking the sliding phase distance with these numbers, it's small enough (around 0.13 m) not to matter much. Now I'm setting up the pendulum hinge geometry, with the pivot positioned above the ball.

so the ball separates from the bob at that point. With a heavy bob (say 1 kg) versus a light ball (~0.03 kg), momentum sharing means the ball should pick up velocity close to the bob's strike velocity, and since MuJoCo's critically-damped contact model doesn't produce bouncing, there's no extra restitution boost—so I'm estimating ball velocity roughly equal to v_bob at the bottom of the swing.

Now I need to nail down the geometry: the bob should strike the ball at roughly the same height so the hit is horizontal, meaning the bob's center needs to sit near the ball's resting height without clipping the floor, which constrains the bob's radius pretty tightly—so I'm considering slightly raising the bob's center and accepting a small downward component to the impact instead.

That means contact happens right near maximum bob speed at vertical, which works fine even with slight penetration overshoot. I also need to check the rod geometry doesn't collide with the ball — with the rod radius thin and offset from the ball's position, there's enough clearance, and as the bob swings through, the ball moves away so no further interference.

Since there's no damping, the pendulum will keep swinging indefinitely after the strike, but that's harmless since the ball is already a meter away by then — I could add slight joint damping just to settle things eventually, but it shouldn't affect the strike speed. Now I'm working out the length relationship: pivot height equals ball radius plus length, and I need to solve for the initial swing angle that gives the bob a velocity of 1.8 at the bottom using energy conservation.

Picking L=0.5 m gives θ0≈50°, yielding v≈1.87 m/s at impact — I'll keep the rod light so the bob mass dominates, making it essentially a simple pendulum, and the bob's own rotational inertia is negligible. For the ball's rolling speed after impact, I'm applying the 5/7 factor from rolling-without-slipping dynamics, giving about 1.34 m/s, then considering how the ramp transition introduces some additional loss depending on the angle.

After climbing the 0.025 m rise, the ball still has plenty of speed left to clear the top comfortably. But if restitution launches the ball much faster — say doubling to around 3.7 m/s linear, 2.7 m/s rolling — then at the ramp's lip the ball could leave the surface entirely and go ballistic, and I'm now working out whether its resulting trajectory would clear the lip or strike the back wall mid-flight given the fall time and wall height.

I'm realizing the ball could fly clean over the existing back wall, so I should raise both the back wall and the side walls to about 0.1 m height to keep everything contained, leaving only the ramp side low. I also need to check whether a fast rebound off the taller back wall could send the ball back toward the lip and pop it over that edge too, though with near-zero restitution this seems unlikely. Then I check the baseline case at 1.17 m/s: computing v²/r against g shows the ball leaves the surface immediately at the edge and goes ballistic there as well, so I'm working out its horizontal launch speed and fall trajectory from that point.

I could shrink the cup's inner region so the resting position sits nearer the center, adjusting the ramp top accordingly. I also need to check that wall friction from the ball's spin, combined with floor friction, doesn't produce enough upward force to lift it, and confirm the landing after flight is treated as inelastic rather than bouncing.

Checking total timing: travel plus fall is roughly 1.5 seconds, well under the 6-second window, so the spin decays quickly against the wall and floor friction before anything else happens. I should also verify the pendulum doesn't clip the ball mid-swing since the ball outpaces the decelerating bob, and confirm nothing obstructs the pendulum's backswing from its 50° starting angle.

Working through the hinge geometry, I'm computing the pivot location and the bob's starting coordinates relative to it, then setting up the hinge axis along y so the rod rotates correctly from the -z resting direction toward +x as the angle increases.

I'm setting the keyframe qpos to +50° (0.8727 rad) for the pendulum hinge, followed by the ball's freejoint values, and double-checking the body ordering in the XML matches this. I also verify the bob's resting height clears the floor by a small margin and start checking whether the pendulum's geoms might collide unexpectedly with the static floor.

For the ball-bob contact geometry, I compute the horizontal offset needed so contact occurs right at vertical: using the Pythagorean relation with the combined radii (0.055) and vertical offset (0.005), I get dx ≈ 0.054772, placing the pivot at x = -0.054772, though I consider nudging it slightly closer so contact triggers just before the bob reaches true vertical.

For masses, the ball (radius 0.03, default density) comes to about 0.113 kg, while the bob needs an explicit mass setting to reach 1 kg given its smaller radius. I'm now working through the momentum exchange between the two given this mass ratio and zero restitution, thinking about how the bob and ball velocities relate after contact.

After checking the common-speed approximation and the effect of rolling and the ramp, I decide to lighten the ball by setting its mass explicitly to 0.05 kg, which brings the velocities into a better range. Now I'm sketching the pendulum geometry: a capsule rod with its endpoints and radius, a mass value, and a sphere bob positioned at the rod's end.

Then I turn to friction settings for the floor, ball, and cup walls, reasoning about how MuJoCo combines friction coefficients and whether the bob-ball contact could impart unwanted spin on the ball during the strike, concluding it's probably fine. I also think through whether the default contact solver parameters introduce any unintended bounciness, deciding the tall walls should contain it regardless, before moving on to positioning the cup body.

Now I'm working out the ramp geometry inside the cup frame — computing the box's center position, half-sizes, and rotation angle so it sits flush against the inner wall at the correct slope angle.

I'm also laying out the back and side walls: setting their centers, half-extents, and heights, while checking whether the side walls might overlap the ramp's upper edge given its position at x_rel -0.06.

Checking that the side walls at |y|≥0.06 clear the ball's path since the ball radius is 0.03 and travels along y=0, so there's no obstruction. I'm leaving the cup floor open rather than adding a thin base, since that would create an unwanted step — the ball should land directly on the world floor inside the cup. For the ramp's lower edge, I'm confirming the top surface meets z=0 exactly at x_rel=-0.18, with the end face extending slightly below the floor, which is fine since contact only matters at the top surface where the ball rolls on.

Now I'm finalizing visuals and the keyframe setup — no skybox needed, just a light, with qpos set to the ramp angle and ball position and qvel defaulting to zero. Writing the final XML file with each element's attributes on a single line.

