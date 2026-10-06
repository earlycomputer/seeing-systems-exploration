Your expectations, checked against the run (1 of 1 hold):

- holds: ball drops through hoop (through at 1.33 s, 7 cm from its centre)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.24 m/s (vx +3.00, vy +0.00, vz +8.74)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.89 s  ball is at the top of its flight, at (2.67, 0.00, 4.01) m
 1.31 s  ball passes 0.06 m from hoop (hoop.rim_15) without touching it: nearest points (3.83, 0.01, 3.09) m and (3.77, 0.02, 3.05) m
 1.39 s  ball passes 0.12 m from backboard without touching it: nearest points (4.28, 0.00, 2.84) m and (4.38, 0.00, 2.90) m
 1.78 s  ball touches floor again
 1.83 s  ball leaves floor
 1.93 s  ball is at the top of its flight, at (5.59, 0.00, 0.17) m
 2.03 s  ball touches floor again
 6.00 s  ball is still moving at the end, 1.62 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.24 m/s (vx +3.00, vy +0.00, vz +8.74); touching floor
0.25 s: ball at (0.75, 0.00, 2.00) m, moving 6.96 m/s (vx +3.00, vy +0.00, vz +6.29); touching nothing
0.50 s: ball at (1.50, 0.00, 3.26) m, moving 4.87 m/s (vx +3.00, vy +0.00, vz +3.83); touching nothing
0.75 s: ball at (2.25, 0.00, 3.91) m, moving 3.30 m/s (vx +3.00, vy +0.00, vz +1.38); touching nothing
1.00 s: ball at (3.00, 0.00, 3.95) m, moving 3.19 m/s (vx +3.00, vy +0.00, vz -1.07); touching nothing
1.25 s: ball at (3.75, 0.00, 3.38) m, moving 4.63 m/s (vx +3.00, vy +0.00, vz -3.52); touching nothing
1.50 s: ball at (4.50, 0.00, 2.19) m, moving 6.69 m/s (vx +3.00, vy +0.00, vz -5.98); touching nothing
1.75 s: ball at (5.25, 0.00, 0.39) m, moving 8.95 m/s (vx +3.00, vy +0.00, vz -8.43); touching nothing
2.00 s: ball at (5.70, 0.00, 0.15) m, moving 1.71 m/s (vx +1.57, vy -0.00, vz -0.67); touching nothing
2.25 s: ball at (6.10, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
2.50 s: ball at (6.50, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
2.75 s: ball at (6.91, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
3.00 s: ball at (7.31, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
3.25 s: ball at (7.72, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
3.50 s: ball at (8.12, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
3.75 s: ball at (8.53, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
4.00 s: ball at (8.93, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
4.25 s: ball at (9.34, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
4.50 s: ball at (9.74, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
4.75 s: ball at (10.15, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
5.00 s: ball at (10.55, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
5.25 s: ball at (10.96, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz +0.00); touching floor
5.50 s: ball at (11.36, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
5.75 s: ball at (11.77, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
6.00 s: ball at (12.17, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- ball at (12.17, 0.00, 0.12) m, moving 1.62 m/s (vx +1.62, vy -0.00, vz -0.00); touching floor
</history>
