Ten dominoes 1 cm thick and 10 cm tall stand 6 cm apart. The first one gets a forward spin about y, so its top swings toward the second and the chain runs down the row.

Why every domino should end at least 15° from upright:
- Each of the first nine can only lean onto the next one, which stands 6 cm away. Its top hits that neighbour when it is already tilted by about asin(6/10) ≈ 37°.
- The last one has nothing to lean on, so it falls flat on the floor.

```world
world  ten dominoes falling

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a             box 1 by 5 by 10 cm, 20 g
  colour           wood
  friction         0.6, spinning 0.005, rolling 0.002
  moves            freely
  repeated         10 times, 6 cm apart along
  first one spins  5 rad/s about y
  stands           on floor, 1 m along

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

I'm planning ten dominoes with consistent thickness and spacing, tipping the first one by rotating it slightly around the y-axis so it leans toward the next piece in line.

I'm checking the physics: giving the domino a small initial spin plus forward velocity so it rolls about its bottom edge, confirming the rotational energy comfortably exceeds the energy needed to tip it over, and verifying the spacing creates a steep enough fall angle to topple each subsequent piece down the line.

Checking the corner velocities during the pivot, the far bottom corner would actually dip into the floor briefly, but that should resolve as a contact impulse and the domino should still tip forward since the top is moving in the +x direction. I'll bump the spin rate up to around 6 rad/s to make sure it reliably topples rather than just rocking in place.

Setting up the chain layout now: each domino touches the next, spaced 6 cm apart with 1 cm thickness giving a 5 cm gap, standing 10 cm tall, with floor friction at 0.8 and domino friction at 0.6 to keep everything stable until the cascade starts.

