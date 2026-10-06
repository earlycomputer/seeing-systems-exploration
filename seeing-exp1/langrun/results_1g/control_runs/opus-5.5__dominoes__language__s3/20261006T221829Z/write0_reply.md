Ten 1 by 5 by 10 cm dominoes stand 5 cm apart. The first gets a 12 rad/s forward spin about y.

**Why that spin should tip it.** When it pivots on its front bottom edge, it keeps about a quarter of that spin, roughly 3 rad/s. About 1.2 rad/s is needed to lift its centre over the edge, so there is a good margin. I worked this out by hand and haven't run it.

**Why each should end tilted at least 15°.** Each domino has a 4 cm gap to the next, so it falls and leans on its neighbour at no less than about 24°. The last one falls onto the floor. I expect the leaners to settle lower than 24°, since the dominoes they rest on are also tilted.

```world
world  ten dominoes

floor
  size      4 m
  friction  0.6, spinning 0.005, rolling 0.002

domino
  is a              box 1 by 5 by 10 cm, 20 g
  colour            wood
  friction          0.5, spinning 0.005, rolling 0.002
  moves             freely
  repeated          10 times, 5 cm apart along
  first one spins   12 rad/s about y
  stands            on floor, 50 cm along

expect
  domino1 touches domino2
  domino9 touches domino10
```

---
thinking (summarized):

I'm sketching domino dimensions—thin rectangular blocks spaced about half their height apart so they topple in sequence—and figuring out how to give the first domino an initial spin to kick off the chain reaction.

Working through the torque directions, I realize the forward friction force at the bottom actually creates a torque opposing the spin, not reinforcing it. Tracing through the geometry more carefully, as the domino tips forward the far bottom edge digs into the floor while the near edge lifts, so the normal force there also works against the spin—meaning I need to rethink whether pure spin alone is enough to tip it, or whether the pivot naturally shifts to that far edge and changes the dynamics.

Solving this gives w' ≥ 1.35, so w ≥ 5.4 rad/s minimum — I'll use something like 10-12 rad/s for a safe margin, even though friction could complicate the real behavior. Now I'm reconsidering with more realistic domino dimensions (closer to actual 48x24x7.5mm proportions, maybe 1cm thick, 5cm wide, 10cm tall) to check if the stability math still holds with reasonable spacing.

Now I'm working out the collapse geometry for the full chain: since each domino leans against the next rather than falling flat, I need to figure out the resting angle based on the gap between dominoes relative to their height, which seems to work out to something like 23.6° for a 4cm effective gap, though the chain compresses further as the last domino hits the floor directly.

For the physical setup I'm setting friction coefficients around 0.5-0.6 for wood dominoes, mass 20g each, spaced 5cm apart along a 0.5m floor segment with floor friction 0.6. I'm also deciding whether to include an explicit touch condition like "domino9 touches domino10" as a simple expectation check, since that seems sufficient rather than verifying every contact in the chain.

