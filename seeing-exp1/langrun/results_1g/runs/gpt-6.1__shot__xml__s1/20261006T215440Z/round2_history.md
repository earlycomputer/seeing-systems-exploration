Your expectations, checked against the run (1 of 1 hold):

- holds: ball drops through hoop (through at 1.40 s, 0 cm from its centre)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.41 m/s (vx +2.86, vy +0.00, vz +8.97)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.92 s  ball is at the top of its flight, at (2.61, 0.00, 4.21) m
 1.38 s  ball passes 0.07 m from hoop (hoop.rim_15) without touching it: nearest points (3.84, 0.01, 3.09) m and (3.77, 0.02, 3.05) m
 1.42 s  ball passes 0.08 m from backboard_assembly (backboard_assembly.bracket) without touching it: nearest points (4.17, 0.00, 3.00) m and (4.24, 0.00, 3.04) m
 1.83 s  ball touches floor again
 1.91 s  ball leaves floor
 1.98 s  ball is at the top of its flight, at (5.51, 0.00, 0.14) m
 2.05 s  ball touches floor again
 6.00 s  ball is still moving at the end, 1.91 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.41 m/s (vx +2.86, vy +0.00, vz +8.97); touching floor
0.25 s: ball at (0.71, 0.00, 2.04) m, moving 7.12 m/s (vx +2.86, vy -0.00, vz +6.52); touching nothing
0.50 s: ball at (1.42, 0.00, 3.37) m, moving 4.97 m/s (vx +2.86, vy -0.00, vz +4.06); touching nothing
0.75 s: ball at (2.14, 0.00, 4.08) m, moving 3.28 m/s (vx +2.86, vy -0.00, vz +1.61); touching nothing
1.00 s: ball at (2.85, 0.00, 4.18) m, moving 2.98 m/s (vx +2.86, vy -0.00, vz -0.84); touching nothing
1.25 s: ball at (3.57, 0.00, 3.66) m, moving 4.36 m/s (vx +2.86, vy -0.00, vz -3.29); touching nothing
1.50 s: ball at (4.28, 0.00, 2.54) m, moving 6.42 m/s (vx +2.86, vy -0.00, vz -5.75); touching nothing
1.75 s: ball at (4.99, 0.00, 0.79) m, moving 8.68 m/s (vx +2.86, vy -0.00, vz -8.20); touching nothing
2.00 s: ball at (5.54, 0.00, 0.14) m, moving 1.80 m/s (vx +1.79, vy -0.00, vz -0.16); touching nothing
2.25 s: ball at (6.00, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
2.50 s: ball at (6.48, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
2.75 s: ball at (6.96, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
3.00 s: ball at (7.44, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
3.25 s: ball at (7.91, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
3.50 s: ball at (8.39, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
3.75 s: ball at (8.87, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
4.00 s: ball at (9.35, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
4.25 s: ball at (9.82, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
4.50 s: ball at (10.30, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
4.75 s: ball at (10.78, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
5.00 s: ball at (11.26, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
5.25 s: ball at (11.73, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
5.50 s: ball at (12.21, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
5.75 s: ball at (12.69, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz -0.00); touching floor
6.00 s: ball at (13.17, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor

At the end (6.00 s):
- ball at (13.17, 0.00, 0.12) m, moving 1.91 m/s (vx +1.91, vy -0.00, vz +0.00); touching floor
</history>
