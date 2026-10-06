MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.09, 0.00, 0.24) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.01 s  ball first touches ramp_body.ramp_board
 0.85 s  ball leaves ramp_body.ramp_board
 0.98 s  ball first touches cup_bottom
 1.04 s  ball first touches cup_wall_0
 1.05 s  ball leaves cup_bottom
 1.10 s  ball leaves cup_wall_0
 1.12 s  ball touches cup_bottom again
 1.70 s  ball comes to rest at (0.63, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (0.09, 0.00, 0.24) m, at rest; touching nothing
0.25 s: ball at (0.13, 0.00, 0.23) m, moving 0.32 m/s (vx +0.31, vy -0.00, vz -0.07); touching ramp_body.ramp_board
0.50 s: ball at (0.24, 0.00, 0.21) m, moving 0.60 m/s (vx +0.58, vy -0.00, vz -0.12); touching ramp_body.ramp_board
0.75 s: ball at (0.42, 0.00, 0.17) m, moving 0.86 m/s (vx +0.84, vy +0.00, vz -0.18); touching ramp_body.ramp_board
1.00 s: ball at (0.65, 0.00, 0.03) m, moving 0.87 m/s (vx +0.87, vy +0.00, vz +0.04); touching cup_bottom
1.25 s: ball at (0.66, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching cup_bottom
1.50 s: ball at (0.64, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching cup_bottom
1.75 s: ball at (0.63, 0.00, 0.04) m, at rest; touching cup_bottom
2.00 s: ball at (0.62, 0.00, 0.04) m, at rest; touching cup_bottom
2.25 s: ball at (0.61, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 2.75 s)
3.00 s: ball at (0.60, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.60, 0.00, 0.04) m, at rest; touching cup_bottom
</history>
