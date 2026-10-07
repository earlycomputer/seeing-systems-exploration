The ball rolls down the ramp onto a raised shelf and topples three short dominoes. The last domino nudges `ball2` off the shelf's far edge, and it drops into a cup on the floor.

- **Domino height:** the dominoes are 8 cm tall and `ball1` has a 5 cm radius. That puts the hit near two-thirds of the domino's height, so it tips forward instead of sliding.
- **Ramp joint:** the ramp runs into the shelf, so the change from ramp to shelf is smooth whichever way the plank's thickness is laid.
- **Cup position:** the cup's near wall sits flush under the shelf's edge, so even a slow `ball2` falls straight in.

I haven't run this, so the expectations at the end still need checking against an actual run.

```world
world  ramp, dominoes and cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    0 m along, 38 cm up

ramp foot
  is a  point
  at    1.2 m along, 28 cm up

shelf
  is a      box 80 by 30 by 30 cm
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    wood
  stands    on floor, 1.3 m along

ramp
  is a      plank from ramp top to ramp foot, 30 cm wide, 4 cm thick
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    wood

ramp leg
  is a    post 6 cm square, from floor to ramp top
  colour  grey

ball1
  is a      sphere 5 cm radius, 60 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on ramp, 20.4 cm from the top

d
  is a      box 1 by 5 by 8 cm, 30 g
  friction  0.6, spinning 0.005, rolling 0.0001
  colour    white
  moves     freely
  repeated  3 times, 6 cm apart along
  stands    on shelf, 1.45 m along

ball2
  is a      sphere 2 cm radius, 20 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on shelf, 1.625 m along

cup
  is an     open box
  length    30 cm
  width     30 cm
  walls     15 cm
  friction  0.8, spinning 0.005, rolling 0.002
  bounce    dead
  colour    grey
  on        floor, 1.84 m along

expect
  ball1 touches d1
  d1 touches d2
  d2 touches d3
  d3 touches ball2
  ball2 comes to rest in cup
```

---
thinking (summarized):

I need to think through the ramp geometry and physics setup carefully, considering how the fixed starting ramp's deck and leg pieces should be named so the checker can correctly identify the geom it expects.

Defining the plank between two height-specified points, deciding whether it represents the centerline or top surface, and figuring out how "1 m up ramp" translates to ball placement relative to the ramp's length and the floor contact at the bottom edge.

Using a shallower slope gives a more reasonable speed around 1.8-2.3 m/s, with rolling friction having minimal effect over such a short distance. For the dominoes, I'm sizing them like typical toppling dominoes — maybe 2 by 8 by 16 cm — scaled up a bit from standard size.

Now I'm thinking about where the ball actually strikes the domino relative to its center of mass. Hitting too low near the base risks kicking the bottom out and tipping the domino the wrong way, so I need the contact point high enough above the domino's COM to tip it forward reliably — which means balancing ball radius against domino height so the collision point lands above center.

The torque at the forward bottom edge equals the hit height, so any horizontal push above the floor tips the domino forward regardless of slip, and the heavy fast ball should topple it into the next one. I'm now considering tweaking dimensions further—maybe a smaller ball radius and a lighter, narrower domino—to make sure the geometry works cleanly for the chain reaction.

For the final stage, d3 needs to knock ball2 into the cup. I'm thinking ball2 rests on the floor ahead of d3, and when d3 topples it pushes the ball forward, rolling it along the floor toward an open-topped cup—likely with one wall lower than the others so the ball can roll over it easily.

The ball ends up with modest forward speed, rolling on the floor toward the cup. I'm wondering whether the cup can sit flush with the floor, or if I need a small ramp or thinner base so a low step doesn't stop the ball from entering—checking whether a shallow 5mm lip is small enough for a 3cm-radius ball to roll over without extra energy.

But then I realize the real risk: once the ball hits the far wall and bounces, it could roll back out through the open near side where the lip is tiny. I need enough friction or rolling resistance to kill that rebound so the ball actually settles inside the cup rather than escaping.

Maybe a cleaner fix is to have ball2 drop into the cup from above instead — rest it on a small platform adjacent to the cup, so when domino 3 knocks it off the platform's far edge, it falls straight down into the cup below rather than rolling in horizontally and risking a bounce-out.

I'm thinking through where to place a low platform (around 4 cm tall) holding ball2 just ahead of the falling domino, so the domino's rotating edge clears the platform's near side and its upper body strikes the ball as it sweeps forward.

Better idea: elevate the whole domino setup on a raised table so ball2 can fall off the table's far edge into a cup sitting on the floor below, rather than trying to make the ball clear a wall on the same level.

I'm estimating the fall physics—given the table height and expected push speed, the ball should travel roughly 12-50 cm horizontally before landing, so I need to size the cup length and wall heights generously (around 40 cm long, walls near 25 cm tall) to make sure it lands inside and doesn't bounce out.

Now I'm working out how domino d3 actually strikes ball2. The domino's height and thickness, plus ball2's radius and position on the table, determine the geometry: as the domino tips forward at angle θ, I need to check the distance from ball2's center to the domino's falling face to confirm contact happens at the right moment and pushes the ball forward reliably.

Checking the ramp-to-table transition: the plank's foot sits at table height, dropping only about 2 cm onto the table surface, so ball1 should roll smoothly from ramp onto table without issue since the geometries are both fixed and don't conflict. I'm also considering just skipping the table setup entirely and simplifying the layout.

I also need to check table width—30 cm should be fine for ball1 rolling straight without falling off the side. There's a question of whether ball1, after hitting domino d1, keeps enough momentum to also hit ball2 or interfere further down the line; given ball1 is much heavier (300g vs 60g domino) at 2 m/s, it'll likely plow through with most of its speed retained, which could complicate the intended sequence.

To fix this, I should make ball1 lighter or the dominoes heavier, and slow the ball down. Reworking the ramp: top at 45 cm, bottom at 30 cm, length about 1.1 m, giving a shallow slope around 7.8° and a height drop of roughly 13.6 cm, which works out to a starting speed near 1.38 m/s for the ball—manageable and physically reasonable. The ramp itself can just be a fixed plank without needing support legs.

Adjusting further, I settle on the ramp's high end at 50 cm and low end at 30 cm with a 1.2 m horizontal run, giving a total length around 1.217 m and a slope angle where sinθ≈0.164, so the ball drops about 16.4 cm and reaches roughly 1.52 m/s—better. For masses, I'm estimating ball1 as a 3 cm radius sphere around 100 g, and the dominoes (1.5×8×16 cm wood blocks) computing out to about 134 g at 700 density, though I'll round to 100 g for simplicity, then check where ball1 strikes the first domino.

Now I'm working through whether the impact height of 3 cm is low enough to tip the domino forward given 0.8 friction—analyzing the impulse at that height, treating the domino as pivoting about its far bottom edge, estimating the moment of inertia about that edge, and checking whether the required friction impulse stays within the friction cone for forward rotation versus sliding.

Since the needed friction (about 0.72J) exceeds what's available (normal impulse too small, around 0.9J max), I realize the base will slide instead of catching. That means the domino undergoes combined translation and rotation rather than pure pivoting, and since the hit is below the center of mass, slipping causes the top to rotate backward toward the ball instead of forward—which is the wrong direction. This tells me the contact point needs to be near or above the center of percussion, not below the COM, for the domino to tip away properly.

So I'm working out that pure rotation about the base with zero friction requirement happens when the strike height equals 2/3 of the domino's height. That means I should size the ball so its radius is close to that fraction of domino height—trying combinations like a 9cm domino with various ball radii, settling on something like a 5cm radius ball against an 8cm domino where the hit point (5cm) nearly matches the ideal 5.33cm, minimizing needed friction. I'm also working out domino spacing (under 8cm height) and the geometry of how the first domino strikes the second using the Pythagorean relationship between spacing and height.

Now I'm tracking the chain further: checking where domino1's top edge lands on domino2's face given the gap after subtracting thickness, confirming the contact height (6.2cm) sits comfortably above the 2/3 threshold. Then I'm moving to the next stage—domino3 falling onto ball2 resting on the table—and solving for the tipping angle where the domino's edge meets the ball's surface, testing angles like 50°, 53°, and 60° to find where the geometry works out with the ball's 2cm radius and 6cm spacing.

I'm now reconsidering the scale of the whole setup, weighing a bigger domino/ball system (1.5×8×15cm, heavier ball) against sticking with smaller components (1×5×8cm domino, 5cm radius ball around 150g), and thinking through the momentum transfer—a 150g ball at 1.5 m/s hitting a 30g domino would still carry forward at roughly 1 m/s and could continue knocking into subsequent dominoes, which actually works in my favor since it just continues the toppling chain regardless.

Now I'm checking whether this residual ball momentum might collide with the next ball or interfere with the cup drop, and since toppling a domino barely requires energy (the center of mass barely rises when it falls), I realize I can safely use a lighter 40g ball and a gentler ramp—dropping the height to 40cm start and 30cm end over a 1.2m horizontal run should be plenty.

I'm recalculating the slope: with a 1.2m span and 10cm drop, sinθ comes out around 0.083, giving the ball a velocity near 1.08 m/s at the bottom, which should be enough to topple a domino without overshooting. I also need to account for how the ball transitions from the end of the ramp onto the table—if the ramp's foot is set too high, the ball will drop an extra couple centimeters before reaching the table surface, so I'm considering adjusting the foot height to around 28cm so the ramp's top surface lines up flush with the table instead of creating an awkward little drop.

I'm reconsidering whether the leg post reaching the deck centerline confirms the centerline assumption, with foot at 28 cm. As an alternative, if the ramp foot extends slightly into the table, the plank's top surface would cross the table top somewhere, allowing a smooth transition regardless of the exact height interpretation, so I'm checking where that crossing point lands if the foot is 10 cm inside the table.

Actually the top-surface reading works better: plank top meets table top 24 cm before the foot, inside the table region, then the plank continues below the table surface — no discontinuity. So I'll set up coordinates with the table as a box, ramp top point raised 38 cm, foot point at 1.2 m along raised 28 cm, giving slope 0.0833 and ramp length about 1.2042 m, with ball1 placed 1 m up the ramp from the bottom.

Measuring the ball 1 m along the ramp from its low end gives a height drop of about 8.3 cm, so exit speed should be roughly 1.08 m/s before accounting for rolling losses — and resting it directly on the ramp surface keeps the initial placement consistent. For the table itself I'm treating it as a shelf box, positioning its near edge so the ramp's foot sits about 30 cm inside it.

Then I'm working out the domino spacing on the table: with dominoes 6 cm apart starting near where the ramp meets the table, the third domino's far face lands around 1.575 m, putting ball 2's center about 6 cm beyond that at roughly 1.635 m. Since the table's far edge is at 1.9 m, ball 2 only needs to roll about 25 cm to reach the edge, and with rolling friction being small it should still have modest speed — maybe 0.3–0.5 m/s — by the time it gets there.

I should lower rolling friction values much more to keep both balls moving rather than stalling—setting shelf, ramp, and ball rolling friction to 0.0001 instead of 0.002, which should cut deceleration significantly. I'm also repositioning ball2 nearer the shelf's far edge, around 1.635, leaving just enough runway before it drops off.

Now I'm working out the cup's placement beyond the shelf—it needs its near wall flush against the shelf's far end at 1.70, with the open box base being 30cm long and walls 20cm tall, 2cm thick. I'm figuring out whether to position it by center or by referencing the near wall directly, settling on placing the base so its near end aligns right at the shelf's edge.

I also need to check the near wall height — with 15 cm walls, even a slow ball should clear it since it's falling from well above, so that's fine. But I should check the edge case of a very slow ball barely rolling off: with tiny speed, the center stays near x=1.70 as it falls, which could clip the near wall's top edge rather than landing safely inside.

Since fixed geoms don't collide with each other, I can just embed the near wall inside the shelf's footprint (say spanning 1.68–1.70) so the cup's interior starts exactly at the shelf's far face, letting a slow ball slide straight off the shelf into the cup without hitting any wall edge.

Now I'm working out how fast ball2 would be moving after domino d3 strikes it — estimating the domino's angular velocity from energy conservation as it tips through 53°, then converting that to the contact point's velocity components (roughly 0.43 m/s horizontal, 0.58 m/s vertical) to see how much push it transfers to the ball.

I'm reconsidering the geometry so the ball doesn't get pinned under the domino, adjusting the ball's placement so the contact angle gives more horizontal push rather than vertical, and solving for the right distance from the far face (testing θ around 15-23° to get contact height near 2 cm).

Then I try a 4 cm gap instead, checking θ near 35-37° and computing the resulting contact point, the drop in center-of-mass height, and the angular velocity that would produce — estimating the point speed at impact and its horizontal component.

I'm also sanity-checking the chain of collisions: ball-to-domino alignment heights, ramp-to-table transition, and ball1's mass and radius placement on the ramp to make sure it strikes domino 1 squarely.

Keeping ball1 solid (not hollow) so its speed down the ramp follows standard solid-sphere rolling dynamics. After hitting the first domino, ball1 loses most of its speed but continues forward, likely following the toppling dominoes and possibly ending up in the cup alongside ball2, which should still fit given the cup's dimensions.

For ball2 settling in the cup, I need friction values that stop it from bouncing forever but still allow some motion—setting cup friction around 0.8 with low rolling resistance so it settles within a few seconds. I'm also setting domino-to-shelf and domino-to-domino friction at 0.6, and double-checking the shelf's position and dimensions to make sure the ramp and dominoes are placed correctly along its length.

Now I'm verifying ball1's trajectory as it transitions from the ramp to the shelf, checking that the crossing point and rolling path line up so it reaches the first domino without gaps. I'm also setting up the three dominoes using a repeated naming pattern (d1, d2, d3) spaced 6 cm apart along the shelf, confirming their positions relative to the ramp's edge.

For ball2, I'm placing it on the shelf at 1.625 m along, calculating that position based on domino d3's far face plus the ball's radius and a small gap, so it rests just behind the third domino without overlapping.

Now moving to the cup — an open box with 30 cm length and width, 15 cm walls, sitting on the floor at 1.84 m along. I notice its near wall would overlap the shelf's edge zone, but since they're on different surfaces (floor vs shelf height) that's not an actual collision, and I'm working out whether part positions reference the base's origin point.

I'm sketching the chain of contacts: ball touches d1, d1 touches d2, d2 touches d3, d3 touches ball2, and ball2 settles into the cup. I'm setting friction and rolling resistance values on the ramp plank, and considering whether to add a supporting post under the ramp for visual stability, figuring out how its height and position should be specified relative to the floor and ramp endpoint.

Now I'm working out the exact coordinates for the ramp's top and foot points, deciding on explicit "along" and "up" values, and defining the plank itself with its width and thickness. I'm also placing ball1 at a specific distance from the ramp's top edge, keeping its lateral offset at the default.

