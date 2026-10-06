MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 85.9437° as MuJoCo applies it; its geoms: door_panel, door.handle_lower_mount, door.handle_upper_mount, door.handle_grip; starts at 68.8°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 68.8°
 1.75 s  door reaches its lower stop (0°) moving -2°/s
 6.00 s  door is at its smallest, 0.0°

State every 0.25 s:
0.00 s: door at 68.8°, still; touching nothing
0.25 s: door at 49.2°, turning -105°/s; touching nothing
0.50 s: door at 26.3°, turning -73°/s; touching nothing
0.75 s: door at 12.7°, turning -39°/s; touching nothing
1.00 s: door at 5.8°, turning -19°/s; touching nothing
1.25 s: door at 2.6°, turning -8°/s; touching nothing
1.50 s: door at 1.1°, turning -4°/s; touching nothing
1.75 s: door at 0.5°, turning -2°/s; touching nothing
2.00 s: door at 0.2°, still; touching nothing
2.25 s: door at 0.1°, still; touching nothing
2.50 s: door at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at 0.0°, still; touching nothing
</history>
