MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 97.4028° as MuJoCo applies it; its geoms: door_panel, door_knob; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 1.35 s  door passes 0.05 m from wall_latch_side without touching it: nearest points (0.90, 0.00, 1.56) m and (0.95, 0.00, 1.56) m
 1.37 s  door reaches its lower stop (0°) moving -53°/s
 1.38 s  door_panel first touches door_stop
 1.39 s  door is at its smallest, -0.3°
 1.45 s  door_panel leaves door_stop
 1.91 s  door reaches its lower stop (0°) again moving -2°/s

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 74.5°, turning -43°/s; touching nothing
0.50 s: door at 60.4°, turning -67°/s; touching nothing
0.75 s: door at 42.3°, turning -75°/s; touching nothing
1.00 s: door at 23.7°, turning -72°/s; touching nothing
1.25 s: door at 7.1°, turning -60°/s; touching nothing
1.50 s: door at 0.2°, turning +4°/s; touching nothing
1.75 s: door at 0.7°, still; touching nothing
2.00 s: door at 0.2°, turning -3°/s; touching nothing
2.25 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
