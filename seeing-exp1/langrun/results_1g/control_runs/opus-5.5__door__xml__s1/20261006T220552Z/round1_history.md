MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 97.4028° as MuJoCo applies it; its geoms: door_panel, door_handle; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 0.91 s  door passes 0.01 m from latch_post without touching it: nearest points (0.90, 0.00, 1.50) m and (0.91, 0.00, 1.50) m
 0.92 s  door reaches its lower stop (0°) moving -108°/s
 0.94 s  door is at its smallest, -0.7°
 0.96 s  door reaches its lower stop (0°) again moving +14°/s
 0.98 s  door passes -0.00 m from door_stop without touching it: nearest points (0.90, -0.02, 1.06) m and (0.90, -0.02, 1.06) m
 1.38 s  door reaches its lower stop (0°) again moving -6°/s

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 71.0°, turning -69°/s; touching nothing
0.50 s: door at 48.2°, turning -108°/s; touching nothing
0.75 s: door at 19.6°, turning -117°/s; touching nothing
1.00 s: door at -0.0°, turning +11°/s; touching nothing
1.25 s: door at 1.0°, turning -2°/s; touching nothing
1.50 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
