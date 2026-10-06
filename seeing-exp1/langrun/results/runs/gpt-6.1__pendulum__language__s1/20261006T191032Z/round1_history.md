MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest
- pendulum: hinge joint swing_axis about axis (0.00, 1.00, 0.00), range -70° to 70° as MuJoCo applies it; its geoms: pendulum; starts at 35.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 35.0°
 0.34 s  ball leaves floor
 0.34 s  ball first touches pendulum
 0.34 s  ball starts moving
 0.37 s  ball leaves pendulum
 0.38 s  ball touches floor again
 0.65 s  pendulum is at its smallest, -15.4°
 1.60 s  ball leaves floor
 1.60 s  ball first touches cup_near_wall
 1.60 s  ball first touches cup_base
 1.61 s  ball leaves cup_near_wall
 2.01 s  ball first touches cup_far_wall
 2.01 s  ball leaves cup_base
 2.04 s  ball touches cup_base again
 2.05 s  ball leaves cup_far_wall
 5.19 s  ball touches cup_near_wall again
 5.35 s  ball leaves cup_base
 5.50 s  ball touches floor again
 5.50 s  ball leaves cup_near_wall
 6.00 s  ball is still moving at the end, 0.14 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 35.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 13.2°, turning -153°/s; touching nothing
0.50 s: ball at (0.13, 0.00, 0.03) m, moving 0.73 m/s (vx +0.73, vy +0.00, vz +0.00); touching floor | pendulum at -11.6°, turning -50°/s; touching nothing
0.75 s: ball at (0.31, 0.00, 0.03) m, moving 0.70 m/s (vx +0.70, vy +0.00, vz +0.00); touching floor | pendulum at -13.7°, turning +34°/s; touching nothing
1.00 s: ball at (0.49, 0.00, 0.03) m, moving 0.67 m/s (vx +0.67, vy +0.00, vz -0.02); touching nothing | pendulum at 1.7°, turning +73°/s; touching nothing
1.25 s: ball at (0.65, 0.00, 0.03) m, moving 0.65 m/s (vx +0.65, vy +0.00, vz +0.00); touching floor | pendulum at 14.5°, turning +17°/s; touching nothing
1.50 s: ball at (0.81, 0.00, 0.03) m, moving 0.62 m/s (vx +0.62, vy +0.00, vz -0.02); touching nothing | pendulum at 8.4°, turning -59°/s; touching nothing
1.75 s: ball at (0.95, 0.00, 0.03) m, moving 0.54 m/s (vx +0.54, vy +0.00, vz +0.00); touching cup_base | pendulum at -8.2°, turning -57°/s; touching nothing
2.00 s: ball at (1.08, 0.00, 0.03) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz -0.00); touching cup_base | pendulum at -13.9°, turning +17°/s; touching nothing
2.25 s: ball at (1.07, 0.00, 0.03) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching cup_base | pendulum at -1.6°, turning +68°/s; touching nothing
2.50 s: ball at (1.05, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base | pendulum at 12.4°, turning +30°/s; touching nothing
2.75 s: ball at (1.04, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base | pendulum at 10.1°, turning -45°/s; touching nothing
3.00 s: ball at (1.02, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base | pendulum at -5.0°, turning -61°/s; touching nothing
3.25 s: ball at (1.00, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base | pendulum at -13.3°, turning +2°/s; touching nothing
3.50 s: ball at (0.98, 0.00, 0.03) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base | pendulum at -4.4°, turning +60°/s; touching nothing
3.75 s: ball at (0.97, 0.00, 0.03) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base | pendulum at 9.9°, turning +40°/s; touching nothing
4.00 s: ball at (0.95, 0.00, 0.03) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base | pendulum at 11.1°, turning -31°/s; touching nothing
4.25 s: ball at (0.94, 0.00, 0.03) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base | pendulum at -1.9°, turning -60°/s; touching nothing
4.50 s: ball at (0.92, 0.00, 0.03) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base | pendulum at -12.1°, turning -12°/s; touching nothing
4.75 s: ball at (0.91, 0.00, 0.03) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup_base | pendulum at -6.5°, turning +50°/s; touching nothing
5.00 s: ball at (0.90, 0.00, 0.03) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching cup_base | pendulum at 7.3°, turning +46°/s; touching nothing
5.25 s: ball at (0.88, 0.00, 0.03) m, at rest; touching cup_base, cup_near_wall | pendulum at 11.4°, turning -17°/s; touching nothing
5.50 s: ball at (0.87, 0.00, 0.03) m, moving 0.18 m/s (vx -0.16, vy +0.00, vz -0.08); touching nothing | pendulum at 0.8°, turning -57°/s; touching nothing
5.75 s: ball at (0.83, 0.00, 0.03) m, moving 0.15 m/s (vx -0.15, vy +0.00, vz -0.00); touching floor | pendulum at -10.5°, turning -23°/s; touching nothing
6.00 s: ball at (0.79, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz -0.00); touching floor | pendulum at -8.0°, turning +39°/s; touching nothing

At the end (6.00 s):
- ball at (0.79, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz -0.00); touching floor
- pendulum at -8.0°, turning +39°/s; touching nothing
</history>
