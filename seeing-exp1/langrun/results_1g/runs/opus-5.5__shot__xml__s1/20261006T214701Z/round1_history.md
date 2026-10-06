Your expectations, checked against the run (2 of 2 hold):

- holds: ball drops through hoop (through at 1.25 s, 8 cm from its centre)
- holds: ball touches floor (first touch at 1.73 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.07 m/s (vx +3.18, vy +0.00, vz +8.50)

What happened, in order:
 0.87 s  ball is at the top of its flight, at (2.76, 0.00, 3.79) m
 1.22 s  ball passes 0.04 m from hoop (hoop.rim_06) without touching it: nearest points (3.80, -0.02, 3.09) m and (3.78, -0.03, 3.06) m
 1.32 s  ball passes 0.10 m from backboard without touching it: nearest points (4.30, 0.00, 2.84) m and (4.38, 0.00, 2.90) m
 1.73 s  ball first touches floor
 1.76 s  ball leaves floor
 1.95 s  ball is at the top of its flight, at (5.84, 0.00, 0.29) m
 2.14 s  ball touches floor again
 2.17 s  ball leaves floor
 2.23 s  ball touches floor again
 2.31 s  ball leaves floor
 2.31 s  ball first touches support_pole
 2.34 s  ball leaves support_pole
 2.44 s  ball touches floor again
 2.47 s  ball comes to rest at (6.35, 0.00, 0.12) m
 4.44 s  ball touches support_pole again
 4.48 s  ball leaves support_pole

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.07 m/s (vx +3.18, vy +0.00, vz +8.50); touching nothing
0.25 s: ball at (0.79, 0.00, 1.92) m, moving 6.83 m/s (vx +3.18, vy +0.00, vz +6.04); touching nothing
0.50 s: ball at (1.58, 0.00, 3.13) m, moving 4.80 m/s (vx +3.18, vy +0.00, vz +3.59); touching nothing
0.75 s: ball at (2.38, 0.00, 3.72) m, moving 3.38 m/s (vx +3.18, vy +0.00, vz +1.14); touching nothing
1.00 s: ball at (3.18, 0.00, 3.70) m, moving 3.44 m/s (vx +3.18, vy +0.00, vz -1.31); touching nothing
1.25 s: ball at (3.97, 0.00, 3.07) m, moving 4.93 m/s (vx +3.18, vy +0.00, vz -3.77); touching nothing
1.50 s: ball at (4.77, 0.00, 1.83) m, moving 6.98 m/s (vx +3.18, vy +0.00, vz -6.22); touching nothing
1.75 s: ball at (5.54, 0.00, 0.09) m, moving 2.45 m/s (vx +1.52, vy -0.00, vz +1.92); touching floor
2.00 s: ball at (5.92, 0.00, 0.27) m, moving 1.58 m/s (vx +1.50, vy -0.00, vz -0.50); touching nothing
2.25 s: ball at (6.29, 0.00, 0.12) m, moving 1.51 m/s (vx +1.51, vy -0.00, vz +0.07); touching floor
2.50 s: ball at (6.35, 0.00, 0.12) m, at rest; touching floor
(the same through 2.75 s)
3.00 s: ball at (6.36, 0.00, 0.12) m, at rest; touching floor
(the same through 3.25 s)
3.50 s: ball at (6.37, 0.00, 0.12) m, at rest; touching floor
(the same through 4.00 s)
4.25 s: ball at (6.38, 0.00, 0.12) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball at (6.38, 0.00, 0.12) m, at rest; touching floor
</history>
