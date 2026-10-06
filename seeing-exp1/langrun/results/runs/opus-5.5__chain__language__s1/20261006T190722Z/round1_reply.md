## What happens in the run

Ball1 hops off the floor at 0.04 s. It bumps ball2, and ball2 bumps ball3, so the chain of hits does happen. But ball3 leaves at only about 1.07 m/s and loses speed quickly on the floor and the ramp. It stalls at x ≈ 1.39 m, just short of the cup's near wall, and rolls back down. All three balls end at rest on the floor near x ≈ 0.75–0.97 m, and the cup stays empty.

## Why it fails

- **Rolling friction was far too high.** A rolling friction of 0.002 m on 2.5 cm balls slows each ball at roughly 0.5 m/s².
- **Ball-on-ball friction made the balls hop.** At 0.8, the spinning ball1 grabbed ball2 at contact and was thrown upward, wasting speed.

## The fix

- Rolling and spinning friction are nearly zero.
- Ball-on-ball friction is low (0.05). The floor's 0.8 still makes the balls roll on the floor.
- Ball1 is launched with no spin.
- Ball2 and ball3 sit only 2 cm apart. Ball2 then reaches ball3 before it loses speed settling into rolling, so ball3 gets nearly all of it.
- I estimate ball3 reaches the ramp at about 1.4 m/s; it needs about 1.05 m/s to climb it.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.0001, rolling 0.00005

ball1
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.0001, rolling 0.00005
  colour    orange
  moves     freely
  rests     on floor, 20 cm along
  launched  4 m/s along

ball2
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.0001, rolling 0.00005
  colour    white
  moves     freely
  rests     on floor, 40 cm beyond ball1

ball3
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.0001, rolling 0.00005
  colour    white
  moves     freely
  rests     on floor, 7 cm beyond ball2

-- the cup: low lip at the near end (3 cm above its floor, more than the ball's radius), tall far and side walls
cup
  is an             open box
  length            35 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    1 cm
  near wall height  4 cm
  at                its base 1.6 m along

-- a shallow ramp leading up to the top of the cup's near wall
ramp top
  is a  point
  at    1.415 m along, 4 cm up

ramp foot
  is a  point
  at    1.015 m along, 0 cm up

cup ramp
  is a    plank from ramp top to ramp foot, 20 cm wide, 4 mm thick
  colour  grey

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup ramp
  ball3 comes to rest in cup
```

```json
{"what_happens": "Ball1 hops off the floor and bumps ball2, which bumps ball3. Ball3 leaves at only about 1 m/s, slows quickly, stalls on the ramp just short of the cup's near wall and rolls back. All three balls end at rest on the floor and the cup stays empty.", "works": false, "problem": "Rolling friction that is too high and grabby ball-on-ball friction (which made the balls hop) drain ball3's speed, so it stalls on the ramp and never reaches the cup."}
```

---
thinking (summarized):

I'm tracking the physics inconsistencies: ball1 seems to have hopped with a questionable spin sign, lost most of its velocity after colliding with ball2, and ball3 decelerated sharply on the flat floor before reaching the ramp—something's off in these numbers that needs double-checking.

On the ramp, the expected rolling deceleration from gravity alone doesn't match the observed slowdown, which points to rolling friction being too large for a small ball radius—so I should shrink rolling friction and use bigger balls instead. I'm also suspecting the collision friction between spinning balls is injecting unwanted vertical motion, since ball1's surface velocity at the contact point could be dragging ball2 downward or upward depending on spin direction, possibly explaining why both balls leave the floor unexpectedly.

I think the cleanest fix is to drop spin entirely, enlarge the balls, lower rolling friction, and set ball-to-ball friction lower than floor friction—keeping in mind MuJoCo combines contact friction by taking the max of the two geoms, so floor contact stays at 0.8 while ball-ball contact can be reduced to around 0.3.

I'm redesigning with 4 cm radius balls at 200 g, rolling friction near zero on both floor and ball contacts, and launching ball1 at 3 m/s with no spin so it slides then rolls to about 2.14 m/s before collision. But even with a restitution around 0.8, the resulting chain transfer only pushes ball2 to roughly 1.2 and ball3 to about 0.7—short of the 1.05 target, so I need to boost the initial launch speed further.

Now I'm recalculating the ramp requirement with a 4 cm radius ball needing a step over 4 cm, settling on a 6 cm wall height that demands ball3 reach about 1.15 m/s. Testing a 5 m/s launch only gets ball3 to roughly 1.17 at e=0.8, which is too marginal, so I'm considering whether arranging the balls touching in a row, Newton's cradle style, would avoid sliding losses entirely during the first impact.

Thinking through momentum transfer with small 2 cm gaps between balls rather than full contact, since this lets ball2 strike ball3 while still mostly sliding, preserving velocity before it decays to the 5/7 rolling fraction over roughly 7 cm of travel. I'm settling on 2 cm gaps as the sweet spot and now positioning ball1 to start 30 cm behind ball2.

I realize the hop happens because ball1's topspin creates friction against ball2's stationary surface, pushing ball1 upward on contact — that explains why ball1 lifted to 0.08. So I need low ball-to-ball friction, maybe 0.05, while keeping floor friction higher around 0.8 for good rolling grip. I'll set radius 2.5 cm, mass 100 g, with ball friction 0.05 and floor friction 0.8, both using small spinning and rolling resistance values.

Now I'm working through the chain reaction: ball1 launches at 4 m/s with no spin, hits ball2, which transfers speed down to around 2.86 m/s once rolling, then rolls into ball3 across a small gap. I'm checking whether ball3 picks up enough speed to clear the ramp — working out the sliding-to-rolling transition gives roughly 1.48 m/s, and I need to verify the top speed and fall time off the ramp still land within the 10 cm target zone.

I'm also checking what happens after the ball enters the cup: hitting the far wall at 10 cm it rebounds around 1 m/s, then hits the near wall at a height where its center sits below the wall's top edge, so it can't climb out and should settle. Then I'm reconsidering whether ball1 keeps moving after the first collision with enough leftover speed (accounting for the restitution coefficient and spin) to hit ball2 again and push it into the cup as well.

Tracing the rolling dynamics further, ball1's remaining translational and spin components recombine into a new rolling speed around 0.96 m/s, which lets it strike ball2 and transfer enough speed that ball2 moves at roughly 0.6 m/s — not enough to clear the ramp, so ball2 falls back short of the required 1.05 m/s threshold. Meanwhile ball3, sitting on the 5.7° incline, momentarily stops before gravity pulls it back down the slope.

