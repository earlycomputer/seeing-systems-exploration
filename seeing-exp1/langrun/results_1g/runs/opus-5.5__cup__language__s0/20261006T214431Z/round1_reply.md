## What happens

The ball starts on the ramp deck at x = 0.10 m and barely moves. It creeps about 11 cm in 6 s and is still on the ramp at the end, so it never reaches the cup.

The cause is rolling friction. MuJoCo applies the larger of the two touching geoms' rolling friction, here the ball's 0.01 m. A 3 cm ball only rolls freely down a slope steeper than about 18° with that, and the ramp is only about 6°.

## The fix

- I've cut the ball's and the ramp's rolling friction to 0.0005, so the ball now rolls on any slope steeper than about 1°.
- The cup keeps rolling 0.02, and its dead bounce still takes energy out on impact, so the ball should settle quickly once inside.
- The geometry stays the same. The run shows the ramp's end points mark the deck's centre line. The ball should leave the ramp with its centre about 19 cm up, clear the 12 cm near wall, and land around x ≈ 1.2 m inside the cup.

```json
{"what_happens": "The ball sits on the ramp deck and creeps only about 11 cm down it over 6 s, ending at (0.21, 0, 0.28) m still on the ramp; it never reaches or touches the cup.", "works": false, "problem": "The ball's rolling friction (0.01 m) is far too high for the 6° ramp, so the ball barely rolls."}
```

```world
world  ball rolls down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   25 cm up
  low end    1 m along, 14 cm up
  width      20 cm
  thickness  4 cm
  friction   0.9, spinning 0.002, rolling 0.0005
  colour     wood

cup
  is a            open box
  length          30 cm
  width           30 cm
  walls           12 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        1.0, spinning 0.02, rolling 0.02
  bounce          dead
  colour          grey
  its base 1.2 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.002, rolling 0.0005
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball touches cup
  ball comes to rest in cup
```

---
thinking (summarized):

I'm checking whether the ball actually rolls down the slope or just creeps, comparing the ramp angle against the effective rolling friction threshold using MuJoCo's friction model, where the larger of the two geoms' friction values dominates.

Lowering both ball and ramp rolling friction to 0.0005 brings the threshold down to about 1°, well below our 6.3° slope, so motion should be reliable. The cup's higher friction (0.02) will still quickly damp the ball's rolling once it lands, which is good.

I also verify the ball's clearance along the deck and trajectory: it exits around 1.18 m/s, falls 14 cm, and lands roughly 1.2 m out, clearing the 12 cm walls comfortably — so I'll keep the current geometry and just adjust the rolling friction values.

