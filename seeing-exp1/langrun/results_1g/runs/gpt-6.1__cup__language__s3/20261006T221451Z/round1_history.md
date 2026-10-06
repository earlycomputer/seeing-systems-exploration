Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (touching from the start)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.13, 0.00, 0.46) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp
 0.02 s  ball starts moving
 0.93 s  ball leaves ramp
 1.03 s  ball first touches cup_base
 1.05 s  ball leaves cup_base
 1.15 s  ball touches cup_base again
 1.16 s  ball leaves cup_base
 1.22 s  ball touches cup_base again
 1.23 s  ball leaves cup_base
 1.27 s  ball touches cup_base again
 1.28 s  ball leaves cup_base
 1.32 s  ball touches cup_base 3 more times between 1.32 s and 6.00 s, still touching at the end
 1.37 s  ball first touches cup_far_wall
 1.40 s  ball leaves cup_far_wall
 1.42 s  ball comes to rest at (1.60, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.13, 0.00, 0.46) m, at rest; touching ramp
0.25 s: ball at (0.19, 0.00, 0.43) m, moving 0.54 m/s (vx +0.51, vy +0.00, vz -0.17); touching ramp
0.50 s: ball at (0.38, 0.00, 0.37) m, moving 1.07 m/s (vx +1.02, vy +0.00, vz -0.33); touching ramp
0.75 s: ball at (0.70, 0.00, 0.27) m, moving 1.60 m/s (vx +1.52, vy +0.00, vz -0.51); touching nothing
1.00 s: ball at (1.14, 0.00, 0.10) m, moving 2.28 m/s (vx +1.89, vy -0.00, vz -1.28); touching nothing
1.25 s: ball at (1.49, 0.00, 0.06) m, moving 1.08 m/s (vx +1.08, vy +0.00, vz -0.01); touching nothing
1.50 s: ball at (1.60, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.60, 0.00, 0.05) m, at rest; touching cup_base
</history>
