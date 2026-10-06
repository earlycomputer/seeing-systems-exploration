## What happens in the run

1. **Launch:** Ball1 starts at 4 m/s, with a couple of small hops in its first 0.1 s.
2. **Ball1 hits ball2 (0.10 s):** Ball2 starts moving.
3. **Ball2 hits ball3 (0.11 s):** Ball3 leaves at about 1.5 m/s.
4. **Ball3 into the cup:**
   - It rolls up the cup ramp from 0.33 s and leaves the ramp at 0.64 s.
   - It lands on the cup base at 0.74 s and bounces off the far wall at 0.92 s.
   - It rolls back to the near wall's inside face at 2.83 s.
   - It settles on the cup base around x ≈ 1.46–1.53 m, inside the cup's footprint (base spans x 1.425–1.775 m).
5. **Ball1 and ball2 afterwards:**
   - They creep up the ramp and stall.
   - They roll back down and are still moving slowly away along −x at the end.

Nothing in the brief needs them to stop, so this doesn't break it.

```json
{"what_happens": "Ball1 is launched and rolls into ball2 at 0.10 s; ball2 immediately strikes ball3, which rolls off at about 1.5 m/s, climbs the ramp, drops over the cup's near lip at about 0.7 s, bounces off the far wall and comes to rest on the cup base. Ball1 and ball2 stall on the ramp, roll back and are still drifting away along -x at the end.", "works": true, "problem": ""}
```

---
thinking (summarized):

Ball3 settles in the cup near x≈1.5, within the cup's base span, with only a tiny 0.07 m drift over three seconds — close enough to count as at rest, while balls 1 and 2 roll back off toward negative x without affecting the outcome.

