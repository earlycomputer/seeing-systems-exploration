MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- wedge: free body; its geoms: wedge, wedge heel, wedge near face, wedge far face; starts at (1.50, 0.00, 0.81) m, at rest
- block: free body; its geoms: block; starts at (1.37, 0.00, 1.37) m, at rest
- ball1: free body; its geoms: ball1; starts at (1.24, -0.06, 0.68) m, at rest
- flap: hinge joint release_hinge about axis (0.00, 1.00, 0.00), range -85° to 6.00001° as MuJoCo applies it; its geoms: flap; starts at 6.0°, still
- ball2: free body; its geoms: ball2; starts at (0.09, 0.11, 0.66) m, at rest

What happened, in order:
 0.00 s  flap starts at its upper stop (6.00001°)
 0.00 s  ball1 first touches starting shelf
 0.00 s  wedge heel first touches starting shelf
 0.01 s  block starts moving
 0.01 s  ball2 starts moving
 0.01 s  ball2 first touches ball2 guide
 0.09 s  flap first touches ball2
 0.09 s  ball2 comes to rest at (0.09, 0.11, 0.66) m
 0.12 s  flap is at its smallest, 6.0°
 0.19 s  flap is at its largest, 6.0°
 0.32 s  wedge first touches block
 0.32 s  wedge starts moving
 0.36 s  wedge leaves block
 0.44 s  wedge near face first touches ball1
 0.44 s  ball1 starts moving
 0.44 s  wedge touches block again
 0.44 s  wedge first touches ball1
 0.45 s  wedge near face first touches block
 0.45 s  wedge leaves ball1
 0.45 s  wedge near face leaves block
 0.51 s  wedge leaves block
 0.51 s  ball1 comes to rest at (1.23, -0.06, 0.67) m
 0.56 s  block first touches ball1
 0.58 s  block leaves ball1
 0.62 s  block first touches starting shelf
 0.64 s  wedge passes 0.20 m from ramp (ramp_leg) without touching it: nearest points (1.22, 0.01, 0.71) m and (1.05, -0.03, 0.61) m
 0.79 s  wedge near face leaves ball1
 0.82 s  block first touches ramp_deck
 0.83 s  block leaves ramp_deck
 0.88 s  block passes 0.43 m from ball2 guide without touching it: nearest points (1.02, 0.03, 0.72) m and (0.58, 0.05, 0.71) m
 1.01 s  block comes to rest at (1.07, -0.02, 0.67) m
 1.40 s  wedge heel leaves starting shelf
 1.40 s  wedge far face first touches starting shelf
 1.45 s  wedge heel touches starting shelf again
 1.46 s  wedge far face leaves starting shelf
 1.50 s  wedge far face touches starting shelf again
 1.50 s  wedge comes to rest at (1.64, -0.04, 0.77) m

State every 0.25 s:
0.00 s: wedge at (1.50, 0.00, 0.81) m, at rest; touching nothing | block at (1.37, 0.00, 1.37) m, at rest; touching nothing | ball1 at (1.24, -0.06, 0.68) m, at rest; touching nothing | flap at 6.0°, still; touching nothing | ball2 at (0.09, 0.11, 0.66) m, at rest; touching nothing
0.25 s: wedge at (1.50, 0.00, 0.81) m, at rest; touching starting shelf | block at (1.37, 0.00, 1.06) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball1 at (1.24, -0.06, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
0.50 s: wedge at (1.40, 0.02, 0.82) m, moving 0.46 m/s (vx -0.31, vy +0.33, vz +0.08), turned 31° from how it started; touching ball1, block | block at (1.22, 0.00, 0.80) m, moving 0.71 m/s (vx -0.66, vy +0.09, vz -0.26), turned 48° from how it started; touching wedge | ball1 at (1.23, -0.06, 0.67) m, moving 0.06 m/s (vx -0.06, vy -0.01, vz +0.00); touching starting shelf, wedge near face | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
0.75 s: wedge at (1.39, 0.01, 0.82) m, moving 0.48 m/s (vx +0.23, vy -0.40, vz -0.13), turned 28° from how it started; touching ball1, starting shelf | block at (1.09, -0.02, 0.68) m, moving 0.57 m/s (vx -0.36, vy -0.25, vz -0.37), turned 152° from how it started; touching starting shelf | ball1 at (1.22, -0.06, 0.67) m, at rest; touching starting shelf, wedge near face | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
1.00 s: wedge at (1.51, -0.02, 0.81) m, moving 0.42 m/s (vx +0.41, vy -0.05, vz +0.03), turned 11° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, moving 0.09 m/s (vx -0.08, vy +0.00, vz -0.05), turned 179° from how it started; touching starting shelf | ball1 at (1.22, -0.05, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
1.25 s: wedge at (1.58, -0.03, 0.80) m, moving 0.31 m/s (vx +0.29, vy -0.04, vz -0.10), turned 31° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.22, -0.05, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
1.50 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.22, -0.05, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
(the same through 1.75 s)
2.00 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.22, -0.04, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
2.25 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.21, -0.04, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
(the same through 2.75 s)
3.00 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.21, -0.03, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
(the same through 3.75 s)
4.00 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.20, -0.03, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
4.25 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.20, -0.02, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
(the same through 5.25 s)
5.50 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.20, -0.01, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
(the same through 5.75 s)
6.00 s: wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf | block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf | ball1 at (1.19, -0.01, 0.67) m, at rest; touching starting shelf | flap at 6.0°, still; touching ball2 | ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap

At the end (6.00 s):
- wedge at (1.64, -0.04, 0.77) m, at rest, turned 50° from how it started; touching starting shelf
- block at (1.07, -0.02, 0.67) m, at rest, turned 180° from how it started; touching starting shelf
- ball1 at (1.19, -0.01, 0.67) m, at rest; touching starting shelf
- flap at 6.0°, still; touching ball2
- ball2 at (0.09, 0.11, 0.66) m, at rest; touching ball2 guide, flap
</history>
