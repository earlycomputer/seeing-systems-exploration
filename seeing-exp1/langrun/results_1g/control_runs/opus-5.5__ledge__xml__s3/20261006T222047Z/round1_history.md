MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.80, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table_top
 0.52 s  ball leaves table_top
 0.90 s  ball first touches bucket_bottom
 0.91 s  ball first touches floor
 0.93 s  ball leaves floor
 1.02 s  ball comes to rest at (0.63, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (-0.80, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (-0.41, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz -0.00); touching table_top
0.50 s: ball at (-0.03, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00); touching table_top
0.75 s: ball at (0.36, 0.00, 0.52) m, moving 2.76 m/s (vx +1.55, vy -0.00, vz -2.29); touching nothing
1.00 s: ball at (0.63, 0.00, 0.05) m, moving 0.11 m/s (vx +0.09, vy -0.00, vz +0.07); touching bucket_bottom
1.25 s: ball at (0.63, 0.00, 0.05) m, at rest; touching bucket_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.63, 0.00, 0.05) m, at rest; touching bucket_bottom
</history>
