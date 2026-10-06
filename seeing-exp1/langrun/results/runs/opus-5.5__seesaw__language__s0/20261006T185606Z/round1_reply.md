**What happens in the run:**
- The seesaw starts level on its 0° stop, with the 100 g ball resting on its near end at a height of 0.35 m.
- The 1 kg weight is released from 2 m. It falls freely and lands on the far end at 0.58 s, moving at about 5 m/s.
- The seesaw snaps round and hits its 20° stop at 0.61 s, turning at 620°/s. It overshoots briefly to 24.9° because the stop is soft.
- At 0.62 s the ball leaves the seesaw at about 4.5 m/s, mostly upward.
- The ball peaks at 2.21 m at 1.20 s. That is about 1.86 m above where it started, well over the 50 cm the brief asks for.
- It then falls back, glances off the seesaw, lands on the floor and rolls away.
- The weight bounces off onto the floor and slides off along x.

So the brief is met by a wide margin.

```json
{"what_happens": "The 1 kg weight falls from 2 m onto the far end of the level seesaw at 0.58 s; the seesaw snaps to its 20° stop and throws the 100 g ball from the near end, which rises from 0.35 m to a peak of 2.21 m at 1.20 s (about 1.86 m higher) before falling back, glancing off the seesaw and rolling away on the floor.", "works": true, "problem": ""}
```

---
thinking (summarized):

The ball drops from 0.35 to a rise of 1.86m at the top, which checks out. The seesaw is a bit odd though — it overshoots to 24.9° against its soft limit and keeps drifting slowly back through 13-19°, which seems strange for a symmetric setup at rest, but it's probably just limit softness causing that slow return.

And now the ball hits the seesaw again and rolls away — good, that's satisfying.

