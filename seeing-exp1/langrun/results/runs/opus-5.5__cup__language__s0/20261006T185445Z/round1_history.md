MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.11, 0.00, 0.39) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_deck
 0.04 s  ball starts moving
 1.26 s  ball leaves ramp_deck
 1.42 s  ball first touches cup_base
 1.48 s  ball leaves cup_base
 1.49 s  ball first touches cup_far_wall
 1.54 s  ball leaves cup_far_wall
 1.57 s  ball touches cup_base again
 2.22 s  ball comes to rest at (1.27, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.11, 0.00, 0.39) m, at rest; touching ramp_deck
0.25 s: ball at (0.15, 0.00, 0.38) m, moving 0.31 m/s (vx +0.31, vy +0.00, vz -0.06); touching ramp_deck
0.50 s: ball at (0.26, 0.00, 0.36) m, moving 0.59 m/s (vx +0.58, vy -0.00, vz -0.11); touching ramp_deck
0.75 s: ball at (0.44, 0.00, 0.32) m, moving 0.86 m/s (vx +0.84, vy +0.00, vz -0.18); touching ramp_deck
1.00 s: ball at (0.68, 0.00, 0.27) m, moving 1.13 m/s (vx +1.11, vy +0.00, vz -0.21); touching ramp_deck
1.25 s: ball at (0.99, 0.00, 0.21) m, moving 1.40 m/s (vx +1.37, vy +0.00, vz -0.27); touching ramp_deck
1.50 s: ball at (1.33, 0.00, 0.06) m, moving 0.26 m/s (vx +0.16, vy +0.00, vz +0.20); touching cup_far_wall
1.75 s: ball at (1.30, 0.00, 0.06) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching cup_base
2.00 s: ball at (1.28, 0.00, 0.06) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup_base
2.25 s: ball at (1.27, 0.00, 0.06) m, at rest; touching cup_base
2.50 s: ball at (1.26, 0.00, 0.06) m, at rest; touching cup_base
2.75 s: ball at (1.25, 0.00, 0.06) m, at rest; touching cup_base
3.00 s: ball at (1.24, 0.00, 0.06) m, at rest; touching cup_base
(the same through 3.25 s)
3.50 s: ball at (1.23, 0.00, 0.06) m, at rest; touching cup_base
(the same through 4.75 s)
5.00 s: ball at (1.22, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.22, 0.00, 0.06) m, at rest; touching cup_base
</history>
