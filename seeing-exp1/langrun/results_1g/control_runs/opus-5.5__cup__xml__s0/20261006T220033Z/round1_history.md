MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.44, 0.00, 0.25) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.02 s  ball first touches ramp_body.ramp
 0.97 s  ball leaves ramp_body.ramp
 1.12 s  ball first touches cup_bottom
 1.42 s  ball first touches cup_wall_far
 1.42 s  ball leaves cup_bottom
 1.46 s  ball touches cup_bottom again
 1.48 s  ball leaves cup_wall_far
 1.98 s  ball comes to rest at (0.32, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (-0.44, 0.00, 0.25) m, at rest; touching nothing
0.25 s: ball at (-0.40, 0.00, 0.24) m, moving 0.27 m/s (vx +0.26, vy -0.00, vz -0.05); touching ramp_body.ramp
0.50 s: ball at (-0.31, 0.00, 0.23) m, moving 0.49 m/s (vx +0.48, vy -0.00, vz -0.09); touching ramp_body.ramp
0.75 s: ball at (-0.17, 0.00, 0.20) m, moving 0.70 m/s (vx +0.69, vy -0.00, vz -0.11); touching ramp_body.ramp
1.00 s: ball at (0.03, 0.00, 0.16) m, moving 0.97 m/s (vx +0.86, vy -0.00, vz -0.43); touching nothing
1.25 s: ball at (0.24, 0.00, 0.04) m, moving 0.77 m/s (vx +0.77, vy +0.00, vz +0.01); touching cup_bottom
1.50 s: ball at (0.36, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy +0.00, vz +0.01); touching cup_bottom
1.75 s: ball at (0.34, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching cup_bottom
2.00 s: ball at (0.32, 0.00, 0.04) m, at rest; touching cup_bottom
2.25 s: ball at (0.31, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 2.50 s)
2.75 s: ball at (0.30, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 3.25 s)
3.50 s: ball at (0.29, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.29, 0.00, 0.04) m, at rest; touching cup_bottom
</history>
