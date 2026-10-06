Your expectations, checked against the run (2 of 3 hold):

- holds: ball touches catapult (touching from the start)
- holds: ball touches bucket (first touch at 0.78 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (0.62, -0.00, 0.04) m, outside bucket)

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
 0.11 s  catapult_scoop_base leaves ball
 0.12 s  catapult_scoop_back leaves ball
 0.13 s  catapult is at its largest, 40.2°
 0.21 s  catapult reaches its upper stop (36°) moving -16°/s
 0.34 s  ball is at the top of its flight, at (0.52, 0.00, 1.10) m
 0.78 s  ball first touches bucket_near_wall
 0.81 s  ball first touches floor
 0.82 s  ball leaves bucket_near_wall
 0.88 s  ball leaves floor
 0.94 s  ball touches floor again
 3.05 s  ball comes to rest at (0.62, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.46, 0.00, 0.57) m, at rest; touching catapult_scoop_back, catapult_scoop_base
0.25 s: catapult at 36.2°, turning -3°/s; touching nothing | ball at (0.18, 0.00, 1.06) m, moving 3.81 m/s (vx +3.71, vy -0.00, vz +0.87); touching nothing
0.50 s: catapult at 36.1°, still; touching nothing | ball at (1.11, 0.00, 0.98) m, moving 4.03 m/s (vx +3.71, vy -0.00, vz -1.58); touching nothing
0.75 s: catapult at 36.1°, still; touching nothing | ball at (2.04, 0.00, 0.28) m, moving 5.48 m/s (vx +3.71, vy -0.00, vz -4.03); touching nothing
1.00 s: catapult at 36.1°, still; touching nothing | ball at (1.92, 0.00, 0.04) m, moving 1.25 m/s (vx -1.25, vy -0.00, vz -0.02); touching floor
1.25 s: catapult at 36.1°, still; touching nothing | ball at (1.62, 0.00, 0.04) m, moving 1.14 m/s (vx -1.14, vy -0.00, vz -0.01); touching floor
1.50 s: catapult at 36.1°, still; touching nothing | ball at (1.35, 0.00, 0.04) m, moving 0.97 m/s (vx -0.97, vy -0.00, vz +0.02); touching floor
1.75 s: catapult at 36.1°, still; touching nothing | ball at (1.13, 0.00, 0.04) m, moving 0.80 m/s (vx -0.80, vy -0.00, vz +0.01); touching floor
2.00 s: catapult at 36.1°, still; touching nothing | ball at (0.95, 0.00, 0.04) m, moving 0.64 m/s (vx -0.64, vy -0.00, vz -0.00); touching floor
2.25 s: catapult at 36.1°, still; touching nothing | ball at (0.81, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy -0.00, vz +0.00); touching floor
2.50 s: catapult at 36.1°, still; touching nothing | ball at (0.71, 0.00, 0.04) m, moving 0.31 m/s (vx -0.31, vy -0.00, vz -0.00); touching floor
2.75 s: catapult at 36.1°, still; touching nothing | ball at (0.65, 0.00, 0.04) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz -0.00); touching floor
3.00 s: catapult at 36.1°, still; touching nothing | ball at (0.63, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
3.25 s: catapult at 36.1°, still; touching nothing | ball at (0.62, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 36.1°, still; touching nothing
- ball at (0.62, 0.00, 0.04) m, at rest; touching floor
</history>
