MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.69 m/s (vx +2.67, vy +0.00, vz +9.32)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.95 s  ball is at the top of its flight, at (2.53, 0.00, 4.54) m
 1.48 s  ball passes 0.08 m from hoop (hoop.rim_07) without touching it: nearest points (3.85, 0.02, 3.10) m and (3.78, 0.03, 3.05) m
 1.87 s  ball first touches hoop_support.support_pole
 1.90 s  ball leaves hoop_support.support_pole
 1.90 s  ball first touches hoop_support.support_base
 1.93 s  ball leaves hoop_support.support_base
 2.08 s  ball is at the top of its flight, at (4.46, 0.00, 0.28) m
 2.26 s  ball touches floor again
 2.29 s  ball leaves floor
 2.36 s  ball touches floor again
 6.00 s  ball is still moving at the end, 3.21 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.69 m/s (vx +2.67, vy +0.00, vz +9.32); touching floor
0.25 s: ball at (0.66, 0.00, 2.13) m, moving 7.37 m/s (vx +2.67, vy +0.00, vz +6.87); touching nothing
0.50 s: ball at (1.33, 0.00, 3.54) m, moving 5.16 m/s (vx +2.67, vy +0.00, vz +4.42); touching nothing
0.75 s: ball at (1.99, 0.00, 4.34) m, moving 3.31 m/s (vx +2.67, vy +0.00, vz +1.96); touching nothing
1.00 s: ball at (2.66, 0.00, 4.53) m, moving 2.71 m/s (vx +2.67, vy +0.00, vz -0.49); touching nothing
1.25 s: ball at (3.33, 0.00, 4.10) m, moving 3.97 m/s (vx +2.67, vy +0.00, vz -2.94); touching nothing
1.50 s: ball at (3.99, 0.00, 3.06) m, moving 6.02 m/s (vx +2.67, vy +0.00, vz -5.39); touching nothing
1.75 s: ball at (4.66, 0.00, 1.41) m, moving 8.29 m/s (vx +2.67, vy +0.00, vz -7.85); touching nothing
2.00 s: ball at (4.70, 0.00, 0.25) m, moving 3.09 m/s (vx -2.99, vy +0.00, vz +0.78); touching nothing
2.25 s: ball at (3.95, 0.00, 0.14) m, moving 3.43 m/s (vx -2.99, vy +0.00, vz -1.68); touching nothing
2.50 s: ball at (3.15, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor
2.75 s: ball at (2.35, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
3.00 s: ball at (1.55, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
3.25 s: ball at (0.75, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
3.50 s: ball at (-0.06, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor
3.75 s: ball at (-0.86, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
4.00 s: ball at (-1.66, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
4.25 s: ball at (-2.46, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
4.50 s: ball at (-3.27, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor
4.75 s: ball at (-4.07, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
5.00 s: ball at (-4.87, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
5.25 s: ball at (-5.67, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor
5.50 s: ball at (-6.48, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
5.75 s: ball at (-7.28, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz -0.00); touching floor
6.00 s: ball at (-8.08, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- ball at (-8.08, 0.00, 0.12) m, moving 3.21 m/s (vx -3.21, vy +0.00, vz +0.00); touching floor
</history>
