The door is a single hinged panel. A spring pulls it toward −10°, but the hinge range stops at 0°. It starts open at 75°, swings shut, and is then held pressed against the 0° stop, so it stays shut. Damping keeps it from bouncing off the stop.

```world
world  a door swings shut and stays shut

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

jamb
  is a      box 8 by 8 by 215 cm
  colour    grey
  stands    on floor, 1 m along, 0 cm to the left

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  at             1 m along, 4 cm outside jamb's left side, raised 1 cm
  turns on       hinge, about z, at its right side
  swings         from 0° to 110°
  spring         20 N·m/rad toward −10°
  damping        6 N·m·s/rad
  starts turned  75°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm working out how to define the door object directly as a box turning on a named hinge, rather than relying on an unclear internal naming convention, and sketching the door's thickness as a starting dimension.

For the physics, I'm computing the door's moment of inertia about its hinge edge and sizing a critical damping coefficient against the spring constant so it settles smoothly into place within a few seconds. I'm reconsidering the spring target angle — rather than springing exactly to 0° with a hard limit there, it's better to spring slightly past 0° so the door presses firmly against its stop and stays shut, using moderate damping so it settles without excessive bouncing.

Now I'm checking the geometry for collisions: gravity doesn't torque the hinge since it's about the vertical axis, and the door's slight floor clearance avoids friction there, but I need to verify that a nearby frame post doesn't clip the panel's corners as it sweeps through its arc, since the panel's thickness gives its corners a radius that could intersect a post placed too close to the hinge side.

I'm resolving the door's floor clearance wording and settling on a frame post defined as a simple box rather than relying on ambiguous point references, since the post syntax needs a named endpoint.

