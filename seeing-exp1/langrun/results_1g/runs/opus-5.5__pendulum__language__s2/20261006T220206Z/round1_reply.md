## What happened in the run

The pendulum swung down normally. It went from 30° to about 12° at 0.25 s, turning at roughly 127°/s, which is the speed expected.

The bob met the ball near the bottom of the swing, at 0.34 s, and the two stayed in contact for 0.14 s. That is far too long for a strike. In that time the pendulum lost nearly all its energy: afterwards it only rocked about ±6°.

The ball came away at just 0.06 m/s. It crept to x = 0.42 m by 6 s and never reached the cup.

## Why it failed

I can't pin down the cause with certainty. My best guess is that the bob dragged on the ball rather than striking it:

- The bob's centre sat 1 cm higher than the ball's, so it hit slightly above the ball's centre and pressed it into the floor.
- With the default friction between bob and ball, the two could grip each other. The floor's friction under the ball would then soak up the bob's push instead of the ball flying off.

## Changes

- **Head-on strike:** a smaller bob (2.5 cm radius) and a bigger ball (3.5 cm radius), with both centres at 3.5 cm high.
- **Less grip:** low friction on the pendulum, so the bob can't drag on the ball.
- **More energy:** the pendulum starts swung back 40° instead of 30°.
- **Cup:** taller walls (15 cm), so a fast ball can't hop over the far wall.

```json
{"what_happens": "The pendulum swings down and its bob meets the ball at the bottom of the swing at 0.34 s, but stays in contact for 0.14 s and loses almost all its energy. The ball comes away at only 0.06 m/s, creeps to x = 0.42 m by 6 s and never reaches the cup at x ≈ 1.06 m.", "works": false, "problem": "The strike gives the ball almost no speed, probably because the bob hit above the ball's centre with high friction and so dragged on it rather than striking it, leaving the ball creeping far short of the cup."}
```

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.001, rolling 0.0001

-- bob centre hangs at 3.5 cm (1 cm clear of the floor), level with the ball's centre, for a head-on strike
pendulum
  is a               pendulum
  pivot height       48.5 cm
  length             45 cm
  bob size           2.5 cm radius
  bob mass           500 g
  rod thickness      1 cm
  rod mass           40 g
  starts swung back  40°
  friction           0.1
  colour             wood

ball
  is a      sphere 3.5 cm radius, 80 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on floor, 6.2 cm along

-- a shallow tray: thin base, low near lip to roll over, tall dead walls to stop the ball
cup
  is an             open box
  length            20 cm
  width             16 cm
  walls             15 cm
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

The pendulum seems to lose most of its energy in that long 0.14s contact, dropping from 12° to just 6° amplitude while the ball only picks up 0.06 m/s — that mismatch suggests the ball might be pressing against the floor during contact rather than swinging freely, so I need to look more closely at the contact geometry.

The amplitude settled at -6°, so energy clearly drained during contact. Ball mass is 60 g versus bob's 400 g, but the ball only ends up moving at 0.06 m/s with no apparent decay — that momentum mismatch doesn't add up through a normal elastic or rolling-friction interaction. I'm wondering if the real energy sink is something unreported, like the rod brushing the stand arm, since the swing looked clean before contact started.

Given the 0.14 s contact duration seems unusually long, I'm checking whether the bob is actually near the bottom of its swing when contact begins — computing its angle and position at 0.34 s shows it's close to vertical, with the ball just a few centimeters away, suggesting the contact margin or geometry might be creating this extended, near head-on collision.

Critical damping from the default solref/dampratio settings would mean essentially zero restitution, so the heavy bob and light ball should emerge at a shared velocity near 0.95-1 m/s — yet the ball only moves at 0.06 m/s, which doesn't add up. I'm wondering if something else is absorbing the momentum, like rolling friction from condim 6 torsional contact, or if the ball is somehow constrained rather than free to translate.

I'm wondering if the ball picked up spin from contact with the bob, with friction at the bob-ball interface possibly locking their motion briefly, but ultimately the horizontal momentum has to transfer somewhere — either into the ball's motion or dissipated through the floor contact.

Running the numbers, absorbing that momentum over the contact window would require a normal force well above the ball's own weight, meaning the bob would need to be pressing down on the ball almost vertically, which doesn't match their current geometry since the bob sits above and slightly offset from the ball rather than directly on top. Rather than keep chasing the exact physics, I think the more practical fix is to redesign the contact geometry so the bob and ball meet head-on at matching centers.

Working through sizes, I try bob radius 2.5 cm with centre at 3.5 cm height (leaving a 1 cm clearance from the floor) paired with a ball radius 3.5 cm at the same centre height, making it a clean head-on collision happening right at the bottom of the swing where horizontal velocity is maximal. I check the x-position math for where contact occurs and confirm the bob's rise at that point is negligible, and I'm also considering adjusting the ball's mass since a lighter ball would pick up more speed from the same impulse.

I also think about lowering friction on the pendulum to prevent any locking at the bob-ball contact, suspecting that rolling/spinning friction mixing under condim 6 might be the culprit, though the ball's own rolling friction seems fine. I run the numbers for a 40° starting angle: bob speed works out to about 1.45 m/s using energy conservation, giving the ball a post-collision speed up to roughly 2.6 m/s for a nearly elastic case, or less for inelastic.

With rolling friction factored in (5/7 scaling), the ball's speed range becomes about 0.9–1.9 m/s, fast enough that it might hop over the walls I'd set at 10 cm given its 3.5 cm radius -- so I bump the wall height to 15 cm and size the lip near the wall to about 1.2 cm. I also consider whether making the ball's bounce "dead" would help prevent chaotic bob-ball collisions, but decide the heavy bob still imparts similar speed regardless, so I leave the ball's default properties alone. Then I work out the geometry: pivot height at 48.5 cm for a 45 cm pendulum length plus the 3.5 cm ball radius, with the ball positioned 6.2 cm along x and the cup base a meter beyond that.

