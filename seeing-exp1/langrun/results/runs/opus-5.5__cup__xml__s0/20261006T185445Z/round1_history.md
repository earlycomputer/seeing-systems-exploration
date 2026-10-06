MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.17, 0.00, 0.28) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_board
 0.02 s  ball starts moving
 0.68 s  ball leaves ramp_board
 0.78 s  ball first touches cup_bottom
 0.87 s  ball first touches cup_wall_far
 0.88 s  ball leaves cup_bottom
 0.91 s  ball touches cup_bottom again
 0.94 s  ball leaves cup_wall_far
 1.33 s  ball comes to rest at (0.44, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (-0.17, 0.00, 0.28) m, at rest; touching ramp_board
0.25 s: ball at (-0.11, 0.00, 0.26) m, moving 0.50 m/s (vx +0.47, vy +0.00, vz -0.18); touching nothing
0.50 s: ball at (0.06, 0.00, 0.20) m, moving 0.98 m/s (vx +0.91, vy -0.00, vz -0.35); touching ramp_board
0.75 s: ball at (0.34, 0.00, 0.07) m, moving 1.68 m/s (vx +1.23, vy +0.00, vz -1.15); touching nothing
1.00 s: ball at (0.46, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching cup_bottom
1.25 s: ball at (0.44, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup_bottom
1.50 s: ball at (0.43, 0.00, 0.04) m, at rest; touching cup_bottom
1.75 s: ball at (0.42, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.42, 0.00, 0.04) m, at rest; touching cup_bottom
</history>
