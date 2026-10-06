Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches ramp (touching from the start)
- holds: ball touches cup (first touch at 1.74 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.10, 0.00, 0.29) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_deck
 0.07 s  ball starts moving
 1.58 s  ball leaves ramp_deck
 1.74 s  ball first touches cup_base
 1.76 s  ball leaves cup_base
 1.81 s  ball touches cup_base again
 1.91 s  ball comes to rest at (1.24, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.10, 0.00, 0.29) m, at rest; touching ramp_deck
0.25 s: ball at (0.13, 0.00, 0.29) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.02); touching ramp_deck
0.50 s: ball at (0.20, 0.00, 0.28) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz -0.04); touching ramp_deck
0.75 s: ball at (0.31, 0.00, 0.27) m, moving 0.55 m/s (vx +0.55, vy +0.00, vz -0.06); touching ramp_deck
1.00 s: ball at (0.47, 0.00, 0.25) m, moving 0.73 m/s (vx +0.72, vy +0.00, vz -0.08); touching ramp_deck
1.25 s: ball at (0.67, 0.00, 0.23) m, moving 0.90 m/s (vx +0.89, vy +0.00, vz -0.10); touching ramp_deck
1.50 s: ball at (0.92, 0.00, 0.20) m, moving 1.07 m/s (vx +1.06, vy +0.00, vz -0.12); touching ramp_deck
1.75 s: ball at (1.19, 0.00, 0.05) m, moving 0.56 m/s (vx +0.50, vy +0.00, vz +0.24); touching cup_base
2.00 s: ball at (1.24, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.24, 0.00, 0.05) m, at rest; touching cup_base
</history>
