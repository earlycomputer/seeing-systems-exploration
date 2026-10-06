Ten 1 × 4 × 8 cm dominoes stand 4.5 cm apart. The first starts with a forward spin about y, so its top pitches toward the second domino.

**Why each one should end tilted at least 15°:**
- The gap leaves 3.5 cm between neighbouring faces.
- A domino resting against the next one leans about asin(3.5/8), which is roughly 26°.
- The last domino has nothing beyond it, so it should fall flat. The ones behind it should then settle lower still.

This is a geometric estimate and I haven't run it. The `expect` block only checks that the first and last pairs touch. It doesn't check the 15° tilt itself, because the language has no form for angles, so the tilt needs checking in the run.

```world
world  ten dominoes

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a             box 1 by 4 by 8 cm, 20 g
  friction         0.5
  colour           wood
  moves            freely
  repeated         10 times, 4.5 cm apart along
  first one spins  5 rad/s about y
  stands           on floor, 1 m along

expect
  domino1 touches domino2
  domino9 touches domino10
```

---
thinking (summarized):

I'm planning ten dominoes in a row with the first one given an initial spin to knock it over, using roughly 1x4x8 cm blocks spaced about 3.5 cm apart.

Since the last domino has nothing to lean against, it falls flat to the floor, while each preceding one cascades onto the next, leaning at increasingly shallow angles. I widen the spacing to around 4.5 cm so each tilts at least 25-30 degrees before resting against its neighbor.

For the first domino, I spin it about the y-axis so the top edge rotates toward the +x direction, giving it a gentle push to topple forward — a spin of a few rad/s is enough since the energy needed to tip it over such a small height is tiny. I'll set each domino's mass around 20 grams with friction around 0.6, and lay them out in a line with contact pairs between consecutive dominoes.

