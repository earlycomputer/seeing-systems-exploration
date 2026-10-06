Your expectations, checked against the run (4 of 4 hold):

- holds: ball touches catapult_beam (touching from the start)
- holds: catapult_arm reaches its upper stop (at its upper stop (45°) at 0.15 s)
- holds: ball touches bucket (first touch at 0.95 s)
- holds: ball comes to rest in bucket (ball at rest inside bucket at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: catapult_arm.catapult_beam, catapult_arm.catapult_lip, catapult_arm.catapult_axle; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.50, 0.00, 0.45) m, at rest

What happened, in order:
 0.00 s  catapult_arm.catapult_beam starts touching ball
 0.00 s  catapult_arm starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.00 s  catapult_arm.catapult_lip first touches ball
 0.12 s  catapult_arm.catapult_beam leaves ball
 0.13 s  catapult_arm is at its largest, 46.7°
 0.13 s  catapult_arm.catapult_lip leaves ball
 0.15 s  catapult_arm reaches its upper stop (45°) moving -33°/s
 0.45 s  ball is at the top of its flight, at (0.90, 0.00, 1.32) m
 0.95 s  ball first touches bucket_bottom
 0.96 s  ball first touches floor
 0.96 s  ball first touches bucket_wall0
 0.99 s  ball leaves floor
 1.03 s  ball leaves bucket_bottom
 1.04 s  ball leaves bucket_wall0
 1.10 s  ball touches bucket_bottom again
 4.44 s  ball first touches bucket_wall4
 4.45 s  ball comes to rest at (2.18, 0.00, 0.06) m
 4.52 s  ball leaves bucket_wall4

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.50, 0.00, 0.45) m, at rest; touching catapult_arm.catapult_beam
0.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (0.16, 0.00, 1.13) m, moving 4.20 m/s (vx +3.74, vy -0.00, vz +1.91); touching nothing
0.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.10, 0.00, 1.31) m, moving 3.78 m/s (vx +3.74, vy -0.00, vz -0.54); touching nothing
0.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.03, 0.00, 0.87) m, moving 4.79 m/s (vx +3.74, vy -0.00, vz -2.99); touching nothing
1.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.84, 0.00, 0.04) m, moving 0.73 m/s (vx -0.38, vy -0.00, vz +0.62); touching bucket_bottom, bucket_wall0
1.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.76, 0.00, 0.06) m, moving 0.24 m/s (vx -0.24, vy -0.00, vz +0.00); touching bucket_bottom
1.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.70, 0.00, 0.06) m, moving 0.23 m/s (vx -0.23, vy -0.00, vz -0.00); touching bucket_bottom
1.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.64, 0.00, 0.06) m, moving 0.22 m/s (vx -0.22, vy -0.00, vz -0.00); touching bucket_bottom
2.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.59, 0.00, 0.06) m, moving 0.21 m/s (vx -0.21, vy -0.00, vz -0.00); touching bucket_bottom
2.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.54, 0.00, 0.06) m, moving 0.20 m/s (vx -0.20, vy -0.00, vz -0.00); touching bucket_bottom
2.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.49, 0.00, 0.06) m, moving 0.19 m/s (vx -0.19, vy -0.00, vz -0.00); touching bucket_bottom
2.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.44, 0.00, 0.06) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz -0.00); touching bucket_bottom
3.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.40, 0.00, 0.06) m, moving 0.17 m/s (vx -0.17, vy -0.00, vz -0.00); touching bucket_bottom
3.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.35, 0.00, 0.06) m, moving 0.17 m/s (vx -0.17, vy -0.00, vz -0.00); touching bucket_bottom
3.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.31, 0.00, 0.06) m, moving 0.16 m/s (vx -0.16, vy -0.00, vz -0.00); touching bucket_bottom
3.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.28, 0.00, 0.06) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz -0.00); touching bucket_bottom
4.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.24, 0.00, 0.06) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz -0.00); touching bucket_bottom
4.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.20, 0.00, 0.06) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching bucket_bottom
4.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.18, 0.00, 0.06) m, at rest; touching bucket_bottom, bucket_wall4
4.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.18, 0.00, 0.06) m, at rest; touching bucket_bottom
5.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.19, 0.00, 0.06) m, at rest; touching bucket_bottom
(the same through 5.75 s)
6.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.20, 0.00, 0.06) m, at rest; touching bucket_bottom

At the end (6.00 s):
- catapult_arm at 45.1°, still; touching nothing
- ball at (2.20, 0.00, 0.06) m, at rest; touching bucket_bottom
</history>
