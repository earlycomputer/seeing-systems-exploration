**What happens:** The ball rolls down the ramp. The ramp ends in mid-air at about x = 1.6 m, z = 0.45 m, so the ball flies off the lip and falls toward the floor. Under these numbers its flight carries it to about x ≈ 2.2 m. That is right where the cup's near wall stands. The wall's top is at 0.3 m, and the ball arrives below that height. In the picture the ball's track runs along the floor up to the outside of the cup's near wall and stops there. It never gets inside the cup.

**Fix:** Move the cup toward the ramp so the ball's arc clears the near wall and lands on the cup floor.

- The ball leaves the ramp at about x ≈ 1.63, z ≈ 0.53, moving at about 2.5 m/s horizontally.
- It would pass over a near wall at x = 1.75 with roughly 0.15 m to spare.
- It would touch down near x ≈ 2.2, the middle of the cup floor.
- It should then roll into the far wall and come to rest inside. The ball's contact is critically damped, so it should bounce very little.

```json
{"what_happens": "The ball rolls down the ramp, leaves its end in mid-air at about x=1.6 m, and falls. It lands at the base of the cup's near wall, outside the cup, and stops against the outside of that wall. It never enters the cup.", "works": false, "problem": "The cup sits too far from the ramp, so the ball's fall carries it into the outside of the near wall instead of over it into the cup."}
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
    <body name="cup" pos="2.2000 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.450 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.450 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.450 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

Checking the ramp geometry: centered at x=0.8, z=0.725 with an 18.97° pitch about y, the positive rotation tilts the high end toward x=0 at z≈1.0, while the low end extends to x=1.6 at z≈0.45 — meaning the ramp's low end doesn't actually reach the ground at z=0, it ends suspended in mid-air.

I'm trying to figure out the pixel-to-meter mapping for the rendered image, using scale factor 33.31 px/m with x offset 0.38, to locate where the ball ends up relative to the cup (spanning x=2.2 to 3.1) and ramp end (x=1.6). Working through the pixel positions, I estimate the last visible ball is around x≈1.8, z≈0.17, suggesting it fell off the end of the ramp rather than landing in the cup.

Calculating the rolling dynamics: after a 0.55m drop along the ramp, the ball's speed should be about 2.77 m/s via energy conservation for rolling motion, decomposing into roughly 2.62 m/s horizontal and 0.9 m/s vertical components as it leaves the ramp and becomes a projectile, eventually landing on the floor and rolling across to strike the cup's near wall before stopping short of entering it.

Computing the ball's exit velocity off the ramp (~2.67 m/s rolling speed, decomposed to vx=2.53, vz=-0.87), I'm checking whether the center clears the near wall's 0.3 height by the time it reaches that x position—working out the fall time of about 0.118s to drop from 0.526 to 0.36.

I'm then tracking where it lands on the cup's base, solving the quadratic for fall time (~0.226s) giving a landing x around 2.20. After that it should bounce or roll forward, strike the far wall, and settle—so I need to figure out if rolling friction (using a rolling coefficient around 0.004) brings it to rest within the 6 second window.

Deceleration from rolling friction works out to roughly 0.46 m/s², meaning it would take close to 5 seconds to stop from 2.5 m/s, and the wall collisions should be fairly inelastic given the critically-damped solref settings. This feels fragile though, so I'm considering redesigning the setup—maybe lowering the ramp height, repositioning the cup directly in the ball's path, increasing the rolling friction, or making the cup walls taller so the ball settles inside more reliably. An alternative is placing the cup closer to the wall, spanning roughly x=1.75 to 2.65.

Tracing through the physics again: the ball lands near x=2.2 with about 2.4 m/s horizontal speed after the vertical component is absorbed, then hits the far wall at x=2.65. Since the wall height (0.3) comfortably exceeds the ball's center height (0.08), it shouldn't hop over, and the critically-damped contact should prevent much bounce-back, letting the ball settle near the wall. I'm also double-checking the ball's starting position relative to the ramp to make sure the initial setup is consistent.

Checking clearance during the fall confirms the ball clears the wall edge comfortably. Lower launch speeds also land safely within the floor bounds between the wall and far edge. I'll keep the cup geometry as is, with the wall height at 0.3 and position at 2.2, trusting friction settling to bring it to rest within the time window.

