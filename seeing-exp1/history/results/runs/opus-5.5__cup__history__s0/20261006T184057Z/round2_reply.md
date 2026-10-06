**What happens in the run**

1. The ball rolls down `ramp_deck` and leaves its low end at 1.26 s, moving at about 2.4 m/s.
2. It clears the near wall and lands on `cup_base` at x ≈ 2.17 at 1.50 s.
3. It hops twice on the base, then hits `cup_far` at 1.69 s. That impact takes out nearly all of its forward speed.
4. It drops back onto the base, rolls slightly backward, and comes to rest at 2.14 s at about (2.53, 0, 0.08).
5. It stays inside the cup, still touching `cup_base`, through 6 s. The final position is (2.51, 0, 0.08), between the cup walls at x = 1.76 and 2.64.

```json
{"what_happens": "The ball rolls down ramp_deck, flies off its low end over the cup's near wall, lands on cup_base, hops and bumps cup_far, which stops it. It then settles at rest on cup_base at about (2.51, 0, 0.08), inside the cup, for the rest of the run.", "works": true, "problem": ""}
```

---
thinking (summarized):

The ball settles at (2.51, 0, 0.08), comfortably within the cup interior bounds and resting on the cup base. There's a slight drift from 2.53 to 2.51 but since it's reported at rest, that's acceptable.

