The ball starts near the top of a gentle ramp, rolls off the raised low end, and drops into a wide, open-topped cup. The ball's contacts are dead and it has some rolling friction, so it should settle inside within the 6 s run.

By hand, I estimate the ball leaves the ramp at about 1.4 m/s and lands roughly 25 cm past the ramp's end, inside the cup's 40 cm length. The cup's 8 cm walls rise above the ball's centre, so it cannot roll back out. I haven't run this, so the `expect` lines are what to check.

```world
world  ball down a ramp into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 40 cm up
  low end    60 cm along, 25 cm up
  width      20 cm
  thickness  2 cm

-- the cup sits where the ball lands after leaving the low end
cup
  is an      open box
  length     40 cm
  width      30 cm
  walls      8 cm
  on         floor, 90 cm along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    orange
  moves     freely
  rests     on ramp.deck, 5 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the geometry — the ramp's high and low points, width and thickness, the deck plank, and the leg post holding it up. For the cup, I'm thinking the ball should roll down the ramp and drop off the low end directly into the cup rather than hitting its walls, so I need to position the cup just past the ramp's foot at the right height for a clean drop.

I'm also figuring out how position clauses work for specifying the ramp's high and low ends (like so many cm up and along), and how to correctly reference the ball's placement on the ramp's deck surface rather than the ramp part itself, since the ramp is made of sub-pieces.

Working through the physics now: calculating the ball's exit speed from a rolling-sphere formula given a height drop, finding it comes out too fast for a short landing distance, and considering shrinking the ramp's drop or instead computing a projectile landing spot to place the cup there with dead-bounce physics. I'm leaning toward a shallower design where the ramp's low end sits flush with the floor and cup wall height, so the ball rolls directly in without launching off a ledge.

Computing the release velocity using rolling physics gives about 1.39 m/s at 14° below horizontal, so I'm breaking it into components and figuring out the ball's center height at release versus where it needs to land in the cup, then setting up the drop equation to solve for landing time.

I'm solving for the time to fall different vertical distances and getting horizontal landing positions around 0.2-0.26 m past the ramp's edge, and I'm checking whether the ball clears the near wall of the cup (10 cm tall) given its 3 cm radius — accounting for the offset between the ball's contact point and its center as it leaves the deck adds some uncertainty to the exact clearance.

Given this, I'll make the cup fairly generous — about 40 cm long, positioned so its near wall sits around 0.70 m and far wall around 1.10 m, with the expected landing point near 0.86 m giving good margin. I'm lowering the walls to 8 cm to reduce bounce-out risk while still keeping them taller than the ball's center height (5 cm), so the ball can't climb over even with horizontal momentum (~1.3 m/s) carrying it toward the far wall. After a dead bounce off the far wall and some rolling friction, the ball should settle within the cup in roughly 6 seconds, so I'm tuning the rolling friction to a moderate value to achieve that.

For placement, I'm positioning the cup as an open box on the floor, 90 cm along, following the pattern used for the raised bucket — specifying its base location directly rather than referencing a piece, since that's simpler and consistent with how similar parts are placed elsewhere.

Then I'm placing the ball on the ramp's deck, 5 cm from the top edge, giving it default across position, weight 100 g, and a 3 cm radius as a sphere. I'm checking that the ramp's width, thickness, and leg position don't interfere with the ball's path, so it should roll freely down the deck and land in the cup without touching the leg.

