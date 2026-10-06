Your expectations, checked against the run (9 of 9 hold):

- holds: domino1 touches domino2 (first touch at 0.12 s)
- holds: domino2 touches domino3 (first touch at 0.32 s)
- holds: domino3 touches domino4 (first touch at 0.46 s)
- holds: domino4 touches domino5 (first touch at 0.58 s)
- holds: domino5 touches domino6 (first touch at 0.69 s)
- holds: domino6 touches domino7 (first touch at 0.79 s)
- holds: domino7 touches domino8 (first touch at 0.90 s)
- holds: domino8 touches domino9 (first touch at 1.00 s)
- holds: domino9 touches domino10 (first touch at 1.10 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.04)
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
 0.13 s  domino2 starts moving
 0.32 s  domino2_geom first touches domino3_geom
 0.33 s  domino3 starts moving
 0.36 s  domino2_geom leaves domino3_geom
 0.39 s  domino2_geom touches domino3_geom again
 0.46 s  domino3_geom first touches domino4_geom
 0.46 s  domino4 starts moving
 0.49 s  domino3_geom leaves domino4_geom
 0.53 s  domino3_geom touches domino4_geom again
 0.58 s  domino4_geom first touches domino5_geom
 0.58 s  domino1 comes to rest at (0.05, 0.00, 0.03) m
 0.58 s  domino5 starts moving
 0.61 s  domino4_geom leaves domino5_geom
 0.65 s  domino4_geom touches domino5_geom again
 0.69 s  domino5_geom first touches domino6_geom
 0.69 s  domino6 starts moving
 0.72 s  domino5_geom leaves domino6_geom
 0.76 s  domino2 comes to rest at (0.11, 0.00, 0.03) m
 0.76 s  domino5_geom touches domino6_geom again
 0.79 s  domino6_geom first touches domino7_geom
 0.80 s  domino7 starts moving
 0.80 s  domino3 comes to rest at (0.17, 0.00, 0.03) m
 0.83 s  domino6_geom leaves domino7_geom
 0.87 s  domino6_geom touches domino7_geom again
 0.90 s  domino7_geom first touches domino8_geom
 0.90 s  domino8 starts moving
 0.91 s  domino4 comes to rest at (0.23, 0.00, 0.03) m
 0.93 s  domino7_geom leaves domino8_geom
 0.97 s  domino7_geom touches domino8_geom again
 1.00 s  domino8_geom first touches domino9_geom
 1.01 s  domino9 starts moving
 1.02 s  domino5 comes to rest at (0.29, 0.00, 0.03) m
 1.04 s  domino8_geom leaves domino9_geom
 1.08 s  domino8_geom touches domino9_geom again
 1.10 s  domino9_geom first touches domino10_geom
 1.11 s  domino10 starts moving
 1.14 s  domino9_geom leaves domino10_geom
 1.18 s  domino9_geom touches domino10_geom again
 1.19 s  domino6 comes to rest at (0.35, 0.00, 0.03) m
 1.29 s  domino7 comes to rest at (0.42, 0.00, 0.03) m
 1.30 s  domino8 comes to rest at (0.48, 0.00, 0.03) m
 1.34 s  domino9 comes to rest at (0.54, 0.00, 0.02) m
 1.38 s  domino10 comes to rest at (0.61, 0.00, 0.01) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.04); touching floor | domino2 at (0.06, 0.00, 0.05) m, at rest; touching floor | domino3 at (0.12, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.25 s: domino1 at (0.03, 0.00, 0.05) m, moving 0.10 m/s (vx +0.09, vy +0.00, vz -0.04), turned 34° from how it started; touching floor | domino2 at (0.07, 0.00, 0.05) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.00), turned 11° from how it started; touching floor | domino3 at (0.12, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 60° from how it started; touching floor | domino2 at (0.10, 0.00, 0.04) m, moving 0.07 m/s (vx +0.05, vy -0.00, vz -0.04), turned 48° from how it started; touching floor | domino3 at (0.15, 0.00, 0.05) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.03), turned 29° from how it started; touching floor | domino4 at (0.19, 0.00, 0.05) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.02), turned 6° from how it started; touching floor | domino5 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
0.75 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 69° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 66° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, moving 0.07 m/s (vx +0.04, vy +0.00, vz -0.06), turned 61° from how it started; touching domino2_geom, floor | domino4 at (0.22, 0.00, 0.04) m, moving 0.13 m/s (vx +0.10, vy +0.00, vz -0.08), turned 51° from how it started; touching domino5_geom, floor | domino5 at (0.27, 0.00, 0.05) m, moving 0.21 m/s (vx +0.20, vy -0.00, vz -0.08), turned 34° from how it started; touching domino4_geom, floor | domino6 at (0.31, 0.00, 0.05) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.00), turned 12° from how it started; touching floor | domino7 at (0.36, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
1.00 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 70° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, at rest, turned 70° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.03) m, at rest, turned 68° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.29, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.35, 0.00, 0.04) m, moving 0.15 m/s (vx +0.10, vy -0.00, vz -0.10), turned 56° from how it started; touching domino5_geom, floor | domino7 at (0.40, 0.00, 0.04) m, moving 0.25 m/s (vx +0.22, vy +0.00, vz -0.13), turned 43° from how it started; touching floor | domino8 at (0.44, 0.00, 0.05) m, moving 0.31 m/s (vx +0.30, vy +0.00, vz -0.06), turned 24° from how it started; touching floor | domino9 at (0.48, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.54, 0.00, 0.05) m, at rest; touching floor
1.25 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.29, 0.00, 0.03) m, at rest, turned 70° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.03) m, at rest, turned 69° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.41, 0.00, 0.03) m, moving 0.08 m/s (vx +0.05, vy +0.00, vz -0.07), turned 67° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.47, 0.00, 0.03) m, moving 0.18 m/s (vx +0.11, vy -0.00, vz -0.14), turned 64° from how it started; touching domino7_geom, floor | domino9 at (0.53, 0.00, 0.04) m, moving 0.32 m/s (vx +0.24, vy +0.00, vz -0.22), turned 55° from how it started; touching domino10_geom, floor | domino10 at (0.58, 0.00, 0.04) m, moving 0.50 m/s (vx +0.42, vy +0.00, vz -0.27), turned 42° from how it started; touching domino9_geom
1.50 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.03) m, at rest, turned 72° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.61, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 1.75 s)
2.00 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.30, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.61, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 4.00 s)
4.25 s: domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.17, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.23, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.29, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.36, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.42, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.48, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.54, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.61, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.05, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, floor
- domino2 at (0.11, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.17, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.23, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.29, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.36, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.42, 0.00, 0.03) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor
- domino8 at (0.48, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (0.54, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10_geom, domino8_geom, floor
- domino10 at (0.61, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
