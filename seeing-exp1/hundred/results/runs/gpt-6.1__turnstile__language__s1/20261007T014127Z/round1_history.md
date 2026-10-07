MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-0.83, 0.00, 1.01) m, at rest
- rotor: hinge joint rotor_hinge about axis (0.00, 0.00, 1.00), range 0° to 24° as MuJoCo applies it; its geoms: rotor; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (0.40, -0.35, 0.51) m, at rest
- latch: free body; its geoms: latch; starts at (0.82, -0.15, 0.54) m, at rest
- block: free body; its geoms: block; starts at (0.82, 0.00, 0.66) m, at rest

What happened, in order:
 0.00 s  latch starts touching block
 0.00 s  ball1 starts touching ramp_deck
 0.00 s  rotor starts at its lower stop (0°)
 0.00 s  latch first touches right lower rail
 0.00 s  latch first touches left lower rail
 0.00 s  ball2 first touches runout
 0.02 s  ball1 starts moving
 0.75 s  ball1 leaves ramp_deck
 0.75 s  ball1 first touches runout
 0.82 s  ball1 first touches rotor
 0.82 s  ball1 leaves runout
 0.83 s  ball2 leaves runout
 0.83 s  rotor first touches ball2
 0.83 s  ball2 starts moving
 0.84 s  ball1 passes 0.29 m from ball2 without touching it: nearest points (0.25, -0.05, 0.53) m and (0.38, -0.30, 0.51) m
 0.86 s  ball1 leaves rotor
 0.87 s  ball2 touches runout again
 0.87 s  rotor leaves ball2
 0.87 s  ball2 leaves runout
 0.91 s  ball2 touches runout again
 0.93 s  rotor reaches its upper stop (24°) moving +152°/s
 0.93 s  ball2 first touches striker runway
 0.95 s  rotor is at its largest, 25.1°
 0.95 s  rotor passes 0.04 m from striker runway without touching it: nearest points (0.54, -0.33, 0.46) m and (0.58, -0.33, 0.46) m
 0.95 s  rotor passes 0.16 m from latch without touching it: nearest points (0.54, -0.33, 0.53) m and (0.70, -0.33, 0.53) m
 0.95 s  rotor passes 0.22 m from ring (ring_08) without touching it: nearest points (0.46, -0.16, 0.46) m and (0.60, -0.09, 0.31) m
 0.95 s  rotor passes 0.29 m from payload near guide without touching it: nearest points (0.48, -0.20, 0.57) m and (0.74, -0.08, 0.62) m
 0.95 s  rotor passes 0.36 m from payload left guide without touching it: nearest points (0.43, -0.09, 0.57) m and (0.75, 0.06, 0.61) m
 0.95 s  rotor passes 0.30 m from payload right guide without touching it: nearest points (0.48, -0.20, 0.57) m and (0.75, -0.08, 0.61) m
 0.95 s  rotor passes 0.29 m from box (box_near_wall) without touching it: nearest points (0.52, -0.28, 0.47) m and (0.53, -0.28, 0.18) m
 0.95 s  rotor passes 0.33 m from block without touching it: nearest points (0.48, -0.19, 0.57) m and (0.77, -0.05, 0.61) m
 0.95 s  rotor passes 0.41 m from payload far guide without touching it: nearest points (0.51, -0.25, 0.57) m and (0.88, -0.08, 0.61) m
 0.95 s  ball2 first touches latch
 0.95 s  latch starts moving
 0.96 s  ball2 leaves runout
 0.96 s  ball2 leaves striker runway
 0.97 s  ball1 touches runout again
 0.97 s  ball1 touches rotor again
 0.97 s  ball1 passes 0.23 m from left lower rail without touching it: nearest points (0.34, 0.00, 0.51) m and (0.55, 0.09, 0.47) m
 0.97 s  ball1 passes 0.24 m from left rail cap without touching it: nearest points (0.34, 0.00, 0.54) m and (0.55, 0.09, 0.61) m
 0.97 s  ball1 passes 0.25 m from left channel wall without touching it: nearest points (0.34, 0.01, 0.52) m and (0.55, 0.14, 0.52) m
 0.97 s  ball1 passes 0.36 m from latch without touching it: nearest points (0.35, -0.01, 0.52) m and (0.71, 0.01, 0.52) m
 0.97 s  latch first touches left channel wall
 0.98 s  ball1 passes 0.30 m from ring (ring_07) without touching it: nearest points (0.34, -0.02, 0.48) m and (0.58, 0.00, 0.31) m
 0.98 s  ball1 passes 0.42 m from payload left guide without touching it: nearest points (0.35, -0.01, 0.53) m and (0.75, 0.06, 0.61) m
 0.98 s  latch first touches right channel wall
 0.99 s  ball2 touches striker runway again
 0.99 s  ball1 leaves rotor
 1.00 s  ball2 leaves latch
 1.01 s  rotor reaches its upper stop (24°) again moving -15°/s
 1.01 s  latch leaves left channel wall
 1.02 s  latch leaves right channel wall
 1.08 s  block starts moving
 1.08 s  ball2 passes 0.16 m from payload near guide without touching it: nearest points (0.79, -0.22, 0.53) m and (0.76, -0.08, 0.61) m
 1.09 s  latch leaves block
 1.09 s  rotor passes 0.06 m from right lower rail without touching it: nearest points (0.53, -0.34, 0.47) m and (0.55, -0.39, 0.47) m
 1.09 s  rotor passes 0.08 m from right rail cap without touching it: nearest points (0.53, -0.34, 0.57) m and (0.55, -0.39, 0.61) m
 1.18 s  ball2 passes 0.15 m from ring (ring_12) without touching it: nearest points (0.90, -0.24, 0.46) m and (0.89, -0.22, 0.31) m
 1.20 s  block first touches payload near guide
 1.20 s  rotor passes 0.10 m from right channel wall without touching it: nearest points (0.51, -0.35, 0.52) m and (0.55, -0.44, 0.52) m
 1.20 s  block leaves payload near guide
 1.21 s  ball2 passes 0.14 m from payload right guide without touching it: nearest points (0.92, -0.19, 0.54) m and (0.89, -0.08, 0.61) m
 1.22 s  ball2 passes 0.14 m from payload far guide without touching it: nearest points (0.93, -0.19, 0.54) m and (0.90, -0.08, 0.61) m
 1.23 s  ball2 passes 0.14 m from block without touching it: nearest points (0.93, -0.18, 0.51) m and (0.89, -0.05, 0.51) m
 1.24 s  ball2 passes 0.26 m from payload left guide without touching it: nearest points (0.95, -0.18, 0.53) m and (0.89, 0.06, 0.61) m
 1.26 s  block passes 0.04 m from left lower rail without touching it: nearest points (0.80, 0.05, 0.43) m and (0.80, 0.09, 0.43) m
 1.26 s  ball1 passes 0.41 m from block without touching it: nearest points (0.36, -0.11, 0.52) m and (0.76, -0.05, 0.52) m
 1.29 s  latch touches right channel wall again
 1.31 s  latch touches left channel wall again
 1.31 s  ball1 passes 0.39 m from payload near guide without touching it: nearest points (0.36, -0.12, 0.53) m and (0.74, -0.08, 0.61) m
 1.31 s  ball1 passes 0.40 m from payload right guide without touching it: nearest points (0.36, -0.12, 0.53) m and (0.75, -0.08, 0.61) m
 1.33 s  latch leaves right channel wall
 1.33 s  latch leaves left channel wall
 1.34 s  block passes 0.12 m from ring (ring_01) without touching it: nearest points (0.90, 0.05, 0.31) m and (1.00, 0.12, 0.30) m
 1.41 s  ball2 leaves striker runway
 1.42 s  block first touches box_base
 1.44 s  ball2 passes 0.25 m from left rail cap without touching it: nearest points (1.15, -0.13, 0.50) m and (1.15, 0.09, 0.61) m
 1.52 s  ball2 passes 0.24 m from left channel wall without touching it: nearest points (1.23, -0.09, 0.40) m and (1.23, 0.14, 0.46) m
 1.53 s  ball2 passes 0.18 m from left lower rail without touching it: nearest points (1.24, -0.09, 0.39) m and (1.24, 0.09, 0.43) m
 1.57 s  ball1 touches rotor again
 1.57 s  ball1 leaves rotor
 1.59 s  ball2 passes 0.16 m from box (box_far_wall) without touching it: nearest points (1.25, -0.11, 0.24) m and (1.11, -0.11, 0.18) m
 1.60 s  latch first touches latch end stop
 1.63 s  block comes to rest at (0.89, 0.00, 0.07) m
 1.65 s  latch leaves latch end stop
 1.68 s  ball2 first touches floor
 2.05 s  latch touches left channel wall again
 2.10 s  latch leaves left channel wall
 2.12 s  ball2 passes 0.35 m from latch end stop without touching it: nearest points (1.78, 0.09, 0.10) m and (1.78, 0.09, 0.45) m
 2.13 s  latch touches right channel wall again
 2.16 s  latch touches left channel wall again
 2.18 s  latch leaves left channel wall
 2.18 s  latch leaves right channel wall
 2.26 s  latch comes to rest at (1.57, -0.15, 0.54) m
 2.27 s  ball1 passes 0.20 m from striker runway without touching it: nearest points (0.39, -0.44, 0.51) m and (0.58, -0.42, 0.46) m
 2.29 s  ball1 passes 0.16 m from right lower rail without touching it: nearest points (0.39, -0.45, 0.51) m and (0.55, -0.43, 0.47) m
 2.29 s  ball1 passes 0.18 m from right rail cap without touching it: nearest points (0.39, -0.45, 0.54) m and (0.55, -0.43, 0.62) m
 2.38 s  ball1 passes 0.15 m from right channel wall without touching it: nearest points (0.40, -0.48, 0.52) m and (0.55, -0.46, 0.52) m
 2.56 s  ball1 leaves runout
 2.74 s  ball1 passes 0.33 m from box (box_right_wall) without touching it: nearest points (0.38, -0.57, 0.24) m and (0.54, -0.29, 0.18) m
 2.81 s  ball1 first touches floor
 6.00 s  ball1 is still moving at the end, 0.08 m/s
 6.00 s  ball2 is still moving at the end, 0.16 m/s

State every 0.25 s:
0.00 s: ball1 at (-0.83, 0.00, 1.01) m, at rest; touching ramp_deck | rotor at 0.0°, still; touching nothing | ball2 at (0.40, -0.35, 0.51) m, at rest; touching nothing | latch at (0.82, -0.15, 0.54) m, at rest; touching block | block at (0.82, 0.00, 0.66) m, at rest; touching latch
0.25 s: ball1 at (-0.74, 0.00, 0.96) m, moving 0.88 m/s (vx +0.76, vy +0.00, vz -0.44); touching ramp_deck | rotor at 0.0°, still; touching nothing | ball2 at (0.40, -0.35, 0.51) m, at rest; touching runout | latch at (0.82, -0.15, 0.54) m, at rest; touching block, left lower rail, right lower rail | block at (0.82, 0.00, 0.66) m, at rest; touching latch
0.50 s: ball1 at (-0.45, 0.00, 0.79) m, moving 1.75 m/s (vx +1.52, vy +0.00, vz -0.88); touching ramp_deck | rotor at 0.0°, still; touching nothing | ball2 at (0.40, -0.35, 0.51) m, at rest; touching runout | latch at (0.82, -0.15, 0.54) m, at rest; touching block, left lower rail, right lower rail | block at (0.82, 0.00, 0.66) m, at rest; touching latch
0.75 s: ball1 at (0.02, 0.00, 0.52) m, moving 2.48 m/s (vx +2.29, vy +0.00, vz -0.94); touching ramp_deck, runout | rotor at 0.0°, still; touching nothing | ball2 at (0.40, -0.35, 0.51) m, at rest; touching runout | latch at (0.82, -0.15, 0.54) m, at rest; touching block, left lower rail, right lower rail | block at (0.82, 0.00, 0.66) m, at rest; touching latch
1.00 s: ball1 at (0.29, -0.03, 0.52) m, moving 0.36 m/s (vx +0.01, vy -0.35, vz +0.09); touching runout | rotor at 24.6°, turning -15°/s; touching nothing | ball2 at (0.71, -0.28, 0.51) m, moving 1.14 m/s (vx +1.09, vy +0.30, vz +0.09); touching striker runway | latch at (0.87, -0.15, 0.54) m, moving 1.34 m/s (vx +1.34, vy -0.01, vz +0.00), turned 6° from how it started; touching block, left channel wall, left lower rail, right channel wall, right lower rail | block at (0.82, 0.00, 0.66) m, at rest; touching latch
1.25 s: ball1 at (0.30, -0.11, 0.52) m, moving 0.33 m/s (vx +0.04, vy -0.33, vz -0.00); touching runout | rotor at 21.1°, turning -13°/s; touching nothing | ball2 at (0.96, -0.23, 0.51) m, moving 1.01 m/s (vx +0.99, vy +0.22, vz +0.00); touching striker runway | latch at (1.19, -0.15, 0.54) m, moving 1.25 m/s (vx +1.25, vy -0.00, vz +0.01), turned 3° from how it started; touching left lower rail, right lower rail | block at (0.82, 0.00, 0.52) m, moving 1.69 m/s (vx +0.04, vy +0.00, vz -1.69), turned 22° from how it started; touching nothing
1.50 s: ball1 at (0.31, -0.19, 0.52) m, moving 0.33 m/s (vx +0.04, vy -0.33, vz -0.00); touching runout | rotor at 17.9°, turning -12°/s; touching nothing | ball2 at (1.21, -0.15, 0.42) m, moving 1.64 m/s (vx +0.97, vy +0.39, vz -1.27); touching nothing | latch at (1.50, -0.15, 0.54) m, moving 1.21 m/s (vx +1.21, vy -0.01, vz +0.01), turned 4° from how it started; touching left lower rail, right lower rail | block at (0.86, 0.01, 0.09) m, moving 0.39 m/s (vx +0.37, vy +0.00, vz -0.15), turned 19° from how it started; touching box_base
1.75 s: ball1 at (0.32, -0.27, 0.52) m, moving 0.33 m/s (vx +0.03, vy -0.33, vz -0.00); touching runout | rotor at 16.0°, turning -6°/s; touching nothing | ball2 at (1.45, -0.05, 0.05) m, moving 1.00 m/s (vx +0.93, vy +0.38, vz +0.06); touching floor | latch at (1.62, -0.16, 0.54) m, moving 0.12 m/s (vx -0.12, vy +0.02, vz +0.00), turned 1° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
2.00 s: ball1 at (0.32, -0.36, 0.52) m, moving 0.33 m/s (vx +0.03, vy -0.33, vz -0.00); touching runout | rotor at 14.6°, turning -5°/s; touching nothing | ball2 at (1.68, 0.04, 0.05) m, moving 0.96 m/s (vx +0.88, vy +0.38, vz +0.01); touching floor | latch at (1.59, -0.15, 0.54) m, moving 0.09 m/s (vx -0.09, vy +0.02, vz +0.00), turned 4° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
2.25 s: ball1 at (0.33, -0.44, 0.52) m, moving 0.33 m/s (vx +0.03, vy -0.33, vz -0.00); touching runout | rotor at 13.3°, turning -5°/s; touching nothing | ball2 at (1.89, 0.14, 0.05) m, moving 0.90 m/s (vx +0.82, vy +0.38, vz +0.00); touching floor | latch at (1.57, -0.15, 0.54) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00), turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
2.50 s: ball1 at (0.34, -0.52, 0.52) m, moving 0.41 m/s (vx +0.04, vy -0.38, vz -0.15); touching runout | rotor at 12.2°, turning -4°/s; touching nothing | ball2 at (2.08, 0.23, 0.05) m, moving 0.84 m/s (vx +0.75, vy +0.38, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
2.75 s: ball1 at (0.35, -0.63, 0.23) m, moving 2.41 m/s (vx +0.04, vy -0.44, vz -2.37); touching nothing | rotor at 11.1°, turning -4°/s; touching nothing | ball2 at (2.27, 0.33, 0.05) m, moving 0.79 m/s (vx +0.69, vy +0.37, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
3.00 s: ball1 at (0.36, -0.74, 0.06) m, moving 0.43 m/s (vx +0.03, vy -0.43, vz +0.00); touching floor | rotor at 10.2°, turning -4°/s; touching nothing | ball2 at (2.43, 0.42, 0.05) m, moving 0.73 m/s (vx +0.64, vy +0.36, vz +0.01); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
3.25 s: ball1 at (0.37, -0.84, 0.06) m, moving 0.38 m/s (vx +0.03, vy -0.38, vz -0.00); touching floor | rotor at 9.3°, turning -3°/s; touching nothing | ball2 at (2.59, 0.51, 0.05) m, moving 0.68 m/s (vx +0.59, vy +0.34, vz +0.01); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
3.50 s: ball1 at (0.37, -0.93, 0.06) m, moving 0.34 m/s (vx +0.02, vy -0.34, vz -0.00); touching floor | rotor at 8.4°, turning -3°/s; touching nothing | ball2 at (2.73, 0.59, 0.05) m, moving 0.63 m/s (vx +0.54, vy +0.33, vz +0.01); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
3.75 s: ball1 at (0.38, -1.01, 0.06) m, moving 0.30 m/s (vx +0.02, vy -0.30, vz -0.00); touching floor | rotor at 7.7°, turning -3°/s; touching nothing | ball2 at (2.85, 0.67, 0.05) m, moving 0.58 m/s (vx +0.49, vy +0.31, vz +0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
4.00 s: ball1 at (0.38, -1.08, 0.06) m, moving 0.26 m/s (vx +0.01, vy -0.26, vz -0.00); touching floor | rotor at 7.0°, turning -3°/s; touching nothing | ball2 at (2.97, 0.74, 0.05) m, moving 0.53 m/s (vx +0.44, vy +0.29, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
4.25 s: ball1 at (0.38, -1.14, 0.06) m, moving 0.23 m/s (vx +0.01, vy -0.23, vz -0.00); touching floor | rotor at 6.4°, turning -2°/s; touching nothing | ball2 at (3.07, 0.81, 0.05) m, moving 0.48 m/s (vx +0.40, vy +0.26, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
4.50 s: ball1 at (0.39, -1.19, 0.06) m, moving 0.20 m/s (vx +0.01, vy -0.20, vz -0.00); touching floor | rotor at 5.8°, turning -2°/s; touching nothing | ball2 at (3.17, 0.88, 0.05) m, moving 0.43 m/s (vx +0.35, vy +0.24, vz +0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
4.75 s: ball1 at (0.39, -1.24, 0.06) m, moving 0.17 m/s (vx +0.01, vy -0.17, vz -0.00); touching floor | rotor at 5.3°, turning -2°/s; touching nothing | ball2 at (3.25, 0.93, 0.05) m, moving 0.38 m/s (vx +0.31, vy +0.22, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
5.00 s: ball1 at (0.39, -1.28, 0.06) m, moving 0.15 m/s (vx +0.01, vy -0.15, vz -0.00); touching floor | rotor at 4.8°, turning -2°/s; touching nothing | ball2 at (3.32, 0.98, 0.05) m, moving 0.33 m/s (vx +0.27, vy +0.19, vz +0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
5.25 s: ball1 at (0.39, -1.31, 0.06) m, moving 0.13 m/s (vx +0.00, vy -0.13, vz -0.00); touching floor | rotor at 4.4°, turning -2°/s; touching nothing | ball2 at (3.39, 1.03, 0.05) m, moving 0.28 m/s (vx +0.23, vy +0.16, vz +0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
5.50 s: ball1 at (0.39, -1.34, 0.06) m, moving 0.11 m/s (vx +0.00, vy -0.11, vz -0.00); touching floor | rotor at 4.0°, turning -2°/s; touching nothing | ball2 at (3.44, 1.07, 0.05) m, moving 0.24 m/s (vx +0.19, vy +0.14, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
5.75 s: ball1 at (0.39, -1.37, 0.06) m, moving 0.09 m/s (vx +0.00, vy -0.09, vz -0.00); touching floor | rotor at 3.6°, turning -1°/s; touching nothing | ball2 at (3.48, 1.10, 0.05) m, moving 0.20 m/s (vx +0.16, vy +0.11, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
6.00 s: ball1 at (0.39, -1.39, 0.06) m, moving 0.08 m/s (vx +0.00, vy -0.08, vz -0.00); touching floor | rotor at 3.2°, turning -1°/s; touching nothing | ball2 at (3.52, 1.12, 0.05) m, moving 0.16 m/s (vx +0.13, vy +0.09, vz -0.00); touching floor | latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail | block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base

At the end (6.00 s):
- ball1 at (0.39, -1.39, 0.06) m, moving 0.08 m/s (vx +0.00, vy -0.08, vz -0.00); touching floor
- rotor at 3.2°, turning -1°/s; touching nothing
- ball2 at (3.52, 1.12, 0.05) m, moving 0.16 m/s (vx +0.13, vy +0.09, vz -0.00); touching floor
- latch at (1.57, -0.15, 0.54) m, at rest, turned 5° from how it started; touching left lower rail, right lower rail
- block at (0.89, 0.00, 0.07) m, at rest, turned 11° from how it started; touching box_base
</history>
