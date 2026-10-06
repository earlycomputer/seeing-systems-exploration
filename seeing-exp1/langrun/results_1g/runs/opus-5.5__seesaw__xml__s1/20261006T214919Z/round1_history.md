Your expectations, checked against the run (2 of 3 hold):

- holds: weight touches seesaw (first touch at 0.53 s)
- holds: seesaw reaches its upper stop (at its upper stop (17°) at 0.58 s)
- DOES NOT HOLD: ball rises at least 0.5 m above its start (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -17.19° to 17.19° as MuJoCo applies it; its geoms: seesaw_plank, seesaw_lip; starts at -17.1°, still
- weight: free body; its geoms: weight; starts at (0.38, 0.00, 1.80) m, at rest
- ball: free body; its geoms: ball; starts at (-0.44, 0.00, 0.16) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its lower stop (-17.19°)
 0.01 s  weight starts moving
 0.01 s  ball starts moving
 0.01 s  seesaw_plank first touches ball
 0.01 s  seesaw_lip first touches ball
 0.53 s  seesaw_plank first touches weight
 0.58 s  seesaw reaches its upper stop (17.19°) moving +778°/s
 0.59 s  seesaw_plank leaves ball
 0.59 s  weight passes 0.30 m from base (base_post) without touching it: nearest points (0.33, 0.00, 0.17) m and (0.03, 0.00, 0.17) m
 0.60 s  seesaw_lip leaves ball
 0.61 s  seesaw is at its largest, 23.5°
 0.69 s  seesaw reaches its upper stop (17.19°) again moving -35°/s
 0.71 s  seesaw_plank leaves weight
 0.84 s  weight first touches floor
 0.96 s  ball is at the top of its flight, at (0.67, 0.00, 1.11) m
 1.28 s  seesaw reaches its lower stop (-17.19°) again moving -100°/s
 1.30 s  seesaw is at its smallest, -17.9°
 1.32 s  seesaw reaches its lower stop (-17.19°) again moving +12°/s
 1.43 s  ball first touches floor
 3.35 s  weight first touches ball
 3.35 s  weight leaves floor
 3.53 s  weight touches floor again
 3.53 s  weight leaves ball
 6.00 s  weight is still moving at the end, 0.06 m/s
 6.00 s  ball is still moving at the end, 0.48 m/s

State every 0.25 s:
0.00 s: seesaw at -17.1°, still; touching nothing | weight at (0.38, 0.00, 1.80) m, at rest; touching nothing | ball at (-0.44, 0.00, 0.16) m, at rest; touching nothing
0.25 s: seesaw at -17.2°, still; touching ball | weight at (0.38, 0.00, 1.50) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (-0.44, 0.00, 0.15) m, at rest; touching seesaw_lip, seesaw_plank
0.50 s: seesaw at -17.2°, still; touching ball | weight at (0.38, 0.00, 0.58) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (-0.44, 0.00, 0.15) m, at rest; touching seesaw_lip, seesaw_plank
0.75 s: seesaw at 16.3°, turning -26°/s; touching nothing | weight at (0.55, 0.00, 0.14) m, moving 1.34 m/s (vx +1.17, vy +0.00, vz -0.64); touching nothing | ball at (0.05, 0.00, 0.90) m, moving 3.62 m/s (vx +3.00, vy +0.00, vz +2.02); touching nothing
1.00 s: seesaw at 5.5°, turning -60°/s; touching nothing | weight at (0.84, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (0.80, 0.00, 1.10) m, moving 3.04 m/s (vx +3.00, vy +0.00, vz -0.43); touching nothing
1.25 s: seesaw at -14.1°, turning -96°/s; touching nothing | weight at (1.14, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (1.55, 0.00, 0.69) m, moving 4.17 m/s (vx +3.00, vy +0.00, vz -2.89); touching nothing
1.50 s: seesaw at -17.2°, still; touching nothing | weight at (1.43, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz -0.00); touching floor | ball at (2.16, 0.00, 0.02) m, moving 0.82 m/s (vx +0.75, vy +0.00, vz +0.33); touching floor
1.75 s: seesaw at -17.2°, still; touching nothing | weight at (1.72, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz -0.00); touching floor | ball at (2.36, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz -0.00); touching floor
2.00 s: seesaw at -17.2°, still; touching nothing | weight at (2.02, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz -0.00); touching floor | ball at (2.57, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz -0.00); touching floor
2.25 s: seesaw at -17.2°, still; touching nothing | weight at (2.31, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz -0.00); touching floor | ball at (2.77, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz -0.00); touching floor
2.50 s: seesaw at -17.2°, still; touching nothing | weight at (2.61, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (2.98, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz +0.00); touching floor
2.75 s: seesaw at -17.2°, still; touching nothing | weight at (2.90, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (3.19, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz +0.00); touching floor
3.00 s: seesaw at -17.2°, still; touching nothing | weight at (3.19, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (3.39, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz +0.00); touching floor
3.25 s: seesaw at -17.2°, still; touching nothing | weight at (3.49, 0.00, 0.05) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.00); touching floor | ball at (3.60, 0.00, 0.03) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz +0.00); touching floor
3.50 s: seesaw at -17.2°, still; touching nothing | weight at (3.69, 0.00, 0.06) m, moving 0.48 m/s (vx +0.38, vy -0.00, vz -0.29); touching ball | ball at (3.76, 0.00, 0.03) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz +0.00); touching floor, weight
3.75 s: seesaw at -17.2°, still; touching nothing | weight at (3.70, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (3.88, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
4.00 s: seesaw at -17.2°, still; touching nothing | weight at (3.68, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.00, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz +0.00); touching floor
4.25 s: seesaw at -17.2°, still; touching nothing | weight at (3.67, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor | ball at (4.12, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
4.50 s: seesaw at -17.2°, still; touching nothing | weight at (3.65, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.24, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz +0.00); touching floor
4.75 s: seesaw at -17.2°, still; touching nothing | weight at (3.64, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.36, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz +0.00); touching floor
5.00 s: seesaw at -17.2°, still; touching nothing | weight at (3.63, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.48, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
5.25 s: seesaw at -17.2°, still; touching nothing | weight at (3.61, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor | ball at (4.60, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
5.50 s: seesaw at -17.2°, still; touching nothing | weight at (3.60, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching floor | ball at (4.72, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at -17.2°, still; touching nothing | weight at (3.58, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.84, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
6.00 s: seesaw at -17.2°, still; touching nothing | weight at (3.57, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball at (4.96, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at -17.2°, still; touching nothing
- weight at (3.57, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor
- ball at (4.96, 0.00, 0.03) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor
</history>
