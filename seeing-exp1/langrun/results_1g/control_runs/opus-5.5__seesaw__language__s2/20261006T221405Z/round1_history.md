MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -20° to 0° as MuJoCo applies it; its geoms: seesaw; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (1.90, 0.00, 0.46) m, at rest
- weight: free body; its geoms: weight; starts at (0.10, 0.00, 2.50) m, at rest

What happened, in order:
 0.00 s  seesaw starts touching ball
 0.00 s  seesaw starts at its upper stop (0°)
 0.01 s  weight starts moving
 0.65 s  seesaw first touches weight
 0.65 s  ball starts moving
 0.70 s  seesaw reaches its lower stop (-20°) moving -355°/s
 0.71 s  seesaw leaves ball
 0.72 s  seesaw first touches floor
 0.73 s  seesaw is at its smallest, -22.8°
 0.74 s  seesaw leaves floor
 0.77 s  seesaw leaves weight
 0.78 s  seesaw reaches its lower stop (-20°) again moving +49°/s
 0.81 s  weight is at the top of its flight, at (-0.04, 0.00, 0.10) m
 0.91 s  weight first touches floor
 1.19 s  seesaw reaches its upper stop (0°) again moving +49°/s
 1.22 s  seesaw is at its largest, 0.3°
 1.32 s  ball is at the top of its flight, at (1.39, 0.00, 2.61) m
 1.98 s  seesaw touches ball again
 1.99 s  ball passes 0.10 m from stand without touching it: nearest points (0.89, 0.00, 0.40) m and (0.98, 0.00, 0.36) m
 2.07 s  seesaw leaves ball
 2.14 s  seesaw touches ball again
 2.30 s  seesaw reaches its lower stop (-20°) again moving -57°/s
 2.89 s  seesaw leaves ball
 2.97 s  ball first touches floor
 3.03 s  ball leaves floor
 3.06 s  ball touches floor again
 5.50 s  ball comes to rest at (-2.07, 0.00, 0.04) m
 6.00 s  weight is still moving at the end, 1.71 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | ball at (1.90, 0.00, 0.46) m, at rest; touching seesaw | weight at (0.10, 0.00, 2.50) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching ball | ball at (1.90, 0.00, 0.46) m, at rest; touching seesaw | weight at (0.10, 0.00, 2.20) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at 0.0°, still; touching ball | ball at (1.90, 0.00, 0.46) m, at rest; touching seesaw | weight at (0.10, 0.00, 1.28) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at -22.1°, turning +49°/s; touching weight | ball at (1.84, 0.00, 1.03) m, moving 5.61 m/s (vx -0.80, vy +0.00, vz +5.55); touching nothing | weight at (0.07, 0.00, 0.08) m, moving 1.83 m/s (vx -1.75, vy -0.00, vz +0.54); touching seesaw
1.00 s: seesaw at -9.9°, turning +49°/s; touching nothing | ball at (1.64, 0.00, 2.12) m, moving 3.20 m/s (vx -0.80, vy +0.00, vz +3.10); touching nothing | weight at (-0.37, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.01); touching floor
1.25 s: seesaw at 0.2°, turning -7°/s; touching nothing | ball at (1.44, 0.00, 2.59) m, moving 1.03 m/s (vx -0.80, vy +0.00, vz +0.65); touching nothing | weight at (-0.80, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
1.50 s: seesaw at -1.4°, turning -7°/s; touching nothing | ball at (1.24, 0.00, 2.45) m, moving 1.97 m/s (vx -0.80, vy +0.00, vz -1.80); touching nothing | weight at (-1.22, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
1.75 s: seesaw at -3.1°, turning -7°/s; touching nothing | ball at (1.04, 0.00, 1.69) m, moving 4.33 m/s (vx -0.80, vy +0.00, vz -4.26); touching nothing | weight at (-1.65, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
2.00 s: seesaw at -5.2°, turning -41°/s; touching ball | ball at (0.84, 0.00, 0.40) m, moving 0.41 m/s (vx -0.40, vy -0.00, vz +0.06); touching seesaw | weight at (-2.08, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
2.25 s: seesaw at -17.0°, turning -54°/s; touching nothing | ball at (0.75, 0.00, 0.39) m, moving 0.62 m/s (vx -0.49, vy -0.00, vz -0.39); touching nothing | weight at (-2.51, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
2.50 s: seesaw at -20.0°, still; touching ball | ball at (0.56, 0.00, 0.30) m, moving 1.04 m/s (vx -0.98, vy -0.00, vz -0.34); touching seesaw | weight at (-2.93, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at -20.0°, still; touching nothing | ball at (0.26, 0.00, 0.20) m, moving 1.51 m/s (vx -1.42, vy -0.00, vz -0.51); touching nothing | weight at (-3.36, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
3.00 s: seesaw at -20.0°, still; touching nothing | ball at (-0.13, 0.00, 0.03) m, moving 1.57 m/s (vx -1.55, vy -0.00, vz +0.25); touching floor | weight at (-3.79, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
3.25 s: seesaw at -19.9°, still; touching nothing | ball at (-0.51, 0.00, 0.04) m, moving 1.43 m/s (vx -1.43, vy -0.00, vz -0.01); touching floor | weight at (-4.21, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.50 s: seesaw at -19.9°, still; touching nothing | ball at (-0.85, 0.00, 0.04) m, moving 1.26 m/s (vx -1.26, vy -0.00, vz -0.01); touching nothing | weight at (-4.64, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.75 s: seesaw at -19.8°, still; touching nothing | ball at (-1.14, 0.00, 0.04) m, moving 1.10 m/s (vx -1.10, vy -0.00, vz +0.01); touching floor | weight at (-5.07, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
4.00 s: seesaw at -19.8°, still; touching nothing | ball at (-1.40, 0.00, 0.04) m, moving 0.93 m/s (vx -0.93, vy -0.00, vz -0.00); touching floor | weight at (-5.50, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
4.25 s: seesaw at -19.7°, still; touching nothing | ball at (-1.61, 0.00, 0.04) m, moving 0.77 m/s (vx -0.77, vy -0.00, vz -0.01); touching nothing | weight at (-5.92, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
4.50 s: seesaw at -19.7°, still; touching nothing | ball at (-1.78, 0.00, 0.04) m, moving 0.61 m/s (vx -0.61, vy -0.00, vz -0.01); touching floor | weight at (-6.35, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at -19.6°, still; touching nothing | ball at (-1.91, 0.00, 0.04) m, moving 0.44 m/s (vx -0.44, vy -0.00, vz -0.00); touching floor | weight at (-6.78, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
5.00 s: seesaw at -19.5°, still; touching nothing | ball at (-2.00, 0.00, 0.04) m, moving 0.28 m/s (vx -0.28, vy -0.00, vz -0.00); touching floor | weight at (-7.21, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
5.25 s: seesaw at -19.5°, still; touching nothing | ball at (-2.05, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching floor | weight at (-7.63, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
5.50 s: seesaw at -19.4°, still; touching nothing | ball at (-2.07, 0.00, 0.04) m, at rest; touching floor | weight at (-8.06, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
5.75 s: seesaw at -19.4°, still; touching nothing | ball at (-2.08, 0.00, 0.04) m, at rest; touching floor | weight at (-8.49, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
6.00 s: seesaw at -19.3°, still; touching nothing | ball at (-2.08, 0.00, 0.04) m, at rest; touching floor | weight at (-8.92, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at -19.3°, still; touching nothing
- ball at (-2.08, 0.00, 0.04) m, at rest; touching floor
- weight at (-8.92, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
</history>
