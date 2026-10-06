Your expectations, checked against the run (2 of 2 hold):

- holds: pendulum touches ball (first touch at 0.36 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range 0° to 30° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 30.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum starts at its upper stop (30°)
 0.00 s  pendulum is at its largest at the start, 30.0°
 0.36 s  pendulum reaches its lower stop (0°) moving -129°/s
 0.36 s  ball leaves floor
 0.36 s  ball first touches pendulum
 0.36 s  ball starts moving
 0.38 s  ball leaves pendulum
 0.38 s  pendulum is at its smallest, -0.7°
 0.39 s  ball touches floor again
 0.40 s  pendulum reaches its lower stop (0°) again moving +13°/s
 1.11 s  pendulum reaches its lower stop (0°) again moving -13°/s
 2.29 s  ball leaves floor
 2.29 s  ball first touches cup_near_wall
 2.32 s  ball first touches cup_base
 2.33 s  ball leaves cup_near_wall
 2.54 s  ball comes to rest at (0.93, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.04) m, at rest; touching floor | pendulum at 30.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.04) m, at rest; touching floor | pendulum at 14.0°, turning -114°/s; touching nothing
0.50 s: ball at (0.07, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz +0.00); touching floor | pendulum at 0.8°, turning +13°/s; touching nothing
0.75 s: ball at (0.18, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.00); touching floor | pendulum at 2.9°, turning +2°/s; touching nothing
1.00 s: ball at (0.29, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.00); touching floor | pendulum at 1.8°, turning -10°/s; touching nothing
1.25 s: ball at (0.41, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.00); touching floor | pendulum at 0.0°, turning +2°/s; touching nothing
1.50 s: ball at (0.52, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.00); touching floor | pendulum at 0.4°, still; touching nothing
1.75 s: ball at (0.63, 0.00, 0.04) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz -0.00); touching floor | pendulum at 0.3°, turning -1°/s; touching nothing
2.00 s: ball at (0.74, 0.00, 0.04) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz -0.00); touching floor | pendulum at -0.0°, still; touching nothing
2.25 s: ball at (0.85, 0.00, 0.04) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz -0.00); touching floor | pendulum at 0.0°, still; touching nothing
2.50 s: ball at (0.92, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz +0.01); touching cup_base | pendulum at 0.0°, still; touching nothing
2.75 s: ball at (0.93, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -0.0°, still; touching nothing
3.00 s: ball at (0.93, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- ball at (0.93, 0.00, 0.04) m, at rest; touching cup_base
- pendulum at 0.0°, still; touching nothing
</history>
