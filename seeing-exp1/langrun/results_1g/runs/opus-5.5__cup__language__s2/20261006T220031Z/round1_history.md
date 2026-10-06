Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (first touch at 0.00 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.11, 0.00, 0.52) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp_deck
 0.04 s  ball starts moving
 1.35 s  ball leaves ramp_deck
 1.55 s  ball first touches cup_base
 1.58 s  ball leaves cup_base
 1.62 s  ball touches cup_base again
 1.73 s  ball leaves cup_base
 1.73 s  ball first touches cup_far_wall
 1.76 s  ball leaves cup_far_wall
 1.77 s  ball touches cup_base again
 1.83 s  ball comes to rest at (1.45, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.11, 0.00, 0.52) m, at rest; touching nothing
0.25 s: ball at (0.14, 0.00, 0.52) m, moving 0.27 m/s (vx +0.26, vy +0.00, vz -0.07); touching ramp_deck
0.50 s: ball at (0.24, 0.00, 0.49) m, moving 0.52 m/s (vx +0.50, vy -0.00, vz -0.13); touching ramp_deck
0.75 s: ball at (0.39, 0.00, 0.45) m, moving 0.77 m/s (vx +0.73, vy -0.00, vz -0.24); touching nothing
1.00 s: ball at (0.61, 0.00, 0.40) m, moving 1.00 m/s (vx +0.98, vy -0.00, vz -0.21); touching ramp_deck
1.25 s: ball at (0.88, 0.00, 0.33) m, moving 1.25 m/s (vx +1.21, vy -0.00, vz -0.31); touching ramp_deck
1.50 s: ball at (1.20, 0.00, 0.15) m, moving 2.20 m/s (vx +1.31, vy -0.00, vz -1.77); touching nothing
1.75 s: ball at (1.46, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz +0.02); touching cup_far_wall
2.00 s: ball at (1.45, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.45, 0.00, 0.05) m, at rest; touching cup_base
</history>
