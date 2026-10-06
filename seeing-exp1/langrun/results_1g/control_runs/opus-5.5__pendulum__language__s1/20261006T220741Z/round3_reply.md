## What happened in the run

The pendulum swung down from 48° and met the ball at 0.37 s.

- **The strike:** the bob stayed pressed against the ball until 0.55 s, riding up over it as it swung past the bottom.
- **The roll:** the ball briefly reached 0.46 m/s while being pushed. Right after the bob let go it had dropped to 0.24 m/s, and it kept slowing as it rolled.
- **The cup:** the ball crept up to the near lip at 4.80 s, barely moving, and stopped against it at x = 0.86 m, outside the cup.
- **The pendulum:** it kept swinging at about ±21° for the rest of the run, so it kept much of its energy but passed little to the ball.

The world does not do what the brief says.

## Why the strike is so weak

Adding mass made things worse, so mass was not the main problem. My best reading of the long contact and the sudden loss of speed is that the ball was jammed. The bob struck slightly above the ball's centre, and both surfaces were grippy. The bob seems to have pinned the ball against the floor, so it slid with heavy friction instead of rolling away, and friction at the bob probably gave it backspin as well.

## Changes

1. **Slippery strike.** In MuJoCo, two touching surfaces use the larger of their two friction values. So I made the ball itself nearly frictionless. Against the floor it still gets the floor's 0.8 grip and rolls properly. Inside the cup it still gets the cup's high rolling friction. Against the bob, both surfaces are slippery, so the bob can only push.
2. **Strike at the ball's centre.** The ball is now 5 cm in radius, so its centre sits 5 cm up, level with the bob's centre at the bottom of the swing. The bob still clears the floor by 1 cm, and the larger ball also climbs the 8 mm lip more easily.
3. **Starting angle 45°.** By my estimate this should send the ball off at about 1.1–1.3 m/s.

This version has not been run yet; the speeds are estimates.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

pivot
  is a  point
  at    55 cm up, 0 m along

pendulum
  is a           sphere 4 cm radius
  weighs         1 kg
  friction       0.05, spinning 0.0001, rolling 0.0001
  colour         grey
  50 cm below pivot, 0 m along
  turns on       pendulum hinge, about y, at pivot
  starts turned  45°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       500 g
  friction     0.05, spinning 0.0001, rolling 0.0001
  colour       grey
  attached to  pendulum

support beam
  is a    box 6 by 30 by 4 cm
  touches nothing
  colour  wood
  4 cm above pivot, 15 cm to the right, 0 m along

support post
  is a    post 6 cm square, from floor to support beam's top
  touches nothing
  colour  wood
  centred on support beam's right side

ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.05, spinning 0.0001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on floor, 9.5 cm beyond pivot

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  8 mm
  friction          1.0, spinning 0.02, rolling 0.06
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

```json
{"what_happens": "The pendulum swings down from 48° and stays pressed against the ball from 0.37 s to 0.55 s, riding over it. The ball reaches 0.46 m/s while being pushed but rolls off at only 0.24 m/s and keeps slowing. It creeps to the cup's near lip at 4.80 s and stops against it at x = 0.86 m, outside the cup. The pendulum keeps swinging at about ±21°.", "works": false, "problem": "The bob strikes slightly above the ball's centre and both surfaces are grippy, which appears to jam the ball against the floor, so it leaves far too slowly to climb into the cup."}
```

---
thinking (summarized):

Something seems off here - the ball's velocity dropped from 0.46 to 0.24 m/s while in contact with the pendulum, which doesn't match a simple sliding-to-rolling transition since 5/7 of 0.46 gives 0.33, not 0.24. I'm trying to reconcile this discrepancy while the ball was still being pushed during that contact window.

The deceleration on the floor seems off too, suggesting velocity-dependent rolling friction. I'm starting to suspect the energy loss comes from the ball being jammed between bob and floor — both surfaces gripping with friction could pin the ball's rotation, dissipating the pendulum's momentum as internal friction rather than transferring it into forward motion.

My fix idea is to lower the ball's own friction significantly while keeping floor friction high, since contact friction is the max of both geoms — this way the bob-ball contact stays low-friction (letting them slide freely against each other) while the ball-floor contact remains high enough for rolling.

I also need to fix the geometry so the bob hits the ball at the right height — making the ball bigger (5cm radius) and the bob smaller (4cm radius) so the contact point lines up near the bottom of the swing, then placing the ball with the proper offset distance from the pivot so contact happens right as the bob reaches its lowest point.

Now thinking about mass: if the earlier mass-ratio estimate of 0.54 was actually contaminated by friction losses at the joint rather than reflecting true mass, the real ratio could be much higher, maybe in the 5–12 range, with the ball transitioning from sliding to rolling and picking up roughly 0.75 of the bob's velocity.

Working backward from a target rolling speed near 1.1 m/s, I can solve for the swing angle using energy conservation, landing around 39–45° depending on which mass ratio assumption holds -- so I'll pick something in that range as a working estimate, acknowledging the ball's actual speed will vary with the uncertain R.

Checking the geometry now: pivot height with the bob center and rod length, ball resting distance beyond the pivot, and cup placement relative to the ball's landing spot -- making sure the cup's interior walls and the ball's radius are compatible so everything fits without collision issues.

