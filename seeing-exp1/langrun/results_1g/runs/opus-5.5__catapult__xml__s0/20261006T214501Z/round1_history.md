Your expectations, checked against the run (3 of 4 hold):

- holds: ball touches catapult_beam (touching from the start)
- holds: catapult_arm reaches its upper stop (at its upper stop (45°) at 0.15 s)
- holds: ball touches bucket (first touch at 0.94 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball is still moving at the end (0.06 m/s), outside bucket)

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
 0.25 s  ball is at the top of its flight, at (0.17, 0.00, 0.89) m
 0.67 s  ball first touches floor
 0.94 s  ball leaves floor
 0.94 s  ball first touches bucket_bottom
 0.94 s  ball first touches bucket_wall4
 0.97 s  ball leaves bucket_bottom
 1.01 s  ball leaves bucket_wall4
 1.10 s  ball touches floor again
 6.00 s  ball is still moving at the end, 0.06 m/s

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (-0.50, 0.00, 0.45) m, at rest; touching catapult_arm.catapult_beam
0.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (0.16, 0.00, 0.89) m, moving 3.70 m/s (vx +3.70, vy -0.00, vz +0.03); touching nothing
0.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.08, 0.00, 0.60) m, moving 4.43 m/s (vx +3.70, vy -0.00, vz -2.43); touching nothing
0.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.86, 0.00, 0.04) m, moving 1.64 m/s (vx +1.62, vy -0.00, vz +0.22); touching floor
1.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.18, 0.00, 0.06) m, moving 0.32 m/s (vx -0.22, vy -0.00, vz +0.24); touching bucket_wall4
1.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.15, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
1.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.13, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
1.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.12, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
2.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.10, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
2.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.09, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
2.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.07, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
2.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.06, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
3.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.04, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
3.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.03, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
3.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.01, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
3.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (2.00, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
4.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.98, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
4.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.96, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
4.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.95, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
4.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.93, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
5.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.92, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
5.25 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.90, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
5.50 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.89, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
5.75 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.87, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
6.00 s: catapult_arm at 45.1°, still; touching nothing | ball at (1.86, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor

At the end (6.00 s):
- catapult_arm at 45.1°, still; touching nothing
- ball at (1.86, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor
</history>
