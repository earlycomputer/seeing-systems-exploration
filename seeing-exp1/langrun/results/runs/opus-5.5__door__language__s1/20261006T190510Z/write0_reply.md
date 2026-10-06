The door is a heavy panel hung on `hinge` and opened 80° at the start. Its spring pulls it toward 0°, the shut position. The hinge's range stops at 0°, so the door cannot swing past shut. Damping takes out most of the swing's energy, and the stop absorbs the rest. The spring then holds the door against the stop.

I have not run this. I estimated the timing by hand. The panel's inertia is about 4.3 kg·m². That gives roughly 0.6 of the damping needed to stop any rebound. It should hit 0° within about a second and settle long before 6 s.

```world
world  a door swings shut and stays shut

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor
  colour  wood

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  at             8 cm outside frame's left side, raised 2 cm
  turns on       hinge, about z, at its right side
  swings         from 0° to 120°
  spring         40 N·m/rad toward 0°
  damping        16 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm unsure whether the hinge should be a nested part name like "door_hinge" or just "hinge," so it's safer to define the door as a top-level thing directly with "turns on hinge," then have it spring shut from an open angle back toward closed.

Working through the physics, I compute the moment of inertia for an 80cm×2m×4cm 20kg panel rotating about its edge (~4.27 kg·m²), then find the natural frequency with a spring constant of 40 (ω≈3.06 rad/s) and critical damping (~26) needed for settling within 6 seconds with minimal bounce. Since a spring pulling toward exactly 0° combined with a hard stop at 0 would only approach asymptotically, I'm considering biasing the spring target to slightly past the stop (like -10°) so the door presses firmly into the limit and rests there, checking that the resulting limit penetration from the spring torque stays small enough to be negligible.

I settle on keeping the spring equilibrium at 0° with damping around 12 (underdamped, ζ≈0.46), reasoning that MuJoCo's hinge limit will catch the door as it swings closed and absorb most of the impact energy, letting it settle near 0° within a couple seconds without needing to bias toward a negative angle. I also note the door needs to be raised slightly off the floor to avoid collision, and I'm considering whether a hinge-side frame post is necessary.

For the panel geometry, I'm sizing it as a thin box roughly 4×80×200 cm, hinged at its right edge, rotating through a 0–120° range, and checking that a frame post placed about 8 cm from the hinge axis clears the sweep of the panel's corner (which is only ~2 cm from the axis given the panel thickness), so no collision occurs.

I'll keep the frame at the origin on the floor, and note that the expected outcome should include the door reaching its lower stop.

