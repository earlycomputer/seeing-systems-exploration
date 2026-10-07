MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-0.97, 0.00, 0.29) m, at rest
- d1: free body; its geoms: d1; starts at (0.23, 0.00, 0.15) m, at rest
- d2: free body; its geoms: d2; starts at (0.38, 0.00, 0.15) m, at rest
- d3: free body; its geoms: d3; starts at (0.53, 0.00, 0.15) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.73, 0.00, 0.19) m, at rest

What happened, in order:
 0.00 s  ball2 starts touching ball2 support
 0.00 s  d1 starts touching floor
 0.00 s  d2 starts touching floor
 0.00 s  d3 starts touching floor
 0.00 s  ball1 first touches ramp
 0.04 s  ball1 starts moving
 1.22 s  ball1 leaves ramp
 1.27 s  ball1 first touches floor
 1.30 s  ball1 leaves floor
 1.31 s  ball1 first touches d1
 1.31 s  d1 starts moving
 1.32 s  d1 leaves floor
 1.34 s  ball1 leaves d1
 1.36 s  d1 touches floor again
 1.38 s  ball1 touches d1 again
 1.43 s  d1 first touches d2
 1.43 s  d2 starts moving
 1.43 s  ball1 leaves d1
 1.44 s  ball1 passes 0.09 m from d2 without touching it: nearest points (0.27, 0.00, 0.06) m and (0.37, 0.00, 0.06) m
 1.45 s  ball1 touches floor again
 1.46 s  d1 leaves d2
 1.48 s  ball1 comes to rest at (0.22, 0.00, 0.06) m
 1.54 s  d1 touches d2 again
 1.56 s  ball1 passes 0.24 m from d3 without touching it: nearest points (0.28, 0.00, 0.06) m and (0.52, 0.00, 0.06) m
 1.57 s  d2 first touches d3
 1.57 s  d3 starts moving
 1.57 s  d1 passes 0.04 m from d3 without touching it: nearest points (0.48, 0.00, 0.24) m and (0.52, 0.00, 0.24) m
 1.58 s  d2 leaves d3
 1.59 s  d1 leaves d2
 1.64 s  d1 touches d2 again
 1.66 s  d2 touches d3 again
 1.68 s  d2 leaves d3
 1.71 s  ball1 passes 0.41 m from ball2 without touching it: nearest points (0.28, 0.00, 0.07) m and (0.67, 0.00, 0.18) m
 1.72 s  d3 first touches ball2
 1.72 s  ball2 starts moving
 1.72 s  d2 touches d3 again
 1.72 s  d1 passes 0.12 m from ball2 without touching it: nearest points (0.56, 0.00, 0.15) m and (0.67, 0.00, 0.18) m
 1.72 s  d2 passes 0.04 m from ball2 without touching it: nearest points (0.63, 0.00, 0.18) m and (0.67, 0.00, 0.19) m
 1.73 s  d2 comes to rest at (0.51, 0.00, 0.10) m
 1.74 s  d1 comes to rest at (0.42, 0.00, 0.09) m
 1.75 s  d3 comes to rest at (0.62, 0.00, 0.13) m
 1.75 s  ball2 comes to rest at (0.74, 0.00, 0.19) m
 4.19 s  d3 first touches ball2 support
 4.20 s  d1 passes 0.09 m from ball2 support without touching it: nearest points (0.57, 0.00, 0.13) m and (0.66, 0.00, 0.13) m
 4.21 s  d2 passes 0.17 m from cup (cup_left_wall) without touching it: nearest points (0.65, 0.07, 0.16) m and (0.80, 0.15, 0.16) m
 4.22 s  d1 passes 0.25 m from cup (cup_near_wall) without touching it: nearest points (0.57, 0.00, 0.13) m and (0.79, 0.00, 0.04) m
 6.00 s  d2 passes 0.03 m from ball2 support without touching it: nearest points (0.65, 0.00, 0.15) m and (0.66, 0.00, 0.13) m
 6.00 s  d3 passes 0.10 m from cup (cup_left_wall) without touching it: nearest points (0.74, 0.07, 0.22) m and (0.80, 0.15, 0.20) m
 6.00 s  ball1 passes 0.38 m from ball2 support without touching it: nearest points (0.28, 0.00, 0.06) m and (0.66, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball1 at (-0.97, 0.00, 0.29) m, at rest; touching nothing | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
0.25 s: ball1 at (-0.92, 0.00, 0.28) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz -0.07); touching ramp | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
0.50 s: ball1 at (-0.80, 0.00, 0.25) m, moving 0.68 m/s (vx +0.67, vy -0.00, vz -0.14); touching ramp | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
0.75 s: ball1 at (-0.59, 0.00, 0.21) m, moving 1.01 m/s (vx +0.99, vy -0.00, vz -0.20); touching ramp | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
1.00 s: ball1 at (-0.30, 0.00, 0.15) m, moving 1.34 m/s (vx +1.31, vy -0.00, vz -0.27); touching ramp | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
1.25 s: ball1 at (0.06, 0.00, 0.07) m, moving 1.71 m/s (vx +1.59, vy -0.00, vz -0.63); touching nothing | d1 at (0.23, 0.00, 0.15) m, at rest; touching floor | d2 at (0.38, 0.00, 0.15) m, at rest; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
1.50 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.34, 0.00, 0.14) m, moving 0.44 m/s (vx +0.41, vy +0.00, vz -0.15), turned 25° from how it started; touching floor | d2 at (0.41, 0.00, 0.15) m, moving 0.46 m/s (vx +0.46, vy +0.00, vz -0.05), turned 12° from how it started; touching floor | d3 at (0.53, 0.00, 0.15) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.19) m, at rest; touching ball2 support
1.75 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.09) m, at rest, turned 59° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 52° from how it started; touching d1, d3, floor | d3 at (0.62, 0.00, 0.13) m, at rest, turned 32° from how it started; touching ball2, d2, floor | ball2 at (0.74, 0.00, 0.19) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching ball2 support, d3
2.00 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.09) m, at rest, turned 59° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 53° from how it started; touching d1, d3, floor | d3 at (0.62, 0.00, 0.13) m, at rest, turned 33° from how it started; touching ball2, d2, floor | ball2 at (0.74, 0.00, 0.19) m, at rest; touching ball2 support, d3
2.25 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.09) m, at rest, turned 60° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 53° from how it started; touching d1, d3, floor | d3 at (0.62, 0.00, 0.13) m, at rest, turned 34° from how it started; touching ball2, d2, floor | ball2 at (0.75, 0.00, 0.19) m, at rest; touching ball2 support, d3
2.50 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 61° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 54° from how it started; touching d1, d3, floor | d3 at (0.62, 0.00, 0.13) m, at rest, turned 35° from how it started; touching ball2, d2, floor | ball2 at (0.76, 0.00, 0.19) m, at rest; touching ball2 support, d3
2.75 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 61° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 55° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.13) m, at rest, turned 36° from how it started; touching ball2, d2, floor | ball2 at (0.76, 0.00, 0.19) m, at rest; touching ball2 support, d3
3.00 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 61° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.10) m, at rest, turned 56° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.13) m, at rest, turned 37° from how it started; touching ball2, d2, floor | ball2 at (0.77, 0.00, 0.19) m, at rest; touching ball2 support, d3
3.25 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 62° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.09) m, at rest, turned 56° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.13) m, at rest, turned 38° from how it started; touching ball2, d2, floor | ball2 at (0.77, 0.00, 0.19) m, at rest; touching ball2 support, d3
3.50 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 62° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 57° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.12) m, at rest, turned 39° from how it started; touching ball2, d2, floor | ball2 at (0.78, 0.00, 0.19) m, at rest; touching ball2 support, d3
3.75 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.43, 0.00, 0.08) m, at rest, turned 63° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 57° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.12) m, at rest, turned 40° from how it started; touching ball2, d2, floor | ball2 at (0.78, 0.00, 0.19) m, at rest; touching ball2 support, d3
4.00 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.43, 0.00, 0.08) m, at rest, turned 63° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.12) m, at rest, turned 41° from how it started; touching ball2, d2, floor | ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
4.25 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.43, 0.00, 0.08) m, at rest, turned 63° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (0.64, 0.00, 0.12) m, at rest, turned 41° from how it started; touching ball2, ball2 support, d2, floor | ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
4.50 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.43, 0.00, 0.08) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (0.64, 0.00, 0.12) m, at rest, turned 41° from how it started; touching ball2, ball2 support, d2, floor | ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
(the same through 4.75 s)
5.00 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (0.52, 0.00, 0.09) m, at rest, turned 59° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.12) m, at rest, turned 42° from how it started; touching ball2, ball2 support, d2, floor | ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
(the same through 5.50 s)
5.75 s: ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor | d1 at (0.42, 0.00, 0.08) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (0.51, 0.00, 0.09) m, at rest, turned 59° from how it started; touching d1, d3, floor | d3 at (0.63, 0.00, 0.12) m, at rest, turned 42° from how it started; touching ball2, ball2 support, d2, floor | ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.22, 0.00, 0.06) m, at rest; touching floor
- d1 at (0.42, 0.00, 0.08) m, at rest, turned 64° from how it started; touching d2, floor
- d2 at (0.51, 0.00, 0.09) m, at rest, turned 59° from how it started; touching d1, d3, floor
- d3 at (0.63, 0.00, 0.12) m, at rest, turned 42° from how it started; touching ball2, ball2 support, d2, floor
- ball2 at (0.79, 0.00, 0.19) m, at rest; touching ball2 support, d3
</history>
