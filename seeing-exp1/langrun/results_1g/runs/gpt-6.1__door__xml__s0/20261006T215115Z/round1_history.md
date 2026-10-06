Your expectations, checked against the run (1 of 1 hold):

- holds: door reaches its lower stop (at its lower stop (0°) at 0.80 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 85.9437° as MuJoCo applies it; its geoms: door_panel, door_handle, door_hinge_upper, door_hinge_lower; starts at 68.8°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 68.8°
 0.80 s  door reaches its lower stop (0°) moving -43°/s
 0.81 s  door is at its smallest, -0.1°

State every 0.25 s:
0.00 s: door at 68.8°, still; touching nothing
0.25 s: door at 49.2°, turning -118°/s; touching nothing
0.50 s: door at 20.9°, turning -98°/s; touching nothing
0.75 s: door at 2.5°, turning -50°/s; touching nothing
1.00 s: door at 0.0°, turning -5°/s; touching nothing
1.25 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
