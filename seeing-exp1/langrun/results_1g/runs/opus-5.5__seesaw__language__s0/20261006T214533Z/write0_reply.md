The seesaw is a 2 m plank on a hinge 30 cm up. It starts tipped 15° with the ball's end down, and a small stop on that end keeps the ball from rolling off. The 1 kg weight falls about 1.9 m onto the raised end, which snaps the plank to its other limit.

A rough angular-momentum estimate, before any run:

- The plank leaves the ball's end moving at about 4.5 m/s.
- That should throw the ball roughly 1 m up, about twice what the brief asks.
- The language has no expectation for height, so the 50 cm rise has to be checked from the run itself.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    0 m along, 30 cm up

post top
  is a  point
  at    0 m along, 26 cm up

fulcrum
  is a    post 6 cm square, from floor to post top
  colour  grey

seesaw
  is a           box 200 by 20 by 4 cm, 500 g
  level with pivot, 0 m along
  turns on       seesaw hinge, about y, at pivot
  swings         from -15° to 15°
  starts turned  15°
  colour         wood

stop
  is a         box 2 by 20 by 6 cm, 20 g
  on           seesaw, at seesaw's far end
  attached to  seesaw
  colour       wood

ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  at        88.7 cm along, 14 cm up
  colour    orange

weight
  is a      sphere 6 cm radius, 1 kg
  bounce    dead
  friction  0.8
  moves     freely
  at        88 cm behind pivot, 2.5 m up
  colour    dark grey

expect
  weight touches seesaw
  ball touches seesaw
```

---
thinking (summarized):

I'm sketching out a seesaw design: a plank balanced on a fulcrum, with a 1 kg weight dropped onto one end to launch a 100g ball from the other end at least 50cm high. I'm working out the arm lengths and initial tilt so the dropped weight's impact translates into enough upward force on the ball.

Using angular momentum conservation and estimating a drop height of about 2 m, I calculate the ball could rise roughly 1.25 m, well above the 50 cm requirement, with the seesaw motion stopping once the heavy end hits the ground and the ball launches off. Now I'm working out the pivot height and tilt angle geometry to make the plank dimensions physically consistent.

Actually using floor contact rather than hard limits might be simpler, letting the seesaw swing freely between roughly −17° and 17°. But I realize if the ball starts resting on the lower end at 15°, it would just roll off downhill due to the slope, so I need some kind of stop or lip attached to the seesaw at that end to keep the ball in place.

I'm tracing the far end's velocity as the seesaw rotates from +15° to −15°: when the ball-holding end swings up and over the pivot, its tangential velocity shifts from straight up to up-and-toward-pivot, which determines the direction the ball launches when released.

Now I'm working out the launch geometry — maybe simplifying with a smaller tilt angle — and setting up the weight object: a 1 kg sphere around 6 cm radius positioned above the near end, roughly 2-2.5 m up, computing its along/height coordinates relative to the pivot's position.

I'm calculating fall height to drop, converting to impact velocity, and then estimating the ball's resulting speed and rise based on the lever arm ratio between the weight's distance and the ball's distance from the pivot — it looks like the ball should launch over a meter high.

Now I'm figuring out the stopper block's position on the seesaw, noting it's rigidly attached so it rotates with the plank, while the ball sits freely in the world frame and needs its position computed relative to the tilted plank surface.

Adding 5mm clearance brings z to about 0.14. I'm confirming the hinge-based tilt approach works for the initial angle rather than sculpting a sloped geometry directly. Checking that the weight falls near the opposite end of the plank around s ≈ −0.88 without catching on the stopper or other geometry.

Setting hinge damping to zero and sizing the seesaw as a light box around 0.5 kg with a small 20g stopper. Running quick numbers on moment of inertia and angular velocity, I estimate the ball launches around 4.7 m/s, enough to reach well over a meter in height, comfortably clearing my 0.5 m target. I'm noting that the weight keeps pressing into the plank as it swings until the hinge hits its limit, at which point the ball separates.

Checking the hinge range from -15° to 15°, confirming no floor contact issues near the lower limit, and deciding on wording like "weight touches seesaw" for the contact event description since the lower stop terminology is ambiguous. Now sketching the fulcrum post dimensions connecting floor to pivot.

I need to lower the post height to avoid colliding with the tilted plank — calculating the plank's bottom clearance near the pivot at 15° tilt gives roughly 0.271m, so setting post top at 0.26m keeps a safe margin, and placing the post centered at the pivot location. Then positioning the seesaw itself centered at the pivot point.

For the remaining elements, I'm placing the stopper at the seesaw's far end, mirroring how the catapult scoop base attaches to the arm's near end. The ball goes at 88.7cm along and 14cm up, while the weight sits 88cm behind the pivot at 2.5m up, which translates to a negative along-coordinate since it's behind rather than ahead.

