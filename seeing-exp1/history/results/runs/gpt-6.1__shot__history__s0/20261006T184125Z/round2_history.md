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
 1.89 s  ball leaves hoop_support.support_pole
 1.91 s  ball first touches hoop_support.support_base
 1.94 s  ball leaves hoop_support.support_base
 2.07 s  ball is at the top of its flight, at (4.58, 0.00, 0.26) m
 2.24 s  ball touches floor again
 2.27 s  ball leaves floor
 2.34 s  ball touches floor again
 6.00 s  ball is still moving at the end, 2.55 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.69 m/s (vx +2.67, vy +0.00, vz +9.32); touching floor
0.25 s: ball at (0.66, 0.00, 2.13) m, moving 7.37 m/s (vx +2.67, vy +0.00, vz +6.87); touching nothing
0.50 s: ball at (1.33, 0.00, 3.54) m, moving 5.16 m/s (vx +2.67, vy +0.00, vz +4.42); touching nothing
0.75 s: ball at (1.99, 0.00, 4.34) m, moving 3.31 m/s (vx +2.67, vy -0.00, vz +1.96); touching nothing
1.00 s: ball at (2.66, 0.00, 4.53) m, moving 2.71 m/s (vx +2.67, vy +0.00, vz -0.49); touching nothing
1.25 s: ball at (3.33, 0.00, 4.10) m, moving 3.97 m/s (vx +2.67, vy +0.00, vz -2.94); touching nothing
1.50 s: ball at (3.99, 0.00, 3.06) m, moving 6.02 m/s (vx +2.67, vy +0.00, vz -5.39); touching nothing
1.75 s: ball at (4.66, 0.00, 1.41) m, moving 8.29 m/s (vx +2.67, vy +0.00, vz -7.85); touching nothing
2.00 s: ball at (4.76, 0.00, 0.23) m, moving 2.49 m/s (vx -2.39, vy +0.00, vz +0.70); touching nothing
2.25 s: ball at (4.16, 0.00, 0.11) m, moving 2.49 m/s (vx -2.49, vy +0.00, vz -0.07); touching floor
2.50 s: ball at (3.52, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
2.75 s: ball at (2.88, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
3.00 s: ball at (2.25, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
3.25 s: ball at (1.61, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
3.50 s: ball at (0.97, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
3.75 s: ball at (0.33, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
4.00 s: ball at (-0.31, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
4.25 s: ball at (-0.95, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
4.50 s: ball at (-1.59, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
4.75 s: ball at (-2.23, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
5.00 s: ball at (-2.86, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
5.25 s: ball at (-3.50, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
5.50 s: ball at (-4.14, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
5.75 s: ball at (-4.78, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz +0.00); touching floor
6.00 s: ball at (-5.42, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor

At the end (6.00 s):
- ball at (-5.42, 0.00, 0.12) m, moving 2.55 m/s (vx -2.55, vy +0.00, vz -0.00); touching floor
</history>
