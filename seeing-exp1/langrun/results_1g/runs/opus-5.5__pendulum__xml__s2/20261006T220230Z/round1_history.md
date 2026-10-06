Your expectations, checked against the run (1 of 3 hold):

- holds: pendulum touches ball (first touch at 0.37 s)
- DOES NOT HOLD: ball touches cup (they never touch)
- DOES NOT HOLD: ball comes to rest in cup (ball is still moving at the end (15.03 m/s), outside cup)

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
 0.37 s  ball leaves floor
 0.37 s  pendulum_bob first touches ball
 0.37 s  pendulum_bob leaves ball
 0.37 s  ball starts moving
 0.42 s  ball passes 0.13 m from cup (cup_left) without touching it: nearest points (0.92, 0.02, 0.18) m and (0.92, 0.09, 0.08) m
 0.76 s  ball is at the top of its flight, at (7.12, 0.00, 0.77) m
 0.82 s  pendulum is at its largest, 107.2°
 1.15 s  ball touches floor again
 1.19 s  ball leaves floor
 1.30 s  ball is at the top of its flight, at (16.49, 0.00, 0.09) m
 1.42 s  ball touches floor again
 1.47 s  ball leaves floor
 1.53 s  ball touches floor again
 3.52 s  pendulum is at its smallest, -107.2°
 6.00 s  ball is still moving at the end, 15.03 m/s

State every 0.25 s:
0.00 s: pendulum at 45.0°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 21.5°, turning -170°/s; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at 49.9°, turning +351°/s; touching nothing | ball at (2.35, 0.00, 0.44) m, moving 18.52 m/s (vx +18.34, vy -0.00, vz +2.54); touching nothing
0.75 s: pendulum at 104.4°, turning +80°/s; touching nothing | ball at (6.93, 0.00, 0.77) m, moving 18.34 m/s (vx +18.34, vy -0.00, vz +0.09); touching nothing
1.00 s: pendulum at 89.7°, turning -197°/s; touching nothing | ball at (11.52, 0.00, 0.49) m, moving 18.49 m/s (vx +18.34, vy -0.00, vz -2.36); touching nothing
1.25 s: pendulum at 8.7°, turning -409°/s; touching nothing | ball at (15.72, 0.00, 0.08) m, moving 14.31 m/s (vx +14.30, vy -0.00, vz +0.51); touching nothing
1.50 s: pendulum at -80.3°, turning -247°/s; touching nothing | ball at (19.34, 0.00, 0.03) m, moving 15.01 m/s (vx +15.01, vy +0.00, vz -0.02); touching nothing
1.75 s: pendulum at -106.7°, turning +31°/s; touching nothing | ball at (23.13, 0.00, 0.03) m, moving 15.21 m/s (vx +15.21, vy +0.00, vz +0.00); touching floor
2.00 s: pendulum at -63.8°, turning +309°/s; touching nothing | ball at (26.93, 0.00, 0.03) m, moving 15.21 m/s (vx +15.21, vy +0.00, vz -0.00); touching floor
2.25 s: pendulum at 32.3°, turning +387°/s; touching nothing | ball at (30.73, 0.00, 0.03) m, moving 15.21 m/s (vx +15.21, vy +0.00, vz -0.01); touching floor
2.50 s: pendulum at 99.4°, turning +133°/s; touching nothing | ball at (34.53, 0.00, 0.03) m, moving 15.19 m/s (vx +15.19, vy +0.00, vz +0.01); touching floor
2.75 s: pendulum at 97.8°, turning -143°/s; touching nothing | ball at (38.33, 0.00, 0.03) m, moving 15.18 m/s (vx +15.18, vy +0.00, vz +0.00); touching floor
3.00 s: pendulum at 27.8°, turning -392°/s; touching nothing | ball at (42.12, 0.00, 0.03) m, moving 15.17 m/s (vx +15.17, vy +0.00, vz -0.02); touching nothing
3.25 s: pendulum at -67.3°, turning -299°/s; touching nothing | ball at (45.92, 0.00, 0.03) m, moving 15.16 m/s (vx +15.16, vy +0.00, vz +0.00); touching floor
3.50 s: pendulum at -107.0°, turning -21°/s; touching nothing | ball at (49.70, 0.00, 0.03) m, moving 15.14 m/s (vx +15.14, vy +0.00, vz +0.01); touching nothing
3.75 s: pendulum at -77.4°, turning +258°/s; touching nothing | ball at (53.49, 0.00, 0.03) m, moving 15.13 m/s (vx +15.13, vy +0.00, vz -0.00); touching nothing
4.00 s: pendulum at 13.4°, turning +407°/s; touching nothing | ball at (57.27, 0.00, 0.03) m, moving 15.12 m/s (vx +15.12, vy +0.00, vz -0.02); touching nothing
4.25 s: pendulum at 91.9°, turning +187°/s; touching nothing | ball at (61.05, 0.00, 0.03) m, moving 15.11 m/s (vx +15.11, vy +0.00, vz -0.00); touching floor
4.50 s: pendulum at 103.4°, turning -90°/s; touching nothing | ball at (64.83, 0.00, 0.03) m, moving 15.10 m/s (vx +15.10, vy +0.00, vz +0.01); touching floor
4.75 s: pendulum at 45.8°, turning -359°/s; touching nothing | ball at (68.60, 0.00, 0.03) m, moving 15.09 m/s (vx +15.09, vy +0.00, vz +0.02); touching floor
5.00 s: pendulum at -52.0°, turning -346°/s; touching nothing | ball at (72.37, 0.00, 0.03) m, moving 15.08 m/s (vx +15.08, vy +0.00, vz +0.00); touching nothing
5.25 s: pendulum at -104.8°, turning -73°/s; touching nothing | ball at (76.14, 0.00, 0.03) m, moving 15.06 m/s (vx +15.06, vy +0.00, vz -0.02); touching floor
5.50 s: pendulum at -88.4°, turning +204°/s; touching nothing | ball at (79.90, 0.00, 0.03) m, moving 15.05 m/s (vx +15.05, vy +0.00, vz -0.01); touching floor
5.75 s: pendulum at -6.2°, turning +410°/s; touching nothing | ball at (83.66, 0.00, 0.03) m, moving 15.04 m/s (vx +15.04, vy +0.00, vz +0.00); touching floor
6.00 s: pendulum at 81.8°, turning +241°/s; touching nothing | ball at (87.42, 0.00, 0.03) m, moving 15.03 m/s (vx +15.03, vy +0.00, vz +0.01); touching floor

At the end (6.00 s):
- pendulum at 81.8°, turning +241°/s; touching nothing
- ball at (87.42, 0.00, 0.03) m, moving 15.03 m/s (vx +15.03, vy +0.00, vz +0.01); touching floor
</history>
