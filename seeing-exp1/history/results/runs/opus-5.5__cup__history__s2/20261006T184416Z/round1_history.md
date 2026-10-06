MuJoCo ran the scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.14, 0.00, 1.04) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.02 s  ball first touches ramp_deck
 1.26 s  ball leaves ramp_deck
 1.48 s  ball first touches cup_near
 1.51 s  ball first touches floor
 1.52 s  ball leaves cup_near
 3.14 s  ball comes to rest at (1.65, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.14, 0.00, 1.04) m, at rest; touching nothing
0.25 s: ball at (0.20, 0.00, 1.02) m, moving 0.50 m/s (vx +0.48, vy -0.00, vz -0.16); touching ramp_deck
0.50 s: ball at (0.38, 0.00, 0.96) m, moving 0.99 m/s (vx +0.93, vy +0.00, vz -0.33); touching ramp_deck
0.75 s: ball at (0.67, 0.00, 0.86) m, moving 1.47 m/s (vx +1.39, vy -0.00, vz -0.48); touching ramp_deck
1.00 s: ball at (1.07, 0.00, 0.72) m, moving 1.96 m/s (vx +1.84, vy -0.00, vz -0.69); touching nothing
1.25 s: ball at (1.59, 0.00, 0.54) m, moving 2.43 m/s (vx +2.30, vy +0.00, vz -0.78); touching nothing
1.50 s: ball at (2.14, 0.00, 0.08) m, moving 1.58 m/s (vx -0.24, vy +0.00, vz -1.56); touching cup_near
1.75 s: ball at (2.00, 0.00, 0.06) m, moving 0.54 m/s (vx -0.54, vy +0.00, vz +0.02); touching floor
2.00 s: ball at (1.88, 0.00, 0.06) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.01); touching floor
2.25 s: ball at (1.78, 0.00, 0.06) m, moving 0.31 m/s (vx -0.31, vy +0.00, vz -0.00); touching floor
2.50 s: ball at (1.72, 0.00, 0.06) m, moving 0.21 m/s (vx -0.21, vy +0.00, vz -0.00); touching floor
2.75 s: ball at (1.68, 0.00, 0.06) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching floor
3.00 s: ball at (1.65, 0.00, 0.06) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching floor
3.25 s: ball at (1.64, 0.00, 0.06) m, at rest; touching floor
(the same through 3.50 s)
3.75 s: ball at (1.63, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball at (1.63, 0.00, 0.06) m, at rest; touching floor
</history>
