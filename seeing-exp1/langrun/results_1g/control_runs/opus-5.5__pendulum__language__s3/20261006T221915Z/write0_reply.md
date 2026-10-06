The pendulum hangs from a 55 cm pivot and is pulled back 45°. Its bob passes just above the floor and strikes a 4 cm ball resting 7.2 cm ahead of the pivot. The ball rolls 1 m to a fixed open-topped cup. The cup has a low front lip (1.5 cm from the floor), so the ball can climb in but not easily roll back out, and dead walls soak up its speed.

None of this has been simulated. One thing I'm unsure of is which way a positive `starts turned` angle tips the bob. If it starts forward instead of back, it swings away first and hits the ball one swing later (about 1.4 s). That still leaves plenty of the 6 s.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

pivot
  is a  point
  at    55 cm up

pendulum
  is a           sphere 3 cm radius, 300 g
  bounce         lively
  colour         grey
  50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  45°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       wood
  attached to  pendulum

stand arm
  is a     box 4 by 20 by 4 cm
  touches  nothing
  colour   dark grey
  level with pivot, 12 cm left of pivot

stand post
  is a     post 4 cm square, from floor to stand arm's top
  touches  nothing
  colour   dark grey
  centred on stand arm's left side

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 7.2 cm beyond pivot

cup
  is an             open box
  length            24 cm
  width             24 cm
  walls             8 cm
  wall thickness    1 cm
  base thickness    5 mm
  near wall height  1.5 cm
  friction          0.8, spinning 0.005, rolling 0.002
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I need the pendulum object named "pendulum" with a hinge, pivoting at the top and the bob hanging below, so I'm working out how to structure the naming so it turns naturally on that pivot point.

For the cup physics, I'm thinking through how the ball rolls one meter and enters a shallow cup: a tall near wall would block the ball from entering, so making the near wall just a few millimeters high lets the ball roll over the lip and settle against the far wall while staying slow enough to rest inside.

I'm working out the physics of a rolling ball climbing a step edge, using conservation of angular momentum about the edge to find the reduced velocity after impact—with step height 1.5cm and ball radius 4cm, applying the formula v' = v(1 - 5h/7r) to check whether the ball retains enough speed to climb into the cup.

Given a minimum required speed near 0.63 m/s, I then consider whether the ball, once inside and bouncing off a far dead wall, could rebound with enough energy to escape back over the lip, likely concluding the rebound speed stays small enough to remain trapped.

Sizing the cup at roughly 20 cm long and wide with a 4 cm ball radius, I factor in rolling friction decelerating the ball across the 1 m floor — the coefficient suggests a deceleration around 0.35 m/s², which noticeably eats into the velocity budget over that distance, so I need to size the initial launch speed with that loss in mind.

Since MuJoCo combines friction as the max of two contacting geoms, I should keep the floor's rolling friction low (around 0.0002) so the ball's own rolling friction dominates, giving a gentler deceleration near 0.04 m/s². For the pendulum strike setup, I'm working out the bob's position at the bottom of its swing so its center aligns with the ball's center at 4 cm height, but I realize a bob of the same 4 cm radius centered there would end up touching the floor, so I need to adjust the geometry.

Raising the bob radius to 3 cm with its center at 5 cm height keeps it clear of the floor while striking slightly above the ball's center, which should actually impart useful topspin. I'm now working through the rotation math for the hinge about the y-axis, applying the rotation matrix to the bob's resting position below the pivot to confirm that a positive rotation angle swings the bob backward in x.

Since the ball needs to sit ahead of the pivot in the forward direction, I'm positioning its center about 7.2 cm ahead so that the bob makes contact with it near the bottom of its swing, accounting for the vertical offset between the bob and ball centers to get the correct horizontal contact distance.

I'm unsure of the sign convention for "starting turned back" relative to the rotation axis -- if it's misinterpreted, the pendulum could start on the forward side instead, meaning it would swing away first and come back around to strike the ball from the wrong direction after a full pass.

I'm checking that this alternate forward starting position wouldn't cause the bob or rod to overlap the ball or stand geometry, and confirming both sign interpretations still work, just with a delay of roughly one pendulum period before impact, which still fits comfortably within the 6-second window. I'm also planning to construct my own stand with a post on the side rather than relying on a built-in one, and now working out the collision physics -- computing drop height from the swing angle and figuring out how the elastic collision transfers speed from the bob to the ball given their mass ratio.

I'm now working through what rolling speed the ball needs after friction slows it from its initial slide, accounting for the mass ratio giving a 1.5x speed transfer and the reduced effect from hitting slightly off-center, aiming for the ball to enter the cup around 1.2 m/s so it clears the lip, hits the far wall without bouncing out, and settles with enough momentum to roll back but not hop over the 8cm wall.

Working out that a 40° pendulum swing gives roughly 1.5 m/s bob speed, transferring to a ball speed of about 1.4-1.6 m/s rolling, which drops to around 1.1 after climbing the lip and lands dead against the far wall as intended.

I'm also considering collision properties - keeping the ball's default bounce but making the cup dead so the ball doesn't bounce chaotically inside it - and figuring out how to position the cup roughly a meter beyond the ball's starting point when describing it as part of the scene.

Working out the near wall thickness so the ball climbs 1.5 cm up and drops 1 cm onto the base, keeping interior length around 23 cm which comfortably fits an 8 cm ball. I'm confirming the cup stays fixed by default, then setting up a pivot point roughly 55 cm up to define the ball's position relative to it.

Now I'm placing the pendulum bob — a 3 cm sphere weighing 300 g — 50 cm below the pivot, hinged about the y-axis and starting turned 40°, connected by a 20 g rod running from the pivot to the bob's top. I need to assume positions are defined at zero angle before the turned starting state is applied via the hinge angle. I'm also sketching a support stand with a post offset to the side near the pivot.

To avoid collisions between the stand arm and the swinging rod, I'll set the stand geoms to touch nothing, which sidesteps worries about whether parent-child contact exclusions apply correctly when the parent is the world body.

I'm placing the ball on the floor, 7.2 cm beyond the pivot, with its along position defaulting to 0 like the pivot and bob. I'm setting up the ball as a small sphere with mass, friction, and spin parameters so it rolls freely, then checking that its speed lets it cover the floor distance well within a second for the elastic collision timing.

I'm tuning contact liveliness so the bob is bouncy while the cup stays dead, then working through the momentum transfer math: with the bob roughly three times the ball's mass, an inelastic hit gives the ball around 1.1 m/s, rising to about 2.2 m/s with added restitution, and converting to rolling speed keeps it comfortably above the 0.63 m/s needed to reach the cup. I'm considering bumping the release angle to 45° for extra margin, which raises the drop height and speed range so the ball consistently rolls into the cup across the expected velocity spread.

I'll set event conditions for the ball touching the pendulum and coming to rest in the cup, and tune floor and cup friction/rolling resistance values so the ball settles below the 5 cm/s rest threshold once inside.

