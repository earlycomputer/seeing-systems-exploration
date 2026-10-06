**What happens in the run:** The ball leaves the floor at 3.18 m/s along and 8.50 m/s up. It peaks at 3.79 m at 0.87 s. It comes down through the rim at about 1.26 s: at 1.25 s its centre is at (3.97, 3.08), almost exactly the rim centre at x = 4 m, z = 3.05 m. It touches neither the rim nor the backboard.

The checker reports the pass at 1.48 s, 1 cm from the centre, which is later than the flight data shows. It may be timing when the ball is fully clear below the rim.

After falling through, the ball hits the pole and then the pole base. It bounces back onto the floor and rolls back past the launch point, still moving at 2.23 m/s at 6 s. That roll-away is outside what the brief asks for.

```json
{"what_happens": "A 24 cm, 620 g hollow lively ball is launched from rest on the floor at 3.18 m/s along and 8.50 m/s up, peaks at 3.79 m, and falls cleanly through the rim centre at 3.05 m, 4 m away, about 1.26 s in, touching neither rim nor backboard. It then strikes the hoop's pole and base, bounces back to the floor and rolls back past the launch point, still moving at the end.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm double-checking the timing discrepancy — my calculation puts the ball passing through the rim center around 1.25-1.26s at position (3.97, 3.08), close to the rim center at x=4, z=3.05, while the checker reports 1.48s. That gap is odd, but the position check at 1.25s still confirms the ball passes near the rim center within a small margin.

No rim or backboard touches are listed, so the shot seems clean. The ball later hits the pole, rolls back across the floor, and settles far off at x=-6.26 while still moving — presumably the floor plane extends infinitely so that's not an issue. Overall this looks like a valid setup: ball launched from the floor, drops through a 3.05m hoop from 4m away, with regulation size and weight — I'm satisfied this works.

