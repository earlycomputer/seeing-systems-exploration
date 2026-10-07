The pendulum's bob hangs 60 cm below its pivot and starts swung back 80.4°, which puts it 0.5 m above its lowest point. At the bottom of its swing it is level with four equal balls on a raised, lipped rail. The balls are 15 cm apart, so each impact passes along the row to ball4. Ball4 then rolls off the rail end over the low near wall of the box. The box is dead and grippy, so its tall far wall and its floor stop ball4 there.

I haven't run this. The sign of the starting angle is the main risk: I took a positive angle to swing the bob back, as the library pendulum's `starts swung back` suggests. If it's the other way, the bob starts in front of the row and misses the first strike. The `expect` block will catch that.

```world
world  pendulum strikes a row of balls into a box

floor
  friction  0.8, spinning 0.005, rolling 0.002

rail
  is a      box 70 by 8.6 by 4 cm
  colour    wood
  friction  0.8, spinning 0.005, rolling 0.002
  at        35 cm along, raised 26 cm

rail left lip
  is a      box 70 by 1 by 2 cm
  colour    wood
  on rail, at rail's near end, at rail's left side

rail right lip
  is a      box 70 by 1 by 2 cm
  colour    wood
  on rail, at rail's near end, at rail's right side

pivot
  is a      point
  at        93.5 cm up

pendulum
  is a           sphere 3 cm radius, 110 g
  colour         grey
  bounce         lively
  friction       0.5, spinning 0.005, rolling 0.002
  60 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  80.4°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       10 g
  colour       dark grey
  touches nothing
  attached to  pendulum

ball
  is a      sphere 3 cm radius, 100 g
  colour    white
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  moves     freely
  repeated  4 times, 15 cm apart along
  on rail, 6.5 cm along

box
  is an            open box
  length           50 cm
  width            40 cm
  walls            35 cm
  near wall height  25 cm
  wall thickness   2 cm
  base thickness   2 cm
  colour           orange
  bounce           dead
  friction         1.0, spinning 0.02, rolling 0.02
  its base 62 cm beyond rail

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

I'm setting up a Newton's cradle chain with balls spaced 0.15 m apart, where ball4 ends up resting in the box. I'm working out the pendulum geometry, picking a length of 0.6 m so that a 0.5 m drop in bob height corresponds to a specific release angle.

Now I'm thinking through the collision physics—the bob hits at roughly 3.13 m/s, which transfers through equal-mass elastic collisions down the line, so ball4 enters the box fast enough that it needs to bounce off the far wall and settle within 6 seconds. I'm also figuring out how to structure the model itself: whether to use a library pendulum part or build a custom hinge-mounted sphere, and designing a simple rail (a flat box on the floor) for the balls to roll along without needing side lips since collisions stay centered.

For the pendulum geometry, I'm placing the bob sphere so its resting center aligns with ball1's height, working out the pivot height and hinge rotation so that a positive angle about the y-axis swings the bob backward first, then forward into ball1 — meaning it needs to start turned at about 80.4° to set up that strike correctly.

I'm also thinking about the collision physics itself: with the bob and ball1 having equal mass, an idealized elastic collision would transfer all momentum and stop the bob, but MuJoCo's default contact model is somewhat inelastic, so using a livelier bounce setting will help approximate the springy transfer I want. For positioning, the bob's center at its lowest swing point needs to sit just touching ball1, roughly offset by the sum of their radii.

Now I'm checking whether the rod will scrape against the rail during the swing, since the bob's bottom edge appears to align exactly with the rail's top — I need to reposition the rail's starting point so it clears the bob's full sweep path, accounting for the bob's radius and its lowest-point offset from ball1.

I'll raise the bob's lowest center to 7.5 cm instead, giving its bottom a clean 5 mm clearance above the rail top, and the resulting off-center impact angle of about 4.8° stays mostly horizontal, which is acceptable. The rod sits above the rail so there's no collision there, and now I need to work out the ball spacing at 0.15 m between centers, starting from ball1's position.

Thinking through the collision physics: a struck rolling ball hitting a stationary one transfers most of its translational velocity but keeps some spin, so the striker continues forward at roughly 2/7 of its original speed, causing secondary collisions that are acceptable for the setup. Ball4 ends up absorbing most of the momentum and heads toward the box.

Now I'm figuring out the box geometry—it needs to sit at floor level so the ball rolling off the end of the rail (which sits 4 cm up) drops into it cleanly, meaning the box should be positioned low against a wall to catch the ball as it falls.

I'm reconsidering the heights: making the rail top flush with the box's base top so the ball rolls straight in rather than dropping, setting both at 2 cm thickness so there's no jarring transition. But then I realize the ball will hit the box's far wall at a few meters per second and could bounce back out onto the rail, so I need a dead-stop far wall or enough friction/length in the box to prevent that rebound.

If the near wall sits just past the rail end with its top below the ball's path, the ball clears it easily and falls into the box, dropping about 0.28 m over roughly 0.24 s while covering 0.6 m horizontally at 2.5 m/s — well within a 0.5 m box length, so it strikes the far wall with a dead bounce and settles inside, then rolls back toward the now-blocking near wall and gradually loses energy to rolling friction.

Estimating rolling resistance for a 3 cm radius ball with a 2 mm friction coefficient gives a deceleration near 0.47 m/s², enough to stop a slow post-bounce roll within a second, but bumping the box's rolling friction coefficient to around 0.02 would raise that to roughly 4.7 m/s² for a much faster settle — since MuJoCo contacts take the max of paired geom frictions, setting the box surface with high sliding and rolling friction should work well.

Now I'm sketching the rail itself: a fixed box about 1 m long, 10 cm wide, with its top surface at 30 cm height, possibly simplified without visible support posts. I'm also considering adding thin 1 cm side guide lips to keep balls from drifting off the flat rail during collisions, since the contacts are centered but lateral drift is still a risk.

Checking clearance: at 1 cm below lip top, ball's horizontal radius is 2.83 cm, giving 1.7 mm clearance—fine for low contact. I'll set inner faces at ±3.3 cm with rail width 8.6 cm so lips stay clear of the swinging bob, which stays within ±3 cm. Now verifying the stack-up: rail top at 30 cm, ball centre at 33 cm, bob centre lowest at 33.5 cm so its bottom clears the rail top comfortably.

Pivot sits at 93.5 cm. Release height puts bob 50 cm above lowest point, giving swing angle θ = acos(1 − 0.5/0.6) ≈ 80.41°. For x-positions I'm placing the pivot at x=0 with the bob's lowest point also near x=0, and spacing the balls along the rail at roughly 6.5, 21.5, and 36 cm.

Continuing the layout, I'm placing ball4 at 51.5 cm with the rail running from x=0 to 70 cm (centered at 35 cm) clearing the swinging bob by 5 mm, leaving ball4 an 18.5 cm roll to the rail's end. Beyond that I'm positioning an open box past the rail's far end, working out how to place its rim relative to the last ball using a positioning offset.

I'll keep the lateral offset at default 0 and just specify "its base 62 cm beyond rail" for the x-axis positioning. Checking the ball's trajectory after leaving the rail: at the near wall it's still too high to clip (30 cm vs 26 cm wall), and at the far wall, with v=3 m/s, it reaches centre x=1.19 after about 0.163 s, which I need to check against the fall distance to confirm clearance.

At v=3, the ball's centre is around 20 cm when it hits the far wall, well below the 26 cm wall top, so it collides safely dead. Even at v=4, it still contacts the wall around centre 26 cm. I'll make the walls a bit more robust: setting walls to 35 cm height and the near wall to 25 cm for safety margin.

For physics properties, I'm setting the ball-box friction to 1, with light spin and rolling friction around 0.02, and no bounce. Balls get 100 g mass each for rolling behavior, and I'm sizing the pendulum bob sphere at 3 cm radius, considering the rod's small mass and how it affects the bob's effective inertia.

Now I'm working out the hinge setup for the pendulum — naming it "pendulum hinge," rotating about the y-axis, anchored at a defined pivot point roughly 93.5 cm up along x=0. I need to establish the order: define the pivot first, then the pendulum, then attach the pendulum rod. For positioning, I'm specifying the pendulum as 60 cm below the pivot, which fixes the vertical offset while leaving the other directional offsets at default.

I'm defining the rod itself as 1 cm thick, running from the pivot to the pendulum's top, weighing 10 g, attached to the pendulum, and set to touch nothing since it won't be in contact with other objects at that height.

For the rail lips, I'm specifying them as small boxes positioned flush against the rail's near end and left side to keep them properly aligned. Now I'm moving on to placing the balls individually.

I'll use a repeated `ball` definition spaced 15 cm apart along the rail, generating ball1 through ball4, with contact properties left lively enough for good energy transfer between them. I'm checking that ball4 reaches the wall around 1 second and that everything settles by 6 seconds, then writing the expect block confirming the pendulum touches ball1 and ball4 comes to rest in the box, with default floor friction.

