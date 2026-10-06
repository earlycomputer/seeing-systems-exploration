The door starts open at 70° on a damped spring that pulls slightly past shut, toward −5°. The hinge's lower stop at 0° catches it, and the spring keeps pressing it there, so it closes and stays closed.

The numbers, for a door that is 20 kg and 0.8 m wide:

- **Inertia:** about 4.3 kg·m² about the hinge.
- **Spring:** 20 N·m/rad gives a natural frequency of about 2.2 rad/s.
- **Damping:** 14 N·m·s/rad is a little under the critical value of 18.5. It swings shut in about 1–2 s instead of creeping toward 0°.
- **Holding torque:** about 1.75 N·m keeps it on the stop for the rest of the 6 s.

```world
world  a door swings shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  colour  grey
  stands  on floor, 1 m along

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  at             1 m along, 8 cm outside frame's left side, raised 2 cm
  turns on       hinge, about z, at its right side
  swings         from 0° to 120°
  spring         20 N·m/rad toward −5°
  damping        14 N·m·s/rad
  starts turned  70°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm deciding to build the door as a top-level object named `door` that turns on a hinge, rather than relying on ambiguous part-prefixed naming. I'll set it up so the door starts rotated 70° open, with a spring pulling it toward 0° and damping to make it swing shut naturally and stay closed.

Working through the physics: the door is 80cm wide, 200cm tall, 4cm thick, 20kg, so I'm computing its moment of inertia about the hinge edge (~4.27 kg·m²). I'm tuning spring stiffness around 20 N·m/rad and damping slightly below critical (~14 instead of 18.5) so it swings closed within a few seconds and presses firmly against a stop near 0°, biasing the spring target slightly negative (-5°) to ensure it settles against the limit rather than hovering.

Now I'm laying out the geometry: the door panel as a box positioned with its hinge at the right edge, raised 2cm off the floor to avoid floor contact, and a frame structure (post roughly 8x8x214cm) offset to the right with a small gap between frame and panel. I'm checking that gravity produces no torque about the vertical hinge axis and considering whether the panel might collide with the frame during its swing.

I'll place the frame on the floor 1 m along, and position the door similarly 1 m along to match, expecting it to settle against its lower stop.

