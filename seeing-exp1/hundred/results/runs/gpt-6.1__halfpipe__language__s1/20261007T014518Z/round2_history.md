MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-1.94, 0.00, 1.21) m, at rest
- block: free body; its geoms: block; starts at (1.35, 0.00, 0.63) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -100° to 10° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (2.07, 0.00, 0.63) m, at rest

What happened, in order:
 0.00 s  block starts touching striker platform
 0.00 s  ball2 starts touching target perch
 0.00 s  pendulum is at its largest at the start, 0.0°
 0.00 s  ball1 first touches ramp_deck
 0.01 s  ball1 starts moving
 0.69 s  ball1 leaves ramp_deck
 0.69 s  ball1 first touches halfpipe_near_upper_deck
 0.80 s  ball1 leaves halfpipe_near_upper_deck
 0.80 s  ball1 first touches halfpipe_near_middle_deck
 0.89 s  ball1 leaves halfpipe_near_middle_deck
 0.89 s  ball1 first touches halfpipe_near_lower_deck
 0.97 s  ball1 leaves halfpipe_near_lower_deck
 0.97 s  ball1 first touches halfpipe_near_bottom_deck
 1.05 s  ball1 leaves halfpipe_near_bottom_deck
 1.05 s  ball1 first touches halfpipe_far_bottom_deck
 1.14 s  ball1 leaves halfpipe_far_bottom_deck
 1.14 s  ball1 first touches halfpipe_far_lower_deck
 1.22 s  ball1 leaves halfpipe_far_lower_deck
 1.22 s  ball1 first touches halfpipe_far_middle_deck
 1.32 s  ball1 leaves halfpipe_far_middle_deck
 1.32 s  ball1 first touches halfpipe_far_upper_deck
 1.43 s  ball1 leaves halfpipe_far_upper_deck
 1.43 s  ball1 first touches striker platform
 1.44 s  ball1 leaves striker platform
 1.46 s  ball1 first touches block
 1.46 s  block starts moving
 1.49 s  ball1 leaves block
 1.65 s  ball1 is at the top of its flight, at (1.33, 0.00, 0.82) m
 1.77 s  block first touches pendulum
 1.80 s  block leaves pendulum
 1.83 s  ball1 touches block again
 1.83 s  ball1 leaves block
 1.83 s  block touches pendulum again
 1.85 s  ball1 touches striker platform again
 1.87 s  ball1 touches block again
 1.87 s  ball1 passes 0.20 m from pendulum without touching it: nearest points (1.60, 0.00, 0.63) m and (1.80, 0.00, 0.63) m
 1.87 s  ball1 leaves block
 1.89 s  pendulum first touches ball2
 1.89 s  ball2 starts moving
 1.90 s  block passes 0.20 m from ball2 without touching it: nearest points (1.82, 0.00, 0.64) m and (2.02, 0.00, 0.63) m
 1.90 s  ball1 passes 0.40 m from ball2 without touching it: nearest points (1.62, 0.00, 0.63) m and (2.02, 0.00, 0.63) m
 1.92 s  ball1 touches block again
 1.92 s  ball1 leaves block
 1.92 s  pendulum leaves ball2
 1.95 s  pendulum first touches target perch
 1.95 s  ball1 passes 0.31 m from cup (cup_near_wall) without touching it: nearest points (1.59, 0.00, 0.55) m and (1.68, 0.00, 0.26) m
 1.95 s  ball1 leaves striker platform
 1.95 s  ball1 touches block 2 more times between 1.95 s and 2.10 s
 1.95 s  pendulum is at its smallest, -6.1°
 1.96 s  block passes 0.18 m from target perch without touching it: nearest points (1.84, -0.09, 0.59) m and (2.02, -0.09, 0.57) m
 1.96 s  ball1 passes 0.34 m from hoop (hoop_08) without touching it: nearest points (1.63, 0.00, 0.58) m and (1.89, 0.00, 0.36) m
 1.96 s  ball1 passes 0.38 m from target perch without touching it: nearest points (1.64, 0.00, 0.62) m and (2.02, 0.00, 0.57) m
 1.98 s  pendulum leaves target perch
 1.99 s  ball1 touches striker platform again
 2.02 s  ball2 leaves target perch
 2.08 s  pendulum touches target perch again
 2.09 s  block passes 0.18 m from hoop (hoop_08) without touching it: nearest points (1.81, 0.00, 0.52) m and (1.89, 0.00, 0.36) m
 2.16 s  block comes to rest at (1.73, 0.00, 0.62) m
 2.33 s  ball2 first touches cup_base
 2.37 s  ball2 leaves cup_base
 2.42 s  ball2 touches cup_base again
 2.52 s  ball2 comes to rest at (2.36, 0.00, 0.09) m
 5.39 s  ball1 leaves striker platform
 5.42 s  ball1 touches halfpipe_far_upper_deck again
 5.68 s  ball1 touches halfpipe_far_middle_deck again
 5.68 s  ball1 leaves halfpipe_far_upper_deck
 5.84 s  ball1 touches halfpipe_far_lower_deck again
 5.84 s  ball1 leaves halfpipe_far_middle_deck
 5.97 s  ball1 touches halfpipe_far_bottom_deck again
 5.97 s  ball1 leaves halfpipe_far_lower_deck
 6.00 s  ball1 is still moving at the end, 2.25 m/s
 6.00 s  block passes 0.26 m from cup (cup_near_wall) without touching it: nearest points (1.80, -0.14, 0.51) m and (1.72, -0.14, 0.26) m

State every 0.25 s:
0.00 s: ball1 at (-1.94, 0.00, 1.21) m, at rest; touching nothing | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
0.25 s: ball1 at (-1.84, 0.00, 1.13) m, moving 1.05 m/s (vx +0.84, vy +0.00, vz -0.63); touching ramp_deck | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
0.50 s: ball1 at (-1.52, 0.00, 0.90) m, moving 2.10 m/s (vx +1.69, vy +0.00, vz -1.26); touching ramp_deck | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
0.75 s: ball1 at (-0.99, 0.00, 0.51) m, moving 3.13 m/s (vx +2.61, vy +0.00, vz -1.74); touching halfpipe_near_upper_deck | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
1.00 s: ball1 at (-0.19, 0.00, 0.24) m, moving 3.55 m/s (vx +3.55, vy +0.00, vz -0.14); touching halfpipe_near_bottom_deck | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
1.25 s: ball1 at (0.66, 0.00, 0.34) m, moving 3.23 m/s (vx +2.95, vy +0.00, vz +1.33); touching halfpipe_far_middle_deck | block at (1.35, 0.00, 0.63) m, at rest; touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
1.50 s: ball1 at (1.21, 0.00, 0.71) m, moving 1.67 m/s (vx +0.87, vy +0.00, vz +1.43); touching nothing | block at (1.39, 0.00, 0.63) m, moving 1.11 m/s (vx +1.11, vy -0.00, vz -0.01); touching nothing | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
1.75 s: ball1 at (1.42, 0.00, 0.77) m, moving 1.34 m/s (vx +0.87, vy +0.00, vz -1.02); touching nothing | block at (1.63, 0.00, 0.63) m, moving 0.86 m/s (vx +0.86, vy -0.00, vz +0.04); touching striker platform | pendulum at 0.0°, still; touching nothing | ball2 at (2.07, 0.00, 0.63) m, at rest; touching target perch
2.00 s: ball1 at (1.56, 0.00, 0.63) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching striker platform | block at (1.74, 0.00, 0.63) m, moving 0.08 m/s (vx -0.07, vy -0.00, vz -0.04), turned 4° from how it started; touching nothing | pendulum at -5.9°, turning +3°/s; touching nothing | ball2 at (2.13, 0.00, 0.63) m, moving 0.57 m/s (vx +0.56, vy +0.00, vz -0.13); touching nothing
2.25 s: ball1 at (1.53, 0.00, 0.63) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.28, 0.00, 0.31) m, moving 2.55 m/s (vx +0.58, vy +0.00, vz -2.49); touching nothing
2.50 s: ball1 at (1.50, 0.00, 0.63) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching cup_base
2.75 s: ball1 at (1.47, 0.00, 0.63) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
3.00 s: ball1 at (1.44, 0.00, 0.63) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
3.25 s: ball1 at (1.41, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
3.50 s: ball1 at (1.37, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
3.75 s: ball1 at (1.34, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
4.00 s: ball1 at (1.31, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
4.25 s: ball1 at (1.28, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
4.50 s: ball1 at (1.25, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
4.75 s: ball1 at (1.22, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
5.00 s: ball1 at (1.20, 0.00, 0.63) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz -0.00); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
5.25 s: ball1 at (1.16, 0.00, 0.63) m, moving 0.19 m/s (vx -0.18, vy +0.00, vz -0.03); touching striker platform | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
5.50 s: ball1 at (1.05, 0.00, 0.55) m, moving 1.02 m/s (vx -0.85, vy +0.00, vz -0.57); touching halfpipe_far_upper_deck | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
5.75 s: ball1 at (0.73, 0.00, 0.37) m, moving 1.89 m/s (vx -1.74, vy +0.00, vz -0.75); touching halfpipe_far_middle_deck | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
6.00 s: ball1 at (0.22, 0.00, 0.24) m, moving 2.25 m/s (vx -2.25, vy +0.00, vz -0.09); touching halfpipe_far_bottom_deck | block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform | pendulum at -6.0°, still; touching block, target perch | ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (0.22, 0.00, 0.24) m, moving 2.25 m/s (vx -2.25, vy +0.00, vz -0.09); touching halfpipe_far_bottom_deck
- block at (1.73, 0.00, 0.62) m, at rest, turned 17° from how it started; touching pendulum, striker platform
- pendulum at -6.0°, still; touching block, target perch
- ball2 at (2.36, 0.00, 0.09) m, at rest; touching cup_base
</history>
