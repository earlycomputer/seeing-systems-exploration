The scene does not work: the ball never stays in the cup.

**What the picture shows**
- **Pendulum:** it starts about 50° back and swings down through the ball's position. After that, its later (darker) copies stay in a narrow fan of about ±15° around vertical. A heavy pendulum that simply hit the ball once would keep swinging about ±40°. Something keeps taking its energy.
- **Ball:** nothing appears to be resting in the cup at x ≈ 1 m. The ball seems to end back near x ≈ 0 under the pendulum.

The likely story is that the ball was hit hard, crossed the cup, bounced off the back wall and back over the low front lip. It then rolled back down the ramp and was hit by the pendulum again and again, which drained the pendulum's swing.

**What I changed in the corrected file**
- **Gentler strike:** the pendulum now starts at 32° instead of 50°.
- **Lower, shallower ramp:** the lip is 2.5 cm high instead of 3 cm, so less speed is lost at the bottom of the ramp.
- **Longer cup:** the inside is about 15 cm long instead of 11 cm.
- **Front wall above the ball's centre:** its inner face is now taller than the height of the ball's centre on the cup base. A ball rolling back can't climb it.
- **Bounces damped out:** the cup walls and the ball have overdamped contacts.
- **Ball stops quickly:** the cup base has strong rolling friction, so the ball comes to rest inside.

```json
{"what_happens": "The pendulum swings down from its raised start and strikes the ball, but afterwards its swing quickly shrinks to a narrow fan around vertical, and no ball is seen resting in the cup at x = 1 m. The ball appears to end back near x = 0 under the pendulum, suggesting it bounced back out over the low front lip of the cup, rolled back down the ramp and was repeatedly hit by the pendulum.", "works": false, "problem": "The ball arrives too fast, bounces off the cup's back wall and escapes back over the low front lip, so it does not end up in the cup."}
```

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0.5 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- visual support beam at the pivot (no collisions) -->
    <geom name="support_beam" type="box" pos="-0.041 0 0.523" size="0.02 0.08 0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: pivot 0.5 m above the bob's lowest point, bob just behind the ball -->
    <body name="pendulum" pos="-0.041 0 0.523">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.48" size="0.005" mass="0.02" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.02" mass="0.3" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.02">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.02" mass="0.03" friction="1 0.005 0.0001" solref="0.02 3" rgba="0.1 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball's start, with a shallow entry ramp up to its front lip -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.159121 0 0.005792" euler="0 -10.125 0" size="0.081266 0.06 0.005" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_front_wall" type="box" pos="-0.08 0 0.0125" size="0.005 0.085 0.0125" solref="0.02 4" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_back_wall" type="box" pos="0.08 0 0.04" size="0.005 0.09 0.04" solref="0.02 4" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_left" type="box" pos="0 0.085 0.04" size="0.085 0.005 0.04" solref="0.02 4" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_right" type="box" pos="0 -0.085 0.04" size="0.085 0.005 0.04" solref="0.02 4" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_base" type="box" pos="0 0 0.001" size="0.075 0.08 0.001" condim="6" friction="1 0.02 0.02" solref="0.02 4" rgba="0.5 0.4 0.25 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.5585 0 0 0.02 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm trying to make out the pendulum's residue trail and the ball's position in the side and plan views—at this resolution it's hard to tell whether the ball stays near x≈0 or sits inside the cup near x≈1.

Looking at the plan view, the pendulum rod and ball show up as a cross shape near x=40, while the side view has a small ball near the floor around the same x position. I'm checking whether the cup region at x=109 shows the ball inside it, and wondering if any residue trail would appear between the pendulum's rest position and the cup if the ball had actually traveled there.

At roughly 0.26s per frame and a speed of 1.2 m/s, the ball would cover about 0.31m per frame, so I'd expect to see a few copies along the floor in the plan view — but I don't see dots in that region beyond background speckle noise. I'm also considering the pendulum's swing amplitude: if it struck the ball and lost some velocity, it should swing out to a wider angle, yet the fan shown is narrow and dense, which suggests either energy loss or that the bob is still in contact with something, like the floor.

Measuring the fan span at the bottom more carefully, it seems to only cover about ±14°, far less than I'd expect from an inelastic collision retaining ~90% velocity. This makes me wonder what's absorbing the extra energy — maybe the ball stays in continuous contact with the pendulum rather than separating cleanly after the strike.

Maybe the ball got trapped under the bob, pushed into the floor by the slightly downward contact normal. Looking at the plan view, the "+" shape near x≈40 seems to be the support beam's vertical line (0.16 m, 10 px) crossing the pendulum rod's residual trace, not the ball itself.

Checking the side view near the floor and the cup region, I still can't clearly distinguish whether a ball is resting there. The real puzzle is why the pendulum lost energy — if the ball stayed pinned in place, repeated contact should still transfer momentum unless the bob is far heavier, which might explain minimal energy loss on each strike.

Calculating a basic elastic-ish exchange gives the ball around 1.68 m/s with the pendulum continuing at a similar speed, swinging up to roughly 40°, which doesn't show damping. That makes me reconsider whether the fan shape in the drawing spans only a narrow ±15°, suggesting the amplitude actually does shrink—I'm trying to measure the fan's pixel extent near the pivot to confirm.

But if the rendering grays older copies lighter and darker ones dark, a steady 40° amplitude should show dark copies across the full fan, not a narrow one, which means something is removing energy from the swing. I'm now wondering whether contact with the floor, some hinge friction, or continued contact with the ball is draining energy from the pendulum.

My new idea is that the ball keeps getting struck, pushed toward the ramp, rolls back down without escaping, and collides with the pendulum again repeatedly, sapping its energy each pass until it settles near the center.

Maybe the ball bounces off the back wall at a reduced speed and rides over the front wall's edge if its center is above the wall height, which could explain a failure. Looking at the side view, there's a dark blob near the floor that might be the ball, but no residue trail in the cup, so my tentative judgment is that it doesn't work and the ball ends up back near the pendulum — though the narrow pendulum fan pattern still nags at me as evidence of repeated interaction.

I want to make the design more robust by removing failure modes like the ball escaping the cup or climbing the ramp. One idea is to match the pendulum and ball masses so the pendulum stops after striking rather than continuing to swing, or to redesign the cup with a higher back wall or ramps on both sides for better containment.

Another approach is lengthening the cup interior and increasing rolling friction so the ball settles before bouncing back toward the front wall, plus making the back wall contact overdamped to reduce restitution. I'm also considering slightly reducing the launch speed so the ball barely clears the lip and drops near the front, then rolls to a stop due to friction.

Running the numbers, with a rolling friction coefficient of 0.01 the deceleration is around 3.5 m/s², stopping a 1 m/s ball in about 0.14 m — close to the cup's 0.11 m interior length. Bumping friction to 0.02 roughly doubles deceleration, stopping the ball in about 0.07 m, though most of the ball's travel happens while airborne before it even touches the cup floor.

A rolling ball without resistance on the floor should be fine either way. I'm also considering making the back wall overdamped via solref settings, though MuJoCo's default solmix averaging means the ball's contact parameters get blended with the wall's across all surfaces, which should still keep things stable even if it slightly dampens the pendulum strike's bounce—acceptable since that collision is meant to be inelastic anyway.

For the front entry, I'm thinking a ramp-up design to a lip, with the interior front wall matching that lip height so a slow-returning ball can't climb back over. The real uncertainty is in the pendulum-to-ball speed transfer: the naive inelastic-collision estimate could be off by up to 2x if the soft contact behaves more elastically than expected, so I want to make that collision more deterministic.

I'm working through whether the contact is overdamped (favoring inelastic) but then realizing the pendulum keeps pushing the ball after merging since sliding friction decelerates the ball faster than the pendulum decelerates near the bottom—so the ball accelerates toward rolling while still in contact, then the pendulum falls behind once rolling kicks in, making the final transferred velocity complicated to pin down from energy arguments alone.

Given this uncertainty, I'm considering striking the ball higher, near the center of percussion, to get pure rolling immediately rather than relying on sliding friction to sort it out—though elastic collisions still leave the roll speed ambiguous. A more robust design might just make the cup tolerant of a wide range of incoming speeds, perhaps with a taller back wall.

I'm also exploring whether a lid over the cup could limit how high the ball bounces, keeping its rebound trajectory low enough to stay contained, though the front wall height still poses a risk of the ball riding over it. A one-way flap feels too complex, so I'm leaning toward a design where the front wall's inner face is taller than its outer ramp face, forcing the ball to climb a step to escape back out.

If that step height roughly matches the ball's radius, a rolling ball physically can't climb it since the contact point stays at center height with a purely horizontal normal force — it would need to become airborne, which overdamped contacts should mostly prevent. I'm setting the step height to match the radius, lengthening the cup's interior and raising the back wall for extra capture margin, and now I'm tuning the pendulum release speed so the ball ends up rolling at roughly the bob's velocity.

Working through the energy equations, a 30° release angle gives a speed that clears the step even at the lower bound of expected rolling speeds, while the upper bound still gets safely captured by the back wall thanks to the soft overdamped contact absorbing the impact.

Now I'm checking the ramp kink losses — with a shallow 8° transition angle the ball only loses about 2% of its energy there, which keeps the shallower ramp option attractive. I'm working out the cup's inner geometry to pin down exactly where the front wall sits relative to the ramp's endpoint.

Checking the box bottom corner clearance — it dips slightly below the floor at that cup frame x, which is fine since it's static geometry. Now I'm setting positions and sizes for the front wall, back wall, side walls, and base panels to make sure they align with the ramp edges.

I realize the front wall's top edge sits below the ball's resting center, so contact there could push the ball upward and let it climb out if moving fast — I'm reconsidering whether to keep the base plate at all. I'm testing raising the wall/ramp height to 0.025 so the escape velocity threshold works out to roughly 0.59 m/s, which should keep normal rolling speeds contained.

Now I'm recalculating the ramp geometry with this new height: extending the slope line, finding its length and angle (about 10.1°), then locating its midpoint and deriving the wall's position and orientation in the cup's local frame so I can place the front wall segment accordingly.

Checking that the ball sits correctly above the cup's base wall edge, I confirm the contact geometry works out with the wall top above the ball's center. For damping, I'm setting individual solref values on the ball and walls so their averaged contact stiffness gives an appropriately inelastic collision at the pendulum strike point, then computing the release velocity from the 32° swing angle using energy conservation, getting about 1.22 m/s.

No extra hinge damping needed since the ball leaves the scene after impact. Time to write up the final answer.

