## What happened in the run

ball1 rolls down the ramp and hits d1, and the chain runs d1 → d2 → d3. This time d3's top corner strikes ball2 at about 2.08 s. That knocks ball2 along the shelf at about 0.2 m/s, and d3 comes to rest leaning on the shelf edge.

ball2 then slows to about 0.08 m/s before reaching the cup. It ends at rest on top of the cup's 2 cm-wide near wall, at x = 1.78 m and z = 0.08 m, so it is still outside the cup.

## Why it stopped short

ball2's rolling friction of 0.002 is too large for a 2 cm ball. It slowed ball2 by roughly 0.5–0.7 m/s², which used up almost all its speed. The near wall was also as tall as the shelf, so ball2 had to roll across the wall's top to get in.

## Changes in the corrected world

- **Low rolling friction:** ball2 and the shelf now have rolling friction 0.0001. The cup keeps 0.002, so ball2 still settles once it is inside.
- **Near wall:** lowered to 3 cm and moved back, so the shelf's far end sticks 3 cm out over the inside of the cup.
- **Drop-in:** even a slow ball2 now just rolls off the shelf edge and drops straight into the cup, where the tall walls hold it.

```world
world  ramp ball domino chain into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    0 m along, 12 cm up

ramp foot
  is a  point
  at    1.2 m along, -2 cm up

ramp
  is a    plank from ramp top to ramp foot, 20 cm wide, 4 cm thick
  colour  wood
  friction  0.8, spinning 0.005, rolling 0.002

-- ball1 sits 1 m up the 1.21 m deck, measured from its low end
ball1
  is a      sphere 6 cm radius, 80 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  on ramp, 20.8 cm from the top

d1
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.45 m along

d2
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.52 m along

d3
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.59 m along

-- shelf: near end 6 cm ahead of d3's front face; its far end overhangs the inside of the cup by 3 cm
shelf
  is a      box 10 by 12 by 6 cm
  colour    grey
  friction  0.8, spinning 0.001, rolling 0.0001
  on floor, 1.71 m along

ball2
  is a      sphere 2 cm radius, 15 g
  rolls
  friction  0.4, spinning 0.001, rolling 0.0001
  colour    black
  moves     freely
  on shelf, 1.68 m along

-- cup: near wall 3 cm high (below the shelf top) spanning 1.71 to 1.73 m, under the shelf; interior beyond the shelf's far end
cup
  is an             open box
  length            14 cm
  width             12 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  3 cm
  bounce            dead
  friction          0.8, spinning 0.005, rolling 0.002
  colour            wood
  its base 1.79 m along

expect
  ball1 touches d1
  d1 touches d2
  d2 touches d3
  d3 touches ball2
  ball2 comes to rest in cup
```

```json
{"what_happens": "ball1 rolls down the ramp and topples d1, which topples d2, which topples d3. d3's top corner knocks ball2 along the shelf at about 0.2 m/s, but ball2 slows sharply and stops on top of the cup's near wall, outside the cup.", "works": false, "problem": "ball2's rolling friction was so large that it lost its speed on the shelf and came to rest on top of the cup's near wall instead of inside the cup."}
```

---
thinking (summarized):

Ball2 launches at about 0.2 m/s and decelerates under rolling friction, ending up right near the far wall around x=1.77-1.78, settling on top of the narrow wall (spanning 1.76-1.78) at that position.

This creates a dead-stop problem instead of a bounce into the cup. I should fix this by sloping the shelf slightly downward toward the cup so the ball keeps rolling after being knocked, or by making the near wall lower/thinner than the shelf edge so the ball just drops off the shelf directly into the cup — essentially letting the shelf's far end overlap into the cup interior past the near wall.

Now I'm reconsidering the ball's deceleration numbers (0.19 to 0.08 m/s over roughly 0.25s) — that's too strong for simple rolling friction, suggesting the ball was sliding rather than rolling, or that it caught on a seam where the near wall height equals the shelf height, creating a tiny lip the ball climbs over.

Actually, running the numbers for MuJoCo's rolling friction formula with a 0.002 m coefficient and 2 cm radius ball gives a deceleration around 0.7 m/s² — much larger than expected, so that rolling friction value is likely the culprit. I should lower the rolling friction for both the ball and shelf/cup surfaces to something like 0.0002 to avoid artificial braking, while relying on cup wall contacts to naturally damp the ball's motion once it settles inside.

Now I'm working out the geometry — repositioning the cup and shelf so the near wall's inner face, shelf overlap, and ball's starting position all align so the ball travels the right distance into the cup.

Checking ball2's fall speed near the shelf edge: dropping from about 8 cm height to 2.5 cm takes roughly 0.106 s, landing close to the shelf face with minor scraping, which seems fine. It should then roll slowly toward the far wall, bounce back, and settle without noticeable lateral deviation.

