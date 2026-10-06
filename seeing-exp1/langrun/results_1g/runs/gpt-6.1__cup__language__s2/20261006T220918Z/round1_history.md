Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (touching from the start)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.16, 0.00, 0.59) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp
 0.02 s  ball starts moving
 1.05 s  ball leaves ramp
 1.18 s  ball first touches cup_base
 1.20 s  ball leaves cup_base
 1.25 s  ball is at the top of its flight, at (1.63, 0.00, 0.07) m
 1.31 s  ball touches cup_base again
 1.32 s  ball leaves cup_base
 1.39 s  ball first touches cup_far_wall
 1.39 s  ball touches cup_base again
 1.42 s  ball leaves cup_far_wall
 1.45 s  ball comes to rest at (1.80, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.16, 0.00, 0.59) m, at rest; touching ramp
0.25 s: ball at (0.22, 0.00, 0.57) m, moving 0.53 m/s (vx +0.50, vy -0.00, vz -0.17); touching ramp
0.50 s: ball at (0.41, 0.00, 0.51) m, moving 1.05 m/s (vx +1.00, vy +0.00, vz -0.33); touching ramp
0.75 s: ball at (0.72, 0.00, 0.41) m, moving 1.58 m/s (vx +1.49, vy +0.00, vz -0.50); touching nothing
1.00 s: ball at (1.15, 0.00, 0.26) m, moving 2.10 m/s (vx +1.99, vy +0.00, vz -0.66); touching ramp
1.25 s: ball at (1.63, 0.00, 0.07) m, moving 1.43 m/s (vx +1.43, vy +0.00, vz +0.04); touching nothing
1.50 s: ball at (1.80, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.80, 0.00, 0.05) m, at rest; touching cup_base
</history>
