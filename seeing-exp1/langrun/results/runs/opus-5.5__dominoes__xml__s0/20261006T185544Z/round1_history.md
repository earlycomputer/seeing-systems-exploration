MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.00, 0.00, 0.05) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz +0.03)
- domino2: free body; its geoms: domino2_geom; starts at (0.07, 0.00, 0.05) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.14, 0.00, 0.05) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.21, 0.00, 0.05) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.28, 0.00, 0.05) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.35, 0.00, 0.05) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.42, 0.00, 0.05) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.49, 0.00, 0.05) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.56, 0.00, 0.05) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (0.63, 0.00, 0.05) m, at rest

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
 0.22 s  domino1_geom first touches domino2_geom
 0.22 s  domino2 starts moving
 0.39 s  domino2_geom first touches domino3_geom
 0.39 s  domino3 starts moving
 0.50 s  domino3_geom first touches domino4_geom
 0.50 s  domino4 starts moving
 0.54 s  domino3_geom leaves domino4_geom
 0.57 s  domino3_geom touches domino4_geom again
 0.59 s  domino4_geom first touches domino5_geom
 0.59 s  domino5 starts moving
 0.60 s  domino1 comes to rest at (0.05, 0.00, 0.03) m
 0.63 s  domino4_geom leaves domino5_geom
 0.67 s  domino4_geom touches domino5_geom again
 0.67 s  domino2 comes to rest at (0.13, 0.00, 0.03) m
 0.68 s  domino5_geom first touches domino6_geom
 0.68 s  domino6 starts moving
 0.76 s  domino3 comes to rest at (0.20, 0.00, 0.03) m
 0.77 s  domino6_geom first touches domino7_geom
 0.77 s  domino7 starts moving
 0.81 s  domino6_geom leaves domino7_geom
 0.84 s  domino6_geom touches domino7_geom again
 0.85 s  domino4 comes to rest at (0.27, 0.00, 0.03) m
 0.86 s  domino7_geom first touches domino8_geom
 0.86 s  domino8 starts moving
 0.90 s  domino7_geom leaves domino8_geom
 0.93 s  domino7_geom touches domino8_geom again
 0.95 s  domino8_geom first touches domino9_geom
 0.95 s  domino9 starts moving
 0.96 s  domino5 comes to rest at (0.34, 0.00, 0.03) m
 0.99 s  domino8_geom leaves domino9_geom
 1.03 s  domino8_geom touches domino9_geom again
 1.03 s  domino6 comes to rest at (0.41, 0.00, 0.03) m
 1.04 s  domino9_geom first touches domino10_geom
 1.04 s  domino10 starts moving
 1.08 s  domino9_geom leaves domino10_geom
 1.11 s  domino9_geom touches domino10_geom again
 1.17 s  domino7 comes to rest at (0.48, 0.00, 0.02) m
 1.19 s  domino8 comes to rest at (0.55, 0.00, 0.02) m
 1.22 s  domino9 comes to rest at (0.62, 0.00, 0.02) m
 1.27 s  domino10 comes to rest at (0.70, 0.00, 0.01) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.05) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz +0.03); touching floor | domino2 at (0.07, 0.00, 0.05) m, at rest; touching floor | domino3 at (0.14, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.21, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.28, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.05) m, at rest; touching floor
0.25 s: domino1 at (0.03, 0.00, 0.05) m, moving 0.06 m/s (vx +0.05, vy -0.00, vz -0.02), turned 33° from how it started; touching domino2_geom, floor | domino2 at (0.07, 0.00, 0.05) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz +0.02), turned 3° from how it started; touching domino1_geom, floor | domino3 at (0.14, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.21, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.28, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.05) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.03) m, moving 0.10 m/s (vx +0.06, vy +0.00, vz -0.08), turned 67° from how it started; touching floor | domino2 at (0.12, 0.00, 0.04) m, moving 0.23 m/s (vx +0.17, vy -0.00, vz -0.15), turned 55° from how it started; touching domino3_geom, floor | domino3 at (0.17, 0.00, 0.05) m, moving 0.31 m/s (vx +0.29, vy -0.00, vz -0.10), turned 32° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.21, 0.00, 0.05) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.01); touching domino3_geom, floor | domino5 at (0.28, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.05) m, at rest; touching floor
0.75 s: domino1 at (0.06, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.19, 0.00, 0.03) m, moving 0.08 m/s (vx +0.04, vy +0.00, vz -0.07), turned 70° from how it started; touching domino2_geom, floor | domino4 at (0.26, 0.00, 0.03) m, moving 0.15 m/s (vx +0.09, vy -0.00, vz -0.11), turned 63° from how it started; touching domino5_geom, floor | domino5 at (0.32, 0.00, 0.04) m, moving 0.30 m/s (vx +0.25, vy -0.00, vz -0.17), turned 48° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.37, 0.00, 0.05) m, moving 0.36 m/s (vx +0.35, vy +0.00, vz -0.06), turned 21° from how it started; touching domino5_geom, floor | domino7 at (0.42, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.05) m, at rest; touching floor
1.00 s: domino1 at (0.06, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.40, 0.00, 0.03) m, at rest, turned 69° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.47, 0.00, 0.03) m, moving 0.11 m/s (vx +0.07, vy -0.00, vz -0.08), turned 60° from how it started; touching domino6_geom, floor | domino8 at (0.53, 0.00, 0.04) m, moving 0.23 m/s (vx +0.20, vy +0.00, vz -0.11), turned 42° from how it started; touching floor | domino9 at (0.57, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz -0.03), turned 15° from how it started; touching nothing | domino10 at (0.63, 0.00, 0.05) m, at rest; touching floor
1.25 s: domino1 at (0.06, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.70, 0.00, 0.01) m, moving 0.10 m/s (vx -0.01, vy +0.00, vz +0.10), turned 94° from how it started; touching domino9_geom, floor
1.50 s: domino1 at (0.06, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.70, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
1.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.70, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 2.50 s)
2.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.13, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.70, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 4.50 s)
4.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor | domino2 at (0.12, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.20, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.27, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor | domino10 at (0.70, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.05, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, floor
- domino2 at (0.12, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.20, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.27, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.34, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.48, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino6_geom, domino8_geom, floor
- domino8 at (0.55, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (0.62, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10_geom, domino8_geom, floor
- domino10 at (0.70, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
