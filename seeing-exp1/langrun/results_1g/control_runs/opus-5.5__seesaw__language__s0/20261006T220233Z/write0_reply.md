The seesaw rests with its ball end down, held by a 25° hinge stop either way, so it doesn't matter which way the hinge angle counts. A lip at that end holds the 100 g ball while it waits. The 1 kg weight falls about 1.4 m onto the raised end. My rough momentum estimate, not checked by running the scene, gives the ball about 4–5 m/s on the 50° swing up to the other stop. That would lift it roughly 1 m above its starting height, about double the 50 cm the brief asks for.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    30 cm up

fulcrum top
  is a  point
  at    26 cm up

fulcrum
  is a    post 4 cm square, from floor to fulcrum top
  colour  grey

seesaw
  is a      box 120 by 20 by 3 cm, 300 g
  colour    wood
  friction  0.8, spinning 0.005, rolling 0.002
  0 cm along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from -25° to 25°

lip
  is a         box 1 by 20 by 6 cm, 20 g
  colour       wood
  on           seesaw, at seesaw's near end
  attached to  seesaw

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on        seesaw, 55 cm behind pivot

weight
  is a      sphere 6 cm radius, 1 kg
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    dark grey
  moves     freely
  at        48 cm along, 2 m up

expect
  weight touches seesaw
  ball touches lip
```

---
thinking (summarized):

I'm designing a seesaw mechanism: a plank pivoting on a fixed fulcrum, with the ball end resting down and the weight dropping onto the raised end to launch the ball upward by at least 50 cm. I'm working out the plank's dimensions and pivot placement to balance the 1 kg drop against the 100 g ball's required launch height.

Computing exact ball placement from tilted geometry seems messy, so maybe starting the board level is simpler—though with the ball resting unevenly on one end, it'll naturally tip before the weight even lands. With a far end half-length of 60 cm and pivot height 30 cm, the end would hit the floor around 30°, so I could just let that be the natural limit rather than adding artificial stops.

But a tilted board also risks the ball rolling off toward the low end before the catapult even fires, so I'm thinking about adding a small lip or stop near the ball's resting end to keep it in place until the weight triggers the launch, like a scoop-back catapult. Alternatively, I could just start the hinge level with an asymmetric range—allowing it to rotate further toward the far end than the near end—so the near end can't dip below the starting position.

Working through the moment of inertia for the board plus ball plus weight, I'm modeling the weight landing as an inelastic collision to get angular momentum conservation, giving ω ≈1.22v. That translates near-end speed to about 0.67v, and to loft the ball 50cm high I need roughly 4 m/s at the tip, meaning the weight should hit around 6 m/s, requiring a drop height near 1.8 m.

Switching to a lighter 300g board lowers inertia so the transfer ratio improves to end speed ≈0.83v, and dropping the weight from 2m gives about 5.2 m/s at the tip — enough for a comfortable 1.4m apex. I'm now considering the ball's launch direction off the tilted, rotating board and whether it actually clears the edge before flying free.

Tracking the near end's position as the board rotates, I see it moves both upward and toward the pivot side, meaning the ball launches up and slightly toward the weight's x-position. Checking whether the ball's trajectory might intersect the weight mid-flight, I estimate roughly a 1-second flight time carrying it about 2m horizontally, putting its peak near x≈0.45 at a height around 1.1m — close enough to the weight's location that I should check for a collision.

Since the weight sits near ground level by the time the ball is mid-flight, there shouldn't be an actual collision; the weight will have already landed and settled. I also want to make sure the ball doesn't start right at the edge of the board (risk of rolling off), so I'll nudge its starting position a few centimeters inward from the near end, specifying it as a fixed offset behind the pivot.

Now I'm working out the support structure: a square post running from the floor up to just under the board, with the pivot point positioned so the board sits level and centered on it, accounting for board thickness.

I need to check clearance between the post top and the rotating board's bottom surface so they don't clip as the board tilts — computing how the corners of the board's underside shift vertically at the tilt angle to make sure there's enough gap above the post.

I'm also second-guessing whether MuJoCo's default contact filtering actually applies here, since the post is a static world body and the seesaw is its child — I need to verify whether the parent-child exclusion rule still kicks in when the parent is specifically the world body, since that would change whether a collision is even possible in the simulation.

To be safe regardless, I'll shrink the post to about 4 cm square with its top set 4 cm below the pivot (around 26 cm), confirming that at a 25° tilt the board's underside stays above that height with a small clearance gap. I'll keep the post collidable but just make sure there's no physical overlap, and I also check whether the far end of the board at max tilt stays clear of the floor.

For naming, I'll call the seesaw object "seesaw" and have it rotate on a hinge about the y-axis at the pivot point, matching the described spec. I'm now considering the swing range from 0° to 25° and making sure the sign convention for positive rotation about y matches MuJoCo's standard axis orientation.

I'm worried about the catapult's sign convention too — if reversed, the initial ball torque could tip the near end down immediately, dumping the ball before the weight even lands, causing failure. To stay robust regardless of sign, I'm considering a symmetric range like -25° to 25° or some other safeguard against premature tipping.

I'm working out the weight placement accounting for the tilted far end—landing around 0.5 m from the pivot works fine given the board's dimensions, and this setup is robust regardless of tip direction with more rotation helping gravity do its work. I'm also adding a small lip near the pivot end to keep the ball from sliding off during the tipping phase, attaching it as a block to the seesaw's near end.

I'm checking the ball placement too: positioning it centered just behind the lip with a small gap, offset slightly from the pivot, so that when the board tips, the ball rolls toward the lip and I need to verify the lip's height is sufficient to actually stop it given the ball's radius.

During the throwing motion, the board rotates so the near end lifts, pressing the ball against the board and driving it toward release. Since the ball moves up and inward relative to the board as it tips, the lip (positioned behind the ball) doesn't obstruct the launch — the ball's velocity stays perpendicular to the board surface, and at the release angle near 25°, I'm working out the resulting launch direction as the perpendicular vector rotates with the board.

I'm computing the moment of inertia contributions from the board, ball, lip, and weight, then using angular impulse from the falling weight's impact to estimate the board's angular velocity at release, which gives me the ball's launch speed.

Testing a weight drop of 1.5-2 m above the board gives impact speeds around 5-6 m/s, translating to ball speeds near 4.7-5.4 m/s with apex heights over a meter — plenty of margin for a visible launch. I'm settling on the weight centered 1.8 m up with a 0.5 m lever arm, and now working out the board's tilted geometry (far end height as it rotates up) to nail down exact positioning.

Checking the impact angle: the weight hits the slanted surface at roughly 25°, mostly delivering vertical impulse with minor slide. Then the ball launches near-vertically at that 25° tilt, so using cos25 for the vertical velocity component, the apex rise works out to about 0.84 m — solid and visible.

Now I'm tracing the ball's start height relative to the tipped board (around 0.11-0.56 m depending on tilt), estimating a release height near 0.56 m, giving a total apex around 1.4 m, which leaves good clearance margin. I'm also checking whether the soft limit at 25° needs custom solref settings, and whether the falling weight might land on the ball instead of the board — want to make sure that doesn't happen. Then I'm sketching the hinge board itself: a 120×20×3 cm box weighing 300 g, positioned at the pivot point.

I'm placing the pivot 30 cm up, with a fulcrum post running from the floor to a point 26 cm up (4 cm below the pivot), checking that at ±25° tilt the board clears the post by a safe margin (~27.8 cm minimum vs 26 cm post top).

Now I'm adding the weight as a 1 kg sphere positioned 50 cm along and 2 m up, set to move freely with dead bounce, and the ball as a small 100 g sphere resting on the seesaw 55 cm behind the pivot, rolling and subject to friction so it can shift toward the lip as the board tilts.

I'm defining a thin lip box (1x20x6 cm, 20 g) attached to the seesaw at its near end to act as a stop, skipping damping and small armature details for simplicity. I'm also checking whether the weight actually makes contact with the tilted far end given the geometry — working through the sphere's contact offset along the slope to confirm it lands correctly rather than missing the board.

