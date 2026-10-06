MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.20, 0.00, 0.78) m, moving 1.56 m/s (vx +1.56, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table
 0.19 s  ball leaves table
 0.58 s  ball first touches bucket_base
 0.61 s  ball leaves bucket_base
 0.70 s  ball touches bucket_base again
 0.72 s  ball leaves bucket_base
 0.75 s  ball touches bucket_base again
 0.83 s  ball first touches bucket_far_wall
 0.86 s  ball comes to rest at (1.26, 0.00, 0.05) m
 0.86 s  ball leaves bucket_far_wall

State every 0.25 s:
0.00 s: ball at (0.20, 0.00, 0.78) m, moving 1.56 m/s (vx +1.56, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.59, 0.00, 0.77) m, moving 1.65 m/s (vx +1.55, vy -0.00, vz -0.55); touching nothing
0.50 s: ball at (0.97, 0.00, 0.32) m, moving 3.38 m/s (vx +1.55, vy -0.00, vz -3.00); touching nothing
0.75 s: ball at (1.22, 0.00, 0.05) m, moving 0.56 m/s (vx +0.56, vy -0.00, vz +0.03); touching bucket_base
1.00 s: ball at (1.26, 0.00, 0.05) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.26, 0.00, 0.05) m, at rest; touching bucket_base
</history>
