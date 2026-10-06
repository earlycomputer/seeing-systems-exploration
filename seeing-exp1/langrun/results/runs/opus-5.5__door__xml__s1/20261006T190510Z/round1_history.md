MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), no range limit; its geoms: door_panel, door_handle; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 1.11 s  door_panel first touches frame.jamb_stop
 1.13 s  door is at its smallest, -0.4°
 1.19 s  door_panel leaves frame.jamb_stop
 2.88 s  door_panel touches frame.jamb_stop again
 2.96 s  door_panel leaves frame.jamb_stop
 3.61 s  door_panel touches frame.jamb_stop again

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 72.2°, turning -59°/s; touching nothing
0.50 s: door at 53.0°, turning -89°/s; touching nothing
0.75 s: door at 29.8°, turning -93°/s; touching nothing
1.00 s: door at 8.0°, turning -79°/s; touching nothing
1.25 s: door at 0.5°, turning +7°/s; touching nothing
1.50 s: door at 1.8°, turning +4°/s; touching nothing
1.75 s: door at 2.4°, still; touching nothing
2.00 s: door at 2.3°, turning -1°/s; touching nothing
2.25 s: door at 1.8°, turning -3°/s; touching nothing
2.50 s: door at 1.1°, turning -3°/s; touching nothing
2.75 s: door at 0.3°, turning -3°/s; touching nothing
3.00 s: door at 0.0°, still; touching nothing
(the same through 3.50 s)
3.75 s: door at -0.0°, still; touching frame.jamb_stop
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching frame.jamb_stop
</history>
