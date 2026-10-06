The first domino rocks by about 3° but returns upright instead of falling. The other nine remain stationary, and no adjacent dominoes touch. The world therefore fails the brief.

This revision uses thinner dominoes, closer spacing, and a stronger initial spin to start the cascade.

```world
world  ten dominoes falling in sequence

floor
  size      6 m
  friction  0.9, spinning 0.005, rolling 0.0001

domino
  is a             box 1 by 5 by 15 cm, 100 g
  stands           on floor
  moves            freely
  friction         0.9, spinning 0.005, rolling 0.0001
  bounce           dead
  colour           wood
  repeated         10 times, 4 cm apart along
  first one spins  10 rad/s about y

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

```json
{
  "what_happens": "The first domino rocks by about 3 degrees and returns upright; the other nine remain stationary, and no adjacent dominoes touch.",
  "works": false,
  "problem": "The initial spin does not tip the first domino far enough to initiate the cascade, so all ten finish upright."
}
```