**What happens:** The chain of collisions works. `ball1` hops at launch, hits `ball2` at 0.09 s, and `ball2` hits `ball3` at 0.29 s.

The collisions and the floor's rolling friction cost far more speed than I planned for. `ball3` leaves at only about 0.5 m/s and slows to about 0.1 m/s by the time it reaches the cup. It taps the 1 cm lip at 1.58 s and stops outside the cup at x = 1.52 m.

**Fixes:**
- Launch `ball1` harder.
- Move the cup closer so `ball3` reaches it sooner and faster.
- Lower the lip to 5 mm so it is easy to roll over.
- Lengthen the cup so its grippy base has room to stop the ball.

```json
{"what_happens": "ball1 is launched, hits ball2, which hits ball3; ball3 rolls slowly toward the cup, taps its 1 cm near lip at about 0.1 m/s and comes to rest just outside the cup at x = 1.52 m.", "works": false, "problem": "ball3 arrives too slowly to climb the cup's lip, so it stops outside the cup instead of rolling into it."}
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
  its base 30 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

The chain of collisions works, but ball3 stalls right at the lip instead of dropping into the cup—friction losses were worse than I predicted, with ball2 only reaching about 1.1 m/s and ball3 decelerating from 0.51 to 0.11 m/s over a second, arriving at the lip too slow to climb in. I need to adjust the setup to compensate for this extra friction.

Ball2 might drift a bit further too with the higher launch speed, but that's tolerable since only ball3's position is checked, and the stop distance stays small. I'll also lengthen the cup to 30 cm so its near wall sits at 1.25 m, giving ball3 enough room to settle inside comfortably.

