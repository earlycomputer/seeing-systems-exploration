The ball is a regulation size-7 basketball (24 cm across, 600 g, hollow). It sits on the floor and is launched at 3.01 m/s along and 8.73 m/s up. That gives an apex near 4.0 m. The ball's centre comes down through the rim plane at 3.05 m about 1.33 s after launch, 4 m from the start, falling at roughly 55°.

Clearances, worked out on a straight-line approximation of the path near the rim and without air drag:
- **Rim edges:** the ball's path passes about 19 cm from the near and far edges of the rim's tube. The ball plus tube needs 12.4 cm, so it should not touch either edge.
- **Bracket and backboard:** the ball is about 2.7 m high by the time it reaches them, below both.
- **After the hoop:** the ball then hits the hoop's pole at about 1.1 m, falls to the floor and rolls off.

```world
world  basketball shot through a hoop

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 24 cm across, 600 g
  is        hollow, lively
  rolls
  bounce    lively
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor
  launched  3.01 m/s along, 8.73 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out regulation basketball specs—roughly 11.9 cm radius and 600 g mass—then setting up the launch geometry from floor level to a rim 3.05 m high and 4 m away.

I'm solving for a trajectory with an apex around 4 m, computing vertical and horizontal velocities to get the ball crossing the rim plane at roughly 55° descent angle, then checking clearance against the rim's near edge so the ball doesn't clip the inner ring on its way through.

I'm skipping air drag since it only applies to objects explicitly slowed by air. For the backboard, I'm working out its position relative to the rim and bracket, placing it from about 38.1 to 41.1 cm beyond the rim, spanning roughly -15 to 90 cm vertically, then tracking how the ball's path continues past the rim with a horizontal velocity as it falls toward the floor.

Calculating the fall time to the floor using the vertical drop equation, I get the ball landing around x≈5.35 m, which puts it right in the path of the support pole located at x=5.1–5.3 m. I'm checking whether the ball actually collides with the pole by working out its position at the time it crosses the pole's x-range.

Then I check the backboard clearance: with the backboard's bottom edge at 2.90 m and spanning x=4.381–4.411, the ball's height at that x-position comes out to about 2.64 m, well under the backboard, so it passes clear. I also confirm the arm and bracket supports sit above or outside the ball's path, so those aren't obstacles either.

The real issue is the pole hit itself — the ball strikes the pole at roughly 1.12 m height with forward and downward velocity, which could send it bouncing back unpredictably rather than cleanly dropping through the hoop. I'm wondering whether a steeper trajectory after the rim would let the ball clear the pole entirely, avoiding this collision issue altogether.

Now I'm working out the geometry for positioning the hoop relative to the ball and floor, figuring out how to express the rim height and distance so they align properly by default. For the ball itself, I'm settling on a sphere sized to regulation basketball dimensions — around 24 cm diameter — to match real-world specs.

The backboard sits past the rim so the ball never reaches it beforehand, and the ring position at x 3.77–4.23 only intersects the trajectory during descent, which checks out fine. I'm also noting the ball's bounce and spin behavior—lively with floor friction, likely backspin—expecting it to drop cleanly through the hoop.

