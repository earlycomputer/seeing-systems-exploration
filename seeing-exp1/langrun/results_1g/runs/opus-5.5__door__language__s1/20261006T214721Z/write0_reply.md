The door starts open at 80° on a hinge with a spring pulling it toward 0°. Damping is set so it closes in a second or two without flapping, and the lower stop at 0° keeps it from swinging past shut. Once at 0° the spring has nothing left to push against, so the door stays shut.

```world
world  a door swings shut and stays shut

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  colour  grey
  stands  on floor, 12 cm to the right

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  raised         2 cm
  8 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 90°
  spring         20 N·m/rad toward 0°
  damping        10 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm settling on naming the thing itself `door` and having it turn on a hinge named `hinge`, rather than nesting it under a separate panel part.

I'm sizing the door as a 4×80×200cm box weighing 20kg, calculating its moment of inertia about the hinge edge, and picking a spring stiffness and damping (underdamped around ζ≈0.54) so it swings closed from 80° and settles against the 0° stop within a couple seconds without excessive bounce. Then I'm positioning a fixed frame post slightly larger than the door opening to mount it against.

I'm checking placement details: frame on the floor offset to the right, door raised 2cm with an 8cm gap from the frame's left side so they don't collide, and the floor also clear of contact. For the final check, I just need to confirm the door swinging from 80° to 0° should be described as reaching its lower stop.

