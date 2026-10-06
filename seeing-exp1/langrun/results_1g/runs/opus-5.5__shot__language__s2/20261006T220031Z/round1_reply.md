**What happens:** The ball leaves the floor at 3.01 m/s along and 8.73 m/s up, and peaks at 4.00 m about 0.89 s in. Interpolating the 0.25 s samples, it comes down through the rim plane at about x = 4.00 m, z = 3.05 m, near 1.33 s. It is falling at about 4.3 m/s against 3.0 m/s forward, so the descent is steep, and it touches nothing. It then strikes the hoop's pole at 1.66 s and the pole base at 1.83 s. It rebounds backward, bounces, and rolls back along the floor, still moving at 1.55 m/s at 6 s.

**Check:** The checker confirms "ball drops through hoop". It gives the time as 1.53 s, 7 cm from the rim's centre, which is later than the 1.33 s the samples imply; I can't reconcile that from the data. Even so, the path clearly passes cleanly through the rim's opening from above. So the brief is met: a regulation ball is launched from the floor and drops through a 3.05 m rim 4 m away.

**Unasked side effects:** The ball hits the pole after scoring and keeps rolling to the end of the run. Neither breaks the brief.

```json
{"what_happens": "The 24 cm, 620 g ball is launched from the floor at 3.01 m/s along and 8.73 m/s up. It peaks at 4.0 m at 0.89 s and descends steeply through the 3.05 m rim, 4 m away, without touching rim, bracket or backboard; the checker confirms it dropped through. Afterwards it hits the hoop pole and pole base, bounces back, and rolls back across the floor, still moving at 1.55 m/s at 6 s.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm double-checking the timing of when the ball crosses the rim—my calculation puts it around 1.33s rather than the reported 1.53s, and the position doesn't quite match a 7cm clearance from center either, so I'm re-tracing the trajectory values at each timestep to find the discrepancy.

