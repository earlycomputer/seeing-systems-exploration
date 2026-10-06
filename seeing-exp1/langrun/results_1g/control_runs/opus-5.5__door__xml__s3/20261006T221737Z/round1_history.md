MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range -17.1887° to 97.4028° as MuJoCo applies it; its geoms: door_panel, door_handle; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 2.01 s  door passes 0.03 m from latch_post without touching it: nearest points (0.92, 0.00, 1.55) m and (0.95, 0.00, 1.55) m
 2.07 s  door_panel first touches door_stop
 2.09 s  door is at its smallest, -0.1°
 2.15 s  door_panel leaves door_stop
 5.05 s  door_panel touches door_stop again
 5.13 s  door_panel leaves door_stop

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 76.1°, turning -30°/s; touching nothing
0.50 s: door at 66.1°, turning -47°/s; touching nothing
0.75 s: door at 53.2°, turning -54°/s; touching nothing
1.00 s: door at 39.8°, turning -53°/s; touching nothing
1.25 s: door at 27.2°, turning -47°/s; touching nothing
1.50 s: door at 16.4°, turning -39°/s; touching nothing
1.75 s: door at 7.8°, turning -30°/s; touching nothing
2.00 s: door at 1.4°, turning -21°/s; touching nothing
2.25 s: door at 0.2°, turning +2°/s; touching nothing
2.50 s: door at 0.6°, turning +1°/s; touching nothing
2.75 s: door at 0.8°, still; touching nothing
(the same through 3.25 s)
3.50 s: door at 0.7°, still; touching nothing
3.75 s: door at 0.5°, still; touching nothing
4.00 s: door at 0.4°, still; touching nothing
4.25 s: door at 0.3°, still; touching nothing
4.50 s: door at 0.2°, still; touching nothing
4.75 s: door at 0.1°, still; touching nothing
5.00 s: door at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at 0.0°, still; touching nothing
</history>
