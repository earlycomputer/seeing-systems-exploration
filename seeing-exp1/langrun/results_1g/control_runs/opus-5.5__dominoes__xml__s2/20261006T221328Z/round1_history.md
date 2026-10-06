MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1.g1; starts at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.03)
- domino2: free body; its geoms: domino2.g2; starts at (0.05, 0.00, 0.05) m, at rest
- domino3: free body; its geoms: domino3.g3; starts at (0.10, 0.00, 0.05) m, at rest
- domino4: free body; its geoms: domino4.g4; starts at (0.15, 0.00, 0.05) m, at rest
- domino5: free body; its geoms: domino5.g5; starts at (0.20, 0.00, 0.05) m, at rest
- domino6: free body; its geoms: domino6.g6; starts at (0.25, 0.00, 0.05) m, at rest
- domino7: free body; its geoms: domino7.g7; starts at (0.30, 0.00, 0.05) m, at rest
- domino8: free body; its geoms: domino8.g8; starts at (0.35, 0.00, 0.05) m, at rest
- domino9: free body; its geoms: domino9.g9; starts at (0.40, 0.00, 0.05) m, at rest
- domino10: free body; its geoms: domino10.g10; starts at (0.45, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  domino1.g1 starts touching floor
 0.00 s  domino7.g7 starts touching floor
 0.00 s  domino4.g4 starts touching floor
 0.00 s  domino10.g10 starts touching floor
 0.00 s  domino3.g3 starts touching floor
 0.00 s  domino9.g9 starts touching floor
 0.00 s  domino6.g6 starts touching floor
 0.00 s  domino2.g2 starts touching floor
 0.00 s  domino5.g5 starts touching floor
 0.00 s  domino8.g8 starts touching floor
 0.10 s  domino1.g1 first touches domino2.g2
 0.10 s  domino2 starts moving
 0.23 s  domino2.g2 first touches domino3.g3
 0.23 s  domino3 starts moving
 0.32 s  domino3.g3 first touches domino4.g4
 0.32 s  domino4 starts moving
 0.39 s  domino4.g4 first touches domino5.g5
 0.39 s  domino5 starts moving
 0.45 s  domino5.g5 first touches domino6.g6
 0.45 s  domino6 starts moving
 0.50 s  domino1 comes to rest at (0.05, 0.00, 0.02) m
 0.51 s  domino6.g6 first touches domino7.g7
 0.51 s  domino7 starts moving
 0.56 s  domino7.g7 first touches domino8.g8
 0.57 s  domino8 starts moving
 0.57 s  domino2 comes to rest at (0.10, 0.00, 0.02) m
 0.62 s  domino8.g8 first touches domino9.g9
 0.62 s  domino9 starts moving
 0.63 s  domino3 comes to rest at (0.15, 0.00, 0.02) m
 0.67 s  domino9.g9 first touches domino10.g10
 0.68 s  domino10 starts moving
 0.68 s  domino4 comes to rest at (0.20, 0.00, 0.02) m
 0.71 s  domino9.g9 leaves domino10.g10
 0.75 s  domino9.g9 touches domino10.g10 again
 0.77 s  domino5 comes to rest at (0.25, 0.00, 0.02) m
 0.80 s  domino6 comes to rest at (0.30, 0.00, 0.02) m
 0.81 s  domino7 comes to rest at (0.36, 0.00, 0.02) m
 0.81 s  domino8 comes to rest at (0.41, 0.00, 0.02) m
 0.83 s  domino9 comes to rest at (0.46, 0.00, 0.02) m
 0.89 s  domino10 comes to rest at (0.52, 0.00, 0.01) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.03); touching floor | domino2 at (0.05, 0.00, 0.05) m, at rest; touching floor | domino3 at (0.10, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.15, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.20, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.25, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.40, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.45, 0.00, 0.05) m, at rest; touching floor
0.25 s: domino1 at (0.04, 0.00, 0.04) m, moving 0.08 m/s (vx +0.07, vy -0.00, vz -0.04), turned 43° from how it started; touching domino2.g2, floor | domino2 at (0.07, 0.00, 0.05) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.04), turned 24° from how it started; touching domino1.g1, domino3.g3, floor | domino3 at (0.10, 0.00, 0.05) m, moving 0.19 m/s (vx +0.18, vy +0.00, vz +0.02), turned 3° from how it started; touching domino2.g2, floor | domino4 at (0.15, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.20, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.25, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.40, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.45, 0.00, 0.05) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.02) m, moving 0.06 m/s (vx +0.03, vy +0.00, vz -0.05), turned 69° from how it started; touching floor | domino2 at (0.10, 0.00, 0.03) m, moving 0.09 m/s (vx +0.05, vy +0.00, vz -0.08), turned 66° from how it started; touching domino3.g3, floor | domino3 at (0.15, 0.00, 0.03) m, moving 0.15 m/s (vx +0.10, vy -0.00, vz -0.12), turned 60° from how it started; touching domino2.g2, domino4.g4, floor | domino4 at (0.19, 0.00, 0.04) m, moving 0.25 m/s (vx +0.19, vy +0.00, vz -0.16), turned 49° from how it started; touching domino3.g3, floor | domino5 at (0.23, 0.00, 0.05) m, moving 0.31 m/s (vx +0.28, vy -0.00, vz -0.14), turned 35° from how it started; touching floor | domino6 at (0.26, 0.00, 0.05) m, moving 0.40 m/s (vx +0.39, vy +0.00, vz -0.09), turned 17° from how it started; touching nothing | domino7 at (0.30, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.35, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.40, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.45, 0.00, 0.05) m, at rest; touching floor
0.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, floor | domino2 at (0.10, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1.g1, domino3.g3, floor | domino3 at (0.15, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2.g2, domino4.g4, floor | domino4 at (0.20, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3.g3, domino5.g5, floor | domino5 at (0.25, 0.00, 0.02) m, at rest, turned 70° from how it started; touching domino4.g4, domino6.g6, floor | domino6 at (0.30, 0.00, 0.03) m, moving 0.09 m/s (vx +0.04, vy -0.00, vz -0.08), turned 68° from how it started; touching domino5.g5, domino7.g7, floor | domino7 at (0.35, 0.00, 0.03) m, moving 0.16 m/s (vx +0.09, vy +0.00, vz -0.13), turned 65° from how it started; touching domino6.g6, domino8.g8, floor | domino8 at (0.40, 0.00, 0.03) m, moving 0.29 m/s (vx +0.19, vy -0.00, vz -0.21), turned 59° from how it started; touching domino7.g7, floor | domino9 at (0.44, 0.00, 0.04) m, moving 0.45 m/s (vx +0.36, vy -0.00, vz -0.27), turned 48° from how it started; touching domino10.g10, floor | domino10 at (0.48, 0.00, 0.05) m, moving 0.56 m/s (vx +0.52, vy -0.00, vz -0.21), turned 32° from how it started; touching domino9.g9, floor
1.00 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, floor | domino2 at (0.10, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1.g1, domino3.g3, floor | domino3 at (0.15, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, domino4.g4, floor | domino4 at (0.21, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3.g3, domino5.g5, floor | domino5 at (0.25, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino4.g4, domino6.g6, floor | domino6 at (0.31, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino5.g5, domino7.g7, floor | domino7 at (0.36, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino6.g6, domino8.g8, floor | domino8 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7.g7, domino9.g9, floor | domino9 at (0.46, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino10.g10, domino8.g8, floor | domino10 at (0.52, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.g9, floor
1.25 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, floor | domino2 at (0.10, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1.g1, domino3.g3, floor | domino3 at (0.15, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, domino4.g4, floor | domino4 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3.g3, domino5.g5, floor | domino5 at (0.25, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino4.g4, domino6.g6, floor | domino6 at (0.31, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino5.g5, domino7.g7, floor | domino7 at (0.36, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino6.g6, domino8.g8, floor | domino8 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7.g7, domino9.g9, floor | domino9 at (0.46, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino10.g10, domino8.g8, floor | domino10 at (0.52, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.g9, floor
(the same through 5.75 s)
6.00 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, floor | domino2 at (0.10, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1.g1, domino3.g3, floor | domino3 at (0.15, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, domino4.g4, floor | domino4 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3.g3, domino5.g5, floor | domino5 at (0.25, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino4.g4, domino6.g6, floor | domino6 at (0.31, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino5.g5, domino7.g7, floor | domino7 at (0.36, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino6.g6, domino8.g8, floor | domino8 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7.g7, domino9.g9, floor | domino9 at (0.46, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.g10, domino8.g8, floor | domino10 at (0.52, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.g9, floor

At the end (6.00 s):
- domino1 at (0.05, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, floor
- domino2 at (0.10, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino1.g1, domino3.g3, floor
- domino3 at (0.15, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino2.g2, domino4.g4, floor
- domino4 at (0.20, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino3.g3, domino5.g5, floor
- domino5 at (0.25, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino4.g4, domino6.g6, floor
- domino6 at (0.31, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino5.g5, domino7.g7, floor
- domino7 at (0.36, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino6.g6, domino8.g8, floor
- domino8 at (0.41, 0.00, 0.02) m, at rest, turned 74° from how it started; touching domino7.g7, domino9.g9, floor
- domino9 at (0.46, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.g10, domino8.g8, floor
- domino10 at (0.52, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.g9, floor
</history>
