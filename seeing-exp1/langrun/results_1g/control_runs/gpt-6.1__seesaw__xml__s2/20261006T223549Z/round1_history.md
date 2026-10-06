MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -28.6479° to 0° as MuJoCo applies it; its geoms: seesaw_beam; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-1.00, 0.00, 2.33) m, at rest
- ball: free body; its geoms: ball; starts at (1.00, 0.00, 0.73) m, at rest

What happened, in order:
 0.00 s  seesaw_beam starts touching ball
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw is at its largest, 0.0°
 0.01 s  weight starts moving
 0.56 s  seesaw_beam first touches weight_sphere
 0.56 s  ball starts moving
 0.57 s  seesaw_beam leaves weight_sphere
 0.67 s  seesaw reaches its lower stop (-28.6479°) moving -244°/s
 0.67 s  seesaw_beam leaves ball
 0.67 s  seesaw_beam touches weight_sphere again
 0.67 s  seesaw is at its smallest, -28.7°
 0.68 s  seesaw_beam leaves weight_sphere
 0.72 s  seesaw_beam touches weight_sphere again
 0.72 s  seesaw_beam leaves weight_sphere
 0.80 s  weight_sphere first touches floor
 0.80 s  weight_sphere leaves floor
 0.87 s  weight_sphere touches floor again
 0.89 s  weight_sphere leaves floor
 0.92 s  weight_sphere touches floor again
 1.17 s  ball is at the top of its flight, at (0.45, 0.00, 2.48) m
 1.77 s  ball passes 0.04 m from support (support.pivot_axle) without touching it: nearest points (-0.09, 0.00, 0.68) m and (-0.05, 0.00, 0.67) m
 1.78 s  seesaw_beam touches ball again
 1.78 s  seesaw_beam leaves ball
 1.78 s  seesaw reaches its lower stop (-28.6479°) again moving -38°/s
 1.94 s  seesaw_beam touches ball again
 1.94 s  seesaw_beam leaves ball
 1.98 s  seesaw reaches its lower stop (-28.6479°) again moving -16°/s
 2.05 s  seesaw_beam touches ball again
 2.08 s  seesaw_beam leaves ball
 2.13 s  seesaw_beam touches ball 2 more times between 2.13 s and 2.16 s
 2.24 s  ball first touches floor
 2.25 s  ball leaves floor
 2.32 s  ball is at the top of its flight, at (-1.41, 0.00, 0.09) m
 2.39 s  ball touches floor again
 2.39 s  ball leaves floor
 2.44 s  ball touches floor again
 2.44 s  ball leaves floor
 2.50 s  ball touches floor again
 2.50 s  ball leaves floor
 2.56 s  ball touches floor 3 more times between 2.56 s and 6.00 s, still touching at the end
 2.64 s  weight_sphere first touches ball
 2.65 s  weight_sphere leaves ball
 2.68 s  ball comes to rest at (-2.04, 0.00, 0.06) m
 2.69 s  weight comes to rest at (-2.20, 0.00, 0.10) m

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | weight at (-1.00, 0.00, 2.33) m, at rest; touching nothing | ball at (1.00, 0.00, 0.73) m, at rest; touching seesaw_beam
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-1.00, 0.00, 2.02) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (1.00, 0.00, 0.73) m, at rest; touching seesaw_beam
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-1.00, 0.00, 1.10) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (1.00, 0.00, 0.73) m, at rest; touching seesaw_beam
0.75 s: seesaw at -28.6°, still; touching nothing | weight at (-1.14, 0.00, 0.17) m, moving 2.12 m/s (vx -1.71, vy +0.00, vz -1.25); touching nothing | ball at (0.87, 0.00, 1.62) m, moving 4.22 m/s (vx -1.00, vy +0.00, vz +4.10); touching nothing
1.00 s: seesaw at -28.5°, still; touching nothing | weight at (-1.52, 0.00, 0.10) m, moving 1.32 m/s (vx -1.32, vy +0.00, vz -0.09); touching nothing | ball at (0.62, 0.00, 2.34) m, moving 1.93 m/s (vx -1.00, vy +0.00, vz +1.65); touching nothing
1.25 s: seesaw at -28.3°, still; touching nothing | weight at (-1.80, 0.00, 0.10) m, moving 1.01 m/s (vx -1.00, vy +0.00, vz -0.10); touching nothing | ball at (0.37, 0.00, 2.45) m, moving 1.28 m/s (vx -1.00, vy +0.00, vz -0.80); touching nothing
1.50 s: seesaw at -28.1°, still; touching nothing | weight at (-2.01, 0.00, 0.10) m, moving 0.68 m/s (vx -0.68, vy +0.00, vz -0.01); touching nothing | ball at (0.12, 0.00, 1.94) m, moving 3.41 m/s (vx -1.00, vy +0.00, vz -3.26); touching nothing
1.75 s: seesaw at -27.9°, still; touching nothing | weight at (-2.14, 0.00, 0.10) m, moving 0.36 m/s (vx -0.36, vy +0.00, vz +0.03); touching floor | ball at (-0.13, 0.00, 0.82) m, moving 5.80 m/s (vx -1.00, vy +0.00, vz -5.71); touching nothing
2.00 s: seesaw at -28.5°, turning -16°/s; touching nothing | weight at (-2.19, 0.00, 0.10) m, at rest; touching floor | ball at (-0.62, 0.00, 0.43) m, moving 2.66 m/s (vx -2.28, vy +0.00, vz -1.38); touching nothing
2.25 s: seesaw at -28.6°, turning +1°/s; touching nothing | weight at (-2.19, 0.00, 0.10) m, at rest; touching floor | ball at (-1.26, 0.00, 0.06) m, moving 2.36 m/s (vx -2.26, vy +0.00, vz +0.69); touching nothing
2.50 s: seesaw at -28.3°, turning +1°/s; touching nothing | weight at (-2.19, 0.00, 0.10) m, at rest; touching floor | ball at (-1.79, 0.00, 0.06) m, moving 1.87 m/s (vx -1.85, vy +0.00, vz +0.28); touching floor
2.75 s: seesaw at -28.0°, turning +1°/s; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
3.00 s: seesaw at -27.7°, turning +1°/s; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
3.25 s: seesaw at -27.5°, turning +1°/s; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
3.50 s: seesaw at -27.2°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
3.75 s: seesaw at -27.0°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
4.00 s: seesaw at -26.7°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
4.25 s: seesaw at -26.5°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
4.50 s: seesaw at -26.3°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
4.75 s: seesaw at -26.1°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
5.00 s: seesaw at -25.9°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
5.25 s: seesaw at -25.7°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
5.50 s: seesaw at -25.5°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
5.75 s: seesaw at -25.3°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
6.00 s: seesaw at -25.1°, still; touching nothing | weight at (-2.20, 0.00, 0.10) m, at rest; touching floor | ball at (-2.04, 0.00, 0.06) m, at rest; touching floor

At the end (6.00 s):
- seesaw at -25.1°, still; touching nothing
- weight at (-2.20, 0.00, 0.10) m, at rest; touching floor
- ball at (-2.04, 0.00, 0.06) m, at rest; touching floor
</history>
