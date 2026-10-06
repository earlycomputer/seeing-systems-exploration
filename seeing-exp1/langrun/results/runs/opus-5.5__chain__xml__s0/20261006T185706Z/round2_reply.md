The scene now does what the brief says.

1. **Ball1 hits ball2.** Ball1 starts rolling at 3 m/s and strikes ball2 at 0.11 s.
2. **Ball2 hits ball3.** About 0.01 s later ball2 strikes ball3, which rolls off at roughly 1.6 m/s.
3. **Ball3 lands in the cup.** It climbs the ramp from 0.42 s and leaves the top at 0.72 s. It drops onto cup_bottom at 0.88 s, bounces once off cup_back, and settles inside the cup by about 2.6 s. It is still there at 6 s.
4. **The other balls stay out.** Ball2 rolls partway up the ramp twice and rolls back down. Ball1 never reaches the ramp, and it ends rolling slowly away in −x.

```json
{"what_happens": "ball1, set rolling at 3 m/s, hits ball2 at 0.11 s; ball2 immediately hits ball3, which rolls at about 1.6 m/s up the ramp, leaves its top at 0.72 s, drops onto cup_bottom at 0.88 s, bounces off cup_back and settles inside the cup, where it stays to the end. ball2 rolls partway up the ramp twice and rolls back down; ball1 never reaches the ramp and ends rolling slowly away in -x.", "works": true, "problem": ""}
```

---
thinking (summarized):

Ball3 settles into the cup, resting against the bottom with just a tiny residual drift from 1.42 to 1.48, well within the interior bounds of 1.383–1.683 — so it counts as at rest. Balls 1 and 2 remain outside, confirming the setup works.

