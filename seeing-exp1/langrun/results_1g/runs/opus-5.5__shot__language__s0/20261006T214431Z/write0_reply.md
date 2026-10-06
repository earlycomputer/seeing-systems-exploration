The ball rests on the floor and is launched at 3.01 m/s along and 8.72 m/s up. That takes it to an apex near 4.0 m. Its centre then comes down through the 3.05 m rim plane about 4.0 m away, at roughly 55°, so a 24.3 cm ball should pass the 45.72 cm rim with about 7–8 cm to spare. It should also clear the bottom of the backboard on the way down. I left air drag off so the path stays predictable. I haven't run it yet.

```world
world  basketball shot into a hoop

floor
  size      20 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 24.3 cm across, 600 g
  rolls
  is        hollow
  bounce    lively
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 1 m along
  launched  3.01 m/s along, 8.72 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the regulation basketball specs - diameter about 24.26 cm, mass around 600g - and setting up the launch scenario with the ball starting on the floor and the rim positioned 3.05 m high, 4 m away.

I need the trajectory's center to pass through the rim with clearance on both sides, accounting for the backboard position behind the rim too. I'm deciding to keep the physics simple by skipping air drag effects, since they'd only cause minor shifts over this short flight and introduce unnecessary complexity.

Picking an apex height of 4.0 m, I compute the launch and descent speeds using basic projectile motion, giving a total flight time of about 1.33 s with vx ≈ 3.01 m/s. At the hoop, the vertical velocity component is around 4.32 m/s, producing a steep 55° entry angle — now I'm checking that this path clears the front of the rim at x ≈ 3.77 m.

At that entry angle, the ball's effective horizontal footprint along the descent direction is about 0.148 m, leaving roughly 0.077 m clearance from the rim tube's inner edge, so it should pass through safely without touching the front or back of the rim.

The ball at z=2.64 with top 2.76 clears the backboard bottom at 2.9. Checking the pole next: it sits at x=5.2 with an 80x80 base spanning roughly 4.8 to 5.6, and tracing the trajectory forward shows the ball would hit the pole around z~1.1 near x=5.1, which seems fine since it just bounces off there.

I don't think the net matters here since there's no net, and the ball should behave like a lively hollow basketball with friction and rolling once it lands. I'll describe the outcome as "ball drops through hoop" rather than worrying about resting time, which feels too uncertain to pin down. For positioning, the ball's height sets the floor reference, and the hoop's rim is placed 4m beyond the ball along the same line, with its lateral position matching the ball's by default.

I'm settling on placing the ball 1m along the floor with the hoop rim 4m beyond it, using a 20m floor size to clear the pole base comfortably. I'll keep the ball resting on the floor at launch since it's being shot upward anyway, and I'm specifying regulation basketball dimensions (24.3cm diameter, 600g) with a radius of 0.1215m, plus launch velocities of 3.01 m/s horizontal and 8.72 m/s vertical based on the height calculation.

I double-check the trajectory math: with 8.72 m/s vertical velocity, the ball apexes near 3.997m and lands at roughly x=3.998, confirming it should pass through the hoop as intended.

