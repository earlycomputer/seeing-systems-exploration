MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.13, 0.00, 0.43) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp
 0.03 s  ball starts moving
 1.29 s  ball leaves ramp
 1.41 s  ball first touches cup_base
 1.70 s  ball leaves cup_base
 1.70 s  ball first touches cup_far_wall
 1.75 s  ball leaves cup_far_wall
 1.80 s  ball touches cup_base again
 2.41 s  ball comes to rest at (1.82, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.13, 0.00, 0.43) m, at rest; touching nothing
0.25 s: ball at (0.17, 0.00, 0.42) m, moving 0.34 m/s (vx +0.33, vy -0.00, vz -0.08); touching ramp
0.50 s: ball at (0.30, 0.00, 0.39) m, moving 0.67 m/s (vx +0.65, vy +0.00, vz -0.15); touching ramp
0.75 s: ball at (0.50, 0.00, 0.35) m, moving 1.00 m/s (vx +0.97, vy +0.00, vz -0.25); touching nothing
1.00 s: ball at (0.78, 0.00, 0.28) m, moving 1.33 m/s (vx +1.29, vy +0.00, vz -0.32); touching nothing
1.25 s: ball at (1.14, 0.00, 0.19) m, moving 1.65 m/s (vx +1.61, vy +0.00, vz -0.37); touching ramp
1.50 s: ball at (1.55, 0.00, 0.06) m, moving 1.58 m/s (vx +1.58, vy +0.00, vz +0.02); touching cup_base
1.75 s: ball at (1.87, 0.00, 0.07) m, moving 0.23 m/s (vx -0.22, vy +0.00, vz +0.06); touching cup_far_wall
2.00 s: ball at (1.84, 0.00, 0.06) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching cup_base
2.25 s: ball at (1.82, 0.00, 0.06) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup_base
2.50 s: ball at (1.81, 0.00, 0.06) m, at rest; touching cup_base
2.75 s: ball at (1.80, 0.00, 0.06) m, at rest; touching cup_base
3.00 s: ball at (1.79, 0.00, 0.06) m, at rest; touching cup_base
(the same through 3.25 s)
3.50 s: ball at (1.78, 0.00, 0.06) m, at rest; touching cup_base
(the same through 4.50 s)
4.75 s: ball at (1.77, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.77, 0.00, 0.06) m, at rest; touching cup_base
</history>
