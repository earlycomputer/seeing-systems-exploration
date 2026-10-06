Your expectations, checked against the run (3 of 3 hold):

- holds: catapult_arm reaches its upper stop (at its upper stop (45°) at 0.13 s)
- holds: ball touches bucket_floor (first touch at 0.95 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: catapult_arm.catapult_beam, catapult_arm.catapult_cup_outer, catapult_arm.catapult_cup_inner, catapult_arm.catapult_cup_side_left, catapult_arm.catapult_cup_side_right; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.60, 0.00, 0.45) m, at rest

What happened, in order:
 0.00 s  catapult_arm.catapult_beam starts touching ball
 0.00 s  catapult_arm starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.02 s  catapult_arm.catapult_cup_outer first touches ball
 0.13 s  catapult_arm reaches its upper stop (45°) moving +447°/s
 0.13 s  catapult_arm.catapult_beam leaves ball
 0.13 s  catapult_arm is at its largest, 46.2°
 0.13 s  catapult_arm.catapult_cup_outer leaves ball
 0.14 s  catapult_arm reaches its upper stop (45°) again moving -76°/s
 0.44 s  ball is at the top of its flight, at (0.73, 0.00, 1.33) m
 0.95 s  ball first touches bucket_floor
 0.95 s  ball first touches floor
 0.99 s  ball leaves floor
 0.99 s  ball first touches bucket_wall_far
 1.01 s  ball leaves bucket_floor
 1.06 s  ball leaves bucket_wall_far
 1.13 s  ball is at the top of its flight, at (2.64, 0.00, 0.13) m
 1.25 s  ball touches bucket_floor again
 2.09 s  ball touches bucket_wall_far again
 2.09 s  ball comes to rest at (2.66, 0.00, 0.06) m
 2.17 s  ball leaves bucket_wall_far

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.60, 0.00, 0.45) m, at rest; touching catapult_arm.catapult_beam
0.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (0.05, 0.00, 1.16) m, moving 4.05 m/s (vx +3.61, vy -0.00, vz +1.83); touching nothing
0.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (0.95, 0.00, 1.31) m, moving 3.66 m/s (vx +3.61, vy -0.00, vz -0.62); touching nothing
0.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.85, 0.00, 0.85) m, moving 4.74 m/s (vx +3.61, vy -0.00, vz -3.08); touching nothing
1.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.67, 0.00, 0.05) m, moving 1.20 m/s (vx +0.46, vy -0.00, vz +1.11); touching bucket_floor, bucket_wall_far
1.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.60, 0.00, 0.06) m, moving 1.20 m/s (vx -0.31, vy -0.00, vz -1.16); touching nothing
1.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.62, 0.00, 0.06) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz +0.00); touching bucket_floor
1.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.64, 0.00, 0.06) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz +0.00); touching bucket_floor
2.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.65, 0.00, 0.06) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz +0.00); touching bucket_floor
2.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.66, 0.00, 0.06) m, at rest; touching bucket_floor
(the same through 2.75 s)
3.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.65, 0.00, 0.06) m, at rest; touching bucket_floor
(the same through 4.50 s)
4.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.64, 0.00, 0.06) m, at rest; touching bucket_floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult_arm at 45.0°, still; touching nothing
- ball at (2.64, 0.00, 0.06) m, at rest; touching bucket_floor
</history>
