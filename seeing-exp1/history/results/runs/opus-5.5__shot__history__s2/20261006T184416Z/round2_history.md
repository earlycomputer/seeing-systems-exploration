MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.48 m/s (vx +2.80, vy +0.00, vz +9.06)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.92 s  ball is at the top of its flight, at (2.58, 0.00, 4.29) m
 1.41 s  ball passes 0.07 m from hoop (hoop.rim_07) without touching it: nearest points (3.84, 0.02, 3.08) m and (3.78, 0.03, 3.05) m
 1.78 s  ball first touches hoop_support.support_pole
 1.81 s  ball leaves hoop_support.support_pole
 1.87 s  ball first touches hoop_support.support_base
 1.90 s  ball leaves hoop_support.support_base
 2.04 s  ball is at the top of its flight, at (4.54, 0.00, 0.27) m
 2.22 s  ball touches floor again
 2.25 s  ball leaves floor
 2.32 s  ball touches floor again
 6.00 s  ball is still moving at the end, 2.50 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.48 m/s (vx +2.80, vy +0.00, vz +9.06); touching floor
0.25 s: ball at (0.69, 0.00, 2.06) m, moving 7.17 m/s (vx +2.80, vy +0.00, vz +6.60); touching nothing
0.50 s: ball at (1.39, 0.00, 3.41) m, moving 5.01 m/s (vx +2.80, vy +0.00, vz +4.15); touching nothing
0.75 s: ball at (2.09, 0.00, 4.14) m, moving 3.28 m/s (vx +2.80, vy +0.00, vz +1.70); touching nothing
1.00 s: ball at (2.79, 0.00, 4.26) m, moving 2.90 m/s (vx +2.80, vy +0.00, vz -0.75); touching nothing
1.25 s: ball at (3.49, 0.00, 3.77) m, moving 4.26 m/s (vx +2.80, vy +0.00, vz -3.21); touching nothing
1.50 s: ball at (4.19, 0.00, 2.67) m, moving 6.31 m/s (vx +2.80, vy +0.00, vz -5.66); touching nothing
1.75 s: ball at (4.89, 0.00, 0.95) m, moving 8.58 m/s (vx +2.80, vy +0.00, vz -8.11); touching nothing
2.00 s: ball at (4.64, 0.00, 0.26) m, moving 2.37 m/s (vx -2.33, vy +0.00, vz +0.42); touching nothing
2.25 s: ball at (4.06, 0.00, 0.12) m, moving 2.49 m/s (vx -2.47, vy +0.00, vz +0.31); touching nothing
2.50 s: ball at (3.43, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
2.75 s: ball at (2.81, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz +0.00); touching floor
3.00 s: ball at (2.19, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
3.25 s: ball at (1.56, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
3.50 s: ball at (0.94, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz +0.00); touching floor
3.75 s: ball at (0.31, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
4.00 s: ball at (-0.31, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
4.25 s: ball at (-0.93, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz +0.00); touching floor
4.50 s: ball at (-1.56, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
4.75 s: ball at (-2.18, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
5.00 s: ball at (-2.81, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz +0.00); touching floor
5.25 s: ball at (-3.43, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
5.50 s: ball at (-4.05, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
5.75 s: ball at (-4.68, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz +0.00); touching floor
6.00 s: ball at (-5.30, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor

At the end (6.00 s):
- ball at (-5.30, 0.00, 0.12) m, moving 2.50 m/s (vx -2.50, vy +0.00, vz -0.00); touching floor
</history>
