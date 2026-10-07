The ball rolls 1 m down a 15° ramp onto a ledge and strikes a hanging paddle. The paddle's lower edge swings into a free slider on the ledge. The slider nudges the block, which already overhangs the ledge's far end by 2 cm, so it tips off, falls through a ring below the edge, and lands in an open box on the floor.

I haven't run this; these are hand estimates. The ball should reach about 1.8 m/s and the slider about 0.9 m/s, so the whole chain should finish within the first two seconds.

Two loose ends:
- **What happens after the strike isn't controlled.** The ball and slider may roll off the ledge and fall onto the hoop or into the box too.
- **A few readings of the language are guesses.** I took `N up` to set an object's centre height. I took a plank's end points to lie on its centre line. If either is wrong, the paddle-to-slider overlap or the ramp-to-ledge join would shift.

```world
world  ramp ball paddle slider block hoop box

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

-- deck runs 1.2 m at 15°, its foot meeting the ledge top at 80 cm
ramp
  is a      ramp
  high end  34 cm along, 109 cm up
  low end   1.5 m along, 78 cm up
  width     30 cm
  friction  0.8, spinning 0.001, rolling 0.0005
  colour    wood

-- 20 cm from the top of a 1.2 m deck: 1 m up the ramp
ball
  is a      sphere 5 cm radius, 150 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0005
  colour    orange
  moves     freely
  on ramp.deck, 20 cm from the top

-- fixed shelf, top at 80 cm, far end at 2.00 m
ledge
  is a      box 55 by 30 by 4 cm
  friction  0.3, spinning 0.001, rolling 0.0005
  colour    grey
  at        1.725 m along, 78 cm up

-- hangs from a hinge at its top; bottom 1.5 cm above the ledge
paddle
  is a      box 2 by 20 by 30 cm, 400 g
  colour    wood
  at        1.8 m along, 96.5 cm up
  turns on  paddle hinge, about y, at its top
  swings    from −100° to 5°
  damping   0.001 N·m·s/rad

-- top at 85 cm, so the paddle's lower 3.5 cm overlaps it; 1 cm gap to the paddle
slider
  is a      box 10 by 10 by 5 cm, 100 g
  friction  0.3, spinning 0.001, rolling 0.0005
  colour    dark grey
  moves     freely
  on ledge, 1.87 m along

-- centre 2 cm inside the ledge's far end: stable, but a small push tips it off
block
  is a      cube 8 cm, 100 g
  friction  0.3, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    white
  moves     freely
  on ledge, 1.98 m along

hoop
  is a      ring 36 cm across, 8 mm thick
  colour    orange
  at        2.08 m along, 45 cm up

box
  is an     open box
  length    50 cm
  width     40 cm
  walls     20 cm
  colour    wood
  on floor, 2.1 m along

expect
  ball touches ramp
  ball touches paddle
  paddle touches slider
  slider touches block
  block drops through hoop
  block comes to rest in box
```

---
thinking (summarized):

I'm sketching out the Rube Goldberg chain components—ball, ramp, paddle, slider, block, ledge, hoop, box—and thinking through how to define each part's geometry, considering whether to use a simpler ring primitive for the hoop instead of a full basketball hoop setup.

Since there's no slide joint available, I realize the slider part needs to be a free-moving box resting on a track surface that gets knocked along it. For the paddle, I'm working out a pendulum-like hinge mechanism at the top that swings forward when struck by the ball from the ramp, so its lower end can then strike the slider and continue the chain reaction.

Maybe simpler to keep everything near table height: ramp foot sits on the ledge itself, so the ball rolls straight onto the ledge without a height drop. I need to pin down the ramp length and where "1 m up the ramp" actually places the ball relative to the ramp's bottom edge.

From there the ledge needs its own chain of events — paddle hanging above swings down to hit a slider, slider knocks a block off the ledge's far end, block drops through the hoop into the box. But I realize a ball rolling along that same ledge would interfere with the slider setup, so I need to rethink how those two mechanisms share the space.

I'm trying to figure out whether the plank's centerline or surface aligns with the given points, and calculating how much the ball drops where the plank meets the ledge depending on that offset.

Computing the top edge offset at the foot end with the normal vector, I find it lands just under the ledge top with a tiny negligible step, so setting foot z at ledge top minus 2cm works well. Since both geoms are static/fixed, overlapping the plank's bottom slightly into the ledge interior isn't a problem since MuJoCo won't generate collisions between world-fixed geoms.

Now I'm thinking the ledge doesn't need support posts since it's fixed and can simply float in place. For the heights, I'm planning the box walls at 20cm, with the hoop ring and ledge at specific heights, and realizing the block's horizontal travel distance depends on its launch speed, which is uncertain — so I should just make the hoop large enough to accommodate variation in trajectory.

I'm estimating a 40cm-wide hoop ring positioned close below the ledge to minimize horizontal deviation, picturing the ball as a 5cm radius sphere around 300g, starting a meter up a ramp. I'm working out the drop height from ramp angle and ledge height (roughly 0.8m ledge, ~17 degree slope) to figure out the physics of the fall.

Now I'm calculating the rolling speed using the standard formula for a sphere rolling down an incline, getting about 2.0 m/s. I'm now placing the exact ramp geometry, setting the foot of the ramp near the ledge top and figuring out coordinates for the high end so the ball starts 20cm from the top edge.

I'm computing the ramp's high end at a 15° angle with length 1.2m, verifying the trig works out so cos and sin terms match the given length — but since the x-coordinates come out negative, I'm considering shifting the whole scene's origin so all positions stay positive.

Now I'm working out the ball's physics: starting 20cm from the top with a 5cm radius, the drop height to the foot is about 0.258m along a 1m path, giving a velocity near 1.9 m/s using the rolling-sphere energy formula (10/7 factor for moment of inertia).

Accounting for rolling friction, I'll estimate the ball reaches the ledge at roughly 1.8 m/s. The ledge sits 0.8m up, 4cm thick, 30cm wide, matching the ramp's width so the ball rolls straight across. I'm placing the paddle mechanism next — a pivoting box hanging from a point around 1.15m high, sized 2cm thick by 20cm wide by 30cm tall, with its bottom edge just 1-2cm above the ledge so the ball strikes it a few centimeters up from the ledge surface.

Working out the pivot geometry: since it hinges at the top about the y-axis, a positive rotation would swing the bottom toward −x, so the forward swing (toward +x where the ball pushes it) corresponds to a negative angle. I'm setting the swing range to roughly −120° to 5° to capture the full forward-and-back motion.

Now I'm placing the slider on a ledge just in front of the paddle, as a 10×8×5 cm box with its top at 0.85 m, separated by a 1 cm gap. The ball strikes the paddle about 3.5 cm above its bottom edge (paddle bottom at 0.815 m), and as the paddle swings forward its bottom arcs upward and forward to strike the slider's top-rear edge, since the slider spans 0.80–0.85 m in height and overlaps the paddle's swept path.

Working out the arc geometry, I find for the paddle length of 0.30 m, staying below the 0.85 m ceiling limits rotation to under about 28°, and the 1 cm gap gets closed at only about 2° of swing -- so contact happens almost immediately, which works well. I confirm the ball strikes the paddle (not the slider directly) since the paddle sits between them, and now I'm thinking through the momentum transfer, starting with a paddle mass around 100 g.

Computing the moment of inertia for the rotating paddle, I find the ball's much greater mass means it barely slows while giving the paddle significant angular velocity, around 6.8 rad/s, inelastically. Essentially the ball keeps shoving the paddle forward, which in turn drives the slider.

I'm reconsidering the mass balance though—maybe the ball should be lighter so it bounces back rather than continuing through, and making the paddle heavier (0.4 kg) changes the effective mass at the contact radius enough to transfer motion properly to the slider at the bottom of the paddle's swing.

Running through the collision chain: ball hits paddle giving it a point speed around 1.0 m/s, then paddle strikes the slider yielding roughly 0.88 m/s. With friction deceleration around 2.9 m/s² at μ=0.3, the slider would travel about 0.13 m before stopping—I need to check if that's enough distance for whatever the slider needs to accomplish.

I'm now thinking about placing a block near the slider so it gets pushed to roughly 0.5 m/s and slides off the ledge edge. Since MuJoCo uses the max friction between contacting geoms, I should lower friction on both the slider and block to around 0.2 to reduce energy loss along the ledge.

A better design: position the block with only a 2-3 cm overhang past the ledge edge so its center of mass still sits just inside for stability, then a small nudge from the slider tips it off with minimal horizontal velocity, letting it fall nearly straight down into a hoop placed right beneath the edge.

Below that, I'll place a catching box (roughly 40x40 cm with 20 cm walls) centered under the hoop on the floor, so after passing through the ring the block drops the remaining distance and settles inside the box.

Now I'm checking the slider's launch speed against the fall trajectory: with speed around 0.6 m/s and a drop from 0.8 to 0.45 m, the block's horizontal travel during the roughly 0.27 s fall needs to line up with the hoop's position, so I'm tuning the slider velocity and hoop placement so the block passes cleanly through the center rather than clipping the edge.

Working out the fall time (~0.40s) and landing zone, I size the collection box at 50cm long centered past the edge, with 20cm walls that clear the ledge height fine. Then I shift to checking whether the slider has room to actually push the block, laying out paddle position at x=1.8 and starting to place the slider relative to the ledge.

Placing the slider 1cm ahead of the paddle (1.82–1.92) and the block cube right after (1.94–2.02), with the ledge spanning 1.45 to 2.00 so the block slightly overhangs. I confirm the slider only needs to travel about 2cm before pushing the block, which is easily achievable at 0.88 m/s even accounting for friction, then start considering whether the ball itself continues on to interact with the paddle/slider setup.

Both the ball and slider might eventually tip off the ledge through the hoop into the box, which should be fine for the end goal of the block resting in the box. I decide to size the ball at 5cm radius and 150g with a 400g paddle, then recompute the effective mass for the collision.

With those values, paddle tip speed comes to about 1.26 m/s, which seems reasonable. I check the contact geometry carefully: ball center height aligns at 3.5cm above the paddle's bottom edge, which lines up well with the paddle face. I also note the small lip at the ramp-to-ledge transition where the angle shifts by 15°, which could affect how the ball rolls over that kink.

At the kink itself, the sharp angle change means the ball briefly goes airborne rather than smoothly following the surface — I work out that it lands with a small downward velocity that gets absorbed without much bounce, which seems fine. Then I double-check whether the ledge's near edge actually sits beneath the deck's sloped surface at that point, confirming the deck line clears the ledge top by a small margin so there's no unwanted collision there.

Confirming the post top sits fine within the deck. For the ball, placing it 20 cm from the top along the deck surface gives roughly 1 m up the ramp, matching the setup. Checking rolling friction requirements for the 15° slope, I set ramp friction to 0.8 so static friction is sufficient for rolling without slipping, and assign ledge, slider, and block friction at 0.3 while keeping the ball at 0.8.

Now I'm working out the paddle hinge placement — it pivots about the y-axis at its top, and I need to clarify whether its position ("1.8 m along, 81.5 cm up") refers to center or bottom height. Comparing to other examples like the ball centered over the block and the door panel's "raised 2 cm," it seems bottom-offset phrasing is used inconsistently, so I'm trying to pin down the convention before finalizing the paddle's placement.

I'll treat "X up" as specifying the center height for safety, so the paddle's centre sits at 0.965 m and its pivot at 1.115 m. I'm deciding to skip adding a fixed mount or crossbar for the hinge to avoid collisions, and I'm leaving damping minimal while setting the swing range from −90° to 5°, being careful with the sign on the negative angle.

Checking clearances: the paddle bottom at 0.815 m stays 1.5 cm above the ledge top, and widths don't conflict. For the slider, I'm placing a 10×10×5 cm, 100 g box on the ledge 1.87 m along, letting "on" set only its vertical position with lateral offset defaulting to zero, which gives a 3.5 cm overlap with the paddle's resting position — that seems fine.

Now the block: an 8 cm cube, 100 g, resting on the ledge at 1.98 m along, with top at 0.88 m. Since the slider's 5 cm height pushes low on the block's face rather than high, the block should tip forward off the edge instead of tipping backward, which is the intended behavior given its center of mass sits only 2 cm from the edge.

Finally, I'm placing a ring — 36 cm across, 8 mm thick — at 2.08 m along and 45 cm up, positioning it right where the ledge ends; I'm not worrying about whether 36 cm refers to outer or centerline diameter since it shouldn't matter for clearance against the ledge bottom at 0.76 m.

I'll set its position using centre coordinates like "1.725 m along, 78 cm up." For ordering, I'll declare ramp first, then ball referencing the ramp, followed by ledge, paddle, slider on the ledge, block, hoop, and box, with expectations chaining touches from ball to paddle to slider to block, through the hoop, and resting in the box. Checking rough timing: the ball rolls about 1 m then onto the ledge, reaching the chain around 1.6 s, with the block landing near 2 s and settling well within the 6 s budget.

Thinking through whether the ball itself needs to come to rest too, I reason it'll likely keep rolling after hitting the paddle, possibly ending up in the box with the block, and rolling friction (coefficient 0.004) should be enough to settle it there eventually. I'm estimating the resulting deceleration from rolling friction on the ramp, roughly 0.08g given the ball's radius, which means noticeable energy loss over a 1 m roll compared to gravitational energy gained.

I'll settle on friction values: ball with friction 0.8, spinning friction 0.001, rolling friction 0.0005; ramp matching those same values; ledge with slightly lower sliding friction 0.3 but the same spinning and rolling values. For the paddle, I'm noting it just needs to swing with some damping, no need for armature specification. The ball itself is a 5 cm radius sphere weighing 150 g, starting 20 cm from the top of the ramp.

Now I'm working out the ramp geometry — high end at 34 cm along and 109 cm up, low end at 1.5 m along and 78 cm up, with a 30 cm width. I need to decide whether the ball's position should reference "on ramp" or more specifically "on ramp.deck" since the ramp part is the sloping plank and the position is measured down from its high end — leaning toward using the deck reference for clarity.

Checking the ball's trajectory onto the ledge: it travels 0.24 m to reach the paddle contact point, which lines up fine with the paddle swing timing even with the slider positioned 1 cm ahead. I'm also verifying the block's stability — a 2 cm overhang still keeps its center of mass inside the edge, so that's stable — and confirming the ring/hoop dimensions fit within the box walls without collision.

With the hoop radius fitting cleanly within the box and the ring confirmed as a fixed, non-moving primitive, everything checks out geometrically. Time to write out the full world definition.

