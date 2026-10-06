MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-1.60, 0.00, 1.43) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.02 s  ball first touches ramp_surface
 1.19 s  ball passes 0.06 m from ramp_support_low without touching it: nearest points (-0.23, 0.00, 0.91) m and (-0.25, 0.00, 0.85) m
 1.40 s  ball leaves ramp_surface
 1.58 s  ball first touches cup_wall_00
 1.62 s  ball leaves cup_wall_00
 1.80 s  ball first touches cup_base
 1.87 s  ball comes to rest at (0.73, 0.00, 0.13) m

State every 0.25 s:
0.00 s: ball at (-1.60, 0.00, 1.43) m, at rest; touching nothing
0.25 s: ball at (-1.54, 0.00, 1.41) m, moving 0.52 m/s (vx +0.49, vy +0.00, vz -0.16); touching ramp_surface
0.50 s: ball at (-1.35, 0.00, 1.35) m, moving 1.04 m/s (vx +0.99, vy +0.00, vz -0.32); touching ramp_surface
0.75 s: ball at (-1.05, 0.00, 1.25) m, moving 1.56 m/s (vx +1.48, vy +0.00, vz -0.48); touching ramp_surface
1.00 s: ball at (-0.61, 0.00, 1.11) m, moving 2.08 m/s (vx +1.97, vy +0.00, vz -0.64); touching nothing
1.25 s: ball at (-0.06, 0.00, 0.93) m, moving 2.59 m/s (vx +2.47, vy +0.00, vz -0.79); touching ramp_surface
1.50 s: ball at (0.61, 0.00, 0.66) m, moving 3.34 m/s (vx +2.76, vy +0.00, vz -1.88); touching nothing
1.75 s: ball at (0.76, 0.00, 0.25) m, moving 2.20 m/s (vx -0.53, vy +0.00, vz -2.14); touching nothing
2.00 s: ball at (0.73, 0.00, 0.13) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.73, 0.00, 0.13) m, at rest; touching cup_base
</history>
