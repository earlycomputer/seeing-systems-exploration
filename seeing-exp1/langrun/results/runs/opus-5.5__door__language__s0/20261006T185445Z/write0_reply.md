The door is a hinged panel beside a fixed frame. It starts swung open at 80°, and a spring pulls it shut. Damping makes it settle onto the 0° stop instead of rattling. The spring aims at −5°, slightly past shut, so it keeps pressing the door against the stop.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor, 1 m along
  colour  grey

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  raised         2 cm
  8 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 90°
  spring         20 N·m/rad toward −5°
  damping        15 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

Checking the motion:

- **Swing:** The door's inertia about its hinged edge is about 4.3 kg·m². With the 20 N·m/rad spring, the swing frequency is about 2.2 rad/s.
- **Closing:** The damping of 15 N·m·s/rad is about 0.8 of critical. So the door should swing closed in roughly 1.5 s, at most tap the stop once, and then stay there for the rest of the 6 s.
- **Gravity and contact:** The hinge axis is vertical, so gravity doesn't turn the door. The panel is raised 2 cm, so it never drags on the floor.

---
thinking (summarized):

I need to figure out the exact naming convention for the door's hinge joint — the part specifies the panel turns on a joint named "hinge", so I should check whether the body/joint structure expects a prefixed name like "door.hinge" or just "hinge" directly.

Working through the physics: a door 80cm wide, 200cm tall, 4cm thick, 20kg has moment of inertia about its hinge edge of roughly 4.27 kg·m². With a spring constant of 20 N·m/rad pulling it toward closed, I'm calculating the natural frequency and critical damping (~18.5) to decide how stiff the damping should be so it swings shut, settles against the 0° stop, and doesn't bounce back open.

I'm also checking geometry so the door panel rotating about its hinge edge doesn't collide with the frame, since the panel is offset 8cm from the frame post and the thickness-driven sweep radius is small.

Drafting the final spec: frame as an 8×8×214cm post on the floor positioned 1m along, and door as a 4×80×200cm 20kg panel raised 2cm off the floor, offset 8cm from the frame's left side, hinged about z at its right edge, constrained to swing 0°–90°, with a 20 N·m/rad spring biasing it toward −5°, damping of 15, and an initial rotation of 80°. I still need to pin down the along-axis position since the offset clause only fixes the lateral placement.

Starting angle of 80° with range up to 90° seems fine, and the spring targeting −5° outside that range should still be acceptable as a reference point. Maybe I should color the wood too.

