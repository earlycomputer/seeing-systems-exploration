Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (first touch at 0.00 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.13, 0.00, 0.71) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp
 0.02 s  ball starts moving
 1.03 s  ball leaves ramp
 1.21 s  ball first touches cup_base
 1.23 s  ball leaves cup_base
 1.28 s  ball is at the top of its flight, at (1.66, 0.00, 0.07) m
 1.34 s  ball touches cup_base again
 1.35 s  ball leaves cup_base
 1.35 s  ball first touches cup_far_wall
 1.38 s  ball leaves cup_far_wall
 1.38 s  ball touches cup_base again
 1.39 s  ball comes to rest at (1.72, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.13, 0.00, 0.71) m, at rest; touching nothing
0.25 s: ball at (0.19, 0.00, 0.69) m, moving 0.54 m/s (vx +0.52, vy -0.00, vz -0.17); touching ramp
0.50 s: ball at (0.39, 0.00, 0.62) m, moving 1.08 m/s (vx +1.02, vy +0.00, vz -0.35); touching ramp
0.75 s: ball at (0.70, 0.00, 0.51) m, moving 1.62 m/s (vx +1.53, vy +0.00, vz -0.55); touching nothing
1.00 s: ball at (1.15, 0.00, 0.35) m, moving 2.16 m/s (vx +2.04, vy +0.00, vz -0.70); touching nothing
1.25 s: ball at (1.63, 0.00, 0.06) m, moving 0.99 m/s (vx +0.94, vy -0.00, vz +0.32); touching nothing
1.50 s: ball at (1.72, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.72, 0.00, 0.05) m, at rest; touching cup_base
</history>
