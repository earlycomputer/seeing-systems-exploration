MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- target: hinge joint release_hinge about axis (0.00, 1.00, 0.00), range -90.0002° to 0° as MuJoCo applies it; its geoms: target, target.release shelf; starts at 0.0°, still
- block: free body; its geoms: block; starts at (1.33, 0.30, 1.31) m, at rest
- ball: free body; its geoms: ball; starts at (1.00, 0.00, 2.60) m, at rest

What happened, in order:
 0.00 s  target starts at its upper stop (0°)
 0.00 s  target.release shelf first touches block
 0.01 s  ball starts moving
 0.27 s  target is at its largest, 0.0°
 0.43 s  ball first touches wall1
 0.43 s  ball leaves wall1
 0.57 s  block passes 0.22 m from ball without touching it: nearest points (1.37, 0.26, 1.35) m and (1.41, 0.06, 1.41) m
 0.65 s  ball first touches wall2
 0.65 s  ball leaves wall2
 0.80 s  target first touches ball
 0.80 s  block starts moving
 0.81 s  target leaves ball
 0.83 s  target.release shelf leaves block
 0.86 s  target touches ball again
 0.87 s  target leaves ball
 0.89 s  block is at the top of its flight, at (1.28, 0.30, 1.33) m
 0.95 s  ball first touches bin_base
 0.97 s  ball leaves bin_base
 1.05 s  ball is at the top of its flight, at (1.44, 0.00, 0.13) m
 1.13 s  ball touches bin_base again
 1.15 s  ball leaves bin_base
 1.18 s  ball touches bin_base again
 1.27 s  target reaches its lower stop (-90.0002°) moving -305°/s
 1.29 s  target passes 0.17 m from bin (bin_left_wall) without touching it: nearest points (0.33, 0.42, 0.31) m and (0.33, 0.58, 0.28) m
 1.29 s  target is at its smallest, -92.2°
 1.35 s  target reaches its lower stop (-90.0002°) again moving +18°/s
 1.39 s  block first touches bin_base
 1.44 s  block leaves bin_base
 1.49 s  block is at the top of its flight, at (0.86, 0.30, 0.11) m
 1.55 s  block touches bin_base again
 1.72 s  block comes to rest at (0.84, 0.30, 0.08) m
 2.55 s  ball comes to rest at (2.03, 0.00, 0.10) m

State every 0.25 s:
0.00 s: target at 0.0°, still; touching nothing | block at (1.33, 0.30, 1.31) m, at rest; touching nothing | ball at (1.00, 0.00, 2.60) m, at rest; touching nothing
0.25 s: target at 0.0°, still; touching block | block at (1.33, 0.30, 1.31) m, at rest; touching target.release shelf | ball at (1.00, 0.00, 2.30) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: target at 0.0°, still; touching block | block at (1.33, 0.30, 1.31) m, at rest; touching target.release shelf | ball at (1.21, 0.00, 1.59) m, moving 3.55 m/s (vx +3.00, vy +0.00, vz -1.91); touching nothing
0.75 s: target at 0.0°, still; touching block | block at (1.33, 0.30, 1.31) m, at rest; touching target.release shelf | ball at (1.43, 0.00, 0.90) m, moving 4.01 m/s (vx -2.07, vy +0.00, vz -3.44); touching nothing
1.00 s: target at -28.0°, turning -163°/s; touching nothing | block at (1.20, 0.30, 1.27) m, moving 1.31 m/s (vx -0.71, vy +0.00, vz -1.11), turned 20° from how it started; touching nothing | ball at (1.40, 0.00, 0.12) m, moving 0.90 m/s (vx +0.76, vy -0.00, vz +0.48); touching nothing
1.25 s: target at -82.7°, turning -290°/s; touching nothing | block at (1.02, 0.30, 0.69) m, moving 3.63 m/s (vx -0.71, vy +0.00, vz -3.56), turned 49° from how it started; touching nothing | ball at (1.59, 0.00, 0.10) m, moving 0.70 m/s (vx +0.70, vy -0.00, vz +0.01); touching bin_base
1.50 s: target at -90.0°, still; touching nothing | block at (0.86, 0.30, 0.10) m, moving 0.50 m/s (vx -0.48, vy -0.00, vz -0.12), turned 153° from how it started; touching nothing | ball at (1.74, 0.00, 0.10) m, moving 0.56 m/s (vx +0.56, vy -0.00, vz -0.02); touching nothing
1.75 s: target at -90.0°, still; touching nothing | block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base | ball at (1.87, 0.00, 0.10) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz -0.02); touching nothing
2.00 s: target at -90.0°, still; touching nothing | block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base | ball at (1.95, 0.00, 0.10) m, moving 0.28 m/s (vx +0.28, vy -0.00, vz +0.01); touching bin_base
2.25 s: target at -90.0°, still; touching nothing | block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base | ball at (2.01, 0.00, 0.10) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.02); touching nothing
2.50 s: target at -90.0°, still; touching nothing | block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base | ball at (2.03, 0.00, 0.10) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching bin_base
2.75 s: target at -90.0°, still; touching nothing | block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base | ball at (2.04, 0.00, 0.10) m, at rest; touching bin_base
(the same through 6.00 s)

At the end (6.00 s):
- target at -90.0°, still; touching nothing
- block at (0.84, 0.30, 0.08) m, at rest, turned 180° from how it started; touching bin_base
- ball at (2.04, 0.00, 0.10) m, at rest; touching bin_base
</history>
