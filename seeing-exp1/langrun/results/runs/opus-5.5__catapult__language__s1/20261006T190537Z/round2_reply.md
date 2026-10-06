## What happens in the run

- **Swing:** the spring swings the arm from 0° to its 40° stop by 0.14 s, turning at 521°/s.
- **Launch:** the ball leaves the scoop at about 4.3 m/s at roughly 33° above the horizontal.
- **Flight:** it peaks at 1.21 m at 0.38 s, at x = 0.52 m.
- **Landing:** at 0.87 s it comes down on `bucket_base` at about x = 2.40 m. That is just past the bucket's centre at x = 2.43 m, which is 3 m from the ball's start at x = −0.57 m. It clears the near wall without touching it.
- **Settling:** the ball makes a few small bounces along the base and taps `bucket_far_wall` at 1.09 s. It comes to rest on the base at (2.72, 0, 0.05) m by 1.31 s, still inside the bucket, and stays there until 6 s.

```json
{"what_happens": "The spring swings the catapult arm to its 40° stop at 0.14 s (521°/s), throwing the ball at about 4.3 m/s. The ball peaks at 1.21 m, clears the near wall and lands on the bucket's base at x ≈ 2.40 m (bucket centre 2.43 m, 3 m from the ball's start). It bounces lightly, taps the far wall and comes to rest on the bucket base at x ≈ 2.72 m, staying there to the end.", "works": true, "problem": ""}
```

---
thinking (summarized):

The ball lands in the bucket at 0.87s around x≈2.40, inside the bucket's walls, then bounces off the far wall and settles near x=2.72, resting against the inner far wall on the base.

