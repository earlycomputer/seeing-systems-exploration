**What happens in the run:** The ball leaves the floor at (1.00, 0, 0.12) m, moving 2.87 m/s along and 8.95 m/s up. It peaks at 4.19 m at 0.91 s, then comes down.

**Passing the hoop:** The hoop sits with its rim centre at x = 5.0 m, 3.05 m up, which is 4 m beyond the launch point. Working from the 0.25 s states, the ball's centre reaches about x = 5.0 m, z = 3.05 m at about 1.40 s. It is descending at about 4.8 m/s and moving 2.87 m/s along, so it falls at about 59°. That puts it through the middle of the ring. It touches neither the rim nor the bracket nor the backboard on the way.

**Afterwards:** Below the rim it strikes the hoop's pole at about 1.74 s and 0.8 m up, then clips the pole base. It bounces back onto the floor and is still rolling backward at 1.66 m/s when the run ends. The brief doesn't require it to come to rest.

```json
{"what_happens": "The basketball is launched from the floor at 2.87 m/s along and 8.95 m/s up, peaks at 4.19 m, and descends at about 59° through the centre of the 3.05 m rim 4 m from the launch point (around 1.40 s) without touching the rim, bracket or backboard. It then hits the hoop pole and pole base below, bounces back and is still rolling backward at the end.", "works": true, "problem": ""}
```

---
thinking (summarized):

Wait, I need to reconsider the rim position — "4 m beyond ball" means the rim is at x=5, not x=4 as I assumed, since the ball started at x=1. That changes my calculation of where the ball crosses the hoop.

Checking the trajectory at x=5.0, interpolating between known points gives z≈3.05, so the ball passes right through the rim plane cleanly without hitting anything — the pole contact at x≈5.99 is separate from the hoop. So the shot works: ball center crosses the rim plane at roughly x=5.0, z=3.03, a clean 4m horizontal distance from launch, with no rim or backboard collision recorded.

