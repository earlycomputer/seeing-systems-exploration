MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.20, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  ball first touches table_top
 0.26 s  ball leaves table_top
 0.65 s  ball first touches bucket_base
 0.71 s  ball leaves bucket_base
 0.76 s  ball touches bucket_base again
 0.77 s  ball first touches bucket_far_wall
 0.77 s  ball leaves bucket_base
 0.82 s  ball leaves bucket_far_wall
 0.87 s  ball touches bucket_base again
 5.34 s  ball comes to rest at (1.05, 0.00, 0.05) m
 5.50 s  ball first touches bucket_near_wall
 5.56 s  ball leaves bucket_near_wall

State every 0.25 s:
0.00 s: ball at (0.20, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.58, 0.00, 0.78) m, moving 1.53 m/s (vx +1.53, vy +0.00, vz -0.00); touching table_top
0.50 s: ball at (0.96, 0.00, 0.50) m, moving 2.79 m/s (vx +1.52, vy +0.00, vz -2.33); touching nothing
0.75 s: ball at (1.33, 0.00, 0.05) m, moving 1.44 m/s (vx +1.43, vy +0.00, vz -0.16); touching nothing
1.00 s: ball at (1.34, 0.00, 0.05) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching bucket_base
1.25 s: ball at (1.32, 0.00, 0.05) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching bucket_base
1.50 s: ball at (1.30, 0.00, 0.05) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching bucket_base
1.75 s: ball at (1.28, 0.00, 0.05) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching bucket_base
2.00 s: ball at (1.26, 0.00, 0.05) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching bucket_base
2.25 s: ball at (1.24, 0.00, 0.05) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching bucket_base
2.50 s: ball at (1.22, 0.00, 0.05) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching bucket_base
2.75 s: ball at (1.20, 0.00, 0.05) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching bucket_base
3.00 s: ball at (1.18, 0.00, 0.05) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching bucket_base
3.25 s: ball at (1.17, 0.00, 0.05) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching bucket_base
3.50 s: ball at (1.15, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
3.75 s: ball at (1.14, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.00 s: ball at (1.12, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.25 s: ball at (1.11, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.50 s: ball at (1.09, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.75 s: ball at (1.08, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching bucket_base
5.00 s: ball at (1.07, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching bucket_base
5.25 s: ball at (1.05, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching bucket_base
5.50 s: ball at (1.04, 0.00, 0.05) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.04, 0.00, 0.05) m, at rest; touching bucket_base
</history>
