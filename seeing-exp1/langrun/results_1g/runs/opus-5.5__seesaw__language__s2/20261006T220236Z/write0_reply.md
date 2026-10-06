The seesaw rests level on its pivot, with its ball end on a fixed block so the 100 g ball can't roll off. The 1 kg weight falls about 1.2 m onto the far end, which drives that end down to the floor.

A rough estimate:
- **Rotation:** the near end and the ball rise about 23 cm.
- **Launch speed:** about 3.5 m/s at the moment the far end strikes the floor.
- **Flight:** that speed adds roughly another half metre of climb, so the ball should rise well over 50 cm.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    0 cm along, 25 cm up

seesaw
  is a      box 120 by 30 by 4 cm, 600 g
  colour    wood
  friction  0.8, spinning 0.01, rolling 0.004
  at        0 cm along, level with pivot
  turns on  seesaw hinge, about y, at pivot

stand
  is a    post 6 cm square, from floor to seesaw's bottom
  touches nothing
  colour  grey

rest block
  is a    box 10 by 30 by 23 cm
  colour  dark grey
  on      floor, at seesaw's near end

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on        seesaw, 55 cm behind pivot

weight
  is a      sphere 5 cm radius, 1 kg
  friction  0.8, spinning 0.01, rolling 0.004
  colour    black
  moves     freely
  at        55 cm beyond pivot, 1.5 m up

expect
  weight touches seesaw
  seesaw touches floor
```

The expectations only confirm the weight lands on the seesaw and the far end reaches the floor. None of the available forms checks how high the ball goes, so the 50 cm rise has to be read from the run itself.

---
thinking (summarized):

I'm designing a seesaw with a plank on a pivot, sized around 1.2 m long with the pivot raised about 20 cm off the ground. The idea is the ball-side starts low near the floor while the weight-side is elevated, so dropping the 1 kg weight launches the 100 g ball at least 50 cm.

Working through the physics: I'm computing the board's moment of inertia, treating the weight's impact as an inelastic collision to find the board's angular velocity, then deriving the ball's launch speed from the arm length. Testing a drop height of 1.5 m gives an impact speed around 5.4 m/s, translating to roughly 4.3 m/s for the ball and a projected rise near 0.94 m, comfortably clearing the 50 cm target.

I'm now reconsidering the setup geometry — the ball needs to stay resting on the board's low end rather than rolling off, which means the board should start tilted with the ball-end down against the floor, and the weight drops onto the opposite raised end to trigger the launch.

Lowering the pivot to 10 cm with the same half-length gives about 9.6°, shallow enough that the lip can manage the ball. I also figure the board naturally stops when the weighted end hits the floor, so I don't need an extra mechanical stop. Now I'm working out rotation direction around the y-axis: positive angle tips the far (+x) end down, so I'll place the ball near end (−x) and weight at the far end (+x), starting with the ball end down and weight end up.

I'm wrestling with whether the board should be authored level with the hinge qpos set to a negative angle, or authored already tilted from the start — if it's level and then rotated via qpos, placing the ball relative to the level geometry could put it in the wrong spot once tilted. It seems cleaner to define the seesaw directly as a sloped plank between two points, hinge it at the pivot with range starting at zero, and then describe the ball's position as resting on the plank, measured down from its high end.

I'm now trying to nail down the actual geometry: pivot height, board thickness, and the low/high end coordinates so the plank's endpoints make physical sense with the floor and the pivot point.

I realize a post directly under the pivot would collide with the rotating board, so I need to rethink the stand design — maybe placing supports on either side of the board instead of underneath it, to avoid interpenetration.

Actually the seesaw itself can hit the floor at its low end, so that naturally acts as the rotational stop rather than needing a separate limiter. I need to define the hinge range relative to the tilted rest pose and work out exactly where the board's corner touches the floor given the tilt angle, so the floor contact and hinge limits line up correctly.

Actually I'm not confident about the sign convention for positive angles, so a hinge range risks being wrong and leaving it stuck. Safer to skip the range and rely on floor contact instead — nudging the low end up by a fraction of a millimeter so the bottom corner just clears the floor, letting gravity settle it naturally, with the far end striking the floor symmetrically once it rotates.

Then there's the question of plank thickness: whether the defining points are the centerline or the top surface changes where the bottom corner actually sits, so I need to bump the low end height up enough (say to 4.5 cm) to avoid penetrating the floor regardless of which convention is used, adjusting the high end and pivot position to match.

Placing the pivot at 24.5 cm up seems reasonable for a 30 cm wide, 4 cm thick plank around 0.6 kg. For attaching a box near the seesaw's end, since the plank tilts but the box stays axis-aligned, I'm unsure how to compute its resting height on a sloped surface cleanly, so I'm considering avoiding this lip-and-box setup altogether in favor of something simpler.

Since a sphere will naturally roll on an 18° slope due to MuJoCo's sliding friction inducing rotation, I need an actual stop rather than relying on friction alone. Rather than tilting the board, I'm leaning toward keeping the board level and adding a fixed support block under the near end so the ball just sits there without rolling.

I need the ball positioned flush with the board's near end, so I'll place it around 55 cm behind the pivot to match that edge. For the board itself, I'm modeling it as a box 120 by 30 by 4 cm weighing 600 g, positioning it level with the pivot height and centered along the pivot axis.

The pivot sits at 25 cm up with default alignment, giving the board a bottom face at 23 cm and top at 27 cm, hinged along the y-axis and named "seesaw hinge." I'm adding a support block (10 by 30 by 23 cm) on the floor under the near end of the seesaw so its top surface touches the board's bottom exactly, creating a resting contact point.

For the stand, I'm placing a single 6 cm square post running from the floor up to the pivot's location, anchored at the seesaw's bottom face center so it supports the hinge without needing extra alignment logic. Now I'm starting to work through the impact dynamics, calculating the board's moment of inertia using its mass and length to set up the physics of the seesaw motion.

Working through impact speed (v≈4.43) giving ball speed ~3.3 m/s and a ballistic rise of 0.56 m, adding to the 0.23 m from rotation for a total near 0.8 m — with gravity actually aiding torque during the fall, giving good margin from a 1.2 m drop. I'm checking the geometry: the near end rises with velocity perpendicular to the board at 24.6° from vertical, heading toward the pivot side, with effective height loss scaled by cos²(24.6)=0.83, and considering whether the ball might separate from the board earlier than assumed.

Now I'm sizing the weight itself: a 1 kg sphere at radius 5 cm gives density ~1910, reasonable, and I'm placing it 55 cm beyond the pivot at 1.2 m height, checking it lands within the 30 cm board width. Working out the drop distance (0.88 m) and resulting impact velocity (4.15 m/s), then testing a higher 1.5 m placement for a 1.18 m drop and 4.8 m/s impact, which pushes the ball speed to 3.6 m/s — a better margin. I'm also considering whether the weight should have bounce disabled on impact.

Default elastic bounce seems fine, keeping things lively enough to transfer energy properly. I'm double-checking the far end doesn't clip the floor awkwardly and that the weight won't roll off unexpectedly. The ball — a 3 cm, 100 g sphere placed 55 cm behind the pivot — stays within the board bounds, and rolling friction should keep it steady without needing explicit roll behavior, since the only interaction forms available are touching, coming to rest, dropping through, or reaching a lower stop.

I'll use "weight touches seesaw" and "seesaw touches floor" as the relevant interactions. For the support block, naming it "rest block" positioned flush at the seesaw's near end with a 10 cm length seems right, and I'm confirming the far end can freely drop since the board clears the floor there, with the pivot post not touching anything. Now I'm finalizing the position lines — pivot at 25 cm up, seesaw level with the pivot — and considering whether to specify additional zero-offset details.

