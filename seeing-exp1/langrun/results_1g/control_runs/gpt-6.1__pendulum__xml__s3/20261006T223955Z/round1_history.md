MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 37.2°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 37.2°
 0.41 s  ball leaves floor
 0.41 s  pendulum_bob first touches ball
 0.41 s  ball starts moving
 0.43 s  pendulum_bob leaves ball
 0.46 s  ball touches floor again
 0.46 s  ball leaves floor
 0.51 s  ball touches floor again
 0.79 s  pendulum is at its smallest, -26.7°
 1.25 s  ball leaves floor
 1.25 s  ball first touches cup_base
 1.25 s  ball leaves cup_base
 1.31 s  ball touches cup_base again
 1.69 s  ball comes to rest at (0.97, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 37.2°, still; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 20.6°, turning -122°/s; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -11.0°, turning -98°/s; touching nothing | ball at (0.11, 0.00, 0.04) m, moving 1.15 m/s (vx +1.13, vy +0.00, vz -0.16); touching nothing
0.75 s: pendulum at -26.4°, turning -16°/s; touching nothing | ball at (0.34, 0.00, 0.04) m, moving 0.89 m/s (vx +0.89, vy +0.00, vz +0.00); touching floor
1.00 s: pendulum at -17.6°, turning +80°/s; touching nothing | ball at (0.56, 0.00, 0.04) m, moving 0.88 m/s (vx +0.88, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 7.3°, turning +102°/s; touching nothing | ball at (0.78, 0.00, 0.04) m, moving 0.80 m/s (vx +0.75, vy +0.00, vz +0.29); touching nothing
1.50 s: pendulum at 25.3°, turning +30°/s; touching nothing | ball at (0.93, 0.00, 0.04) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz +0.00); touching nothing
1.75 s: pendulum at 20.1°, turning -68°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: pendulum at -3.5°, turning -104°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: pendulum at -23.7°, turning -44°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: pendulum at -22.1°, turning +55°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: pendulum at -0.2°, turning +104°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 21.7°, turning +57°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at 23.6°, turning -42°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at 3.9°, turning -102°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at -19.3°, turning -68°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at -24.6°, turning +28°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at -7.4°, turning +98°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at 16.5°, turning +77°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at 25.1°, turning -14°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at 10.6°, turning -92°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at -13.5°, turning -85°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at -25.0°, still; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at -13.6°, turning +84°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at 10.4°, turning +91°/s; touching nothing | ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 10.4°, turning +91°/s; touching nothing
- ball at (0.97, 0.00, 0.04) m, at rest; touching cup_base
</history>
