MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, -1.00, 0.00), no range limit; its geoms: pendulum1_rod, pendulum1_tip; starts at -55.0°, still
- ball1: free body; its geoms: ball1_sphere; starts at (0.07, 0.00, 0.49) m, at rest
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.45 m as MuJoCo applies it; its geoms: cart1_chassis; starts at 0.000 m, still

What happened, in order:
 0.00 s  ball1_sphere starts touching ramp1_surface
 0.00 s  cart1 starts at its lower stop (0 m)
 0.02 s  ball1 starts moving
 0.35 s  ball1_sphere leaves ramp1_surface
 0.35 s  pendulum1_tip first touches ball1_sphere
 0.37 s  pendulum1_tip leaves ball1_sphere
 0.39 s  ball1_sphere touches ramp1_surface again
 0.75 s  pendulum1 is at its largest, 31.7°
 0.80 s  ball1_sphere leaves ramp1_surface
 0.83 s  ball1_sphere first touches cart1_chassis
 0.84 s  ball1_sphere leaves cart1_chassis
 0.92 s  ball1 is at the top of its flight, at (1.04, 0.00, 0.20) m
 0.98 s  ball1_sphere touches cart1_chassis again
 1.09 s  ball1_sphere leaves cart1_chassis
 1.22 s  ball1_sphere first touches floor
 1.22 s  ball1 passes 0.01 m from cart_track (cart_track_left_rail) without touching it: nearest points (1.17, 0.05, 0.04) m and (1.17, 0.06, 0.04) m
 1.23 s  ball1_sphere leaves floor
 1.30 s  ball1_sphere touches floor again
 1.47 s  ball1 comes to rest at (1.19, 0.00, 0.05) m
 1.62 s  cart1 reaches its upper stop (0.45 m) moving +0.50 m/s
 1.64 s  cart1 is at its largest, 0.5 m
 1.64 s  cart1 passes 0.16 m from receiving_stop (receiving_stop_wall) without touching it: nearest points (1.69, 0.09, 0.11) m and (1.85, 0.09, 0.11) m
 2.84 s  pendulum1 passes 0.00 m from ramp1 (ramp1_surface) without touching it: nearest points (0.02, 0.00, 0.45) m and (0.02, 0.00, 0.45) m

State every 0.25 s:
0.00 s: pendulum1 at -55.0°, still; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ramp1_surface | cart1 at 0.000 m, still; touching nothing
0.25 s: pendulum1 at -28.6°, turning +190°/s; touching nothing | ball1 at (0.14, 0.00, 0.46) m, moving 0.57 m/s (vx +0.54, vy +0.00, vz -0.19); touching ramp1_surface | cart1 at 0.000 m, still; touching nothing
0.50 s: pendulum1 at 14.0°, turning +131°/s; touching nothing | ball1 at (0.40, 0.00, 0.37) m, moving 1.48 m/s (vx +1.40, vy +0.00, vz -0.48); touching ramp1_surface | cart1 at 0.000 m, still; touching nothing
0.75 s: pendulum1 at 31.7°, still; touching nothing | ball1 at (0.82, 0.00, 0.23) m, moving 2.05 m/s (vx +1.94, vy +0.00, vz -0.67); touching ramp1_surface | cart1 at 0.000 m, still; touching nothing
1.00 s: pendulum1 at 15.4°, turning -116°/s; touching nothing | ball1 at (1.09, 0.00, 0.18) m, moving 0.52 m/s (vx +0.52, vy +0.00, vz -0.02); touching cart1_chassis | cart1 at 0.094 m, moving +0.57 m/s; touching ball1_sphere
1.25 s: pendulum1 at -15.1°, turning -102°/s; touching nothing | ball1 at (1.17, 0.00, 0.05) m, moving 0.17 m/s (vx +0.11, vy +0.00, vz +0.13); touching nothing | cart1 at 0.244 m, moving +0.58 m/s; touching nothing
1.50 s: pendulum1 at -26.7°, turning +15°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.383 m, moving +0.53 m/s; touching nothing
1.75 s: pendulum1 at -9.7°, turning +105°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.445 m, moving -0.05 m/s; touching nothing
2.00 s: pendulum1 at 15.6°, turning +77°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.434 m, moving -0.04 m/s; touching nothing
2.25 s: pendulum1 at 22.0°, turning -28°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.423 m, moving -0.04 m/s; touching nothing
2.50 s: pendulum1 at 5.0°, turning -93°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.414 m, moving -0.04 m/s; touching nothing
2.75 s: pendulum1 at -15.5°, turning -54°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.405 m, moving -0.03 m/s; touching nothing
3.00 s: pendulum1 at -17.6°, turning +37°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.397 m, moving -0.03 m/s; touching nothing
3.25 s: pendulum1 at -1.2°, turning +80°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.390 m, moving -0.03 m/s; touching nothing
3.50 s: pendulum1 at 14.8°, turning +35°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.384 m, moving -0.02 m/s; touching nothing
3.75 s: pendulum1 at 13.6°, turning -42°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.378 m, moving -0.02 m/s; touching nothing
4.00 s: pendulum1 at -1.7°, turning -67°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.373 m, moving -0.02 m/s; touching nothing
4.25 s: pendulum1 at -13.6°, turning -19°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.368 m, moving -0.02 m/s; touching nothing
4.50 s: pendulum1 at -10.0°, turning +44°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.364 m, moving -0.02 m/s; touching nothing
4.75 s: pendulum1 at 3.7°, turning +54°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.360 m, moving -0.01 m/s; touching nothing
5.00 s: pendulum1 at 12.1°, turning +7°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.356 m, moving -0.01 m/s; touching nothing
5.25 s: pendulum1 at 6.9°, turning -43°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.353 m, moving -0.01 m/s; touching nothing
5.50 s: pendulum1 at -5.0°, turning -42°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.350 m, moving -0.01 m/s; touching nothing
5.75 s: pendulum1 at -10.4°, turning +3°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.348 m, still; touching nothing
6.00 s: pendulum1 at -4.3°, turning +40°/s; touching nothing | ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing

At the end (6.00 s):
- pendulum1 at -4.3°, turning +40°/s; touching nothing
- ball1 at (1.19, 0.00, 0.05) m, at rest; touching floor
- cart1 at 0.345 m, still; touching nothing
</history>
