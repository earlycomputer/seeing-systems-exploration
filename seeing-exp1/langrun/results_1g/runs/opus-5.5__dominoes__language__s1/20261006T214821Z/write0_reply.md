Ten 1 × 5 × 10 cm dominoes stand 6 cm apart along x. The first starts with a forward spin about y, which tips its top toward the row. Because the gap is wider than half a domino's height, each fallen domino rests leaning at least about 30° on the next one. The last domino falls flat onto the floor.

```world
world  domino row

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a              box 1 by 5 by 10 cm, 30 g
  friction          0.5, spinning 0.005, rolling 0.002
  colour            wood
  moves             freely
  repeated          10 times, 6 cm apart along
  first one spins   3 rad/s about y
  stands            on floor, 1 m along

expect
  domino1 touches domino2
  domino2 touches domino3
  domino3 touches domino4
  domino4 touches domino5
  domino5 touches domino6
  domino6 touches domino7
  domino7 touches domino8
  domino8 touches domino9
  domino9 touches domino10
```

---
thinking (summarized):

I'm sketching out domino dimensions and spacing for the box, then working through how the initial spin of 4 rad/s about the y-axis determines the tipping direction of the first domino.

Thinking through the physics of the tip: with the domino spinning about its center while resting on the floor, friction should still drive it into a forward tip, since the energy needed to raise the center slightly is tiny compared to the input spin. I'm then reasoning about how each subsequent domino leans on the next, with the last one ending flat on the floor and the chain geometry determined by spacing versus height.

I'm also pinning down concrete values—domino dimensions, mass, friction coefficient, spacing, and positions for the row of ten—settling on something like 1×5×10 cm dominoes spaced 6 cm apart, and checking whether the chosen spin rate is physically reasonable without causing unwanted edge effects near the floor contact point.

For the event sequence, I'll use "touches" as the relation to describe dominoes falling into one another down the chain, including the final one meeting the floor.

I'll set domino friction to 0.5 so they pivot cleanly without excessive slipping.

