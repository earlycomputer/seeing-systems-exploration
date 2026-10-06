MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (-0.90, 0.00, 0.88) m, at rest

What happened, in order:
 0.01 s  ball starts moving
 0.01 s  ball first touches ramp_surface
 1.04 s  ball leaves ramp_surface
 1.30 s  ball first touches cup_bottom
 1.33 s  ball leaves cup_bottom
 1.38 s  ball touches cup_bottom again
 1.40 s  ball comes to rest at (0.58, 0.00, 0.13) m

State every 0.25 s:
0.00 s: ball at (-0.90, 0.00, 0.88) m, at rest; touching nothing
0.25 s: ball at (-0.84, 0.00, 0.86) m, moving 0.47 m/s (vx +0.45, vy +0.00, vz -0.13); touching ramp_surface
0.50 s: ball at (-0.68, 0.00, 0.81) m, moving 0.93 m/s (vx +0.90, vy +0.00, vz -0.26); touching ramp_surface
0.75 s: ball at (-0.40, 0.00, 0.73) m, moving 1.40 m/s (vx +1.34, vy +0.00, vz -0.38); touching ramp_surface
1.00 s: ball at (-0.01, 0.00, 0.62) m, moving 1.86 m/s (vx +1.79, vy +0.00, vz -0.54); touching nothing
1.25 s: ball at (0.46, 0.00, 0.28) m, moving 3.18 m/s (vx +1.87, vy +0.00, vz -2.58); touching nothing
1.50 s: ball at (0.58, 0.00, 0.13) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.58, 0.00, 0.13) m, at rest; touching cup_bottom
</history>
