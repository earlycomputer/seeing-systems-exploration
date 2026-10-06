MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint pivot about axis (0.00, 1.00, 0.00), range -17.1887° to 17.1887° as MuJoCo applies it; its geoms: seesaw.plank, seesaw.lip; starts at 17.2°, still
- weight: free body; its geoms: weight_geom; starts at (-0.85, 0.00, 3.00) m, at rest
- ball: free body; its geoms: ball; starts at (0.91, 0.00, 0.17) m, at rest

What happened, in order:
 0.00 s  seesaw.lip starts touching ball
 0.00 s  seesaw starts at its upper stop (17.1887°)
 0.00 s  seesaw.plank first touches ball
 0.01 s  weight starts moving
 0.68 s  seesaw.plank first touches weight_geom
 0.68 s  ball starts moving
 0.75 s  seesaw.plank leaves weight_geom
 0.78 s  seesaw reaches its lower stop (-17.1887°) moving -392°/s
 0.78 s  seesaw.plank leaves ball
 0.79 s  seesaw.lip leaves ball
 0.79 s  seesaw.plank touches weight_geom again
 0.80 s  seesaw is at its smallest, -20.0°
 0.86 s  seesaw reaches its lower stop (-17.1887°) again moving +44°/s
 0.89 s  seesaw.plank leaves weight_geom
 0.93 s  weight is at the top of its flight, at (-1.02, 0.00, 0.20) m
 1.10 s  weight_geom first touches floor
 1.23 s  ball is at the top of its flight, at (-0.49, 0.00, 1.73) m
 1.51 s  seesaw reaches its upper stop (17.1887°) again moving +70°/s
 1.53 s  seesaw is at its largest, 17.7°
 1.54 s  seesaw reaches its upper stop (17.1887°) again moving -5°/s
 1.82 s  ball first touches floor
 1.90 s  ball leaves floor
 1.98 s  ball touches floor again
 3.01 s  ball comes to rest at (-2.74, 0.00, 0.04) m
 3.84 s  weight comes to rest at (-2.56, 0.00, 0.06) m
 6.00 s  weight passes 0.07 m from ball without touching it: nearest points (-2.64, 0.00, 0.05) m and (-2.71, 0.00, 0.04) m

State every 0.25 s:
0.00 s: seesaw at 17.2°, still; touching ball | weight at (-0.85, 0.00, 3.00) m, at rest; touching nothing | ball at (0.91, 0.00, 0.17) m, at rest; touching seesaw.lip
0.25 s: seesaw at 17.2°, still; touching ball | weight at (-0.85, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.91, 0.00, 0.17) m, at rest; touching seesaw.lip, seesaw.plank
0.50 s: seesaw at 17.2°, still; touching ball | weight at (-0.85, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.91, 0.00, 0.17) m, at rest; touching seesaw.lip, seesaw.plank
0.75 s: seesaw at -6.5°, turning -398°/s; touching ball, weight_geom | weight at (-0.85, 0.00, 0.38) m, moving 4.98 m/s (vx +0.09, vy -0.00, vz -4.98); touching seesaw.plank | ball at (0.94, 0.00, 0.54) m, moving 6.63 m/s (vx -0.90, vy -0.00, vz +6.56); touching seesaw.lip, seesaw.plank
1.00 s: seesaw at -12.0°, turning +43°/s; touching nothing | weight at (-1.10, 0.00, 0.17) m, moving 1.45 m/s (vx -1.28, vy +0.00, vz -0.68); touching nothing | ball at (0.22, 0.00, 1.47) m, moving 3.81 m/s (vx -3.08, vy +0.00, vz +2.24); touching nothing
1.25 s: seesaw at 0.3°, turning +56°/s; touching nothing | weight at (-1.40, 0.00, 0.06) m, moving 1.08 m/s (vx -1.08, vy +0.00, vz -0.01); touching floor | ball at (-0.55, 0.00, 1.73) m, moving 3.09 m/s (vx -3.08, vy +0.00, vz -0.21); touching nothing
1.50 s: seesaw at 16.1°, turning +69°/s; touching nothing | weight at (-1.65, 0.00, 0.06) m, moving 0.94 m/s (vx -0.94, vy +0.00, vz -0.00); touching floor | ball at (-1.32, 0.00, 1.37) m, moving 4.07 m/s (vx -3.08, vy +0.00, vz -2.67); touching nothing
1.75 s: seesaw at 16.8°, turning +2°/s; touching nothing | weight at (-1.87, 0.00, 0.06) m, moving 0.80 m/s (vx -0.80, vy +0.00, vz +0.01); touching floor | ball at (-2.09, 0.00, 0.40) m, moving 5.97 m/s (vx -3.08, vy +0.00, vz -5.12); touching nothing
2.00 s: seesaw at 17.2°, still; touching nothing | weight at (-2.05, 0.00, 0.06) m, moving 0.66 m/s (vx -0.66, vy +0.00, vz -0.01); touching nothing | ball at (-2.44, 0.00, 0.04) m, moving 0.66 m/s (vx -0.66, vy +0.00, vz +0.06); touching floor
2.25 s: seesaw at 17.2°, still; touching nothing | weight at (-2.20, 0.00, 0.06) m, moving 0.52 m/s (vx -0.52, vy +0.00, vz +0.00); touching floor | ball at (-2.58, 0.00, 0.04) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz +0.01); touching floor
2.50 s: seesaw at 17.2°, still; touching nothing | weight at (-2.32, 0.00, 0.06) m, moving 0.39 m/s (vx -0.39, vy +0.00, vz -0.00); touching floor | ball at (-2.67, 0.00, 0.04) m, moving 0.26 m/s (vx -0.26, vy +0.00, vz +0.00); touching floor
2.75 s: seesaw at 17.2°, still; touching nothing | weight at (-2.40, 0.00, 0.06) m, moving 0.29 m/s (vx -0.29, vy +0.00, vz -0.00); touching floor | ball at (-2.71, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching floor
3.00 s: seesaw at 17.2°, still; touching nothing | weight at (-2.46, 0.00, 0.06) m, moving 0.21 m/s (vx -0.21, vy +0.00, vz -0.00); touching floor | ball at (-2.74, 0.00, 0.04) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz -0.00); touching floor
3.25 s: seesaw at 17.2°, still; touching nothing | weight at (-2.51, 0.00, 0.06) m, moving 0.15 m/s (vx -0.15, vy +0.00, vz -0.00); touching floor | ball at (-2.74, 0.00, 0.04) m, at rest; touching floor
3.50 s: seesaw at 17.2°, still; touching nothing | weight at (-2.54, 0.00, 0.06) m, moving 0.10 m/s (vx -0.10, vy +0.00, vz -0.00); touching floor | ball at (-2.75, 0.00, 0.04) m, at rest; touching floor
3.75 s: seesaw at 17.2°, still; touching nothing | weight at (-2.56, 0.00, 0.06) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball at (-2.75, 0.00, 0.04) m, at rest; touching floor
4.00 s: seesaw at 17.2°, still; touching nothing | weight at (-2.57, 0.00, 0.06) m, at rest; touching floor | ball at (-2.75, 0.00, 0.04) m, at rest; touching floor
(the same through 4.25 s)
4.50 s: seesaw at 17.2°, still; touching nothing | weight at (-2.58, 0.00, 0.06) m, at rest; touching floor | ball at (-2.75, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- seesaw at 17.2°, still; touching nothing
- weight at (-2.58, 0.00, 0.06) m, at rest; touching floor
- ball at (-2.75, 0.00, 0.04) m, at rest; touching floor
</history>
