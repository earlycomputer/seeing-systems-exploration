I built the door directly rather than from the library's door part, so that the body is named exactly `door` and its hinge `hinge`.

The door starts open at 80°. A spring pulls it toward −5°, which lies past the hinge's 0° stop. The door swings shut, lands on that stop, and the spring keeps pressing it there. The damping is set below critical, so it closes in about a second and does not drift back open.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

-- a jamb beside the hinge side, for looks only
jamb
  is a      post 8 cm square, from floor to 2.15 m up
  1 m along, 46 cm to the right
  touches nothing
  colour    grey

door
  is a           box 4 by 80 by 200 cm, 20 kg
  raised         1 cm, 1 m along
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 110°
  spring         20 N·m/rad toward −5°
  damping        12 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm trying to figure out how the door and hinge naming convention works here—whether the hinge gets prefixed with the part name or stays as just "hinge". Given the uncertainty, I think it's safer to construct the door part manually myself rather than rely on an assumed naming scheme.

For the design, I'm working through a box-shaped door panel roughly 4×80×200 cm, hinged about a vertical axis at its edge. I want it to spring closed from an open 80° position and settle against a stop at 0°, using a spring that preloads slightly past the stop so it stays shut rather than bouncing. I calculate the moment of inertia (~4.27 kg·m²) and work out spring and damping constants to get a reasonably fast but non-bouncy closing motion within the 6-second requirement, checking that the damping ratio gives a sensible settling time and that the stop will catch it without excessive rebound.

I'm also thinking about floor clearance and a simple door jamb or post near the hinge, making sure the rotating door edge doesn't collide with it by adding enough gap or marking it as non-colliding, since the goal is just a basic swinging door rather than a full frame.

For positioning, I'll settle on "raised 1 cm, 1 m along" as the placement, and note the door should stop at its lower limit, starting rotated 80° and swinging between 0° and 110°.

