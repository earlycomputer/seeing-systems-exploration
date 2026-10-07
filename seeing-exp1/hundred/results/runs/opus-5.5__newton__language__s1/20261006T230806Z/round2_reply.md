Ball4 now reaches the box and comes to rest, but balls 1–3 follow it in, which goes against the brief.

**What happened.** The pendulum struck ball1 at 0.44 s. The impacts passed ball1→ball2→ball3→ball4 by 0.60 s. Ball4 left the rail at about 1.25 m/s, landed in the box, hit the far wall and came to rest at x = 1.18 m. The collisions are only partly elastic, so each striker kept about 0.2–0.45 m/s. On the almost frictionless rail nothing slowed those leftover balls. Ball3, ball2 and ball1 slid off the rail end into the box one after another (1.71 s, 2.12 s, 2.40 s). All four balls finished in the box.

**What I changed.** I gave the rail and balls modest sliding friction (0.05). I also set rolling friction (0.005) high enough that the balls should slide rather than spin up. Sliding then costs only a few hundredths of a m/s over each 9 cm gap, so the fast hand-offs survive. The slow leftover balls should stop within a few centimetres to about 20 cm, which keeps them on the rail. Ball4 should still leave the rail end at roughly 1 m/s and drop over the 25 cm near wall into the box.

```json
{"what_happens": "The pendulum strikes ball1 at 0.44 s and the impacts pass ball1→ball2→ball3→ball4 by 0.60 s. Ball4 leaves the rail at about 1.25 m/s, drops into the box and comes to rest against the far wall. Each collision is only partly elastic, so balls 1–3 keep 0.2–0.45 m/s. On the nearly frictionless rail they keep sliding and fall off the end into the box too (at 1.71, 2.12 and 2.40 s). All four balls end at rest in the box.", "works": false, "problem": "Balls 1–3 keep their leftover speed on the frictionless rail and follow ball4 into the box, so it is not just ball4 that is passed the impact and caught."}
```

```world
world  pendulum strikes a row of balls into a box

floor
  friction  0.8, spinning 0.005, rolling 0.002

rail
  is a      box 66.5 by 8.6 by 4 cm
  colour    wood
  friction  0.05, spinning 0.005, rolling 0.005
  at        36.75 cm along, raised 26 cm

rail left lip
  is a      box 66.5 by 1 by 2 cm
  colour    wood
  friction  0.05, spinning 0.005, rolling 0.005
  on rail, at rail's near end, at rail's left side

rail right lip
  is a      box 66.5 by 1 by 2 cm
  colour    wood
  friction  0.05, spinning 0.005, rolling 0.005
  on rail, at rail's near end, at rail's right side

pivot
  is a      point
  at        93.2 cm up

pendulum
  is a           sphere 3 cm radius, 100 g
  colour         grey
  bounce         lively
  friction       0.01, spinning 0, rolling 0
  60 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  80.4°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       5 g
  colour       dark grey
  touches nothing
  attached to  pendulum

ball
  is a      sphere 3 cm radius, 100 g
  colour    white
  rolls
  bounce    lively
  friction  0.05, spinning 0.005, rolling 0.005
  moves     freely
  repeated  4 times, 15 cm apart along
  on rail, 6.5 cm along

box
  is an            open box
  length           50 cm
  width            40 cm
  walls            35 cm
  near wall height  25 cm
  wall thickness   2 cm
  base thickness   2 cm
  colour           orange
  bounce           dead
  friction         1.0, spinning 0.02, rolling 0.02
  its base 60.25 cm beyond rail

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

I notice all balls ending up in the box rather than just ball4 — that seems off for a Newton's-cradle setup where only the last ball should move while others stay on the rail. The collisions aren't perfectly elastic either, with ball1 retaining some residual velocity around 0.45, so I'm judging this behavior as likely incorrect against the expected physics.

With condim 3 rolling friction, a sliding ball will spin up and then roll freely forever since there's no rolling resistance to stop it — so just adding friction won't make residual balls stop, they'd just keep rolling into the box. I'm considering whether a small lip or bump at the rail's end could block slow residual balls while letting the fast, deliberately-struck ball pass through.

Rolling friction won't help a nonspinning sliding ball since it acts on angular velocity, so that path's dead. Sliding friction with low μ=0.01 barely slows the ball toward rolling, leaving residual velocity that just keeps rolling indefinitely — not useful either. I'm now considering whether small ridges or seats along the rail could help balls settle, or whether adjusting mass might change the dynamics enough to work.

Residual energy from inelastic collisions between equal balls seems unavoidable — computing the restitution coefficient from the velocities gives e≈0.6, meaning about 20% residual speed survives each hit. I'm reconsidering whether high sliding friction with no rolling (condim 3) could damp things out, recalling an earlier test run where high friction stopped the balls quickly but caused too much loss through the chain.

I'm comparing stage efficiencies from that run and wondering about an alternative design — maybe a small ramp or incline at the rail's end, since ball4 moves much faster than the residual balls and could jump over a barrier that stops the slower ones, using the condition that velocity squared must exceed twice gravity times ramp height to clear it.

A 3 cm rise would let ball4 (at 1.25 m/s) clear while residual balls below 0.45 m/s roll back. But I realize those rolled-back balls would travel back along the frictionless rail toward the still-swinging pendulum, potentially colliding with it or falling off near the pivot — so I need to think through what happens to them after they retreat.

The brief technically only cares that ball4 ends at rest, but if residual balls get re-struck by pendulum swings and sent over the kicker, that's a problem. I think the fix is to make the rail itself dissipative for slow balls using rolling friction (small coefficient, constant deceleration), which will gradually settle any stray balls without needing a separate mechanism.

I'll mark that approach as not working and try again. Maybe a kicker combined with an end stopper and light rolling friction could settle the residual energy, but I need to think through whether residual balls would just roll back and collide with the ball behind them at low speed, restarting the chain reaction instead of truly stopping.

Even with inelastic collisions and friction damping, balls drifting back could get struck again by the oscillating pendulum near the rail start and get kicked forward again — I'd need to check whether that nudge is enough to send them back over the kicker threshold, which depends on the pendulum's swing amplitude and the resulting velocity at the bottom of its arc.

I wonder if there's a cleaner way to kill residual speeds entirely rather than tuning damping — maybe through elasticity tricks or exploiting how struck balls take most of the energy while the striker keeps its spin and friction state. That spin retention could explain why ball1 kept rolling after impact in run 1, so maybe I can lean into that mechanic instead of fighting it.

Running the numbers on friction coefficients: at low sliding friction, balls barely decelerate over the short gaps between them, and residual velocities just transition into slow endless rolling since there's no rolling resistance modeled in that collision type. Switching to a friction setting with actual rolling resistance would at least guarantee eventual decay, though I need to check how that interacts with the sliding-to-rolling transition during spin-up.

Tracing the collision chain: ball1 arrives at ~2.26 m/s, each transfer loses 20%, so ball2 ~1.81, ball3 ~1.43, ball4 ~1.12, dropping to about 1.03 m/s after sliding to the rail end with friction. Then I'm working out the box's flight: falling 0.28 m takes about 0.24 s, carrying the ball roughly 0.25 m horizontally to land near x~0.95 inside the box.

For residual motion, I'm checking how far each ball coasts after collision—ball1 stops within about 0.2 m, ball2 within roughly 0.13 m, ball3 travels about 8 cm further—accounting for possible re-collisions that nudge things slightly, with the pendulum itself continuing to swing with reduced amplitude after the impact.

I'm setting rolling friction to 0.005 to match the rail's value, accounting for it in the contact model even though MuJoCo's cone approximation makes the effect imprecise. Estimating how rolling resistance decelerates each ball — for ball4 starting at 1.12 m/s, the combined slip-then-roll transition and friction over 18 cm brings it down to roughly 0.47 m/s before its next flight phase.

Now I'm checking whether the ball clears the near wall: tracking the ball's center position and drop height as it tips over the rail edge at x=0.70, comparing against the wall's top surface at 0.25 and far edge at 0.73, with only about a 5 cm vertical gap to work with.

Good, the ball bottom at 0.28 clears the 0.25 wall threshold, landing near x=0.81. I'm also double-checking the pendulum doesn't clip the rail corner during its swing, settling on consistent friction coefficients (μ=0.05, rolling 0.005, spinning 0.005) across balls, rail, lips, and pendulum contacts, and confirming the pendulum-struck ball's resulting velocity looks reasonable.

Confirming rolling friction in MuJoCo acts as a bounded constraint resisting relative rotation rather than a free-spin generator, so it behaves correctly here. Now I'm ready to write out the world definition.

