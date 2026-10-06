Your expectations, checked against the run (1 of 1 hold):

- holds: door reaches its lower stop (at its lower stop (0°) at 1.35 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 97.4028° as MuJoCo applies it; its geoms: door_slab, door_knob; starts at 80.2°, still

What happened, in order:
 0.00 s  door is at its largest at the start, 80.2°
 1.33 s  door passes 0.02 m from frame_latch_post without touching it: nearest points (0.89, 0.00, 1.03) m and (0.91, 0.00, 1.03) m
 1.35 s  door reaches its lower stop (0°) moving -69°/s
 1.37 s  door is at its smallest, -0.5°
 1.78 s  door reaches its lower stop (0°) again moving -4°/s

State every 0.25 s:
0.00 s: door at 80.2°, still; touching nothing
0.25 s: door at 75.3°, turning -37°/s; touching nothing
0.50 s: door at 62.8°, turning -62°/s; touching nothing
0.75 s: door at 45.5°, turning -75°/s; touching nothing
1.00 s: door at 26.2°, turning -78°/s; touching nothing
1.25 s: door at 7.3°, turning -73°/s; touching nothing
1.50 s: door at 0.4°, turning +5°/s; touching nothing
1.75 s: door at 0.6°, turning -3°/s; touching nothing
2.00 s: door at -0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at -0.0°, still; touching nothing
</history>
