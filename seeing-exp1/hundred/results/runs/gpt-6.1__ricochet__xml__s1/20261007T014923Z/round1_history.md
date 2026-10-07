MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball_sphere; starts at (0.00, 0.00, 3.34) m, at rest
- target: hinge joint target_hinge about axis (0.00, -1.00, 0.00), range -63.0254° to 0° as MuJoCo applies it; its geoms: target_axle, target_strike_paddle, target_release_shelf, target_release_lip, target_counterweight_arm, target_counterweight; starts at 0.0°, still
- block: free body; its geoms: block_payload; starts at (0.25, 0.65, 1.03) m, at rest

What happened, in order:
 0.00 s  target_release_shelf starts touching block_payload
 0.00 s  target starts at its upper stop (0°)
 0.00 s  target is at its largest, 0.0°
 0.01 s  ball starts moving
 0.45 s  ball_sphere first touches wall1_surface
 0.47 s  ball_sphere leaves wall1_surface
 0.75 s  ball_sphere first touches wall2_surface
 0.77 s  ball_sphere leaves wall2_surface
 0.99 s  target_release_shelf leaves block_payload
 0.99 s  ball_sphere first touches target_strike_paddle
 1.00 s  block starts moving
 1.00 s  ball_sphere leaves target_strike_paddle
 1.07 s  ball_sphere touches target_strike_paddle again
 1.18 s  ball_sphere leaves target_strike_paddle
 1.21 s  ball_sphere touches target_strike_paddle again
 1.27 s  target reaches its lower stop (-63.0254°) moving -298°/s
 1.27 s  target is at its smallest, -63.3°
 1.27 s  ball passes 0.46 m from hinge_mount (hinge_mount_bearing) without touching it: nearest points (-0.21, -0.08, 0.84) m and (-0.34, -0.51, 0.90) m
 1.29 s  ball_sphere leaves target_strike_paddle
 1.36 s  ball_sphere touches target_strike_paddle again
 1.36 s  ball_sphere leaves target_strike_paddle
 1.40 s  ball_sphere touches target_strike_paddle 5 more times between 1.40 s and 1.66 s
 1.41 s  target passes 0.10 m from bin (bin_back) without touching it: nearest points (-0.06, 0.80, 0.34) m and (-0.06, 0.90, 0.34) m
 1.41 s  block_payload first touches bin_bottom
 1.44 s  block_payload leaves bin_bottom
 1.50 s  block_payload touches bin_bottom again
 1.50 s  block comes to rest at (0.25, 0.65, 0.17) m
 1.66 s  ball passes 0.27 m from bin (bin_front) without touching it: nearest points (0.06, 0.08, 0.36) m and (0.06, 0.35, 0.36) m
 1.73 s  ball passes 0.47 m from block (block_payload) without touching it: nearest points (0.15, 0.08, 0.18) m and (0.15, 0.55, 0.18) m
 1.77 s  ball_sphere first touches floor
 1.79 s  ball_sphere leaves floor
 1.85 s  ball_sphere touches floor again
 2.08 s  ball comes to rest at (0.32, 0.00, 0.08) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 3.34) m, at rest; touching nothing | target at 0.0°, still; touching block_payload | block at (0.25, 0.65, 1.03) m, at rest; touching target_release_shelf
0.25 s: ball at (0.00, 0.00, 3.03) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | target at 0.0°, still; touching block_payload | block at (0.25, 0.65, 1.03) m, at rest; touching target_release_shelf
0.50 s: ball at (0.18, 0.00, 2.30) m, moving 4.12 m/s (vx +4.03, vy +0.00, vz -0.88); touching nothing | target at 0.0°, still; touching block_payload | block at (0.25, 0.65, 1.03) m, at rest; touching target_release_shelf
0.75 s: ball at (1.19, 0.00, 1.77) m, moving 5.23 m/s (vx +4.03, vy -0.00, vz -3.33); touching nothing | target at 0.0°, still; touching block_payload | block at (0.25, 0.65, 1.03) m, at rest; touching target_release_shelf
1.00 s: ball at (0.28, 0.00, 1.00) m, moving 2.81 m/s (vx -2.65, vy -0.00, vz -0.92); touching target_strike_paddle | target at -1.6°, turning -178°/s; touching ball_sphere | block at (0.25, 0.65, 1.03) m, moving 0.10 m/s (vx -0.00, vy -0.00, vz -0.10); touching nothing
1.25 s: ball at (-0.17, 0.00, 0.84) m, moving 0.66 m/s (vx -0.56, vy +0.00, vz -0.37); touching nothing | target at -57.4°, turning -290°/s; touching nothing | block at (0.25, 0.65, 0.71) m, moving 2.55 m/s (vx -0.00, vy -0.00, vz -2.55); touching nothing
1.50 s: ball at (-0.10, 0.00, 0.67) m, moving 1.53 m/s (vx +0.82, vy +0.00, vz -1.29); touching nothing | target at -63.0°, still; touching nothing | block at (0.25, 0.65, 0.17) m, moving 0.28 m/s (vx +0.00, vy +0.00, vz -0.28); touching nothing
1.75 s: ball at (0.18, 0.00, 0.13) m, moving 3.35 m/s (vx +1.37, vy +0.00, vz -3.05); touching nothing | target at -63.0°, still; touching nothing | block at (0.25, 0.65, 0.17) m, at rest; touching bin_bottom
2.00 s: ball at (0.31, 0.00, 0.08) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.01); touching floor | target at -63.0°, still; touching nothing | block at (0.25, 0.65, 0.17) m, at rest; touching bin_bottom
2.25 s: ball at (0.32, 0.00, 0.08) m, at rest; touching floor | target at -63.0°, still; touching nothing | block at (0.25, 0.65, 0.17) m, at rest; touching bin_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.32, 0.00, 0.08) m, at rest; touching floor
- target at -63.0°, still; touching nothing
- block at (0.25, 0.65, 0.17) m, at rest; touching bin_bottom
</history>
