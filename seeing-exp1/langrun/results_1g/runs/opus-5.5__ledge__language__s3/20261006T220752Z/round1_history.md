Your expectations, checked against the run (1 of 2 hold):

- holds: ball touches table (first touch at 0.00 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball is still moving at the end (0.05 m/s), inside bucket)

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
 0.62 s  ball leaves bucket_base
 0.66 s  ball touches bucket_base again
 0.69 s  ball leaves bucket_base
 0.69 s  ball first touches bucket_far_wall
 0.72 s  ball leaves bucket_far_wall
 0.79 s  ball touches bucket_base again
 6.00 s  ball is still moving at the end, 0.05 m/s

State every 0.25 s:
0.00 s: ball at (0.30, 0.00, 0.78) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.00); touching nothing
0.25 s: ball at (0.68, 0.00, 0.77) m, moving 1.64 m/s (vx +1.55, vy +0.00, vz -0.54); touching nothing
0.50 s: ball at (1.07, 0.00, 0.33) m, moving 3.37 m/s (vx +1.55, vy +0.00, vz -3.00); touching nothing
0.75 s: ball at (1.35, 0.00, 0.06) m, moving 0.25 m/s (vx -0.23, vy +0.00, vz -0.10); touching nothing
1.00 s: ball at (1.33, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
1.25 s: ball at (1.32, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
1.50 s: ball at (1.30, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
1.75 s: ball at (1.29, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
2.00 s: ball at (1.28, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
2.25 s: ball at (1.26, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
2.50 s: ball at (1.25, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
2.75 s: ball at (1.23, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
3.00 s: ball at (1.22, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
3.25 s: ball at (1.21, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
3.50 s: ball at (1.19, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
3.75 s: ball at (1.18, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.00 s: ball at (1.16, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.25 s: ball at (1.15, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.50 s: ball at (1.14, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching bucket_base
4.75 s: ball at (1.12, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching bucket_base
5.00 s: ball at (1.11, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base
5.25 s: ball at (1.10, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base
5.50 s: ball at (1.08, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base
5.75 s: ball at (1.07, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base
6.00 s: ball at (1.05, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base

At the end (6.00 s):
- ball at (1.05, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching bucket_base
</history>
