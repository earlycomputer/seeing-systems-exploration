MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.05) m, at rest
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 35.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 35.0°
 0.40 s  ball leaves floor
 0.40 s  ball first touches pendulum_bob
 0.40 s  ball starts moving
 0.43 s  ball leaves pendulum_bob
 0.46 s  ball touches floor again
 0.78 s  pendulum is at its smallest, -23.1°
 1.33 s  ball leaves floor
 1.33 s  ball first touches cup_near_wall
 1.34 s  ball leaves cup_near_wall
 1.40 s  ball first touches cup_base
 1.75 s  ball comes to rest at (0.97, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.05) m, at rest; touching floor | pendulum at 35.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.05) m, at rest; touching floor | pendulum at 19.2°, turning -115°/s; touching nothing
0.50 s: ball at (0.10, 0.00, 0.05) m, moving 0.84 m/s (vx +0.84, vy -0.00, vz -0.00); touching floor | pendulum at -9.5°, turning -85°/s; touching nothing
0.75 s: ball at (0.31, 0.00, 0.05) m, moving 0.84 m/s (vx +0.84, vy -0.00, vz -0.00); touching floor | pendulum at -22.9°, turning -13°/s; touching nothing
1.00 s: ball at (0.52, 0.00, 0.05) m, moving 0.84 m/s (vx +0.84, vy -0.00, vz -0.00); touching floor | pendulum at -15.0°, turning +70°/s; touching nothing
1.25 s: ball at (0.73, 0.00, 0.05) m, moving 0.83 m/s (vx +0.83, vy -0.00, vz -0.00); touching floor | pendulum at 6.6°, turning +88°/s; touching nothing
1.50 s: ball at (0.90, 0.00, 0.05) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz +0.01); touching cup_base | pendulum at 21.8°, turning +24°/s; touching nothing
1.75 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 16.7°, turning -61°/s; touching nothing
2.00 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -3.8°, turning -89°/s; touching nothing
2.25 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -20.5°, turning -34°/s; touching nothing
2.50 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -18.1°, turning +51°/s; touching nothing
2.75 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 1.0°, turning +88°/s; touching nothing
3.00 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 18.9°, turning +43°/s; touching nothing
3.25 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 19.1°, turning -41°/s; touching nothing
3.50 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 1.7°, turning -86°/s; touching nothing
3.75 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -17.0°, turning -51°/s; touching nothing
4.00 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -19.8°, turning +30°/s; touching nothing
4.25 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -4.2°, turning +83°/s; touching nothing
4.50 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 15.1°, turning +58°/s; touching nothing
4.75 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 20.1°, turning -20°/s; touching nothing
5.00 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 6.5°, turning -79°/s; touching nothing
5.25 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -12.9°, turning -64°/s; touching nothing
5.50 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -20.1°, turning +10°/s; touching nothing
5.75 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at -8.6°, turning +74°/s; touching nothing
6.00 s: ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base | pendulum at 10.7°, turning +68°/s; touching nothing

At the end (6.00 s):
- ball at (0.97, 0.00, 0.05) m, at rest; touching cup_base
- pendulum at 10.7°, turning +68°/s; touching nothing
</history>
