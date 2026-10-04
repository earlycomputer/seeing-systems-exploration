## Expected run

1. **Swing and hit.** The pendulum is released from 40° back and swings down under gravity. Its 1 kg bob reaches about 1.5 m/s at the bottom of its arc, 5 mm above the floor. Just past the lowest point it meets the 50 g ball squarely at centre height (z = 0.03), pushing it along +x.
2. **Roll to the ramp.** The ball slides briefly, then rolls straight along y = 0. My estimate is about 1–1.6 m/s.
3. **Climb.** The ball rolls up the separate 12° ramp onto the top of the cup's 4 cm front lip. Clearing it needs only about 0.75 m/s.
4. **Drop in.** The ball drops into the cup interior, which runs from x = 0.90 to 1.10 and is centred at x = 1.0. That centre is 1 m from the ball's start.
5. **Settle.** The ball hits the 10 cm back wall with its centre well below the wall top. It loses energy in the bounces and stays trapped, because every wall is taller than its 3 cm radius. This should all happen within about a second of the 6 s run.

## Other checks

- The pendulum keeps swinging in the y = 0 plane well short of the cup.
- The keyframe's qpos order is hinge first, then the free joint, which matches the order the bodies are declared.
- The cup body and its geoms are now centred at x = 1.

```json
{"what_happens": "The pendulum released at 40 degrees swings down and its heavy bob strikes the resting ball at centre height just past the bottom of its arc; the ball rolls along +x at roughly 1-1.6 m/s, climbs the shallow ramp over the 4 cm front lip and drops into the walled cup centred at x = 1 m, where it bounces off the taller back wall and remains trapped for the rest of the 6 s run.", "works": true, "problem": ""}
```

---
thinking (summarized):

Checking the ramp body setup, confirming it's a static body with separate name space from its geom. I'm verifying the pendulum bob reaches the ball right near the bottom given the pivot position and radii, and thinking through whether the resulting ball speed from the collision makes sense.

Tracing the ball's trajectory along the ramp and over the lip into the cup, checking clearances at the front and back walls so it lands and bounces cleanly without escaping. I'm also confirming the pendulum swings back through its arc without interfering with the cup, and double-checking the keyframe qpos ordering matches the hinge joint before the ball's free joint.

Cup geoms span 0.89 to 1.11, so the center sits at x=1.0, matching the ball's 1-meter travel distance from its start at x=0. Rolling without friction isn't an issue since the ball ends up trapped in the cup regardless—overall the setup looks sound.

