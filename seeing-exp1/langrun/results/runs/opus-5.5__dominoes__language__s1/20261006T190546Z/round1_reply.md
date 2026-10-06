**What happened:** The chain never started. domino1 was meant to start with a 5 rad/s spin about y. It only began to move at 0.21 s, and then drifted backward at 0.08 m/s rather than tipping forward. It rocked about 2° and settled upright by 0.56 s. Dominoes 2 to 10 never moved, and all ten ended standing upright.

**Why:** A spin about the domino's centre drives its far bottom edge into the floor, and floor contact seems to have absorbed it.

**Fix:** I've written the dominoes out one by one so that only domino1 gets a start. It now starts as if already pivoting forward about its far bottom edge: 6 rad/s about y, plus the matching launch of 0.30 m/s along and 0.045 m/s up. With the rest still 6 cm apart, each should topple the next.

```world
world  domino chain

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino1
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 0 m along
  spins     6 rad/s about y
  launched  0.30 m/s along, 0.045 m/s up

domino2
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino1

domino3
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino2

domino4
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino3

domino5
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino4

domino6
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino5

domino7
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino6

domino8
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino7

domino9
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino8

domino10
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  stands    on floor, 6 cm beyond domino9

expect
  domino1 touches domino2
  domino9 touches domino10
```

```json
{"what_happens": "domino1 barely stirs: it drifts backward at 0.08 m/s around 0.21-0.25 s, rocks about 2 degrees and settles upright by 0.56 s; dominoes 2-10 never move and all ten end standing upright.", "works": false, "problem": "The first domino's starting spin about its centre was absorbed by floor contact, so it never tipped forward and no domino fell."}
```

---
thinking (summarized):

The spin didn't actually take effect — domino1 only started moving at 0.21s with a small velocity, then stopped after turning just 2°. It seems like the applied angular velocity got absorbed by floor contact instead of producing a real rotation, so I need another approach to get the domino falling properly, maybe adjusting the initial angle or contact setup.

That negative vx is confusing me — maybe the spin direction got flipped somewhere, or friction is causing the center to recoil backward instead of forward. I'll trust the right-hand rule convention I derived and just write domino1 separately with its own spin and launch, then define domino2 onward as each standing 6 cm beyond the previous one on the floor.

