MuJoCo ran the scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 2.1° as MuJoCo applies it; its geoms: door_panel; starts at 68.8°, still

What happened, in order:
 0.00 s  door starts at 68.8°, outside its range of 0° to 2.1°
 0.00 s  door is at its largest at the start, 68.8°
 0.06 s  door reaches its upper stop (2.1°) moving -1041°/s
 0.06 s  door reaches its lower stop (0°) moving -1032°/s
 0.08 s  door is at its smallest, -6.5°
 0.14 s  door reaches its lower stop (0°) again moving +103°/s
 0.16 s  door reaches its upper stop (2.1°) again moving +93°/s
 0.20 s  door reaches its upper stop (2.1°) again moving -11°/s
 0.48 s  door reaches its lower stop (0°) again moving -5°/s

State every 0.25 s:
0.00 s: door at 68.8°, still; touching nothing
0.25 s: door at 2.1°, turning -10°/s; touching nothing
0.50 s: door at 0.4°, turning -4°/s; touching nothing
0.75 s: door at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at 0.0°, still; touching nothing
</history>
