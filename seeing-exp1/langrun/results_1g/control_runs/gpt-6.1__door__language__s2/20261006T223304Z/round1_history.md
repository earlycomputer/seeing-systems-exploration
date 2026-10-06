MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 100° as MuJoCo applies it; its geoms: door; starts at 80.0°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.0°
 0.91 s  door reaches its lower stop (0°) moving -23°/s
 0.95 s  door is at its smallest, -0.1°

State every 0.25 s:
0.00 s: door at 80.0°, still; touching nothing
0.25 s: door at 51.7°, turning -147°/s; touching nothing
0.50 s: door at 21.3°, turning -91°/s; touching nothing
0.75 s: door at 5.5°, turning -41°/s; touching nothing
1.00 s: door at -0.0°, turning +2°/s; touching nothing
1.25 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
