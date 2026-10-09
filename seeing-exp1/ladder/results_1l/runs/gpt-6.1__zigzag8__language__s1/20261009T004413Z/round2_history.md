MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1.lever scoop base, lever1.lever scoop back, lever1.lever striker; starts at 0.0°, still
- ball1: free body; its geoms: ball1; starts at (-0.27, 0.00, 1.05) m, at rest
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range -0.55 m to 0 m as MuJoCo applies it; its geoms: cart1; starts at 0.000 m, still
- ball2: free body; its geoms: ball2; starts at (-0.64, 0.00, 0.54) m, at rest
- domino1: free body; its geoms: domino1; starts at (-0.46, 0.00, 0.61) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range -70° to 0° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -38° to 0° as MuJoCo applies it; its geoms: pendulum1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (-2.42, 0.00, 0.42) m, at rest

What happened, in order:
 0.00 s  ball2 starts touching ramp1_deck
 0.00 s  ball2 starts touching ramp retaining lip
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  lever1 is at its largest at the start, 0.0°
 0.00 s  cart1 starts at its upper stop (0 m)
 0.00 s  cart1 is at its largest at the start, 0.0 m
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  domino1 first touches domino support
 0.00 s  block1 first touches block support
 0.01 s  ball1 starts moving
 0.25 s  ball1 passes 0.03 m from ring1 (ring1_03) without touching it: nearest points (-0.26, 0.05, 0.75) m and (-0.25, 0.08, 0.75) m
 0.25 s  lever1.lever striker first touches cart1
 0.27 s  lever1.lever striker leaves cart1
 0.32 s  ball1 passes 0.27 m from ball2 without touching it: nearest points (-0.32, 0.00, 0.54) m and (-0.59, 0.00, 0.54) m
 0.33 s  lever1.lever striker touches cart1 again
 0.34 s  lever1 first touches ball1
 0.34 s  lever1.lever scoop base first touches ball1
 0.35 s  lever1.lever striker leaves cart1
 0.36 s  lever1 leaves ball1
 0.36 s  lever1.lever scoop base leaves ball1
 0.40 s  ball1 passes 0.09 m from domino1 without touching it: nearest points (-0.32, 0.00, 0.48) m and (-0.41, 0.00, 0.49) m
 0.43 s  ball1 passes 0.32 m from ramp retaining lip without touching it: nearest points (-0.33, 0.00, 0.46) m and (-0.64, 0.00, 0.49) m
 0.44 s  ball1 passes 0.06 m from domino support without touching it: nearest points (-0.33, 0.00, 0.45) m and (-0.39, 0.00, 0.45) m
 0.45 s  lever1 touches ball1 again
 0.45 s  lever1.lever scoop base touches ball1 again
 0.47 s  ball1 passes 0.19 m from cart1 without touching it: nearest points (-0.24, 0.00, 0.45) m and (-0.10, 0.00, 0.57) m
 0.57 s  lever1 leaves ball1
 0.57 s  lever1.lever scoop base leaves ball1
 0.57 s  ball1 passes 0.24 m from ramp1 (ramp1_leg) without touching it: nearest points (-0.34, 0.00, 0.32) m and (-0.58, 0.00, 0.32) m
 0.57 s  lever1.lever scoop back first touches ball1
 0.59 s  cart1 passes 0.07 m from ring1 (ring1_00) without touching it: nearest points (-0.18, 0.00, 0.67) m and (-0.18, 0.00, 0.74) m
 0.61 s  lever1 reaches its -45° stop (neither end sits lower) moving -255°/s
 0.63 s  lever1.lever scoop back leaves ball1
 0.63 s  lever1 touches ball1 again
 0.63 s  lever1.lever scoop base touches ball1 again
 0.63 s  lever1 is at its smallest, -46.8°
 0.68 s  lever1.lever scoop back touches ball1 again
 0.68 s  lever1 reaches its -45° stop (neither end sits lower) again moving +27°/s
 0.70 s  ball1 comes to rest at (-0.26, 0.00, 0.27) m
 0.91 s  cart1 passes 0.08 m from domino support without touching it: nearest points (-0.39, 0.09, 0.57) m and (-0.39, 0.09, 0.49) m
 0.94 s  cart1 first touches domino1
 0.94 s  domino1 starts moving
 1.00 s  cart1 leaves domino1
 1.04 s  cart1 touches domino1 again
 1.18 s  cart1 is at its smallest, -0.4 m
 1.18 s  cart1 passes 0.15 m from ball2 without touching it: nearest points (-0.44, 0.00, 0.57) m and (-0.59, 0.00, 0.55) m
 1.18 s  cart1 passes 0.17 m from ramp1 (ramp1_leg) without touching it: nearest points (-0.44, 0.03, 0.57) m and (-0.58, 0.03, 0.47) m
 1.18 s  cart1 passes 0.22 m from ramp retaining lip without touching it: nearest points (-0.44, -0.09, 0.57) m and (-0.64, -0.09, 0.49) m
 1.45 s  cart1 leaves domino1
 1.72 s  domino1 comes to rest at (-0.47, 0.00, 0.61) m
 5.60 s  lever1.lever striker touches cart1 again
 5.62 s  lever1.lever striker leaves cart1

State every 0.25 s:
0.00 s: lever1 at 0.0°, still; touching nothing | ball1 at (-0.27, 0.00, 1.05) m, at rest; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.46, 0.00, 0.61) m, at rest; touching nothing | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching nothing
0.25 s: lever1 at -0.7°, turning -5°/s; touching nothing | ball1 at (-0.27, 0.00, 0.75) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.45, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
0.50 s: lever1 at -21.4°, turning -175°/s; touching nothing | ball1 at (-0.28, 0.00, 0.40) m, moving 0.94 m/s (vx -0.08, vy -0.00, vz -0.94); touching nothing | cart1 at -0.123 m, moving -0.74 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.45, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
0.75 s: lever1 at -45.1°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.299 m, moving -0.67 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.45, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
1.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.436 m, moving -0.14 m/s; touching domino1 | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, moving 0.23 m/s (vx -0.22, vy +0.00, vz +0.06), turned 3° from how it started; touching cart1, domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
1.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.445 m, moving +0.03 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.49, 0.00, 0.62) m, at rest, turned 10° from how it started; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
1.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.423 m, moving +0.14 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
1.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.390 m, moving +0.13 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
2.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.360 m, moving +0.11 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
2.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.333 m, moving +0.10 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
2.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.309 m, moving +0.09 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
2.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.286 m, moving +0.08 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
3.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.266 m, moving +0.08 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
3.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.248 m, moving +0.07 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
3.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.232 m, moving +0.06 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
3.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.217 m, moving +0.06 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
4.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.203 m, moving +0.05 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
4.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.191 m, moving +0.05 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
4.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.180 m, moving +0.04 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
4.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.170 m, moving +0.04 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
5.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.161 m, moving +0.03 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
5.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.153 m, moving +0.03 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
5.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.145 m, moving +0.03 m/s; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
5.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.144 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
6.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.146 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
6.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.148 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
6.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.150 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
6.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.152 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
7.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.153 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
7.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.155 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
7.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.156 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
7.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.157 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
8.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.158 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
8.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.159 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
8.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.160 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
8.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.161 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
(the same through 9.00 s)
9.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.162 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
9.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.163 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
(the same through 9.75 s)
10.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.164 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
(the same through 10.50 s)
10.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.165 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
(the same through 11.25 s)
11.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base | cart1 at -0.166 m, still; touching nothing | ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck | domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support
(the same through 12.00 s)

At the end (12.00 s):
- lever1 at -45.0°, still; touching ball1
- ball1 at (-0.26, 0.00, 0.27) m, at rest; touching lever1, lever1.lever scoop back, lever1.lever scoop base
- cart1 at -0.166 m, still; touching nothing
- ball2 at (-0.64, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1_deck
- domino1 at (-0.47, 0.00, 0.61) m, at rest; touching domino support
- door1 at 0.0°, still; touching nothing
- pendulum1 at 0.0°, still; touching nothing
- block1 at (-2.42, 0.00, 0.42) m, at rest; touching block support

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.21 m across, centre (-0.27, 0.00, 0.75) m
- ball1 comes down through ring1's height at 0.25 s, 0.00 m from its centre: through it
</history>
