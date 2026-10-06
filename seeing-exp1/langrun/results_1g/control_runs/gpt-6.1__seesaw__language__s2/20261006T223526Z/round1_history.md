MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range 0° to 35° as MuJoCo applies it; its geoms: seesaw; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.52, 0.00, 0.85) m, at rest
- weight: free body; its geoms: weight; starts at (0.52, 0.00, 3.00) m, at rest

What happened, in order:
 0.00 s  seesaw starts touching ball
 0.00 s  seesaw starts at its lower stop (0°)
 0.01 s  weight starts moving
 0.66 s  seesaw first touches weight
 0.66 s  ball starts moving
 0.67 s  weight passes 0.44 m from axle without touching it: nearest points (0.45, 0.00, 0.81) m and (0.01, 0.00, 0.80) m
 0.69 s  seesaw leaves weight
 0.71 s  seesaw leaves ball
 0.72 s  seesaw reaches its upper stop (35°) moving +587°/s
 0.73 s  weight passes 0.42 m from left bearing without touching it: nearest points (0.45, 0.02, 0.50) m and (0.04, 0.14, 0.50) m
 0.73 s  weight passes 0.42 m from right bearing without touching it: nearest points (0.45, -0.02, 0.50) m and (0.04, -0.14, 0.50) m
 0.73 s  seesaw touches weight again
 0.74 s  seesaw is at its largest, 39.6°
 0.75 s  seesaw leaves weight
 0.80 s  seesaw reaches its upper stop (35°) again moving -85°/s
 0.88 s  weight first touches floor
 1.21 s  seesaw reaches its lower stop (0°) again moving -84°/s
 1.24 s  seesaw is at its smallest, -0.6°
 1.25 s  seesaw reaches its lower stop (0°) again moving +10°/s
 1.37 s  ball is at the top of its flight, at (0.34, 0.00, 3.25) m
 2.17 s  ball first touches floor
 2.24 s  ball leaves floor
 2.33 s  ball touches floor again
 3.13 s  ball comes to rest at (1.48, 0.00, 0.04) m
 4.60 s  seesaw reaches its upper stop (35°) again moving +10°/s
 6.00 s  weight is still moving at the end, 1.06 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | ball at (-0.52, 0.00, 0.85) m, at rest; touching seesaw | weight at (0.52, 0.00, 3.00) m, at rest; touching nothing
0.25 s: seesaw at -0.0°, still; touching ball | ball at (-0.52, 0.00, 0.85) m, at rest; touching seesaw | weight at (0.52, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at -0.0°, still; touching ball | ball at (-0.52, 0.00, 0.85) m, at rest; touching seesaw | weight at (0.52, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at 39.3°, turning -54°/s; touching weight | ball at (-0.44, 0.00, 1.39) m, moving 6.16 m/s (vx +1.27, vy +0.00, vz +6.03); touching nothing | weight at (0.54, 0.00, 0.44) m, moving 2.89 m/s (vx +1.80, vy -0.00, vz -2.26); touching seesaw
1.00 s: seesaw at 18.2°, turning -84°/s; touching nothing | ball at (-0.12, 0.00, 2.59) m, moving 3.79 m/s (vx +1.27, vy +0.00, vz +3.57); touching nothing | weight at (1.01, 0.00, 0.07) m, moving 2.01 m/s (vx +2.01, vy +0.00, vz +0.01); touching nothing
1.25 s: seesaw at -0.5°, turning +11°/s; touching nothing | ball at (0.19, 0.00, 3.18) m, moving 1.70 m/s (vx +1.27, vy +0.00, vz +1.12); touching nothing | weight at (1.51, 0.00, 0.07) m, moving 1.99 m/s (vx +1.99, vy +0.00, vz +0.00); touching floor
1.50 s: seesaw at 2.3°, turning +11°/s; touching nothing | ball at (0.51, 0.00, 3.16) m, moving 1.84 m/s (vx +1.27, vy +0.00, vz -1.33); touching nothing | weight at (2.00, 0.00, 0.07) m, moving 1.94 m/s (vx +1.94, vy +0.00, vz -0.00); touching floor
1.75 s: seesaw at 5.1°, turning +11°/s; touching nothing | ball at (0.83, 0.00, 2.52) m, moving 3.99 m/s (vx +1.27, vy +0.00, vz -3.78); touching nothing | weight at (2.48, 0.00, 0.07) m, moving 1.89 m/s (vx +1.89, vy +0.00, vz +0.01); touching floor
2.00 s: seesaw at 7.8°, turning +11°/s; touching nothing | ball at (1.15, 0.00, 1.27) m, moving 6.36 m/s (vx +1.27, vy +0.00, vz -6.24); touching nothing | weight at (2.95, 0.00, 0.07) m, moving 1.85 m/s (vx +1.85, vy +0.00, vz -0.01); touching nothing
2.25 s: seesaw at 10.5°, turning +11°/s; touching nothing | ball at (1.39, 0.00, 0.04) m, moving 0.36 m/s (vx +0.15, vy -0.00, vz +0.32); touching nothing | weight at (3.41, 0.00, 0.07) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz -0.00); touching nothing
2.50 s: seesaw at 13.1°, turning +11°/s; touching nothing | ball at (1.42, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz +0.00); touching floor | weight at (3.85, 0.00, 0.07) m, moving 1.75 m/s (vx +1.75, vy +0.00, vz -0.02); touching nothing
2.75 s: seesaw at 15.8°, turning +11°/s; touching nothing | ball at (1.45, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.00); touching floor | weight at (4.28, 0.00, 0.07) m, moving 1.70 m/s (vx +1.70, vy +0.00, vz -0.00); touching floor
3.00 s: seesaw at 18.4°, turning +10°/s; touching nothing | ball at (1.47, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor | weight at (4.70, 0.00, 0.07) m, moving 1.65 m/s (vx +1.65, vy +0.00, vz -0.03); touching nothing
3.25 s: seesaw at 21.0°, turning +10°/s; touching nothing | ball at (1.48, 0.00, 0.04) m, at rest; touching floor | weight at (5.10, 0.00, 0.07) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.01); touching floor
3.50 s: seesaw at 23.6°, turning +10°/s; touching nothing | ball at (1.49, 0.00, 0.04) m, at rest; touching floor | weight at (5.50, 0.00, 0.07) m, moving 1.55 m/s (vx +1.55, vy +0.00, vz +0.01); touching floor
3.75 s: seesaw at 26.1°, turning +10°/s; touching nothing | ball at (1.49, 0.00, 0.04) m, at rest; touching floor | weight at (5.88, 0.00, 0.07) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor
4.00 s: seesaw at 28.6°, turning +10°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (6.25, 0.00, 0.07) m, moving 1.45 m/s (vx +1.45, vy +0.00, vz +0.01); touching floor
4.25 s: seesaw at 31.1°, turning +10°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (6.61, 0.00, 0.07) m, moving 1.40 m/s (vx +1.40, vy +0.00, vz -0.00); touching floor
4.50 s: seesaw at 33.5°, turning +10°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (6.95, 0.00, 0.07) m, moving 1.35 m/s (vx +1.35, vy +0.00, vz +0.00); touching floor
4.75 s: seesaw at 35.0°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (7.28, 0.00, 0.07) m, moving 1.30 m/s (vx +1.30, vy +0.00, vz +0.00); touching floor
5.00 s: seesaw at 34.7°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (7.60, 0.00, 0.07) m, moving 1.25 m/s (vx +1.25, vy +0.00, vz +0.01); touching floor
5.25 s: seesaw at 34.4°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (7.91, 0.00, 0.07) m, moving 1.21 m/s (vx +1.21, vy +0.00, vz +0.01); touching floor
5.50 s: seesaw at 34.1°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (8.21, 0.00, 0.07) m, moving 1.16 m/s (vx +1.16, vy +0.00, vz -0.00); touching floor
5.75 s: seesaw at 33.8°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (8.49, 0.00, 0.07) m, moving 1.11 m/s (vx +1.11, vy +0.00, vz -0.00); touching floor
6.00 s: seesaw at 33.5°, turning -1°/s; touching nothing | ball at (1.50, 0.00, 0.04) m, at rest; touching floor | weight at (8.76, 0.00, 0.07) m, moving 1.06 m/s (vx +1.06, vy +0.00, vz +0.01); touching floor

At the end (6.00 s):
- seesaw at 33.5°, turning -1°/s; touching nothing
- ball at (1.50, 0.00, 0.04) m, at rest; touching floor
- weight at (8.76, 0.00, 0.07) m, moving 1.06 m/s (vx +1.06, vy +0.00, vz +0.01); touching floor
</history>
