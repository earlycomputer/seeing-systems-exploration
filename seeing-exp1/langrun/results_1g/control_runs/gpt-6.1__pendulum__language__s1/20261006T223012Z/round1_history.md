MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -40° to 40° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 30.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 30.0°
 0.43 s  ball first touches pendulum
 0.43 s  ball starts moving
 0.46 s  ball leaves pendulum
 0.82 s  pendulum is at its smallest, -13.1°
 1.61 s  ball leaves floor
 1.61 s  ball first touches cup_near_wall
 1.61 s  ball leaves cup_near_wall
 1.65 s  ball first touches cup_base
 2.09 s  ball comes to rest at (1.00, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.04) m, at rest; touching floor | pendulum at 30.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.04) m, at rest; touching floor | pendulum at 18.1°, turning -88°/s; touching nothing
0.50 s: ball at (0.06, 0.00, 0.04) m, moving 0.72 m/s (vx +0.72, vy +0.00, vz +0.00); touching floor | pendulum at -4.4°, turning -47°/s; touching nothing
0.75 s: ball at (0.23, 0.00, 0.04) m, moving 0.71 m/s (vx +0.71, vy +0.00, vz -0.00); touching floor | pendulum at -12.6°, turning -14°/s; touching nothing
1.00 s: ball at (0.41, 0.00, 0.04) m, moving 0.71 m/s (vx +0.71, vy +0.00, vz -0.00); touching floor | pendulum at -10.4°, turning +30°/s; touching nothing
1.25 s: ball at (0.59, 0.00, 0.04) m, moving 0.70 m/s (vx +0.70, vy +0.00, vz -0.00); touching floor | pendulum at 0.2°, turning +49°/s; touching nothing
1.50 s: ball at (0.76, 0.00, 0.04) m, moving 0.69 m/s (vx +0.69, vy +0.00, vz -0.00); touching floor | pendulum at 10.4°, turning +27°/s; touching nothing
1.75 s: ball at (0.92, 0.00, 0.04) m, moving 0.47 m/s (vx +0.47, vy +0.00, vz +0.00); touching nothing | pendulum at 12.0°, turning -16°/s; touching nothing
2.00 s: ball at (0.99, 0.00, 0.04) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.00); touching cup_base | pendulum at 3.7°, turning -45°/s; touching nothing
2.25 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -7.4°, turning -37°/s; touching nothing
2.50 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -12.3°, still; touching nothing
2.75 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -7.1°, turning +37°/s; touching nothing
3.00 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 3.8°, turning +43°/s; touching nothing
3.25 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 11.3°, turning +13°/s; touching nothing
3.50 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 9.5°, turning -26°/s; touching nothing
3.75 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 0.0°, turning -44°/s; touching nothing
4.00 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -9.3°, turning -25°/s; touching nothing
4.25 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -10.9°, turning +13°/s; touching nothing
4.50 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -3.6°, turning +41°/s; touching nothing
4.75 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 6.5°, turning +34°/s; touching nothing
5.00 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 11.1°, still; touching nothing
5.25 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 6.6°, turning -33°/s; touching nothing
5.50 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -3.2°, turning -39°/s; touching nothing
5.75 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -10.2°, turning -13°/s; touching nothing
6.00 s: ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -8.7°, turning +23°/s; touching nothing

At the end (6.00 s):
- ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base
- pendulum at -8.7°, turning +23°/s; touching nothing
</history>
