MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -15° to 0° as MuJoCo applies it; its geoms: seesaw_plank; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.90, 0.00, 3.00) m, at rest
- ball: free body; its geoms: ball; starts at (0.90, 0.00, 0.60) m, at rest

What happened, in order:
 0.00 s  seesaw_plank starts touching ball
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw is at its largest, 0.0°
 0.01 s  weight starts moving
 0.69 s  seesaw_plank first touches weight_sphere
 0.69 s  ball starts moving
 0.70 s  seesaw_plank leaves weight_sphere
 0.72 s  seesaw_plank leaves ball
 0.73 s  seesaw reaches its lower stop (-15°) moving -392°/s
 0.73 s  seesaw is at its smallest, -15.9°
 0.74 s  seesaw_plank touches weight_sphere again
 0.74 s  seesaw reaches its lower stop (-15°) again moving +57°/s
 0.74 s  seesaw_plank leaves weight_sphere
 0.89 s  weight is at the top of its flight, at (-1.11, 0.00, 0.52) m
 0.91 s  seesaw_plank touches weight_sphere again
 0.91 s  seesaw_plank leaves weight_sphere
 1.19 s  weight_sphere first touches floor
 1.20 s  weight_sphere leaves floor
 1.29 s  weight_sphere touches floor again
 1.42 s  ball is at the top of its flight, at (0.46, 0.00, 3.17) m
 1.65 s  weight comes to rest at (-1.66, 0.00, 0.12) m
 2.14 s  seesaw_plank touches ball again
 2.15 s  seesaw_plank leaves ball
 2.15 s  ball passes -0.02 m from stand (stand.pivot_pin) without touching it: nearest points (0.00, 0.00, 0.54) m and (0.00, 0.00, 0.55) m
 2.23 s  ball is at the top of its flight, at (-0.03, 0.00, 0.63) m
 2.32 s  seesaw_plank touches ball again
 2.32 s  seesaw_plank leaves ball
 2.36 s  seesaw_plank touches ball again
 2.73 s  seesaw reaches its lower stop (-15°) again moving -35°/s
 3.30 s  seesaw_plank leaves ball
 3.34 s  seesaw_plank touches ball 10 more times between 3.34 s and 3.79 s
 4.01 s  ball first touches floor
 4.02 s  ball leaves floor
 4.06 s  ball touches floor again
 4.20 s  ball comes to rest at (-1.38, 0.00, 0.06) m
 4.68 s  weight passes 0.10 m from ball without touching it: nearest points (-1.54, 0.00, 0.10) m and (-1.44, 0.00, 0.08) m

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | weight at (-0.90, 0.00, 3.00) m, at rest; touching nothing | ball at (0.90, 0.00, 0.60) m, at rest; touching seesaw_plank
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.90, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.90, 0.00, 0.60) m, at rest; touching seesaw_plank
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-0.90, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.90, 0.00, 0.60) m, at rest; touching seesaw_plank
0.75 s: seesaw at -15.0°, turning +57°/s; touching nothing | weight at (-0.92, 0.00, 0.42) m, moving 1.89 m/s (vx -1.27, vy +0.00, vz +1.40); touching nothing | ball at (0.87, 0.00, 0.98) m, moving 6.58 m/s (vx -0.62, vy +0.00, vz +6.55); touching nothing
1.00 s: seesaw at -7.3°, turning -2°/s; touching nothing | weight at (-1.24, 0.00, 0.47) m, moving 1.58 m/s (vx -1.24, vy +0.00, vz -0.99); touching nothing | ball at (0.72, 0.00, 2.31) m, moving 4.15 m/s (vx -0.62, vy +0.00, vz +4.10); touching nothing
1.25 s: seesaw at -7.8°, turning -2°/s; touching nothing | weight at (-1.51, 0.00, 0.13) m, moving 0.70 m/s (vx -0.69, vy +0.00, vz -0.08); touching nothing | ball at (0.56, 0.00, 3.03) m, moving 1.76 m/s (vx -0.62, vy +0.00, vz +1.65); touching nothing
1.50 s: seesaw at -8.1°, turning -1°/s; touching nothing | weight at (-1.63, 0.00, 0.12) m, moving 0.30 m/s (vx -0.29, vy +0.00, vz -0.03); touching nothing | ball at (0.41, 0.00, 3.14) m, moving 1.01 m/s (vx -0.62, vy +0.00, vz -0.80); touching nothing
1.75 s: seesaw at -8.4°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (0.25, 0.00, 2.64) m, moving 3.31 m/s (vx -0.62, vy +0.00, vz -3.26); touching nothing
2.00 s: seesaw at -8.5°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (0.10, 0.00, 1.52) m, moving 5.74 m/s (vx -0.62, vy +0.00, vz -5.71); touching nothing
2.25 s: seesaw at -8.0°, turning +5°/s; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.04, 0.00, 0.63) m, moving 0.57 m/s (vx -0.51, vy +0.00, vz -0.25); touching nothing
2.50 s: seesaw at -8.9°, turning -14°/s; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.16, 0.00, 0.58) m, moving 0.42 m/s (vx -0.42, vy +0.00, vz -0.06); touching nothing
2.75 s: seesaw at -15.0°, still; touching ball | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.26, 0.00, 0.53) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.03); touching seesaw_plank
3.00 s: seesaw at -15.0°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.40, 0.00, 0.50) m, moving 0.63 m/s (vx -0.62, vy +0.00, vz -0.15); touching nothing
3.25 s: seesaw at -15.0°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.57, 0.00, 0.45) m, moving 0.80 m/s (vx -0.77, vy +0.00, vz -0.22); touching nothing
3.50 s: seesaw at -15.0°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-0.78, 0.00, 0.39) m, moving 0.94 m/s (vx -0.93, vy +0.00, vz -0.14); touching nothing
3.75 s: seesaw at -15.0°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.03, 0.00, 0.33) m, moving 1.10 m/s (vx -1.09, vy +0.00, vz -0.18); touching nothing
4.00 s: seesaw at -14.8°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.31, 0.00, 0.08) m, moving 2.42 m/s (vx -1.12, vy +0.00, vz -2.15); touching nothing
4.25 s: seesaw at -14.6°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.38, 0.00, 0.06) m, at rest; touching floor
4.50 s: seesaw at -14.4°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.38, 0.00, 0.06) m, at rest; touching floor
4.75 s: seesaw at -14.3°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.38, 0.00, 0.06) m, at rest; touching floor
(the same through 5.00 s)
5.25 s: seesaw at -14.2°, still; touching nothing | weight at (-1.66, 0.00, 0.12) m, at rest; touching floor | ball at (-1.38, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- seesaw at -14.2°, still; touching nothing
- weight at (-1.66, 0.00, 0.12) m, at rest; touching floor
- ball at (-1.38, 0.00, 0.06) m, at rest; touching floor
</history>
