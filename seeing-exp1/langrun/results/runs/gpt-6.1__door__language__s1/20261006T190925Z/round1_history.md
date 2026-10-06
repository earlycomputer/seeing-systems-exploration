MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 100° as MuJoCo applies it; its geoms: door; starts at 80.0°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.0°
 1.44 s  door reaches its lower stop (0°) moving -12°/s
 1.50 s  door is at its smallest, -0.1°

State every 0.25 s:
0.00 s: door at 80.0°, still; touching nothing
0.25 s: door at 62.1°, turning -102°/s; touching nothing
0.50 s: door at 37.9°, turning -85°/s; touching nothing
0.75 s: door at 20.6°, turning -55°/s; touching nothing
1.00 s: door at 9.8°, turning -33°/s; touching nothing
1.25 s: door at 3.5°, turning -19°/s; touching nothing
1.50 s: door at -0.1°, still; touching nothing
1.75 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
