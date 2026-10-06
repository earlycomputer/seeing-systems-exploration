The ball leaves the floor at x = 0 moving at (vx 2.87, vz 8.95) m/s. It peaks at 4.19 m at 0.91 s, about 2.6 m out, and then comes down on a steep path. At about 1.40 s its centre crosses the rim plane at z = 3.05 m, about x = 4.0 m, inside the ring. The 1.25 s and 1.50 s samples (3.58, 3.64) and (4.29, 2.50) lie on that parabola. The closest it gets to the rim is 0.07 m from rim7, the shooter-side edge, at 1.37 s, and it never touches any rim geom.

It passes under the backboard without contact and lands at 1.83 s. It bounces once to 0.40 m, taps the support pole at 2.30 s, settles on the floor, and rolls slowly back toward the shooter. It is still moving at 0.47 m/s at the end.

```json
{"what_happens": "The ball launches from the floor at x=0, peaks at 4.19 m at 0.91 s, and descends steeply through the rim (centre at 3.05 m, 4 m away) at about 1.40 s, clearing the rim by 0.07 m without touching it. It then passes under the backboard, lands at 1.83 s, bounces into the support pole, and rolls back slowly along the floor until the run ends.", "works": true, "problem": ""}
```

---
thinking (summarized):

Checking clearance at 1.37s confirms the ball passes 0.2m from the tube center as predicted, so it clears the rim without touching. Around 1.40s the ball sits at x≈4.0, z=3.05, comfortably inside the rim, and the surrounding timestamps confirm it follows the parabola cleanly through the hoop before landing near 1.83s.

The bounce at 1.83s drops vx from 2.87 to 1.64 due to friction, which checks out, and after 2.5s the ball settles into a constant 0.47 m/s slide with no vertical velocity — consistent with rolling given the small rolling friction coefficient. Everything matches the brief: the ball launches from the floor and drops through the hoop at 3.05m height, 4m away.

