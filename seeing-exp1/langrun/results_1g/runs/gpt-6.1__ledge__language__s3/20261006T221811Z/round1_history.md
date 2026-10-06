Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches table (touching from the start)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.30, 0.00, 0.84) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball starts touching table_top
 0.20 s  ball leaves table_top
 0.60 s  ball first touches bucket_base
 0.64 s  ball leaves bucket_base
 0.71 s  ball touches bucket_base again
 0.73 s  ball leaves bucket_base
 0.74 s  ball first touches bucket_far_wall
 0.77 s  ball leaves bucket_far_wall
 0.82 s  ball touches bucket_base again
 0.85 s  ball comes to rest at (1.36, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.30, 0.00, 0.84) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching table_top
0.25 s: ball at (0.67, 0.00, 0.83) m, moving 1.55 m/s (vx +1.48, vy -0.00, vz -0.46); touching nothing
0.50 s: ball at (1.04, 0.00, 0.41) m, moving 3.27 m/s (vx +1.48, vy -0.00, vz -2.92); touching nothing
0.75 s: ball at (1.37, 0.00, 0.06) m, moving 0.31 m/s (vx -0.16, vy -0.00, vz +0.27); touching bucket_far_wall
1.00 s: ball at (1.35, 0.00, 0.06) m, at rest; touching bucket_base
(the same through 1.50 s)
1.75 s: ball at (1.34, 0.00, 0.06) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.34, 0.00, 0.06) m, at rest; touching bucket_base
</history>
