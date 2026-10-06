Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches table (touching from the start)
- holds: ball touches bucket (first touch at 0.80 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.83) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball starts touching table_top
 0.40 s  ball leaves table_top
 0.80 s  ball first touches bucket_base
 0.83 s  ball leaves bucket_base
 0.90 s  ball touches bucket_base again
 1.08 s  ball first touches bucket_far_wall
 1.10 s  ball comes to rest at (1.36, 0.00, 0.05) m
 1.12 s  ball leaves bucket_far_wall

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.83) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching table_top
0.25 s: ball at (0.37, 0.00, 0.83) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz -0.00); touching table_top
0.50 s: ball at (0.75, 0.00, 0.78) m, moving 1.78 m/s (vx +1.50, vy +0.00, vz -0.96); touching nothing
0.75 s: ball at (1.12, 0.00, 0.24) m, moving 3.73 m/s (vx +1.50, vy +0.00, vz -3.41); touching nothing
1.00 s: ball at (1.33, 0.00, 0.05) m, moving 0.47 m/s (vx +0.47, vy -0.00, vz -0.04); touching nothing
1.25 s: ball at (1.36, 0.00, 0.05) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.36, 0.00, 0.05) m, at rest; touching bucket_base
</history>
