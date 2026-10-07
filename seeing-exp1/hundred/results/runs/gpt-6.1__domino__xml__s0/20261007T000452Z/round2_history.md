MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.03, 0.00, 0.57) m, at rest
- d1: free body; its geoms: d1_block; starts at (0.00, 0.00, 0.28) m, at rest
- d2: free body; its geoms: d2_block; starts at (0.18, 0.00, 0.28) m, at rest
- d3: free body; its geoms: d3_block; starts at (0.36, 0.00, 0.28) m, at rest
- ball2: free body; its geoms: ball2_sphere; starts at (0.61, 0.00, 0.18) m, at rest

What happened, in order:
 0.00 s  ball2_sphere starts touching stage_deck
 0.00 s  d1_block first touches stage_deck
 0.00 s  d3_block first touches stage_deck
 0.00 s  d2_block first touches stage_deck
 0.00 s  ball1_sphere first touches ramp_surface
 0.04 s  ball1 starts moving
 1.16 s  ball1_sphere leaves ramp_surface
 1.16 s  ball1_sphere first touches d1_block
 1.16 s  d1 starts moving
 1.18 s  ball1_sphere leaves d1_block
 1.23 s  ball1_sphere touches ramp_surface again
 1.30 s  ball1_sphere leaves ramp_surface
 1.35 s  ball1_sphere touches d1_block again
 1.36 s  d1_block first touches d2_block
 1.36 s  d2 starts moving
 1.36 s  ball1 passes 0.10 m from d2 (d2_block) without touching it: nearest points (0.06, 0.00, 0.31) m and (0.16, 0.00, 0.31) m
 1.37 s  ball1 passes 0.28 m from d3 (d3_block) without touching it: nearest points (0.06, 0.00, 0.31) m and (0.34, 0.00, 0.31) m
 1.37 s  d1_block leaves d2_block
 1.41 s  ball1 passes 0.50 m from ball2 (ball2_sphere) without touching it: nearest points (0.06, 0.00, 0.27) m and (0.55, 0.00, 0.19) m
 1.43 s  d1_block touches d2_block again
 1.43 s  d1_block leaves d2_block
 1.46 s  ball1_sphere touches ramp_surface again
 1.46 s  d1_block touches d2_block again
 1.46 s  d1_block leaves d2_block
 1.46 s  ball1_sphere leaves ramp_surface
 1.50 s  d1_block touches d2_block again
 1.53 s  ball1_sphere touches ramp_surface again
 1.53 s  ball1_sphere leaves ramp_surface
 1.55 s  d2_block first touches d3_block
 1.55 s  d3 starts moving
 1.56 s  d2_block leaves d3_block
 1.57 s  ball1_sphere touches ramp_surface 2 more times between 1.57 s and 6.00 s, still touching at the end
 1.61 s  d2_block touches d3_block again
 1.80 s  d3_block first touches ball2_sphere
 1.80 s  ball2 starts moving
 1.80 s  d2 passes 0.06 m from ball2 (ball2_sphere) without touching it: nearest points (0.50, 0.00, 0.23) m and (0.56, 0.00, 0.20) m
 1.80 s  d1 passes 0.22 m from ball2 (ball2_sphere) without touching it: nearest points (0.33, 0.00, 0.21) m and (0.55, 0.00, 0.19) m
 1.81 s  ball2_sphere leaves stage_deck
 1.82 s  d3_block leaves ball2_sphere
 1.82 s  ball2_sphere first touches cup_entry_lip
 1.82 s  ball2_sphere leaves cup_entry_lip
 1.86 s  d3_block touches ball2_sphere again
 1.87 s  d3_block leaves ball2_sphere
 1.90 s  d1 passes 0.05 m from d3 (d3_block) without touching it: nearest points (0.34, -0.06, 0.19) m and (0.38, -0.06, 0.16) m
 1.94 s  d3_block first touches cup_entry_lip
 1.94 s  d1 comes to rest at (0.18, 0.00, 0.18) m
 1.94 s  d2 comes to rest at (0.36, 0.00, 0.17) m
 1.95 s  ball1 comes to rest at (-0.02, 0.00, 0.20) m
 1.95 s  d2 passes 0.13 m from cup (cup_entry_lip) without touching it: nearest points (0.52, 0.06, 0.19) m and (0.63, 0.06, 0.12) m
 1.95 s  ball2_sphere first touches cup_bottom
 1.97 s  ball2_sphere leaves cup_bottom
 1.97 s  d3 comes to rest at (0.55, 0.00, 0.14) m
 2.01 s  ball2_sphere touches cup_bottom again
 2.34 s  ball2 comes to rest at (0.97, 0.00, 0.08) m
 6.00 s  ball1 passes 0.02 m from stage (stage_deck) without touching it: nearest points (-0.02, 0.00, 0.14) m and (-0.02, 0.00, 0.12) m
 6.00 s  d1 passes 0.29 m from cup (cup_entry_lip) without touching it: nearest points (0.34, -0.06, 0.19) m and (0.63, -0.06, 0.12) m

State every 0.25 s:
0.00 s: ball1 at (-1.03, 0.00, 0.57) m, at rest; touching nothing | d1 at (0.00, 0.00, 0.28) m, at rest; touching nothing | d2 at (0.18, 0.00, 0.28) m, at rest; touching nothing | d3 at (0.36, 0.00, 0.28) m, at rest; touching nothing | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
0.25 s: ball1 at (-0.99, 0.00, 0.56) m, moving 0.36 m/s (vx +0.36, vy +0.00, vz -0.08); touching ramp_surface | d1 at (0.00, 0.00, 0.28) m, at rest; touching stage_deck | d2 at (0.18, 0.00, 0.28) m, at rest; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
0.50 s: ball1 at (-0.86, 0.00, 0.53) m, moving 0.73 m/s (vx +0.71, vy +0.00, vz -0.15); touching ramp_surface | d1 at (0.00, 0.00, 0.28) m, at rest; touching stage_deck | d2 at (0.18, 0.00, 0.28) m, at rest; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
0.75 s: ball1 at (-0.63, 0.00, 0.49) m, moving 1.09 m/s (vx +1.07, vy +0.00, vz -0.23); touching ramp_surface | d1 at (0.00, 0.00, 0.28) m, at rest; touching stage_deck | d2 at (0.18, 0.00, 0.28) m, at rest; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
1.00 s: ball1 at (-0.32, 0.00, 0.42) m, moving 1.46 m/s (vx +1.42, vy +0.00, vz -0.30); touching ramp_surface | d1 at (0.00, 0.00, 0.28) m, at rest; touching stage_deck | d2 at (0.18, 0.00, 0.28) m, at rest; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
1.25 s: ball1 at (-0.05, 0.00, 0.36) m, moving 0.41 m/s (vx +0.39, vy -0.00, vz -0.13); touching ramp_surface | d1 at (0.03, 0.00, 0.28) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz -0.02), turned 11° from how it started; touching stage_deck | d2 at (0.18, 0.00, 0.28) m, at rest; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
1.50 s: ball1 at (-0.02, 0.00, 0.24) m, moving 0.36 m/s (vx -0.09, vy +0.00, vz -0.34); touching d1_block | d1 at (0.11, 0.00, 0.25) m, moving 0.38 m/s (vx +0.32, vy -0.00, vz -0.21), turned 41° from how it started; touching ball1_sphere | d2 at (0.23, 0.00, 0.28) m, moving 0.50 m/s (vx +0.49, vy -0.00, vz -0.08), turned 17° from how it started; touching stage_deck | d3 at (0.36, 0.00, 0.28) m, at rest; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
1.75 s: ball1 at (-0.02, 0.00, 0.21) m, at rest; touching d1_block | d1 at (0.17, 0.00, 0.20) m, moving 0.37 m/s (vx +0.18, vy -0.00, vz -0.32), turned 68° from how it started; touching ball1_sphere, stage_deck | d2 at (0.33, 0.00, 0.22) m, moving 0.59 m/s (vx +0.38, vy -0.00, vz -0.45), turned 58° from how it started; touching nothing | d3 at (0.47, 0.00, 0.25) m, moving 1.03 m/s (vx +0.86, vy -0.00, vz -0.57), turned 41° from how it started; touching stage_deck | ball2 at (0.61, 0.00, 0.18) m, at rest; touching stage_deck
2.00 s: ball1 at (-0.02, 0.00, 0.20) m, at rest; touching d1_block, ramp_surface | d1 at (0.18, 0.00, 0.18) m, at rest, turned 77° from how it started; touching ball1_sphere, d2_block, stage_deck | d2 at (0.36, 0.00, 0.17) m, at rest, turned 77° from how it started; touching d1_block, d3_block, stage_deck | d3 at (0.55, 0.00, 0.14) m, at rest, turned 90° from how it started; touching cup_entry_lip, d2_block, stage_deck | ball2 at (0.85, 0.00, 0.08) m, moving 0.68 m/s (vx +0.67, vy -0.00, vz -0.10); touching nothing
2.25 s: ball1 at (-0.02, 0.00, 0.20) m, at rest; touching d1_block, ramp_surface | d1 at (0.18, 0.00, 0.18) m, at rest, turned 77° from how it started; touching ball1_sphere, d2_block, stage_deck | d2 at (0.36, 0.00, 0.17) m, at rest, turned 77° from how it started; touching d1_block, d3_block, stage_deck | d3 at (0.55, 0.00, 0.14) m, at rest, turned 90° from how it started; touching cup_entry_lip, d2_block, stage_deck | ball2 at (0.96, 0.00, 0.08) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz +0.01); touching nothing
2.50 s: ball1 at (-0.02, 0.00, 0.20) m, at rest; touching d1_block, ramp_surface | d1 at (0.18, 0.00, 0.18) m, at rest, turned 77° from how it started; touching ball1_sphere, d2_block, stage_deck | d2 at (0.36, 0.00, 0.17) m, at rest, turned 77° from how it started; touching d1_block, d3_block, stage_deck | d3 at (0.55, 0.00, 0.14) m, at rest, turned 90° from how it started; touching cup_entry_lip, d2_block, stage_deck | ball2 at (0.97, 0.00, 0.08) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.02, 0.00, 0.20) m, at rest; touching d1_block, ramp_surface
- d1 at (0.18, 0.00, 0.18) m, at rest, turned 77° from how it started; touching ball1_sphere, d2_block, stage_deck
- d2 at (0.36, 0.00, 0.17) m, at rest, turned 77° from how it started; touching d1_block, d3_block, stage_deck
- d3 at (0.55, 0.00, 0.14) m, at rest, turned 90° from how it started; touching cup_entry_lip, d2_block, stage_deck
- ball2 at (0.97, 0.00, 0.08) m, at rest; touching cup_bottom
</history>
