Three 4 cm balls sit 50 cm apart along x. `ball1` starts at 2 m/s with a matching rolling spin of 50 rad/s about y. The cup is an open box whose base and near lip are only 5 mm high, so `ball3` can roll straight in. The cup is a dead bounce, so `ball3` stops against the far wall instead of rebounding out.

I haven't run this. Since the balls are equal and the collisions aren't perfectly elastic, `ball1` and `ball2` will probably keep creeping forward after their hits, and `ball2` may follow `ball3` toward the cup. The expectations only check the touches and that `ball3` ends at rest in the cup.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 0 m along, 0 m to the left
  launched  2 m/s along
  spins     50 rad/s about y

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 50 cm beyond ball1, 0 m to the left

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 50 cm beyond ball2, 0 m to the left

cup
  is an              open box
  length             30 cm
  width              30 cm
  walls              12 cm
  wall thickness     1 cm
  base thickness     5 mm
  near wall height   5 mm
  bounce             dead
  friction           0.9, spinning 0.01, rolling 0.01
  colour             wood
  on                 floor, 65 cm beyond ball3, 0 m to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning the scene layout: three balls in a row that collide and send the last one rolling into a cup, and I'm thinking through how the cup's geometry needs a low enough lip for the ball to roll in given its radius.

I settle on a small near-wall height of about 5mm with a 4cm ball radius, so at a modest rolling speed it can hop the lip, while the taller far wall and dead bounce physics keep it from escaping once inside.

For the chain collisions, since masses are equal and contacts are soft rather than perfectly elastic, momentum transfer will be partial — each ball retains some spin and forward motion after impact, so balls further down the line may also roll into the cup, which isn't forbidden by the task.

For ball1's launch, I need angular velocity matching rolling-without-slip at 2 m/s with radius 0.04m, giving ω = 50 rad/s about the y-axis so the contact point has zero velocity relative to the ground.

I'm laying out three balls along a line roughly 50 cm apart with a cup near the far wall, figuring ball3's speed will decay slightly from rolling friction but stay close to 1 m/s. Since each ball needs its own name and only the first ball gets the spin/launch description, I'll write separate entries for ball1, ball2, and ball3 rather than reusing a repeated template.

Now I'm working out the cup's dimensions—open box with 30 cm length and width, 10 cm walls, thin base and near wall around 5mm thick—positioning it centered around 1.6 m along so its near lip sits close to ball3's resting position, letting the ball roll over the lip onto the base smoothly.

I want balls 1 and 2 to be bouncy for good energy transfer while the cup stays mostly inert, though I'm unsure how the contact bounce mixes between materials, so I'll bump the cup walls up to 12 cm just to be safe. The sequence I'm aiming for is ball1 hitting ball2, ball2 hitting ball3, and ball3 settling to rest inside the cup — checking that "touches" works generically between any two things, including ball-to-ball contact.

