I expect the scene to do what the brief asks. This is based on rechecking the geometry and trajectory by hand, not on a run or a measurement.

**Expected sequence:**
- **Launch.** The ball starts resting just above the floor at x = 0. It leaves at about 9.1 m/s, about 69° up.
- **Flight.** It peaks near 3.8 m around x ≈ 2.8 m. It then comes down at about 50° below horizontal.
- **Through the hoop.** At about t = 1.25 s it passes through the rim plane at x ≈ 4 m, z = 3.05 m.
  - The closest approach of the curved path to the front and back rim tube is about 0.18 m. The ball radius plus tube radius is 0.127 m, so roughly 5 cm of clearance is left on each side.
  - The 1 cm extra vertical speed should cancel the ~1 cm low drift from the integrator.
- **Under the backboard.** Below the rim the ball moves forward about 0.12 m while dropping 0.15 m. It stays at least about 9 cm clear of the backboard's bottom edge and the rim bracket.
- **Landing.** It lands near x ≈ 5.5 m at about t = 1.7 s. It bounces a few times and may roll or bounce into the pole at x = 7 m before the 6 s run ends. This happens after the shot, so it doesn't affect the brief.

```json
{"what_happens": "The ball leaves the floor at x=0 at ~9.1 m/s, ~69 deg, peaks near 3.8 m, and descends at ~50 deg cleanly through the 3.05 m rim at x=4 m about 1.25 s after launch (~5 cm clearance to the rim tube on both sides), passes beneath the backboard, lands near x=5.5 m and bounces away toward the stanchion.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm double-checking the ball's trajectory against the backboard position, calculating where the ball's center would be when its front edge first reaches the board's face at x=4.381.

Checking the other candidate crossing points against the bracket corner, the clearances stay safely above 0.119, so the ball avoids the rim and arm. The rebound height after bouncing looks modest enough (maybe under a meter) that it won't reach the arm at z~3.34, and the ball should be clear of that region by the time it moves past x=5.5. Now I need to check clearance against the pole at x=7, radius 0.1.

I'm also double-checking the direction of the numerical drift from MuJoCo's semi-implicit Euler integration, confirming the velocity-then-position update lowers z by roughly g·dt·t/2, which matches my earlier compensation. Then I'm verifying the curvature effect near the front rim crossing — since the parabola is concave down, the true trajectory should dip slightly below the straight tangent line, so I'm comparing the tangent line's z-value against the actual parabola's z-value at x=3.763 to see how much separation that gives at the rim.

Now I'm minimizing the distance between the front rim point and the parabolic path by testing several parameter values near t=-0.03 to -0.05, computing the squared distance for each and narrowing in on where the closest approach occurs.

Since the vertices at φ=0 and 180 are full-radius polygon points, the clearance works out to about 0.05, which is fine. Launching from the floor also checks out, and the whole thing completes within 6 seconds.

