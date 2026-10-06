Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches table_top (first touch at 0.00 s)
- holds: ball touches bucket_bottom (first touch at 0.63 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.40, 0.00, 0.78) m, moving 1.67 m/s (vx +1.67, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table_top
 0.24 s  ball leaves table_top
 0.63 s  ball first touches bucket_bottom
 0.64 s  ball first touches floor
 0.66 s  ball leaves floor
 0.68 s  ball first touches bucket_wall0
 0.70 s  ball leaves bucket_bottom
 0.75 s  ball leaves bucket_wall0
 0.81 s  ball touches bucket_bottom again
 0.86 s  ball comes to rest at (0.68, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (-0.40, 0.00, 0.78) m, moving 1.67 m/s (vx +1.67, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.01, 0.00, 0.78) m, moving 1.67 m/s (vx +1.67, vy +0.00, vz -0.08); touching nothing
0.50 s: ball at (0.43, 0.00, 0.46) m, moving 3.03 m/s (vx +1.67, vy +0.00, vz -2.53); touching nothing
0.75 s: ball at (0.69, 0.00, 0.06) m, moving 0.16 m/s (vx -0.15, vy +0.00, vz +0.04); touching nothing
1.00 s: ball at (0.68, 0.00, 0.05) m, at rest; touching bucket_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.68, 0.00, 0.05) m, at rest; touching bucket_bottom
</history>
