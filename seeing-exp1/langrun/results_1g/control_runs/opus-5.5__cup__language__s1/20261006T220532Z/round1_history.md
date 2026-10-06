MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.11, 0.00, 0.33) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp_deck
 0.07 s  ball starts moving
 3.99 s  ball leaves ramp_deck
 4.09 s  ball first touches cup_near_wall
 4.23 s  ball leaves cup_near_wall
 4.32 s  ball first touches cup_base
 4.38 s  ball comes to rest at (1.11, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.11, 0.00, 0.33) m, at rest; touching nothing
0.25 s: ball at (0.12, 0.00, 0.33) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz -0.02); touching ramp_deck
0.50 s: ball at (0.15, 0.00, 0.33) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.02); touching ramp_deck
0.75 s: ball at (0.19, 0.00, 0.32) m, moving 0.15 m/s (vx +0.14, vy +0.00, vz -0.02); touching ramp_deck
1.00 s: ball at (0.22, 0.00, 0.32) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.02); touching ramp_deck
1.25 s: ball at (0.27, 0.00, 0.31) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz -0.02); touching ramp_deck
1.50 s: ball at (0.31, 0.00, 0.30) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz -0.04); touching ramp_deck
1.75 s: ball at (0.36, 0.00, 0.30) m, moving 0.22 m/s (vx +0.21, vy +0.00, vz -0.04); touching ramp_deck
2.00 s: ball at (0.42, 0.00, 0.29) m, moving 0.24 m/s (vx +0.23, vy +0.00, vz -0.05); touching nothing
2.25 s: ball at (0.48, 0.00, 0.28) m, moving 0.26 m/s (vx +0.25, vy +0.00, vz -0.06); touching nothing
2.50 s: ball at (0.54, 0.00, 0.27) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz -0.03); touching ramp_deck
2.75 s: ball at (0.61, 0.00, 0.26) m, moving 0.29 m/s (vx +0.28, vy -0.00, vz -0.05); touching nothing
3.00 s: ball at (0.69, 0.00, 0.25) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.05); touching ramp_deck
3.25 s: ball at (0.76, 0.00, 0.24) m, moving 0.32 m/s (vx +0.32, vy +0.00, vz -0.04); touching ramp_deck
3.50 s: ball at (0.85, 0.00, 0.22) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz -0.05); touching ramp_deck
3.75 s: ball at (0.93, 0.00, 0.21) m, moving 0.35 m/s (vx +0.35, vy +0.00, vz -0.03); touching ramp_deck
4.00 s: ball at (1.02, 0.00, 0.19) m, moving 0.50 m/s (vx +0.39, vy +0.00, vz -0.32); touching nothing
4.25 s: ball at (1.09, 0.00, 0.11) m, moving 0.56 m/s (vx +0.26, vy +0.00, vz -0.50); touching nothing
4.50 s: ball at (1.11, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.11, 0.00, 0.05) m, at rest; touching cup_base
</history>
