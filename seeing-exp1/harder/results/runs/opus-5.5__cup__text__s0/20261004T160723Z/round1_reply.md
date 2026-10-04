**Expected run**

1. **The ramp.** The deck is a box half 0.8459 m long, pitched 18.97°. Its high end sits at about (0, 1.0) on the leg, and its low end hangs in mid-air at about (1.6, 0.45).
2. **The roll.** The ball starts resting on the deck near the top. It rolls down with acceleration of about (5/7)·g·sin θ ≈ 2.28 m/s². It covers about 1.57 m in about 1.2 s.
3. **Leaving the ramp.** It leaves the low edge at about x = 1.63 m, center height z = 0.53 m. Its speed there is about 2.7 m/s, with v ≈ (2.53, −0.87) m/s. That speed is far above √(g·r), so it launches straight off the edge and does not curl around the corner.
4. **The flight.** As a projectile, it reaches the near wall's outer face (x ≈ 2.13) after about 0.2 s. By then its center is only about 0.16 m high. To clear the 0.30 m wall it would need to be above 0.36 m.
5. **The result.** The ball strikes the outside of the cup's near wall, rebounds, and ends up on the floor outside the cup. The cup is placed too far out for this launch.

**Fix**

I moved the near wall back so the ball clears it. The ball's center is still above 0.36 m until about x ≈ 1.9, so the wall now sits at x = 1.75. That leaves a gap of about 0.08 m below the ball at the crossing, and it does not intersect the ramp end at (1.6, 0.43–0.47).

I also lengthened the cup so there is room for the ball to settle:
- The cup spans x ∈ [1.75, 2.95].
- The ball lands on the base at about x ≈ 2.2, around t ≈ 1.4 s.
- The cup's contacts are critically damped, so it barely bounces.
- It rolls about 0.7 m toward the far wall, knocks against it, and rolling friction slows it to rest inside the cup well before 6 s.

```xml
<mujoco model="cup_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.8 0.005 0.002"/>
    <geom name="ramp_deck" type="box" pos="0.8000 0 0.7250" euler="0 18.9704 0" size="0.8459 0.2 0.02"/>
    <geom name="ramp_leg" type="box" pos="0.0000 0 0.5000" size="0.03 0.03 0.5000"/>
    <body name="ball" pos="0.1398 0 1.0376">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.2" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="cup" pos="2.3500 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.600 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.600 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.600 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.600 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.600 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down the 19-degree ramp and leaves its mid-air low end at about 2.7 m/s from about 0.53 m high. On its arc its center has dropped to about 0.16 m by the time it reaches the cup's near wall at x≈2.2 m, so it strikes the outside of the 0.30 m wall and ends up on the floor outside the cup.", "works": false, "problem": "The cup is placed too far from the ramp's end, so the ball's flight hits the outside of the near wall instead of clearing it and landing inside."}
```

---
thinking (summarized):

I'm working out the ramp deck geometry: with the center at (0.8, 0, 0.725) and an 18.97° pitch about the y-axis, I'm computing the cosine and sine of that angle to find where the two ends of the ramp sit by offsetting from the center along the rotated local x-axis.

I locate the high end near x=0, z=1.0 and the low end near x=1.6, z=0.45, then account for the ramp's thickness by shifting outward along the surface normal (sin θ, 0, cos θ) to get the top surface position. I verify the ball's given position (0.1398, 0, 1.0376) roughly matches a point on that surface at a parameter s≈-0.7256, and now I'm computing how far the ball has to roll to the end of the deck (distance 1.5715 m) and using rolling-sphere kinematics with acceleration g·sinθ·5/7 ≈ 2.278 m/s² to get the final speed squared.

Taking that speed (v≈2.676 m/s) at the ramp's edge, I find the launch position (x≈1.626, z≈0.5257) and break the velocity into horizontal and vertical components (vx≈2.531, vz≈-0.870) to treat the motion after leaving the ramp as a projectile. I'm now setting up the fall time equation to land the ball on the cup's base (around x=2.65, top at z=0.02, ball center at z=0.08), solving 0.4457 = 0.870t + 4.905t² for the time to impact.

Solving that gives t≈0.2255 and a horizontal distance landing at x≈2.197 — which is right at the near wall, so I need to check if the ball clears it. Checking the ball's height when it reaches the wall's near face (x≈2.13) at t≈0.199, I compute z≈0.158, which is well below the wall's top at 0.30 — meaning the ball would hit the wall rather than clear it.

So this setup fails: the ball hits the outer face of the near wall and bounces back, missing the cup. I need to rethink the cup placement or wall height so the trajectory actually clears the near wall and lands inside the cup's 0.9 m interior.

Checking the far wall is 2.65, giving about 0.45m clearance for the ball after landing with horizontal velocity ~2.53 m/s. With the critically-damped contact solver there's little bounce, so I'm estimating the ball will slide/roll toward the far wall, bounce back with reduced energy, and gradually settle due to rolling friction (condim 6, small rolling resistance) until it comes to rest in the cup.

Working through the timing: down the ramp takes about 1.175s, plus flight time lands around 1.4s, leaving 4.6s to settle with low-restitution impacts — plausible for the ball to stop by 6s given the rolling friction deceleration. I'm considering deepening the cup geometry, maybe moving the far wall or cup center further out to reduce bounce-back.

Checking clearances near the ramp edge: the ball's trajectory stays well above the wall height as it crosses, and even with the slight downward bend from rolling over the edge corner, there's enough margin before it reaches the wall position.

Finishing cup dimensions...

