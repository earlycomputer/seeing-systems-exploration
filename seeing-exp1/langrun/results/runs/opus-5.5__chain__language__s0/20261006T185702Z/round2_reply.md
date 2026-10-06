**What happens:** `ball1` is launched at 5 m/s and hops briefly before it hits `ball2` at 0.05 s. `ball2` hits `ball3` at 0.13 s. `ball3` hops over the 5 mm lip into the cup, strikes the far wall and comes to rest inside on `cup_base` at x = 1.50 m. `ball1` stops on the floor at 0.79 m.

**The problem:** `ball2` keeps rolling forward on its leftover spin. It mounts the lip at 0.47 s and also ends up in the cup, resting on `cup_base` at x = 1.26 m. The brief only has the third ball going into the cup.

**The fix:** `ball2` stops by about x = 1.27 m, so I'll move the cup's near wall out to about 1.40 m. `ball3` still arrives at about 1.2 m/s, well above what it needs to clear the lip.

```json
{"what_happens": "ball1 is launched and hits ball2, ball2 hits ball3, and ball3 hops over the low lip into the cup and comes to rest inside at x = 1.50 m; but ball2 follows on its leftover spin, climbs the lip and also comes to rest inside the cup at x = 1.26 m, while ball1 stops on the floor.", "works": false, "problem": "ball2 drifts after its collision and ends up in the cup too, when only the third ball should roll in."}
```

```parts
part low lipped cup
  needs  length
  needs  width
  needs  walls
  needs  lip, else 5 mm
  needs  wall thickness, else 1 cm
  needs  base thickness, else 5 mm

  base
    is a      box length by width by base thickness
    on        floor
    friction  0.9, spinning 0.02, rolling 0.01
    bounce    dead
  near wall
    is a      box wall thickness by width by lip
    on        floor, centred on base's near end
    bounce    dead
  far wall
    is a      box wall thickness by width by walls
    on        floor, centred on base's far end
    bounce    dead
  left wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's left side
    bounce    dead
  right wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's right side
    bounce    dead
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 50 cm along
  launched  5 m/s along

ball2
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 30 cm beyond ball2

cup
  is a    low lipped cup
  length  30 cm
  width   14 cm
  walls   8 cm
  lip     5 mm
  its base 45 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm noticing a problem: the brief only calls for the third ball to roll into the cup, but ball2 is also ending up near the cup lip, which muddles whether that counts as an unintended deviation. I should flag this as a potential strict-honesty issue worth addressing.

To fix it, I'll move the cup further away—placing it so ball2's deceleration (roughly 1 m/s² from 0.52 m/s) causes it to stop just short, around 1.27m, while giving ball3 a ~27cm runway to still enter the cup with reasonable speed (~1.2 m/s). I'll also note the slight hop at ball1's launch is minor and can stay as-is.

