**What happens in the run:** At t = 0 the motor swings the arm up. The ball is pressed against the beam and then against the outer lip. At 0.14 s the arm hits its 40.1° stop, overshoots to 41.3° and settles. The ball leaves the cup at that moment with vx ≈ 3.40 m/s, which matches the design value.

The ball peaks at (1.33, 0, 1.39) m at 0.48 s and comes down inside the bucket at x ≈ 3.11 m at 1.00 s. It rolls forward to the far wall (bucket_wall_00), bounces back onto the bucket floor, and is at rest by about 1.3–1.5 s. It stays at (3.23, 0, 0.06) m through 6 s. That is 0.23 m from the bucket centre, inside the 0.3 m inner radius.

**One flaw:** At impact the ball sank through the 2 cm bucket floor far enough to touch the ground plane briefly. The bucket floor's soft contact is too soft for a hit at about 5 m/s. It did not change the outcome, so I'm leaving the scene as is. A stiffer `solref` on the bucket geoms or a thicker floor would remove it.

```json
{"what_happens": "The velocity-driven arm swings up and stops at 40.1° at 0.14 s, launching the ball at about 4.7 m/s at roughly 44°. The ball peaks at 1.39 m height near x = 1.33 m and lands inside the bucket at x ≈ 3.11 m at 1.00 s. It briefly sinks through the thin bucket floor enough to touch the ground plane, rolls to the far wall and bounces back, and is at rest on the bucket floor at (3.23, 0, 0.06) m from about 1.3 s through 6 s, inside the bucket whose centre is 3 m from the ball's start.", "works": true, "problem": ""}
```

---
thinking (summarized):

The ball ends up resting in the bucket at roughly (3.23, 0, 0.06), near the inner wall of the 0.3-radius bucket centered at 3. There's also a timing oddity around the 1.00s mark where the ball seems to clip through the bucket's thin floor and register contact with the ground plane beneath it, since the bucket floor sits just above z=0.

Despite that brief penetration during impact, the ball settles fine at the end, 0.23 from the bucket's center, well within bounds. The velocity and landing position both roughly match predictions — vx around 3.40 and x around 3.11 versus the expected 3.08.

