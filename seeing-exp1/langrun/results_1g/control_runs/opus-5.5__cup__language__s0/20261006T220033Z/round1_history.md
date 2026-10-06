MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.29, 0.00, 0.27) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp_deck
 0.05 s  ball starts moving
 1.25 s  ball leaves ramp_deck
 1.40 s  ball first touches cup_base
 1.42 s  ball leaves cup_base
 1.46 s  ball touches cup_base again
 1.64 s  ball comes to rest at (1.00, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.29, 0.00, 0.27) m, at rest; touching nothing
0.25 s: ball at (0.31, 0.00, 0.27) m, moving 0.19 m/s (vx +0.18, vy -0.00, vz -0.03); touching ramp_deck
0.50 s: ball at (0.38, 0.00, 0.26) m, moving 0.35 m/s (vx +0.34, vy +0.00, vz -0.08); touching ramp_deck
0.75 s: ball at (0.48, 0.00, 0.23) m, moving 0.51 m/s (vx +0.49, vy +0.00, vz -0.13); touching nothing
1.00 s: ball at (0.63, 0.00, 0.21) m, moving 0.67 m/s (vx +0.65, vy +0.00, vz -0.16); touching nothing
1.25 s: ball at (0.81, 0.00, 0.17) m, moving 0.82 m/s (vx +0.81, vy -0.00, vz -0.16); touching ramp_deck
1.50 s: ball at (0.97, 0.00, 0.05) m, moving 0.33 m/s (vx +0.33, vy -0.00, vz -0.00); touching nothing
1.75 s: ball at (1.00, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.00, 0.00, 0.05) m, at rest; touching cup_base
</history>
