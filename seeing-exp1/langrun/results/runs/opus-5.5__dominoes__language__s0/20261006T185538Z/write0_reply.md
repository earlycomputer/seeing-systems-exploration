Ten 2 × 5 × 10 cm dominoes stand 6 cm apart along x. The first gets a starting spin of 8 rad/s about y, which tips its top forward toward the others. Toppling needs only about 4.7 rad/s, so 8 rad/s gives some margin.

The gap between dominoes is 4 cm and each is 10 cm tall. A domino caught leaning on the next one sits at least about 24° from upright. The last domino falls flat, so every domino should end past 15°.

```world
world  ten dominoes

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a             box 2 by 5 by 10 cm, 50 g
  friction         0.5, spinning 0.005, rolling 0.002
  colour           wood
  moves            freely
  repeated         10 times, 6 cm apart along
  first one spins  8 rad/s about y
  stands           on floor, 0.5 m along

expect
  domino1 touches domino2
  domino9 touches domino10
```

---
thinking (summarized):

I'm setting up ten dominoes in a row with boxes sized roughly 1 by 2.4 by 5 cm, spacing them about 3 cm apart so each one topples the next, with the final domino simply falling flat since nothing follows it.

For the lean angle, I calculate asin(2/5) giving about 23.6°, which comfortably exceeds the 15° requirement for the whole chain.

Now I'm working out how to tip the first domino — giving it a starting spin about the y-axis so its top edge rotates toward the next piece, using an angular velocity like 6 rad/s to get enough tangential speed at the top (about 0.15 m/s) to knock it over.

I'm checking whether this spin causes the bottom edge to dig into the floor: computing the velocity at the far bottom corner using ω×r shows a small downward component (about 4 cm/s at 8 rad/s), which should just get absorbed by the floor contact rather than causing penetration. I also verify the energy is sufficient — the center of mass only needs to rise a tiny amount (about 0.05 cm), so even a modest rotational kinetic energy from spinning at 8 rad/s is more than enough.

Let me rescale to a bigger domino, 2 by 5 by 10 cm at 50 g, recomputing the energy needed to tip it over and finding ω around 4.7 rad/s works, so I'll round up to 8 rad/s for safety margin.

Now I'm laying out the domino chain description: a box of those dimensions with friction, repeated ten times spaced 6 cm apart, with the first one given an initial spin about the y-axis and standing on the floor, plus a touching relationship between consecutive dominoes to make sure the chain reaction is captured.

