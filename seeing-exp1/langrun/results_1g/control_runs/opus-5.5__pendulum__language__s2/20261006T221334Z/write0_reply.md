The pendulum's bob hangs at the ball's height. It starts swung back 23°, which gives it about 0.85 m/s at the bottom of its swing. The ball sits 6.5 cm ahead of the pivot. The cup's centre is 1 m beyond the ball.

The cup is an open box with a low 3 mm lip that the ball can roll over. Its dead walls and grippier rolling friction inside stop the ball quickly. These numbers come from rough hand estimates, not from a run.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

-- pivot sits over the origin; the bob hangs 50 cm below it, centre 3.5 cm up
pendulum
  is a               pendulum
  pivot height       53.5 cm
  length             50 cm
  bob size           3 cm radius
  bob mass           500 g
  rod thickness      1 cm
  rod mass           20 g
  starts swung back  23°

ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 6.5 cm along

-- a shallow-lipped cup: a 3 mm step in, walls that soak up the bounce,
-- and enough rolling resistance on its pieces to bring the ball to rest
cup
  is an             open box
  length            24 cm
  width             24 cm
  walls             5 cm
  wall thickness    1 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          0.8, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  sits              on floor, 1 m beyond ball

expect
  ball touches pendulum.bob
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the geometry of the pendulum setup—figuring out the pivot point, bob position, rod attachment, and how the stand arm and post need to be positioned relative to each other so everything connects correctly.

I also need to make sure the pendulum hinges properly about the y-axis and that the bob's resting position and swing trajectory will actually strike the ball at the right height, accounting for ball and bob radii and the rotation direction under the right-hand rule.

Now I need the ball to roll a meter and land in the cup, which means getting past the cup's wall. A rolling ball can't simply climb a wall, so I'm considering making the near wall very low or thin so the ball can clear it with enough speed, though a zero-height wall might not register as a real barrier.

I'm thinking of setting the base thickness to 5mm and near wall height to 5mm, small enough for the ball to climb onto, then letting it roll to the far wall, bounce, and settle via rolling friction. But there's a risk it rebounds back over the near wall and exits the cup entirely.

I'm working through the physics of rolling friction to calculate how much deceleration is needed so the ball arrives at the far wall with low enough speed to stay put rather than bounce back out.

If cup friction is high (rolling 0.02), the ball-base contact decel becomes about 4.7 m/s², so a ball entering around 0.5 m/s stops within just a few centimeters—plenty good inside the cup. But I realize the near wall and base are both 5 mm tall, forming a small step the ball needs enough speed to climb over before settling.

I'm working through the energy and angular momentum needed to roll over that 5 mm step with a 3 cm radius ball, accounting for the velocity loss from the impulsive collision at the step edge—getting a reduction factor of about 0.88 on the post-impact speed.

Beyond clearing the step, I also need to check the ball doesn't overshoot the cup after decelerating from rolling friction, picking rough cup dimensions (24 cm length/width, 4 cm walls) so it settles inside rather than bouncing back out. I'm also thinking through how the pendulum bob's collision with the ball should behave—mass ratio and MuJoCo's soft-contact restitution will determine how much energy transfers on impact.

After the collision, the ball then experiences rolling friction on the floor while the bob swings back and forth near the collision point, well behind the departed ball, so no second collision occurs. I'm picking rough numbers: ball radius 3 cm, 50 g; bob radius 3 cm, 500 g, with a small floor rolling friction coefficient to let the ball coast realistically.

Working through the physics, I want the ball to arrive at roughly 0.6 m/s after rolling, which means it needs to leave the collision at about 0.67 m/s rolling speed, translating to an initial slipping velocity near 0.94 m/s given the 7/5 ratio for a rolling sphere. With the bob at 500 g and ball at 50 g, I still need to account for an uncertain coefficient of restitution from MuJoCo's soft contact model to back out the required swing speed.

Deciding the ball should stay lively off the bounce but the cup should absorb energy dead. Working out pendulum geometry: treating the bob as a point mass with length ~50 cm, pivot height 53.5 cm, I calculate a release angle around 22-23° to achieve the target velocity, accounting slightly for the rod's mass reducing the effective speed. Now positioning the bob so its center aligns with the ball at the bottom of the swing.

Placing the bob slightly behind the ball's resting position—around 6.5 cm back—so contact happens just past the bottom of the swing, since the small horizontal offset barely raises the bob's height at that point.

I could try absolute coordinates instead: pendulum at the origin, ball positioned 6.5 cm along, cup placed 1 m beyond the ball, avoiding any part-based placement ambiguity. It's a bit risky without confirming the pivot's along position defaults to zero, but it seems reasonable enough to go with.

Now I need to place the stand supporting the rod, with its arm resting on top near the pivot and the post offset away from the ball's rolling path so it doesn't interfere, while checking whether the rod's swing could collide with the stand arm as it rotates.

I recall the world body is likely exempt from that exclusion rule, so I'll trust the part's setup. Checking positions: the ball rests at x=6.5cm and the pendulum bob swung back 23° starts at roughly x=-0.195m, height 0.075m, which seems fine with no extra damping needed. For the cup geometry—a 24x24cm open box with 1cm wall thickness and 5mm base/near-wall heights—the ball would roll over the near wall edge onto the base, which seems consistent.

The cup sits 1m beyond the ball on the floor, with its base symmetric around its center, spanning roughly 0.945 to 1.185m, so the ball entering at the near wall edge around x=0.94 should stop well within the cup's footprint around x≈1.0+. I'm now wondering whether that 5mm step is actually climbable given the cup's relatively high rolling friction coefficient of 0.02.

Working through the energy balance: rolling friction creates a resisting torque while the ball pivots around the step's edge through an angle of about 0.586 radians. The energy lost to friction (~0.0117mg) plus the gravitational potential energy needed (~0.005mg) gives a total requirement of about 0.0167mg, which translates to a required post-collision velocity of roughly 0.48 m/s, meaning the incoming velocity needs to be about 0.55 m/s after accounting for the restitution factor.

Trying a lower friction coefficient of 0.01 instead, the edge loss drops to about 0.00586mg, bringing total energy needed to 0.0109mg and incoming velocity down to about 0.45 m/s. Checking deceleration inside the cup at 2.3 m/s², the ball travels about 14 cm before stopping, which fits within the 24 cm cup — entry at 0.94 cm, stopping by 1.08 cm, well within the 1.185 cm base limit, so that configuration works.

Now I'm testing an alternative with a lower step: base and wall thickness at 3 mm each, giving h/r = 0.1 and an edge angle of about 0.451 radians, which with 0.01 friction yields a combined loss of about 0.0075mg.

Checking the timing budget: ball reaches the pendulum around 1.5s and the swing adds about 0.35s, comfortably within the 6s window. The main remaining concern is whether the bob, after being struck, swings forward and back past the bottom point in time, but by then the ball should already be gone from that area so it's not an issue.

Now I'm working out the geometry: rod thickness and mass, pendulum length measured as the distance from pivot to bob center, pivot height placing the bob center a few centimeters above the ground, bob radius, and the initial swing-back angle. I also need to check the ball's lateral alignment with the stand's arm span, and set floor and ball friction coefficients for sliding, spinning, and rolling.

Now I'm setting the cup's friction values and marking its bounce as dead, then defining the expected end state where the ball touches the pendulum's bob before coming to rest inside the cup.

