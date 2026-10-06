MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -45° to 45° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 35.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 35.0°
 0.40 s  ball leaves floor
 0.40 s  ball first touches pendulum
 0.40 s  ball starts moving
 0.43 s  ball leaves pendulum
 0.46 s  ball touches floor again
 0.79 s  pendulum is at its smallest, -24.0°
 1.30 s  ball leaves floor
 1.30 s  ball first touches entry ramp
 1.38 s  ball first touches cup_near_wall
 1.38 s  ball leaves cup_near_wall
 1.41 s  ball leaves entry ramp
 1.42 s  ball first touches cup_base
 1.77 s  ball leaves cup_base
 1.77 s  ball first touches cup_far_wall
 1.80 s  ball leaves cup_far_wall
 1.81 s  ball touches cup_base again
 1.87 s  ball comes to rest at (1.11, 0.00, 0.03) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 35.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 19.2°, turning -116°/s; touching nothing
0.50 s: ball at (0.11, 0.00, 0.03) m, moving 0.86 m/s (vx +0.86, vy -0.00, vz -0.00); touching floor | pendulum at -9.9°, turning -88°/s; touching nothing
0.75 s: ball at (0.32, 0.00, 0.03) m, moving 0.85 m/s (vx +0.85, vy -0.00, vz -0.00); touching floor | pendulum at -23.8°, turning -14°/s; touching nothing
1.00 s: ball at (0.53, 0.00, 0.03) m, moving 0.84 m/s (vx +0.84, vy -0.00, vz -0.00); touching floor | pendulum at -15.8°, turning +72°/s; touching nothing
1.25 s: ball at (0.74, 0.00, 0.03) m, moving 0.83 m/s (vx +0.83, vy -0.00, vz -0.00); touching floor | pendulum at 6.8°, turning +92°/s; touching nothing
1.50 s: ball at (0.94, 0.00, 0.03) m, moving 0.75 m/s (vx +0.75, vy -0.00, vz -0.01); touching nothing | pendulum at 22.8°, turning +26°/s; touching nothing
1.75 s: ball at (1.10, 0.00, 0.03) m, moving 0.58 m/s (vx +0.58, vy -0.00, vz -0.00); touching cup_base | pendulum at 17.8°, turning -62°/s; touching nothing
2.00 s: ball at (1.11, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -3.6°, turning -94°/s; touching nothing
2.25 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -21.5°, turning -38°/s; touching nothing
2.50 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -19.5°, turning +52°/s; touching nothing
2.75 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 0.4°, turning +94°/s; touching nothing
3.00 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 19.9°, turning +49°/s; touching nothing
3.25 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 20.9°, turning -41°/s; touching nothing
3.50 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 2.6°, turning -92°/s; touching nothing
3.75 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -17.9°, turning -58°/s; touching nothing
4.00 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -21.8°, turning +29°/s; touching nothing
4.25 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -5.6°, turning +89°/s; touching nothing
4.50 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 15.7°, turning +66°/s; touching nothing
4.75 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 22.3°, turning -17°/s; touching nothing
5.00 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 8.4°, turning -85°/s; touching nothing
5.25 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -13.3°, turning -73°/s; touching nothing
5.50 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -22.5°, turning +5°/s; touching nothing
5.75 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -10.9°, turning +79°/s; touching nothing
6.00 s: ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 10.6°, turning +79°/s; touching nothing

At the end (6.00 s):
- ball at (1.10, 0.00, 0.03) m, at rest; touching cup_base
- pendulum at 10.6°, turning +79°/s; touching nothing
</history>
