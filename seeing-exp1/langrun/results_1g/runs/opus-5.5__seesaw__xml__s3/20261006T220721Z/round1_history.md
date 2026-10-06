Your expectations, checked against the run (1 of 2 hold):

- holds: weight touches seesaw (first touch at 0.53 s)
- DOES NOT HOLD: ball rises at least 0.5 m above its start (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -30.9397° to 0° as MuJoCo applies it; its geoms: seesaw_plank, seesaw_lip; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.86, 0.00, 2.00) m, at rest
- ball: free body; its geoms: ball; starts at (0.90, 0.00, 0.13) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (0°)
 0.01 s  weight starts moving
 0.01 s  ball starts moving
 0.01 s  seesaw_lip first touches ball
 0.02 s  seesaw_plank first touches ball
 0.53 s  seesaw_plank first touches weight
 0.61 s  seesaw_plank leaves weight
 0.64 s  seesaw reaches its lower stop (-30.9397°) moving -309°/s
 0.64 s  seesaw_plank leaves ball
 0.65 s  seesaw_plank first touches floor
 0.65 s  seesaw_plank touches weight again
 0.66 s  seesaw_lip leaves ball
 0.66 s  seesaw is at its smallest, -33.1°
 0.70 s  seesaw_plank leaves floor
 0.71 s  seesaw reaches its lower stop (-30.9397°) again moving +30°/s
 0.81 s  seesaw_plank leaves weight
 0.89 s  weight first touches floor
 0.99 s  ball is at the top of its flight, at (0.05, 0.00, 1.21) m
 1.43 s  seesaw_plank touches ball again
 1.46 s  seesaw_plank leaves ball
 1.53 s  ball first touches floor
 1.61 s  seesaw reaches its lower stop (-30.9397°) again moving -46°/s
 2.61 s  seesaw reaches its upper stop (0°) again moving +59°/s
 2.64 s  seesaw is at its largest, 0.4°
 2.83 s  weight first touches ball
 2.83 s  ball leaves floor
 2.84 s  weight leaves ball
 2.92 s  ball touches floor again
 6.00 s  weight is still moving at the end, 0.97 m/s
 6.00 s  ball is still moving at the end, 0.58 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | weight at (-0.86, 0.00, 2.00) m, at rest; touching nothing | ball at (0.90, 0.00, 0.13) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.86, 0.00, 1.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.90, 0.00, 0.12) m, at rest; touching seesaw_lip, seesaw_plank
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-0.86, 0.00, 0.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.90, 0.00, 0.12) m, at rest; touching seesaw_lip, seesaw_plank
0.75 s: seesaw at -30.5°, turning +19°/s; touching weight | weight at (-0.94, 0.00, 0.13) m, moving 0.98 m/s (vx -0.96, vy +0.00, vz +0.14); touching seesaw_plank | ball at (0.62, 0.00, 0.93) m, moving 3.32 m/s (vx -2.37, vy +0.00, vz +2.33); touching nothing
1.00 s: seesaw at -29.7°, turning +7°/s; touching nothing | weight at (-1.18, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz +0.02); touching floor | ball at (0.03, 0.00, 1.21) m, moving 2.37 m/s (vx -2.37, vy +0.00, vz -0.12); touching nothing
1.25 s: seesaw at -26.1°, turning +21°/s; touching nothing | weight at (-1.42, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz +0.00); touching floor | ball at (-0.57, 0.00, 0.87) m, moving 3.50 m/s (vx -2.37, vy +0.00, vz -2.57); touching nothing
1.50 s: seesaw at -25.1°, turning -52°/s; touching nothing | weight at (-1.66, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz +0.00); touching floor | ball at (-1.09, 0.00, 0.12) m, moving 2.50 m/s (vx -1.43, vy +0.00, vz -2.05); touching nothing
1.75 s: seesaw at -30.4°, turning +10°/s; touching nothing | weight at (-1.90, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-1.42, 0.00, 0.05) m, moving 1.31 m/s (vx -1.31, vy +0.00, vz -0.00); touching floor
2.00 s: seesaw at -26.1°, turning +24°/s; touching nothing | weight at (-2.14, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-1.75, 0.00, 0.05) m, moving 1.31 m/s (vx -1.31, vy +0.00, vz -0.00); touching floor
2.25 s: seesaw at -18.2°, turning +39°/s; touching nothing | weight at (-2.39, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-2.08, 0.00, 0.05) m, moving 1.31 m/s (vx -1.31, vy +0.00, vz +0.00); touching floor
2.50 s: seesaw at -6.7°, turning +53°/s; touching nothing | weight at (-2.63, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-2.41, 0.00, 0.05) m, moving 1.31 m/s (vx -1.31, vy +0.00, vz -0.00); touching floor
2.75 s: seesaw at -0.1°, turning -2°/s; touching nothing | weight at (-2.87, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-2.73, 0.00, 0.05) m, moving 1.31 m/s (vx -1.31, vy +0.00, vz -0.00); touching floor
3.00 s: seesaw at 0.0°, still; touching nothing | weight at (-3.11, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-2.96, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz +0.02); touching floor
3.25 s: seesaw at 0.0°, still; touching nothing | weight at (-3.36, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.10, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz +0.00); touching floor
3.50 s: seesaw at 0.0°, still; touching nothing | weight at (-3.60, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz +0.00); touching floor | ball at (-3.24, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz +0.00); touching floor
3.75 s: seesaw at 0.0°, still; touching nothing | weight at (-3.84, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.39, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
4.00 s: seesaw at 0.0°, still; touching nothing | weight at (-4.08, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.53, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
4.25 s: seesaw at 0.0°, still; touching nothing | weight at (-4.33, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.68, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
4.50 s: seesaw at 0.0°, still; touching nothing | weight at (-4.57, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.82, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at 0.0°, still; touching nothing | weight at (-4.81, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-3.97, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
5.00 s: seesaw at 0.0°, still; touching nothing | weight at (-5.05, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-4.11, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
5.25 s: seesaw at 0.0°, still; touching nothing | weight at (-5.30, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-4.25, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
5.50 s: seesaw at 0.0°, still; touching nothing | weight at (-5.54, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-4.40, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at 0.0°, still; touching nothing | weight at (-5.78, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-4.54, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
6.00 s: seesaw at 0.0°, still; touching nothing | weight at (-6.02, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor | ball at (-4.69, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at 0.0°, still; touching nothing
- weight at (-6.02, 0.00, 0.06) m, moving 0.97 m/s (vx -0.97, vy +0.00, vz -0.00); touching floor
- ball at (-4.69, 0.00, 0.05) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.00); touching floor
</history>
