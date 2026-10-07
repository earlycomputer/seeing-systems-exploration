MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.21, 0.00, 0.43) m, at rest
- d1: free body; its geoms: d1; starts at (1.45, 0.00, 0.34) m, at rest
- d2: free body; its geoms: d2; starts at (1.51, 0.00, 0.34) m, at rest
- d3: free body; its geoms: d3; starts at (1.57, 0.00, 0.34) m, at rest
- ball2: free body; its geoms: ball2; starts at (1.62, 0.00, 0.32) m, at rest

What happened, in order:
 0.00 s  ball1 first touches ramp
 0.00 s  d1 first touches shelf
 0.00 s  ball2 first touches shelf
 0.00 s  d3 first touches shelf
 0.00 s  d2 first touches shelf
 0.09 s  ball1 starts moving
 1.85 s  ball1 first touches shelf
 1.86 s  ball1 leaves ramp
 2.03 s  ball1 leaves shelf
 2.03 s  ball1 first touches d1
 2.03 s  d1 starts moving
 2.08 s  d1 first touches d2
 2.08 s  d2 starts moving
 2.09 s  ball1 passes 0.03 m from d2 without touching it: nearest points (1.48, 0.00, 0.35) m and (1.51, 0.00, 0.35) m
 2.13 s  d2 first touches d3
 2.13 s  d3 starts moving
 2.14 s  ball1 passes 0.07 m from d3 without touching it: nearest points (1.49, 0.00, 0.36) m and (1.57, 0.00, 0.35) m
 2.18 s  ball1 passes 0.11 m from ball2 without touching it: nearest points (1.49, 0.00, 0.35) m and (1.61, 0.00, 0.32) m
 2.18 s  ball1 passes 0.26 m from cup (cup_near_wall) without touching it: nearest points (1.48, 0.00, 0.32) m and (1.68, 0.00, 0.15) m
 2.21 s  d3 first touches ball2
 2.21 s  ball2 starts moving
 2.21 s  d1 comes to rest at (1.50, 0.00, 0.31) m
 2.22 s  d2 comes to rest at (1.56, 0.00, 0.32) m
 2.25 s  d3 comes to rest at (1.61, 0.00, 0.33) m
 2.25 s  ball2 comes to rest at (1.63, 0.00, 0.32) m
 2.28 s  ball1 touches shelf again
 2.28 s  ball1 leaves d1
 3.15 s  ball1 touches ramp again
 3.15 s  ball1 leaves shelf
 4.05 s  ball1 touches shelf again
 4.05 s  ball1 leaves ramp
 4.93 s  ball1 leaves shelf
 4.93 s  ball1 touches d1 again
 5.05 s  ball1 touches shelf again
 5.05 s  ball1 leaves d1
 6.00 s  ball1 is still moving at the end, 0.18 m/s

State every 0.25 s:
0.00 s: ball1 at (0.21, 0.00, 0.43) m, at rest; touching nothing | d1 at (1.45, 0.00, 0.34) m, at rest; touching nothing | d2 at (1.51, 0.00, 0.34) m, at rest; touching nothing | d3 at (1.57, 0.00, 0.34) m, at rest; touching nothing | ball2 at (1.62, 0.00, 0.32) m, at rest; touching nothing
0.25 s: ball1 at (0.23, 0.00, 0.43) m, moving 0.15 m/s (vx +0.14, vy +0.00, vz -0.01); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
0.50 s: ball1 at (0.28, 0.00, 0.43) m, moving 0.29 m/s (vx +0.29, vy +0.00, vz -0.02); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
0.75 s: ball1 at (0.37, 0.00, 0.42) m, moving 0.44 m/s (vx +0.43, vy -0.00, vz -0.04); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
1.00 s: ball1 at (0.50, 0.00, 0.41) m, moving 0.58 m/s (vx +0.58, vy +0.00, vz -0.05); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
1.25 s: ball1 at (0.66, 0.00, 0.40) m, moving 0.73 m/s (vx +0.72, vy +0.00, vz -0.06); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
1.50 s: ball1 at (0.86, 0.00, 0.38) m, moving 0.87 m/s (vx +0.87, vy +0.00, vz -0.07); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
1.75 s: ball1 at (1.09, 0.00, 0.36) m, moving 1.02 m/s (vx +1.01, vy +0.00, vz -0.08); touching ramp | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
2.00 s: ball1 at (1.36, 0.00, 0.35) m, moving 1.07 m/s (vx +1.07, vy +0.00, vz +0.00); touching shelf | d1 at (1.45, 0.00, 0.34) m, at rest; touching shelf | d2 at (1.51, 0.00, 0.34) m, at rest; touching shelf | d3 at (1.57, 0.00, 0.34) m, at rest; touching shelf | ball2 at (1.62, 0.00, 0.32) m, at rest; touching shelf
2.25 s: ball1 at (1.44, 0.00, 0.35) m, moving 0.19 m/s (vx -0.17, vy -0.00, vz -0.08); touching d1 | d1 at (1.50, 0.00, 0.31) m, at rest, turned 77° from how it started; touching ball1, d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 71° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 45° from how it started; touching ball2, d2, shelf | ball2 at (1.63, 0.00, 0.32) m, at rest; touching d3, shelf
2.50 s: ball1 at (1.38, 0.00, 0.35) m, moving 0.26 m/s (vx -0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 72° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 46° from how it started; touching ball2, d2, shelf | ball2 at (1.63, 0.00, 0.32) m, at rest; touching d3, shelf
2.75 s: ball1 at (1.31, 0.00, 0.35) m, moving 0.26 m/s (vx -0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 73° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 49° from how it started; touching ball2, d2, shelf | ball2 at (1.64, 0.00, 0.32) m, at rest; touching d3, shelf
3.00 s: ball1 at (1.24, 0.00, 0.35) m, moving 0.26 m/s (vx -0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 73° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 51° from how it started; touching ball2, d2, shelf | ball2 at (1.64, 0.00, 0.32) m, at rest; touching d3, shelf
3.25 s: ball1 at (1.18, 0.00, 0.35) m, moving 0.20 m/s (vx -0.20, vy -0.00, vz +0.02); touching ramp | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 74° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 52° from how it started; touching ball2, d2, shelf | ball2 at (1.64, 0.00, 0.32) m, at rest; touching d3, shelf
3.50 s: ball1 at (1.15, 0.00, 0.35) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching ramp | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 74° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 54° from how it started; touching ball2, d2, shelf | ball2 at (1.64, 0.00, 0.32) m, at rest; touching d3, shelf
3.75 s: ball1 at (1.15, 0.00, 0.35) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.01); touching ramp | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.32) m, at rest, turned 75° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 55° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
4.00 s: ball1 at (1.19, 0.00, 0.35) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.02); touching ramp | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.31) m, at rest, turned 75° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 56° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
4.25 s: ball1 at (1.25, 0.00, 0.35) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.31) m, at rest, turned 76° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 57° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
4.50 s: ball1 at (1.32, 0.00, 0.35) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.31) m, at rest, turned 76° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 57° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
4.75 s: ball1 at (1.38, 0.00, 0.35) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf | d2 at (1.56, 0.00, 0.31) m, at rest, turned 76° from how it started; touching d1, d3, shelf | d3 at (1.61, 0.00, 0.33) m, at rest, turned 58° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
5.00 s: ball1 at (1.44, 0.00, 0.35) m, at rest; touching d1 | d1 at (1.50, 0.00, 0.31) m, at rest, turned 78° from how it started; touching ball1, d2, shelf | d2 at (1.56, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf | d3 at (1.62, 0.00, 0.32) m, at rest, turned 59° from how it started; touching ball2, d2, shelf | ball2 at (1.65, 0.00, 0.32) m, at rest; touching d3, shelf
5.25 s: ball1 at (1.40, 0.00, 0.35) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf | d2 at (1.55, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf | d3 at (1.62, 0.00, 0.32) m, at rest, turned 59° from how it started; touching ball2, d2, shelf | ball2 at (1.66, 0.00, 0.32) m, at rest; touching d3, shelf
5.50 s: ball1 at (1.35, 0.00, 0.35) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf | d2 at (1.55, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf | d3 at (1.62, 0.00, 0.32) m, at rest, turned 60° from how it started; touching ball2, d2, shelf | ball2 at (1.66, 0.00, 0.32) m, at rest; touching d3, shelf
5.75 s: ball1 at (1.31, 0.00, 0.35) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz -0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf | d2 at (1.55, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf | d3 at (1.62, 0.00, 0.32) m, at rest, turned 60° from how it started; touching ball2, d2, shelf | ball2 at (1.66, 0.00, 0.32) m, at rest; touching d3, shelf
6.00 s: ball1 at (1.26, 0.00, 0.35) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz +0.00); touching shelf | d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf | d2 at (1.55, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf | d3 at (1.62, 0.00, 0.32) m, at rest, turned 61° from how it started; touching ball2, d2, shelf | ball2 at (1.66, 0.00, 0.32) m, at rest; touching d3, shelf

At the end (6.00 s):
- ball1 at (1.26, 0.00, 0.35) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz +0.00); touching shelf
- d1 at (1.50, 0.00, 0.31) m, at rest, turned 79° from how it started; touching d2, shelf
- d2 at (1.55, 0.00, 0.31) m, at rest, turned 77° from how it started; touching d1, d3, shelf
- d3 at (1.62, 0.00, 0.32) m, at rest, turned 61° from how it started; touching ball2, d2, shelf
- ball2 at (1.66, 0.00, 0.32) m, at rest; touching d3, shelf
</history>
