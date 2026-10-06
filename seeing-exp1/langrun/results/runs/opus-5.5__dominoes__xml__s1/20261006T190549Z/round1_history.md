MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.00)
- domino2: free body; its geoms: domino2_geom; starts at (0.06, 0.00, 0.05) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.12, 0.00, 0.05) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.18, 0.00, 0.05) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.24, 0.00, 0.05) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.30, 0.00, 0.05) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.36, 0.00, 0.05) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.42, 0.00, 0.05) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.48, 0.00, 0.05) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (0.54, 0.00, 0.05) m, at rest

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
 0.12 s  domino1_geom first touches domino2_geom
 0.12 s  domino2 starts moving
 0.16 s  domino1_geom leaves domino2_geom
 0.20 s  domino1_geom touches domino2_geom again
 0.25 s  domino2_geom first touches domino3_geom
 0.25 s  domino3 starts moving
 0.28 s  domino2_geom leaves domino3_geom
 0.33 s  domino2_geom touches domino3_geom again
 0.34 s  domino3_geom first touches domino4_geom
 0.34 s  domino4 starts moving
 0.37 s  domino3_geom leaves domino4_geom
 0.42 s  domino3_geom touches domino4_geom again
 0.43 s  domino4_geom first touches domino5_geom
 0.43 s  domino5 starts moving
 0.46 s  domino4_geom leaves domino5_geom
 0.50 s  domino4_geom touches domino5_geom again
 0.51 s  domino1 comes to rest at (0.06, 0.00, 0.01) m
 0.51 s  domino5_geom first touches domino6_geom
 0.51 s  domino6 starts moving
 0.51 s  domino1 passes 0.19 m from domino6 (domino6_geom) without touching it: nearest points (0.11, 0.00, 0.02) m and (0.30, 0.00, 0.02) m
 0.51 s  domino2 comes to rest at (0.11, 0.00, 0.02) m
 0.54 s  domino5_geom leaves domino6_geom
 0.58 s  domino1 passes 0.25 m from domino7 (domino7_geom) without touching it: nearest points (0.11, 0.00, 0.02) m and (0.35, 0.00, 0.02) m
 0.58 s  domino5_geom touches domino6_geom again
 0.59 s  domino6_geom first touches domino7_geom
 0.59 s  domino7 starts moving
 0.59 s  domino3 comes to rest at (0.17, 0.00, 0.02) m
 0.62 s  domino6_geom leaves domino7_geom
 0.66 s  domino1 passes 0.31 m from domino8 (domino8_geom) without touching it: nearest points (0.11, 0.00, 0.02) m and (0.42, 0.00, 0.02) m
 0.66 s  domino2 passes 0.25 m from domino8 (domino8_geom) without touching it: nearest points (0.17, 0.00, 0.02) m and (0.42, 0.00, 0.02) m
 0.66 s  domino6_geom touches domino7_geom again
 0.67 s  domino7_geom first touches domino8_geom
 0.67 s  domino8 starts moving
 0.67 s  domino4 comes to rest at (0.23, 0.00, 0.02) m
 0.70 s  domino7_geom leaves domino8_geom
 0.74 s  domino1 passes 0.37 m from domino9 (domino9_geom) without touching it: nearest points (0.11, 0.00, 0.02) m and (0.47, 0.00, 0.02) m
 0.74 s  domino2 passes 0.31 m from domino9 (domino9_geom) without touching it: nearest points (0.17, 0.00, 0.02) m and (0.47, 0.00, 0.02) m
 0.74 s  domino7_geom touches domino8_geom again
 0.75 s  domino8_geom first touches domino9_geom
 0.75 s  domino9 starts moving
 0.76 s  domino5 comes to rest at (0.29, 0.00, 0.02) m
 0.76 s  domino1 passes 0.43 m from domino10 (domino10_geom) without touching it: nearest points (0.11, 0.00, 0.02) m and (0.54, 0.00, 0.02) m
 0.78 s  domino8_geom leaves domino9_geom
 0.82 s  domino2 passes 0.37 m from domino10 (domino10_geom) without touching it: nearest points (0.17, -0.02, 0.02) m and (0.54, -0.02, 0.02) m
 0.82 s  domino3 passes 0.31 m from domino10 (domino10_geom) without touching it: nearest points (0.23, -0.02, 0.02) m and (0.54, -0.02, 0.02) m
 0.82 s  domino8_geom touches domino9_geom again
 0.82 s  domino9_geom first touches domino10_geom
 0.83 s  domino10 starts moving
 0.84 s  domino6 comes to rest at (0.35, 0.00, 0.02) m
 0.86 s  domino9_geom leaves domino10_geom
 0.90 s  domino9_geom touches domino10_geom again
 0.97 s  domino7 comes to rest at (0.42, 0.00, 0.01) m
 0.97 s  domino8 comes to rest at (0.48, 0.00, 0.01) m
 1.06 s  domino9 comes to rest at (0.54, 0.00, 0.01) m
 1.06 s  domino10 comes to rest at (0.60, 0.00, 0.00) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.00); touching floor | domino2 at (0.06, 0.00, 0.05) m, at rest; touching floor | domino3 at (0.12, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.25 s: domino1 at (0.04, 0.00, 0.03) m, moving 0.22 m/s (vx +0.15, vy -0.00, vz -0.16), turned 56° from how it started; touching domino2_geom, floor | domino2 at (0.09, 0.00, 0.04) m, moving 0.26 m/s (vx +0.24, vy -0.00, vz -0.10), turned 32° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.12, 0.00, 0.05) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.00); touching domino2_geom, floor | domino4 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 78° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.02) m, moving 0.12 m/s (vx +0.04, vy -0.00, vz -0.11), turned 75° from how it started; touching domino1_geom, floor | domino3 at (0.17, 0.00, 0.02) m, moving 0.20 m/s (vx +0.10, vy +0.00, vz -0.18), turned 68° from how it started; touching domino4_geom, floor | domino4 at (0.22, 0.00, 0.03) m, moving 0.40 m/s (vx +0.28, vy +0.00, vz -0.28), turned 52° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.26, 0.00, 0.05) m, moving 0.44 m/s (vx +0.40, vy -0.00, vz -0.19), turned 27° from how it started; touching domino4_geom | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.75 s: domino1 at (0.06, 0.00, 0.01) m, at rest, turned 80° from how it started; touching domino2_geom, floor | domino2 at (0.12, 0.00, 0.01) m, at rest, turned 80° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 80° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.01) m, at rest, turned 79° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.29, 0.00, 0.02) m, moving 0.09 m/s (vx +0.03, vy +0.00, vz -0.09), turned 76° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.35, 0.00, 0.02) m, moving 0.18 m/s (vx +0.08, vy +0.00, vz -0.16), turned 70° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.40, 0.00, 0.03) m, moving 0.31 m/s (vx +0.20, vy +0.00, vz -0.23), turned 57° from how it started; touching domino6_geom, domino8_geom | domino8 at (0.45, 0.00, 0.04) m, moving 0.35 m/s (vx +0.31, vy +0.00, vz -0.17), turned 32° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.48, 0.00, 0.05) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz +0.01); touching domino8_geom, floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
1.00 s: domino1 at (0.06, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.12, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.18, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.24, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 82° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, moving 0.10 m/s (vx +0.02, vy -0.00, vz -0.10), turned 85° from how it started; touching domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 94° from how it started; touching floor
1.25 s: domino1 at (0.06, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.12, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.18, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.24, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
1.50 s: domino1 at (0.06, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.12, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.24, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 2.00 s)
2.25 s: domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.24, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
2.50 s: domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.25 s)
5.50 s: domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 82° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.60, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
5.75 s: domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 82° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.61, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
6.00 s: domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.29, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.01) m, at rest, turned 82° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.61, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor

At the end (6.00 s):
- domino1 at (0.05, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, floor
- domino2 at (0.11, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.17, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.23, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.29, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.36, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.42, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino6_geom, domino8_geom, floor
- domino8 at (0.48, 0.00, 0.01) m, at rest, turned 81° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (0.54, 0.00, 0.01) m, at rest, turned 82° from how it started; touching domino10_geom, domino8_geom, floor
- domino10 at (0.61, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
