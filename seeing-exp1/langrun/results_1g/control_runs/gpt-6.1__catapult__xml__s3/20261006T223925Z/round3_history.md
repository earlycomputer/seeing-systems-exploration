MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult_arm: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range -2° to 45° as MuJoCo applies it; its geoms: catapult_arm_beam, catapult_arm.catapult_spoon_bottom, catapult_arm.catapult_spoon_outer_lip, catapult_arm.catapult_spoon_left_lip, catapult_arm.catapult_spoon_right_lip; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.40) m, at rest

What happened, in order:
 0.00 s  catapult_arm.catapult_spoon_bottom starts touching ball
 0.01 s  ball starts moving
 0.15 s  catapult_arm.catapult_spoon_outer_lip first touches ball
 0.37 s  catapult_arm reaches its upper stop (45°) moving +247°/s
 0.37 s  catapult_arm is at its largest, 45.2°
 0.37 s  catapult_arm.catapult_spoon_bottom leaves ball
 0.37 s  catapult_arm.catapult_spoon_outer_lip leaves ball
 0.65 s  ball is at the top of its flight, at (1.36, 0.00, 1.47) m
 1.17 s  ball first touches bucket_bottom
 1.19 s  ball leaves bucket_bottom
 1.26 s  ball is at the top of its flight, at (3.30, 0.00, 0.18) m
 1.32 s  ball touches bucket_bottom again
 1.33 s  ball leaves bucket_bottom
 1.38 s  ball touches bucket_bottom again
 1.38 s  ball leaves bucket_bottom
 1.42 s  ball touches bucket_bottom again
 1.43 s  ball leaves bucket_bottom
 1.47 s  ball touches bucket_bottom 1 more times between 1.47 s and 6.00 s, still touching at the end
 1.59 s  ball first touches bucket_far_wall
 1.60 s  ball comes to rest at (3.60, 0.00, 0.16) m
 2.15 s  ball leaves bucket_far_wall

State every 0.25 s:
0.00 s: catapult_arm at 0.0°, still; touching ball | ball at (0.00, 0.00, 0.40) m, at rest; touching catapult_arm.catapult_spoon_bottom
0.25 s: catapult_arm at 20.3°, turning +160°/s; touching ball | ball at (0.09, 0.00, 0.74) m, moving 2.88 m/s (vx +1.32, vy +0.00, vz +2.56); touching catapult_arm.catapult_spoon_bottom, catapult_arm.catapult_spoon_outer_lip
0.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (0.82, 0.00, 1.35) m, moving 3.84 m/s (vx +3.53, vy +0.00, vz +1.49); touching nothing
0.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (1.70, 0.00, 1.42) m, moving 3.66 m/s (vx +3.53, vy +0.00, vz -0.96); touching nothing
1.00 s: catapult_arm at 45.0°, still; touching nothing | ball at (2.59, 0.00, 0.88) m, moving 4.91 m/s (vx +3.53, vy +0.00, vz -3.41); touching nothing
1.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (3.29, 0.00, 0.18) m, moving 1.27 m/s (vx +1.27, vy -0.00, vz +0.04); touching nothing
1.50 s: catapult_arm at 45.0°, still; touching nothing | ball at (3.55, 0.00, 0.16) m, moving 0.71 m/s (vx +0.71, vy -0.00, vz +0.03); touching nothing
1.75 s: catapult_arm at 45.0°, still; touching nothing | ball at (3.60, 0.00, 0.16) m, at rest; touching bucket_bottom, bucket_far_wall
(the same through 2.00 s)
2.25 s: catapult_arm at 45.0°, still; touching nothing | ball at (3.60, 0.00, 0.16) m, at rest; touching bucket_bottom
(the same through 6.00 s)

At the end (6.00 s):
- catapult_arm at 45.0°, still; touching nothing
- ball at (3.60, 0.00, 0.16) m, at rest; touching bucket_bottom
</history>
