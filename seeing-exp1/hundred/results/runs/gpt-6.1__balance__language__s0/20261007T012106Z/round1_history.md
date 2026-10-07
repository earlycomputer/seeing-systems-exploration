MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- balance: hinge joint balance_hinge about axis (0.00, 1.00, 0.00), range -25° to 0° as MuJoCo applies it; its geoms: balance, balance.receiver entrance, balance.receiver back, balance.receiver left, balance.receiver right; starts at 0.0°, still
- ball1: free body; its geoms: ball1; starts at (-1.51, 0.00, 1.59) m, at rest
- block: free body; its geoms: block; starts at (0.62, 0.00, 1.12) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.00, 0.00, 1.40) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching ramp_deck
 0.00 s  balance starts at its upper stop (0°)
 0.00 s  balance first touches block
 0.01 s  ball2 starts moving
 0.02 s  ball1 starts moving
 0.10 s  balance is at its largest, 0.0°
 0.30 s  balance first touches ball2
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
 0.98 s  balance is at its smallest, -26.4°
 0.98 s  balance passes 0.20 m from ball2 perch without touching it: nearest points (0.50, 0.09, 1.17) m and (0.41, 0.15, 1.34) m
 0.98 s  balance passes 0.15 m from hoop (hoop_08) without touching it: nearest points (-0.59, 0.09, 0.59) m and (-0.52, 0.10, 0.46) m
 0.98 s  balance passes 0.32 m from cup (cup_right_wall) without touching it: nearest points (-0.62, -0.09, 0.57) m and (-0.62, -0.13, 0.25) m
 1.02 s  block first touches ball2 perch
 1.03 s  block leaves ball2 perch
 1.03 s  balance reaches its lower stop (-25°) again moving +17°/s
 1.07 s  ball2 passes 0.05 m from pivot stand without touching it: nearest points (-0.05, 0.00, 0.90) m and (-0.03, 0.00, 0.85) m
 1.09 s  balance leaves ball1
 1.10 s  balance.receiver entrance touches ball1 again
 1.12 s  block is at the top of its flight, at (0.33, 0.00, 1.51) m
 1.13 s  balance.receiver entrance leaves ball1
 1.18 s  balance touches ball1 again
 1.18 s  balance.receiver entrance touches ball1 again
 1.20 s  ball1 comes to rest at (-0.59, 0.00, 0.72) m
 1.20 s  ball1 passes 0.21 m from hoop (hoop_08) without touching it: nearest points (-0.57, 0.00, 0.65) m and (-0.50, 0.02, 0.46) m
 1.20 s  ball1 passes 0.42 m from cup (cup_right_wall) without touching it: nearest points (-0.59, -0.02, 0.65) m and (-0.59, -0.13, 0.25) m
 1.35 s  balance leaves ball2
 1.35 s  balance.receiver back first touches ball2
 1.36 s  ball1 passes 0.19 m from ball2 without touching it: nearest points (-0.52, 0.00, 0.75) m and (-0.35, 0.00, 0.81) m
 1.39 s  balance.receiver back leaves ball2
 1.39 s  ball2 passes 0.48 m from ramp (ramp_deck) without touching it: nearest points (-0.34, 0.00, 0.85) m and (-0.76, 0.00, 1.08) m
 1.42 s  balance touches block again
 1.43 s  balance.receiver back touches ball2 again
 1.43 s  balance leaves block
 1.44 s  balance touches ball2 again
 1.44 s  ball2 passes 0.36 m from hoop (hoop_09) without touching it: nearest points (-0.32, -0.01, 0.79) m and (-0.44, -0.09, 0.46) m
 1.44 s  balance.receiver back leaves ball2
 1.44 s  ball2 comes to rest at (-0.31, 0.00, 0.82) m
 1.47 s  balance touches block again
 1.48 s  balance.receiver back touches ball2 again
 1.72 s  block passes 0.05 m from pivot stand without touching it: nearest points (-0.05, 0.04, 0.90) m and (-0.03, 0.04, 0.85) m
 1.80 s  block comes to rest at (0.02, -0.03, 0.99) m
 6.00 s  block passes 0.05 m from ball2 without touching it: nearest points (-0.23, 0.02, 0.86) m and (-0.27, 0.01, 0.84) m
 6.00 s  ball1 passes 0.31 m from block without touching it: nearest points (-0.53, 0.00, 0.75) m and (-0.24, 0.02, 0.89) m

State every 0.25 s:
0.00 s: balance at 0.0°, still; touching nothing | ball1 at (-1.51, 0.00, 1.59) m, at rest; touching ramp_deck | block at (0.62, 0.00, 1.12) m, at rest; touching nothing | ball2 at (0.00, 0.00, 1.40) m, at rest; touching nothing
0.25 s: balance at 0.0°, still; touching block | ball1 at (-1.42, 0.00, 1.54) m, moving 0.84 m/s (vx +0.73, vy +0.00, vz -0.41); touching ramp_deck | block at (0.62, 0.00, 1.12) m, at rest; touching balance | ball2 at (0.00, 0.00, 1.10) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: balance at 0.0°, still; touching ball2, block | ball1 at (-1.15, 0.00, 1.38) m, moving 1.69 m/s (vx +1.45, vy +0.00, vz -0.86); touching nothing | block at (0.62, 0.00, 1.12) m, at rest; touching balance | ball2 at (0.00, 0.00, 0.96) m, at rest; touching balance
0.75 s: balance at -1.0°, turning -106°/s; touching ball1, ball2, block | ball1 at (-0.69, 0.00, 1.12) m, moving 2.33 m/s (vx +2.06, vy +0.00, vz -1.08); touching balance.receiver entrance | block at (0.62, 0.00, 1.13) m, moving 1.20 m/s (vx -0.24, vy +0.00, vz +1.18); touching balance | ball2 at (0.00, 0.00, 0.96) m, at rest; touching balance
1.00 s: balance at -26.0°, turning +24°/s; touching ball1 | ball1 at (-0.49, 0.00, 0.76) m, moving 0.99 m/s (vx -0.95, vy +0.00, vz -0.25); touching balance | block at (0.44, 0.00, 1.44) m, moving 1.77 m/s (vx -1.23, vy +0.00, vz +1.28), turned 22° from how it started; touching nothing | ball2 at (-0.04, 0.00, 0.95) m, moving 0.40 m/s (vx -0.36, vy -0.00, vz -0.17); touching nothing
1.25 s: balance at -25.2°, turning +2°/s; touching ball1 | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (0.20, 0.00, 1.42) m, moving 1.61 m/s (vx -0.92, vy -0.00, vz -1.32), turned 88° from how it started; touching nothing | ball2 at (-0.20, 0.00, 0.87) m, moving 1.04 m/s (vx -0.94, vy -0.00, vz -0.44); touching nothing
1.50 s: balance at -25.1°, still; touching ball1, ball2, block | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (0.03, -0.03, 0.99) m, moving 0.19 m/s (vx +0.06, vy -0.18, vz -0.00), turned 120° from how it started; touching balance | ball2 at (-0.31, 0.00, 0.82) m, at rest; touching balance, balance.receiver back
1.75 s: balance at -25.1°, still; touching ball1, ball2, block | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (0.02, -0.02, 0.99) m, at rest, turned 123° from how it started; touching balance | ball2 at (-0.31, 0.00, 0.82) m, at rest; touching balance, balance.receiver back
2.00 s: balance at -25.1°, still; touching ball1, ball2, block | ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance | block at (0.02, -0.03, 0.99) m, at rest, turned 123° from how it started; touching balance | ball2 at (-0.31, 0.00, 0.82) m, at rest; touching balance, balance.receiver back
(the same through 6.00 s)

At the end (6.00 s):
- balance at -25.1°, still; touching ball1, ball2, block
- ball1 at (-0.59, 0.00, 0.72) m, at rest; touching balance, balance.receiver entrance
- block at (0.02, -0.03, 0.99) m, at rest, turned 123° from how it started; touching balance
- ball2 at (-0.31, 0.00, 0.82) m, at rest; touching balance, balance.receiver back
</history>
