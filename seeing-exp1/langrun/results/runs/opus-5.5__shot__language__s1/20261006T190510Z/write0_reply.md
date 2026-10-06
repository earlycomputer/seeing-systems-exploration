The ball (24 cm across, 620 g, hollow) starts on the floor with its centre at 12 cm. It is launched at 3.01 m/s along and 8.73 m/s up, so it peaks near 4.0 m. It comes down through the 3.05 m rim, 4 m away, about 1.33 s later.

- **Clearances:** it descends at about 55°. It clears the rim tube, the bracket and the bottom edge of the backboard.
- **After the basket:** it then strikes the pole at about 1.1 m height before landing.

```world
world  free throw from the floor

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 12 cm radius, 620 g
  is        hollow
  rolls
  bounce    lively
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0 m along, 0 m to the left
  launched  3.01 m/s along, 8.73 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball, 0 m to the left

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical setup: a regulation basketball (radius ~0.12 m, mass ~0.62 kg) starting on the floor and launched toward a hoop 3.05 m high and 4 m away, needing to account for the rim's actual diameter of about 45.72 cm for clearance.

Choosing an apex height of 4.0 m, I calculate the initial vertical velocity (~8.73 m/s), the time to apex (~0.89 s), and the descent time to rim height (~0.44 s), giving a total flight time around 1.33 s and a horizontal velocity of about 3.01 m/s — producing a natural descending angle of roughly 55° through the hoop, ignoring air drag since gravity alone should make the trajectory exact. I'm also confirming the ball starts on the -x side so the backboard remains beyond the rim as expected.

Now I'm checking clearances to make sure the ball doesn't collide with the backboard bracket — comparing the bracket's far-face offset from the rim center against the ball's position and radius as it passes through x=4, to verify the inner rim edge and ball edge don't interfere.

After clearing, I trace the ball's descent past the hoop: continuing at 3 m/s horizontally while falling from 3.05 m to 0.12 m, solving the quadratic for time gives t≈0.449 s, landing around x=5.35 m. But checking the support pole's position (near face at x=5.1 m), it looks like the ball would actually strike the pole on its way down.

Checking the bracket clearance too - ball clears it by about 4 cm, which is tight but fine. Now I need to think about whether the ball actually touches the rim while entering at a 55° angle, considering the effective opening based on the rim's inner radius versus the ball's size projected at that angle.

With a 12 cm radius, 620 g hollow ball, I'm setting velocity values of roughly vx 3.01, vz 8.73, and working out the time to descend through the hoop plane using the quadratic for vertical motion.

