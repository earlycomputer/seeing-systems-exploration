MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -30° to 0° as MuJoCo applies it; its geoms: seesaw.plank, seesaw.lip_ball, seesaw.lip_weight; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.82, 0.00, 3.00) m, at rest
- ball: free body; its geoms: ball; starts at (0.88, 0.00, 0.13) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (0°)
 0.01 s  weight starts moving
 0.01 s  ball starts moving
 0.02 s  seesaw.plank first touches ball
 0.14 s  seesaw.lip_ball first touches ball
 0.20 s  seesaw is at its largest, 0.0°
 0.69 s  seesaw.lip_weight first touches weight
 0.70 s  seesaw.lip_weight leaves weight
 0.70 s  seesaw.plank first touches weight
 0.79 s  seesaw.plank leaves ball
 0.79 s  seesaw reaches its lower stop (-30°) moving -334°/s
 0.80 s  seesaw.plank first touches floor
 0.81 s  seesaw.lip_ball leaves ball
 0.81 s  seesaw is at its smallest, -32.5°
 0.85 s  seesaw.plank leaves floor
 0.87 s  seesaw reaches its lower stop (-30°) again moving +35°/s
 1.00 s  seesaw reaches its lower stop (-30°) again moving -20°/s
 1.17 s  ball is at the top of its flight, at (-0.04, 0.00, 1.29) m
 1.29 s  seesaw.lip_weight touches weight again
 1.35 s  weight comes to rest at (-0.86, 0.00, 0.17) m
 1.61 s  weight passes 0.18 m from ball without touching it: nearest points (-0.92, 0.00, 0.22) m and (-1.07, 0.00, 0.31) m
 1.68 s  ball first touches floor
 2.05 s  ball comes to rest at (-1.38, 0.00, 0.04) m

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | weight at (-0.82, 0.00, 3.00) m, at rest; touching nothing | ball at (0.88, 0.00, 0.13) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.82, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.88, 0.00, 0.12) m, at rest; touching seesaw.lip_ball, seesaw.plank
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-0.82, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.88, 0.00, 0.12) m, at rest; touching seesaw.lip_ball, seesaw.plank
0.75 s: seesaw at -15.3°, turning -326°/s; touching ball, weight | weight at (-0.78, 0.00, 0.39) m, moving 4.03 m/s (vx +0.85, vy +0.00, vz -3.94); touching seesaw.plank | ball at (0.91, 0.00, 0.35) m, moving 5.16 m/s (vx -0.20, vy -0.00, vz +5.16); touching seesaw.lip_ball, seesaw.plank
1.00 s: seesaw at -29.4°, turning -19°/s; touching weight | weight at (-0.75, 0.00, 0.21) m, moving 0.33 m/s (vx -0.16, vy -0.00, vz -0.29); touching seesaw.plank | ball at (0.37, 0.00, 1.15) m, moving 2.94 m/s (vx -2.42, vy +0.00, vz +1.67); touching nothing
1.25 s: seesaw at -30.0°, still; touching weight | weight at (-0.84, 0.00, 0.18) m, moving 0.51 m/s (vx -0.49, vy +0.00, vz -0.13); touching seesaw.plank | ball at (-0.23, 0.00, 1.26) m, moving 2.54 m/s (vx -2.42, vy +0.00, vz -0.78); touching nothing
1.50 s: seesaw at -30.0°, still; touching weight | weight at (-0.86, 0.00, 0.17) m, at rest; touching seesaw.lip_weight, seesaw.plank | ball at (-0.84, 0.00, 0.76) m, moving 4.04 m/s (vx -2.42, vy +0.00, vz -3.24); touching nothing
1.75 s: seesaw at -30.0°, still; touching weight | weight at (-0.86, 0.00, 0.17) m, at rest; touching seesaw.lip_weight, seesaw.plank | ball at (-1.31, 0.00, 0.04) m, moving 0.48 m/s (vx -0.40, vy +0.00, vz +0.27); touching floor
2.00 s: seesaw at -30.0°, still; touching weight | weight at (-0.86, 0.00, 0.17) m, at rest; touching seesaw.lip_weight, seesaw.plank | ball at (-1.37, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching floor
2.25 s: seesaw at -30.0°, still; touching weight | weight at (-0.86, 0.00, 0.17) m, at rest; touching seesaw.lip_weight, seesaw.plank | ball at (-1.38, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- seesaw at -30.0°, still; touching weight
- weight at (-0.86, 0.00, 0.17) m, at rest; touching seesaw.lip_weight, seesaw.plank
- ball at (-1.38, 0.00, 0.04) m, at rest; touching floor
</history>
