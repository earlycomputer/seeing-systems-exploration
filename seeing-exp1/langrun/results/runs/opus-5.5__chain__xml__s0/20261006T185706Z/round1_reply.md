**What happened:** the run blew up at the first collision. At 0.07 s ball1 touched ball2, and both were thrown apart at about 375 m/s, flying kilometres away. Ball3 never moved, and nothing reached the ramp or the cup.

**Cause:** my ball contact setting `solref="0.005 0.02"` made the contact act like a spring that oscillates at about 10,000 rad/s. With a 0.002 s step the integrator can't follow that, so the collision added energy instead of conserving it.

**Changes in this version:**
- **Contact stiffness:** the ball contacts are slower and still bouncy (`solref="0.025 0.1"`), about 400 rad/s. The integrator stays stable and restitution should be around 0.7.
- **Balls:** they are larger (r = 0.04 m) so contact overlap stays small. Ball1 starts rolling at 3 m/s.
- **Ball3 placement:** it sits just 2 cm past ball2, so ball2 hits it while still sliding.
- **Ramp and cup:** they are rescaled to a 0.10 m rim. By my estimate ball3 reaches the ramp at about 1.6 m/s and clears the rim. Ball1 and ball2 should end up too slow to clear it.

I haven't run this version.

```json
{"what_happens": "ball1 hits ball2 at 0.07 s and the contact goes numerically unstable: both balls are thrown apart at about 375 m/s and fly off kilometres away, while ball3 never moves and nothing reaches the ramp or cup.", "works": false, "problem": "The ball contact settings (solref 0.005 0.02) make a near-undamped spring of about 10,000 rad/s that the 0.002 s step cannot integrate, so the first collision explodes."}
```

```xml
<mujoco model="three_ball_chain_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.75 0.78 0.8 1"/>
    <material name="ramp_mat" rgba="0.55 0.4 0.25 1"/>
    <material name="cup_mat" rgba="0.2 0.45 0.8 1"/>
    <material name="ball1_mat" rgba="0.85 0.15 0.15 1"/>
    <material name="ball2_mat" rgba="0.95 0.75 0.1 1"/>
    <material name="ball3_mat" rgba="0.15 0.7 0.25 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0.8 -1.0 2.5" dir="-0.2 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="side" pos="0.85 -1.8 0.5" xyaxes="1 0 0 0 0.3 1"/>

    <geom name="floor" type="plane" size="5 5 0.1" pos="0 0 0" material="floor_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>

    <!-- 15 degree ramp: top surface meets the floor at x = 1.0 and rises to z = 0.10 at x = 1.373 -->
    <geom name="ramp" type="box" size="0.193 0.08 0.01" pos="1.1890 0 0.0393" euler="0 -15 0" material="ramp_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>

    <body name="ball1" pos="0 0 0.04">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.04" density="1000" material="ball1_mat" friction="0.05 0.005 0.0001" solref="0.025 0.1"/>
    </body>

    <body name="ball2" pos="0.4 0 0.04">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.04" density="1000" material="ball2_mat" friction="0.05 0.005 0.0001" solref="0.025 0.1"/>
    </body>

    <body name="ball3" pos="0.5 0 0.04">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.04" density="1000" material="ball3_mat" friction="0.05 0.005 0.0001" solref="0.025 0.1"/>
    </body>

    <!-- static cup sitting on the floor just past the top of the ramp -->
    <body name="cup" pos="0 0 0">
      <geom name="cup_bottom" type="box" size="0.16 0.1 0.005" pos="1.533 0 0.005" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_front" type="box" size="0.005 0.1 0.0475" pos="1.378 0 0.0475" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_back" type="box" size="0.005 0.1 0.125" pos="1.688 0 0.125" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_left" type="box" size="0.16 0.005 0.0475" pos="1.533 0.095 0.0475" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_right" type="box" size="0.16 0.005 0.0475" pos="1.533 -0.095 0.0475" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- ball1 starts rolling without slip at 3 m/s along +x (spin 75 rad/s about +y) -->
    <key name="start" qpos="0 0 0.04 1 0 0 0  0.4 0 0.04 1 0 0 0  0.5 0 0.04 1 0 0 0" qvel="3 0 0 0 75 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm suspecting the ball-ball collision explosion comes from the contact solref being too stiff relative to the timestep—a time constant of 0.005 with a 0.002s step and low damping creates an unstable, nearly-undamped spring that pumps energy into the system rather than dissipating it.

The deeper issue is penetration: moving 8mm per step at 4 m/s means the balls penetrate significantly before the solver reacts, and solimp saturates at that depth, producing a massive restoring force and runaway velocity. I'm thinking the fix is to loosen the stiffness or accept a more inelastic collision where both balls move at roughly half the initial velocity afterward, though I need to consider how that affects the rest of the chain—whether ball2 still gets pushed toward the cup or clumps together with ball1.

That penetration of 25mm is way bigger than the 20mm ball radius, which is bad since the balls would pass through each other. Getting penetration under control requires either much stiffer contacts (unresolvable at this timestep) or slower speeds and larger balls, so I'm considering dropping to radius 0.05m and v1=2 m/s, estimating ball3's speed after the chain reaction at roughly 0.87 m/s.

Checking the rim height needed for ball2 (~0.6 m/s, climb ~0.026m) against a 0.04m rim with 0.05m radius balls — it's tight and the ball might roll out of the cup. I'm also wondering if I should sidestep the bounce-collision complexity entirely and just rely on geometry/ramps, though the brief implies a specific chain where only the third ball ends up in the cup, so I need to be careful not to let all three fall in.

I'm working out stability constraints for MuJoCo's contact model: with ball radius 0.03m, v1=1.5 m/s, and spin at 500 rad/s, penetration depth comes out to about 3mm (10% of radius), and I'm checking whether the implicit semi-explicit Euler integration stays stable given the reference acceleration formula tied to the contact stiffness and damping.

Working through the math, effective stiffness simplifies so that ω ≈ 1/(tc·ζ) for d near dmax, with damping ratio staying at ζ. Testing values: ζ=0.2, tc=0.01 gives low restitution (~0.53), while ζ=0.1, tc=0.02 gives better restitution (~0.73) and satisfies MuJoCo's constraint that tc ≥ 2h. I'll go with solref="0.02 0.1" as a reasonable choice.

Checking penetration depth against velocity: even at v1=3, penetration stays around 6mm, about 20% of the 3cm radius — acceptable visually, and the stability condition ωh<1 holds. The default dmax of 0.95 with solimp width of 0.001 means stiffness ramps to max after just 1mm of penetration, which seems fine.

With e=0.73 instead of 0.85, I need to recompute the collision chain using these velocities — tracking how ball2 picks up most of the linear momentum while ball1 retains a small residual, accounting for rolling without spin.

I'm working through the chain reaction: ball2 slides before reaching rolling speed, checking whether it reaches ball3 before transitioning to pure rolling given the 0.34m gap, then computing the resulting velocities after ball2 hits ball3 — ball3 ends up rolling near 1.15 m/s while ball2 retains about 0.71 m/s with leftover spin.

Then I check if ball1 (now at 1.14 m/s) catches up to ball2 (0.71 m/s), working through that collision to get ball2 settling near 0.97 m/s and ball1 near 0.88 m/s, confirming no further catch-up since ball1 stays behind ball2. Finally I convert each ball's final speed into how high it climbs using the rolling energy relation, getting roughly 0.094 m, 0.067 m, and 0.055 m for balls 3, 2, and 1 respectively.

The margins between these climb heights look too thin given uncertainties like kink energy loss or contact softness, so I try bumping v1 up to 4 m/s and recompute: ball3 climbs about 0.168 m, ball2 about 0.119 m, which still leaves a narrow margin if the rim sits around 0.14 m. The real issue seems to be that ball1 catching up to ball2 re-energizes it too much, so I'm considering whether starting ball1 without spin (purely sliding) would reduce that re-energization, though I need to account for whether ball1 transitions to rolling before any collision occurs.

I try placing ball1 very close to ball2 so the collision happens while ball1 is still sliding with minimal spin — that way after impact ball1 retains roughly 0.135v, settling into rolling at 5/7 of that. I'm also considering whether putting all three balls close together could let a near-instantaneous chain collision happen while everything is still sliding and spin-free, which would let ball3 pick up close to 0.75v.

However, the phrase "rolled into" implies ball1 starts with spin, so I think about a compromise: ball1 rolls normally (with spin), but the gap between ball2 and ball3 is kept small so that second collision happens while ball2 is still sliding with little spin. Working through the numbers, ball1 ends up around 0.38v after its own post-collision spin-up, while ball2's resulting speed needs similar treatment to find the right ratio of final speeds.

Continuing the calculation, I check whether ball1 (rolling again at ~0.38v) catches up to ball2, running through successive collision outcomes to get approximate final speeds for all three balls, then converting those to climb heights with v=3 to see if they fit a 0.10 m rim constraint.

Trying r=0.04 with ω=400 instead gives penetration around 19% of radius with a half period of ~7.9 ms, roughly 4 simulation steps — acceptable. Ball3's second collision at 2.6 m/s yields a similarly small penetration, and I'm fine with potential discrepancies between simulated and target restitution. For ball-floor contact, the floor's solref should keep resting penetration minimal.

Friction between balls at 0.05 with ball1 spinning should produce only a small tangential force against ball2. Ball2 and ball3 aren't initially touching, just 0.02 m apart. Working out the layout with r=0.04: ball1 at x=0, ball2 at x=0.4, ball3 at x=0.50, so ball1 reaches the collision point around t=0.107 s. I'm setting the ramp start at x0=1.0 with a rim height of 0.10 m and a 15° angle, giving a ramp length of about 0.386 m, which works fine with the 0.04 m ball radius at the kink point.

Tracking ball3's exit velocity off the ramp at about 1.08 m/s after climbing the 0.10 m height, then working through the projectile motion as it leaves the ramp edge and falls toward the cup — computing the drop height of 0.09 m, the time of flight around 0.167 s, and a horizontal travel distance of roughly 0.17 m to see if it lands in the cup.

Now I'm verifying the cup geometry: interior length 0.30 m, back wall 0.25 m high, checking front wall height against the ramp's top height so the ball clears it. I'm also computing the ramp box's geometric center and surface positions using the 15° tilt to nail down exact collision coordinates.

I'm laying out the cup's walls and floor panels (front, back, sides, bottom) with their center positions and half-extents, confirming the interior width of 0.18 m comfortably fits the 0.08 m ball diameter, and now thinking about whether the ball will actually settle inside the cup after bouncing.

I figure the wall height (0.085 above the bottom) exceeds the ball radius, so the ball can't roll back out once it's inside — this applies similarly to ball2 at higher speed, which climbs slightly before rolling back and colliding with ball1. I'm setting ball1's initial keyframe velocity and angular velocity for rolling motion, along with the floor and ball contact solver parameters and friction values, and double-checking that ball1 rolls correctly against the floor without excessive sliding.

Checking the catch-up timing: ball1 accelerates from friction after the collision but shouldn't overtake ball2 before ball2 reaches ball3, since ball2 is moving much faster initially. This timing works out fine, so I'm ready to write the final answer.

