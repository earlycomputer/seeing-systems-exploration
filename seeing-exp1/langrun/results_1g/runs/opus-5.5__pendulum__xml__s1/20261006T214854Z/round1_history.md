Your expectations, checked against the run (4 of 4 hold):

- holds: pendulum touches ball (first touch at 0.38 s)
- holds: ball touches ramp (first touch at 0.70 s)
- holds: ball touches cup (first touch at 0.90 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 60.0°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 60.0°
 0.38 s  pendulum_bob first touches ball
 0.38 s  ball starts moving
 0.42 s  pendulum_bob leaves ball
 0.70 s  ball leaves floor
 0.70 s  ball first touches ramp
 0.72 s  pendulum is at its smallest, -31.7°
 0.72 s  pendulum passes 0.36 m from ramp without touching it: nearest points (0.23, 0.00, 0.10) m and (0.58, 0.00, 0.00) m
 0.90 s  ball leaves ramp
 0.90 s  ball first touches cup_near
 0.90 s  ball leaves cup_near
 0.93 s  ball is at the top of its flight, at (0.91, 0.00, 0.10) m
 1.05 s  ball first touches cup_far
 1.06 s  ball touches floor again
 1.13 s  ball leaves cup_far
 2.58 s  ball touches cup_near again
 2.58 s  ball comes to rest at (0.93, 0.00, 0.03) m
 2.66 s  ball leaves cup_near

State every 0.25 s:
0.00 s: pendulum at 60.0°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 30.7°, turning -217°/s; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -18.2°, turning -114°/s; touching nothing | ball at (0.21, 0.00, 0.03) m, moving 1.81 m/s (vx +1.81, vy +0.00, vz -0.01); touching nothing
0.75 s: pendulum at -31.4°, turning +18°/s; touching nothing | ball at (0.65, 0.00, 0.05) m, moving 1.61 m/s (vx +1.55, vy +0.00, vz +0.43); touching ramp
1.00 s: pendulum at -10.7°, turning +131°/s; touching nothing | ball at (1.00, 0.00, 0.08) m, moving 1.47 m/s (vx +1.32, vy +0.00, vz -0.65); touching nothing
1.25 s: pendulum at 21.8°, turning +102°/s; touching nothing | ball at (1.05, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor
1.50 s: pendulum at 30.5°, turning -37°/s; touching nothing | ball at (1.03, 0.00, 0.03) m, moving 0.11 m/s (vx -0.11, vy -0.00, vz +0.00); touching floor
1.75 s: pendulum at 6.3°, turning -137°/s; touching nothing | ball at (1.00, 0.00, 0.03) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching floor
2.00 s: pendulum at -24.9°, turning -87°/s; touching nothing | ball at (0.98, 0.00, 0.03) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz +0.00); touching floor
2.25 s: pendulum at -28.9°, turning +56°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz +0.00); touching floor
2.50 s: pendulum at -1.7°, turning +140°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz +0.00); touching floor
2.75 s: pendulum at 27.4°, turning +70°/s; touching nothing | ball at (0.93, 0.00, 0.03) m, at rest; touching floor
3.00 s: pendulum at 26.8°, turning -74°/s; touching nothing | ball at (0.93, 0.00, 0.03) m, at rest; touching floor
3.25 s: pendulum at -2.9°, turning -139°/s; touching nothing | ball at (0.93, 0.00, 0.03) m, at rest; touching floor
3.50 s: pendulum at -29.4°, turning -52°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
3.75 s: pendulum at -24.1°, turning +90°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
4.00 s: pendulum at 7.5°, turning +136°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
4.25 s: pendulum at 30.8°, turning +33°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
4.50 s: pendulum at 20.8°, turning -104°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
4.75 s: pendulum at -11.9°, turning -130°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
5.00 s: pendulum at -31.6°, turning -13°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
5.25 s: pendulum at -17.2°, turning +117°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
5.50 s: pendulum at 16.0°, turning +121°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
5.75 s: pendulum at 31.7°, turning -6°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor
6.00 s: pendulum at 13.1°, turning -127°/s; touching nothing | ball at (0.94, 0.00, 0.03) m, at rest; touching floor

At the end (6.00 s):
- pendulum at 13.1°, turning -127°/s; touching nothing
- ball at (0.94, 0.00, 0.03) m, at rest; touching floor
</history>
