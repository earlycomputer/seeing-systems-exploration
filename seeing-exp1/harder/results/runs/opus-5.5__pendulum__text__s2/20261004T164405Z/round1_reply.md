## What I expect to happen

**The strike.** The pendulum starts 36° back, with its 0.5 kg bob about 0.34 m behind the ball. It swings down and reaches about 1.36 m/s near the bottom. It meets the 0.05 kg ball about 0.02 rad before vertical, with both centres at about 0.03 m height, so the push is almost purely along +x. Because the bob is ten times heavier, the ball leaves at roughly bob speed. Floor friction then turns its sliding into rolling. The bob shoves it a little longer during that phase, which keeps some of the speed. I expect a rolling speed of about 0.9–1.3 m/s.

**The roll.** Ball and floor use condim 3, which has no rolling resistance. The ball should roll straight down the y = 0 line at nearly constant speed and reach the ramp foot at x ≈ 0.87 m in under a second.

**The ramp and lip.** Climbing the 14°, 1.5 cm ramp needs at least about 0.64 m/s, so there is margin. The ball leaves contact at the top edge and hops over the lip. At 1 m/s it lands at about x ≈ 0.98, inside the cup, which runs from 0.94 to 1.06.

**The cup.**
- **Low speeds:** the ball simply rolls off the lip edge and drops inside.
- **High speeds** (up to about 1.8 m/s, if the bob contact is unusually bouncy): the ball hits the 8 cm back wall about 5 cm up. Topspin lifts it only a few millimetres more against the wall. It loses most of its horizontal speed and falls back in.
- **Settling:** the floor plate uses condim 6 with rolling friction 0.02 m, which quickly kills both rolling and sliding. The ball stops near the cup centre, x ≈ 1.0 m from its start, and cannot climb back over the 1.5 cm inner lip face.

**Afterwards.** The pendulum keeps swinging around x ≈ 0 for the rest of the 6 s. It never reaches the cup.

## Caveat

The ramp belongs to the `cup` body. The cup body and its interior are centred at x = 1.0. If something instead measured the cup by the bounding box of all its geoms, the ramp would pull that centre to about 0.97 m. I'm treating the body position and interior as the cup's centre, so I don't count this as a failure.

I haven't run it, so the strike speed and the landing point are estimates. The cup's catch range (about 0.7–1.8 m/s) covers the speeds I expect.

```json
{"what_happens": "The pendulum swings down from 36 degrees and its heavy bob strikes the ball through its centre. The ball rolls along +x at roughly 0.9-1.3 m/s, climbs the short ramp, hops the low lip and lands inside the cup. If it is fast it hits the back wall, then the high-rolling-friction floor plate stops it at about x = 1.0 m, 1 m from its start. The pendulum keeps swinging near the origin.", "works": true, "problem": ""}
```

---
thinking (summarized):

Let me recheck the pendulum math: with the body position and local bob offset, rotating by q about y gives the bob landing at roughly (-0.339, 0, 0.125) in world space, and gravity correctly pulls it back toward q=0, confirming the setup works.

Estimating impact speed using energy conservation with the rod's small moment of inertia, the bob hits the floor around 1.36 m/s. With soft contact settings, there's some penetration during impact, but momentum transfer pushes the lighter ball forward at roughly double the bob's post-collision speed, and with no rolling friction specified, the ball should roll at constant velocity afterward.

I'm double-checking the ramp's rotation math: a -14° rotation about y correctly tilts the local x-axis upward in the +x direction, which matches the intended ramp geometry, and I'm confirming the ramp's world-space center position and top surface coordinates align with expectations.

At the top, checking whether the ball maintains contact over the convex kink—computing the centripetal condition shows v>0.54 clears it, so the ball actually leaves the ramp surface and becomes a projectile. I'm estimating where it lands, likely around x≈0.99-1.03, and need to check if that's on the base floor or against the back wall, accounting for the lip's inner face position.

I'm checking whether the ball clears the lip's inner edge without getting stuck — since the lip is narrow and the ball maintains forward momentum, it should roll past the edge and drop down, continuing to gain forward push as it passes.

Then I consider what happens once it lands: with rolling friction around 0.02 it's a mild torque limit on angular velocity rather than a hard stop, so the ball likely keeps rolling toward the back wall. If it hits that wall with some softness and rebounds slightly, I need to check whether a slow rebound could actually climb back over the lip's small vertical step, which seems unlikely at low speed.

A more interesting concern hits me: if the ball is spinning forward (topspin) when it contacts the wall, the surface velocity at the contact point actually points downward, meaning friction acts upward on the ball — so the spin could make it climb the wall rather than just bounce off, and I need to check whether that climb could exceed the wall's height given typical spin rates.

Checking the bob's swing after striking the ball: it carries some residual energy, rises a bit, and swings back and forth, never approaching the cup again. I should also consider whether friction between the bob and ball during contact could impart unwanted spin on the ball during separation.

The interplay between bob-ball friction and floor friction is getting complicated, but the net effect seems to be that the ball ends up moving around 1–1.3 m/s, with the bob-ball contact force tending to oppose spin-up while floor friction acts in its own direction at the contact point.

Actually if contact is softer and more elastic given the mass ratio, the ball could rebound up to ~2.5 m/s, rolling around 1.8 m/s worst case. Tracing the ramp exit trajectory at 14°, I'm checking whether the ball clears the gap or just reaches the back wall — the numbers suggest it lands right around the inner wall boundary at x≈1.03-1.10, so it likely clips the back wall near that height.

Working through the impact point: at x=1.03 the ball hits around z=0.05, which is under the 0.08 wall height, so it's fine. Now I'm considering what topspin does during this collision — friction against the wall could convert spin into upward velocity, so I'm estimating the friction impulse limits using the ball's moment of inertia and the relative sliding velocity at contact.

I'm getting roughly a 7mm rise from the spin-to-vertical conversion, which still keeps the ball within bounds, and double-checking the floor contact at z=0.03 is also fine.

Checking the ramp-to-cup contact and rolling dynamics—MuJoCo's condim 3 handles this without explicit rolling resistance, so that should work out. Now I'm second-guessing how "cup centre" gets defined: the ball starts at x=0 and the cup body sits at x=1, but since the ramp geometry is attached to the cup body and spans roughly 0.87 to 1.07, a bounding-box calculation of the cup's geoms would put its centre closer to 0.97 rather than exactly 1.0 — worth considering whether a checker would use the body position or the geom AABB centre.

A cleaner fix would be moving the ramp into the worldbody as its own separate geom rather than keeping it as part of the cup body, since the brief only requires that the cup's own geoms belong to it — this would make the cup's remaining geoms span symmetrically around x=1.0. It's a minor ambiguity though, and the underlying physics setup genuinely satisfies the brief's intent either way, so I'm weighing whether this is worth flagging as a real issue or just a nitpick.

