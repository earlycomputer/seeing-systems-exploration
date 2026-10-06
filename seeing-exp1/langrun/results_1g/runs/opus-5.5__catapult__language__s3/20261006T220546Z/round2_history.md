Your expectations, checked against the run (1 of 1 hold):

- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 35° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.36, 0.00, 0.57) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_base starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.00 s  catapult_scoop_back first touches ball
 0.07 s  catapult reaches its upper stop (35°) moving +870°/s
 0.07 s  catapult_scoop_base leaves ball
 0.09 s  catapult_scoop_back leaves ball
 0.09 s  catapult is at its largest, 41.8°
 0.20 s  catapult reaches its upper stop (35°) again moving -8°/s
 0.31 s  ball is at the top of its flight, at (0.73, 0.00, 1.06) m
 0.76 s  ball first touches bucket_base
 0.81 s  ball leaves bucket_base
 0.89 s  ball touches bucket_base again
 0.91 s  ball leaves bucket_base
 0.95 s  ball touches bucket_base again
 1.01 s  ball leaves bucket_base
 1.01 s  ball first touches bucket_far_wall
 1.06 s  ball leaves bucket_far_wall
 1.11 s  ball touches bucket_base again
 1.23 s  ball comes to rest at (3.07, 0.00, 0.06) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.36, 0.00, 0.57) m, at rest; touching catapult_scoop_base
0.25 s: catapult at 35.3°, turning -1°/s; touching nothing | ball at (0.48, 0.00, 1.04) m, moving 4.22 m/s (vx +4.18, vy +0.00, vz +0.58); touching nothing
0.50 s: catapult at 35.3°, still; touching nothing | ball at (1.52, 0.00, 0.88) m, moving 4.58 m/s (vx +4.18, vy +0.00, vz -1.88); touching nothing
0.75 s: catapult at 35.3°, still; touching nothing | ball at (2.57, 0.00, 0.11) m, moving 6.02 m/s (vx +4.18, vy +0.00, vz -4.33); touching nothing
1.00 s: catapult at 35.3°, still; touching nothing | ball at (3.07, 0.00, 0.06) m, moving 1.83 m/s (vx +1.83, vy +0.00, vz -0.06); touching nothing
1.25 s: catapult at 35.3°, still; touching nothing | ball at (3.07, 0.00, 0.06) m, at rest; touching bucket_base
1.50 s: catapult at 35.3°, still; touching nothing | ball at (3.06, 0.00, 0.06) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 35.3°, still; touching nothing
- ball at (3.06, 0.00, 0.06) m, at rest; touching bucket_base
</history>
