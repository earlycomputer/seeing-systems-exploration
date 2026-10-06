**What happens in the run**

Ball1 is launched at 4 m/s and strikes ball2 at 0.06 s. Ball2 rolls on and strikes ball3 at 0.14 s. Ball3 rolls about 0.75 m along the floor at roughly 1.4 m/s, rides up over the cup's low near wall at 0.67 s, and drops onto the cup's base at 0.88 s. It stops at x = 1.98 m, inside the cup between its walls and touching cup_base, and stays there to the end.

The two followers trail behind. Ball2 ends perched on top of the cup's near-wall sill. Ball1 stops on the floor just behind it. Neither disturbs ball3.

The sequence the brief asks for happens, and ball3 finishes at rest in the cup.

```json
{"what_happens": "ball1 is launched at 4 m/s and hits ball2 (0.06 s), which hits ball3 (0.14 s); ball3 rolls along the floor, rides over the cup's low near wall and drops onto the cup's base at 0.88 s, coming to rest inside the cup at x = 1.98 m. ball2 ends perched on the cup's near-wall sill and ball1 stops on the floor just behind it.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm checking the cup's position on the floor and its near wall location, then confirming ball3 sits inside touching the base while ball2 rests on the near wall's sill.

Ball3 stopped quickly past the wall, which makes sense given strong rolling friction, but it's still properly inside the cup. The chain works: ball1 hits ball2, ball2 hits ball3, ball3 ends up resting in the cup. Ball2 perched on the sill is just cosmetic, not a real violation — the setup checks out.

