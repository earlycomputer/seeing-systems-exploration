MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.00, 0.00, 0.10) m, at rest
- domino2: free body; its geoms: domino2_geom; starts at (0.06, 0.00, 0.10) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.12, 0.00, 0.10) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.18, 0.00, 0.10) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.24, 0.00, 0.10) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.30, 0.00, 0.10) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.36, 0.00, 0.10) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.42, 0.00, 0.10) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.48, 0.00, 0.10) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (0.54, 0.00, 0.10) m, at rest

What happened, in order:
 0.00 s  domino7_geom starts touching floor
 0.00 s  domino4_geom starts touching floor
 0.00 s  domino10_geom starts touching floor
 0.00 s  domino3_geom starts touching floor
 0.00 s  domino9_geom starts touching floor
 0.00 s  domino6_geom starts touching floor
 0.00 s  domino2_geom starts touching floor
 0.00 s  domino5_geom starts touching floor
 0.00 s  domino8_geom starts touching floor
 0.00 s  domino1_geom first touches floor
 0.03 s  domino1 starts moving
 0.07 s  domino1_geom first touches domino2_geom
 0.07 s  domino2 starts moving
 0.24 s  domino2_geom first touches domino3_geom
 0.24 s  domino3 starts moving
 0.26 s  domino2_geom leaves domino3_geom
 0.30 s  domino2_geom touches domino3_geom again
 0.34 s  domino3_geom first touches domino4_geom
 0.34 s  domino4 starts moving
 0.36 s  domino3_geom leaves domino4_geom
 0.40 s  domino3_geom touches domino4_geom again
 0.43 s  domino4_geom first touches domino5_geom
 0.43 s  domino5 starts moving
 0.44 s  domino4_geom leaves domino5_geom
 0.45 s  domino3_geom leaves domino4_geom
 0.45 s  domino2_geom leaves domino3_geom
 0.49 s  domino2_geom touches domino3_geom again
 0.49 s  domino3_geom touches domino4_geom again
 0.50 s  domino5_geom first touches domino6_geom
 0.50 s  domino6 starts moving
 0.50 s  domino4_geom touches domino5_geom again
 0.52 s  domino5_geom leaves domino6_geom
 0.52 s  domino4_geom leaves domino5_geom
 0.56 s  domino6_geom first touches domino7_geom
 0.56 s  domino7 starts moving
 0.56 s  domino1 passes 0.20 m from domino7 (domino7_geom) without touching it: nearest points (0.15, 0.03, 0.09) m and (0.35, 0.03, 0.09) m
 0.56 s  domino4_geom touches domino5_geom again
 0.57 s  domino5_geom touches domino6_geom again
 0.58 s  domino6_geom leaves domino7_geom
 0.59 s  domino5_geom leaves domino6_geom
 0.62 s  domino7_geom first touches domino8_geom
 0.62 s  domino8 starts moving
 0.62 s  domino1 passes 0.25 m from domino8 (domino8_geom) without touching it: nearest points (0.16, 0.03, 0.08) m and (0.41, 0.03, 0.08) m
 0.62 s  domino6_geom touches domino7_geom again
 0.63 s  domino5_geom touches domino6_geom again
 0.64 s  domino7_geom leaves domino8_geom
 0.64 s  domino6_geom leaves domino7_geom
 0.65 s  domino5_geom leaves domino6_geom
 0.65 s  domino4_geom leaves domino5_geom
 0.67 s  domino8_geom first touches domino9_geom
 0.67 s  domino9 starts moving
 0.67 s  domino1 passes 0.31 m from domino9 (domino9_geom) without touching it: nearest points (0.16, 0.03, 0.07) m and (0.47, 0.03, 0.07) m
 0.67 s  domino7_geom touches domino8_geom again
 0.68 s  domino4_geom touches domino5_geom again
 0.68 s  domino6_geom touches domino7_geom again
 0.69 s  domino5_geom touches domino6_geom again
 0.69 s  domino8_geom leaves domino9_geom
 0.72 s  domino1 passes 0.37 m from domino10 (domino10_geom) without touching it: nearest points (0.16, 0.03, 0.07) m and (0.53, 0.03, 0.07) m
 0.72 s  domino2 passes 0.28 m from domino10 (domino10_geom) without touching it: nearest points (0.25, 0.04, 0.09) m and (0.53, 0.04, 0.09) m
 0.72 s  domino8_geom touches domino9_geom again
 0.72 s  domino9_geom first touches domino10_geom
 0.72 s  domino10 starts moving
 0.74 s  domino9_geom leaves domino10_geom
 0.79 s  domino9_geom touches domino10_geom again
 0.83 s  domino2 passes 0.22 m from domino9 (domino9_geom) without touching it: nearest points (0.26, 0.04, 0.07) m and (0.48, 0.04, 0.01) m
 0.85 s  domino1 passes 0.14 m from domino6 (domino6_geom) without touching it: nearest points (0.17, 0.03, 0.05) m and (0.31, 0.03, 0.02) m
 0.85 s  domino2 passes 0.17 m from domino8 (domino8_geom) without touching it: nearest points (0.26, 0.04, 0.07) m and (0.43, 0.04, 0.02) m
 0.85 s  domino3 passes 0.22 m from domino10 (domino10_geom) without touching it: nearest points (0.32, 0.04, 0.07) m and (0.54, 0.04, 0.01) m
 0.87 s  domino3 passes 0.17 m from domino9 (domino9_geom) without touching it: nearest points (0.32, 0.04, 0.06) m and (0.48, 0.04, 0.02) m
 0.87 s  domino4 passes 0.17 m from domino10 (domino10_geom) without touching it: nearest points (0.38, 0.04, 0.07) m and (0.54, 0.04, 0.02) m
 0.88 s  domino5 passes 0.11 m from domino10 (domino10_geom) without touching it: nearest points (0.44, 0.04, 0.06) m and (0.55, 0.04, 0.02) m
 0.89 s  domino8_geom leaves floor
 0.89 s  domino1 comes to rest at (0.07, 0.00, 0.03) m
 0.89 s  domino1 passes 0.08 m from domino5 (domino5_geom) without touching it: nearest points (0.17, 0.03, 0.05) m and (0.25, 0.03, 0.02) m
 0.89 s  domino2 passes 0.04 m from domino5 (domino5_geom) without touching it: nearest points (0.24, 0.04, 0.05) m and (0.25, 0.04, 0.02) m
 0.89 s  domino2 passes 0.06 m from domino6 (domino6_geom) without touching it: nearest points (0.26, 0.04, 0.06) m and (0.31, 0.04, 0.02) m
 0.89 s  domino2 passes 0.12 m from domino7 (domino7_geom) without touching it: nearest points (0.26, 0.04, 0.06) m and (0.37, 0.04, 0.02) m
 0.89 s  domino3 passes 0.04 m from domino6 (domino6_geom) without touching it: nearest points (0.30, 0.04, 0.05) m and (0.31, 0.04, 0.02) m
 0.89 s  domino3 passes 0.06 m from domino7 (domino7_geom) without touching it: nearest points (0.32, 0.04, 0.06) m and (0.37, 0.04, 0.02) m
 0.89 s  domino3 passes 0.11 m from domino8 (domino8_geom) without touching it: nearest points (0.32, 0.04, 0.06) m and (0.43, 0.04, 0.02) m
 0.89 s  domino4 passes 0.06 m from domino8 (domino8_geom) without touching it: nearest points (0.38, 0.04, 0.06) m and (0.43, 0.04, 0.02) m
 0.89 s  domino4 passes 0.11 m from domino9 (domino9_geom) without touching it: nearest points (0.38, 0.04, 0.06) m and (0.49, 0.04, 0.02) m
 0.89 s  domino5 passes 0.06 m from domino9 (domino9_geom) without touching it: nearest points (0.45, 0.04, 0.06) m and (0.49, 0.04, 0.02) m
 0.89 s  domino6 passes 0.06 m from domino10 (domino10_geom) without touching it: nearest points (0.51, 0.04, 0.06) m and (0.55, 0.04, 0.02) m
 0.89 s  domino2 comes to rest at (0.17, 0.00, 0.04) m
 0.89 s  domino3 comes to rest at (0.23, 0.00, 0.04) m
 0.90 s  domino4 comes to rest at (0.29, 0.00, 0.04) m
 0.90 s  domino5 comes to rest at (0.35, 0.00, 0.04) m
 0.90 s  domino4 passes 0.03 m from domino7 (domino7_geom) without touching it: nearest points (0.36, -0.03, 0.05) m and (0.37, -0.03, 0.02) m
 0.90 s  domino5 passes 0.03 m from domino8 (domino8_geom) without touching it: nearest points (0.42, 0.04, 0.05) m and (0.43, 0.04, 0.02) m
 0.90 s  domino6 passes 0.03 m from domino9 (domino9_geom) without touching it: nearest points (0.48, 0.04, 0.05) m and (0.49, 0.04, 0.02) m
 0.90 s  domino7 passes 0.03 m from domino10 (domino10_geom) without touching it: nearest points (0.55, 0.04, 0.05) m and (0.56, 0.04, 0.02) m
 0.91 s  domino9_geom leaves domino10_geom
 0.91 s  domino6 comes to rest at (0.41, 0.00, 0.04) m
 0.92 s  domino7 comes to rest at (0.47, 0.00, 0.04) m
 0.92 s  domino8 comes to rest at (0.53, 0.00, 0.04) m
 0.94 s  domino7_geom leaves floor
 0.94 s  domino9_geom touches domino10_geom again
 0.95 s  domino2_geom leaves floor
 0.96 s  domino10 comes to rest at (0.66, 0.00, 0.01) m
 0.96 s  domino9 comes to rest at (0.59, 0.00, 0.04) m
 1.01 s  domino2_geom touches floor again
 1.31 s  domino2_geom leaves floor
 1.91 s  domino2_geom touches floor again
 3.37 s  domino8_geom touches floor again

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.10) m, at rest; touching nothing | domino2 at (0.06, 0.00, 0.10) m, at rest; touching floor | domino3 at (0.12, 0.00, 0.10) m, at rest; touching floor | domino4 at (0.18, 0.00, 0.10) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.10) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.10) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.10) m, at rest; touching floor
0.25 s: domino1 at (0.02, 0.00, 0.09) m, moving 0.08 m/s (vx +0.07, vy +0.00, vz -0.04), turned 15° from how it started; touching domino2_geom, floor | domino2 at (0.08, 0.00, 0.10) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.02), turned 13° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.12, 0.00, 0.10) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz +0.01); touching domino2_geom, floor | domino4 at (0.18, 0.00, 0.10) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.10) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.10) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.10) m, at rest; touching floor
0.50 s: domino1 at (0.06, 0.00, 0.06) m, moving 0.17 m/s (vx +0.10, vy -0.00, vz -0.14), turned 38° from how it started; touching floor | domino2 at (0.13, 0.00, 0.08) m, moving 0.28 m/s (vx +0.22, vy -0.00, vz -0.17), turned 44° from how it started; touching floor | domino3 at (0.18, 0.00, 0.09) m, moving 0.34 m/s (vx +0.30, vy +0.00, vz -0.17), turned 35° from how it started; touching domino4_geom, floor | domino4 at (0.22, 0.00, 0.10) m, moving 0.46 m/s (vx +0.44, vy +0.00, vz -0.14), turned 24° from how it started; touching domino3_geom, floor | domino5 at (0.26, 0.00, 0.10) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.00), turned 13° from how it started; touching domino6_geom | domino6 at (0.30, 0.00, 0.10) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.01); touching domino5_geom, floor | domino7 at (0.36, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.10) m, at rest; touching floor
0.75 s: domino1 at (0.07, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.05) m, at rest, turned 65° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.22, 0.00, 0.05) m, moving 0.07 m/s (vx +0.04, vy -0.00, vz -0.06), turned 62° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.06) m, moving 0.12 m/s (vx +0.08, vy -0.00, vz -0.09), turned 58° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.33, 0.00, 0.07) m, moving 0.19 m/s (vx +0.14, vy -0.00, vz -0.14), turned 53° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.38, 0.00, 0.08) m, moving 0.26 m/s (vx +0.20, vy -0.00, vz -0.16), turned 46° from how it started; touching domino5_geom, floor | domino7 at (0.43, 0.00, 0.08) m, moving 0.32 m/s (vx +0.27, vy -0.00, vz -0.16), turned 37° from how it started; touching floor | domino8 at (0.47, 0.00, 0.09) m, moving 0.37 m/s (vx +0.34, vy +0.00, vz -0.13), turned 28° from how it started; touching floor | domino9 at (0.51, 0.00, 0.10) m, moving 0.39 m/s (vx +0.38, vy +0.00, vz -0.08), turned 18° from how it started; touching floor | domino10 at (0.55, 0.00, 0.10) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz -0.01), turned 6° from how it started; touching floor
1.00 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.17, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom | domino3 at (0.23, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom | domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 1.50 s)
1.75 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom | domino3 at (0.23, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom | domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
2.00 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.23, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom | domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 3.25 s)
3.50 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.23, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.25 s)
5.50 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.22, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.07, 0.00, 0.03) m, at rest, turned 56° from how it started; touching domino2_geom, floor
- domino2 at (0.16, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.22, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.29, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.41, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.47, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_geom, domino8_geom
- domino8 at (0.53, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_geom, domino8_geom, floor
- domino10 at (0.66, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
