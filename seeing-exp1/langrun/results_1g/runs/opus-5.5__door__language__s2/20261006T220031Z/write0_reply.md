The door is a 20 kg panel hinged on a fixed post. It starts open at 90°, and a spring toward 0° swings it shut against its 0° stop. Damping below critical lets it close briskly, then kills any rebound so it stays shut.

```world
world  door swings shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor
  colour  grey

door
  is a           box 4 by 100 by 200 cm, 20 kg
  colour         wood
  raised         1 cm, 3 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         20 N·m/rad toward 0°
  damping        15 N·m·s/rad
  starts turned  90°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I need the door part named `door` to turn on a hinge, but I'm unsure whether MuJoCo would name that hinge `hinge` or `door_hinge` automatically, so it's safer to construct the model explicitly myself rather than rely on naming conventions.

For the physics, I'm calculating the door's moment of inertia (about 6.67 kg·m² for a 1m×2m, 20kg door) and working out spring/damping values so it swings from 90° closed toward 0° without excessive bouncing. A spring constant of 20 N·m/rad gives critical damping around 23, so using damping around 15 means it's slightly underdamped but should settle at the 0° stop within the 6-second window, possibly with a small bounce that gets absorbed. I'm also considering biasing the spring equilibrium slightly past 0° so the door stays pressed firmly against the stop once closed.

Now I'm working out the layout: a fixed frame post (8×8×214 cm) on the floor, with a door (4 cm thick, 100 cm wide, 200 cm tall) hinged at its right edge, raised 1 cm off the floor and offset with a small gap from the frame's left side to avoid unwanted collisions while still closing properly against it.

That corner would push 2cm into the frame if the gap is only 1cm, so I need a 3cm gap instead. The door starting at 90° sits on the negative x side, which seems fine, and I'll keep it raised 1cm above the floor since friction isn't a concern there. For positioning, I'll specify it as raised 1cm and 3cm outside the frame's left side on one line, letting it align with the frame along the default axis.

Since raised already fixes the vertical position, I just need to keep things simple -- I'll put the frame at the origin and let the door reference it, similar to how the part library structures its positioning.

