Ten 1 × 4 × 8 cm dominoes stand 5 cm apart along x. A starting spin about y tips only the first one forward. Each falling domino hits the next before it gets far, so the dominoes end up leaning on one another at about 30° or more, and the last one lies on the floor.

```world
world  domino row

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a             box 1 by 4 by 8 cm, 25 g
  colour           wood
  friction         0.6, spinning 0.005, rolling 0.002
  moves            freely
  repeated         10 times, 5 cm apart along
  first one spins  4 rad/s about y
  stands           on floor, 1 m along

expect
  domino1 touches domino2
  domino9 touches domino10
  domino10 touches floor
```

Why these choices:

- **Spin and direction:** a positive spin about y swings the top of `domino1` toward +x, which is down the row.
- **Toppling:** the domino only needs to lean past about 7° to fall (thickness ÷ height). The 4 rad/s spin carries it well past that without making it hop.
- **Spacing:** the gap between faces is 4 cm on an 8 cm height. A leaning domino therefore rests on the next one at roughly 30°, which clears the 15° requirement.
- **The last two:** `domino10` falls flat at about 90°, and `domino9` ends steeper still against it.
- **Timing:** each domino takes roughly 0.2–0.3 s to fall, so the whole row should be down in about 3 s, inside the 6 s run.

I haven't run this in MuJoCo, so these angles and times are estimates. The `expect` block checks the first and last contacts and that `domino10` reaches the floor.

---
thinking (summarized):

I'm sketching out domino proportions for a chain reaction setup—roughly 1cm thick, 4cm wide, 8cm tall, spaced about 5cm apart with 30g mass each—and starting to think through the physics of the first tile tipping over and spinning about its base.

Only the first domino should have the initial spin applied (not every copy), so I'm working out the sign conventions: a positive angular velocity about the y-axis makes the top of the tile swing toward +x while the bottom edge, pressed against the floor, moves toward -x due to friction. I'm computing the velocity vectors at the base and corners using the cross product of angular velocity and position to make sure the rotation direction matches the domino falling forward into the next tile in the row.

I'm estimating a safe spin value, around 4 rad/s, large enough to carry past the small ~7° critical tipping angle but not so much it causes bouncing. Then I'm working out how adjacent dominoes lean against each other given the 5 cm spacing, 1 cm thickness, and 8 cm height, solving for the angle where a falling domino's top edge contacts the back face of the next one in the chain.

For the last domino in the row, there's nothing to lean against, so it ends up lying flat near 90°, while the second-to-last leans heavily against it; the rest settle around 30°+, which satisfies the ≥15° requirement. For friction, I'll set domino-to-domino at 0.6 to keep things stable without excessive sliding, and I'm sizing the mass at roughly 25g based on a wood density estimate for the block's volume, positioning ten dominoes spaced 5 cm apart along the one-meter line.

I'll keep the expect conditions simple—just a couple of "touches" checks between neighboring dominoes (domino1-domino2 and domino9-domino10)—since the exact format beyond examples is unclear. Timing-wise, each domino should topple in about 0.2-0.3s, so the full chain reaction of ten should finish well within the 6s window; I'll give the initial push a bit more force (ω around 4 rad/s) to make sure the chain reliably completes.

