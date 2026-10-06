MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.11, 0.00, 0.43) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_deck
 0.04 s  ball starts moving
 1.23 s  ball leaves ramp_deck
 1.41 s  ball first touches cup_base
 1.43 s  ball leaves cup_base
 1.50 s  ball touches cup_base again
 1.65 s  ball comes to rest at (1.38, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.11, 0.00, 0.43) m, at rest; touching ramp_deck
0.25 s: ball at (0.15, 0.00, 0.42) m, moving 0.32 m/s (vx +0.31, vy +0.00, vz -0.06); touching ramp_deck
0.50 s: ball at (0.26, 0.00, 0.40) m, moving 0.62 m/s (vx +0.60, vy +0.00, vz -0.13); touching nothing
0.75 s: ball at (0.45, 0.00, 0.36) m, moving 0.91 m/s (vx +0.89, vy -0.00, vz -0.18); touching ramp_deck
1.00 s: ball at (0.71, 0.00, 0.31) m, moving 1.20 m/s (vx +1.18, vy +0.00, vz -0.23); touching ramp_deck
1.25 s: ball at (1.04, 0.00, 0.24) m, moving 1.53 m/s (vx +1.45, vy +0.00, vz -0.49); touching nothing
1.50 s: ball at (1.33, 0.00, 0.05) m, moving 0.55 m/s (vx +0.55, vy +0.00, vz -0.02); touching cup_base
1.75 s: ball at (1.38, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.38, 0.00, 0.05) m, at rest; touching cup_base
</history>
