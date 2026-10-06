Your expectations, checked against the run (2 of 2 hold):

- holds: door reaches its lower stop (at its lower stop (0°) at 1.01 s)
- holds: door touches jamb (first touch at 1.01 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 91.6732° as MuJoCo applies it; its geoms: door_panel, door_knob; starts at 68.8°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 68.8°
 1.01 s  door reaches its lower stop (0°) moving -87°/s
 1.01 s  door_panel first touches jamb
 1.02 s  door is at its smallest, -0.2°
 1.05 s  door_panel leaves jamb
 1.29 s  door reaches its lower stop (0°) again moving -4°/s
 1.38 s  door_panel touches jamb again

State every 0.25 s:
0.00 s: door at 68.8°, still; touching nothing
0.25 s: door at 62.1°, turning -50°/s; touching nothing
0.50 s: door at 45.5°, turning -80°/s; touching nothing
0.75 s: door at 23.6°, turning -92°/s; touching nothing
1.00 s: door at 1.0°, turning -87°/s; touching nothing
1.25 s: door at 0.6°, turning -2°/s; touching nothing
1.50 s: door at -0.0°, still; touching jamb
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching jamb
</history>
