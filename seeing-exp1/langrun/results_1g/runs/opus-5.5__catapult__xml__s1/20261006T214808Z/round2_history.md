Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches catapult_arm_beam (touching from the start)
- holds: ball touches bucket_bottom (first touch at 0.97 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 38.16° as MuJoCo applies it; its geoms: catapult_arm_beam, catapult_arm.catapult_cup_outer, catapult_arm.catapult_cup_inner; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.50, 0.00, 0.46) m, at rest

What happened, in order:
 0.00 s  catapult_arm_beam starts touching ball
 0.00 s  catapult_arm starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.01 s  catapult_arm.catapult_cup_outer first touches ball
 0.09 s  catapult_arm is at its largest, 38.7°
 0.09 s  catapult_arm_beam leaves ball
 0.09 s  catapult_arm.catapult_cup_outer leaves ball
 0.09 s  catapult_arm reaches its upper stop (38.16°) moving +564°/s
 0.45 s  ball is at the top of its flight, at (0.89, 0.00, 1.38) m
 0.95 s  ball first touches bucket_wall0
 0.97 s  ball first touches bucket_bottom
 0.97 s  ball leaves bucket_wall0
 1.01 s  ball leaves bucket_bottom
 1.08 s  ball touches bucket_bottom again
 1.27 s  ball leaves bucket_bottom
 1.27 s  ball first touches bucket_wall6
 1.31 s  ball leaves bucket_wall6
 1.33 s  ball touches bucket_bottom again
 1.40 s  ball comes to rest at (2.35, 0.00, 0.06) m

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.50, 0.00, 0.46) m, at rest; touching catapult_arm_beam
0.25 s: catapult_arm at 38.2°, still; touching nothing | ball at (0.21, 0.00, 1.19) m, moving 3.99 m/s (vx +3.50, vy +0.00, vz +1.91); touching nothing
0.50 s: catapult_arm at 38.2°, still; touching nothing | ball at (1.08, 0.00, 1.37) m, moving 3.55 m/s (vx +3.50, vy +0.00, vz -0.54); touching nothing
0.75 s: catapult_arm at 38.2°, still; touching nothing | ball at (1.96, 0.00, 0.93) m, moving 4.61 m/s (vx +3.50, vy +0.00, vz -2.99); touching nothing
1.00 s: catapult_arm at 38.2°, still; touching nothing | ball at (2.63, 0.00, 0.05) m, moving 1.18 m/s (vx -1.09, vy +0.00, vz +0.45); touching bucket_bottom
1.25 s: catapult_arm at 38.2°, still; touching nothing | ball at (2.36, 0.00, 0.06) m, moving 1.01 m/s (vx -1.01, vy +0.00, vz +0.04); touching bucket_bottom
1.50 s: catapult_arm at 38.2°, still; touching nothing | ball at (2.35, 0.00, 0.06) m, at rest; touching bucket_bottom
(the same through 6.00 s)

At the end (6.00 s):
- catapult_arm at 38.2°, still; touching nothing
- ball at (2.35, 0.00, 0.06) m, at rest; touching bucket_bottom
</history>
