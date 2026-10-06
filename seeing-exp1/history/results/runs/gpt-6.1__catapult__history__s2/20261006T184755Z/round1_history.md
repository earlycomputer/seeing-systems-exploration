MuJoCo ran the scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 55° as MuJoCo applies it; its geoms: catapult_arm.catapult_beam, catapult_arm.catapult_cup_floor, catapult_arm.catapult_cup_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.92, 0.00, 0.49) m, at rest

What happened, in order:
 0.00 s  catapult_arm.catapult_cup_floor starts touching ball
 0.00 s  catapult_arm starts at its lower stop (0°)
 0.01 s  ball starts moving
 0.25 s  catapult_arm.catapult_cup_back first touches ball
 0.53 s  catapult_arm reaches its upper stop (55°) moving +188°/s
 0.53 s  catapult_arm.catapult_cup_floor leaves ball
 0.54 s  catapult_arm.catapult_cup_back leaves ball
 0.55 s  catapult_arm is at its largest, 56.3°
 0.59 s  catapult_arm reaches its upper stop (55°) again moving -17°/s
 0.64 s  ball is at the top of its flight, at (-0.17, 0.00, 1.28) m
 1.14 s  ball first touches floor
 1.20 s  ball leaves floor
 1.27 s  ball touches floor again
 1.40 s  ball leaves floor
 1.40 s  ball first touches bucket_near
 1.45 s  ball leaves bucket_near
 1.49 s  ball touches floor again
 1.90 s  ball comes to rest at (1.49, 0.00, 0.06) m

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.92, 0.00, 0.49) m, at rest; touching catapult_arm.catapult_cup_floor
0.25 s: catapult_arm at 13.7°, turning +103°/s; touching ball | ball at (-0.89, 0.00, 0.71) m, moving 1.69 m/s (vx +0.43, vy +0.00, vz +1.64); touching catapult_arm.catapult_cup_back, catapult_arm.catapult_cup_floor
0.50 s: catapult_arm at 49.3°, turning +180°/s; touching ball | ball at (-0.55, 0.00, 1.17) m, moving 2.97 m/s (vx +2.41, vy -0.00, vz +1.72); touching catapult_arm.catapult_cup_back, catapult_arm.catapult_cup_floor
0.75 s: catapult_arm at 55.0°, still; touching nothing | ball at (0.11, 0.00, 1.23) m, moving 2.84 m/s (vx +2.63, vy -0.00, vz -1.06); touching nothing
1.00 s: catapult_arm at 55.0°, still; touching nothing | ball at (0.76, 0.00, 0.66) m, moving 4.39 m/s (vx +2.63, vy -0.00, vz -3.51); touching nothing
1.25 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.31, 0.00, 0.07) m, moving 1.47 m/s (vx +1.46, vy +0.00, vz -0.13); touching nothing
1.50 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.52, 0.00, 0.06) m, moving 0.16 m/s (vx -0.13, vy +0.00, vz -0.09); touching floor
1.75 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.50, 0.00, 0.06) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching floor
2.00 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.49, 0.00, 0.06) m, at rest; touching floor
2.25 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.48, 0.00, 0.06) m, at rest; touching floor
2.50 s: catapult_arm at 55.0°, still; touching nothing | ball at (1.47, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult_arm at 55.0°, still; touching nothing
- ball at (1.47, 0.00, 0.06) m, at rest; touching floor
</history>
