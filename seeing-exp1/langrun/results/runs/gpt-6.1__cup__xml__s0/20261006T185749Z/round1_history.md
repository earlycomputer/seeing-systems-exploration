MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-1.63, 0.00, 1.16) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp_deck
 0.02 s  ball starts moving
 1.25 s  ball leaves ramp_deck
 1.49 s  ball first touches cup_bottom
 1.52 s  ball leaves cup_bottom
 1.59 s  ball is at the top of its flight, at (0.76, 0.00, 0.14) m
 1.66 s  ball touches cup_bottom again
 1.68 s  ball leaves cup_bottom
 1.74 s  ball touches cup_bottom again
 1.84 s  ball comes to rest at (0.90, 0.00, 0.12) m

State every 0.25 s:
0.00 s: ball at (-1.63, 0.00, 1.16) m, at rest; touching ramp_deck
0.25 s: ball at (-1.57, 0.00, 1.14) m, moving 0.55 m/s (vx +0.53, vy +0.00, vz -0.18); touching ramp_deck
0.50 s: ball at (-1.37, 0.00, 1.07) m, moving 1.11 m/s (vx +1.05, vy +0.00, vz -0.35); touching ramp_deck
0.75 s: ball at (-1.04, 0.00, 0.96) m, moving 1.66 m/s (vx +1.58, vy +0.00, vz -0.53); touching ramp_deck
1.00 s: ball at (-0.58, 0.00, 0.81) m, moving 2.21 m/s (vx +2.10, vy +0.00, vz -0.70); touching ramp_deck
1.25 s: ball at (0.01, 0.00, 0.61) m, moving 2.77 m/s (vx +2.63, vy +0.00, vz -0.88); touching ramp_deck
1.50 s: ball at (0.66, 0.00, 0.11) m, moving 1.52 m/s (vx +1.49, vy +0.00, vz -0.31); touching cup_bottom
1.75 s: ball at (0.88, 0.00, 0.12) m, moving 0.37 m/s (vx +0.35, vy +0.00, vz +0.13); touching cup_bottom
2.00 s: ball at (0.90, 0.00, 0.12) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.90, 0.00, 0.12) m, at rest; touching cup_bottom
</history>
