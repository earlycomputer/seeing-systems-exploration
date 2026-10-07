In the run, the pendulum fell from 90° and struck ball1 at 0.42 s. The strike threw ball1 off the rail into the air, with an upward velocity of 0.30 m/s. Ball1 flew over ball2 and ball3 without touching them and hit ball4 at 0.63 s. That knocked ball4 into the box, where it came to rest at (1.10, 0, 0.03) m by 1.18 s. The same hit sent ball1 backwards at 3.7 m/s, faster than it arrived. Ball1 was still sliding across the floor at 3.54 m/s at 6 s. Ball2 and ball3 never moved.

The cause is the contact settings. Ball contacts used solref "0.01 0.1", which gives a contact period of about 6 ms. That is only three 2 ms steps, so the 3 m/s impacts were badly resolved: ball1 was launched upward and energy was gained on the rebound. Friction acting during the impacts made the upward kick worse.

Changes in the corrected file:
- **Softer, longer impacts:** ball, bob and rail contacts now use solref "0.1 0.05", which spreads each impact over about 8 steps.
- **Larger balls:** radius is now 0.04 m so the deeper contact squeeze stays small relative to the ball.
- **Frictionless rail and impacts:** balls, bob and rail now use condim="1", so the push stays horizontal and passes ball to ball.
- **Box:** it now dominates its contacts through solmix and has stiff, critically damped walls and floor with rolling friction, so a ball that lands stops.

I haven't run this version.

```json
{"what_happens": "The pendulum hits ball1 at 0.42 s and launches it upward off the rail. Ball1 flies over ball2 and ball3 without touching them and strikes ball4 at 0.63 s. Ball4 goes into the box and rests at (1.10, 0, 0.03) m by 1.18 s. Ball1 rebounds backwards at 3.7 m/s, faster than it arrived, and is still sliding across the floor at 3.54 m/s at 6 s. Ball2 and ball3 never move.", "works": false, "problem": "The contacts were too stiff for the 2 ms timestep and had friction, so the pendulum launched ball1 into the air over ball2 and ball3 and the impacts gained energy, skipping the ball-to-ball chain."}
```

```xml
<mujoco model="pendulum_ball_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.4 -1 2" dir="0 0.5 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.08 0 0.74">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.46" size="0.004" mass="0.001" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.04" mass="0.1" contype="2" conaffinity="2" condim="1" solref="0.1 0.05" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="rail" pos="0 0 0">
      <geom name="rail_base" type="box" pos="0.23 0 0.1" size="0.27 0.05 0.1" contype="1" conaffinity="1" condim="1" solref="0.1 0.05" rgba="0.5 0.5 0.6 1"/>
      <geom name="rail_guide_left" type="box" pos="0.23 0.0475 0.2075" size="0.27 0.0025 0.0075" contype="1" conaffinity="1" condim="1" solref="0.1 0.05" rgba="0.4 0.4 0.5 1"/>
      <geom name="rail_guide_right" type="box" pos="0.23 -0.0475 0.2075" size="0.27 0.0025 0.0075" contype="1" conaffinity="1" condim="1" solref="0.1 0.05" rgba="0.4 0.4 0.5 1"/>
    </body>

    <body name="ball1" pos="0 0 0.24">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" condim="1" solref="0.1 0.05" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball2" pos="0.15 0 0.24">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" condim="1" solref="0.1 0.05" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball3" pos="0.30 0 0.24">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" condim="1" solref="0.1 0.05" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball4" pos="0.45 0 0.24">
      <freejoint name="ball4_free"/>
      <geom name="ball4_geom" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" condim="1" solref="0.1 0.05" rgba="0.9 0.7 0.1 1"/>
    </body>

    <body name="box" pos="0 0 0">
      <geom name="box_floor" type="box" pos="0.9 0 0.005" size="0.38 0.13 0.005" condim="6" friction="0.8 0.01 0.01" solref="0.005 1" solmix="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_near" type="box" pos="0.525 0 0.07" size="0.005 0.13 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.005 1" solmix="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_far" type="box" pos="1.275 0 0.07" size="0.005 0.13 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.005 1" solmix="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_left" type="box" pos="0.9 0.125 0.07" size="0.38 0.005 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.005 1" solmix="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_right" type="box" pos="0.9 -0.125 0.07" size="0.38 0.005 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.005 1" solmix="1000" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5708  0 0 0.24 1 0 0 0  0.15 0 0.24 1 0 0 0  0.30 0 0.24 1 0 0 0  0.45 0 0.24 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The run failed — ball1 launched upward instead of forward, skipped over balls 2 and 3, hit ball4, and bounced back with an unrealistic speed gain. I need to figure out why ball1 got that upward velocity; it seems tied to the timing of the pendulum bob's contact at 0.42s, so I should check the pendulum's angle at that exact moment.

The sinking seems to come from soft contact penetration — the ball settling about 5mm into the rail — which combined with a slightly misaligned bob height means the bob strikes above center and pushes the ball down before the rail shoves it back up. The solref time constants (0.01s) are too small relative to the 0.002s timestep, giving only a handful of simulation steps per contact and likely causing these energy errors, especially at the ball1-ball4 collision where the rebound speed nearly doubled.

The bob still has downward velocity just before reaching the bottom of its arc, so when contact begins the normal direction between sphere centers tilts, pushing into the rail at an angle rather than straight on. With a 3 m/s relative speed and 2ms steps, penetration per step is around 6mm — large compared to the 25mm ball radius — so the contact is getting hammered with deep interpenetration, and as the bob swings past bottom and starts rising it may also push the ball upward.

This upward friction drag combined with ball-to-ball collisions (like ball1 striking ball4 from above and pressing it into the rail) seems to be causing spurious energy gain from stiff, mismatched contact timescales. Possible fixes: reduce contact stiffness/sensitivity since I can't change the drop height or required speed, though the needed 2ms timestep is fixed, so softening the contacts with a longer time constant seems like the way to go.

Estimating penetration depth at these speeds with solref 0.02 suggests several centimeters of overlap, which is too much relative to ball radius—so increasing ball/bob radius or spacing could help reduce relative penetration. Another option is better constraining the balls along the rail rather than relying purely on freejoint dynamics to prevent unwanted vertical escape.

I'm considering a top guide or rail cap to stop balls launching upward, but it would need to stop short of ball4's position so it can still exit into the box when struck. A cleaner fix might be lowering friction between the balls and bob to avoid unwanted rotational/sliding effects that cause the unwanted launch behavior.

Using condim=1 (frictionless) everywhere on the rail would let balls slide cleanly without spin, giving a proper Newton's cradle transfer where each ball stops dead after striking the next. Then once a ball lands in the box, its higher-condim surface would introduce friction to convert sliding into natural rolling motion.

But if collisions aren't perfectly elastic, residual velocities after each transfer would let balls 1-3 slowly drift off the rail and into the box, potentially disturbing ball 4 right before the simulation ends — I'm estimating drift speeds around 0.3 m/s could cause this within the time window, so I need to think about whether that's acceptable or if I should adjust the restitution/friction setup to avoid it.

I'm trying to pin down where that upward velocity comes from — most of the momentum transfer traces to the bob, but the vertical component doesn't fit a pure horizontal contact. It could be a slight tilt in the contact normal since the bob's center sits a bit higher than the ball's, or possibly friction effects at the bottom of the swing where the bob's velocity is purely horizontal, so I need to check how the ball's contact geometry interacts with that.

This friction modeling is getting too finicky with soft contacts, so I'll just switch to frictionless contacts (condim 1) for balls, bob, and rail entirely, meaning forces only act along the contact normal. I need to make sure the bob's resting height roughly matches the ball's settled height on the rail, accounting for slight sinking under gravity, so the normal isn't noticeably tilted and vertical velocity at impact stays small.

The energy gain I'm seeing between ball1 and ball4 points to contact instability, so I should tune solref parameters—adjusting timeconst and damping ratio—to make the contact stiffer and more stable, working through the relationship between timeconst, dampratio, and the resulting stiffness/damping coefficients to avoid injecting spurious energy.

With bigger balls (radius 40mm, spacing 150mm, gap 70mm), the 15mm penetration looks acceptable. Checking restitution across different tc/ζ combos: ζ=0.25 gives e≈0.44 (too low), while ζ=0.1 with tc=0.05 gives ω=200 and e≈0.73, which seems more reasonable; I'm also noting solimp's impedance clamps and the dt-based tc floor are fine. I still need to figure out the rail's solref, since ball-rail contact uses an average of both solrefs.

I'm checking the static sink of a resting ball under ω=200 (~0.25mm, negligible), and deciding to use the same solref across balls, bob, and rail, while keeping the box's damped solref separate for moderate mixing. Then I'm tracing through the restitution chain with e=0.85 (lower ζ=0.05, tc=0.1): each ball passes ~92.5% of velocity forward while retaining a small residual (~7.5%), so by ball4 the velocity has grown to ~2.3 m/s while earlier balls drift forward with leftover velocity and eventually re-collide.

Balls 1-3 likely drift toward the end at low speed and fall into the box near the near wall, while ball4 flies farther and bounces off the far wall before stopping, so the landing spots seem reasonably separated. I'm now weighing whether these residual drifting balls truly need to come to rest, and considering adding small rail friction to settle things cleanly.

Actually, freejoints don't support damping directly, and adding condim friction would barely affect fast balls over such short gaps while letting slow ones roll indefinitely without rolling resistance — so I'll just keep the rail frictionless.

With a frictionless rail, the pendulum bob keeps its 0.23 m/s, swings back and forth, and could strike ball1 again if it hasn't drifted off — that's acceptable. For balls entering the box, the condim 6 contact uses the box's higher friction (0.8, 0.01, 0.01), so they'll settle properly there. Vertically things stay stable since ball-ball collisions occur along the same center height, and with the rail penetration tiny (~0.25mm at this spin), the bob's center sits right at the expected 0.24 height above the rail.

Now I'm working out the side guide placement — with ball radius 0.04 and guides at y=±0.045, I need roughly 5mm clearance between guide inner faces and the balls, setting guide half-width around 0.0025 so the inner face lands at 0.045. I'm finalizing the full geometry: ball radius 0.04, centers at z=0.24, with ball1 at x=0, ball2 at 0.15, ball3 at 0.30, ball4 at 0.45, and the pendulum bob (also radius 0.04) starting at its bottom position around x=-0.08.

I'm tracking the pendulum pivot at (-0.08, 0, 0.74) with a 0.5m arm, and sizing the rail so ball4 (center 0.45) just clears the rail edge at x=0.5 before tipping off. For the landing box, I'm computing the fall time for ball4 from z=0.24 down to the floor (about 0.19m drop, ~0.197s), and estimating its horizontal travel at an exit speed of 2.3 m/s to land around x≈0.96, checking that the box walls (0.13m tall) are positioned correctly to catch it.

For contact stiffness, I'm realizing the default solmix between the ball (0.1 mass, 0.05 solimp) and box (0.02, 1) gives a very soft contact — roughly 32 rad/s natural frequency — which would let the ball penetrate about 6cm on landing at 2 m/s, way more than its 0.04 radius. I need to stiffen the box's solref parameters so the contact mix isn't so compliant, otherwise the ball will sink through the floor instead of bouncing realistically.

The hinge works fine when the bob hits the ball. Rolling friction with coefficient 0.01 and radius 0.04 gives deceleration of about 1.75 m/s², which checks out, and small damping ratios shouldn't cause issues with solimp. I'm ready to write up the answer with initial qpos values: pendulum at 1.5708 radians, balls positioned at 0.24, and spaced out at 0.15 intervals afterward.

