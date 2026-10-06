Your expectations, checked against the run (2 of 2 hold):

- holds: door reaches its lower stop (at its lower stop (0°) at 0.97 s)
- holds: door touches jamb (first touch at 0.97 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 97.4028° as MuJoCo applies it; its geoms: door_panel, door_knob; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 0.97 s  door reaches its lower stop (0°) moving -100°/s
 0.97 s  door_panel first touches jamb
 0.98 s  door is at its smallest, -0.3°
 1.01 s  door_panel leaves jamb
 1.01 s  door passes 0.03 m from wall_right without touching it: nearest points (0.90, -0.02, 1.06) m and (0.93, -0.02, 1.06) m
 1.65 s  door reaches its lower stop (0°) again moving -6°/s
 1.72 s  door_panel touches jamb again

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 71.6°, turning -64°/s; touching nothing
0.50 s: door at 50.3°, turning -101°/s; touching nothing
0.75 s: door at 23.3°, turning -110°/s; touching nothing
1.00 s: door at -0.1°, turning +10°/s; touching jamb
1.25 s: door at 1.5°, turning +2°/s; touching nothing
1.50 s: door at 1.3°, turning -4°/s; touching nothing
1.75 s: door at -0.0°, still; touching jamb
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching jamb
</history>
