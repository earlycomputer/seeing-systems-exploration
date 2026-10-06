Your expectations, checked against the run (2 of 3 hold):

- holds: catapult_arm reaches its upper stop (at its upper stop (45°) at 0.13 s)
- holds: ball touches bucket_floor (first touch at 1.18 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball is still moving at the end (0.05 m/s), outside bucket)

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
 0.14 s  catapult_arm.catapult_cup_outer leaves ball
 0.14 s  catapult_arm reaches its upper stop (45°) again moving -76°/s
 0.19 s  ball is at the top of its flight, at (-0.18, 0.00, 0.89) m
 0.61 s  ball first touches floor
 1.17 s  ball leaves floor
 1.17 s  ball first touches bucket_wall_near
 1.18 s  ball first touches bucket_floor
 1.19 s  ball leaves bucket_floor
 1.23 s  ball leaves bucket_wall_near
 1.25 s  ball touches floor again
 5.99 s  ball comes to rest at (1.62, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.60, 0.00, 0.45) m, at rest; touching catapult_arm.catapult_beam
0.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (0.04, 0.00, 0.88) m, moving 3.65 m/s (vx +3.60, vy -0.00, vz -0.59); touching nothing
0.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (0.94, 0.00, 0.42) m, moving 4.72 m/s (vx +3.60, vy -0.00, vz -3.05); touching nothing
0.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.52, 0.00, 0.04) m, moving 1.27 m/s (vx +1.27, vy +0.00, vz -0.01); touching floor
1.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.84, 0.00, 0.04) m, moving 1.23 m/s (vx +1.23, vy -0.00, vz -0.00); touching floor
1.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.04, 0.00, 0.04) m, moving 0.38 m/s (vx -0.20, vy -0.00, vz -0.32); touching nothing
1.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.00, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz +0.00); touching floor
1.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.97, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz +0.00); touching floor
2.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.94, 0.00, 0.04) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor
2.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.91, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy -0.00, vz +0.00); touching floor
2.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.88, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy -0.00, vz +0.00); touching floor
2.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.86, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
3.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.83, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
3.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.81, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz +0.00); touching floor
3.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.79, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz +0.00); touching floor
3.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.76, 0.00, 0.04) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz +0.00); touching floor
4.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.74, 0.00, 0.04) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz +0.00); touching floor
4.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.73, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz +0.00); touching floor
4.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.71, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz +0.00); touching floor
4.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.69, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz +0.00); touching floor
5.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.68, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
5.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.66, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
5.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.65, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
5.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.63, 0.00, 0.04) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching floor
6.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.62, 0.00, 0.04) m, at rest; touching floor

At the end (6.00 s):
- catapult_arm at 45.0°, still; touching nothing
- ball at (1.62, 0.00, 0.04) m, at rest; touching floor
</history>
