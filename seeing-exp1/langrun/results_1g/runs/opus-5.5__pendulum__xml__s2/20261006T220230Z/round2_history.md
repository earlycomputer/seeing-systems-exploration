Your expectations, checked against the run (3 of 3 hold):

- holds: pendulum touches ball (first touch at 0.37 s)
- holds: ball touches cup (first touch at 0.91 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 45.0°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 45.0°
 0.37 s  pendulum_bob first touches ball
 0.37 s  ball starts moving
 0.38 s  pendulum_bob leaves ball
 0.91 s  ball leaves floor
 0.91 s  ball first touches cup_front
 0.93 s  ball leaves cup_front
 0.99 s  ball is at the top of its flight, at (0.95, 0.00, 0.06) m
 1.05 s  ball first touches cup_base
 1.11 s  ball first touches cup_back
 1.12 s  ball leaves cup_base
 1.17 s  ball leaves cup_back
 1.18 s  ball touches cup_base again
 2.16 s  ball touches cup_front again
 2.17 s  ball comes to rest at (0.93, 0.00, 0.04) m
 2.21 s  ball leaves cup_front
 5.02 s  pendulum is at its smallest, -30.8°

State every 0.25 s:
0.00 s: pendulum at 45.0°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 21.5°, turning -170°/s; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -17.5°, turning -112°/s; touching nothing | ball at (0.22, 0.00, 0.03) m, moving 1.61 m/s (vx +1.61, vy +0.00, vz +0.00); touching floor
0.75 s: pendulum at -30.5°, turning +16°/s; touching nothing | ball at (0.63, 0.00, 0.03) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -10.6°, turning +127°/s; touching nothing | ball at (0.96, 0.00, 0.06) m, moving 0.89 m/s (vx +0.87, vy +0.00, vz -0.15); touching nothing
1.25 s: pendulum at 20.9°, turning +99°/s; touching nothing | ball at (1.05, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.02); touching cup_base
1.50 s: pendulum at 29.7°, turning -35°/s; touching nothing | ball at (1.02, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
1.75 s: pendulum at 6.3°, turning -133°/s; touching nothing | ball at (0.98, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.00 s: pendulum at -24.0°, turning -85°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.25 s: pendulum at -28.2°, turning +53°/s; touching nothing | ball at (0.93, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: pendulum at -1.9°, turning +135°/s; touching nothing | ball at (0.94, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: pendulum at 26.5°, turning +69°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 26.1°, turning -70°/s; touching nothing | ball at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at -2.6°, turning -135°/s; touching nothing | ball at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at -28.5°, turning -52°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at -23.5°, turning +86°/s; touching nothing | ball at (0.98, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at 7.0°, turning +132°/s; touching nothing | ball at (0.99, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at 29.8°, turning +33°/s; touching nothing | ball at (1.00, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at 20.5°, turning -100°/s; touching nothing | ball at (1.00, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at -11.2°, turning -126°/s; touching nothing | ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at -30.6°, turning -14°/s; touching nothing | ball at (1.02, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at -16.9°, turning +112°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at 15.2°, turning +118°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at 30.7°, turning -5°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at 13.0°, turning -122°/s; touching nothing | ball at (1.05, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 13.0°, turning -122°/s; touching nothing
- ball at (1.05, 0.00, 0.04) m, at rest; touching cup_base
</history>
