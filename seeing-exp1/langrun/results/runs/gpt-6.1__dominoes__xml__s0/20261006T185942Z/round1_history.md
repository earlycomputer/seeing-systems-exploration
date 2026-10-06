MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.03, 0.00, 0.12) m, at rest
- domino2: free body; its geoms: domino2_geom; starts at (0.10, 0.00, 0.12) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.20, 0.00, 0.12) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.30, 0.00, 0.12) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.40, 0.00, 0.12) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.50, 0.00, 0.12) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.60, 0.00, 0.12) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.70, 0.00, 0.12) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.80, 0.00, 0.12) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (0.90, 0.00, 0.12) m, at rest

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
 0.05 s  domino1 starts moving
 0.10 s  domino1_geom first touches domino2_geom
 0.10 s  domino2 starts moving
 0.40 s  domino2_geom first touches domino3_geom
 0.40 s  domino3 starts moving
 0.41 s  domino2_geom leaves domino3_geom
 0.42 s  domino1_geom leaves domino2_geom
 0.46 s  domino1_geom touches domino2_geom again
 0.47 s  domino2_geom touches domino3_geom again
 0.47 s  domino2_geom leaves domino3_geom
 0.51 s  domino2_geom touches domino3_geom again
 0.54 s  domino3_geom first touches domino4_geom
 0.54 s  domino4 starts moving
 0.56 s  domino3_geom leaves domino4_geom
 0.62 s  domino3_geom touches domino4_geom again
 0.65 s  domino4_geom first touches domino5_geom
 0.65 s  domino5 starts moving
 0.66 s  domino4_geom leaves domino5_geom
 0.67 s  domino3_geom leaves domino4_geom
 0.71 s  domino3_geom touches domino4_geom again
 0.74 s  domino4_geom touches domino5_geom again
 0.74 s  domino5_geom first touches domino6_geom
 0.74 s  domino6 starts moving
 0.74 s  domino1 passes 0.26 m from domino6 (domino6_geom) without touching it: nearest points (0.23, 0.05, 0.11) m and (0.49, 0.05, 0.11) m
 0.75 s  domino5_geom leaves domino6_geom
 0.80 s  domino5_geom touches domino6_geom again
 0.82 s  domino2 passes 0.26 m from domino7 (domino7_geom) without touching it: nearest points (0.33, 0.05, 0.11) m and (0.59, 0.05, 0.11) m
 0.82 s  domino1 passes 0.35 m from domino7 (domino7_geom) without touching it: nearest points (0.24, 0.05, 0.09) m and (0.59, 0.05, 0.09) m
 0.82 s  domino6_geom first touches domino7_geom
 0.82 s  domino7 starts moving
 0.84 s  domino6_geom leaves domino7_geom
 0.90 s  domino6_geom touches domino7_geom again
 0.90 s  domino3 passes 0.25 m from domino8 (domino8_geom) without touching it: nearest points (0.43, 0.05, 0.11) m and (0.69, 0.05, 0.11) m
 0.90 s  domino2 passes 0.35 m from domino8 (domino8_geom) without touching it: nearest points (0.34, 0.05, 0.09) m and (0.69, 0.05, 0.09) m
 0.90 s  domino1 passes 0.44 m from domino8 (domino8_geom) without touching it: nearest points (0.24, 0.05, 0.08) m and (0.69, 0.05, 0.08) m
 0.90 s  domino7_geom first touches domino8_geom
 0.90 s  domino8 starts moving
 0.92 s  domino7_geom leaves domino8_geom
 0.97 s  domino7_geom touches domino8_geom again
 0.98 s  domino8_geom first touches domino9_geom
 0.98 s  domino9 starts moving
 0.98 s  domino4 passes 0.25 m from domino9 (domino9_geom) without touching it: nearest points (0.53, 0.05, 0.11) m and (0.79, 0.05, 0.11) m
 0.98 s  domino3 passes 0.35 m from domino9 (domino9_geom) without touching it: nearest points (0.44, 0.05, 0.09) m and (0.79, 0.05, 0.09) m
 0.98 s  domino2 passes 0.44 m from domino9 (domino9_geom) without touching it: nearest points (0.34, 0.05, 0.08) m and (0.79, 0.05, 0.08) m
 0.98 s  domino1 comes to rest at (0.13, 0.00, 0.05) m
 1.00 s  domino7_geom leaves domino8_geom
 1.00 s  domino8_geom leaves domino9_geom
 1.04 s  domino7_geom touches domino8_geom again
 1.05 s  domino1 passes 0.16 m from domino5 (domino5_geom) without touching it: nearest points (0.25, 0.05, 0.07) m and (0.40, 0.05, 0.02) m
 1.05 s  domino3 passes 0.44 m from domino10 (domino10_geom) without touching it: nearest points (0.44, 0.05, 0.08) m and (0.89, 0.05, 0.08) m
 1.06 s  domino9_geom first touches domino10_geom
 1.06 s  domino10 starts moving
 1.06 s  domino2 passes 0.17 m from domino6 (domino6_geom) without touching it: nearest points (0.35, 0.05, 0.08) m and (0.50, 0.05, 0.02) m
 1.06 s  domino5 passes 0.26 m from domino10 (domino10_geom) without touching it: nearest points (0.63, 0.05, 0.11) m and (0.89, 0.05, 0.11) m
 1.06 s  domino4 passes 0.35 m from domino10 (domino10_geom) without touching it: nearest points (0.54, 0.05, 0.09) m and (0.89, 0.05, 0.09) m
 1.06 s  domino8_geom touches domino9_geom again
 1.07 s  domino9_geom leaves domino10_geom
 1.08 s  domino8_geom leaves domino9_geom
 1.13 s  domino8_geom touches domino9_geom again
 1.14 s  domino2 comes to rest at (0.23, 0.00, 0.05) m
 1.14 s  domino3 passes 0.16 m from domino7 (domino7_geom) without touching it: nearest points (0.45, 0.05, 0.08) m and (0.60, 0.05, 0.02) m
 1.14 s  domino9_geom touches domino10_geom again
 1.19 s  domino4 passes 0.16 m from domino8 (domino8_geom) without touching it: nearest points (0.55, 0.05, 0.08) m and (0.70, 0.05, 0.02) m
 1.20 s  domino5 passes 0.17 m from domino9 (domino9_geom) without touching it: nearest points (0.64, 0.05, 0.08) m and (0.80, 0.05, 0.02) m
 1.22 s  domino6 passes 0.16 m from domino10 (domino10_geom) without touching it: nearest points (0.74, 0.05, 0.08) m and (0.90, 0.05, 0.02) m
 1.22 s  domino1_geom leaves floor
 1.24 s  domino3 passes 0.07 m from domino6 (domino6_geom) without touching it: nearest points (0.45, 0.05, 0.07) m and (0.51, 0.05, 0.03) m
 1.24 s  domino3 comes to rest at (0.33, 0.00, 0.05) m
 1.24 s  domino4 comes to rest at (0.43, 0.00, 0.05) m
 1.24 s  domino4_geom leaves floor
 1.25 s  domino9_geom leaves floor
 1.25 s  domino1 passes 0.07 m from domino4 (domino4_geom) without touching it: nearest points (0.25, 0.05, 0.07) m and (0.31, 0.05, 0.03) m
 1.25 s  domino2 passes 0.07 m from domino5 (domino5_geom) without touching it: nearest points (0.35, 0.05, 0.07) m and (0.41, 0.05, 0.03) m
 1.25 s  domino4 passes 0.07 m from domino7 (domino7_geom) without touching it: nearest points (0.55, 0.05, 0.07) m and (0.61, 0.05, 0.03) m
 1.25 s  domino5 passes 0.03 m from domino7 (domino7_geom) without touching it: nearest points (0.60, 0.05, 0.05) m and (0.61, 0.05, 0.03) m
 1.25 s  domino5 passes 0.08 m from domino8 (domino8_geom) without touching it: nearest points (0.65, 0.05, 0.07) m and (0.71, 0.05, 0.03) m
 1.25 s  domino6 passes 0.08 m from domino9 (domino9_geom) without touching it: nearest points (0.75, 0.05, 0.07) m and (0.82, 0.05, 0.03) m
 1.25 s  domino7 passes 0.07 m from domino10 (domino10_geom) without touching it: nearest points (0.85, 0.05, 0.07) m and (0.91, 0.05, 0.03) m
 1.25 s  domino5 comes to rest at (0.53, 0.00, 0.05) m
 1.26 s  domino2 passes 0.03 m from domino4 (domino4_geom) without touching it: nearest points (0.35, 0.05, 0.07) m and (0.36, 0.05, 0.04) m
 1.26 s  domino3 passes 0.03 m from domino5 (domino5_geom) without touching it: nearest points (0.40, 0.05, 0.05) m and (0.41, 0.05, 0.03) m
 1.26 s  domino4 passes 0.03 m from domino6 (domino6_geom) without touching it: nearest points (0.50, 0.05, 0.05) m and (0.51, 0.05, 0.03) m
 1.26 s  domino6 passes 0.03 m from domino8 (domino8_geom) without touching it: nearest points (0.71, 0.05, 0.05) m and (0.71, 0.05, 0.03) m
 1.26 s  domino7 passes 0.03 m from domino9 (domino9_geom) without touching it: nearest points (0.81, 0.05, 0.05) m and (0.82, 0.05, 0.03) m
 1.26 s  domino8 passes 0.03 m from domino10 (domino10_geom) without touching it: nearest points (0.91, 0.05, 0.05) m and (0.92, 0.05, 0.03) m
 1.27 s  domino6 comes to rest at (0.63, 0.00, 0.05) m
 1.29 s  domino7 comes to rest at (0.73, 0.00, 0.05) m
 1.30 s  domino8 comes to rest at (0.84, 0.00, 0.05) m
 1.30 s  domino9 comes to rest at (0.95, 0.00, 0.05) m
 1.31 s  domino10 comes to rest at (1.04, 0.00, 0.01) m
 3.40 s  domino1_geom touches floor again
 5.09 s  domino4_geom touches floor again
 6.00 s  domino7_geom leaves floor

State every 0.25 s:
0.00 s: domino1 at (0.03, 0.00, 0.12) m, at rest; touching nothing | domino2 at (0.10, 0.00, 0.12) m, at rest; touching floor | domino3 at (0.20, 0.00, 0.12) m, at rest; touching floor | domino4 at (0.30, 0.00, 0.12) m, at rest; touching floor | domino5 at (0.40, 0.00, 0.12) m, at rest; touching floor | domino6 at (0.50, 0.00, 0.12) m, at rest; touching floor | domino7 at (0.60, 0.00, 0.12) m, at rest; touching floor | domino8 at (0.70, 0.00, 0.12) m, at rest; touching floor | domino9 at (0.80, 0.00, 0.12) m, at rest; touching floor | domino10 at (0.90, 0.00, 0.12) m, at rest; touching floor
0.25 s: domino1 at (0.05, 0.00, 0.12) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.02), turned 7° from how it started; touching floor | domino2 at (0.11, 0.00, 0.12) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.00), turned 5° from how it started; touching floor | domino3 at (0.20, 0.00, 0.12) m, at rest; touching floor | domino4 at (0.30, 0.00, 0.12) m, at rest; touching floor | domino5 at (0.40, 0.00, 0.12) m, at rest; touching floor | domino6 at (0.50, 0.00, 0.12) m, at rest; touching floor | domino7 at (0.60, 0.00, 0.12) m, at rest; touching floor | domino8 at (0.70, 0.00, 0.12) m, at rest; touching floor | domino9 at (0.80, 0.00, 0.12) m, at rest; touching floor | domino10 at (0.90, 0.00, 0.12) m, at rest; touching floor
0.50 s: domino1 at (0.08, 0.00, 0.10) m, moving 0.24 m/s (vx +0.19, vy +0.00, vz -0.13), turned 27° from how it started; touching domino2_geom, floor | domino2 at (0.16, 0.00, 0.11) m, moving 0.31 m/s (vx +0.29, vy +0.00, vz -0.11), turned 28° from how it started; touching domino1_geom, floor | domino3 at (0.22, 0.00, 0.12) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.02), turned 11° from how it started; touching floor | domino4 at (0.30, 0.00, 0.12) m, at rest; touching floor | domino5 at (0.40, 0.00, 0.12) m, at rest; touching floor | domino6 at (0.50, 0.00, 0.12) m, at rest; touching floor | domino7 at (0.60, 0.00, 0.12) m, at rest; touching floor | domino8 at (0.70, 0.00, 0.12) m, at rest; touching floor | domino9 at (0.80, 0.00, 0.12) m, at rest; touching floor | domino10 at (0.90, 0.00, 0.12) m, at rest; touching floor
0.75 s: domino1 at (0.12, 0.00, 0.07) m, moving 0.09 m/s (vx +0.07, vy +0.00, vz -0.05), turned 49° from how it started; touching domino2_geom, floor | domino2 at (0.21, 0.00, 0.08) m, moving 0.10 m/s (vx +0.08, vy -0.00, vz -0.06), turned 58° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.30, 0.00, 0.09) m, moving 0.19 m/s (vx +0.15, vy -0.00, vz -0.12), turned 48° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.37, 0.00, 0.11) m, moving 0.28 m/s (vx +0.25, vy -0.00, vz -0.12), turned 35° from how it started; touching domino3_geom, floor | domino5 at (0.44, 0.00, 0.12) m, moving 0.30 m/s (vx +0.29, vy -0.00, vz -0.06), turned 19° from how it started; touching domino6_geom, floor | domino6 at (0.50, 0.00, 0.12) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz +0.02), turned 2° from how it started; touching domino5_geom | domino7 at (0.60, 0.00, 0.12) m, at rest; touching floor | domino8 at (0.70, 0.00, 0.12) m, at rest; touching floor | domino9 at (0.80, 0.00, 0.12) m, at rest; touching floor | domino10 at (0.90, 0.00, 0.12) m, at rest; touching floor
1.00 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 57° from how it started; touching domino2_geom, floor | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 70° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.32, 0.00, 0.06) m, at rest, turned 68° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.42, 0.00, 0.07) m, moving 0.05 m/s (vx +0.03, vy +0.00, vz -0.04), turned 64° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.51, 0.00, 0.08) m, moving 0.09 m/s (vx +0.06, vy +0.00, vz -0.07), turned 58° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.60, 0.00, 0.09) m, moving 0.17 m/s (vx +0.13, vy -0.00, vz -0.11), turned 49° from how it started; touching domino5_geom, floor | domino7 at (0.68, 0.00, 0.11) m, moving 0.23 m/s (vx +0.21, vy -0.00, vz -0.11), turned 36° from how it started; touching floor | domino8 at (0.75, 0.00, 0.12) m, moving 0.37 m/s (vx +0.37, vy -0.00, vz -0.08), turned 20° from how it started; touching floor | domino9 at (0.81, 0.00, 0.12) m, moving 0.52 m/s (vx +0.52, vy +0.00, vz +0.03), turned 4° from how it started; touching floor | domino10 at (0.90, 0.00, 0.12) m, at rest; touching floor
1.25 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom | domino5 at (0.53, 0.00, 0.05) m, moving 0.06 m/s (vx +0.04, vy +0.00, vz -0.05), turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, moving 0.20 m/s (vx +0.08, vy -0.00, vz -0.18), turned 74° from how it started; touching domino5_geom, floor | domino7 at (0.73, 0.00, 0.05) m, moving 0.32 m/s (vx +0.14, vy -0.00, vz -0.29), turned 74° from how it started; touching domino8_geom, floor | domino8 at (0.83, 0.00, 0.05) m, moving 0.58 m/s (vx +0.25, vy -0.00, vz -0.53), turned 74° from how it started; touching domino7_geom, floor | domino9 at (0.93, 0.00, 0.05) m, moving 0.91 m/s (vx +0.48, vy +0.00, vz -0.77), turned 73° from how it started; touching domino10_geom | domino10 at (1.03, 0.00, 0.05) m, moving 1.63 m/s (vx +0.78, vy -0.00, vz -1.44), turned 73° from how it started; touching domino9_geom
1.50 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.74, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.95, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 2.75 s)
3.00 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.74, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 3.25 s)
3.50 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom, floor | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.74, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
3.75 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom, floor | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.73, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.00 s)
5.25 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom, floor | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.73, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.75 s)
6.00 s: domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom, floor | domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.73, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor

At the end (6.00 s):
- domino1 at (0.13, 0.00, 0.05) m, at rest, turned 59° from how it started; touching domino2_geom, floor
- domino2 at (0.23, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.33, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.43, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.53, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.63, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.73, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom
- domino8 at (0.84, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (0.94, 0.00, 0.05) m, at rest, turned 74° from how it started; touching domino10_geom, domino8_geom
- domino10 at (1.04, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
