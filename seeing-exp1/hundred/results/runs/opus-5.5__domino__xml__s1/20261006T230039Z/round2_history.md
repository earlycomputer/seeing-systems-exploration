MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (-0.99, 0.00, 0.16) m, at rest
- d1: free body; its geoms: d1_geom; starts at (0.30, 0.00, 0.05) m, at rest
- d2: free body; its geoms: d2_geom; starts at (0.37, 0.00, 0.05) m, at rest
- d3: free body; its geoms: d3_geom; starts at (0.44, 0.00, 0.05) m, at rest
- ball2: free body; its geoms: ball2_geom; starts at (0.50, 0.00, 0.07) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching ramp_slab
 0.00 s  d2_geom starts touching floor
 0.00 s  d1_geom starts touching floor
 0.00 s  ball2_geom starts touching stand_block
 0.00 s  d3_geom starts touching floor
 0.08 s  ball1 starts moving
 1.82 s  ball1_geom first touches floor
 1.83 s  ball1_geom leaves ramp_slab
 2.02 s  ball1_geom first touches d1_geom
 2.02 s  d1 starts moving
 2.03 s  ball1_geom leaves floor
 2.06 s  d1_geom first touches d2_geom
 2.06 s  d2 starts moving
 2.11 s  d2_geom first touches d3_geom
 2.11 s  d3 starts moving
 2.11 s  ball1 passes 0.08 m from d3 (d3_geom) without touching it: nearest points (0.35, 0.00, 0.07) m and (0.43, 0.00, 0.07) m
 2.15 s  d3_geom first touches ball2_geom
 2.15 s  ball1_geom touches floor again
 2.15 s  ball2 starts moving
 2.15 s  ball1 passes 0.12 m from ball2 (ball2_geom) without touching it: nearest points (0.35, 0.00, 0.07) m and (0.47, 0.00, 0.07) m
 2.15 s  ball1 comes to rest at (0.29, 0.00, 0.07) m
 2.16 s  d1 passes 0.06 m from ball2 (ball2_geom) without touching it: nearest points (0.42, 0.00, 0.06) m and (0.47, 0.00, 0.07) m
 2.16 s  ball1 passes 0.03 m from d2 (d2_geom) without touching it: nearest points (0.34, 0.00, 0.03) m and (0.37, 0.00, 0.01) m
 2.16 s  d3_geom first touches stand_block
 2.17 s  ball1 passes 0.12 m from stand (stand_block) without touching it: nearest points (0.35, 0.00, 0.06) m and (0.47, 0.00, 0.05) m
 2.17 s  ball1 passes 0.15 m from cup (cup_wall_near) without touching it: nearest points (0.35, 0.00, 0.06) m and (0.51, 0.00, 0.03) m
 2.17 s  d2 comes to rest at (0.41, 0.00, 0.04) m
 2.17 s  d1 comes to rest at (0.38, 0.00, 0.04) m
 2.17 s  d3 comes to rest at (0.46, 0.00, 0.05) m
 2.18 s  ball1_geom leaves d1_geom
 2.18 s  d3_geom leaves floor
 2.18 s  d1 passes 0.05 m from stand (stand_block) without touching it: nearest points (0.42, 0.00, 0.06) m and (0.47, 0.00, 0.05) m
 2.18 s  d1 passes 0.09 m from cup (cup_wall_left) without touching it: nearest points (0.42, 0.04, 0.06) m and (0.51, 0.07, 0.06) m
 2.21 s  d3_geom leaves ball2_geom
 2.31 s  ball2_geom leaves stand_block
 2.36 s  ball2_geom first touches cup_wall_near
 2.37 s  ball2_geom leaves cup_wall_near
 2.38 s  ball2_geom first touches cup_base
 2.41 s  d3_geom touches floor again
 2.67 s  ball2_geom first touches cup_wall_far
 2.68 s  ball2 comes to rest at (0.63, 0.00, 0.03) m
 2.73 s  ball2_geom leaves cup_wall_far

State every 0.25 s:
0.00 s: ball1 at (-0.99, 0.00, 0.16) m, at rest; touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
0.25 s: ball1 at (-0.97, 0.00, 0.16) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.01); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
0.50 s: ball1 at (-0.91, 0.00, 0.15) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.03); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
0.75 s: ball1 at (-0.82, 0.00, 0.14) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.04); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
1.00 s: ball1 at (-0.69, 0.00, 0.13) m, moving 0.60 m/s (vx +0.60, vy +0.00, vz -0.05); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
1.25 s: ball1 at (-0.52, 0.00, 0.12) m, moving 0.75 m/s (vx +0.75, vy +0.00, vz -0.07); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
1.50 s: ball1 at (-0.32, 0.00, 0.10) m, moving 0.90 m/s (vx +0.90, vy +0.00, vz -0.08); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
1.75 s: ball1 at (-0.07, 0.00, 0.08) m, moving 1.05 m/s (vx +1.04, vy +0.00, vz -0.09); touching ramp_slab | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
2.00 s: ball1 at (0.20, 0.00, 0.07) m, moving 1.08 m/s (vx +1.08, vy +0.00, vz +0.00); touching floor | d1 at (0.30, 0.00, 0.05) m, at rest; touching floor | d2 at (0.37, 0.00, 0.05) m, at rest; touching floor | d3 at (0.44, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.50, 0.00, 0.07) m, at rest; touching stand_block
2.25 s: ball1 at (0.28, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 52° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 47° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 20° from how it started; touching d2_geom, stand_block | ball2 at (0.51, 0.00, 0.07) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.03); touching stand_block
2.50 s: ball1 at (0.28, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 52° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 48° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 26° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.58, 0.00, 0.03) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz -0.00); touching cup_base
2.75 s: ball1 at (0.28, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 52° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 49° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 26° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.63, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: ball1 at (0.28, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 49° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 27° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: ball1 at (0.27, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 49° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 27° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: ball1 at (0.27, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 50° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 28° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
(the same through 3.75 s)
4.00 s: ball1 at (0.27, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 50° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 29° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: ball1 at (0.26, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 51° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 29° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: ball1 at (0.26, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 54° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 51° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 30° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
(the same through 5.00 s)
5.25 s: ball1 at (0.25, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 54° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 52° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 31° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
(the same through 5.50 s)
5.75 s: ball1 at (0.25, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 54° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 52° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 32° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: ball1 at (0.25, 0.00, 0.07) m, at rest; touching floor | d1 at (0.37, 0.00, 0.04) m, at rest, turned 55° from how it started; touching d2_geom, floor | d2 at (0.41, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d1_geom, d3_geom, floor | d3 at (0.46, 0.00, 0.05) m, at rest, turned 32° from how it started; touching d2_geom, floor, stand_block | ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (0.25, 0.00, 0.07) m, at rest; touching floor
- d1 at (0.37, 0.00, 0.04) m, at rest, turned 55° from how it started; touching d2_geom, floor
- d2 at (0.41, 0.00, 0.04) m, at rest, turned 53° from how it started; touching d1_geom, d3_geom, floor
- d3 at (0.46, 0.00, 0.05) m, at rest, turned 32° from how it started; touching d2_geom, floor, stand_block
- ball2 at (0.62, 0.00, 0.03) m, at rest; touching cup_base
</history>
