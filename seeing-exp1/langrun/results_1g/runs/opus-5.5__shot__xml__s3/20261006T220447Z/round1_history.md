Your expectations, checked against the run (2 of 2 hold):

- holds: ball drops through hoop (through at 1.33 s, 8 cm from its centre)
- holds: ball touches floor (first touch at 1.78 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.23 m/s (vx +3.01, vy +0.00, vz +8.72)

What happened, in order:
 0.89 s  ball is at the top of its flight, at (2.67, 0.00, 3.99) m
 1.30 s  ball passes 0.06 m from hoop (hoop.rim_07) without touching it: nearest points (3.82, 0.02, 3.09) m and (3.77, 0.03, 3.05) m
 1.39 s  ball passes 0.12 m from backboard without touching it: nearest points (4.28, 0.00, 2.83) m and (4.38, 0.00, 2.90) m
 1.78 s  ball first touches floor
 1.81 s  ball leaves floor
 1.89 s  ball first touches support.pole
 1.92 s  ball leaves support.pole
 2.03 s  ball is at the top of its flight, at (5.53, 0.00, 0.32) m
 2.23 s  ball touches floor again
 2.27 s  ball leaves floor
 2.32 s  ball touches floor again
 2.35 s  ball comes to rest at (5.45, 0.00, 0.12) m
 5.20 s  ball touches support.pole again
 5.23 s  ball leaves support.pole

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.23 m/s (vx +3.01, vy +0.00, vz +8.72); touching nothing
0.25 s: ball at (0.75, 0.00, 1.98) m, moving 6.96 m/s (vx +3.01, vy +0.00, vz +6.27); touching nothing
0.50 s: ball at (1.50, 0.00, 3.24) m, moving 4.86 m/s (vx +3.01, vy +0.00, vz +3.82); touching nothing
0.75 s: ball at (2.25, 0.00, 3.90) m, moving 3.30 m/s (vx +3.01, vy +0.00, vz +1.37); touching nothing
1.00 s: ball at (3.00, 0.00, 3.93) m, moving 3.20 m/s (vx +3.01, vy +0.00, vz -1.08); touching nothing
1.25 s: ball at (3.75, 0.00, 3.36) m, moving 4.64 m/s (vx +3.01, vy +0.00, vz -3.54); touching nothing
1.50 s: ball at (4.51, 0.00, 2.17) m, moving 6.70 m/s (vx +3.01, vy +0.00, vz -5.99); touching nothing
1.75 s: ball at (5.26, 0.00, 0.37) m, moving 8.96 m/s (vx +3.01, vy +0.00, vz -8.44); touching nothing
2.00 s: ball at (5.55, 0.00, 0.31) m, moving 0.52 m/s (vx -0.43, vy -0.00, vz +0.28); touching nothing
2.25 s: ball at (5.44, 0.00, 0.11) m, moving 0.40 m/s (vx +0.03, vy -0.00, vz +0.40); touching floor
2.50 s: ball at (5.45, 0.00, 0.12) m, at rest; touching floor
2.75 s: ball at (5.47, 0.00, 0.12) m, at rest; touching floor
3.00 s: ball at (5.48, 0.00, 0.12) m, at rest; touching floor
3.25 s: ball at (5.49, 0.00, 0.12) m, at rest; touching floor
3.50 s: ball at (5.50, 0.00, 0.12) m, at rest; touching floor
3.75 s: ball at (5.51, 0.00, 0.12) m, at rest; touching floor
4.00 s: ball at (5.52, 0.00, 0.12) m, at rest; touching floor
4.25 s: ball at (5.54, 0.00, 0.12) m, at rest; touching floor
4.50 s: ball at (5.55, 0.00, 0.12) m, at rest; touching floor
4.75 s: ball at (5.56, 0.00, 0.12) m, at rest; touching floor
5.00 s: ball at (5.57, 0.00, 0.12) m, at rest; touching floor
5.25 s: ball at (5.58, 0.00, 0.12) m, at rest; touching floor
(the same through 5.75 s)
6.00 s: ball at (5.57, 0.00, 0.12) m, at rest; touching floor

At the end (6.00 s):
- ball at (5.57, 0.00, 0.12) m, at rest; touching floor
</history>
