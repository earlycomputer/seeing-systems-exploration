The pendulum starts swung back 60° and swings forward through its lowest point. There it strikes a 3 cm ball sitting just ahead of it. The ball rolls 1 m into a low-lipped open box.

**How the cup catches the ball**
- The near lip is only 8 mm high, so the ball can roll in over it.
- The ball and cup are both set to dead bounce, so the ball doesn't spring back off the 12 cm far wall.
- After the ball stops at the far wall, the inside lip stops it rolling back out.

**Estimated speeds** (hand calculations, not a simulation run)
- The bob reaches about 2.2 m/s at the bottom of its swing.
- The ball should leave at about 1 m/s after it settles into rolling.
- It should reach the cup at about 0.9 m/s, enough to climb the lip.

**Geometry**
- The bob's centre at the bottom of its swing is 3.5 cm above the floor. That keeps it 1 cm clear of the floor and level with the ball's centre.
- The ball starts 1.2 mm in front of the bob. The cup's centre is 1 m beyond the ball's start.

**Assumption to check:** the swing direction depends on how the pendulum part reads its starting angle. I've taken a positive angle to put the bob behind the pivot. If it puts the bob in front instead, the bob starts on the ball's side and the swing is wrong; changing the 60° to −60° fixes it.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0005

pendulum
  is a               pendulum
  pivot height       53.5 cm
  length             50 cm
  bob size           2.5 cm radius
  bob mass           200 g
  rod thickness      1 cm
  rod mass           30 g
  starts swung back  60°
  colour             grey

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 5.6 cm along

cup
  is a              open box
  length            24 cm
  width             16 cm
  walls             12 cm
  base thickness    4 mm
  near wall height  8 mm
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum.bob
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the pendulum's physics setup—placing the pivot, hinging it on the y-axis, and making sure the part is named `pendulum` so its bob and hinge structure matches the brief's naming requirements.

Thinking through the rotation math for the hinge, positive angle about y swings the bob toward -x, meaning "swung back" corresponds to that negative-x position, so the ball starts there and swings forward through +x as expected.

Now I'm figuring out the vertical placement so the bob strikes the ball at the right height without clipping the floor -- if the bob radius equals the ball radius and sits too low, it touches the ground, so I'm raising the bob's resting height slightly (around 3.5-4 cm) to keep its bottom just clear of the floor while still making solid contact with the ball at the bottom of the swing, then positioning the ball horizontally so it touches the bob right at that lowest point.

For the cup, I'm placing it roughly a meter past the ball's starting position, but realize an open box with full walls would block the ball from rolling in -- so the near wall needs to be very short or essentially absent for the ball to roll over it into the cup.

Instead I'm keeping walls thin (about 3mm) so the ball can roll over the lip, but then worry about the ball bouncing back off the far wall and escaping over that same low near lip. I need to tune the approach speed and friction so the ball settles inside rather than ricocheting back out.

Working through the step-climbing physics, I get the ball needs roughly v ≥ 0.49 m/s to mount the lip, though MuJoCo's soft contacts will behave differently in practice. Once inside, a dead bounce off the far wall and a slightly lower inner lip height could keep a slow-rolling ball trapped — though this whole approach feels uncertain enough that I should consider a simpler design instead.

Estimating rolling friction deceleration using MuJoCo's rolling coefficient, I get roughly 0.47 m/s², which would help settle the ball but isn't dramatic enough to rely on alone.

Thinking about a more robust catch mechanism, I'm leaning toward a lip-and-wall design where the ball enters over a low lip and hits a dead far wall to absorb momentum regardless of entry speed.

With near-zero restitution on that wall collision, the ball's translational velocity stops but its forward spin persists, and friction with the base floor then re-accelerates it into the wall again, keeping it pinned there while the spin gradually dissipates — which is exactly the stable resting behavior I want.

So the design just needs enough entry speed to clear the near lip and a tall far wall (say 10cm) to prevent overshoot. Making the near lip flush with the base thickness keeps entry easy, but I'm weighing whether a slightly raised lip (base 5mm, wall 1cm) would better prevent bounce-back out the entrance, which might mean using a larger ball radius to make climbing that lip trivial.

I'm settling on r=3cm with base 4mm and near wall 8mm, giving h/r≈0.27, requiring roughly 0.45 m/s entry speed. Now I need to figure out cup dimensions (20cm x 16cm) and how to position it relative to the ball using the part's base offset convention, similar to how the open box was placed.

For the interior layout, I'm computing where the near wall sits relative to the base, accounting for wall thickness so the geometry doesn't overlap incorrectly. Now I'm thinking about the pendulum-ball collision dynamics — picking masses for bob versus ball and working out the post-collision velocity using an elastic-ish restitution formula, while considering how MuJoCo's default contact model handles this.

I'm also weighing the slide-to-roll transition: hitting slightly above center barely changes things, but I need the ball to arrive at the cup around 0.8-1.2 m/s, so I'm adjusting rolling friction coefficients on the ball and floor to tune the deceleration rate appropriately.

I also need to think about momentum transfer during impact — if the bob and ball masses are close, the bob won't fully stop and could catch up to the ball again after the first hit, so I'm considering mass ratios that avoid a second collision.

Working through target velocities: bob speed at the bottom of its swing depends on pendulum length and drop angle, and the ball's post-collision velocity depends on the coefficient of restitution and mass ratio, then rolling friction cuts it to 5/7 of that. I'm testing a 200g bob against a 100g ball to see if it lands near the 1.3 m/s target.

With a restitution coefficient around 0.5, I find a 50° release angle on a 0.5 m pendulum gives roughly the right speed, though varying e between 0.3 and 0.9 produces a fairly wide range of possible arrival speeds — something to keep in mind for sensitivity.

I'm also checking whether the entry lip could cause the ball to hop over the cup interior before the far wall stops it, and confirming the pendulum bob clears the floor and swings away cleanly after impact so it doesn't interfere with the ball's path afterward.

Then I'm considering the stand arm's placement above the pivot — since it extends from the pivot outward and sits on top of the rod, it shouldn't collide with the swinging rod itself, assuming parts don't register self-collisions.

Figuring out the pendulum's resting geometry: with pivot height 54 cm and rod length 50 cm, the bob center sits around 3.5 cm up (radius 2.5 cm), and with the ball's radius 3 cm giving a center height of 3 cm, the vertical gap is 0.5 cm against a combined radius of 5.5 cm — so I'm solving for the horizontal contact offset, landing around 5.477 cm, to position the ball correctly.

Checking the gap at 5.6 cm placement: it comes out to about 1.2 mm, which seems acceptable, so I'll finalize pivot height at 53.5 cm, rod length 50 cm, and bob specified as a 2.5 cm radius sphere weighing 200 g. I'm double-checking whether the bob actually reaches the ball right at the lowest swing point given that small clearance.

Since the bob's lowest-point distance slightly exceeds 5.5 cm, it will pass bottom-dead-center and touch the ball just after, rising negligibly as it moves forward — close enough to treat as contact at the bottom. I'm placing the ball on the floor at 5.6 cm along (absolute, not relative to pivot), with zero lateral offset, then positioning the cup's base 1 m beyond the ball with 4 mm base thickness and 8 mm near-wall height.

I'm checking that the cup's inner dimensions and the ball's travel path don't cause unwanted lateral contact — the geometry stays symmetric so there's no sideways drift. For the bounce setting, if I set the ball to "dead" that would also reduce restitution for its collision with the bob, lowering the bob's exit velocity and resulting roll speed enough that it may not even reach the ball.

Still, at 0.75 m/s this doesn't clear the threshold I need (around 0.45 margin is required, so it should pass, but the dead setting on the ball also kills restitution with the far wall, which isn't ideal). I'm considering instead marking the cup as "dead" rather than the ball, though MuJoCo's contact mixing rules (solmix/priority) make it unclear how that resolves when combined with other contact properties. As an alternative, I'm testing a steeper swing angle of 60°, which gives better velocity margins throughout — the bob speed, roll speed, and arrival calculations all check out with comfortable headroom, and rolling contact with the floor stays fine under the dead setting. I'm still unsure whether "dead" guarantees near-zero restitution specifically for the bob-ball collision in MuJoCo's contact model.

I'm reasoning through the rotation direction for the pendulum's starting position — working out that a positive rotation about the y-axis takes the bob from hanging straight down to swinging toward negative x, which means the bob starts on the opposite side from the ball and swings forward to make contact, confirming the setup geometry is correct along with the effective contact mass once the rod's distributed mass is factored in.

Now I'm setting friction values for the ball and floor, and figuring out the right syntax for the contact events — writing something like "ball touches pendulum.bob" and "ball comes to rest in cup" as the collision triggers, with the scene settling by the 6 second mark.

I'm double-checking the physics: the ball reaches the wall around 1 second and stays pressed there, so I need to verify its spin decays properly via rolling friction without causing it to climb the wall due to the angular velocity direction at the contact point.

Working through the geometry, the wall contact point slides downward, so wall friction acts upward on the ball, but the maximum upward friction force is only about 0.64 of gravity's pull—not enough to lift it. So the ball stays settled against the wall as expected.

