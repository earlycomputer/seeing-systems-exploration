Your expectations, checked against the run (2 of 3 hold):

- holds: catapult_arm reaches its upper stop (at its upper stop (40°) at 0.15 s)
- holds: ball touches bucket (first touch at 0.97 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (2.64, -0.00, 0.04) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: catapult_arm_beam, catapult_arm.catapult_cup_outer, catapult_arm.catapult_cup_inner, catapult_arm.catapult_cup_side_left, catapult_arm.catapult_cup_side_right; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.35) m, at rest

What happened, in order:
 0.00 s  catapult_arm_beam starts touching ball
 0.00 s  catapult_arm starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.00 s  catapult_arm.catapult_cup_outer first touches ball
 0.15 s  catapult_arm_beam leaves ball
 0.15 s  catapult_arm reaches its upper stop (40°) moving +542°/s
 0.15 s  catapult_arm is at its largest, 40.5°
 0.15 s  catapult_arm.catapult_cup_outer leaves ball
 0.34 s  ball is at the top of its flight, at (0.83, 0.00, 0.85) m
 0.74 s  ball first touches floor
 0.79 s  ball leaves floor
 0.85 s  ball touches floor again
 0.96 s  ball leaves floor
 0.97 s  ball first touches bucket_wall_06
 0.98 s  ball leaves bucket_wall_06
 1.06 s  ball touches floor again
 1.07 s  ball comes to rest at (2.64, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (0.00, 0.00, 0.35) m, at rest; touching catapult_arm_beam
0.25 s: catapult_arm at 40.0°, still; touching nothing | ball at (0.52, 0.00, 0.81) m, moving 3.68 m/s (vx +3.58, vy -0.00, vz +0.85); touching nothing
0.50 s: catapult_arm at 40.0°, still; touching nothing | ball at (1.41, 0.00, 0.72) m, moving 3.92 m/s (vx +3.58, vy -0.00, vz -1.60); touching nothing
0.75 s: catapult_arm at 40.0°, still; touching nothing | ball at (2.30, 0.00, 0.03) m, moving 2.11 m/s (vx +2.07, vy -0.00, vz -0.40); touching floor
1.00 s: catapult_arm at 40.0°, still; touching nothing | ball at (2.66, 0.00, 0.05) m, moving 0.23 m/s (vx -0.19, vy +0.00, vz +0.13); touching nothing
1.25 s: catapult_arm at 40.0°, still; touching nothing | ball at (2.64, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult_arm at 40.0°, still; touching nothing
- ball at (2.64, 0.00, 0.04) m, at rest; touching floor
</history>
