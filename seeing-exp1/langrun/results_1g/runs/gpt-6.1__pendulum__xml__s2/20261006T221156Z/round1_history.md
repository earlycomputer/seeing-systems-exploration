Your expectations, checked against the run (4 of 4 hold):

- holds: pendulum touches ball (first touch at 0.37 s)
- holds: ball touches floor (touching from the start)
- holds: ball touches ramp (first touch at 1.06 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 45.8°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 45.8°
 0.37 s  ball leaves floor
 0.37 s  pendulum_bob first touches ball
 0.37 s  ball starts moving
 0.39 s  pendulum_bob leaves ball
 0.41 s  ball touches floor again
 0.72 s  pendulum passes 0.49 m from ramp without touching it: nearest points (0.18, 0.00, 0.11) m and (0.66, 0.00, 0.00) m
 0.72 s  pendulum is at its smallest, -27.8°
 1.06 s  ball leaves floor
 1.06 s  ball first touches ramp
 1.27 s  ball first touches cup_wall_08
 1.27 s  ball leaves cup_wall_08
 1.49 s  ball leaves ramp
 1.51 s  ball first touches cup_base
 1.63 s  ball comes to rest at (0.94, 0.00, 0.06) m

State every 0.25 s:
0.00 s: pendulum at 45.8°, still; touching nothing | ball at (0.00, 0.00, 0.05) m, at rest; touching floor
0.25 s: pendulum at 22.4°, turning -170°/s; touching nothing | ball at (0.00, 0.00, 0.05) m, at rest; touching floor
0.50 s: pendulum at -15.4°, turning -103°/s; touching nothing | ball at (0.14, 0.00, 0.05) m, moving 0.94 m/s (vx +0.94, vy +0.00, vz +0.00); touching floor
0.75 s: pendulum at -27.6°, turning +13°/s; touching nothing | ball at (0.37, 0.00, 0.05) m, moving 0.91 m/s (vx +0.91, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -10.1°, turning +112°/s; touching nothing | ball at (0.59, 0.00, 0.05) m, moving 0.89 m/s (vx +0.89, vy +0.00, vz -0.01); touching nothing
1.25 s: pendulum at 17.8°, turning +88°/s; touching nothing | ball at (0.78, 0.00, 0.07) m, moving 0.63 m/s (vx +0.62, vy +0.00, vz +0.09); touching ramp
1.50 s: pendulum at 25.8°, turning -29°/s; touching nothing | ball at (0.91, 0.00, 0.07) m, moving 0.67 m/s (vx +0.47, vy -0.00, vz -0.47); touching nothing
1.75 s: pendulum at 6.0°, turning -112°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
2.00 s: pendulum at -19.7°, turning -72°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
2.25 s: pendulum at -23.5°, turning +43°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
2.50 s: pendulum at -2.0°, turning +110°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
2.75 s: pendulum at 21.0°, turning +56°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
3.00 s: pendulum at 20.8°, turning -56°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
3.25 s: pendulum at -1.8°, turning -105°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
3.50 s: pendulum at -21.7°, turning -39°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
3.75 s: pendulum at -17.8°, turning +66°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
4.00 s: pendulum at 5.2°, turning +98°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
4.25 s: pendulum at 21.9°, turning +23°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
4.50 s: pendulum at 14.5°, turning -75°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
4.75 s: pendulum at -8.3°, turning -89°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
5.00 s: pendulum at -21.5°, turning -7°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
5.25 s: pendulum at -11.1°, turning +80°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
5.50 s: pendulum at 11.0°, turning +78°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
5.75 s: pendulum at 20.6°, turning -8°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
6.00 s: pendulum at 7.7°, turning -84°/s; touching nothing | ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 7.7°, turning -84°/s; touching nothing
- ball at (0.94, 0.00, 0.06) m, at rest; touching cup_base
</history>
