Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (touching from the start)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.16, 0.00, 0.42) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_deck
 0.04 s  ball starts moving
 1.22 s  ball leaves ramp_deck
 1.36 s  ball first touches cup_base
 1.38 s  ball leaves cup_base
 1.45 s  ball touches cup_base again
 1.46 s  ball leaves cup_base
 1.49 s  ball touches cup_base again
 1.95 s  ball comes to rest at (1.55, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.16, 0.00, 0.42) m, at rest; touching ramp_deck
0.25 s: ball at (0.20, 0.00, 0.41) m, moving 0.30 m/s (vx +0.29, vy +0.00, vz -0.08); touching nothing
0.50 s: ball at (0.31, 0.00, 0.38) m, moving 0.59 m/s (vx +0.58, vy -0.00, vz -0.13); touching ramp_deck
0.75 s: ball at (0.48, 0.00, 0.34) m, moving 0.88 m/s (vx +0.86, vy -0.00, vz -0.18); touching ramp_deck
1.00 s: ball at (0.73, 0.00, 0.27) m, moving 1.18 m/s (vx +1.14, vy -0.00, vz -0.28); touching ramp_deck
1.25 s: ball at (1.05, 0.00, 0.19) m, moving 1.54 m/s (vx +1.39, vy -0.00, vz -0.67); touching nothing
1.50 s: ball at (1.34, 0.00, 0.06) m, moving 0.84 m/s (vx +0.84, vy -0.00, vz +0.05); touching nothing
1.75 s: ball at (1.50, 0.00, 0.06) m, moving 0.40 m/s (vx +0.40, vy -0.00, vz +0.03); touching nothing
2.00 s: ball at (1.55, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.55, 0.00, 0.06) m, at rest; touching cup_base
</history>
