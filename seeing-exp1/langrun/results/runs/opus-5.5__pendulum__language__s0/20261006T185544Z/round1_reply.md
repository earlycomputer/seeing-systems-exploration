**What happens in the run:** The pendulum is released from 38° and swings down. At 0.37 s the bob strikes the resting ball at the bottom of its arc. The ball rolls away at about 0.83 m/s, slowing only slightly to 0.80 m/s by the cup. At 1.35 s it hops over the cup's low near lip, rolls across the base and hits the far wall at 1.88 s. It rebounds very slowly at about 0.05 m/s and creeps back across the base. It comes to rest at about x = 0.98 m, against the near lip, on the cup base. The cup's centre is at 1.09 m, so the ball rests inside the 30 cm cup, about 11 cm short of its centre.

After the strike the pendulum keeps swinging between about ±15°. Two oddities don't break the brief:
- The pendulum's rod is reported touching the stand arm for the whole run. It only slowly saps the swing.
- The ball's 3.5 s creep after the rebound is longer than I'd expect, but it stays inside the walls.

```json
{"what_happens": "The pendulum swings down from 38° and strikes the ball at 0.37 s. The ball rolls along the floor at about 0.8 m/s, hops over the cup's low near lip at 1.35 s, rolls to the far wall and rebounds gently. It creeps back and comes to rest on the cup base at about x = 0.98 m, inside the cup whose centre is 1 m from the ball's start. The pendulum keeps swinging at about ±15°, its rod touching the stand arm throughout.", "works": true, "problem": ""}
```

---
thinking (summarized):

Tracing the ball's path: the pendulum strikes it at 0.37s, it rolls at 0.83 m/s, hops the lip, hits the far wall, and rebounds slowly backwards at 0.05 m/s. It creeps toward the near wall, settling near x=1.00 at 5.44s, then finally touches the near wall and comes to rest at x=0.98 around 5.81s, resting against the cup base.

I also notice the pendulum rod stays in contact with the stand arm throughout the run, and the pendulum's swing amplitude drops sharply from 38° to about 16° after the collision, then decays slowly over subsequent swings.

The ball's slow creep at a constant speed for several seconds is odd since rolling friction should've stopped it, but ultimately it ends at rest within the cup's base, offset 0.11 m from the cup center against a 0.15 m half-length tolerance — so it works, with the rod-on-stand-arm contact just a cosmetic issue worth noting.

