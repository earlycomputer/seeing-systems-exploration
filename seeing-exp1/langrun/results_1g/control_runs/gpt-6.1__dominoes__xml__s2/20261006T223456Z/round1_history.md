MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_box; starts at (0.02, 0.00, 0.10) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz -0.02)
- domino2: free body; its geoms: domino2_box; starts at (0.08, 0.00, 0.10) m, at rest
- domino3: free body; its geoms: domino3_box; starts at (0.16, 0.00, 0.10) m, at rest
- domino4: free body; its geoms: domino4_box; starts at (0.24, 0.00, 0.10) m, at rest
- domino5: free body; its geoms: domino5_box; starts at (0.32, 0.00, 0.10) m, at rest
- domino6: free body; its geoms: domino6_box; starts at (0.40, 0.00, 0.10) m, at rest
- domino7: free body; its geoms: domino7_box; starts at (0.48, 0.00, 0.10) m, at rest
- domino8: free body; its geoms: domino8_box; starts at (0.56, 0.00, 0.10) m, at rest
- domino9: free body; its geoms: domino9_box; starts at (0.64, 0.00, 0.10) m, at rest
- domino10: free body; its geoms: domino10_box; starts at (0.72, 0.00, 0.10) m, at rest

What happened, in order:
 0.00 s  domino1_box starts touching floor
 0.00 s  domino7_box starts touching floor
 0.00 s  domino4_box starts touching floor
 0.00 s  domino10_box starts touching floor
 0.00 s  domino3_box starts touching floor
 0.00 s  domino9_box starts touching floor
 0.00 s  domino6_box starts touching floor
 0.00 s  domino2_box starts touching floor
 0.00 s  domino5_box starts touching floor
 0.00 s  domino8_box starts touching floor
 0.04 s  domino1_box first touches domino2_box
 0.04 s  domino2 starts moving
 0.06 s  domino1_box leaves domino2_box
 0.09 s  domino1_box touches domino2_box again
 0.23 s  domino2_box first touches domino3_box
 0.23 s  domino3 starts moving
 0.24 s  domino2_box leaves domino3_box
 0.29 s  domino2_box touches domino3_box again
 0.36 s  domino3_box first touches domino4_box
 0.36 s  domino4 starts moving
 0.37 s  domino3_box leaves domino4_box
 0.37 s  domino2_box leaves domino3_box
 0.41 s  domino2_box touches domino3_box again
 0.41 s  domino3_box touches domino4_box again
 0.46 s  domino4_box first touches domino5_box
 0.46 s  domino5 starts moving
 0.47 s  domino4_box leaves domino5_box
 0.52 s  domino4_box touches domino5_box again
 0.54 s  domino5_box first touches domino6_box
 0.54 s  domino6 starts moving
 0.54 s  domino1 passes 0.20 m from domino6 (domino6_box) without touching it: nearest points (0.19, -0.02, 0.10) m and (0.39, -0.02, 0.10) m
 0.55 s  domino4_box leaves domino5_box
 0.55 s  domino5_box leaves domino6_box
 0.59 s  domino4_box touches domino5_box again
 0.61 s  domino1 passes 0.27 m from domino7 (domino7_box) without touching it: nearest points (0.20, -0.01, 0.09) m and (0.47, -0.01, 0.09) m
 0.61 s  domino6_box first touches domino7_box
 0.61 s  domino7 starts moving
 0.62 s  domino5_box touches domino6_box again
 0.62 s  domino2 passes 0.20 m from domino7 (domino7_box) without touching it: nearest points (0.27, -0.04, 0.10) m and (0.47, -0.04, 0.09) m
 0.63 s  domino6_box leaves domino7_box
 0.63 s  domino5_box leaves domino6_box
 0.68 s  domino5_box touches domino6_box again
 0.68 s  domino1 passes 0.35 m from domino8 (domino8_box) without touching it: nearest points (0.20, -0.04, 0.08) m and (0.55, -0.04, 0.08) m
 0.68 s  domino2 passes 0.27 m from domino8 (domino8_box) without touching it: nearest points (0.28, -0.04, 0.09) m and (0.55, -0.04, 0.09) m
 0.68 s  domino7_box first touches domino8_box
 0.68 s  domino8 starts moving
 0.69 s  domino6_box touches domino7_box again
 0.69 s  domino3 passes 0.20 m from domino8 (domino8_box) without touching it: nearest points (0.35, 0.02, 0.10) m and (0.55, 0.02, 0.09) m
 0.71 s  domino6_box leaves domino7_box
 0.71 s  domino5_box leaves domino6_box
 0.71 s  domino7_box leaves domino8_box
 0.74 s  domino5_box touches domino6_box again
 0.75 s  domino6_box touches domino7_box again
 0.75 s  domino3 passes 0.27 m from domino9 (domino9_box) without touching it: nearest points (0.36, -0.04, 0.09) m and (0.63, -0.04, 0.09) m
 0.75 s  domino4 passes 0.20 m from domino9 (domino9_box) without touching it: nearest points (0.43, 0.04, 0.10) m and (0.63, 0.04, 0.10) m
 0.75 s  domino2 passes 0.35 m from domino9 (domino9_box) without touching it: nearest points (0.28, 0.02, 0.08) m and (0.63, 0.02, 0.08) m
 0.75 s  domino1 passes 0.42 m from domino9 (domino9_box) without touching it: nearest points (0.20, 0.01, 0.07) m and (0.63, 0.01, 0.07) m
 0.75 s  domino8_box first touches domino9_box
 0.75 s  domino9 starts moving
 0.76 s  domino7_box touches domino8_box again
 0.76 s  domino8_box leaves domino9_box
 0.77 s  domino7_box leaves domino8_box
 0.82 s  domino9_box first touches domino10_box
 0.82 s  domino10 starts moving
 0.82 s  domino4 passes 0.27 m from domino10 (domino10_box) without touching it: nearest points (0.44, 0.04, 0.08) m and (0.71, 0.04, 0.08) m
 0.82 s  domino5 passes 0.20 m from domino10 (domino10_box) without touching it: nearest points (0.51, -0.04, 0.10) m and (0.71, -0.04, 0.10) m
 0.82 s  domino3 passes 0.35 m from domino10 (domino10_box) without touching it: nearest points (0.36, -0.04, 0.08) m and (0.71, -0.04, 0.07) m
 0.82 s  domino2 passes 0.42 m from domino10 (domino10_box) without touching it: nearest points (0.28, -0.04, 0.07) m and (0.71, -0.04, 0.07) m
 0.82 s  domino7_box touches domino8_box again
 0.83 s  domino8_box touches domino9_box again
 0.83 s  domino1 comes to rest at (0.11, 0.00, 0.04) m
 0.83 s  domino9_box leaves domino10_box
 0.84 s  domino8_box leaves domino9_box
 0.89 s  domino8_box touches domino9_box again
 0.89 s  domino1 passes 0.13 m from domino5 (domino5_box) without touching it: nearest points (0.21, 0.04, 0.06) m and (0.33, 0.04, 0.02) m
 0.90 s  domino9_box touches domino10_box again
 0.92 s  domino2 passes 0.13 m from domino6 (domino6_box) without touching it: nearest points (0.29, 0.04, 0.06) m and (0.41, 0.04, 0.02) m
 0.97 s  domino3 passes 0.13 m from domino7 (domino7_box) without touching it: nearest points (0.37, -0.04, 0.06) m and (0.49, -0.04, 0.02) m
 0.97 s  domino4 passes 0.13 m from domino8 (domino8_box) without touching it: nearest points (0.45, -0.04, 0.06) m and (0.57, -0.04, 0.02) m
 0.97 s  domino5 passes 0.13 m from domino9 (domino9_box) without touching it: nearest points (0.53, -0.04, 0.07) m and (0.65, -0.04, 0.02) m
 0.97 s  domino2 comes to rest at (0.19, 0.00, 0.04) m
 0.98 s  domino6 passes 0.13 m from domino10 (domino10_box) without touching it: nearest points (0.61, -0.04, 0.07) m and (0.72, -0.04, 0.02) m
 0.99 s  domino3 passes 0.06 m from domino6 (domino6_box) without touching it: nearest points (0.37, 0.04, 0.06) m and (0.41, 0.04, 0.02) m
 0.99 s  domino7 passes 0.06 m from domino10 (domino10_box) without touching it: nearest points (0.69, -0.04, 0.06) m and (0.73, -0.04, 0.02) m
 0.99 s  domino3_box leaves floor
 0.99 s  domino3 comes to rest at (0.27, 0.00, 0.04) m
 1.00 s  domino9_box leaves floor
 1.00 s  domino4 comes to rest at (0.35, 0.00, 0.04) m
 1.00 s  domino1 passes 0.06 m from domino4 (domino4_box) without touching it: nearest points (0.21, 0.04, 0.06) m and (0.25, 0.04, 0.02) m
 1.00 s  domino2 passes 0.02 m from domino4 (domino4_box) without touching it: nearest points (0.24, 0.04, 0.05) m and (0.25, 0.04, 0.02) m
 1.00 s  domino2 passes 0.06 m from domino5 (domino5_box) without touching it: nearest points (0.29, 0.04, 0.06) m and (0.33, 0.04, 0.02) m
 1.00 s  domino3 passes 0.02 m from domino5 (domino5_box) without touching it: nearest points (0.32, 0.04, 0.05) m and (0.33, 0.04, 0.02) m
 1.00 s  domino4 passes 0.02 m from domino6 (domino6_box) without touching it: nearest points (0.45, 0.04, 0.06) m and (0.45, 0.04, 0.04) m
 1.00 s  domino4 passes 0.06 m from domino7 (domino7_box) without touching it: nearest points (0.45, -0.04, 0.06) m and (0.49, -0.04, 0.02) m
 1.00 s  domino5 passes 0.02 m from domino7 (domino7_box) without touching it: nearest points (0.49, -0.04, 0.05) m and (0.49, -0.04, 0.02) m
 1.00 s  domino5 passes 0.06 m from domino8 (domino8_box) without touching it: nearest points (0.53, -0.04, 0.06) m and (0.57, -0.04, 0.02) m
 1.00 s  domino6 passes 0.02 m from domino8 (domino8_box) without touching it: nearest points (0.56, -0.04, 0.05) m and (0.57, -0.04, 0.02) m
 1.00 s  domino6 passes 0.06 m from domino9 (domino9_box) without touching it: nearest points (0.61, -0.04, 0.06) m and (0.65, -0.04, 0.02) m
 1.00 s  domino7 passes 0.02 m from domino9 (domino9_box) without touching it: nearest points (0.65, -0.04, 0.05) m and (0.65, -0.04, 0.02) m
 1.00 s  domino8 passes 0.02 m from domino10 (domino10_box) without touching it: nearest points (0.73, -0.04, 0.04) m and (0.73, -0.04, 0.02) m
 1.00 s  domino5 comes to rest at (0.43, 0.00, 0.04) m
 1.02 s  domino5_box leaves floor
 1.03 s  domino6 comes to rest at (0.51, 0.00, 0.04) m
 1.03 s  domino7 comes to rest at (0.60, 0.00, 0.04) m
 1.04 s  domino7_box leaves floor
 1.04 s  domino9_box touches floor again
 1.04 s  domino8 comes to rest at (0.68, 0.00, 0.04) m
 1.04 s  domino9 comes to rest at (0.76, 0.00, 0.04) m
 1.04 s  domino9_box leaves floor
 1.05 s  domino10 comes to rest at (0.84, 0.00, 0.01) m
 1.75 s  domino3_box touches floor again
 3.06 s  domino5_box touches floor again

State every 0.25 s:
0.00 s: domino1 at (0.02, 0.00, 0.10) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz -0.02); touching floor | domino2 at (0.08, 0.00, 0.10) m, at rest; touching floor | domino3 at (0.16, 0.00, 0.10) m, at rest; touching floor | domino4 at (0.24, 0.00, 0.10) m, at rest; touching floor | domino5 at (0.32, 0.00, 0.10) m, at rest; touching floor | domino6 at (0.40, 0.00, 0.10) m, at rest; touching floor | domino7 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.56, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.64, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.72, 0.00, 0.10) m, at rest; touching floor
0.25 s: domino1 at (0.06, 0.00, 0.09) m, moving 0.11 m/s (vx +0.10, vy -0.00, vz -0.05), turned 21° from how it started; touching floor | domino2 at (0.11, 0.00, 0.10) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.02), turned 18° from how it started; touching floor | domino3 at (0.16, 0.00, 0.10) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz +0.02), turned 2° from how it started; touching floor | domino4 at (0.24, 0.00, 0.10) m, at rest; touching floor | domino5 at (0.32, 0.00, 0.10) m, at rest; touching floor | domino6 at (0.40, 0.00, 0.10) m, at rest; touching floor | domino7 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.56, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.64, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.72, 0.00, 0.10) m, at rest; touching floor
0.50 s: domino1 at (0.09, 0.00, 0.07) m, moving 0.11 m/s (vx +0.07, vy +0.00, vz -0.08), turned 45° from how it started; touching domino2_box, floor | domino2 at (0.16, 0.00, 0.08) m, moving 0.20 m/s (vx +0.15, vy -0.00, vz -0.13), turned 48° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.22, 0.00, 0.09) m, moving 0.30 m/s (vx +0.26, vy +0.00, vz -0.15), turned 37° from how it started; touching domino2_box, floor | domino4 at (0.28, 0.00, 0.10) m, moving 0.35 m/s (vx +0.33, vy -0.00, vz -0.10), turned 23° from how it started; touching floor | domino5 at (0.33, 0.00, 0.10) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz -0.01), turned 8° from how it started; touching floor | domino6 at (0.40, 0.00, 0.10) m, at rest; touching floor | domino7 at (0.48, 0.00, 0.10) m, at rest; touching floor | domino8 at (0.56, 0.00, 0.10) m, at rest; touching floor | domino9 at (0.64, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.72, 0.00, 0.10) m, at rest; touching floor
0.75 s: domino1 at (0.11, 0.00, 0.05) m, moving 0.08 m/s (vx +0.04, vy +0.00, vz -0.07), turned 57° from how it started; touching domino2_box, floor | domino2 at (0.18, 0.00, 0.05) m, moving 0.11 m/s (vx +0.05, vy +0.00, vz -0.10), turned 67° from how it started; touching domino1_box, domino3_box | domino3 at (0.26, 0.00, 0.05) m, moving 0.14 m/s (vx +0.08, vy +0.00, vz -0.12), turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.34, 0.00, 0.06) m, moving 0.24 m/s (vx +0.15, vy +0.00, vz -0.19), turned 60° from how it started; touching domino3_box, floor | domino5 at (0.41, 0.00, 0.07) m, moving 0.38 m/s (vx +0.27, vy -0.00, vz -0.27), turned 53° from how it started; touching floor | domino6 at (0.47, 0.00, 0.08) m, moving 0.41 m/s (vx +0.34, vy +0.00, vz -0.23), turned 43° from how it started; touching domino7_box, floor | domino7 at (0.53, 0.00, 0.09) m, moving 0.51 m/s (vx +0.47, vy -0.00, vz -0.20), turned 30° from how it started; touching domino6_box, floor | domino8 at (0.59, 0.00, 0.10) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz -0.08), turned 16° from how it started; touching floor | domino9 at (0.64, 0.00, 0.10) m, at rest; touching floor | domino10 at (0.72, 0.00, 0.10) m, at rest; touching floor
1.00 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 61° from how it started; touching domino2_box | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, moving 0.07 m/s (vx +0.06, vy +0.00, vz +0.03), turned 73° from how it started; touching domino4_box, domino6_box | domino6 at (0.51, 0.00, 0.04) m, moving 0.10 m/s (vx +0.08, vy +0.00, vz +0.06), turned 73° from how it started; touching domino5_box, domino7_box | domino7 at (0.59, 0.00, 0.04) m, moving 0.18 m/s (vx +0.15, vy +0.00, vz +0.09), turned 73° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, moving 0.21 m/s (vx +0.20, vy +0.00, vz +0.03), turned 74° from how it started; touching domino7_box, domino9_box | domino9 at (0.75, 0.00, 0.04) m, moving 0.28 m/s (vx +0.28, vy +0.00, vz -0.02), turned 74° from how it started; touching domino10_box, domino8_box | domino10 at (0.83, 0.00, 0.03) m, moving 1.31 m/s (vx +0.53, vy +0.00, vz -1.20), turned 76° from how it started; touching domino9_box, floor
1.25 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 72° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 72° from how it started; touching domino2_box, domino4_box | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box | domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.60, 0.00, 0.04) m, at rest, turned 72° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box | domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
1.50 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box | domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.60, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box | domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
1.75 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 61° from how it started; touching domino2_box, floor | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box | domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.60, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box | domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 3.00 s)
3.25 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 61° from how it started; touching domino2_box, floor | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.60, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box | domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 3.75 s)
4.00 s: domino1 at (0.11, 0.00, 0.04) m, at rest, turned 61° from how it started; touching domino2_box, floor | domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_box, domino8_box | domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box | domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.11, 0.00, 0.04) m, at rest, turned 61° from how it started; touching domino2_box, floor
- domino2 at (0.19, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino1_box, domino3_box, floor
- domino3 at (0.27, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino2_box, domino4_box, floor
- domino4 at (0.35, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino3_box, domino5_box, floor
- domino5 at (0.43, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino4_box, domino6_box, floor
- domino6 at (0.51, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino5_box, domino7_box, floor
- domino7 at (0.59, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino6_box, domino8_box
- domino8 at (0.67, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino7_box, domino9_box, floor
- domino9 at (0.76, 0.00, 0.04) m, at rest, turned 73° from how it started; touching domino10_box, domino8_box
- domino10 at (0.84, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
</history>
