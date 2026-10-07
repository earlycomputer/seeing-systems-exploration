MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- balance: hinge joint balance_hinge about axis (0.00, 1.00, 0.00), range -25° to 0° as MuJoCo applies it; its geoms: balance, balance.receiver entrance, balance.receiver back, balance.receiver left, balance.receiver right; starts at 0.0°, still
- ball1: free body; its geoms: ball1; starts at (-1.51, 0.00, 1.59) m, at rest
- block: free body; its geoms: block; starts at (0.62, 0.00, 1.12) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.39, 0.18, 1.40) m, at rest

What happened, in order:
 0.00 s  ball2 starts touching ball2 perch
 0.00 s  ball1 starts touching ramp_deck
 0.00 s  balance starts at its upper stop (0°)
 0.00 s  balance first touches block
 0.02 s  ball1 starts moving
 0.10 s  balance is at its largest, 0.0°
 0.73 s  ball1 leaves ramp_deck
 0.74 s  balance.receiver entrance first touches ball1
 0.74 s  block starts moving
 0.76 s  balance.receiver entrance leaves ball1
 0.87 s  balance.receiver back first touches ball1
 0.88 s  ball1 passes 0.35 m from pivot stand without touching it: nearest points (-0.38, 0.00, 0.89) m and (-0.03, 0.00, 0.85) m
 0.88 s  balance first touches ball1
 0.90 s  balance.receiver back leaves ball1
 0.95 s  balance reaches its lower stop (-25°) moving -184°/s
 0.96 s  balance leaves block
 0.96 s  ball2 leaves ball2 perch
 0.96 s  block first touches ball2
 0.96 s  ball2 starts moving
 0.98 s  balance is at its smallest, -26.4°
 0.98 s  block leaves ball2
 0.98 s  balance passes 0.20 m from ball2 perch without touching it: nearest points (0.50, 0.09, 1.17) m and (0.41, 0.15, 1.34) m
 0.98 s  balance passes 0.15 m from hoop (hoop_08) without touching it: nearest points (-0.59, 0.09, 0.59) m and (-0.52, 0.10, 0.46) m
 0.98 s  balance passes 0.32 m from cup (cup_right_wall) without touching it: nearest points (-0.62, -0.09, 0.57) m and (-0.62, -0.14, 0.25) m
 0.99 s  ball2 is at the top of its flight, at (0.37, 0.18, 1.40) m
 1.03 s  balance reaches its lower stop (-25°) again moving +17°/s
 1.09 s  balance leaves ball1
 1.10 s  balance.receiver entrance touches ball1 again
 1.11 s  block first touches ball2 perch
 1.12 s  block leaves ball2 perch
 1.13 s  balance.receiver entrance leaves ball1
 1.18 s  balance touches ball1 again
 1.18 s  balance.receiver entrance touches ball1 again
 1.20 s  ball1 comes to rest at (-0.59, 0.00, 0.72) m
 1.20 s  ball1 passes 0.21 m from hoop (hoop_08) without touching it: nearest points (-0.57, 0.00, 0.65) m and (-0.50, 0.02, 0.46) m
 1.20 s  ball1 passes 0.42 m from cup (cup_right_wall) without touching it: nearest points (-0.59, -0.02, 0.65) m and (-0.59, -0.13, 0.25) m
 1.27 s  balance passes 0.05 m from ball2 without touching it: nearest points (0.21, 0.09, 1.02) m and (0.21, 0.14, 1.02) m
 1.42 s  ball2 passes 0.26 m from hoop (hoop_00) without touching it: nearest points (0.16, 0.19, 0.49) m and (0.41, 0.24, 0.45) m
 1.44 s  balance touches block again
 1.47 s  block passes 0.05 m from pivot stand without touching it: nearest points (-0.05, 0.04, 0.89) m and (-0.03, 0.04, 0.85) m
 1.52 s  ball2 first touches cup_base
 1.52 s  balance leaves block
 1.55 s  ball2 leaves cup_base
 1.57 s  balance touches block again
 1.63 s  ball2 touches cup_base again
 1.80 s  balance leaves block
 1.83 s  balance touches block again
 1.84 s  balance leaves block
 1.95 s  block passes 0.48 m from ramp (ramp_deck) without touching it: nearest points (-0.29, 0.14, 1.02) m and (-0.76, 0.09, 1.08) m
 2.06 s  ball1 passes 0.24 m from block without touching it: nearest points (-0.53, 0.04, 0.73) m and (-0.32, 0.16, 0.75) m
 2.16 s  block touches ball2 again
 2.17 s  block first touches cup_base
 2.18 s  block leaves ball2
 2.27 s  block passes 0.07 m from hoop (hoop_06) without touching it: nearest points (-0.39, 0.44, 0.39) m and (-0.42, 0.47, 0.44) m
 2.30 s  block leaves cup_base
 2.30 s  block first touches cup_left_wall
 2.33 s  block leaves cup_left_wall
 2.38 s  block touches cup_left_wall again
 2.42 s  block touches cup_base again
 2.49 s  ball2 comes to rest at (0.05, 0.13, 0.06) m
 2.69 s  block comes to rest at (-0.10, 0.38, 0.21) m
 3.33 s  ball2 passes 0.05 m from pivot stand without touching it: nearest points (0.04, 0.09, 0.06) m and (0.03, 0.04, 0.06) m

State every 0.25 s:
0.00 s: balance at 0.0°, still; touching nothing | ball1 at (-1.51, 0.00, 1.59) m, at rest; touching ramp_deck | block at (0.62, 0.00, 1.12) m, at rest; touching nothing | ball2 at (0.39, 0.18, 1.40) m, at rest; touching ball2 perch
0.25 s: balance at 0.0°, still; touching block | ball1 at (-1.42, 0.00, 1.54) m, moving 0.84 m/s (vx +0.73, vy +0.00, vz -0.41); touching ramp_deck | block at (0.62, 0.00, 1.12) m, at rest; touching balance | ball2 at (0.39, 0.18, 1.40) m, at rest; touching ball2 perch
0.50 s: balance at 0.0°, still; touching block | ball1 at (-1.15, 0.00, 1.38) m, moving 1.69 m/s (vx +1.45, vy +0.00, vz -0.86); touching nothing | block at (0.62, 0.00, 1.12) m, at rest; touching balance | ball2 at (0.39, 0.18, 1.40) m, at rest; touching ball2 perch
0.75 s: balance at -1.0°, turning -106°/s; touching ball1, block | ball1 at (-0.69, 0.00, 1.12) m, moving 2.33 m/s (vx +2.06, vy +0.00, vz -1.08); touching balance.receiver entrance | block at (0.62, 0.00, 1.13) m, moving 1.20 m/s (vx -0.24, vy +0.00, vz +1.18); touching balance | ball2 at (0.39, 0.18, 1.40) m, at rest; touching ball2 perch
1.00 s: balance at -26.0°, turning +24°/s; touching ball1 | ball1 at (-0.49, 0.00, 0.76) m, moving 0.99 m/s (vx -0.95, vy +0.00, vz -0.25); touching balance | block at (0.45, 0.00, 1.44) m, moving 1.61 m/s (vx -1.08, vy -0.00, vz +1.20), turned 23° from how it started; touching nothing | ball2 at (0.37, 0.18, 1.40) m, moving 0.60 m/s (vx -0.60, vy +0.01, vz -0.09); touching nothing
1.25 s: balance at -25.2°, turning +3°/s; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (0.19, 0.00, 1.43) m, moving 1.58 m/s (vx -0.96, vy +0.01, vz -1.26), turned 70° from how it started; touching nothing | ball2 at (0.22, 0.18, 1.08) m, moving 2.61 m/s (vx -0.60, vy +0.01, vz -2.54); touching nothing
1.50 s: balance at -25.1°, still; touching ball1, block | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.01, 0.02, 0.99) m, moving 0.67 m/s (vx -0.29, vy +0.30, vz +0.53), turned 127° from how it started; touching balance | ball2 at (0.07, 0.19, 0.14) m, moving 5.03 m/s (vx -0.60, vy +0.01, vz -4.99); touching nothing
1.75 s: balance at -25.1°, still; touching ball1, block | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.06, 0.10, 0.97) m, moving 0.50 m/s (vx -0.14, vy +0.31, vz -0.36), turned 149° from how it started; touching balance | ball2 at (0.00, 0.19, 0.06) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching cup_base
2.00 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.10, 0.19, 0.73) m, moving 2.11 m/s (vx -0.17, vy +0.40, vz -2.06), turned 173° from how it started; touching nothing | ball2 at (-0.01, 0.19, 0.06) m, at rest; touching cup_base
2.25 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.15, 0.32, 0.27) m, moving 0.74 m/s (vx -0.12, vy +0.73, vz +0.00), turned 149° from how it started; touching cup_base | ball2 at (0.02, 0.16, 0.06) m, moving 0.31 m/s (vx +0.20, vy -0.24, vz -0.01); touching cup_base
2.50 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.11, 0.39, 0.21) m, moving 0.10 m/s (vx +0.08, vy -0.04, vz -0.04), turned 145° from how it started; touching cup_base | ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
2.75 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.10, 0.38, 0.21) m, at rest, turned 148° from how it started; touching cup_base | ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
3.00 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.10, 0.38, 0.21) m, at rest, turned 148° from how it started; touching cup_base, cup_left_wall | ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
(the same through 3.25 s)
3.50 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.10, 0.38, 0.21) m, at rest, turned 149° from how it started; touching cup_base, cup_left_wall | ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
3.75 s: balance at -25.1°, still; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (-0.09, 0.37, 0.21) m, at rest, turned 151° from how it started; touching cup_base, cup_left_wall | ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- balance at -25.1°, still; touching ball1
- ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance
- block at (-0.09, 0.37, 0.21) m, at rest, turned 151° from how it started; touching cup_base, cup_left_wall
- ball2 at (0.05, 0.13, 0.06) m, at rest; touching cup_base
</history>
