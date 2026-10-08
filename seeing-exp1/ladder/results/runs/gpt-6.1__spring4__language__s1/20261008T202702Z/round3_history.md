Before the run, at the start:
- ball retainer already touches ball1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 8 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 8.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.02, 0.00, 0.54) m, at rest
- ball retainer: hinge joint ball_retainer_hinge about axis (0.00, 1.00, 0.00), range 0° to 29° as MuJoCo applies it; its geoms: ball retainer; starts at 0.0°, still
- cart1: free body; its geoms: cart1; starts at (-0.12, 0.00, 1.12) m, at rest
- left pusher arm: hinge joint left_cart_spring_hinge about axis (0.00, 1.00, 0.00), range -18.435° to 0° as MuJoCo applies it; its geoms: left pusher arm, left pusher arm.left pusher outer tip, left pusher arm.left pusher inner tip; starts at -18.4°, still
- right pusher arm: hinge joint right_cart_spring_hinge about axis (0.00, 1.00, 0.00), range 0° to 18.435° as MuJoCo applies it; its geoms: right pusher arm, right pusher arm.right pusher outer tip, right pusher arm.right pusher inner tip; starts at 18.4°, still
- pendulum1: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: pendulum1; starts at 0.0°, still
- door1: hinge joint door_hinge about axis (0.00, 0.00, 1.00), range -70° to 0° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (1.94, -0.09, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching ball retainer
 0.00 s  block1 starts touching floor
 0.00 s  ball retainer starts at its 0° stop (the end where it sits higher)
 0.00 s  left pusher arm starts at its -18.435° stop (the end where it sits higher)
 0.00 s  right pusher arm starts at its 18.435° stop (the end where it sits higher)
 0.00 s  right pusher arm is at its largest at the start, 18.4°
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  cart1 first touches left pusher arm.left pusher outer tip
 0.00 s  ball1 first touches ramp1
 0.00 s  cart1 first touches right pusher arm.right pusher outer tip
 0.00 s  cart1 first touches right pusher arm.right pusher inner tip
 0.00 s  cart1 first touches left pusher arm.left pusher inner tip
 0.00 s  cart1 starts moving
 0.01 s  ball retainer is at its smallest, -0.0°
 0.15 s  cart1 leaves left pusher arm.left pusher outer tip
 0.15 s  cart1 leaves right pusher arm.right pusher outer tip
 0.15 s  cart1 leaves right pusher arm.right pusher inner tip
 0.15 s  cart1 leaves left pusher arm.left pusher inner tip
 0.16 s  left pusher arm reaches its 0° stop (the end where it sits lower) moving +199°/s
 0.16 s  right pusher arm reaches its 0° stop (the end where it sits lower) moving -199°/s
 0.18 s  ball1 passes 0.37 m from right pusher arm without touching it: nearest points (0.02, 0.00, 0.59) m and (0.01, 0.00, 0.96) m
 0.18 s  ball retainer passes 0.42 m from right pusher arm without touching it: nearest points (0.08, 0.00, 0.55) m and (0.07, 0.00, 0.96) m
 0.18 s  ball1 passes 0.39 m from left pusher arm without touching it: nearest points (0.01, 0.00, 0.59) m and (-0.09, 0.00, 0.96) m
 0.18 s  ball retainer passes 0.44 m from left pusher arm without touching it: nearest points (0.08, 0.00, 0.55) m and (-0.09, 0.00, 0.96) m
 0.18 s  right pusher arm passes 0.47 m from ramp1 without touching it: nearest points (-0.01, 0.00, 0.96) m and (0.00, 0.00, 0.49) m
 0.18 s  left pusher arm passes 0.48 m from ramp1 without touching it: nearest points (-0.09, 0.06, 0.96) m and (0.00, 0.06, 0.49) m
 0.18 s  left pusher arm is at its largest, 1.4°
 0.18 s  right pusher arm is at its smallest, -1.4°
 0.23 s  left pusher arm reaches its 0° stop (the end where it sits lower) again moving -17°/s
 0.23 s  right pusher arm reaches its 0° stop (the end where it sits lower) again moving +17°/s
 0.28 s  ball1 first touches cart1
 0.28 s  ball1 starts moving
 0.28 s  ball retainer passes 0.09 m from cart1 without touching it: nearest points (0.07, 0.00, 0.54) m and (-0.01, 0.00, 0.56) m
 0.29 s  cart1 passes 0.07 m from ramp1 without touching it: nearest points (-0.02, 0.00, 0.56) m and (0.00, 0.00, 0.49) m
 0.29 s  ball1 leaves ball retainer
 0.29 s  ball1 leaves cart1
 0.35 s  ball1 touches ball retainer again
 0.37 s  ball1 leaves ball retainer
 0.41 s  ball1 touches ball retainer again
 0.41 s  ball1 leaves ball retainer
 0.44 s  ball1 touches ball retainer again
 0.44 s  ball1 leaves ball retainer
 0.46 s  cart1 first touches floor
 0.49 s  ball1 touches ball retainer 2 more times between 0.49 s and 0.55 s
 0.55 s  cart1 comes to rest at (-0.24, 0.00, 0.05) m
 0.83 s  ball retainer reaches its 29° stop (the end where it sits lower) moving +101°/s
 0.85 s  ball retainer is at its largest, 29.7°
 0.87 s  ball retainer reaches its 29° stop (the end where it sits lower) again moving -13°/s
 1.28 s  ball1 leaves ramp1
 1.30 s  ball1 first touches pendulum1
 1.33 s  ball1 leaves pendulum1
 1.47 s  ball1 first touches floor
 1.63 s  pendulum1 reaches its 40° stop (the end where it sits lower) moving +180°/s
 1.63 s  pendulum1 first touches door1
 1.65 s  pendulum1 leaves door1
 1.66 s  pendulum1 is at its largest, 40.5°
 1.66 s  pendulum1 passes 0.41 m from block1 without touching it: nearest points (1.47, 0.00, 0.06) m and (1.88, -0.03, 0.06) m
 2.14 s  ball1 touches pendulum1 again
 2.15 s  ball1 passes 0.20 m from door1 without touching it: nearest points (1.35, -0.04, 0.05) m and (1.48, -0.19, 0.05) m
 2.16 s  ball1 comes to rest at (1.32, 0.00, 0.05) m
 2.18 s  ball1 leaves pendulum1
 2.59 s  door1 reaches its -70° stop (neither end sits lower) moving -32°/s
 2.60 s  door1 first touches block1
 2.65 s  door1 leaves block1
 2.71 s  door1 touches block1 again
 2.74 s  door1 is at its smallest, -69.9°
 2.75 s  door1 leaves block1

State every 0.25 s:
0.00 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer | ball retainer at 0.0°, still; touching ball1 | cart1 at (-0.12, 0.00, 1.12) m, at rest; touching nothing | left pusher arm at -18.4°, still; touching nothing | right pusher arm at 18.4°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.25 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer, ramp1 | ball retainer at 0.0°, still; touching ball1 | cart1 at (-0.12, 0.00, 0.70) m, moving 3.07 m/s (vx -0.00, vy +0.00, vz -3.07); touching nothing | left pusher arm at 0.2°, turning -8°/s; touching nothing | right pusher arm at -0.2°, turning +8°/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.50 s: ball1 at (0.09, 0.00, 0.51) m, moving 0.35 m/s (vx +0.33, vy -0.00, vz -0.12); touching ramp1 | ball retainer at 8.7°, turning +40°/s; touching nothing | cart1 at (-0.24, 0.00, 0.04) m, moving 0.32 m/s (vx +0.05, vy -0.00, vz +0.31), turned 179° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.75 s: ball1 at (0.22, 0.00, 0.47) m, moving 0.86 m/s (vx +0.80, vy -0.00, vz -0.29); touching ramp1 | ball retainer at 21.8°, turning +74°/s; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
1.00 s: ball1 at (0.49, 0.00, 0.37) m, moving 1.45 m/s (vx +1.37, vy -0.00, vz -0.50); touching ramp1 | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
1.25 s: ball1 at (0.90, 0.00, 0.22) m, moving 2.05 m/s (vx +1.93, vy -0.00, vz -0.70); touching ramp1 | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
1.50 s: ball1 at (1.10, 0.00, 0.05) m, moving 0.37 m/s (vx +0.33, vy -0.00, vz +0.17); touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 20.1°, turning +119°/s; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
1.75 s: ball1 at (1.18, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz +0.00); touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -14.6°, turning -115°/s; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
2.00 s: ball1 at (1.27, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz +0.00); touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -38.5°, turning -79°/s; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
2.25 s: ball1 at (1.31, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -55.0°, turning -54°/s; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
2.50 s: ball1 at (1.30, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -66.2°, turning -37°/s; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
2.75 s: ball1 at (1.29, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching block1 | block1 at (1.94, -0.09, 0.06) m, at rest; touching door1, floor
3.00 s: ball1 at (1.28, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
3.25 s: ball1 at (1.27, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
3.50 s: ball1 at (1.26, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
3.75 s: ball1 at (1.25, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
4.00 s: ball1 at (1.23, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
4.25 s: ball1 at (1.22, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
4.50 s: ball1 at (1.21, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
4.75 s: ball1 at (1.20, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
5.00 s: ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
5.25 s: ball1 at (1.18, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
5.50 s: ball1 at (1.17, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
5.75 s: ball1 at (1.16, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
6.00 s: ball1 at (1.15, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
6.25 s: ball1 at (1.13, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
6.50 s: ball1 at (1.12, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
6.75 s: ball1 at (1.11, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
7.00 s: ball1 at (1.10, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
7.25 s: ball1 at (1.09, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
7.50 s: ball1 at (1.08, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
7.75 s: ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
8.00 s: ball1 at (1.06, 0.00, 0.05) m, at rest; touching floor | ball retainer at 29.0°, still; touching nothing | cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | left pusher arm at 0.0°, still; touching nothing | right pusher arm at -0.0°, still; touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at -69.9°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor

At the end (8.00 s):
- ball1 at (1.06, 0.00, 0.05) m, at rest; touching floor
- ball retainer at 29.0°, still; touching nothing
- cart1 at (-0.24, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor
- left pusher arm at 0.0°, still; touching nothing
- right pusher arm at -0.0°, still; touching nothing
- pendulum1 at 40.0°, still; touching nothing
- door1 at -69.9°, still; touching nothing
- block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
</history>
