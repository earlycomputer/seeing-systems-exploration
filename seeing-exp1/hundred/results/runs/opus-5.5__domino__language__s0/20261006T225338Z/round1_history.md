MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.22, 0.00, 0.18) m, at rest
- d1: free body; its geoms: d1; starts at (1.45, 0.00, 0.05) m, at rest
- d2: free body; its geoms: d2; starts at (1.51, 0.00, 0.05) m, at rest
- d3: free body; its geoms: d3; starts at (1.57, 0.00, 0.05) m, at rest
- ball2: free body; its geoms: ball2; starts at (1.63, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching ramp
 0.00 s  d2 starts touching floor
 0.00 s  d1 starts touching floor
 0.00 s  ball2 starts touching shelf
 0.00 s  d3 starts touching floor
 0.06 s  ball1 starts moving
 1.72 s  ball1 leaves ramp
 1.72 s  ball1 first touches floor
 1.89 s  ball1 leaves floor
 1.89 s  ball1 first touches d1
 1.89 s  d1 starts moving
 1.93 s  d1 first touches d2
 1.93 s  d2 starts moving
 1.94 s  ball1 passes 0.03 m from d2 without touching it: nearest points (1.48, 0.00, 0.06) m and (1.50, 0.00, 0.06) m
 1.99 s  d2 first touches d3
 1.99 s  d3 starts moving
 1.99 s  ball1 passes 0.08 m from d3 without touching it: nearest points (1.48, 0.00, 0.06) m and (1.56, 0.00, 0.06) m
 1.99 s  ball1 passes 0.13 m from ball2 without touching it: nearest points (1.48, 0.00, 0.06) m and (1.61, 0.00, 0.06) m
 2.00 s  ball1 passes 0.13 m from shelf without touching it: nearest points (1.48, 0.00, 0.05) m and (1.61, 0.00, 0.04) m
 2.00 s  ball1 passes 0.23 m from cup (cup_near_wall) without touching it: nearest points (1.48, 0.00, 0.06) m and (1.71, 0.00, 0.04) m
 2.01 s  ball1 touches floor again
 2.03 s  ball1 leaves d1
 2.05 s  d3 first touches ball2
 2.05 s  ball2 starts moving
 2.07 s  d1 comes to rest at (1.51, 0.00, 0.03) m
 2.08 s  d2 comes to rest at (1.56, 0.00, 0.04) m
 2.09 s  d3 comes to rest at (1.60, 0.00, 0.05) m
 2.11 s  ball2 comes to rest at (1.64, 0.00, 0.06) m
 2.35 s  d3 first touches shelf
 2.37 s  d1 passes 0.05 m from shelf without touching it: nearest points (1.56, 0.00, 0.04) m and (1.61, 0.00, 0.04) m
 2.37 s  d1 passes 0.15 m from cup (cup_near_wall) without touching it: nearest points (1.56, 0.00, 0.04) m and (1.71, 0.00, 0.04) m
 3.31 s  ball1 comes to rest at (1.32, 0.00, 0.06) m

State every 0.25 s:
0.00 s: ball1 at (0.22, 0.00, 0.18) m, at rest; touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
0.25 s: ball1 at (0.24, 0.00, 0.17) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.02); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
0.50 s: ball1 at (0.31, 0.00, 0.16) m, moving 0.36 m/s (vx +0.36, vy +0.00, vz -0.04); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
0.75 s: ball1 at (0.42, 0.00, 0.15) m, moving 0.52 m/s (vx +0.52, vy +0.00, vz -0.06); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
1.00 s: ball1 at (0.57, 0.00, 0.13) m, moving 0.68 m/s (vx +0.67, vy +0.00, vz -0.07); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
1.25 s: ball1 at (0.75, 0.00, 0.11) m, moving 0.83 m/s (vx +0.82, vy -0.00, vz -0.10); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
1.50 s: ball1 at (0.98, 0.00, 0.09) m, moving 0.98 m/s (vx +0.97, vy -0.00, vz -0.11); touching ramp | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
1.75 s: ball1 at (1.24, 0.00, 0.06) m, moving 1.09 m/s (vx +1.09, vy +0.00, vz +0.03); touching floor | d1 at (1.45, 0.00, 0.05) m, at rest; touching floor | d2 at (1.51, 0.00, 0.05) m, at rest; touching floor | d3 at (1.57, 0.00, 0.05) m, at rest; touching floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
2.00 s: ball1 at (1.42, 0.00, 0.06) m, moving 0.14 m/s (vx -0.03, vy -0.00, vz -0.14); touching d1 | d1 at (1.50, 0.00, 0.04) m, moving 0.32 m/s (vx +0.26, vy -0.00, vz -0.18), turned 50° from how it started; touching ball1, d2 | d2 at (1.54, 0.00, 0.05) m, moving 0.30 m/s (vx +0.29, vy +0.00, vz -0.09), turned 32° from how it started; touching d1, d3, floor | d3 at (1.57, 0.00, 0.05) m, moving 0.28 m/s (vx +0.28, vy +0.00, vz +0.03), turned 2° from how it started; touching d2, floor | ball2 at (1.63, 0.00, 0.06) m, at rest; touching shelf
2.25 s: ball1 at (1.40, 0.00, 0.06) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 63° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.04) m, at rest, turned 54° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.05) m, at rest, turned 28° from how it started; touching ball2, d2, floor | ball2 at (1.64, 0.00, 0.06) m, at rest; touching d3, shelf
2.50 s: ball1 at (1.37, 0.00, 0.06) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz -0.00); touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 55° from how it started; touching d1, d3, floor | d3 at (1.61, 0.00, 0.05) m, at rest, turned 31° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
2.75 s: ball1 at (1.35, 0.00, 0.06) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz -0.00); touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 56° from how it started; touching d1, d3, floor | d3 at (1.61, 0.00, 0.05) m, at rest, turned 31° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
3.00 s: ball1 at (1.34, 0.00, 0.06) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 64° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 56° from how it started; touching d1, d3, floor | d3 at (1.61, 0.00, 0.05) m, at rest, turned 32° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
3.25 s: ball1 at (1.32, 0.00, 0.06) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 56° from how it started; touching d1, d3, floor | d3 at (1.61, 0.00, 0.05) m, at rest, turned 33° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
3.50 s: ball1 at (1.31, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 57° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.05) m, at rest, turned 34° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
3.75 s: ball1 at (1.30, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 57° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.05) m, at rest, turned 35° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
4.00 s: ball1 at (1.29, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 57° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.05) m, at rest, turned 35° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
4.25 s: ball1 at (1.29, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.56, 0.00, 0.03) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 36° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
4.50 s: ball1 at (1.28, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 65° from how it started; touching d2, floor | d2 at (1.55, 0.00, 0.03) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 37° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
4.75 s: ball1 at (1.27, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 66° from how it started; touching d2, floor | d2 at (1.55, 0.00, 0.03) m, at rest, turned 58° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 37° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
5.00 s: ball1 at (1.27, 0.00, 0.06) m, at rest; touching floor | d1 at (1.51, 0.00, 0.03) m, at rest, turned 66° from how it started; touching d2, floor | d2 at (1.55, 0.00, 0.03) m, at rest, turned 59° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 38° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
(the same through 5.25 s)
5.50 s: ball1 at (1.26, 0.00, 0.06) m, at rest; touching floor | d1 at (1.50, 0.00, 0.03) m, at rest, turned 66° from how it started; touching d2, floor | d2 at (1.55, 0.00, 0.03) m, at rest, turned 59° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 39° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
(the same through 5.75 s)
6.00 s: ball1 at (1.26, 0.00, 0.06) m, at rest; touching floor | d1 at (1.50, 0.00, 0.03) m, at rest, turned 66° from how it started; touching d2, floor | d2 at (1.55, 0.00, 0.03) m, at rest, turned 60° from how it started; touching d1, d3, floor | d3 at (1.60, 0.00, 0.04) m, at rest, turned 40° from how it started; touching ball2, d2, floor, shelf | ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf

At the end (6.00 s):
- ball1 at (1.26, 0.00, 0.06) m, at rest; touching floor
- d1 at (1.50, 0.00, 0.03) m, at rest, turned 66° from how it started; touching d2, floor
- d2 at (1.55, 0.00, 0.03) m, at rest, turned 60° from how it started; touching d1, d3, floor
- d3 at (1.60, 0.00, 0.04) m, at rest, turned 40° from how it started; touching ball2, d2, floor, shelf
- ball2 at (1.65, 0.00, 0.06) m, at rest; touching d3, shelf
</history>
