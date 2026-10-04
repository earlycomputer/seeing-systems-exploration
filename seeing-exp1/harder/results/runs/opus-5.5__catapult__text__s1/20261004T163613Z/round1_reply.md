**What I expect to happen**

1. The hinge spring (stiffness 2, springref 150°) gives about 5.2 N·m at 0°. Gravity on the arm and ball gives about 3.1 N·m against it, so the arm swings up until it hits the 55° stop.
2. Spring work over 0.96 rad is about 4.1 J. Lifting the arm, cup and ball takes about 2.6 J. That leaves about 1.5 J of kinetic energy, and the arm's inertia about the hinge is about 0.27 kg·m².
3. So ω is about 3.4 rad/s and the ball leaves at about 3.1 m/s. It launches 35° above horizontal from about (x = −0.46, z = 1.2).
4. It falls past the bucket's 0.4 m wall height at x ≈ 1.1 m. The bucket's near wall is at x = 1.6, so the ball lands on the floor short of the bucket.
5. The bucket centre is also 2.92 m from the ball start, not 3 m.

**Fix**

- I moved the bucket to x = 2.08, so its centre is 3.00 m from the ball.
- I raised the hinge stiffness to 2.65. Spring work becomes about 5.4 J, kinetic energy about 2.85 J, and launch speed about 4.3 m/s at 35°.
- The ball should then cross the wall-top height near x ≈ 2.05, inside the bucket opening (x = 1.69 to 2.47).
- With about 10% energy loss it still lands near x ≈ 1.85, which is still inside.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 55" stiffness="2.65" springref="150" damping="0.05" armature="0.01"/>
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
{"what_happens": "The spring swings the arm up to its 55° stop and releases the ball at about 3.1 m/s at 35° from about 1.2 m height; the ball comes down at x ≈ 1.1 m, short of the bucket whose near wall is at 1.6 m (and the bucket centre is 2.92 m, not 3 m, from the ball start).", "works": false, "problem": "The spring is too weak, so the ball lands on the floor about half a metre short of the bucket, which is also placed 2.92 m rather than 3 m from the ball."}
```

---
thinking (summarized):

The ball starts at x=-0.92 and the bucket is at x=2.0, giving a distance of about 2.92 meters, close enough to the 3 m target within tolerance. Now I'm working out the arm dynamics — the hinge rotates about the y-axis from 0 to 55 degrees with a spring reference at 150 degrees, and I need to figure out how a point on the arm extending in -x moves as it rotates through that angle.

Computing the torques: the spring provides about 5.24 Nm at angle zero, while gravity from the beam, cup, and ball totals roughly 3.1 Nm, giving a net positive torque of around 2.1 Nm that drives the arm upward until it hits the 55-degree range limit. I'm then calculating the energy balance — the spring does about 4.10 J of work over that range, while lifting the beam, cup, and ball against gravity costs roughly 1.2 J, 0.23 J, and a similar amount for the ball, leaving excess energy to convert into kinetic energy for the launch.

Summing the moments of inertia for the beam, cup, back plate, armature, and ball gives a total around 0.265 kg·m², which I use with the leftover energy of about 1.5 J to get an angular velocity of roughly 3.37 rad/s at release.

This converts to a ball speed near 3.1 m/s, launched tangent to its circular path. Working out the velocity direction at θ=55°, the ball leaves at about 35° above horizontal, and I'm now computing the exact launch height by tracking the ball's rotated position relative to the hinge.

I'm tracking the trajectory from launch point to the bucket, computing fall time to reach the wall height, then getting horizontal distance — it lands around x=1.13 m, short of the bucket's wall at x=1.6, so it would end up hitting the floor rather than going in.

Let me reconsider the geometry: the bucket center should be at x=2.08 given the actual separation distance of 2.92 m, not 3. I need a higher launch speed to reach there, so I'm setting up the projectile equation using a 35° angle from the release point (-0.455, 1.2) to the target (2.08, 0.3), solving for the required speed v using the standard trajectory height-drop formula.

I work through the trig and get v≈4.19 m/s, which translates to arm angular speed ω≈4.53 rad/s and kinetic energy ≈2.72 J. Adding estimated losses, I figure the spring needs to supply roughly 5.3 J, implying a stiffness k≈2.58, though I'm wary since the model simplifies away effects like the ball possibly losing contact early or sliding — so I want to sanity-check how forgiving the bucket's 0.78 m width is to these uncertainties.

Checking whether the ball stays seated through the swing: the centripetal pull toward the hinge is handled by the back wall pushing inward, while the cup floor manages tangential acceleration, so the geometry works out fine even as the arm decelerates hard at the limit stop.

Damping at 0.05 is small enough that losses are negligible over the relevant timescale. I need to confirm MuJoCo converts both ref and springref to radians when angle is set to degrees for hinge joints — I believe both are converted. With that settled, I'm testing stiffness at 2.7 against the bucket position at 2.08, recomputing spring work and kinetic energy from there.

Working through the trajectory equations, I find the landing point lands farther than the bucket — solving for where z=0.3 gives x≈2.24, which falls within range.

Checking the wall-top clearance at z=0.4 confirms x≈2.17 clears the near wall at 1.68 but stays short of the far wall at 2.48, which works. I try k=2.6 as a candidate spring constant, recomputing kinetic energy, angular velocity, and launch speed, then solve the landing equation again for z=0.4 to see where it lands.

Testing k=2.6 more precisely gives a landing point around x=2.02, well centered between the walls. Accounting for possible energy losses (10% KE loss) still keeps the landing inside the acceptable range once the ball's radius is factored in, so I settle on k=2.65 for a bit of safety margin, and note the contact damping should be set low-bounce with critical damping so the ball doesn't ricochet out given its ~4 m/s descent speed.

Checking initial ball placement: the cup floor's top sits at 0.43, and the ball's center at 0.4895 puts its bottom at 0.4295, a tiny overlap of 0.0005 which is acceptable. Everything checks out, so I'm ready to write the final answer.

