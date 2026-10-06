Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches ramp (first touch at 0.02 s)
- holds: ball touches cup (first touch at 1.32 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.28, 0.00, 0.33) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.02 s  ball first touches ramp
 1.19 s  ball leaves ramp
 1.32 s  ball first touches cup_bottom
 1.33 s  ball first touches floor
 1.34 s  ball leaves floor
 1.38 s  ball leaves cup_bottom
 1.41 s  ball touches cup_bottom again
 1.61 s  ball first touches cup_far_wall
 1.69 s  ball leaves cup_far_wall
 1.71 s  ball comes to rest at (0.77, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (-0.28, 0.00, 0.33) m, at rest; touching nothing
0.25 s: ball at (-0.25, 0.00, 0.32) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz -0.06); touching ramp
0.50 s: ball at (-0.16, 0.00, 0.30) m, moving 0.49 m/s (vx +0.48, vy -0.00, vz -0.10); touching ramp
0.75 s: ball at (-0.01, 0.00, 0.26) m, moving 0.74 m/s (vx +0.71, vy -0.00, vz -0.20); touching ramp
1.00 s: ball at (0.20, 0.00, 0.20) m, moving 0.98 m/s (vx +0.95, vy +0.00, vz -0.23); touching ramp
1.25 s: ball at (0.46, 0.00, 0.12) m, moving 1.42 m/s (vx +1.13, vy +0.00, vz -0.87); touching nothing
1.50 s: ball at (0.69, 0.00, 0.04) m, moving 0.75 m/s (vx +0.75, vy +0.00, vz +0.01); touching cup_bottom
1.75 s: ball at (0.77, 0.00, 0.04) m, at rest; touching cup_bottom
2.00 s: ball at (0.76, 0.00, 0.04) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.76, 0.00, 0.04) m, at rest; touching cup_bottom
</history>
