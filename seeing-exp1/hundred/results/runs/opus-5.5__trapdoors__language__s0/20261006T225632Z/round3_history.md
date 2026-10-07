MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 3.25) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: flap1; starts at 0.0°, still
- block: free body; its geoms: block; starts at (-0.42, 0.65, 1.99) m, at rest
- flap2: hinge joint flap2_hinge about axis (1.00, 0.00, 0.00), range -90.0002° to 0° as MuJoCo applies it; its geoms: flap2, flap2 weight; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (0.18, 0.50, 1.09) m, at rest

What happened, in order:
 0.00 s  flap1 starts at its upper stop (0°)
 0.00 s  flap2 starts at its upper stop (0°)
 0.00 s  flap1 first touches block
 0.00 s  flap2 first touches ball2
 0.01 s  ball1 starts moving
 0.03 s  flap2 is at its largest, 0.0°
 0.40 s  ball1 passes 0.16 m from hoop1 (hoop1_rim_01) without touching it: nearest points (0.05, 0.03, 2.46) m and (0.19, 0.12, 2.45) m
 0.50 s  flap1 leaves block
 0.50 s  ball1 first touches flap1
 0.51 s  block starts moving
 0.55 s  ball1 leaves flap1
 0.57 s  flap1 reaches its lower stop (-45°) moving -693°/s
 0.59 s  ball1 touches flap1 again
 0.59 s  flap1 is at its smallest, -49.9°
 0.59 s  flap1 passes 0.27 m from flap2 without touching it: nearest points (-0.21, 0.75, 1.32) m and (-0.20, 0.75, 1.05) m
 0.59 s  flap1 passes 0.41 m from ball2 without touching it: nearest points (-0.16, 0.50, 1.38) m and (0.15, 0.50, 1.12) m
 0.65 s  flap1 reaches its lower stop (-45°) again moving +91°/s
 0.75 s  ball1 leaves flap1
 0.80 s  ball1 passes 0.37 m from flap2 (flap2 weight) without touching it: nearest points (-0.45, 0.02, 1.30) m and (-0.20, 0.12, 1.05) m
 0.81 s  flap1 touches block again
 0.82 s  flap1 leaves block
 0.93 s  block passes 0.26 m from flap2 without touching it: nearest points (-0.45, 0.69, 1.14) m and (-0.20, 0.69, 1.05) m
 0.93 s  flap1 reaches its upper stop (0°) again moving +442°/s
 0.95 s  flap1 is at its largest, 2.9°
 1.02 s  flap1 reaches its upper stop (0°) again moving -17°/s
 1.12 s  ball1 first touches floor
 1.15 s  block first touches floor
 1.18 s  ball1 leaves floor
 1.28 s  ball1 touches floor again
 1.30 s  ball1 leaves floor
 1.33 s  ball1 touches floor again
 1.46 s  block comes to rest at (-0.77, 0.65, 0.04) m
 6.00 s  ball1 is still moving at the end, 0.25 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 3.25) m, at rest; touching nothing | flap1 at 0.0°, still; touching nothing | block at (-0.42, 0.65, 1.99) m, at rest; touching nothing | flap2 at 0.0°, still; touching nothing | ball2 at (0.18, 0.50, 1.09) m, at rest; touching nothing
0.25 s: ball1 at (0.00, 0.00, 2.95) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | flap1 at 0.0°, still; touching block | block at (-0.42, 0.65, 1.99) m, at rest; touching flap1 | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
0.50 s: ball1 at (0.00, 0.00, 2.03) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | flap1 at 0.0°, still; touching block | block at (-0.42, 0.65, 1.99) m, at rest; touching flap1 | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
0.75 s: ball1 at (-0.36, 0.00, 1.45) m, moving 3.12 m/s (vx -2.47, vy -0.00, vz -1.91); touching nothing | flap1 at -41.2°, turning +32°/s; touching nothing | block at (-0.42, 0.65, 1.69) m, moving 2.43 m/s (vx +0.00, vy +0.00, vz -2.43); touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
1.00 s: ball1 at (-0.98, 0.00, 0.67) m, moving 5.01 m/s (vx -2.47, vy -0.00, vz -4.36); touching nothing | flap1 at 0.9°, turning -30°/s; touching nothing | block at (-0.55, 0.65, 0.85) m, moving 4.53 m/s (vx -0.72, vy +0.00, vz -4.48), turned 137° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
1.25 s: ball1 at (-1.57, 0.00, 0.07) m, moving 2.27 m/s (vx -2.26, vy -0.00, vz -0.23); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.72, 0.65, 0.06) m, moving 0.39 m/s (vx -0.39, vy -0.00, vz +0.05), turned 121° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
1.50 s: ball1 at (-2.14, 0.00, 0.06) m, moving 2.27 m/s (vx -2.27, vy -0.00, vz -0.05); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
1.75 s: ball1 at (-2.69, 0.00, 0.06) m, moving 2.16 m/s (vx -2.16, vy -0.00, vz -0.03); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
2.00 s: ball1 at (-3.22, 0.00, 0.06) m, moving 2.05 m/s (vx -2.05, vy -0.00, vz +0.01); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
2.25 s: ball1 at (-3.72, 0.00, 0.06) m, moving 1.93 m/s (vx -1.93, vy -0.00, vz +0.03); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
2.50 s: ball1 at (-4.19, 0.00, 0.06) m, moving 1.82 m/s (vx -1.82, vy -0.00, vz +0.03); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
2.75 s: ball1 at (-4.63, 0.00, 0.06) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.03); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
3.00 s: ball1 at (-5.04, 0.00, 0.06) m, moving 1.60 m/s (vx -1.60, vy -0.00, vz -0.03); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
3.25 s: ball1 at (-5.43, 0.00, 0.06) m, moving 1.49 m/s (vx -1.49, vy -0.00, vz +0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
3.50 s: ball1 at (-5.78, 0.00, 0.06) m, moving 1.37 m/s (vx -1.37, vy -0.00, vz +0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
3.75 s: ball1 at (-6.11, 0.00, 0.06) m, moving 1.26 m/s (vx -1.26, vy -0.00, vz +0.00); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
4.00 s: ball1 at (-6.42, 0.00, 0.06) m, moving 1.15 m/s (vx -1.15, vy -0.00, vz +0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
4.25 s: ball1 at (-6.69, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy -0.00, vz -0.01); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
4.50 s: ball1 at (-6.93, 0.00, 0.06) m, moving 0.93 m/s (vx -0.93, vy -0.00, vz -0.02); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
4.75 s: ball1 at (-7.15, 0.00, 0.06) m, moving 0.81 m/s (vx -0.81, vy -0.00, vz +0.00); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
5.00 s: ball1 at (-7.34, 0.00, 0.06) m, moving 0.70 m/s (vx -0.70, vy -0.00, vz -0.01); touching nothing | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
5.25 s: ball1 at (-7.50, 0.00, 0.06) m, moving 0.59 m/s (vx -0.59, vy -0.00, vz +0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
5.50 s: ball1 at (-7.64, 0.00, 0.06) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz +0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
5.75 s: ball1 at (-7.74, 0.00, 0.06) m, moving 0.36 m/s (vx -0.36, vy -0.00, vz -0.01); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
6.00 s: ball1 at (-7.82, 0.00, 0.06) m, moving 0.25 m/s (vx -0.25, vy -0.00, vz +0.00); touching floor | flap1 at 0.1°, still; touching nothing | block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor | flap2 at 0.0°, still; touching ball2 | ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2

At the end (6.00 s):
- ball1 at (-7.82, 0.00, 0.06) m, moving 0.25 m/s (vx -0.25, vy -0.00, vz +0.00); touching floor
- flap1 at 0.1°, still; touching nothing
- block at (-0.77, 0.65, 0.04) m, at rest, turned 180° from how it started; touching floor
- flap2 at 0.0°, still; touching ball2
- ball2 at (0.18, 0.50, 1.09) m, at rest; touching flap2
</history>
