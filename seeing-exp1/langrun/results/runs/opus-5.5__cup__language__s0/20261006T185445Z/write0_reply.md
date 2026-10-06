The ball starts near the top of a sloping ramp and rolls down. It leaves the low end just above the cup's low near wall and drops onto the cup's base. The taller far wall stops it, and its dead bounce and rolling friction let it settle inside well within 6 s.

```world
world  ball down a ramp into a cup

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

-- the ramp drops 20 cm over 1 m; its low end overhangs the cup's near wall
ramp
  is a       ramp
  high end   0 m along, 35 cm up
  low end    1 m along, 15 cm up
  width      20 cm
  thickness  4 cm

-- an open box whose near wall (12 cm) sits just under the ramp's low end,
-- so the ball clears it and drops in; the other walls are taller to stop it
cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             16 cm
  near wall height  12 cm
  its base 1.17 m along

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out how to set up the ramp's geometry in this world-building language — thinking through how to express the high end as a point with a height offset, plus the deck plank and leg post dimensions needed to construct the scene.

I'm figuring out whether low end sits at floor level and how plank thickness interacts with it, noting that static world geoms don't actually collide with each other so overlap at joints isn't an issue. For the leg post, I'm placing it under the plank's high end using matching coordinates, and for the cup I'm considering how to position it as an open box on the floor using a relative placement clause like the ball-relative example, so the ball can eventually roll down the ramp and land inside it.

The trickier part is getting the ball to actually settle in the cup rather than bouncing out — I'm weighing whether to lower the near wall so the ball rolls in freely while the far wall stops it, versus having the ramp's low end positioned so the ball launches or drops directly into the box. I'm running the physics for a solid sphere rolling off the ramp, computing the drop height and resulting velocity using rotational inertia factors, to see if the ball would land gently or fly in too fast.

Actually a deep open box sitting on the floor with the ramp feeding into its near wall top makes more sense—ball falls in, bounces around with dead restitution and rolling friction, and the walls are tall enough it can't escape after losing energy. I'm trying to figure out how rolling friction works in MuJoCo and whether the ball will actually settle within six seconds given repeated wall collisions.

Right, with that friction level the ball might not roll at all on a gentle slope, so I need the ramp steeper — maybe a 45cm to 12cm drop over 0.9m gives sinθ≈0.344, producing enough acceleration (~2.41 m/s²) to overcome rolling resistance. I should also double check spinning friction doesn't cause issues.

Checking the exit speed: dropping about 0.3m gives v≈2.05 m/s at the bottom, still quick even after friction losses. The ball exits around 18cm height and needs to land in the cup, which is a 40cm box with 15cm walls — working out the fall of roughly 12cm to hit the cup's base center height of 6cm, so I'm calculating the fall time from that drop.

Factoring in the downward velocity component from the slope angle, the fall time comes to about 0.10s, and with horizontal speed around 1.93 m/s that puts the landing point about 19cm into the cup — comfortably inside the 40cm length. After landing it'll likely roll and hit the far wall at ~1.9 m/s, bounce back dead, then possibly roll toward the near wall, which at 15cm is tall enough to contain it.

Let me try a gentler ramp instead — 35cm high, 15cm low, over 1m length — giving a shallower angle and net acceleration near 1.0 m/s² after friction, so exit velocity drops to about 1.34 m/s, which seems more manageable. I'm now checking what height the low end of the plank sits at relative to the cup opening.

I need to figure out where the cup should sit near the ramp's low end so the ball clears the near wall but still drops into the cup. I'm also reconsidering the heights of the near and far cup walls based on the ball's exit height, and noting the ramp needs proper support at its low end since currently it's only anchored at the top.

Let me shift the cup so its near wall sits at x=0.97, base centered at 1.17 m, giving enough clearance against the plank's end height. Then I'm working out landing dynamics: horizontal speed ~1.31 m/s, vertical ~0.26 m/s, with the ball dropping from 21 cm to 6 cm center height, solving the quadratic for time to impact.

Solving that gives t≈0.15 s, so horizontal travel is about 0.197 m, landing the ball near center of the cup, well clear of the far wall at 1.36 m. For placement phrasing, I'm deciding that "on ramp, 12 cm from the top" should fully fix the ball's position along the plank, trusting that convention rather than needing separate across-axis centering.

Now I'm working out how to define the ramp as a part — specifying high end, low end, and width, with height measured "up" and position "along," checking that defaults like along=0 apply correctly at the high end. For the cup, I'm figuring out how to anchor its base position along the floor using an absolute distance rather than a relative clause tied to the ball.

For the cup's walls, I'm setting the near wall height to 12 cm (short enough that the ball can't climb back out after hitting the far wall) and other walls to 16 cm, with a 30 cm width and default 2 cm thickness. I'm deciding to skip part colors since those likely aren't settable, but giving the ball an orange color, 100 g mass, 4 cm radius, dead bounce, and friction values (0.9 sliding, 0.005 spinning, 0.002 rolling) — then checking that after the ball hits the far wall around 1.3 m/s and rebounds, rolling friction deceleration of about 0.35 m/s² will bring any small rebound to rest well within the 6 second window.

