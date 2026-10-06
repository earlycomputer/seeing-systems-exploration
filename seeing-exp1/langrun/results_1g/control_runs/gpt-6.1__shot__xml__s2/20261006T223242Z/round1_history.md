MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 10.00 m/s (vx +2.50, vy +0.00, vz +9.68)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.99 s  ball is at the top of its flight, at (2.46, 0.00, 4.89) m
 1.58 s  ball passes 0.08 m from hoop (hoop.rim_15) without touching it: nearest points (3.85, 0.01, 3.10) m and (3.77, 0.02, 3.05) m
 1.97 s  ball touches floor again
 2.01 s  ball leaves floor
 2.10 s  ball is at the top of its flight, at (4.98, 0.00, 0.16) m
 2.19 s  ball touches floor again
 2.30 s  ball comes to rest at (5.02, 0.00, 0.12) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 10.00 m/s (vx +2.50, vy +0.00, vz +9.68); touching floor
0.25 s: ball at (0.62, 0.00, 2.22) m, moving 7.65 m/s (vx +2.50, vy -0.00, vz +7.23); touching nothing
0.50 s: ball at (1.24, 0.00, 3.72) m, moving 5.39 m/s (vx +2.50, vy -0.00, vz +4.77); touching nothing
0.75 s: ball at (1.87, 0.00, 4.61) m, moving 3.41 m/s (vx +2.50, vy -0.00, vz +2.32); touching nothing
1.00 s: ball at (2.49, 0.00, 4.88) m, moving 2.50 m/s (vx +2.50, vy -0.00, vz -0.13); touching nothing
1.25 s: ball at (3.12, 0.00, 4.55) m, moving 3.59 m/s (vx +2.50, vy -0.00, vz -2.58); touching nothing
1.50 s: ball at (3.74, 0.00, 3.60) m, moving 5.62 m/s (vx +2.50, vy -0.00, vz -5.04); touching nothing
1.75 s: ball at (4.37, 0.00, 2.03) m, moving 7.89 m/s (vx +2.50, vy -0.00, vz -7.49); touching nothing
2.00 s: ball at (4.94, 0.00, 0.11) m, moving 1.02 m/s (vx +0.32, vy +0.00, vz +0.97); touching floor
2.25 s: ball at (5.02, 0.00, 0.12) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz -0.00); touching floor
2.50 s: ball at (5.02, 0.00, 0.12) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball at (5.02, 0.00, 0.12) m, at rest; touching floor
</history>
