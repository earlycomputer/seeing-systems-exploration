Ball1 starts with a keyframe velocity and matching spin, so it rolls along +x. It knocks ball2, and ball2 knocks ball3. The cup is a box corral open toward the balls, with a 5 mm lip across its mouth. Ball3 rolls over the lip and hits the back wall. Its leftover forward spin keeps it pressed against that wall, and the lip stops it rolling back out. Rolling friction on the balls makes everything settle well before 6 s.

```xml
<mujoco model="ball_chain_into_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.025">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.3 0 0.025">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.6 0 0.025">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_back" type="box" pos="0.065 0 0.03" size="0.005 0.045 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_left" type="box" pos="0 0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_right" type="box" pos="0 -0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_lip" type="box" pos="-0.06 0 0.0025" size="0.003 0.035 0.0025" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.025 1 0 0 0  0.3 0 0.025 1 0 0 0  0.6 0 0.025 1 0 0 0" qvel="2 0 0 0 80 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches cup
ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning the physics setup: balls in a row along the x-axis, with ball1 given initial velocity so collisions transfer momentum between equal-mass balls somewhat inelastically. I'm thinking through how rolling spin affects each collision—ball1 keeps its spin and continues while ball2 gains linear velocity but slides without spin until friction catches it—and now I'm considering where to place a cup in the scene.

Since the floor can't have a literal hole, I'm working out how to make ball3 end up resting inside a cup using raised walls instead. A simple U-shaped corral with a back wall could stop the ball, but it might bounce back out, so I need some kind of lip or small step at the entrance low enough for the ball to roll over but high enough to trap it once inside—balancing the lip height against the ball's radius and incoming speed so it clears the step going in but gets blocked coming back out.

Rather than building a raised platform, I'm leaning toward a simpler fix: make the cup's back wall highly damped and inelastic (via solref settings) so the ball's forward velocity just gets absorbed on contact, and rely on its residual rolling spin plus floor friction to keep driving it forward against the wall so it naturally stays pinned in place.

For the cup shape itself, I'll skip the front lip entirely and just use side and back walls, leaving the front open—since a "resting in cup" check is likely based on whether the ball's center falls within the cup geometry's bounding box in x, y, and z, an open-front U-shape should satisfy that as long as the ball settles inside it. I also need to remember that MuJoCo balls won't naturally stop rolling on a floor without rolling friction, so condim 6 will be necessary to get realistic damping behavior.

For the multi-ball collision scenario, ball1 will keep rolling after hitting ball2 due to residual spin, bouncing between them until everything converges toward the cup, which should be fine since the success condition only cares about ball3's position—though I need to watch that ball1 and ball2 don't shove ball3 around once they're near the cup. To get the balls to actually settle rather than roll forever, I'm adding rolling friction via condim="6" with a small rolling friction coefficient, estimating the resulting deceleration to make sure they stop within a reasonable distance given the ball radius.

Now I'm working through how restitution behaves in these contacts—since MuJoCo's default solref produces a critically damped spring-damper response, I'm checking whether that yields near-zero bounce-back velocity when two equal-mass balls collide, which matters for predicting how far ball1 travels after striking ball2.

Floor-ball contact mixing should be fine too, even if slightly jittery with low damping. Actually, maybe I should avoid over-engineering this: if I give ball1 enough speed, even inelastic collisions will chain momentum through to ball3, with all three rolling toward the cup eventually. I just need to design the cup narrow enough that only ball3 fits, so ball1 and ball2 don't accidentally displace it.

With elastic-ish collisions instead, ball1 keeps some spin and velocity after hitting ball2, ball2 slows from friction before hitting ball3, and so on — it gets messy tracking exact fractions of v0 through each collision, but as long as rolling friction eventually stops everything, I just need to work out the distances between balls so the chain reaction resolves correctly.

Let me actually plug in real numbers: ball radius 0.025m, mass ~0.065kg, spacing them at 0.3m intervals with initial velocity 1.5 m/s. I'm computing the rolling friction deceleration, then tracing roughly how far each ball travels before the next collision and how its speed decays, down to ball3's impact with the back wall of the cup.

Working through the chain of collisions: ball1's leftover speed still gets it close enough to the cup to pile up with the others, and ball2 ends up knocking ball3 further into the wall. For them to count as settled in the cup by 6 seconds, their speeds need to drop below 5 cm/s, which depends on properly configuring rolling friction — likely needing condim 6 and torsional/rolling friction coefficients set on the ball geoms rather than just the floor.

Now I'm sketching the cup's geometry: positioning the back wall, side walls, and interior dimensions so a 5cm ball fits with clearance, checking that ball3 ends up resting inside the bounding box and ball2 sits just behind it.

I'm debating whether to add a small front lip to help trap the ball on entry, reasoning through whether a thin raised edge (a few millimeters) would stop the ball at its entry speed without making entry too hard, versus keeping it a simple open-front U-shape.

Ball3 loses some velocity fraction crossing the lip edge, dropping from roughly 0.67 to 0.55 m/s, which still clears the needed threshold of about 0.41 m/s with moderate margin — so a smaller lip height around 0.004 should work geometrically with the thin box-edge collider. I'm also considering wall damping settings to keep the bounce inelastic enough that the ball doesn't rebound with excess spin.

For the ball-ball collisions, even in the worst case of zero restitution, momentum transfer plus rolling friction should carry enough forward energy through the chain — ball1's spin and linear motion push into ball2, and together they roll forward with enough speed that ball3 still ends up near 0.6 m/s after impact.

Bumping v0 up to 2.0 gives more margin: ball3 would hit the back wall around 0.9-1.0 m/s, which is fine since the lip is small enough not to cause problematic bouncing, and the 0.33 m travel distance from ball3's position to the lip leaves enough room. For the initial velocity setup, I'm setting ball1's qvel with forward linear velocity and matching angular velocity for a pure rolling state, using the free joint's local frame which aligns with world frame given identity orientation.

Now I'm working out the full keyframe qpos for all three balls positioned collinearly along x at y=0, resting at the correct height, with the cup positioned at x=1 and its wall geometry (back wall and side walls) sized so the inner faces align with where the balls should come to rest, keeping everything straight since there's no y-offset.

Defining the lip geometry...

Checking cup capacity for two balls and estimating settling times. I'm considering bumping rolling friction slightly to help balls stop sooner, then tracking residual speeds for ball3 after collisions to verify it still ends up seated properly.

Now I'll set up the expected contact/rest conditions (ball1-ball2, ball2-ball3, ball3-cup, ball3 at rest), define the floor plane, add lighting, and finish the scene.

