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
 0.89 s  ball is at the top of its flight, at (2.67, 0.00, 4.00) m
 1.30 s  ball passes 0.05 m from hoop (hoop.rim_15) without touching it: nearest points (3.81, 0.01, 3.09) m and (3.77, 0.01, 3.06) m
 1.39 s  ball passes 0.12 m from backboard (backboard_panel) without touching it: nearest points (4.27, 0.00, 2.84) m and (4.38, 0.00, 2.90) m
 1.78 s  ball touches floor again
 1.82 s  ball leaves floor
 1.89 s  ball is at the top of its flight, at (5.35, 0.00, 0.15) m
 1.97 s  ball touches floor again
 2.00 s  ball comes to rest at (5.36, 0.00, 0.12) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.24 m/s (vx +3.00, vy +0.00, vz +8.74); touching floor
0.25 s: ball at (0.74, 0.00, 1.98) m, moving 6.96 m/s (vx +3.00, vy +0.00, vz +6.29); touching nothing
0.50 s: ball at (1.49, 0.00, 3.25) m, moving 4.87 m/s (vx +3.00, vy +0.00, vz +3.83); touching nothing
0.75 s: ball at (2.24, 0.00, 3.90) m, moving 3.30 m/s (vx +3.00, vy +0.00, vz +1.38); touching nothing
1.00 s: ball at (2.99, 0.00, 3.94) m, moving 3.19 m/s (vx +3.00, vy +0.00, vz -1.07); touching nothing
1.25 s: ball at (3.74, 0.00, 3.37) m, moving 4.63 m/s (vx +3.00, vy +0.00, vz -3.52); touching nothing
1.50 s: ball at (4.49, 0.00, 2.19) m, moving 6.69 m/s (vx +3.00, vy +0.00, vz -5.98); touching nothing
1.75 s: ball at (5.24, 0.00, 0.39) m, moving 8.95 m/s (vx +3.00, vy +0.00, vz -8.43); touching nothing
2.00 s: ball at (5.36, 0.00, 0.12) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball at (5.36, 0.00, 0.12) m, at rest; touching floor
</history>
