The door starts 80° open, and a hinge spring pulls it toward −10°. Because the hinge's range stops at 0°, the spring keeps the door pressed shut against that stop instead of letting it swing through. The damping (20 N·m·s/rad) is close to critical for this panel (about 4.3 kg·m² about its edge with a 20 N·m/rad spring). My estimate is that it closes in about 1.5–2 s without rebounding. I haven't run it.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 cm by 214 cm
  stands  on floor, 12 cm to the right
  colour  grey

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  raised         2 cm
  8 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         20 N·m/rad toward -10°
  damping        20 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm working out the naming structure for the door and hinge bodies, making sure the main body is named `door` while deciding how to structure the frame and panel pieces around it.

For the physics, I'm figuring out realistic dimensions for the door (80cm wide, 200cm tall, 4cm thick, 20kg) and calculating its rotational inertia about the hinge edge, then choosing spring and damping constants so the door swings closed smoothly without bouncing — aiming for slightly overdamped behavior so it settles against the 0° stop rather than oscillating past it.

Trying damping of 20 instead, which gives faster roots and a shut time around 1.5 s with a gentle impact velocity near 0.3 rad/s, so minimal bounce. Now I'm checking the physical layout to make sure the door doesn't collide with the frame post as it swings closed, considering the hinge position, the gap, and the door's elevation above the floor.

So "raised 2 cm" just sets that offset alone, that's fine. I could add a doorstop post at the shut position for realism, but the hinge limit already handles that, so I'll keep it simple and move on to writing it out.

