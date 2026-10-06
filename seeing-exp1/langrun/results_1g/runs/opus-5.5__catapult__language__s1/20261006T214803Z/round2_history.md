Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches catapult (touching from the start)
- holds: ball touches bucket (first touch at 0.84 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 36° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.46, 0.00, 0.57) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_back starts touching ball
 0.00 s  catapult_scoop_base starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.09 s  catapult reaches its upper stop (36°) moving +695°/s
 0.09 s  catapult_scoop_base leaves ball
 0.11 s  catapult_scoop_back leaves ball
 0.11 s  catapult is at its largest, 40.5°
 0.20 s  catapult reaches its upper stop (36°) again moving -14°/s
 0.36 s  ball is at the top of its flight, at (0.79, 0.00, 1.19) m
 0.84 s  ball first touches bucket_base
 0.85 s  ball first touches floor
 0.86 s  ball leaves floor
 0.89 s  ball leaves bucket_base
 0.92 s  ball first touches bucket_far_wall
 0.97 s  ball leaves bucket_far_wall
 1.00 s  ball is at the top of its flight, at (2.98, 0.00, 0.10) m
 1.09 s  ball touches bucket_base again
 1.15 s  ball comes to rest at (2.95, 0.00, 0.06) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.46, 0.00, 0.57) m, at rest; touching catapult_scoop_back, catapult_scoop_base
0.25 s: catapult at 36.2°, turning -2°/s; touching nothing | ball at (0.32, 0.00, 1.13) m, moving 4.37 m/s (vx +4.24, vy -0.00, vz +1.07); touching nothing
0.50 s: catapult at 36.1°, still; touching nothing | ball at (1.38, 0.00, 1.09) m, moving 4.46 m/s (vx +4.24, vy -0.00, vz -1.38); touching nothing
0.75 s: catapult at 36.1°, still; touching nothing | ball at (2.44, 0.00, 0.44) m, moving 5.72 m/s (vx +4.24, vy -0.00, vz -3.84); touching nothing
1.00 s: catapult at 36.1°, still; touching nothing | ball at (2.98, 0.00, 0.10) m, moving 0.32 m/s (vx -0.32, vy -0.00, vz +0.01); touching nothing
1.25 s: catapult at 36.1°, still; touching nothing | ball at (2.95, 0.00, 0.06) m, at rest; touching bucket_base
1.50 s: catapult at 36.1°, still; touching nothing | ball at (2.94, 0.00, 0.06) m, at rest; touching bucket_base
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 36.1°, still; touching nothing
- ball at (2.94, 0.00, 0.06) m, at rest; touching bucket_base
</history>
