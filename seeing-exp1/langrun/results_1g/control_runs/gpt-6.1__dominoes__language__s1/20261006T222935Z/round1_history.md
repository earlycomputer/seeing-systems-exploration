MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1; starts at (0.00, 0.00, 0.05) m, at rest
- domino2: free body; its geoms: domino2; starts at (0.03, 0.00, 0.05) m, at rest
- domino3: free body; its geoms: domino3; starts at (0.06, 0.00, 0.05) m, at rest
- domino4: free body; its geoms: domino4; starts at (0.09, 0.00, 0.05) m, at rest
- domino5: free body; its geoms: domino5; starts at (0.12, 0.00, 0.05) m, at rest
- domino6: free body; its geoms: domino6; starts at (0.15, 0.00, 0.05) m, at rest
- domino7: free body; its geoms: domino7; starts at (0.18, 0.00, 0.05) m, at rest
- domino8: free body; its geoms: domino8; starts at (0.21, 0.00, 0.05) m, at rest
- domino9: free body; its geoms: domino9; starts at (0.24, 0.00, 0.05) m, at rest
- domino10: free body; its geoms: domino10; starts at (0.27, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  domino1 starts touching floor
 0.00 s  domino7 starts touching floor
 0.00 s  domino4 starts touching floor
 0.00 s  domino10 starts touching floor
 0.00 s  domino3 starts touching floor
 0.00 s  domino9 starts touching floor
 0.00 s  domino6 starts touching floor
 0.00 s  domino2 starts touching floor
 0.00 s  domino5 starts touching floor
 0.00 s  domino8 starts touching floor
 0.01 s  domino1 starts moving
 0.08 s  domino1 first touches domino2
 0.08 s  domino2 starts moving
 0.19 s  domino2 first touches domino3
 0.19 s  domino3 starts moving
 0.28 s  domino3 first touches domino4
 0.28 s  domino4 starts moving
 0.30 s  domino3 leaves domino4
 0.34 s  domino3 touches domino4 again
 0.34 s  domino4 first touches domino5
 0.34 s  domino5 starts moving
 0.40 s  domino5 first touches domino6
 0.40 s  domino6 starts moving
 0.41 s  domino5 leaves domino6
 0.44 s  domino6 first touches domino7
 0.44 s  domino7 starts moving
 0.45 s  domino5 touches domino6 again
 0.48 s  domino7 first touches domino8
 0.48 s  domino8 starts moving
 0.53 s  domino8 first touches domino9
 0.53 s  domino9 starts moving
 0.56 s  domino9 first touches domino10
 0.56 s  domino10 starts moving
 0.58 s  domino9 leaves domino10
 0.59 s  domino8 leaves domino9
 0.62 s  domino8 touches domino9 again
 0.63 s  domino9 touches domino10 again
 0.69 s  domino9 leaves floor
 0.69 s  domino1 comes to rest at (0.05, 0.00, 0.02) m
 0.69 s  domino6 leaves floor
 0.69 s  domino2 comes to rest at (0.08, 0.00, 0.02) m
 0.69 s  domino3 comes to rest at (0.11, 0.00, 0.02) m
 0.70 s  domino4 comes to rest at (0.14, 0.00, 0.02) m
 0.70 s  domino5 comes to rest at (0.17, 0.00, 0.02) m
 0.71 s  domino8 leaves floor
 0.72 s  domino6 comes to rest at (0.21, 0.00, 0.02) m
 0.72 s  domino7 comes to rest at (0.24, 0.00, 0.02) m
 0.72 s  domino8 comes to rest at (0.27, 0.00, 0.02) m
 0.72 s  domino6 touches floor again
 0.72 s  domino9 comes to rest at (0.30, 0.00, 0.02) m
 0.73 s  domino3 leaves floor
 0.76 s  domino10 comes to rest at (0.33, 0.00, 0.00) m
 0.82 s  domino8 touches floor again
 1.00 s  domino3 touches floor again
 1.10 s  domino6 leaves floor
 2.22 s  domino9 touches floor again
 2.93 s  domino6 touches floor again

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.05) m, at rest; touching floor | domino2 at (0.03, 0.00, 0.05) m, at rest; touching floor | domino3 at (0.06, 0.00, 0.05) m, at rest; touching floor | domino4 at (0.09, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.12, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.15, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.21, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.27, 0.00, 0.05) m, at rest; touching floor
0.25 s: domino1 at (0.02, 0.00, 0.05) m, moving 0.12 m/s (vx +0.10, vy +0.00, vz -0.05), turned 31° from how it started; touching floor | domino2 at (0.05, 0.00, 0.05) m, moving 0.13 m/s (vx +0.12, vy +0.00, vz -0.03), turned 18° from how it started; touching floor | domino3 at (0.07, 0.00, 0.05) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.00), turned 7° from how it started; touching floor | domino4 at (0.09, 0.00, 0.05) m, at rest; touching floor | domino5 at (0.12, 0.00, 0.05) m, at rest; touching floor | domino6 at (0.15, 0.00, 0.05) m, at rest; touching floor | domino7 at (0.18, 0.00, 0.05) m, at rest; touching floor | domino8 at (0.21, 0.00, 0.05) m, at rest; touching floor | domino9 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.27, 0.00, 0.05) m, at rest; touching floor
0.50 s: domino1 at (0.04, 0.00, 0.03) m, moving 0.12 m/s (vx +0.07, vy -0.00, vz -0.10), turned 61° from how it started; touching floor | domino2 at (0.07, 0.00, 0.03) m, moving 0.17 m/s (vx +0.11, vy +0.00, vz -0.13), turned 56° from how it started; touching floor | domino3 at (0.10, 0.00, 0.04) m, moving 0.15 m/s (vx +0.12, vy +0.00, vz -0.09), turned 50° from how it started; touching domino4, floor | domino4 at (0.13, 0.00, 0.04) m, moving 0.15 m/s (vx +0.13, vy -0.00, vz -0.08), turned 44° from how it started; touching domino3, domino5, floor | domino5 at (0.15, 0.00, 0.04) m, moving 0.19 m/s (vx +0.18, vy +0.00, vz -0.08), turned 36° from how it started; touching domino4, domino6, floor | domino6 at (0.17, 0.00, 0.05) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.05), turned 25° from how it started; touching domino5, domino7, floor | domino7 at (0.19, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.03), turned 14° from how it started; touching domino6, domino8, floor | domino8 at (0.21, 0.00, 0.05) m, moving 0.28 m/s (vx +0.28, vy +0.00, vz +0.01), turned 3° from how it started; touching domino7, floor | domino9 at (0.24, 0.00, 0.05) m, at rest; touching floor | domino10 at (0.27, 0.00, 0.05) m, at rest; touching floor
0.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino2, domino4 | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino5, domino7, floor | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino7, domino9 | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino10, domino8 | domino10 at (0.33, 0.00, 0.00) m, moving 0.07 m/s (vx +0.00, vy +0.00, vz +0.07), turned 92° from how it started; touching domino9, floor
1.00 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino5, domino7, floor | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino10, domino8 | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
1.25 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino5, domino7 | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino10, domino8 | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
(the same through 1.50 s)
1.75 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino5, domino7 | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino10, domino8 | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
2.00 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 71° from how it started; touching domino5, domino7 | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10, domino8 | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
2.25 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino5, domino7 | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10, domino8, floor | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
(the same through 2.75 s)
3.00 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino5, domino7, floor | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10, domino8, floor | domino10 at (0.33, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
3.25 s: domino1 at (0.05, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino5, domino7, floor | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino10, domino8, floor | domino10 at (0.34, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
(the same through 4.50 s)
4.75 s: domino1 at (0.04, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor | domino2 at (0.08, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1, domino3, floor | domino3 at (0.11, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, domino4, floor | domino4 at (0.14, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino3, domino5, floor | domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor | domino6 at (0.21, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino5, domino7, floor | domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor | domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor | domino9 at (0.30, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino10, domino8, floor | domino10 at (0.34, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.04, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, floor
- domino2 at (0.08, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino1, domino3, floor
- domino3 at (0.11, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino2, domino4, floor
- domino4 at (0.14, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino3, domino5, floor
- domino5 at (0.17, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino4, domino6, floor
- domino6 at (0.21, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino5, domino7, floor
- domino7 at (0.24, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino6, domino8, floor
- domino8 at (0.27, 0.00, 0.02) m, at rest, turned 72° from how it started; touching domino7, domino9, floor
- domino9 at (0.30, 0.00, 0.02) m, at rest, turned 73° from how it started; touching domino10, domino8, floor
- domino10 at (0.34, 0.00, 0.00) m, at rest, turned 90° from how it started; touching domino9, floor
</history>
