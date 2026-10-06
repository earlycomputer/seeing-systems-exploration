MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1.d1; starts at (0.00, 0.00, 0.06) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz +0.02)
- domino2: free body; its geoms: domino2.d2; starts at (0.07, 0.00, 0.06) m, at rest
- domino3: free body; its geoms: domino3.d3; starts at (0.14, 0.00, 0.06) m, at rest
- domino4: free body; its geoms: domino4.d4; starts at (0.21, 0.00, 0.06) m, at rest
- domino5: free body; its geoms: domino5.d5; starts at (0.28, 0.00, 0.06) m, at rest
- domino6: free body; its geoms: domino6.d6; starts at (0.35, 0.00, 0.06) m, at rest
- domino7: free body; its geoms: domino7.d7; starts at (0.42, 0.00, 0.06) m, at rest
- domino8: free body; its geoms: domino8.d8; starts at (0.49, 0.00, 0.06) m, at rest
- domino9: free body; its geoms: domino9.d9; starts at (0.56, 0.00, 0.06) m, at rest
- domino10: free body; its geoms: domino10.d10; starts at (0.63, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  domino1.d1 starts touching floor
 0.00 s  domino7.d7 starts touching floor
 0.00 s  domino4.d4 starts touching floor
 0.00 s  domino10.d10 starts touching floor
 0.00 s  domino3.d3 starts touching floor
 0.00 s  domino9.d9 starts touching floor
 0.00 s  domino6.d6 starts touching floor
 0.00 s  domino2.d2 starts touching floor
 0.00 s  domino5.d5 starts touching floor
 0.00 s  domino8.d8 starts touching floor
 0.33 s  domino1.d1 first touches domino2.d2
 0.33 s  domino2 starts moving
 0.51 s  domino2.d2 first touches domino3.d3
 0.51 s  domino3 starts moving
 0.61 s  domino3.d3 first touches domino4.d4
 0.62 s  domino4 starts moving
 0.62 s  domino1 passes 0.09 m from domino4 (domino4.d4) without touching it: nearest points (0.12, 0.00, 0.06) m and (0.20, 0.00, 0.06) m
 0.70 s  domino4.d4 first touches domino5.d5
 0.70 s  domino1 passes 0.15 m from domino5 (domino5.d5) without touching it: nearest points (0.12, -0.02, 0.05) m and (0.27, -0.02, 0.05) m
 0.70 s  domino5 starts moving
 0.71 s  domino2 passes 0.08 m from domino5 (domino5.d5) without touching it: nearest points (0.19, 0.00, 0.06) m and (0.27, 0.00, 0.05) m
 0.74 s  domino4.d4 leaves domino5.d5
 0.77 s  domino4.d4 touches domino5.d5 again
 0.78 s  domino5.d5 first touches domino6.d6
 0.78 s  domino1 comes to rest at (0.06, 0.00, 0.03) m
 0.78 s  domino6 starts moving
 0.78 s  domino1 passes 0.22 m from domino6 (domino6.d6) without touching it: nearest points (0.12, -0.02, 0.04) m and (0.34, -0.02, 0.04) m
 0.78 s  domino2 passes 0.15 m from domino6 (domino6.d6) without touching it: nearest points (0.19, 0.02, 0.05) m and (0.34, 0.02, 0.04) m
 0.78 s  domino3 passes 0.08 m from domino6 (domino6.d6) without touching it: nearest points (0.26, 0.02, 0.06) m and (0.34, 0.02, 0.06) m
 0.81 s  domino5.d5 leaves domino6.d6
 0.85 s  domino5.d5 touches domino6.d6 again
 0.85 s  domino1 passes 0.28 m from domino7 (domino7.d7) without touching it: nearest points (0.13, 0.00, 0.04) m and (0.41, 0.00, 0.04) m
 0.85 s  domino2 passes 0.22 m from domino7 (domino7.d7) without touching it: nearest points (0.19, 0.00, 0.04) m and (0.41, 0.00, 0.04) m
 0.85 s  domino3 passes 0.15 m from domino7 (domino7.d7) without touching it: nearest points (0.26, 0.00, 0.05) m and (0.41, 0.00, 0.05) m
 0.85 s  domino6.d6 first touches domino7.d7
 0.85 s  domino2 comes to rest at (0.13, 0.00, 0.03) m
 0.85 s  domino7 starts moving
 0.86 s  domino4 passes 0.08 m from domino7 (domino7.d7) without touching it: nearest points (0.33, 0.00, 0.06) m and (0.41, 0.00, 0.06) m
 0.89 s  domino6.d6 leaves domino7.d7
 0.92 s  domino1 passes 0.35 m from domino8 (domino8.d8) without touching it: nearest points (0.13, 0.00, 0.04) m and (0.48, 0.00, 0.04) m
 0.92 s  domino2 passes 0.28 m from domino8 (domino8.d8) without touching it: nearest points (0.20, 0.00, 0.04) m and (0.48, 0.00, 0.04) m
 0.93 s  domino7.d7 first touches domino8.d8
 0.93 s  domino8 starts moving
 0.93 s  domino6.d6 touches domino7.d7 again
 0.93 s  domino3 passes 0.22 m from domino8 (domino8.d8) without touching it: nearest points (0.26, 0.00, 0.04) m and (0.48, 0.00, 0.04) m
 0.93 s  domino4 passes 0.15 m from domino8 (domino8.d8) without touching it: nearest points (0.33, 0.00, 0.05) m and (0.48, 0.00, 0.04) m
 0.93 s  domino5 passes 0.08 m from domino8 (domino8.d8) without touching it: nearest points (0.40, 0.00, 0.06) m and (0.48, 0.00, 0.06) m
 0.94 s  domino3 comes to rest at (0.20, 0.00, 0.03) m
 0.96 s  domino7.d7 leaves domino8.d8
 0.99 s  domino2 passes 0.35 m from domino9 (domino9.d9) without touching it: nearest points (0.20, 0.02, 0.04) m and (0.55, 0.02, 0.04) m
 0.99 s  domino1 passes 0.42 m from domino9 (domino9.d9) without touching it: nearest points (0.13, 0.00, 0.03) m and (0.55, 0.00, 0.03) m
 1.00 s  domino7.d7 touches domino8.d8 again
 1.00 s  domino8.d8 first touches domino9.d9
 1.00 s  domino9 starts moving
 1.00 s  domino3 passes 0.28 m from domino9 (domino9.d9) without touching it: nearest points (0.27, 0.02, 0.04) m and (0.55, 0.02, 0.04) m
 1.00 s  domino4 passes 0.21 m from domino9 (domino9.d9) without touching it: nearest points (0.34, 0.00, 0.04) m and (0.55, 0.00, 0.04) m
 1.00 s  domino5 passes 0.15 m from domino9 (domino9.d9) without touching it: nearest points (0.40, 0.00, 0.05) m and (0.55, 0.00, 0.05) m
 1.00 s  domino6 passes 0.08 m from domino9 (domino9.d9) without touching it: nearest points (0.47, 0.00, 0.06) m and (0.55, 0.00, 0.06) m
 1.01 s  domino4 comes to rest at (0.28, 0.00, 0.03) m
 1.07 s  domino3 passes 0.35 m from domino10 (domino10.d10) without touching it: nearest points (0.27, 0.00, 0.03) m and (0.62, 0.00, 0.03) m
 1.07 s  domino4 passes 0.28 m from domino10 (domino10.d10) without touching it: nearest points (0.34, -0.01, 0.04) m and (0.62, -0.01, 0.04) m
 1.07 s  domino5 passes 0.22 m from domino10 (domino10.d10) without touching it: nearest points (0.40, 0.01, 0.04) m and (0.62, 0.01, 0.04) m
 1.07 s  domino6 passes 0.15 m from domino10 (domino10.d10) without touching it: nearest points (0.47, 0.00, 0.05) m and (0.62, 0.00, 0.05) m
 1.07 s  domino2 passes 0.42 m from domino10 (domino10.d10) without touching it: nearest points (0.20, 0.03, 0.03) m and (0.62, 0.03, 0.03) m
 1.07 s  domino1 passes 0.49 m from domino10 (domino10.d10) without touching it: nearest points (0.13, -0.02, 0.03) m and (0.62, -0.02, 0.03) m
 1.07 s  domino9.d9 first touches domino10.d10
 1.07 s  domino10 starts moving
 1.07 s  domino5 comes to rest at (0.35, 0.00, 0.03) m
 1.08 s  domino7 passes 0.08 m from domino10 (domino10.d10) without touching it: nearest points (0.54, 0.00, 0.06) m and (0.62, 0.00, 0.06) m
 1.11 s  domino9.d9 leaves domino10.d10
 1.14 s  domino9.d9 touches domino10.d10 again
 1.21 s  domino6 comes to rest at (0.42, 0.00, 0.03) m
 1.22 s  domino7 comes to rest at (0.49, 0.00, 0.03) m
 1.22 s  domino8 comes to rest at (0.56, 0.00, 0.03) m
 1.25 s  domino9 comes to rest at (0.63, 0.00, 0.02) m
 1.31 s  domino10 comes to rest at (0.71, 0.00, 0.01) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.06) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz +0.02); touching floor | domino2 at (0.07, 0.00, 0.06) m, at rest; touching floor | domino3 at (0.14, 0.00, 0.06) m, at rest; touching floor | domino4 at (0.21, 0.00, 0.06) m, at rest; touching floor | domino5 at (0.28, 0.00, 0.06) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.06) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.06) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.06) m, at rest; touching floor
0.25 s: domino1 at (0.02, 0.00, 0.06) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.01), turned 15° from how it started; touching floor | domino2 at (0.07, 0.00, 0.06) m, at rest; touching floor | domino3 at (0.14, 0.00, 0.06) m, at rest; touching floor | domino4 at (0.21, 0.00, 0.06) m, at rest; touching floor | domino5 at (0.28, 0.00, 0.06) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.06) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.06) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.06) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.05) m, moving 0.21 m/s (vx +0.17, vy +0.00, vz -0.12), turned 44° from how it started; touching floor | domino2 at (0.09, 0.00, 0.06) m, moving 0.29 m/s (vx +0.28, vy +0.00, vz -0.08), turned 23° from how it started; touching nothing | domino3 at (0.14, 0.00, 0.06) m, at rest; touching floor | domino4 at (0.21, 0.00, 0.06) m, at rest; touching floor | domino5 at (0.28, 0.00, 0.06) m, at rest; touching floor | domino6 at (0.35, 0.00, 0.06) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.06) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.06) m, at rest; touching floor
0.75 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 69° from how it started; touching domino2.d2, floor | domino2 at (0.13, 0.00, 0.04) m, moving 0.10 m/s (vx +0.05, vy +0.00, vz -0.08), turned 64° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.19, 0.00, 0.04) m, moving 0.20 m/s (vx +0.14, vy -0.00, vz -0.14), turned 54° from how it started; touching domino2.d2, floor | domino4 at (0.25, 0.00, 0.05) m, moving 0.29 m/s (vx +0.26, vy -0.00, vz -0.12), turned 37° from how it started; touching floor | domino5 at (0.29, 0.00, 0.06) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz -0.02), turned 14° from how it started; touching floor | domino6 at (0.35, 0.00, 0.06) m, at rest; touching floor | domino7 at (0.42, 0.00, 0.06) m, at rest; touching floor | domino8 at (0.49, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.56, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.63, 0.00, 0.06) m, at rest; touching floor
1.00 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 72° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, moving 0.06 m/s (vx +0.03, vy +0.00, vz -0.05), turned 70° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.34, 0.00, 0.03) m, moving 0.14 m/s (vx +0.08, vy -0.00, vz -0.12), turned 67° from how it started; touching domino4.d4, floor | domino6 at (0.41, 0.00, 0.04) m, moving 0.23 m/s (vx +0.16, vy +0.00, vz -0.17), turned 60° from how it started; touching domino7.d7, floor | domino7 at (0.47, 0.00, 0.05) m, moving 0.38 m/s (vx +0.32, vy +0.00, vz -0.22), turned 46° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.52, 0.00, 0.06) m, moving 0.41 m/s (vx +0.39, vy +0.00, vz -0.13), turned 25° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.56, 0.00, 0.06) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz +0.01); touching domino8.d8, floor | domino10 at (0.63, 0.00, 0.06) m, at rest; touching floor
1.25 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, floor | domino9 at (0.63, 0.00, 0.02) m, moving 0.05 m/s (vx +0.01, vy +0.00, vz +0.05), turned 76° from how it started; touching domino10.d10, floor | domino10 at (0.71, 0.00, 0.00) m, at rest, turned 96° from how it started; touching domino9.d9, floor
1.50 s: domino1 at (0.07, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
1.75 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
(the same through 2.00 s)
2.25 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
(the same through 2.50 s)
2.75 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 73° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
3.00 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.14, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
3.25 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.13, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.21, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
(the same through 5.25 s)
5.50 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor | domino2 at (0.13, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor | domino3 at (0.20, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor | domino4 at (0.28, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino3.d3, domino5.d5, floor | domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor | domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor | domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor | domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor | domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor | domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.06, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, floor
- domino2 at (0.13, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino1.d1, domino3.d3, floor
- domino3 at (0.20, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino2.d2, domino4.d4, floor
- domino4 at (0.28, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino3.d3, domino5.d5, floor
- domino5 at (0.35, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino4.d4, domino6.d6, floor
- domino6 at (0.42, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino5.d5, domino7.d7, floor
- domino7 at (0.49, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino6.d6, domino8.d8, floor
- domino8 at (0.56, 0.00, 0.03) m, at rest, turned 74° from how it started; touching domino7.d7, domino9.d9, floor
- domino9 at (0.63, 0.00, 0.02) m, at rest, turned 75° from how it started; touching domino10.d10, domino8.d8, floor
- domino10 at (0.71, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9.d9, floor
</history>
