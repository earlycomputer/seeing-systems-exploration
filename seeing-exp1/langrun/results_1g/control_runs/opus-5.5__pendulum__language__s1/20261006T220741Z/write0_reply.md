The pendulum hangs from a pivot 55 cm up and starts swung back 45°. Its bob passes just above the floor and strikes the ball at about full speed. The ball rolls along the floor and climbs a 1 cm lip into an open box whose base centre is 1 m from the ball's start.

None of this has been run in MuJoCo, and the speeds below are rough hand estimates. MuJoCo's soft contacts make the strike's energy transfer the main uncertainty.

- **Strike:** I expect the ball to leave at roughly 1 to 1.3 m/s.
- **Reaching the cup:** by my estimate the ball needs at least about 0.7 m/s to reach the lip and climb it, so there is some margin.
- **Stopping:** I gave the cup a high rolling friction so the ball should stop quickly inside it rather than bounce back out. This assumes MuJoCo's "larger value wins" rule when two touching surfaces have different friction.

If the ball falls short or overshoots, change the pendulum's `starts swung back` angle first.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

pendulum
  is a               pendulum
  pivot height       55 cm
  length             50 cm
  bob size           4 cm radius
  bob mass           500 g
  rod thickness      1 cm
  rod mass           50 g
  starts swung back  45°

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 9.5 cm beyond pendulum.pivot

cup
  is an             open box
  length            30 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  1 cm
  friction          1.0, spinning 0.02, rolling 0.03
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum.bob
  ball comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the physical setup: the pendulum needs to strike a ball that rolls about a meter into a cup and stops there. The tricky part is that the cup's near wall and raised base could block the ball from entering, so I need to consider wall height and base thickness relative to the ball's radius to make sure it can actually roll in and settle.

Working out the step-climbing physics: with base 4mm and near wall 8mm tall, the ball needs enough incoming speed to climb that lip after losing energy from the edge impact. Running the numbers for a sphere with h/r≈0.27, I find it needs roughly 0.41 m/s of approach velocity to make it over.

Then I'm checking the exit side too—getting out requires clearing a smaller 4mm lip, needing about 0.27 m/s after a likely low-restitution dead bounce off the far wall. It seems workable but tight, so I'm considering alternatives like reducing wall height further or tuning rolling friction inside the cup instead of relying on exact bounce dynamics.

Checking the floor's rolling friction effect too: with condim 6 giving torque-based rolling resistance, I estimate deceleration over the ~0.9m runway from start to cup lip, and it seems the energy loss is bigger than expected—entry speed of 0.8 m/s would need a higher starting speed around 1.13 m/s. I should probably lower the floor's rolling friction coefficient to compensate.

I'm trying ball radius 4cm with rolling friction 0.001, which gives a more reasonable deceleration and velocity-squared loss of about 0.28 over 0.8m, so starting at 1.0 m/s yields entry speed around 0.85 m/s into the cup, which should be enough to climb the lip. Now I'm working out the cup geometry—centered 1m from the ball's start, with the near wall at about 0.85m and a 30cm cup width.

Checking the lip climb requirement: with h/r=0.25, the required velocity to clear the near wall is around 0.46 m/s after losses, well within the 0.85 m/s entry speed. I'm also confirming the ball lands properly onto the base after climbing the thin near wall, and that the cup stays fixed in place rather than being free to move.

For the pendulum, I'm working out the geometry so the bob's center aligns with the ball's center at height 4 cm at the pendulum's lowest point, meaning the pivot sits at length plus 4 cm above the base. Setting up rotation about the y-axis, I find that a positive angle swings the bob backward along -x, so to strike the ball forward in +x, the pendulum should start pulled back at a positive angle, something like 60 degrees.

For placement, I'll keep the pendulum at the origin by default, then position the ball relative to it using the bob's unturned rest position plus the sum of the bob and ball radii for the spacing.

Now I'm sizing the bob so its bottom clears the floor while its centre sits at the right collision height relative to the ball.

I'm trusting the geometry is fine for stand arm clearance above the rod. For the collision, since the ball is hit slightly above its centre, I expect it to start sliding then transition to rolling, with speed roughly 5/7 of the initial translational velocity imparted by the pendulum strike.

The bob likely keeps decelerating after rising, with maybe a second minor contact as the ball slides—it's a small effect I can ignore. Working backward, if I want the ball's rolling speed near 1.0 m/s, that means v_b should be about 1.3 m/s, so I'm solving 1.69 = 2*9.81*0.5*(1-cosθ) for the swing angle.

There's a trade-off: entering too fast means the ball bounces off the far wall, while too slow means it won't climb the lip (needs roughly 0.7 m/s minimum at entry). Aiming a bit higher, if I target 1.3 m/s for the ball, that implies v_b near 1.7, giving 1-cosθ ≈ 0.295, so θ≈45°—I'll go with 45° and now check how rolling friction in the cup decelerates the ball as it enters around 1.2 m/s.

Working out the physics: rolling resistance decelerates the ball at roughly 5.3 m/s², stopping it after about 14 cm, which is well within the 26 cm cup interior, so even a dead hit on the far wall is fine given the high sliding friction too. I wonder if climbing the lip at 1.2 m/s could cause the ball to hop slightly, but that should be acceptable, and I should also account for MuJoCo's handling of rolling resistance mid-air and whether spinning friction syntax needs to be specified alongside rolling friction—I'll add a small spinning friction value of 0.01 to be safe, plus rely on the rolling friction of 0.03 to keep the ball settled at rest at the end.

I'm setting friction values: ball friction 0.8 with spinning 0.005 and rolling 0.001, floor rolling matching at 0.001, and cup rolling at 0.03, since MuJoCo combines friction by taking the max per component across contacting geoms. I'm also considering the pendulum bob's interaction with the ball—after striking, the pendulum will keep swinging indefinitely since there's no damping, but it should swing away from the ball's path without a second collision. I'll leave restitution and other defaults untouched for both the ball and bob, and structure the cup as an open box without needing extra positioning since parts are placed with absolute coordinates.

Now I'm working out the cup's dimensions—length and width 30 cm, wall height 10 cm, base thickness 5 mm—and figuring out how to position it relative to the ball using the "its base X beyond ball" placement syntax, making sure the y-coordinates align so the cup sits directly along the ball's path. I'm also calculating the geometry between the pendulum bob and the ball: with bob radius 4 cm and ball radius 4 cm, I need roughly a 1.5 cm gap, and I'm checking that the 2D distance between their centers exceeds the contact threshold of 8 cm so they don't collide prematurely.

Solving for where dx gives a distance of exactly 8 cm, I get the bob's x-position near 1.56 cm, meaning the bob is just slightly past the bottom of its swing with a tiny angle of about -1.8°, close to maximum speed. I'm confirming the bob's height comes out to 5 cm below the pivot (pivot at 55 cm, rod length 50 cm), and now I'm finalizing the rod specs (1 cm thick, 50 g mass) and the ball specs (4 cm radius sphere, 100 g), along with how to phrase the contact conditions—ball touching the pendulum's bob and then coming to rest in the cup.

