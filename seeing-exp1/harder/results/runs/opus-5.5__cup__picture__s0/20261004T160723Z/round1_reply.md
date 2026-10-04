**What happens:** The ball rolls down the ramp and leaves its low end at about x = 1.6 m, z ≈ 0.5 m, moving at roughly 2.6 m/s. It drops to the floor before reaching the cup, whose near wall is at x ≈ 2.2 m. The plan view shows a streak running from the ramp end up to that near wall. The last copy of the ball sits on the floor at about x ≈ 1.7 m, outside the cup. The ball hit the outside of the near wall and rolled back, so it never ends up in the cup.

**Fix:**
- Move the cup so its near wall sits just under the ramp's low end, at x ≈ 1.55 m. The ramp's underside there is at z ≈ 0.45 m, above the 0.3 m wall top, so the ball clears the wall and lands inside at about x ≈ 2.2 m.
- Lengthen the cup to 1.1 m so the landing point falls well within it.
- Give the cup floor higher rolling friction (0.02). The ball should then stop well within the 6 s run, either against the far wall or on the floor.

```json
{"what_happens": "The ball rolls down the ramp, flies off its low end near x=1.6 m, lands on the floor short of the cup, hits the outside of the cup's near wall and rolls back to rest on the floor around x=1.7 m, outside the cup.", "works": false, "problem": "The cup is too far from the ramp end: the ball lands on the floor before the cup and hits the outside of its near wall instead of falling in."}
```

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
    <body name="cup" pos="2.1000 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.550 0.300 0.01" friction="0.8 0.01 0.02"/>
      <geom name="cup_near" type="box" pos="-0.550 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.550 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.550 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.550 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm working out the ramp deck's tilted geometry, checking how the rotation about the y-axis shifts the high and low ends of the slope based on the center position and pitch angle.

Now I'm calculating the ball's trajectory as it leaves the ramp: using energy conservation for a rolling sphere to get its launch speed, decomposing velocity along the slope direction, then solving the projectile motion to find where it lands relative to the cup's walls. I'm comparing that landing position against the cup's wall height and the pixel coordinates visible in the image to see whether the ball would clip the near wall or land inside.

So the ball seems to bounce off the cup wall rather than landing in it, meaning the current setup fails. I need to reposition the cup or ramp so the ball actually falls inside — maybe lowering the ramp's exit point over the cup's near wall, accounting for the ball's exit velocity and position so it clears the wall height and drops in.

The wall bounces will have low restitution and absorb energy, but even so, rolling friction alone would take roughly 5-6 seconds to stop the ball from 2.6 m/s, which cuts it close against the 6s window. I should probably just reduce the initial speed to be safe.

Options come to mind: start the ball lower on the ramp to cut v² roughly in half, or bump the cup floor's rolling friction coefficient to something like 0.02, which would give a decel around 2.3 m/s² and stop the ball in about a second — combined with wall collisions and critical damping to keep bounce minimal. I'm also considering making the cup narrower to help trap the ball faster.

Now I'm working out the actual geometry: placing the cup centered around x=2.1 with walls at roughly 1.55 and 2.65, checking the ramp's bottom surface height near the near wall to confirm clearance for the ball, and tracing where the ball leaves the ramp and lands inside the cup before rolling toward the far wall at a few meters per second.

I'll add friction to the cup base with condim 6, matching the ball's contact dimensions since mixing takes the max.

