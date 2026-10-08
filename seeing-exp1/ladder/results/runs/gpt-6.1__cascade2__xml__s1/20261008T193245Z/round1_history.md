MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.45, 0.00, 0.54) m, at rest
- domino1: free body; its geoms: domino1_box; starts at (0.59, 0.00, 0.12) m, at rest
- domino2: free body; its geoms: domino2_box; starts at (0.77, 0.00, 0.12) m, at rest

What happened, in order:
 0.00 s  domino1_box starts touching floor
 0.00 s  domino2_box starts touching floor
 0.00 s  ball1_sphere first touches ramp1_surface
 0.03 s  ball1 starts moving
 1.06 s  ball1_sphere leaves ramp1_surface
 1.08 s  ball1_sphere first touches domino1_box
 1.08 s  domino1 starts moving
 1.09 s  ball1_sphere leaves domino1_box
 1.17 s  domino1_box first touches domino2_box
 1.17 s  domino2 starts moving
 1.18 s  ball1_sphere touches domino1_box again
 1.18 s  ball1 passes 0.11 m from domino2 (domino2_box) without touching it: nearest points (0.65, 0.00, 0.13) m and (0.76, 0.00, 0.12) m
 1.18 s  domino1_box leaves domino2_box
 1.19 s  ball1_sphere leaves domino1_box
 1.22 s  ball1_sphere touches domino1_box again
 1.26 s  domino1_box touches domino2_box again
 1.26 s  domino1_box leaves domino2_box
 1.29 s  ball1_sphere leaves domino1_box
 1.32 s  domino1_box touches domino2_box again
 1.35 s  ball1_sphere first touches floor
 1.36 s  ball1_sphere leaves floor
 1.39 s  domino1_box leaves domino2_box
 1.40 s  ball1_sphere touches floor again
 1.42 s  domino1_box touches domino2_box again
 1.44 s  domino1 comes to rest at (0.75, 0.00, 0.05) m
 1.51 s  domino2 comes to rest at (0.93, 0.00, 0.02) m
 2.05 s  ball1 comes to rest at (0.34, 0.00, 0.05) m
 6.00 s  domino1_box leaves floor

State every 0.25 s:
0.00 s: ball1 at (-0.45, 0.00, 0.54) m, at rest; touching nothing | domino1 at (0.59, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.77, 0.00, 0.12) m, at rest; touching floor
0.25 s: ball1 at (-0.40, 0.00, 0.52) m, moving 0.45 m/s (vx +0.42, vy +0.00, vz -0.15); touching nothing | domino1 at (0.59, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.77, 0.00, 0.12) m, at rest; touching floor
0.50 s: ball1 at (-0.24, 0.00, 0.46) m, moving 0.90 m/s (vx +0.84, vy +0.00, vz -0.32); touching nothing | domino1 at (0.59, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.77, 0.00, 0.12) m, at rest; touching floor
0.75 s: ball1 at (0.02, 0.00, 0.37) m, moving 1.34 m/s (vx +1.27, vy +0.00, vz -0.42); touching nothing | domino1 at (0.59, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.77, 0.00, 0.12) m, at rest; touching floor
1.00 s: ball1 at (0.39, 0.00, 0.23) m, moving 1.79 m/s (vx +1.69, vy +0.00, vz -0.58); touching ramp1_surface | domino1 at (0.59, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.77, 0.00, 0.12) m, at rest; touching floor
1.25 s: ball1 at (0.59, 0.00, 0.10) m, moving 0.53 m/s (vx -0.24, vy +0.00, vz -0.48); touching nothing | domino1 at (0.70, 0.00, 0.09) m, moving 0.63 m/s (vx +0.50, vy +0.00, vz -0.40), turned 50° from how it started; touching floor | domino2 at (0.81, 0.00, 0.12) m, moving 0.57 m/s (vx +0.56, vy -0.00, vz -0.10), turned 19° from how it started; touching nothing
1.50 s: ball1 at (0.47, 0.00, 0.05) m, moving 0.43 m/s (vx -0.43, vy -0.00, vz -0.00); touching nothing | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
1.75 s: ball1 at (0.39, 0.00, 0.05) m, moving 0.26 m/s (vx -0.26, vy -0.00, vz +0.02); touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
2.00 s: ball1 at (0.34, 0.00, 0.05) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz +0.00); touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
2.25 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
(the same through 3.00 s)
3.25 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching floor
3.50 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
(the same through 4.00 s)
4.25 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching nothing | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
4.50 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching floor
4.75 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
5.00 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
5.25 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box, floor | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
(the same through 5.75 s)
6.00 s: ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box | domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor

At the end (6.00 s):
- ball1 at (0.34, 0.00, 0.05) m, at rest; touching floor
- domino1 at (0.75, 0.00, 0.05) m, at rest, turned 77° from how it started; touching domino2_box
- domino2 at (0.93, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino1_box, floor
</history>
