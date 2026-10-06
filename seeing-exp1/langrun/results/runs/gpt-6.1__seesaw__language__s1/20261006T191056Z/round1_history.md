MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: seesaw; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.80, 0.00, 0.80) m, at rest
- weight: free body; its geoms: weight; starts at (0.80, 0.00, 3.00) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its lower stop (0°)
 0.00 s  seesaw first touches ball
 0.01 s  weight starts moving
 0.67 s  seesaw first touches weight
 0.67 s  ball starts moving
 0.70 s  seesaw leaves weight
 0.77 s  seesaw reaches its upper stop (40°) moving +347°/s
 0.77 s  seesaw leaves ball
 0.79 s  seesaw touches weight again
 0.80 s  seesaw leaves weight
 0.80 s  seesaw is at its largest, 42.5°
 0.81 s  weight first touches floor
 0.85 s  seesaw reaches its upper stop (40°) again moving -46°/s
 0.88 s  weight leaves floor
 0.92 s  weight touches floor again
 1.40 s  ball is at the top of its flight, at (0.36, 0.00, 3.37) m
 1.72 s  seesaw reaches its lower stop (0°) again moving -45°/s
 1.75 s  seesaw is at its smallest, -0.3°
 2.23 s  ball first touches floor
 2.29 s  ball leaves floor
 2.37 s  ball is at the top of its flight, at (1.78, 0.00, 0.06) m
 2.45 s  ball touches floor again
 2.74 s  ball comes to rest at (1.76, 0.00, 0.03) m
 6.00 s  weight is still moving at the end, 1.76 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | ball at (-0.80, 0.00, 0.80) m, at rest; touching nothing | weight at (0.80, 0.00, 3.00) m, at rest; touching nothing
0.25 s: seesaw at -0.0°, still; touching ball | ball at (-0.80, 0.00, 0.80) m, at rest; touching seesaw | weight at (0.80, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at -0.0°, still; touching ball | ball at (-0.80, 0.00, 0.80) m, at rest; touching seesaw | weight at (0.80, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at 32.6°, turning +368°/s; touching ball | ball at (-0.75, 0.00, 1.28) m, moving 6.27 m/s (vx +1.28, vy +0.00, vz +6.14); touching seesaw | weight at (0.80, 0.00, 0.37) m, moving 5.81 m/s (vx -0.07, vy -0.00, vz -5.81); touching nothing
1.00 s: seesaw at 33.4°, turning -46°/s; touching nothing | ball at (-0.33, 0.00, 2.57) m, moving 4.30 m/s (vx +1.72, vy +0.00, vz +3.95); touching nothing | weight at (1.14, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
1.25 s: seesaw at 21.9°, turning -46°/s; touching nothing | ball at (0.10, 0.00, 3.25) m, moving 2.28 m/s (vx +1.72, vy +0.00, vz +1.50); touching nothing | weight at (1.58, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
1.50 s: seesaw at 10.5°, turning -46°/s; touching nothing | ball at (0.53, 0.00, 3.32) m, moving 1.96 m/s (vx +1.72, vy +0.00, vz -0.96); touching nothing | weight at (2.02, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
1.75 s: seesaw at -0.3°, still; touching nothing | ball at (0.96, 0.00, 2.78) m, moving 3.82 m/s (vx +1.72, vy +0.00, vz -3.41); touching nothing | weight at (2.46, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
2.00 s: seesaw at 1.1°, turning +6°/s; touching nothing | ball at (1.39, 0.00, 1.62) m, moving 6.11 m/s (vx +1.72, vy +0.00, vz -5.86); touching nothing | weight at (2.90, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
2.25 s: seesaw at 2.5°, turning +6°/s; touching nothing | ball at (1.79, 0.00, -0.01) m, moving 1.06 m/s (vx -0.01, vy -0.00, vz +1.06); touching floor | weight at (3.34, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
2.50 s: seesaw at 4.0°, turning +6°/s; touching nothing | ball at (1.77, 0.00, 0.03) m, moving 0.10 m/s (vx -0.09, vy +0.00, vz +0.04); touching floor | weight at (3.78, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at 5.4°, turning +6°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (4.22, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
3.00 s: seesaw at 6.8°, turning +6°/s; touching nothing | ball at (1.75, 0.00, 0.03) m, at rest; touching floor | weight at (4.66, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
3.25 s: seesaw at 8.2°, turning +6°/s; touching nothing | ball at (1.75, 0.00, 0.03) m, at rest; touching floor | weight at (5.10, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
3.50 s: seesaw at 9.6°, turning +6°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (5.54, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
3.75 s: seesaw at 11.0°, turning +6°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (5.98, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
4.00 s: seesaw at 12.3°, turning +6°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (6.42, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
4.25 s: seesaw at 13.7°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (6.86, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
4.50 s: seesaw at 15.1°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (7.30, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at 16.4°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (7.74, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
5.00 s: seesaw at 17.8°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (8.18, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
5.25 s: seesaw at 19.1°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (8.62, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
5.50 s: seesaw at 20.5°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (9.06, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at 21.8°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (9.50, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
6.00 s: seesaw at 23.1°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.03) m, at rest; touching floor | weight at (9.94, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor

At the end (6.00 s):
- seesaw at 23.1°, turning +5°/s; touching nothing
- ball at (1.74, 0.00, 0.03) m, at rest; touching floor
- weight at (9.94, 0.00, 0.05) m, moving 1.76 m/s (vx +1.76, vy -0.00, vz +0.00); touching floor
</history>
