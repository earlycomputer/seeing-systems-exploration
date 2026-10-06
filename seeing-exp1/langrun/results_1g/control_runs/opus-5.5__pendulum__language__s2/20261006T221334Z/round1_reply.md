**What happened in the run**

- The pendulum swung down from 23° and its bob struck the ball at 0.37 s.
- The ball rolled along the floor at a steady 0.42–0.44 m/s and reached the cup's 3 mm lip at 2.35 s.
- The lip and the cup's rolling resistance stopped the ball almost at once, at x = 0.95 m.

The cup's base starts at x ≈ 0.945 m, so the ball is perched only about 5 mm inside the near edge. It stopped about 11.5 cm short of the cup's centre at 1.065 m, essentially on the lip. That is too marginal to count as rolling into the cup.

**The fix**

- Start the pendulum swung back 35° instead of 23°. This should give the ball about 50% more speed, around 0.65 m/s.
- Halve the cup's rolling resistance to 0.005. Together with the extra speed, the ball should carry over the lip and coast to rest near the middle of the cup, well before the far wall.

```json
{"what_happens": "The pendulum swings down from 23° and strikes the ball at 0.37 s; the ball rolls at about 0.43 m/s along the floor, reaches the cup at 2.35 s, climbs the 3 mm lip and stops immediately at x = 0.95 m, only about 5 mm inside the cup base's near edge and 11.5 cm short of the cup centre.", "works": false, "problem": "The ball arrives too slowly and stops right on the cup's lip rather than rolling into the cup."}
```

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
  starts swung back  35°

ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 6.5 cm along

-- a shallow-lipped cup: a 3 mm step in, dead walls, and enough rolling
-- resistance to stop the ball near its middle
cup
  is an             open box
  length            24 cm
  width             24 cm
  walls             5 cm
  wall thickness    1 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          0.8, spinning 0.01, rolling 0.005
  bounce            dead
  colour            wood
  sits              on floor, 1 m beyond ball

expect
  ball touches pendulum.bob
  ball comes to rest in cup
```

---
thinking (summarized):

Checking the ball's resting position against the cup geometry — it settled at 0.95, barely past the base's near edge at 0.945, so it looks like it's just resting on the lip rather than fully inside the base, with the height matching that edge contact.

This feels marginal rather than a clean success — the ball technically crosses into the footprint but it's fragile and could easily not count as "in cup." To make it robust, I should increase the launch angle to something like 35° and reduce the cup's rolling friction, which should roughly 1.5x the arrival speed and push the ball further toward center.

