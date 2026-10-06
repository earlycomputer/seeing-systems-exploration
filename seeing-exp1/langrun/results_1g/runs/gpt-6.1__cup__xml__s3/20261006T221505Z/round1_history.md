Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (first touch at 0.01 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.83, 0.00, 0.64) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.01 s  ball first touches ramp_surface
 0.85 s  ball leaves ramp_surface
 1.06 s  ball first touches cup_base
 1.09 s  ball leaves cup_base
 1.11 s  ball first touches cup_wall_00
 1.15 s  ball leaves cup_wall_00
 1.19 s  ball touches cup_base again
 1.22 s  ball comes to rest at (0.33, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (-0.83, 0.00, 0.64) m, at rest; touching nothing
0.25 s: ball at (-0.77, 0.00, 0.62) m, moving 0.54 m/s (vx +0.51, vy +0.00, vz -0.17); touching ramp_surface
0.50 s: ball at (-0.58, 0.00, 0.55) m, moving 1.07 m/s (vx +1.02, vy +0.00, vz -0.34); touching ramp_surface
0.75 s: ball at (-0.26, 0.00, 0.45) m, moving 1.61 m/s (vx +1.53, vy +0.00, vz -0.50); touching ramp_surface
1.00 s: ball at (0.16, 0.00, 0.21) m, moving 2.66 m/s (vx +1.74, vy +0.00, vz -2.01); touching nothing
1.25 s: ball at (0.33, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.33, 0.00, 0.06) m, at rest; touching cup_base
</history>
