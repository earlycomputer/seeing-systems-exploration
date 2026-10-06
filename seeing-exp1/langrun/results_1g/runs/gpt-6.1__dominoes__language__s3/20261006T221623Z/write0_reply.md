```world
world  ten falling dominoes

floor
  size      4 m
  friction  0.8, spinning 0.001, rolling 0.0001

domino
  is a             box 2 by 8 by 20 cm, 200 g
  moves            freely
  friction         0.8, spinning 0.001, rolling 0.0001
  bounce           dead
  colour           white
  stands           on floor, 0 m along
  repeated         10 times, 7 cm apart along
  first one spins  5 rad/s about y

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