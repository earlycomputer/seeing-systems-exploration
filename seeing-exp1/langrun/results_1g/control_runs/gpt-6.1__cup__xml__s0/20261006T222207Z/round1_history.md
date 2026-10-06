MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-1.08, 0.00, 0.72) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.03 s  ball first touches ramp_surface
 1.76 s  ball passes 0.07 m from ramp_support_low without touching it: nearest points (0.22, 0.00, 0.31) m and (0.20, 0.00, 0.24) m
 1.83 s  ball leaves ramp_surface
 2.02 s  ball first touches cup_base
 2.04 s  ball leaves cup_base
 2.11 s  ball touches cup_base again
 2.22 s  ball comes to rest at (0.71, 0.00, 0.10) m

State every 0.25 s:
0.00 s: ball at (-1.08, 0.00, 0.72) m, at rest; touching nothing
0.25 s: ball at (-1.05, 0.00, 0.71) m, moving 0.23 m/s (vx +0.22, vy +0.00, vz -0.05); touching ramp_surface
0.50 s: ball at (-0.97, 0.00, 0.69) m, moving 0.44 m/s (vx +0.43, vy +0.00, vz -0.12); touching ramp_surface
0.75 s: ball at (-0.84, 0.00, 0.65) m, moving 0.65 m/s (vx +0.64, vy +0.00, vz -0.14); touching ramp_surface
1.00 s: ball at (-0.65, 0.00, 0.60) m, moving 0.87 m/s (vx +0.85, vy +0.00, vz -0.22); touching ramp_surface
1.25 s: ball at (-0.42, 0.00, 0.54) m, moving 1.10 m/s (vx +1.05, vy +0.00, vz -0.31); touching nothing
1.50 s: ball at (-0.13, 0.00, 0.46) m, moving 1.31 m/s (vx +1.26, vy +0.00, vz -0.33); touching nothing
1.75 s: ball at (0.21, 0.00, 0.37) m, moving 1.53 m/s (vx +1.47, vy +0.00, vz -0.44); touching nothing
2.00 s: ball at (0.60, 0.00, 0.14) m, moving 2.52 m/s (vx +1.54, vy +0.00, vz -2.00); touching nothing
2.25 s: ball at (0.71, 0.00, 0.10) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.71, 0.00, 0.10) m, at rest; touching cup_base
</history>
