MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.04, 0.00, 0.15) m, at rest
- domino2: free body; its geoms: domino2_geom; starts at (0.11, 0.00, 0.15) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.22, 0.00, 0.15) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.33, 0.00, 0.15) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.44, 0.00, 0.15) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.55, 0.00, 0.15) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.66, 0.00, 0.15) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.77, 0.00, 0.15) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.88, 0.00, 0.15) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (0.99, 0.00, 0.15) m, at rest

What happened, in order:
 0.00 s  domino1_geom starts touching floor
 0.00 s  domino7_geom starts touching floor
 0.00 s  domino4_geom starts touching floor
 0.00 s  domino10_geom starts touching floor
 0.00 s  domino3_geom starts touching floor
 0.00 s  domino9_geom starts touching floor
 0.00 s  domino6_geom starts touching floor
 0.00 s  domino2_geom starts touching floor
 0.00 s  domino5_geom starts touching floor
 0.00 s  domino8_geom starts touching floor
 0.04 s  domino1 starts moving
 0.05 s  domino1_geom first touches domino2_geom
 0.15 s  domino2 starts moving
 0.42 s  domino2_geom first touches domino3_geom
 0.42 s  domino3 starts moving
 0.43 s  domino1_geom leaves domino2_geom
 0.43 s  domino2_geom leaves domino3_geom
 0.46 s  domino1_geom touches domino2_geom again
 0.48 s  domino2_geom touches domino3_geom again
 0.56 s  domino3_geom first touches domino4_geom
 0.56 s  domino4 starts moving
 0.58 s  domino3_geom leaves domino4_geom
 0.58 s  domino2_geom leaves domino3_geom
 0.58 s  domino1_geom leaves domino2_geom
 0.62 s  domino1_geom touches domino2_geom again
 0.63 s  domino2_geom touches domino3_geom again
 0.64 s  domino3_geom touches domino4_geom again
 0.67 s  domino4_geom first touches domino5_geom
 0.67 s  domino5 starts moving
 0.68 s  domino4_geom leaves domino5_geom
 0.68 s  domino3_geom leaves domino4_geom
 0.73 s  domino3_geom touches domino4_geom again
 0.74 s  domino4_geom touches domino5_geom again
 0.75 s  domino5_geom first touches domino6_geom
 0.75 s  domino6 starts moving
 0.77 s  domino4_geom leaves domino5_geom
 0.77 s  domino5_geom leaves domino6_geom
 0.80 s  domino4_geom touches domino5_geom again
 0.83 s  domino5_geom touches domino6_geom again
 0.83 s  domino2 passes 0.26 m from domino7 (domino7_geom) without touching it: nearest points (0.39, 0.00, 0.15) m and (0.65, 0.00, 0.15) m
 0.83 s  domino1 passes 0.36 m from domino7 (domino7_geom) without touching it: nearest points (0.29, -0.05, 0.13) m and (0.65, -0.05, 0.13) m
 0.83 s  domino6_geom first touches domino7_geom
 0.83 s  domino7 starts moving
 0.84 s  domino5_geom leaves domino6_geom
 0.84 s  domino4_geom leaves domino5_geom
 0.85 s  domino6_geom leaves domino7_geom
 0.87 s  domino5_geom touches domino6_geom again
 0.88 s  domino4_geom touches domino5_geom again
 0.90 s  domino7_geom first touches domino8_geom
 0.90 s  domino8 starts moving
 0.90 s  domino2 passes 0.36 m from domino8 (domino8_geom) without touching it: nearest points (0.40, -0.05, 0.13) m and (0.76, -0.05, 0.13) m
 0.90 s  domino1 passes 0.46 m from domino8 (domino8_geom) without touching it: nearest points (0.30, -0.05, 0.11) m and (0.76, -0.05, 0.11) m
 0.91 s  domino6_geom touches domino7_geom again
 0.91 s  domino7_geom leaves domino8_geom
 0.92 s  domino5_geom leaves domino6_geom
 0.92 s  domino6_geom leaves domino7_geom
 0.95 s  domino5_geom touches domino6_geom again
 0.97 s  domino7_geom touches domino8_geom again
 0.97 s  domino8_geom first touches domino9_geom
 0.97 s  domino9 starts moving
 0.97 s  domino3 passes 0.36 m from domino9 (domino9_geom) without touching it: nearest points (0.51, -0.05, 0.13) m and (0.87, -0.05, 0.13) m
 0.97 s  domino2 passes 0.46 m from domino9 (domino9_geom) without touching it: nearest points (0.41, -0.05, 0.11) m and (0.87, -0.05, 0.11) m
 0.98 s  domino6_geom touches domino7_geom again
 0.99 s  domino8_geom leaves domino9_geom
 0.99 s  domino6_geom leaves domino7_geom
 1.03 s  domino6_geom touches domino7_geom again
 1.03 s  domino3 passes 0.46 m from domino10 (domino10_geom) without touching it: nearest points (0.52, -0.05, 0.12) m and (0.97, -0.05, 0.12) m
 1.04 s  domino9_geom first touches domino10_geom
 1.04 s  domino10 starts moving
 1.04 s  domino8_geom touches domino9_geom again
 1.04 s  domino1 passes 0.26 m from domino6 (domino6_geom) without touching it: nearest points (0.30, -0.05, 0.09) m and (0.55, -0.05, 0.02) m
 1.04 s  domino4 passes 0.36 m from domino10 (domino10_geom) without touching it: nearest points (0.62, -0.05, 0.13) m and (0.98, -0.05, 0.12) m
 1.05 s  domino9_geom leaves domino10_geom
 1.06 s  domino8_geom leaves domino9_geom
 1.06 s  domino7_geom leaves domino8_geom
 1.10 s  domino7_geom touches domino8_geom again
 1.12 s  domino8_geom touches domino9_geom again
 1.13 s  domino9_geom touches domino10_geom again
 1.13 s  domino3 passes 0.26 m from domino8 (domino8_geom) without touching it: nearest points (0.52, -0.05, 0.10) m and (0.77, -0.05, 0.02) m
 1.14 s  domino9_geom leaves domino10_geom
 1.17 s  domino4 passes 0.26 m from domino9 (domino9_geom) without touching it: nearest points (0.63, 0.05, 0.09) m and (0.88, 0.05, 0.02) m
 1.18 s  domino9_geom touches domino10_geom again
 1.19 s  domino10_geom leaves floor
 1.19 s  domino5 passes 0.25 m from domino10 (domino10_geom) without touching it: nearest points (0.75, 0.05, 0.09) m and (0.99, 0.05, 0.02) m
 1.19 s  domino1 comes to rest at (0.16, 0.00, 0.06) m
 1.20 s  domino1 passes 0.15 m from domino5 (domino5_geom) without touching it: nearest points (0.31, -0.05, 0.08) m and (0.45, -0.05, 0.03) m
 1.21 s  domino1_geom leaves floor
 1.21 s  domino2 passes 0.15 m from domino6 (domino6_geom) without touching it: nearest points (0.42, -0.05, 0.08) m and (0.56, -0.05, 0.03) m
 1.21 s  domino3 passes 0.15 m from domino7 (domino7_geom) without touching it: nearest points (0.53, -0.05, 0.08) m and (0.67, -0.05, 0.03) m
 1.21 s  domino4 passes 0.16 m from domino8 (domino8_geom) without touching it: nearest points (0.64, -0.05, 0.08) m and (0.78, -0.05, 0.03) m
 1.21 s  domino5 passes 0.15 m from domino9 (domino9_geom) without touching it: nearest points (0.75, 0.05, 0.09) m and (0.89, 0.05, 0.03) m
 1.21 s  domino6 passes 0.16 m from domino10 (domino10_geom) without touching it: nearest points (0.86, 0.05, 0.09) m and (1.00, 0.05, 0.03) m
 1.21 s  domino2 comes to rest at (0.27, 0.00, 0.06) m
 1.21 s  domino3_geom leaves floor
 1.22 s  domino3 comes to rest at (0.38, 0.00, 0.06) m
 1.22 s  domino5_geom leaves floor
 1.22 s  domino1 passes 0.06 m from domino4 (domino4_geom) without touching it: nearest points (0.31, 0.05, 0.08) m and (0.34, 0.05, 0.03) m
 1.22 s  domino4 comes to rest at (0.49, 0.00, 0.05) m
 1.23 s  domino10_geom touches floor again
 1.23 s  domino8_geom leaves floor
 1.23 s  domino9_geom leaves floor
 1.23 s  domino2 passes 0.03 m from domino4 (domino4_geom) without touching it: nearest points (0.33, 0.05, 0.06) m and (0.34, 0.05, 0.03) m
 1.23 s  domino2 passes 0.06 m from domino5 (domino5_geom) without touching it: nearest points (0.42, -0.05, 0.08) m and (0.45, -0.05, 0.03) m
 1.23 s  domino3 passes 0.03 m from domino5 (domino5_geom) without touching it: nearest points (0.44, 0.05, 0.06) m and (0.45, 0.05, 0.03) m
 1.23 s  domino3 passes 0.06 m from domino6 (domino6_geom) without touching it: nearest points (0.53, 0.05, 0.08) m and (0.56, 0.05, 0.03) m
 1.23 s  domino4 passes 0.03 m from domino6 (domino6_geom) without touching it: nearest points (0.55, -0.05, 0.06) m and (0.56, -0.05, 0.03) m
 1.23 s  domino4 passes 0.06 m from domino7 (domino7_geom) without touching it: nearest points (0.64, 0.05, 0.08) m and (0.68, 0.05, 0.03) m
 1.23 s  domino5 passes 0.03 m from domino7 (domino7_geom) without touching it: nearest points (0.67, -0.05, 0.06) m and (0.68, -0.05, 0.03) m
 1.23 s  domino5 passes 0.06 m from domino8 (domino8_geom) without touching it: nearest points (0.75, 0.05, 0.08) m and (0.79, 0.05, 0.03) m
 1.23 s  domino6 passes 0.03 m from domino8 (domino8_geom) without touching it: nearest points (0.78, -0.05, 0.06) m and (0.79, -0.05, 0.03) m
 1.23 s  domino6 passes 0.06 m from domino9 (domino9_geom) without touching it: nearest points (0.86, -0.05, 0.08) m and (0.90, -0.05, 0.03) m
 1.23 s  domino7 passes 0.03 m from domino9 (domino9_geom) without touching it: nearest points (0.89, -0.05, 0.06) m and (0.90, -0.05, 0.03) m
 1.24 s  domino5 comes to rest at (0.60, 0.00, 0.06) m
 1.26 s  domino8_geom touches floor again
 1.27 s  domino9_geom touches floor again
 1.27 s  domino9_geom leaves floor
 1.28 s  domino7 passes 0.06 m from domino10 (domino10_geom) without touching it: nearest points (0.98, 0.05, 0.08) m and (1.02, 0.05, 0.03) m
 1.28 s  domino8 passes 0.03 m from domino10 (domino10_geom) without touching it: nearest points (1.01, 0.05, 0.06) m and (1.02, 0.05, 0.03) m
 1.28 s  domino8 comes to rest at (0.95, 0.00, 0.05) m
 1.28 s  domino6 comes to rest at (0.71, 0.00, 0.05) m
 1.28 s  domino7 comes to rest at (0.83, 0.00, 0.05) m
 1.29 s  domino9 comes to rest at (1.06, 0.00, 0.06) m
 1.29 s  domino10 comes to rest at (1.17, 0.00, 0.01) m
 4.94 s  domino7_geom leaves floor

State every 0.25 s:
0.00 s: domino1 at (0.04, 0.00, 0.15) m, at rest; touching floor | domino2 at (0.11, 0.00, 0.15) m, at rest; touching floor | domino3 at (0.22, 0.00, 0.15) m, at rest; touching floor | domino4 at (0.33, 0.00, 0.15) m, at rest; touching floor | domino5 at (0.44, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.55, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.66, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.77, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.88, 0.00, 0.15) m, at rest; touching floor | domino10 at (0.99, 0.00, 0.15) m, at rest; touching floor
0.25 s: domino1 at (0.05, 0.00, 0.15) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.02), turned 4° from how it started; touching floor | domino2 at (0.12, 0.00, 0.15) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.00), turned 4° from how it started; touching floor | domino3 at (0.22, 0.00, 0.15) m, at rest; touching floor | domino4 at (0.33, 0.00, 0.15) m, at rest; touching floor | domino5 at (0.44, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.55, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.66, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.77, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.88, 0.00, 0.15) m, at rest; touching floor | domino10 at (0.99, 0.00, 0.15) m, at rest; touching floor
0.50 s: domino1 at (0.09, 0.00, 0.13) m, moving 0.24 m/s (vx +0.20, vy -0.00, vz -0.12), turned 21° from how it started; touching floor | domino2 at (0.17, 0.00, 0.14) m, moving 0.28 m/s (vx +0.27, vy -0.00, vz -0.08), turned 22° from how it started; touching floor | domino3 at (0.24, 0.00, 0.15) m, moving 0.29 m/s (vx +0.29, vy -0.00, vz -0.01), turned 7° from how it started; touching floor | domino4 at (0.33, 0.00, 0.15) m, at rest; touching floor | domino5 at (0.44, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.55, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.66, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.77, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.88, 0.00, 0.15) m, at rest; touching floor | domino10 at (0.99, 0.00, 0.15) m, at rest; touching floor
0.75 s: domino1 at (0.14, 0.00, 0.09) m, moving 0.29 m/s (vx +0.17, vy -0.00, vz -0.24), turned 44° from how it started; touching floor | domino2 at (0.24, 0.00, 0.10) m, moving 0.35 m/s (vx +0.24, vy -0.00, vz -0.25), turned 52° from how it started; touching domino3_geom, floor | domino3 at (0.33, 0.00, 0.12) m, moving 0.44 m/s (vx +0.34, vy -0.00, vz -0.28), turned 42° from how it started; touching domino2_geom | domino4 at (0.41, 0.00, 0.14) m, moving 0.58 m/s (vx +0.53, vy -0.00, vz -0.23), turned 29° from how it started; touching floor | domino5 at (0.48, 0.00, 0.15) m, moving 0.60 m/s (vx +0.59, vy -0.00, vz -0.10), turned 15° from how it started; touching floor | domino6 at (0.55, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.66, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.77, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.88, 0.00, 0.15) m, at rest; touching floor | domino10 at (0.99, 0.00, 0.15) m, at rest; touching floor
1.00 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.26, 0.00, 0.07) m, at rest, turned 69° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.37, 0.00, 0.08) m, moving 0.08 m/s (vx +0.04, vy +0.00, vz -0.07), turned 66° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.47, 0.00, 0.08) m, moving 0.14 m/s (vx +0.08, vy +0.00, vz -0.11), turned 61° from how it started; touching domino3_geom, floor | domino5 at (0.57, 0.00, 0.10) m, moving 0.23 m/s (vx +0.16, vy +0.00, vz -0.17), turned 55° from how it started; touching floor | domino6 at (0.67, 0.00, 0.11) m, moving 0.34 m/s (vx +0.27, vy +0.00, vz -0.22), turned 46° from how it started; touching floor | domino7 at (0.75, 0.00, 0.13) m, moving 0.48 m/s (vx +0.43, vy +0.00, vz -0.22), turned 34° from how it started; touching floor | domino8 at (0.83, 0.00, 0.15) m, moving 0.57 m/s (vx +0.55, vy +0.00, vz -0.14), turned 21° from how it started; touching floor | domino9 at (0.90, 0.00, 0.15) m, moving 0.67 m/s (vx +0.67, vy +0.00, vz -0.03), turned 7° from how it started; touching nothing | domino10 at (0.99, 0.00, 0.15) m, at rest; touching floor
1.25 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, floor | domino7 at (0.83, 0.00, 0.06) m, moving 0.23 m/s (vx +0.23, vy +0.00, vz -0.02), turned 74° from how it started; touching domino8_geom | domino8 at (0.94, 0.00, 0.06) m, moving 0.28 m/s (vx +0.27, vy -0.00, vz +0.07), turned 74° from how it started; touching domino7_geom | domino9 at (1.05, 0.00, 0.05) m, moving 0.37 m/s (vx +0.35, vy -0.00, vz +0.13), turned 75° from how it started; touching nothing | domino10 at (1.17, 0.00, 0.01) m, moving 0.48 m/s (vx +0.05, vy -0.00, vz -0.48), turned 91° from how it started; touching floor
1.50 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.95, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 2.50 s)
2.75 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.94, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 3.00 s)
3.25 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
3.50 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 4.75 s)
5.00 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.25 s)
5.50 s: domino1 at (0.16, 0.00, 0.06) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.75 s)
6.00 s: domino1 at (0.16, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.27, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.60, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom | domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor

At the end (6.00 s):
- domino1 at (0.16, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom
- domino2 at (0.27, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.38, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom
- domino4 at (0.49, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.60, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom
- domino6 at (0.71, 0.00, 0.05) m, at rest, turned 75° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.83, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom
- domino8 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (1.06, 0.00, 0.06) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom
- domino10 at (1.17, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
