MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.11, 0.00, 0.52) m, at rest

What happened, in order:
 0.00 s  ball first touches ramp
 0.03 s  ball starts moving
 1.34 s  ball leaves ramp
 1.45 s  ball first touches cup_base
 1.46 s  ball leaves cup_base
 1.52 s  ball is at the top of its flight, at (1.83, 0.00, 0.08) m
 1.58 s  ball touches cup_base again
 1.58 s  ball leaves cup_base
 1.64 s  ball touches cup_base again
 1.65 s  ball leaves cup_base
 1.69 s  ball touches cup_base again
 1.69 s  ball leaves cup_base
 1.73 s  ball touches cup_base 1 more times between 1.73 s and 6.00 s, still touching at the end
 1.81 s  ball first touches cup_far_wall
 1.81 s  ball comes to rest at (2.10, 0.00, 0.06) m
 2.47 s  ball leaves cup_far_wall

State every 0.25 s:
0.00 s: ball at (0.11, 0.00, 0.52) m, at rest; touching nothing
0.25 s: ball at (0.16, 0.00, 0.51) m, moving 0.41 m/s (vx +0.40, vy +0.00, vz -0.10); touching ramp
0.50 s: ball at (0.31, 0.00, 0.47) m, moving 0.80 m/s (vx +0.78, vy +0.00, vz -0.19); touching ramp
0.75 s: ball at (0.55, 0.00, 0.41) m, moving 1.20 m/s (vx +1.16, vy -0.00, vz -0.30); touching nothing
1.00 s: ball at (0.89, 0.00, 0.33) m, moving 1.60 m/s (vx +1.54, vy -0.00, vz -0.42); touching nothing
1.25 s: ball at (1.32, 0.00, 0.22) m, moving 1.99 m/s (vx +1.93, vy -0.00, vz -0.49); touching nothing
1.50 s: ball at (1.80, 0.00, 0.07) m, moving 1.44 m/s (vx +1.43, vy -0.00, vz +0.18); touching nothing
1.75 s: ball at (2.07, 0.00, 0.06) m, moving 0.60 m/s (vx +0.60, vy -0.00, vz +0.02); touching nothing
2.00 s: ball at (2.10, 0.00, 0.06) m, at rest; touching cup_base, cup_far_wall
(the same through 2.25 s)
2.50 s: ball at (2.10, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball at (2.10, 0.00, 0.06) m, at rest; touching cup_base
</history>
