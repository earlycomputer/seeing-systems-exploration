MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-1.05, 0.00, 3.05) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: flap1, flap1 ballast, flap1 mast, flap1 shaft, flap1.gate1, flap1 gate arm; starts at 0.0°, still
- block: free body; its geoms: block; starts at (-1.11, 0.60, 1.92) m, at rest
- flap2: hinge joint flap2_hinge about axis (0.00, 1.00, 0.00), range -48° to 0° as MuJoCo applies it; its geoms: flap2, flap2 ballast, flap2 mast, flap2 shaft, flap2.gate2, flap2 gate arm; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (-1.80, 1.20, 1.16) m, at rest

What happened, in order:
 0.00 s  flap1 starts at its upper stop (0°)
 0.00 s  flap2 starts at its upper stop (0°)
 0.01 s  ball1 starts moving
 0.01 s  block starts moving
 0.01 s  ball2 starts moving
 0.04 s  block first touches block rail left
 0.04 s  block first touches block rail right
 0.04 s  ball2 first touches ball rail left
 0.04 s  ball2 first touches ball rail right
 0.09 s  flap1 is at its largest, 0.0°
 0.09 s  flap1.gate1 first touches block
 0.12 s  flap2.gate2 first touches ball2
 0.18 s  flap1.gate1 leaves block
 0.26 s  flap1.gate1 touches block again
 0.28 s  flap2 is at its largest, 0.0°
 0.40 s  ball1 passes 0.13 m from hoop1 (hoop1_02) without touching it: nearest points (-1.02, 0.05, 2.26) m and (-0.95, 0.15, 2.25) m
 0.49 s  ball1 passes 0.46 m from block without touching it: nearest points (-1.05, 0.05, 1.87) m and (-1.05, 0.51, 1.87) m
 0.50 s  ball1 passes 0.47 m from block rail right without touching it: nearest points (-1.05, 0.05, 1.82) m and (-1.05, 0.52, 1.82) m
 0.50 s  flap1.gate1 leaves block
 0.51 s  ball1 first touches flap1
 0.54 s  ball1 leaves flap1
 0.61 s  flap1 passes 0.21 m from flap2 (flap2 ballast) without touching it: nearest points (-1.19, 0.12, 1.51) m and (-1.35, 0.23, 1.42) m
 0.65 s  flap1 reaches its lower stop (-40°) moving -258°/s
 0.67 s  flap1 is at its smallest, -41.9°
 0.68 s  ball1 touches flap1 again
 0.71 s  ball1 leaves flap1
 0.72 s  flap1 reaches its lower stop (-40°) again moving +27°/s
 0.75 s  ball1 touches flap1 again
 0.75 s  ball1 leaves flap1
 0.85 s  ball1 passes 0.17 m from flap2 (flap2 ballast) without touching it: nearest points (-1.31, 0.05, 1.36) m and (-1.37, 0.21, 1.39) m
 1.21 s  ball1 first touches floor
 1.26 s  block leaves block rail left
 1.26 s  block leaves block rail right
 1.27 s  ball1 leaves floor
 1.30 s  block touches block rail left again
 1.30 s  block touches block rail right again
 1.32 s  block leaves block rail left
 1.32 s  block leaves block rail right
 1.33 s  ball1 touches floor again
 1.55 s  block passes 0.46 m from ball2 without touching it: nearest points (-1.86, 0.69, 1.16) m and (-1.82, 1.15, 1.15) m
 1.58 s  block passes 0.46 m from ball rail right without touching it: nearest points (-1.88, 0.69, 1.08) m and (-1.88, 1.15, 1.08) m
 1.63 s  flap2.gate2 leaves ball2
 1.63 s  block first touches flap2
 1.88 s  block leaves flap2
 1.89 s  block passes 0.41 m from hoop2 (hoop2_14) without touching it: nearest points (-2.07, 0.68, 0.66) m and (-2.31, 1.01, 0.65) m
 1.91 s  flap2 passes 0.30 m from cup (cup_right_wall) without touching it: nearest points (-2.10, 0.72, 0.42) m and (-2.28, 0.94, 0.30) m
 1.99 s  flap2 reaches its lower stop (-48°) moving -171°/s
 2.00 s  block touches flap2 again
 2.01 s  flap2 is at its smallest, -49.1°
 2.01 s  flap2 passes 0.24 m from hoop2 (hoop2_00) without touching it: nearest points (-2.08, 1.20, 0.84) m and (-2.24, 1.20, 0.66) m
 2.01 s  block leaves flap2
 2.04 s  flap2 reaches its lower stop (-48°) again moving +18°/s
 2.05 s  block touches flap2 again
 2.05 s  block leaves flap2
 2.22 s  block first touches floor
 2.43 s  ball2 leaves ball rail left
 2.43 s  ball2 leaves ball rail right
 2.46 s  block comes to rest at (-2.22, 0.60, 0.06) m
 2.70 s  ball2 passes 0.16 m from hoop2 (hoop2_07) without touching it: nearest points (-2.59, 1.21, 0.59) m and (-2.74, 1.24, 0.65) m
 2.84 s  ball2 first touches cup_base
 2.87 s  ball2 leaves cup_base
 2.95 s  ball2 touches cup_base again
 3.23 s  ball2 comes to rest at (-2.83, 1.20, 0.07) m
 3.80 s  ball1 comes to rest at (-3.24, 0.00, 0.05) m
 6.00 s  block passes 0.25 m from cup (cup_right_wall) without touching it: nearest points (-2.27, 0.69, 0.00) m and (-2.27, 0.94, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-1.05, 0.00, 3.05) m, at rest; touching nothing | flap1 at 0.0°, still; touching nothing | block at (-1.11, 0.60, 1.92) m, at rest; touching nothing | flap2 at 0.0°, still; touching nothing | ball2 at (-1.80, 1.20, 1.16) m, at rest; touching nothing
0.25 s: ball1 at (-1.05, 0.00, 2.75) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | flap1 at -1.7°, turning -10°/s; touching nothing | block at (-1.12, 0.60, 1.88) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.02), turned 23° from how it started; touching block rail left, block rail right | flap2 at -0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
0.50 s: ball1 at (-1.05, 0.00, 1.83) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | flap1 at -3.3°, turning -3°/s; touching block | block at (-1.12, 0.60, 1.88) m, at rest, turned 23° from how it started; touching block rail left, block rail right, flap1.gate1 | flap2 at 0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
0.75 s: ball1 at (-1.16, 0.00, 1.49) m, moving 1.56 m/s (vx -1.28, vy -0.00, vz -0.90); touching flap1 | flap1 at -39.9°, turning +13°/s; touching ball1 | block at (-1.17, 0.60, 1.86) m, moving 0.40 m/s (vx -0.38, vy -0.00, vz -0.14), turned 23° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
1.00 s: ball1 at (-1.48, 0.00, 0.97) m, moving 3.55 m/s (vx -1.29, vy -0.00, vz -3.30); touching nothing | flap1 at -40.0°, still; touching nothing | block at (-1.31, 0.60, 1.80) m, moving 0.81 m/s (vx -0.75, vy -0.00, vz -0.30), turned 23° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
1.25 s: ball1 at (-1.80, 0.00, 0.05) m, moving 1.21 m/s (vx -1.09, vy -0.00, vz +0.51); touching floor | flap1 at -40.0°, still; touching nothing | block at (-1.54, 0.60, 1.70) m, moving 1.23 m/s (vx -1.12, vy -0.00, vz -0.51), turned 23° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
1.50 s: ball1 at (-2.07, 0.00, 0.05) m, moving 1.06 m/s (vx -1.06, vy -0.00, vz +0.01); touching floor | flap1 at -40.0°, still; touching nothing | block at (-1.84, 0.60, 1.37) m, moving 2.76 m/s (vx -1.21, vy +0.00, vz -2.49), turned 68° from how it started; touching nothing | flap2 at 0.0°, still; touching ball2 | ball2 at (-1.82, 1.20, 1.15) m, at rest; touching ball rail left, ball rail right, flap2.gate2
1.75 s: ball1 at (-2.32, 0.00, 0.05) m, moving 0.94 m/s (vx -0.93, vy -0.00, vz +0.02); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.00, 0.60, 0.85) m, moving 1.25 m/s (vx +0.06, vy +0.00, vz -1.25), turned 103° from how it started; touching nothing | flap2 at -12.9°, turning -118°/s; touching nothing | ball2 at (-1.83, 1.20, 1.15) m, moving 0.18 m/s (vx -0.17, vy -0.00, vz -0.05); touching ball rail left, ball rail right
2.00 s: ball1 at (-2.54, 0.00, 0.05) m, moving 0.81 m/s (vx -0.81, vy -0.00, vz -0.01); touching floor | flap1 at -40.0°, still; touching nothing | block at (-1.97, 0.60, 0.37) m, moving 2.05 m/s (vx -0.24, vy +0.00, vz -2.03), turned 141° from how it started; touching flap2 | flap2 at -49.0°, turning -34°/s; touching block | ball2 at (-1.91, 1.20, 1.12) m, moving 0.52 m/s (vx -0.50, vy -0.00, vz -0.12); touching ball rail left, ball rail right
2.25 s: ball1 at (-2.73, 0.00, 0.06) m, moving 0.69 m/s (vx -0.69, vy -0.00, vz -0.02); touching nothing | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.05) m, moving 0.50 m/s (vx -0.45, vy -0.00, vz +0.22), turned 178° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.08, 1.20, 1.07) m, moving 0.87 m/s (vx -0.83, vy -0.00, vz -0.27); touching nothing
2.50 s: ball1 at (-2.89, 0.00, 0.05) m, moving 0.57 m/s (vx -0.57, vy -0.00, vz +0.01); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.32, 1.20, 0.97) m, moving 1.46 m/s (vx -1.08, vy -0.00, vz -0.99); touching nothing
2.75 s: ball1 at (-3.01, 0.00, 0.05) m, moving 0.45 m/s (vx -0.45, vy -0.00, vz -0.00); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.59, 1.20, 0.42) m, moving 3.60 m/s (vx -1.08, vy -0.00, vz -3.44); touching nothing
3.00 s: ball1 at (-3.11, 0.00, 0.05) m, moving 0.33 m/s (vx -0.33, vy -0.00, vz +0.00); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.78, 1.20, 0.07) m, moving 0.43 m/s (vx -0.43, vy -0.00, vz -0.00); touching cup_base
3.25 s: ball1 at (-3.18, 0.00, 0.05) m, moving 0.20 m/s (vx -0.20, vy +0.00, vz +0.00); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.83, 1.20, 0.07) m, at rest; touching cup_base
3.50 s: ball1 at (-3.22, 0.00, 0.05) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz -0.00); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.83, 1.20, 0.07) m, at rest; touching cup_base
3.75 s: ball1 at (-3.24, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.83, 1.20, 0.07) m, at rest; touching cup_base
4.00 s: ball1 at (-3.25, 0.00, 0.05) m, at rest; touching floor | flap1 at -40.0°, still; touching nothing | block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor | flap2 at -48.0°, still; touching nothing | ball2 at (-2.83, 1.20, 0.07) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-3.25, 0.00, 0.05) m, at rest; touching floor
- flap1 at -40.0°, still; touching nothing
- block at (-2.22, 0.60, 0.06) m, at rest, turned 180° from how it started; touching floor
- flap2 at -48.0°, still; touching nothing
- ball2 at (-2.83, 1.20, 0.07) m, at rest; touching cup_base
</history>
