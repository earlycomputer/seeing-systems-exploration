The door starts open at 70° on a hinge whose range stops at 0°. Its spring aims a little past shut, at −10°, so once the door closes it stays pressed against the 0° stop and doesn't drift. The damping is just under critical, so it closes within a few seconds instead of slamming and bouncing. It hangs 3 cm clear of the jamb so its edge can't catch the jamb as it turns.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

jamb
  is a    box 8 by 8 by 214 cm
  stands  on floor
  colour  wood

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  raised 2 cm, 3 cm outside jamb's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         20 N·m/rad toward −10°
  damping        15 N·m·s/rad
  starts turned  70°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm uncertain whether naming the door part "door" would make its hinge become "door_hinge" or just "hinge," so it seems safer to build the door directly as a top-level object named "door" that turns on a hinge called "hinge," starting it swung shut and staying that way.

I'm computing the physics: for an 80cm-wide, 2m-tall, 4cm-thick, 20kg door, the moment of inertia about the hinge edge gives a natural frequency with spring constant 20 N·m/rad, then comparing critical damping (~18.5) against a chosen damping of 15, which leaves it slightly underdamped so it may overshoot a bit before the 0° limit catches it, and estimating closing time from 70° to near 0°.

To prevent bouncing off the stop, I'm adjusting the spring target to slightly negative (around −10°) so the door is driven firmly into the closed position and held there with a small, physically negligible penetration torque. I'm also considering whether to add a jamb or stop post near the hinge side to constrain the door's swing, making sure it's positioned close without causing collision issues at rest.

Working out the frame and floor geometry now, deciding whether positive rotation swings the free edge toward −x so a stop post on the far side would match the joint limit, and relying mainly on the joint limit itself with small clearance gaps around any added posts for robustness.

Now I'm specifying the door's actual properties: dimensions, mass, color, its 2 cm raise, 1 cm offset from the jamb's left side, hinge placement at the right side about z, swing range from 0° to 100°, spring and damping values pulling toward −10°, and a starting angle of 70°. I'm noting that the vertical and lateral position are already fixed by the raise and offset constraints, while the along-axis position follows the same default pattern as the jamb, with the hinge sitting just 1 cm from the jamb.

When the door rotates through its 70° starting angle, I want to check that the swinging corners of its right face (radius 2 cm from the hinge axis) won't clip the jamb, since the axis itself sits only 1 cm away — so I'm widening that gap to 3 cm to keep the 2 cm corner radius safely clear. I also confirm that a spring target outside the hinge's allowed range should still work fine as a springref in MuJoCo, and I'm planning to include an expectation that the door settles against its lower stop.

