Your expectations, checked against the run (3 of 3 hold):

- holds: pendulum touches ball (first touch at 0.36 s)
- holds: ball touches cup (first touch at 1.37 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 25.8°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 25.8°
 0.36 s  ball leaves floor
 0.36 s  pendulum_bob first touches ball
 0.36 s  ball starts moving
 0.40 s  ball touches floor again
 0.41 s  pendulum_bob leaves ball
 1.37 s  ball leaves floor
 1.37 s  ball first touches cup_lip
 1.39 s  ball leaves cup_lip
 1.43 s  ball touches floor again
 1.52 s  ball first touches cup_back
 1.52 s  ball leaves floor
 1.57 s  ball touches floor again
 1.58 s  ball leaves cup_back
 2.14 s  pendulum is at its smallest, -21.9°
 2.38 s  ball touches cup_lip again
 2.39 s  ball leaves floor
 2.42 s  ball touches floor 1 more times between 2.42 s and 6.00 s, still touching at the end
 2.44 s  ball leaves cup_lip
 3.85 s  ball touches cup_back again
 3.85 s  ball comes to rest at (1.04, 0.00, 0.02) m
 3.91 s  ball leaves cup_back

State every 0.25 s:
0.00 s: pendulum at 25.8°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 11.7°, turning -101°/s; touching nothing | ball at (0.00, 0.00, 0.02) m, at rest; touching floor
0.50 s: pendulum at -13.1°, turning -77°/s; touching nothing | ball at (0.13, 0.00, 0.02) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz +0.00); touching floor
0.75 s: pendulum at -21.6°, turning +16°/s; touching nothing | ball at (0.36, 0.00, 0.02) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz +0.00); touching floor
1.00 s: pendulum at -6.5°, turning +92°/s; touching nothing | ball at (0.58, 0.00, 0.02) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz +0.00); touching floor
1.25 s: pendulum at 15.8°, turning +67°/s; touching nothing | ball at (0.81, 0.00, 0.02) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz -0.00); touching floor
1.50 s: pendulum at 20.7°, turning -31°/s; touching nothing | ball at (1.02, 0.00, 0.02) m, moving 0.79 m/s (vx +0.79, vy -0.00, vz +0.02); touching floor
1.75 s: pendulum at 3.0°, turning -96°/s; touching nothing | ball at (1.02, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
2.00 s: pendulum at -18.0°, turning -55°/s; touching nothing | ball at (0.99, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
2.25 s: pendulum at -19.3°, turning +45°/s; touching nothing | ball at (0.97, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
2.50 s: pendulum at 0.5°, turning +97°/s; touching nothing | ball at (0.96, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
2.75 s: pendulum at 19.7°, turning +42°/s; touching nothing | ball at (0.97, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
3.00 s: pendulum at 17.4°, turning -58°/s; touching nothing | ball at (0.99, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
3.25 s: pendulum at -4.0°, turning -95°/s; touching nothing | ball at (1.00, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
3.50 s: pendulum at -21.0°, turning -28°/s; touching nothing | ball at (1.01, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
3.75 s: pendulum at -15.1°, turning +70°/s; touching nothing | ball at (1.03, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
4.00 s: pendulum at 7.4°, turning +91°/s; touching nothing | ball at (1.03, 0.00, 0.02) m, at rest; touching floor
4.25 s: pendulum at 21.7°, turning +13°/s; touching nothing | ball at (1.03, 0.00, 0.02) m, at rest; touching floor
4.50 s: pendulum at 12.4°, turning -79°/s; touching nothing | ball at (1.03, 0.00, 0.02) m, at rest; touching floor
4.75 s: pendulum at -10.6°, turning -85°/s; touching nothing | ball at (1.03, 0.00, 0.02) m, at rest; touching floor
5.00 s: pendulum at -21.9°, turning +3°/s; touching nothing | ball at (1.02, 0.00, 0.02) m, at rest; touching floor
5.25 s: pendulum at -9.3°, turning +87°/s; touching nothing | ball at (1.02, 0.00, 0.02) m, at rest; touching floor
5.50 s: pendulum at 13.5°, turning +76°/s; touching nothing | ball at (1.02, 0.00, 0.02) m, at rest; touching floor
5.75 s: pendulum at 21.5°, turning -18°/s; touching nothing | ball at (1.01, 0.00, 0.02) m, at rest; touching floor
6.00 s: pendulum at 6.0°, turning -93°/s; touching nothing | ball at (1.01, 0.00, 0.02) m, at rest; touching floor

At the end (6.00 s):
- pendulum at 6.0°, turning -93°/s; touching nothing
- ball at (1.01, 0.00, 0.02) m, at rest; touching floor
</history>
