The pendulum is a 100 g bob on a 50 cm hinge, started horizontal at 90° so it drops exactly 0.5 m to its lowest point. There it strikes `ball1`, the first of four equal lively balls set 15 cm apart (centre to centre) on a level rail. The impacts pass down the row to `ball4`, which rolls off the rail's end, over the box's low near wall, and is stopped by the dead, high-friction box.

I haven't simulated this, so a few points are uncertain:
- **Swing direction:** a positive 90° turn about y should put the bob behind the rail so it swings forward, but I haven't confirmed the hinge's sign convention.
- **Impacts:** without `lively` contacts the impacts would soak up most of the speed. I'm relying on them to carry the motion down the row. The balls also pick up spin from the rail, so more than one ball may follow `ball4` into the box.
- **Placement syntax:** `its base 1.3 m along`, which places the box by its base with an absolute offset, is a guess at valid syntax.

```world
world  pendulum chain into a box

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    65 cm up

pendulum
  is a           sphere 3 cm radius, 100 g
  bounce         lively
  colour         grey
  50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  90°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       5 g
  touches nothing
  colour       dark grey
  attached to  pendulum

rail
  is a      box 100 by 10 by 12 cm
  friction  0.6, spinning 0.002, rolling 0.0005
  colour    wood
  on floor, 53.5 cm along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.5, spinning 0.002, rolling 0.0005
  colour    orange
  moves     freely
  repeated  4 times, 15 cm apart along
  on rail, 6.1 cm along

box
  is an             open box
  length            50 cm
  width             30 cm
  walls             20 cm
  near wall height  8 cm
  bounce            dead
  friction          0.9, spinning 0.01, rolling 0.02
  colour            white
  its base 1.3 m along

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

I'm planning a Newton's cradle-style chain reaction where a pendulum strikes a sequence of balls spaced 0.15 m apart, with the final ball rolling into a box to rest, and working out how to structure the pendulum and ball parts physically.

I'm calculating the pendulum geometry: with a 0.5 m length arm starting at a 90° horizontal release, it swings down to hit the first ball at about 3.13 m/s, transferring momentum down the chain so the last ball rolls off the rail at reduced speed and drops into a waiting box.

I'm also worried about MuJoCo's default contact solref being fairly damped, which could make collisions behave more inelastically than a clean elastic transfer—so the bob and ball1 might partly stick together and move at a shared reduced speed rather than cleanly swapping momentum.

So I should set `bounce lively` on the balls and bob to boost restitution and get a proper elastic chain reaction through ball2 to ball4. For the rail, I'm thinking a flat box about 1.2 m long and 10 cm wide should keep balls rolling straight if struck centrally, with the pendulum pivot height set relative to the ball center height.

I'm settling on ball radius 3 cm and mass 100 g, with the bob also a 3 cm sphere at 100 g, keeping the rod mass small so it doesn't dominate the collision dynamics. I need to check whether the rod hanging down to the bob's top could physically intersect with the balls at rest height, since the rod capsule extends and its endpoints matter for collision geometry.

Checking the contact geometry more carefully, I convince myself the rod won't actually touch the balls given the lateral offsets involved, but I decide to make the rod non-colliding anyway just to be safe. Now I'm working out the pendulum's swing direction — it should start pulled back and swing forward to strike the first ball, so I need to get the rotation about the y-axis oriented correctly.

I need to make sure the bob doesn't collide with the rail at the bottom of its swing. If I position the rail's near end just past the bob's swept path, like starting around x=0.035 while the bob swings between −0.03 and 0.03, the ball sitting on the rail at x≈0.065 should stay clear while still lining up for a center-to-center impact at matching heights.

Continuing the spacing, ball4 sits at 0.515, leaving 0.52 m of rail before it rolls off the end at ~2 m/s. I'm working out the fall trajectory: with the rail top at 10 cm and the ball center at 0.13 m height, it drops about 0.1 m, taking roughly 0.14 s and carrying it forward about 0.28 m. So the box needs to catch it there — I'm sizing the box at 50 cm by 30 cm with 15 cm walls, but the near wall facing the rail needs to be shorter than the ball's arc so it doesn't block the incoming ball before it lands inside.

Working through the drop distance, the ball hits the far wall at roughly 0.32 m if the box is 40 cm long, and I'm worried about bounce-back behavior given uncertain restitution mixing between lively balls and a dead box. I need to size the near wall carefully—maybe 5 cm—so a ball bouncing back doesn't roll out, while keeping the far wall tall enough (perhaps 20 cm) to contain the initial impact.

Raising the rail height to 12 cm clears the ball properly and lets the near wall sit around 7-8 cm, which should stop a rolling ball without marginal edge cases. I'm also considering small rolling friction on the balls to settle motion naturally, and noting that ball3 might pick up some velocity from imperfect elastic collisions and drift toward the box too.

Rail width at 10 cm with a 3 cm radius ball centered should keep it from rolling off sideways without needing a groove. For box placement, I'm positioning it so its base sits along the rail's far end, using a relative placement clause to fix the along-axis position while keeping the box length at 50 cm.

Checking the trajectory: the ball exits the rail at 1.035 with a 5 mm gap to the near wall, clearing the near wall's 8 cm top easily since the ball's bottom sits at 12 cm. At 2.5 m/s it lands around x≈1.36 within the far wall boundary and rolls to stop there; even at 1 m/s it lands around 1.17, still inside. With the box walls dead and the ball lively, I'm now considering whether rolling friction brings it to rest within six seconds after bouncing inside.

Estimating rolling resistance deceleration using μ_r·g/r with the 5/7 factor for a rolling sphere gives roughly 0.47 m/s², so a ball starting around 1 m/s after bouncing would stop in about 2 seconds. Applying that same deceleration along the rail, I'm working out how much speed ball4 loses over its 0.52 m travel at 2.5 m/s.

I'm setting the box's base to have higher rolling friction (like 0.01) so the ball comes to rest quickly there, while the rail itself keeps lower rolling resistance. Checking the overall timing now — the pendulum swing, chain reaction, and ball4 reaching the rail end all fit comfortably within a second, with plenty of margin, and I'm noting that the pendulum bob might keep oscillating and strike ball1 again afterward, which seems fine.

I'm using condim 6 ("rolls") on the balls for proper rolling contact, and working out the pivot geometry: the bob's center at rest should align with the ball height, pivot point above it, and the initial 90°-rotated position placed so the bob drops the full 0.5 m height as intended.

Now I'm fine-tuning the gap between the bob and ball1 so impact happens almost exactly at the bottom of the swing, settling on a small 1 mm clearance (0.061 vs 0.06) to avoid starting in contact, then starting to write out the pivot and position definitions for the world description.

I'm defining the pendulum sphere (3 cm radius, 100 g, lively bounce) hanging 50 cm below the pivot, hinged about the y-axis and starting at 90°, plus a thin connecting rod (1 cm thick, 5 g) running from the pivot to the pendulum's top — though I need to double check the rod's reference to the pendulum's starting position works correctly given the ordering.

Next I'm placing a wooden rail box (100×10×12 cm) on the floor at 53.5 cm along, then repeating four balls spaced 15 cm apart along the rail, positioned 6.1 cm along it so "on rail" sets their height while the along/across offsets place them individually — need to confirm the repeated copies position correctly relative to each other.

Now I'm working through the physics of the collision chain: ball1 slides then transitions to rolling via friction (0.6), carrying spin (0.002) with low rolling resistance (0.0005) on the rail versus higher rolling resistance (0.02) in the box. Since ball1 retains spin after an elastic hit with ball2, it reaccelerates forward and can strike ball2 again, potentially pushing several balls forward in sequence until they roll off into the box — which is fine since the goal is just for ball4 to end up resting inside the box.

I'm considering lowering sliding friction to around 0.2 so balls slide more rather than spin excessively, but decide to keep it near 0.5 for simplicity. For the box itself, I'm setting it up as an open container 50 cm long, 30 cm wide, with 20 cm walls and an 8 cm near-wall height, using dead bounce, high friction (0.9), and modest spin/rolling resistance (0.01/0.02), positioning it with "its base 1.3 m along" the floor — checking whether that offset syntax is valid for placing the whole part.

I'm verifying the chain reaction: the pendulum bob (105 g including rod) hits ball1, which cascades through ball2 and ball3 to ball4, which should settle inside the box after falling about 10 cm from its initial height to the box floor. I'm also double-checking that the pendulum, after striking ball1 at its lowest point, continues swinging forward along its arc without hitting any rail or obstruction.

