**Expected behaviour of the current scene:**

1. **Start.** The ball starts about 1 mm above the high end of the 19° deck. It settles onto the deck at once and starts rolling.
2. **Down the ramp.** It rolls about 1.57 m. Rolling resistance (combined coefficient 0.004) leaves a net acceleration of about 1.84 m/s². It reaches the raised lip, at about z ≈ 0.53 for the ball centre, at about 2.4 m/s after roughly 1.3 s.
3. **Launch.** It leaves the lip almost immediately. Since v²/r ≫ g, it barely rolls over the corner. Its velocity is about 2.27 m/s forward and 0.78 m/s downward.
4. **Over the near wall.** The wall spans x = 1.74–1.76 and is 0.20 m tall. The ball's bottom passes over it at about z ≈ 0.36–0.44, a clearance of about 16 cm. Even at 2.0 m/s the clearance is still about 15 cm.
5. **Landing.** About 0.23 s after launch it lands on the cup base at x ≈ 2.15–2.2. The base runs from x = 1.76 to 2.99, so this is well inside.
   - The impact is nearly critically damped, so there is little bounce.
   - The base is 2 cm thick and the ball moves about 6 mm per step, so there is no risk of tunnelling.
6. **Far wall.** The ball keeps rolling at about 2.3 m/s and hits the inner face of the far wall at x = 2.99 at about t ≈ 1.9 s.
   - The contact is at z ≈ 0.08, well below the 0.20 m wall top.
   - The rebound is small.
   - Topspin against the wall can lift the ball at most about 0.68 m/s, a hop of about 2–3 cm, so it cannot clear the wall.
7. **Settling.** Friction with the floor and wall resyncs its spin. Rolling resistance (about 0.44 m/s²) removes the remaining few tenths of a m/s within about a second. The ball comes to rest inside the cup well before 6 s.

The cup is fixed to the world and its side walls at y = ±0.3 are well clear of the ball's straight path along y = 0.

```json
{"what_happens": "The ball rolls down the 19-degree ramp, leaves the raised lip at about 2.4 m/s and clears the 0.20 m near wall of the cup by about 16 cm. It lands on the cup base near x=2.15 with little bounce, rolls into the far wall, rebounds slightly and settles at rest inside the cup by about t=3-4 s.", "works": true, "problem": ""}
```

---
thinking (summarized):

Rechecking the scene geometry, I'm tracking when the ball's leading edge reaches the near wall and whether its height clears the wall at that point, finding the ball is still well above the wall height when it arrives.

Moving forward, the ball lands within the base bounds, rolls toward the far wall at modest speed, and its height there also stays below wall height, so it won't escape. I'm also checking that the soft contact physics won't cause tunneling through the thin base at the ball's impact speed, and confirming the cup geometry is static and correctly positioned so the ball interacts with the base rather than the floor.

Given the total flight and roll timing, the far-wall impact happens around 1.9 seconds in, leaving plenty of time within 6 seconds for friction and rolling resistance to damp out the remaining speed and spin, settling the ball with minor back-and-forth bouncing.

Checking the geometry details: the ramp's lateral width, the cup walls at y=±0.3, and the ball's small initial drop above the deck all look consistent, and the ramp leg placement under the high end doesn't cause interference. The setup checks out.

