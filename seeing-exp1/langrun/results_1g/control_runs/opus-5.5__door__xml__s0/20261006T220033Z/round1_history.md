MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 91.6732° as MuJoCo applies it; its geoms: door_panel, door_knob; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 2.30 s  door reaches its lower stop (0°) moving -6°/s
 2.40 s  door is at its smallest, -0.0°

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 74.1°, turning -43°/s; touching nothing
0.50 s: door at 61.1°, turning -58°/s; touching nothing
0.75 s: door at 46.4°, turning -58°/s; touching nothing
1.00 s: door at 32.8°, turning -50°/s; touching nothing
1.25 s: door at 21.6°, turning -39°/s; touching nothing
1.50 s: door at 13.1°, turning -29°/s; touching nothing
1.75 s: door at 7.1°, turning -20°/s; touching nothing
2.00 s: door at 3.2°, turning -12°/s; touching nothing
2.25 s: door at 0.8°, turning -7°/s; touching nothing
2.50 s: door at 0.0°, still; touching nothing
2.75 s: door at 0.1°, still; touching nothing
(the same through 4.00 s)
4.25 s: door at 0.0°, still; touching nothing
(the same through 5.25 s)
5.50 s: door at -0.0°, still; touching nothing
5.75 s: door at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at 0.0°, still; touching nothing
</history>
