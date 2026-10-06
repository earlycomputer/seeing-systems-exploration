**What happens in the run**

The ball leaves the floor at 9.22 m/s (vx 3.01, vz 8.72) and flies a clean parabola, with horizontal speed holding at 3.01 m/s. It peaks at 3.99 m at x = 2.68 m. It is descending steeply when it reaches the hoop.

At 1.25 s it is at (3.76, 3.35). From there it reaches rim height (z = 3.05) at about x = 3.99 m, only about 0.01 m from the rim center at x = 4.00. For a 0.1194 m ball inside a 0.2286 m inner-radius rim, the center has 0.109 m of room on each side, so this passes cleanly. It goes down through the rim without touching any rim geom; its closest approach is a 0.05 m gap to the front rim, `rim_07`.

Below the rim it passes under the backboard and hits the support pole at 1.66 s. It bounces off the support base, lands on the floor and rolls back out of the scene.

```json
{"what_happens": "The ball launches from the floor at 9.22 m/s and follows a drag-free parabola to a 3.99 m peak. It descends steeply and crosses rim height (3.05 m) at x≈3.99 m, almost exactly at the center of the hoop 4 m away. It drops through the rim without touching it, clearing the front rim by 0.05 m. It then passes under the backboard, bounces off the support pole and base, and rolls back along the floor.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm checking whether the ball actually crosses through the hoop plane by interpolating its position around t≈1.33s near x=4.0, then comparing the closest approach distance to rim_07's surface against the required clearance gap.

Working through the vertical drop math confirms the ball center passes within the rim radius—roughly 0.11m tolerance versus the computed offset—so the shot does go through the hoop before striking the support pole at 1.66s, consistent with the earlier 0.05m clearance estimate.

