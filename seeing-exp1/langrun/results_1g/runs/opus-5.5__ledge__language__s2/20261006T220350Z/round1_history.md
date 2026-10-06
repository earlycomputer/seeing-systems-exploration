Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches table (first touch at 0.00 s)
- holds: ball touches bucket (first touch at 0.58 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.30, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table_top
 0.20 s  ball leaves table_top
 0.58 s  ball first touches bucket_base
 0.63 s  ball leaves bucket_base
 0.72 s  ball touches bucket_base again
 0.74 s  ball leaves bucket_base
 0.74 s  ball first touches bucket_far_wall
 0.78 s  ball touches bucket_base again
 0.79 s  ball leaves bucket_far_wall
 0.80 s  ball comes to rest at (1.31, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.30, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.68, 0.00, 0.77) m, moving 1.64 m/s (vx +1.55, vy -0.00, vz -0.53); touching nothing
0.50 s: ball at (1.07, 0.00, 0.33) m, moving 3.36 m/s (vx +1.55, vy -0.00, vz -2.99); touching nothing
0.75 s: ball at (1.31, 0.00, 0.05) m, moving 0.09 m/s (vx +0.05, vy +0.00, vz +0.07); touching bucket_far_wall
1.00 s: ball at (1.31, 0.00, 0.05) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.31, 0.00, 0.05) m, at rest; touching bucket_base
</history>
