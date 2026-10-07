MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-0.76, 0.00, 1.33) m, at rest
- block: free body; its geoms: block; starts at (2.08, 0.00, 0.77) m, at rest
- pendulum: hinge joint final_striker_hinge about axis (0.00, 1.00, 0.00), range -60.0001° to 10° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (2.52, 0.00, 0.82) m, at rest

What happened, in order:
 0.00 s  block starts touching striker shelf
 0.00 s  ball2 starts touching ball2 perch
 0.00 s  pendulum is at its largest at the start, 0.0°
 0.00 s  ball1 first touches ramp_deck
 0.01 s  ball1 starts moving
 0.69 s  ball1 leaves ramp_deck
 0.69 s  ball1 first touches halfpipe_descending_one
 0.79 s  ball1 leaves halfpipe_descending_one
 0.79 s  ball1 first touches halfpipe_descending_two
 0.87 s  ball1 leaves halfpipe_descending_two
 0.87 s  ball1 first touches halfpipe_descending_three
 0.94 s  ball1 leaves halfpipe_descending_three
 0.94 s  ball1 first touches halfpipe_descending_four
 1.00 s  ball1 leaves halfpipe_descending_four
 1.00 s  ball1 first touches halfpipe_ascending_one
 1.07 s  ball1 leaves halfpipe_ascending_one
 1.07 s  ball1 first touches halfpipe_ascending_two
 1.15 s  ball1 leaves halfpipe_ascending_two
 1.15 s  ball1 first touches halfpipe_ascending_three
 1.23 s  ball1 leaves halfpipe_ascending_three
 1.23 s  ball1 first touches halfpipe_ascending_four
 1.32 s  ball1 leaves halfpipe_ascending_four
 1.32 s  ball1 first touches striker shelf
 1.34 s  ball1 leaves striker shelf
 1.37 s  ball1 first touches block
 1.37 s  block starts moving
 1.39 s  ball1 leaves block
 1.54 s  ball1 is at the top of its flight, at (2.03, 0.00, 0.94) m
 1.56 s  block first touches pendulum
 1.59 s  block leaves pendulum
 1.65 s  ball1 touches block again
 1.66 s  ball1 leaves block
 1.67 s  block touches pendulum again
 1.70 s  block leaves pendulum
 1.79 s  ball1 touches striker shelf again
 1.93 s  pendulum first touches ball2
 1.95 s  block touches pendulum again
 1.96 s  ball2 starts moving
 1.96 s  block passes 0.16 m from ball2 without touching it: nearest points (2.31, 0.00, 0.82) m and (2.47, 0.00, 0.82) m
 1.98 s  pendulum leaves ball2
 1.98 s  ball2 comes to rest at (2.52, 0.00, 0.82) m
 2.02 s  pendulum is at its smallest, -11.3°
 2.02 s  block passes 0.20 m from ball2 perch without touching it: nearest points (2.31, 0.04, 0.80) m and (2.50, 0.04, 0.77) m
 2.05 s  ball1 comes to rest at (2.06, 0.00, 0.75) m
 2.61 s  ball1 touches block again
 2.61 s  ball1 passes 0.36 m from cup (cup_near_wall) without touching it: nearest points (2.10, 0.00, 0.70) m and (2.22, 0.00, 0.36) m
 2.61 s  ball1 passes 0.27 m from hoop (hoop_07) without touching it: nearest points (2.12, 0.00, 0.72) m and (2.31, 0.00, 0.53) m
 2.61 s  ball1 passes 0.34 m from ball2 without touching it: nearest points (2.14, 0.00, 0.76) m and (2.47, 0.00, 0.81) m
 2.61 s  ball1 passes 0.37 m from ball2 perch without touching it: nearest points (2.14, 0.00, 0.75) m and (2.50, 0.00, 0.75) m
 2.61 s  block comes to rest at (2.20, 0.00, 0.77) m
 2.62 s  ball1 passes 0.12 m from pendulum without touching it: nearest points (2.14, 0.00, 0.76) m and (2.26, 0.00, 0.79) m
 2.63 s  ball1 leaves block

State every 0.25 s:
0.00 s: ball1 at (-0.76, 0.00, 1.33) m, at rest; touching nothing | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
0.25 s: ball1 at (-0.66, 0.00, 1.25) m, moving 1.05 m/s (vx +0.84, vy +0.00, vz -0.63); touching ramp_deck | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
0.50 s: ball1 at (-0.34, 0.00, 1.02) m, moving 2.10 m/s (vx +1.68, vy +0.00, vz -1.26); touching ramp_deck | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
0.75 s: ball1 at (0.19, 0.00, 0.64) m, moving 3.12 m/s (vx +2.63, vy +0.00, vz -1.68); touching halfpipe_descending_one | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
1.00 s: ball1 at (0.99, 0.00, 0.37) m, moving 3.57 m/s (vx +3.55, vy -0.00, vz -0.36); touching nothing | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
1.25 s: ball1 at (1.76, 0.00, 0.60) m, moving 2.88 m/s (vx +2.40, vy +0.00, vz +1.60); touching halfpipe_ascending_four | block at (2.08, 0.00, 0.77) m, at rest; touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
1.50 s: ball1 at (2.01, 0.00, 0.93) m, moving 0.53 m/s (vx +0.35, vy -0.00, vz +0.39); touching nothing | block at (2.14, 0.00, 0.77) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz +0.01); touching striker shelf | pendulum at 0.0°, still; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
1.75 s: ball1 at (2.05, 0.00, 0.81) m, moving 1.12 m/s (vx -0.15, vy -0.00, vz -1.11); touching nothing | block at (2.20, 0.00, 0.77) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.01); touching striker shelf | pendulum at -6.0°, turning -44°/s; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
2.00 s: ball1 at (2.06, 0.00, 0.75) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching striker shelf | block at (2.24, 0.00, 0.77) m, at rest, turned 11° from how it started; touching pendulum, striker shelf | pendulum at -11.2°, turning -2°/s; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
2.25 s: ball1 at (2.07, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.23, 0.00, 0.77) m, at rest, turned 7° from how it started; touching striker shelf | pendulum at -9.9°, turning +11°/s; touching nothing | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
2.50 s: ball1 at (2.08, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.21, 0.00, 0.77) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz +0.01); touching pendulum, striker shelf | pendulum at -6.2°, turning +15°/s; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
2.75 s: ball1 at (2.08, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.20, 0.00, 0.77) m, at rest; touching pendulum, striker shelf | pendulum at -4.6°, still; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
3.00 s: ball1 at (2.07, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.20, 0.00, 0.77) m, at rest; touching pendulum, striker shelf | pendulum at -4.6°, still; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
(the same through 3.25 s)
3.50 s: ball1 at (2.06, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.20, 0.00, 0.77) m, at rest; touching pendulum, striker shelf | pendulum at -4.6°, still; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
(the same through 4.50 s)
4.75 s: ball1 at (2.06, 0.00, 0.75) m, at rest; touching striker shelf | block at (2.20, 0.00, 0.77) m, at rest; touching pendulum, striker shelf | pendulum at -4.5°, still; touching block | ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (2.06, 0.00, 0.75) m, at rest; touching striker shelf
- block at (2.20, 0.00, 0.77) m, at rest; touching pendulum, striker shelf
- pendulum at -4.5°, still; touching block
- ball2 at (2.52, 0.00, 0.82) m, at rest; touching ball2 perch
</history>
