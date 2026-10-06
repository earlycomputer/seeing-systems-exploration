**What happens in the run:** Ball1 is launched at 3 m/s and hits ball2 at 0.04 s. Ball2 hits ball3 at 0.10 s, and ball3 rolls off at about 1.5 m/s. At 0.27 s it hops over the cup's low near wall. It lands on the cup base at 0.42 s and taps the far wall at 0.58 s. It is at rest by 0.64 s at x = 1.94 m, inside the cup, which spans x = 1.70 to 2.00 m. It stays there, touching cup_base, until 6 s.

Ball1 and ball2 bounce back slightly and creep a few centimetres over the run. Both read as at rest the whole time.

```json
{"what_happens": "ball1 is launched into ball2 (0.04 s), ball2 hits ball3 (0.10 s), and ball3 rolls across the floor, hops over the cup's low near wall, taps the far wall and comes to rest on the cup base at x = 1.94 m, staying there through 6 s; ball1 and ball2 stop on the floor behind.", "works": true, "problem": ""}
```

---
thinking (summarized):

Checking ball3's position against the cup base span of 1.70–2.00 — it rests at 1.94, which is inside the cup, so that placement checks out despite the minor jitter.

