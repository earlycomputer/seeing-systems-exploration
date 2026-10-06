The pendulum's bob hangs just above the floor and starts swung back 30°. When it swings through the bottom it strikes the ball. The ball rolls 0.9 m to a shallow-lipped cup with dead walls, whose centre is 1 m ahead of where the ball starts. Once over the low near lip, the ball is stopped by the tall far wall.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.001, rolling 0.0001

pendulum
  is a               pendulum
  pivot height       49 cm
  length             45 cm
  bob size           3 cm radius
  bob mass           400 g
  rod thickness      1 cm
  rod mass           40 g
  starts swung back  30°
  colour             wood

-- bob centre hangs at 4 cm, 1 cm clear of the floor; the ball's centre sits at 3 cm, just ahead of the bob
ball
  is a      sphere 3 cm radius, 60 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on floor, 6 cm along

-- a shallow tray: thin base, low near lip to roll over, tall dead walls to stop the ball
cup
  is an             open box
  length            20 cm
  width             16 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    2 mm
  near wall height  1.2 cm
  bounce            dead
  friction          0.8, spinning 0.001, rolling 0.0001
  colour            white
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working through the pendulum setup's physical structure—figuring out how the pivot, rod, bob, and stand arm connect geometrically, deciding where each attaches relative to the pivot point and rod's top.

I'm also thinking about potential collisions between the pendulum rod and the fixed stand arm since both sit near the pivot's y=0 position, though this overlap is likely an accepted part of the design. The hinge rotates about the y axis, so I'm considering how that affects the swing direction.

Working through rotation about y: for a bob hanging below pivot, a positive angle swings it toward -x (backward), meaning "starts swung back" corresponds to positive qpos, and as it swings forward through zero it reaches +x where it should strike the target ball. Now I'm sizing things — pivot height, rod length, bob radius — so the bob's center aligns with the ball's center at the bottom of the swing.

Ball radius around 3 cm resting on the floor puts its center at z=3 cm, so I want the bob's center near that height too, choosing a bob radius that keeps it just clear of the floor (maybe centered at 4-5 cm) while still making solid contact with the ball rather than grazing it or scraping the ground.

Now I'm working out positioning: pivot placed at origin with the bob hanging straight down, and the ball resting in front so it gets struck at the bottom of the swing where speed is highest. I'll set the ball's center at a distance equal to the sum of the bob and ball radii (around 6 cm) so they touch when the bob reaches bottom-dead-center.

I'm also figuring out the cup placement roughly 1 m away, and thinking through how an open-top box can catch the rolling ball -- the near wall needs to be short enough (relative to the ball's 3 cm radius) for the ball to roll over it and settle inside rather than bouncing off.

With a 1 cm step and 3 cm radius ball, I'm checking whether rolling speed survives the edge collision — using angular momentum conservation about the step edge, I derive that the post-impact velocity ratio is v'/v = 1 - (5/7)(h/r), which tells me how much speed the ball retains after climbing the lip.

Plugging in h/r = 1/3 gives v' ≈ 0.76v, and then I set up the energy condition for the ball to actually clear the step height afterward, which gives a minimum pre-impact speed around 0.49 m/s. I'm now thinking through what happens on the way back — the ball needs to hit the far wall, lose energy, and not have enough speed to hop back out over the near lip — plus factoring in rolling friction over the approach distance to figure out what initial launch speed is needed.

Checking the rolling resistance math, the default MuJoCo friction coefficients would produce way too much deceleration over a 1-meter roll, so I'm realizing I need to dial down the rolling friction coefficient substantially — maybe to something like 0.0001 on both surfaces — to keep the ball's speed loss manageable and controllable.

Now I'm thinking through the cup geometry: the ball needs dead walls to absorb energy so it settles rather than bouncing indefinitely between the near lip and far wall. With low rolling friction, there's a risk the ball oscillates slowly back and forth for too long before settling under the required rest threshold by the 6-second mark, so wall damping and box interior length need to be tuned together.

I'm also double-checking the base thickness and wall heights relative to the floor — the near wall needs enough effective height from inside the cup to prevent escape, accounting for the 2 mm base and ball radius positioning.

Then I'm considering how the side walls span the full box length, overlapping the near wall ends, so the enclosure stays sealed. For the ball to make it over the lip and settle, it needs roughly 0.6–0.9 m/s at impact, with enough reverse momentum accounted for after any bounce-back.

The pendulum collision physics matters here: the bob's effective mass and MuJoCo's contact damping (dampratio 1, fairly inelastic) determine how much velocity transfers to the ball, and friction will convert sliding into rolling motion, reducing the ball's effective speed to about 5/7 of its initial post-collision velocity.

Given the uncertainty, I should err toward a higher arrival speed—maybe 1.2 m/s—since the real risk is the ball being too slow to clear the lip, not too fast. Overshooting isn't dangerous because the far wall is tall enough (10cm vs 3mm ball radius) and dead (low restitution), so even a fast ball just bounces back weakly rather than escaping.

For the pendulum setup, I'm thinking through mass ratios: a heavier bob relative to the ball means more energy transfer, with the collision type (elastic vs. perfectly inelastic) determining whether the ball ends up moving faster or at the same speed as the bob. I'll need to settle on concrete values—something like a 3cm bob radius, 500g bob mass, 50g rod, and a ~60g ball—to calculate the actual arrival velocity.

Working through the geometry: with pivot height at 49 cm and a 45 cm pendulum length swung back 30 degrees, I calculate the bob's speed at the bottom of the swing using energy conservation, getting roughly 1.09 m/s. Then accounting for the collision physics and subsequent rolling friction (factoring in the 5/7 rolling coefficient), the ball's final speed likely lands somewhere between 0.7 and 1.4 m/s depending on how elastic the collision turns out to be.

The contact angle is slightly off-horizontal since the bob center sits about a centimeter higher than the ball, pushing it faintly into the floor, but that shouldn't change much. After impact, the heavy bob keeps swinging forward (only partial momentum transfer), reaching roughly 22 cm displacement at a near-30-degree forward angle before swinging back and forth for the remaining several seconds, well behind the ball which is now moving faster toward the lip.

I need to check whether the pendulum's geometry clears the stand arm. The arm sits atop the rod near the pivot, spanning a few centimeters in x and extending down toward y=-30, while the rod itself rotates in the xz-plane about that same pivot with some small radius from its thickness. Since the rod's top stays close to the pivot as it swings, it should stay within the arm's clearance radius without colliding.

Also worth remembering: MuJoCo by default disables contacts between a body and its direct parent, so since the pendulum body is parented to the world body, I don't need to worry about spurious contacts between them.

The stand post at y=-30, x=0 shouldn't interfere with the ball's path along x at y=0, and the pendulum bob's swing starting around x=-22cm doesn't bring it near anything else. I'm now thinking through the cup's dimensions as an open box roughly 20cm long.

I need to figure out placement: the base should sit "1 m beyond ball," which fixes the along-axis offset while leaving the other directions at default, with height handled by the part's internal "on floor" constraint. Since ball is defined first, the cup's center follows from its base center.

Checking the box geometry, the walls sit on the base's ends so the usable interior is 18 cm rather than 20, meaning the ball crosses the near wall around 0.96 m and has about 0.9 m to roll before reaching the lip. I'm confirming the cup's center counts as the base center, and that the ball coming to rest against the far wall still falls within the cup's bounds, accounting for the 2 cm-thick near wall with its sloped top. Finally I need to define the ball itself as a 3 cm radius, 60 g sphere that rolls and moves freely.

Now I'm placing the ball on the floor 6 cm along, aligning the pendulum bob's center with the pivot along x=0, and setting friction values for the ball and floor (0.8 sliding, 0.001 spinning, 0.0001 rolling), noting MuJoCo mixes contact friction by max by default and that the cup is set to dead/bounceless. I'm also considering hinge damping for the pendulum and finalizing the bob size at 3 cm.

For the pendulum geometry, the rod is 1 cm thick, starting swung back 30°, with a 400 g bob. Since the bob hangs below the pivot by the rod length, and pivot height is 49 cm with length 45 cm, the bob's center ends up at z=4 cm. I'm also working out how to express the touch condition between the ball and the pendulum's bob piece, likely using a dotted naming convention like `pendulum.bob touches ball`.

I'll use `ball touches pendulum` and `ball comes to rest in cup` as my success conditions. Checking the timing at 6 seconds, the ball travels roughly 0.9 m at ≥0.7 m/s, which works out to about 1.3 seconds — well within budget. Rolling friction after impact shouldn't cause issues either, so I'm ready to finalize this.

