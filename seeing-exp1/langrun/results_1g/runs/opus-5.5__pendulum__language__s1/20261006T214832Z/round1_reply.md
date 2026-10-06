**What happens:** The pendulum is released from 40° and swings down. At 0.37 s the bob strikes the ball, which rolls along the floor at about 1.0 m/s. The ball hops the cup's near lip at 1.16 s and lands on the cup base at 1.28 s. It hits the far wall at 1.56 s, which takes most of its speed. Then, with almost no rolling friction, it keeps drifting back and forth across the cup base. It rolls back at 0.11 m/s, taps the near wall at 3.51 s, and rolls forward again at 0.07 m/s. At 6 s it is still moving at 0.07 m/s, above the 5 cm/s rest threshold.

**The fix:** The cup gets a high rolling friction. MuJoCo uses the larger of the two geoms' values, so the ball still rolls freely on the floor but stops within about 10–15 cm on the cup base. Everything else stays the same.

```world
world  pendulum knocks ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.001, rolling 0.0002

pendulum
  is a               pendulum
  pivot height       55 cm
  length             50 cm
  bob size           4 cm radius
  bob mass           1 kg
  rod thickness      1 cm
  rod mass           100 g
  starts swung back  40°
  colour             grey

ball
  is a      sphere 5 cm radius, 200 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 9.5 cm beyond pendulum.pivot

cup
  is an             open box
  length            30 cm
  width             20 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  1.2 cm
  friction          0.8, spinning 0.01, rolling 0.015
  bounce            dead
  colour            white
  its base 1 m beyond ball

expect
  ball touches pendulum.bob
  ball touches cup.base
  ball comes to rest in cup
```

```json
{"what_happens": "The pendulum swings down from 40° and strikes the ball at 0.37 s. The ball rolls about 1.0 m/s along the floor, hops the cup's near lip at 1.16 s and lands on the cup base at 1.28 s. It bounces off the far wall at 1.56 s, then drifts back and forth inside the cup on near-zero rolling friction and is still moving at 0.07 m/s at 6 s.", "works": false, "problem": "The ball gets into the cup but never comes to rest, because almost nothing slows its rolling on the cup base."}
```

---
thinking (summarized):

The ball is rattling around the cup with almost no rolling friction, bouncing off the walls instead of settling. I need to increase rolling friction on the cup base so it decelerates properly—with rolling friction around 0.01, deceleration works out to about 1.4 m/s², meaning a ball entering at 0.73 m/s would stop within roughly 0.19 m.

With the cup's interior spanning about 0.95-1.25 m, the ball should come to rest somewhere around 1.09 m, well within the cup bounds. I'm also checking that the pendulum rod's contact with the stand arm isn't causing unwanted energy loss, but the amplitude barely decays so that's fine.

