Ball1 is launched rolling, with a spin that matches its speed. It knocks into ball2, which knocks into ball3. Ball3 rolls up a shallow ramp and drops over the cup's low near wall.

**Why ball3 should stay in the cup**
- Inside the cup, the near wall stands 3 cm above the cup's floor. That is taller than the 2.5 cm ball radius, so the ball can't roll back out that way.
- The far wall is tall enough to stop it.

**Speed check (estimated, not yet run)**
- Some speed is lost at each collision. More is lost when each struck ball changes from sliding to rolling.
- I estimate ball3 reaches the ramp at roughly 1.6 m/s.
- It needs about 1.05 m/s to get up to the top of the near wall.

**Assumptions I haven't confirmed**
- I've assumed the plank runs along its centreline between its two end points. That would leave a 2 mm lip at the ramp's foot.
- I've assumed `its base 1.6 m along` places the whole cup by its base.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 20 cm along
  launched  4 m/s along
  spins     160 rad/s about y

ball2
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball2

-- the cup: low lip at the near end (3 cm above its floor, more than the ball's radius), tall far and side walls
cup
  is an             open box
  length            35 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    1 cm
  near wall height  4 cm
  colour            wood
  its base 1.6 m along

-- a shallow ramp leading up to the top of the cup's near wall
ramp top
  is a  point
  at    1.415 m along, 4 cm up

ramp foot
  is a  point
  at    1.015 m along, 0 cm up

cup ramp
  is a    plank from ramp top to ramp foot, 20 cm wide, 4 mm thick
  colour  grey

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup ramp
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the chain-reaction setup: three balls in a row that collide sequentially, with the third needing to land in a cup. The tricky part is how a rolling ball can actually get into a cup with raised walls, since the floor can't sink and a ball can't climb over a wall without a ramp.

My solution is to keep the cup's near wall very low, just a few millimeters tall, roughly equal to the base thickness — small enough that the ball's momentum lets it climb the step easily, while the far and side walls stay tall so it stops once inside.

Now I'm thinking about the collision physics between balls: MuJoCo's default contact damping is fairly inelastic, so equal-mass balls colliding would tend to move together rather than transfer velocity cleanly like a Newton's cradle. I need to use a livelier bounce/restitution setting so momentum actually passes through the chain of balls, letting the final ball roll into the cup at a reasonable speed instead of crawling in at a fraction of the original velocity.

I'm also reconsidering the cup geometry — the entry lip height relative to ball radius matters a lot. A ball needs enough energy to climb over an edge, so I'm estimating the velocity threshold using basic energy conservation (mgh vs kinetic energy), and worrying that a ball exiting the far wall at too high a speed could roll back out over the lip just as easily as it rolled in.

Each collision knocks off another 2/7 of speed as sliding converts to rolling, so launching at 3 m/s degrades through three transfers to roughly 1.1 m/s, which isn't enough. I'm considering launching faster, around 4.5 m/s, or alternatively giving the ball spin from the start so it's already rolling and skips that energy loss at each stage.

I'm also reconsidering the ramp geometry itself: with cup walls 4 cm high and a 3 cm ball radius, I need to work out the minimum velocity at the ramp's base to clear the wall, which comes out to about 1.05 m/s, but then I have to check whether a ball moving too fast would simply overshoot the cup entirely.

With wall height 4 cm, base 1 cm, and ball radius 2.5 cm, the inside step is 3 cm, safely exceeding the radius so the ball can't escape. I'm considering building the cup as an open box with a separate ramp plank running from floor level up to the near wall's top, though I need to pin down exactly how the ramp part's endpoints map to its deck surface versus its support post.

Setting the ramp top point at the wall height and foot at floor level, with a 1 cm thick plank, should work fine if those points define the deck surface — any slight burial or offset at the transition won't cause the ball to deflect badly. I still need to figure out how the cup part itself gets positioned relative to the floor and the ball's starting point, since placement seems to depend on referencing the whole part's location rather than its individual pieces.

The ramp foot sits at x=1.04 with height 0, giving a slope of roughly 4/40, about 5.7 degrees. For naming, I'll reference the cup's near wall and specify the ramp top point positionally, like "at 1.44 m along, 4 cm up" rather than relying on relative face references, since that keeps the placement unambiguous.

For the balls, I'm setting radius at 2.5 cm, 100g each, placed on the floor at x=0.2, 0.5, and 0.8 before the ramp foot at 1.04, with rolling and lively bounce behavior plus friction. I'm working out the launch speed and matching spin for ball1 at 2.5 m/s, computing angular velocity as v/r = 100 rad/s, and checking the sign convention so the contact point velocity correctly represents rolling without slipping as it moves in the +x direction.

Then I'm tracing out the collision chain: after collision ball2 picks up roughly 2.5 times restitution while sliding toward rolling speed (around 1.6 m/s with e~0.9), ball1 keeps some spin and may creep into ball2 again, and ball3 ends up around 1.0 m/s after the same scaling — which is borderline against the 1.05 m/s target, so I need to account for the slipping-to-rolling transition distance given μ=0.8 before finalizing these numbers.

Checking the horizontal travel over the 3 cm drop gives about 11 cm, landing on the base before bouncing lively, then striking the far wall at 10 cm high — fine, and the rebound stays contained since the near step's 3 cm exceeds the ball's 2.5 cm radius. I'm testing sensitivity to restitution uncertainty: even if the ball is less elastic (~2 m/s) or more elastic, the flight path still clears the cup with a few cm of margin either way.

I'm extending the cup to 35 cm length and recalculating positions — near wall around 1.415–1.435, ramp foot at 1.015, ball3 at 0.8 still checks out, and the plank/wall geometry still lines up for a clean drop. Now I'm considering ball1's behavior after the collision: with spin transfer and friction, it regains speed to about 1.14 m/s and will chase after ball2.

But I'm worried ball2 might also end up rolling toward the cup after hitting ball3, which complicates the outcome — ball1 could catch up to ball2 again and push it further. I'm testing whether removing ball1's spin changes this: without spin, ball1 slides at 4 m/s, collides almost immediately within 0.3 m before reaching pure rolling, so the dynamics shift. Either way, after the collision ball1 ends up rolling at roughly 2/7 of its incoming speed, and I need to work out what residual speed ball2 carries after hitting ball3.

I'm now checking whether ball2's remaining speed is enough to climb the ramp — if the ramp needs 1.05 m/s and ball2 only has about 0.6, it'll stop partway up and roll back down, possibly intersecting with ball1 again, which seems acceptable. I'm also considering whether to shrink the gaps between balls to simplify the setup, but decide to keep it as is, since the expected outcome (ball1 touches ball2, ball2 touches ball3, ball3 settles in the cup) should still hold for an open box. I also need to account for rolling friction and check the ramp's geometry where it meets the floor, since if the plank's endpoint is measured at its centerline, the deck surface might sit half a thickness above the floor instead of flush.

To keep the step where the ramp meets the floor negligible for a 2.5 cm ball, I'm switching to a thinner 4 mm plank instead of trying to bury the foot below floor level, which keeps the transition smooth enough without complicating the geometry.

