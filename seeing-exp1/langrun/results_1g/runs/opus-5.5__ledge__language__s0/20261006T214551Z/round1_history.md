Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches table (first touch at 0.00 s)
- holds: ball touches bucket (first touch at 0.51 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.20, 0.00, 0.78) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table_top
 0.12 s  ball leaves table_top
 0.13 s  ball is at the top of its flight, at (0.40, 0.00, 0.78) m
 0.51 s  ball first touches bucket_base
 0.54 s  ball leaves bucket_base
 0.63 s  ball touches bucket_base again
 0.65 s  ball leaves bucket_base
 0.68 s  ball touches bucket_base again
 0.84 s  ball first touches bucket_far_wall
 0.85 s  ball comes to rest at (1.21, 0.00, 0.05) m
 0.87 s  ball leaves bucket_far_wall

State every 0.25 s:
0.00 s: ball at (0.20, 0.00, 0.78) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.59, 0.00, 0.71) m, moving 1.99 m/s (vx +1.58, vy +0.00, vz -1.21); touching nothing
0.50 s: ball at (0.99, 0.00, 0.10) m, moving 3.99 m/s (vx +1.58, vy +0.00, vz -3.67); touching nothing
0.75 s: ball at (1.18, 0.00, 0.05) m, moving 0.47 m/s (vx +0.47, vy -0.00, vz +0.06); touching bucket_base
1.00 s: ball at (1.21, 0.00, 0.05) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.21, 0.00, 0.05) m, at rest; touching bucket_base
</history>
