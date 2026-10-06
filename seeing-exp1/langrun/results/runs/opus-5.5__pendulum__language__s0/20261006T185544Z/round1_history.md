MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 38.0°, still
- ball: free body; its geoms: ball; starts at (0.09, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  pendulum_rod starts touching pendulum_stand_arm
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 38.0°
 0.37 s  pendulum_bob first touches ball
 0.37 s  ball starts moving
 0.41 s  pendulum_bob leaves ball
 0.69 s  pendulum is at its smallest, -16.0°
 1.35 s  ball leaves floor
 1.35 s  ball first touches cup_near_wall
 1.46 s  ball leaves cup_near_wall
 1.50 s  ball first touches cup_base
 1.88 s  ball first touches cup_far_wall
 1.95 s  ball leaves cup_far_wall
 5.44 s  ball comes to rest at (1.00, 0.00, 0.05) m
 5.81 s  ball touches cup_near_wall again
 5.90 s  ball leaves cup_near_wall

State every 0.25 s:
0.00 s: pendulum at 38.0°, still; touching pendulum_stand_arm | ball at (0.09, 0.00, 0.05) m, at rest; touching floor
0.25 s: pendulum at 17.8°, turning -145°/s; touching pendulum_stand_arm | ball at (0.09, 0.00, 0.05) m, at rest; touching floor
0.50 s: pendulum at -10.5°, turning -54°/s; touching pendulum_stand_arm | ball at (0.21, 0.00, 0.05) m, moving 0.83 m/s (vx +0.83, vy -0.00, vz +0.00); touching floor
0.75 s: pendulum at -15.5°, turning +18°/s; touching pendulum_stand_arm | ball at (0.41, 0.00, 0.05) m, moving 0.82 m/s (vx +0.82, vy -0.00, vz -0.00); touching floor
1.00 s: pendulum at -3.3°, turning +69°/s; touching pendulum_stand_arm | ball at (0.62, 0.00, 0.05) m, moving 0.81 m/s (vx +0.81, vy -0.00, vz -0.00); touching floor
1.25 s: pendulum at 12.3°, turning +43°/s; touching pendulum_stand_arm | ball at (0.82, 0.00, 0.05) m, moving 0.80 m/s (vx +0.80, vy -0.00, vz -0.00); touching floor
1.50 s: pendulum at 14.0°, turning -30°/s; touching pendulum_stand_arm | ball at (0.98, 0.00, 0.05) m, moving 0.56 m/s (vx +0.54, vy +0.00, vz -0.16); touching cup_base
1.75 s: pendulum at 0.3°, turning -68°/s; touching pendulum_stand_arm | ball at (1.11, 0.00, 0.05) m, moving 0.54 m/s (vx +0.54, vy +0.00, vz +0.00); touching cup_base
2.00 s: pendulum at -13.5°, turning -31°/s; touching pendulum_stand_arm | ball at (1.18, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base
2.25 s: pendulum at -12.1°, turning +40°/s; touching pendulum_stand_arm | ball at (1.17, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base
2.50 s: pendulum at 2.6°, turning +65°/s; touching pendulum_stand_arm | ball at (1.15, 0.00, 0.05) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base
2.75 s: pendulum at 14.2°, turning +18°/s; touching pendulum_stand_arm | ball at (1.14, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
3.00 s: pendulum at 9.8°, turning -48°/s; touching pendulum_stand_arm | ball at (1.12, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
3.25 s: pendulum at -5.3°, turning -60°/s; touching pendulum_stand_arm | ball at (1.11, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
3.50 s: pendulum at -14.3°, turning -5°/s; touching pendulum_stand_arm | ball at (1.10, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
3.75 s: pendulum at -7.3°, turning +54°/s; touching pendulum_stand_arm | ball at (1.08, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
4.00 s: pendulum at 7.6°, turning +52°/s; touching pendulum_stand_arm | ball at (1.07, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
4.25 s: pendulum at 13.8°, turning -7°/s; touching pendulum_stand_arm | ball at (1.06, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
4.50 s: pendulum at 4.6°, turning -58°/s; touching pendulum_stand_arm | ball at (1.04, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
4.75 s: pendulum at -9.5°, turning -43°/s; touching pendulum_stand_arm | ball at (1.03, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
5.00 s: pendulum at -12.8°, turning +19°/s; touching pendulum_stand_arm | ball at (1.02, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
5.25 s: pendulum at -1.9°, turning +59°/s; touching pendulum_stand_arm | ball at (1.01, 0.00, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base
5.50 s: pendulum at 10.9°, turning +33°/s; touching pendulum_stand_arm | ball at (0.99, 0.00, 0.05) m, at rest; touching cup_base
5.75 s: pendulum at 11.4°, turning -29°/s; touching pendulum_stand_arm | ball at (0.98, 0.00, 0.05) m, at rest; touching cup_base
6.00 s: pendulum at -0.7°, turning -58°/s; touching pendulum_stand_arm | ball at (0.98, 0.00, 0.05) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at -0.7°, turning -58°/s; touching pendulum_stand_arm
- ball at (0.98, 0.00, 0.05) m, at rest; touching cup_base
</history>
