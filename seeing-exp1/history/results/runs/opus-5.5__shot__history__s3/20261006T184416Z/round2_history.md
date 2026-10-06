MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.22 m/s (vx +3.01, vy +0.00, vz +8.72)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.89 s  ball is at the top of its flight, at (2.68, 0.00, 3.99) m
 1.30 s  ball passes 0.05 m from hoop (hoop.rim_07) without touching it: nearest points (3.82, 0.02, 3.08) m and (3.78, 0.03, 3.05) m
 1.66 s  ball first touches hoop_support.support_pole
 1.68 s  ball leaves hoop_support.support_pole
 1.83 s  ball first touches hoop_support.support_base
 1.86 s  ball leaves hoop_support.support_base
 1.99 s  ball is at the top of its flight, at (4.53, 0.00, 0.25) m
 2.16 s  ball touches floor again
 2.19 s  ball leaves floor
 2.25 s  ball touches floor again
 6.00 s  ball is still moving at the end, 2.28 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.22 m/s (vx +3.01, vy +0.00, vz +8.72); touching floor
0.25 s: ball at (0.75, 0.00, 1.98) m, moving 6.95 m/s (vx +3.01, vy +0.00, vz +6.27); touching nothing
0.50 s: ball at (1.50, 0.00, 3.24) m, moving 4.86 m/s (vx +3.01, vy +0.00, vz +3.81); touching nothing
0.75 s: ball at (2.25, 0.00, 3.89) m, moving 3.31 m/s (vx +3.01, vy +0.00, vz +1.36); touching nothing
1.00 s: ball at (3.01, 0.00, 3.93) m, moving 3.20 m/s (vx +3.01, vy +0.00, vz -1.09); touching nothing
1.25 s: ball at (3.76, 0.00, 3.35) m, moving 4.65 m/s (vx +3.01, vy +0.00, vz -3.54); touching nothing
1.50 s: ball at (4.51, 0.00, 2.16) m, moving 6.71 m/s (vx +3.01, vy +0.00, vz -6.00); touching nothing
1.75 s: ball at (4.93, 0.00, 0.63) m, moving 5.46 m/s (vx -0.77, vy +0.00, vz -5.41); touching nothing
2.00 s: ball at (4.51, 0.00, 0.25) m, moving 2.15 m/s (vx -2.14, vy +0.00, vz -0.10); touching nothing
2.25 s: ball at (3.96, 0.00, 0.12) m, moving 2.27 m/s (vx -2.27, vy +0.00, vz -0.07); touching floor
2.50 s: ball at (3.39, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
2.75 s: ball at (2.82, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
3.00 s: ball at (2.25, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
3.25 s: ball at (1.68, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
3.50 s: ball at (1.11, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
3.75 s: ball at (0.54, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
4.00 s: ball at (-0.03, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
4.25 s: ball at (-0.60, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
4.50 s: ball at (-1.17, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
4.75 s: ball at (-1.74, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
5.00 s: ball at (-2.31, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
5.25 s: ball at (-2.88, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
5.50 s: ball at (-3.45, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
5.75 s: ball at (-4.02, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz -0.00); touching floor
6.00 s: ball at (-4.59, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- ball at (-4.59, 0.00, 0.12) m, moving 2.28 m/s (vx -2.28, vy +0.00, vz +0.00); touching floor
</history>
