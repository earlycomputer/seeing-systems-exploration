MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.16, 0.00, 0.67) m, at rest

What happened, in order:
 0.00 s  ball starts touching ramp
 0.03 s  ball starts moving
 1.47 s  ball leaves ramp
 1.63 s  ball first touches cup_base
 1.65 s  ball leaves cup_base
 1.71 s  ball is at the top of its flight, at (2.30, 0.00, 0.08) m
 1.77 s  ball touches cup_base again
 1.78 s  ball leaves cup_base
 1.85 s  ball touches cup_base again
 1.86 s  ball leaves cup_base
 1.89 s  ball touches cup_base again
 1.90 s  ball leaves cup_base
 1.94 s  ball touches cup_base 2 more times between 1.94 s and 6.00 s, still touching at the end
 1.95 s  ball first touches cup_far_wall
 1.99 s  ball leaves cup_far_wall
 2.00 s  ball comes to rest at (2.60, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball at (0.16, 0.00, 0.67) m, at rest; touching ramp
0.25 s: ball at (0.21, 0.00, 0.66) m, moving 0.40 m/s (vx +0.39, vy +0.00, vz -0.09); touching ramp
0.50 s: ball at (0.35, 0.00, 0.63) m, moving 0.79 m/s (vx +0.77, vy +0.00, vz -0.19); touching ramp
0.75 s: ball at (0.59, 0.00, 0.57) m, moving 1.18 m/s (vx +1.15, vy +0.00, vz -0.29); touching nothing
1.00 s: ball at (0.93, 0.00, 0.49) m, moving 1.57 m/s (vx +1.53, vy +0.00, vz -0.36); touching ramp
1.25 s: ball at (1.36, 0.00, 0.39) m, moving 1.96 m/s (vx +1.91, vy +0.00, vz -0.45); touching ramp
1.50 s: ball at (1.88, 0.00, 0.26) m, moving 2.39 m/s (vx +2.24, vy +0.00, vz -0.85); touching nothing
1.75 s: ball at (2.36, 0.00, 0.07) m, moving 1.60 m/s (vx +1.55, vy +0.00, vz -0.39); touching nothing
2.00 s: ball at (2.60, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (2.60, 0.00, 0.06) m, at rest; touching cup_base
</history>
