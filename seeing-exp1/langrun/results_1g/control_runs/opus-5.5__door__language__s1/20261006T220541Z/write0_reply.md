This builds the door directly as a top-level thing, so its body is named `door` and it turns on `hinge`. The door starts 70° open. A spring pulls it toward −10°, just past the 0° stop, so the spring keeps pressing the door against the stop. Damping makes it shut without a big rebound, and the preload holds it shut.

```world
world  a door swings shut and stays shut

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor, 1 m along
  colour  wood

door
  is a           box 4 by 80 by 200 cm, 15 kg
  raised         2 cm, 1 m along, 8 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 110°
  spring         20 N·m/rad toward −10°
  damping        5 N·m·s/rad
  starts turned  70°
  colour         wood

expect
  door reaches its lower stop
```

The door's moment of inertia about the hinge edge is about 3.2 kg·m². With the 20 N·m/rad spring, it should reach 0° in roughly half a second. After that it should settle against the stop well within the 6 s run, and the −10° spring target keeps it held at 0°. I haven't run this in MuJoCo, so the timing and the size of any rebound off the stop are estimates.

---
thinking (summarized):

I'm thinking the door should be named `door` with pieces door_frame and door_panel, and the panel turns on a hinge named `hinge`, so each top-level part becomes a MuJoCo body with its pieces as named geoms.

For the design: a fixed frame post and a door panel box (4×80×200cm, 15kg) that turns on the z-axis hinge at its right edge, swinging between 0° and 110° with damping to settle. To make it "stay shut," I'm giving the spring a slight negative target angle like −10° instead of 0°, so it preloads against the stop rather than resting with zero force exactly at the limit.

Working out the dynamics: the door's moment of inertia about its edge is about 3.2 kg·m², so with spring stiffness 20 N·m/rad I get a natural frequency around 2.5 rad/s and critical damping near 16 — I'll use something lower like 4-6 for an underdamped swing that closes in roughly half a second and settles within a few seconds, accepting a small bounce off the stop. For geometry, I'm placing an 8×8×214cm frame post on the floor and positioning the door panel raised 2cm with its hinge edge in the gap beside the post, matching how the library expects hinge placement.

Checking clearance: rotating the door 70° about its hinge edge, the corners near the hinge only move a couple centimeters, well clear of the frame post sitting 8cm away, so no collision there. Since the door's bottom is raised 2cm it also won't scrape the floor, and the joint limit itself serves as the stop.

For positioning, I'll align both frame and door along a shared coordinate (say 1m along), with the frame sitting on the floor and the door raised 2cm and offset 8cm outside the frame's left side, noting the door should rest at its lower stop.

Now I need to fill in the remaining properties: marking it as a door that's a kind of box, specifying it turns on and swings via a spring with damping, setting its starting state and colour, giving it a mass of 15 kg, and a damping value of 5.

