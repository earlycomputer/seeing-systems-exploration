Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches ramp (first touch at 0.02 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-1.35, 0.00, 1.03) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.02 s  ball first touches ramp_surface
 1.29 s  ball leaves ramp_surface
 1.57 s  ball first touches cup_base
 1.59 s  ball leaves cup_base
 1.65 s  ball is at the top of its flight, at (0.70, 0.00, 0.14) m
 1.71 s  ball touches cup_base again
 1.72 s  ball leaves cup_base
 1.77 s  ball touches cup_base again
 2.02 s  ball comes to rest at (0.90, 0.00, 0.12) m

State every 0.25 s:
0.00 s: ball at (-1.35, 0.00, 1.03) m, at rest; touching nothing
0.25 s: ball at (-1.30, 0.00, 1.01) m, moving 0.43 m/s (vx +0.41, vy +0.00, vz -0.11); touching ramp_surface
0.50 s: ball at (-1.14, 0.00, 0.97) m, moving 0.85 m/s (vx +0.83, vy +0.00, vz -0.22); touching ramp_surface
0.75 s: ball at (-0.89, 0.00, 0.90) m, moving 1.28 m/s (vx +1.23, vy +0.00, vz -0.35); touching nothing
1.00 s: ball at (-0.53, 0.00, 0.81) m, moving 1.71 m/s (vx +1.65, vy +0.00, vz -0.45); touching nothing
1.25 s: ball at (-0.06, 0.00, 0.68) m, moving 2.13 m/s (vx +2.06, vy +0.00, vz -0.53); touching ramp_surface
1.50 s: ball at (0.47, 0.00, 0.33) m, moving 3.38 m/s (vx +2.13, vy +0.00, vz -2.63); touching nothing
1.75 s: ball at (0.79, 0.00, 0.13) m, moving 0.78 m/s (vx +0.78, vy +0.00, vz -0.08); touching nothing
2.00 s: ball at (0.90, 0.00, 0.12) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz +0.02); touching cup_base
2.25 s: ball at (0.90, 0.00, 0.12) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.90, 0.00, 0.12) m, at rest; touching cup_base
</history>
