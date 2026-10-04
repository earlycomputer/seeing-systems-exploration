**Expected behaviour of my previous corrected scene:**

1. **Down the ramp.** The ball rolls about 1.57 m down the deck. Rolling resistance acts on it: the third friction value combines by max to 0.004. That gives about 1.84 m/s² of acceleration along the slope. It reaches the lip at about 2.4 m/s.
2. **Launch.** It leaves the lip at about (1.63, 0.53), moving forward at about 2.27 m/s and downward at about 0.78 m/s. It barely pivots over the corner, since v²/r ≫ g.
3. **Over the near wall.** The wall is at x = 1.8, 0.30 m tall. The ball's trailing edge passes it with its bottom at only about z ≈ 0.325. That is a margin of about 2.5 cm. If contact softness or slip cost even 10–15 % of speed, the ball would clip the wall top and could bounce out.
4. **Inside the cup.** If it clears, it lands at about x ≈ 2.15. The impact is nearly critically damped, so it barely bounces. It rolls into the far wall. Topspin against the wall gives only about a 2 cm hop, so it settles inside.

The margin is too thin to call reliable.

**Fix:**
- Lower the cup walls to 0.20 m, which is still far higher than any hop the ball can make.
- Move the near wall to x = 1.75, centring the cup at x = 2.375 with half-length 0.625.

The ball's bottom now clears the near wall by about 16 cm. It lands near x ≈ 2.15–2.2 on the base, well before the far wall at x = 3.0. The ramp's lowest corner is at x ≈ 1.59, so it doesn't touch the cup.

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
    <body name="cup" pos="2.3750 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.625 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.625 0 0.100" size="0.01 0.300 0.100"/>
      <geom name="cup_far" type="box" pos="0.625 0 0.100" size="0.01 0.300 0.100"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.100" size="0.625 0.01 0.100"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.100" size="0.625 0.01 0.100"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down the ramp, reaching about 2.4 m/s at the raised lip, then flies off. In the previous version its bottom clears the 0.30 m near wall at x=1.8 by only about 2.5 cm, so a modest speed loss would make it clip the wall top. If it clears, it lands near x=2.15 inside the cup, rolls into the far wall and settles.", "works": false, "problem": "The ball clears the cup's 0.30 m near wall by only about 2.5 cm, so small speed losses from contact softness or slip would make it clip the wall instead of landing reliably in the cup."}
```

---
thinking (summarized):

Double-checking the corrected scene geometry: the ramp's upper end sits near x≈1.6, the cup is centered around x=1.8 spanning roughly 1.79–1.81 with height 0.3, and I'm computing the exact corner positions of the ramp deck's lower edge using the rotation trig to confirm the top and bottom corners land near x=1.6065 and x=1.5.

Tracking the ball's trajectory off the ramp, I verify its leading and trailing edges clear the cup rim at x=1.79–1.81 with sufficient height margin, then solve the quadratic for when it descends into the cup basin, landing at x≈2.17 well within the cup's 1.81–2.99 span. The impact speed is around 3.07 m/s vertically, but since the solver reference damps bounce heavily, the ball should settle with minimal rebound.

After landing, I'm checking whether its forward roll (2.38 m/s with matching spin) could carry it into the far wall 0.8 m away, and whether the combined contact stiffness there is soft enough to absorb the hit rather than bounce it over the 0.3 m rim—considering how topspin interacts with wall friction at the contact point.

So friction acts upward on the ball at the wall, meaning topspin lets it climb up. I'm working out the normal impulse from the bounce, then checking how much tangential impulse friction can supply before slip stops, using the sphere's effective tangential mass factor to find the impulse needed to zero out the slip speed.

That gives a small upward velocity on rebound, so the hop height is tiny, well within the wall's height — the ball stays in the cup. Afterward it rebounds slowly, rolls with rolling friction decelerating it, and I'm tallying up the elapsed time so far against the 6-second window.

Recomputing the ramp more carefully: with gravity component along the slope minus rolling resistance, the ramp distance is actually closer to 1.57 m rather than my earlier estimate, giving an exit velocity near 2.40 m/s and a ramp transit time around 1.31 seconds.

Rechecking clearance with this corrected velocity: the ball's trailing edge passes the deck corner with only about a 2.5 cm margin above the 0.30 threshold, which is tighter than I'd like. There's also the physical effect of the ball pivoting over the edge corner, which adds extra downward velocity right before launch, making the real trajectory a bit lower and steeper than my idealized calculation—so this margin carries real risk. I also need to double check whether 0.004 is truly the correct rolling resistance coefficient, since MuJoCo combines friction properties by taking the max across geoms, and the ball and surface have different default friction triples for sliding and torsional components.

Rolling resistance saturates fully at the limit, so that holds. Checking the edge-pivot effect at the ramp's trailing corner: since v²/r is far greater than g, the ball separates from the edge almost immediately, so that's negligible. The 2.5 cm clearance margin works but feels tighter than ideal, so I'm considering shifting the cup further out to improve safety margin, checking the geometry at the ramp's bottom corner and ball position.

Testing with a 10-15% speed reduction shows the margin could shrink to just 1cm or even clip the wall entirely — too risky given possible energy loss from contact damping. I'll fix this by lowering the wall height to 0.2 and repositioning it closer at 1.75, then redefine the cup geometry with a wider half-length of 0.625 centered at 2.375.

Checking clearances: the ramp's bottom corner sits well clear of the repositioned wall, and even a worst-case landing with no rolling resistance (max speed, x≈2.2) still falls safely within the cup's bounds of 1.76–2.99.

