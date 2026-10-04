## What the picture shows

**Pendulum.** It starts high on the left (the lightest copy at about x = −0.5, z = 0.3). It sweeps down through the bottom and swings out to about x ≈ 0.3. Its copies make a fan around the hinge, and it keeps swinging for the rest of the run.

**Ball.** Unlike the last run, no dark copy of the ball sits on the floor between the pendulum and the ramp. None appears beyond the cup either.

**Cup.** In the plan view the cup and its notch show darker shading inside, which looks like the ball sitting in the cup. In the side view a ball inside would be hidden behind the 0.12 m walls.

**Caveat.** At 128 px I can't pick out the ball itself. I'm inferring it is in the cup because no ball shows anywhere else at the end, not because I can see it there.

```json
{"what_happens": "The pendulum swings down from the left, strikes the resting ball at the bottom of its arc, and keeps swinging. The ball rolls along the floor, up the short ramp, over the notch in the cup rim and into the cup centred 1 m away. Its final copy is no longer visible on the floor, so it appears to stay inside the walls, though I can't see the ball itself at this resolution.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm working out the pixel-to-meter scale, placing the ball's start position around px 46 and the cup center near px 106, then checking the top-down view to locate the ball dot relative to the pendulum fan and ramp near px 43-85.

In elevation the ball sitting inside the cup would be hidden by the walls, so it wouldn't show as a separate visible dot—that occlusion could explain why I can't spot it outside the pendulum fan. From above though, the ball inside the cup should appear as a darker blob near the cup's interior, which I think I'm seeing as a faint darker patch near the center-right of the cup shape, suggesting the ball ended up inside rather than rolling back toward the pendulum's starting position.

