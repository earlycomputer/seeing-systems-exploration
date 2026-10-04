**What I expect to happen**

The door is a 20 kg panel, 0.9 m wide and 1.96 m tall. It hangs on a vertical hinge with a return spring (stiffness 40, springref 0) and a damper (damping 25). The `start` keyframe opens it to 1.2 rad.

- **Inertia:** about the hinge axis it is roughly 20·(0.04²+0.9²)/12 + 20·0.45² ≈ 5.4 kg·m².
- **Natural frequency:** ωn = √(40/5.4) ≈ 2.7 rad/s.
- **Damping ratio:** critical damping would be 2√(40·5.4) ≈ 29.4, so 25 gives ζ ≈ 0.85.
- **Swing:** the door swings back toward 0 with essentially no overshoot. The undamped overshoot would only be about 0.008 rad, and the joint limit at 0 stops it anyway. It should reach about 0 within roughly 1.5–2 s.
- **Holding:** the spring and damper keep it there for the rest of the 6 s.
- **Gravity:** it has no effect on a vertical hinge.

**Contacts**

- **Floor:** the panel's bottom edge sits at z = 0.02, so it never touches the floor.
- **Frame post:** the post occupies y ∈ [-0.16, -0.08]. The door's hinge edge only reaches about y ≈ -0.02 while opened, so they never collide.

Nothing obstructs the swing, and the door ends shut, held at `hinge` = 0.

```json
{"what_happens": "Starting open at 1.2 rad, the near-critically-damped hinge spring (zeta ~0.85) swings the door back to hinge = 0 in about 1.5-2 s, the lower joint limit stops any overshoot, and the spring holds it shut for the rest of the 6 s with no contacts interfering.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm working out the door panel's geometry and mass distribution to compute its moment of inertia about the hinge axis, accounting for the panel's offset position relative to the hinge.

From there I calculate the natural frequency and damping ratio of the spring-damper system, finding it's underdamped with ζ≈0.85, giving a negligible overshoot (~0.0076 rad) that's effectively blocked by the joint limit at zero anyway.

Now I'm checking for collisions between the door frame post and the swinging panel, working out how the panel's extent transforms when rotated about the z-axis by the hinge angle.

At θ=1.2 radians the panel corners don't reach far enough in y to overlap the post's bounding box, so there's no contact there, and the panel bottom clears the floor too. Since the hinge is vertical there's no gravity torque to worry about, and I'm now checking whether parent-child body pairs (door attached to world) are automatically filtered from collision checks.

Looking at the settling dynamics, the decay rate gives essentially zero displacement within the 6-second window, with the hinge angle converging to roughly 0 within about 1.5 seconds and staying there due to the spring and limit settings.

Visually this all checks out — the door swings shut and stays closed, held by the spring rather than a latch, with the frame post only on the hinge side as expected.

