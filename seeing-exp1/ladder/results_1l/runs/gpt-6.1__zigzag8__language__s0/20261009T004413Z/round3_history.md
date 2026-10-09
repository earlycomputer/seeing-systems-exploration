MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever1: hinge joint lever_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1.lever striker, lever1.lever retaining lip; starts at 0.0°, still
- ball1: free body; its geoms: ball1; starts at (-0.27, -0.15, 0.86) m, at rest
- cart1: slide joint cart_track about axis (1.00, 0.00, 0.00), range -0.5 m to 0 m as MuJoCo applies it; its geoms: cart1; starts at 0.000 m, still
- domino1: free body; its geoms: domino1; starts at (-0.46, -0.15, 0.42) m, at rest
- ball2: free body; its geoms: ball2; starts at (-0.64, -0.15, 0.54) m, at rest
- door latch: slide joint door_release_slide about axis (0.00, 0.00, 1.00), range -0.025 m to 0 m as MuJoCo applies it; its geoms: door latch, door latch.door release bridge, door latch.door release paddle; starts at 0.000 m, still
- door1: hinge joint door_hinge about axis (0.00, 0.00, 1.00), range -70° to 0° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- pendulum1: hinge joint pendulum_hinge about axis (1.00, 0.00, 0.00), range 0° to 38° as MuJoCo applies it; its geoms: pendulum1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (-2.02, 0.38, 0.26) m, at rest

What happened, in order:
 0.00 s  ball2 starts touching ramp ball retainer
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 starts at its upper stop (0 m)
 0.00 s  cart1 is at its largest at the start, 0.0 m
 0.00 s  door latch starts at its upper stop (0 m)
 0.00 s  door1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  door latch first touches door1
 0.00 s  door latch leaves door1
 0.00 s  ball2 first touches ramp1
 0.00 s  block1 first touches block plinth
 0.00 s  domino1 first touches domino plinth
 0.01 s  ball1 starts moving
 0.06 s  door latch is at its smallest, -0.0 m
 0.08 s  door1 first touches pendulum1
 0.10 s  door latch reaches its upper stop (0 m) again moving +0.14 m/s
 0.10 s  door1 leaves pendulum1
 0.14 s  door latch is at its largest, 0.0 m
 0.21 s  door1 touches pendulum1 again
 0.22 s  door1 leaves pendulum1
 0.24 s  door1 reaches its -70° stop (neither end sits lower) moving -95°/s
 0.25 s  ball1 passes 0.03 m from ring1 (ring1_09) without touching it: nearest points (-0.31, -0.18, 0.56) m and (-0.34, -0.19, 0.56) m
 0.25 s  ball1 passes 0.27 m from ball2 without touching it: nearest points (-0.32, -0.15, 0.55) m and (-0.59, -0.15, 0.54) m
 0.26 s  pendulum1 reaches its 38° stop (the end where it sits higher) moving +186°/s
 0.26 s  door1 passes 0.17 m from block1 without touching it: nearest points (-1.90, 0.15, 0.20) m and (-1.96, 0.32, 0.20) m
 0.26 s  pendulum1 first touches block1
 0.26 s  block1 starts moving
 0.27 s  door1 is at its smallest, -70.6°
 0.27 s  ball1 passes 0.23 m from cart1 without touching it: nearest points (-0.22, -0.15, 0.50) m and (0.01, -0.15, 0.50) m
 0.27 s  door1 passes 0.10 m from block plinth without touching it: nearest points (-1.87, 0.16, 0.20) m and (-1.91, 0.26, 0.20) m
 0.28 s  pendulum1 is at its largest, 38.9°
 0.28 s  pendulum1 leaves block1
 0.28 s  ball1 passes 0.33 m from ramp ball retainer without touching it: nearest points (-0.32, -0.15, 0.47) m and (-0.65, -0.15, 0.48) m
 0.28 s  door1 reaches its -70° stop (neither end sits lower) again moving +11°/s
 0.29 s  ball1 passes 0.28 m from ramp1 without touching it: nearest points (-0.32, -0.15, 0.45) m and (-0.60, -0.15, 0.45) m
 0.30 s  pendulum1 reaches its 38° stop (the end where it sits higher) again moving -27°/s
 0.32 s  block1 comes to rest at (-2.02, 0.39, 0.26) m
 0.33 s  lever1 is at its largest, 0.0°
 0.34 s  lever1 first touches ball1
 0.34 s  ball1 passes 0.09 m from domino1 without touching it: nearest points (-0.32, -0.15, 0.30) m and (-0.42, -0.15, 0.30) m
 0.36 s  lever1 leaves ball1
 0.39 s  lever1.lever striker first touches cart1
 0.39 s  door1 touches pendulum1 again
 0.39 s  lever1 touches ball1 again
 0.40 s  door1 leaves pendulum1
 0.40 s  lever1.lever striker leaves cart1
 0.41 s  lever1 leaves ball1
 0.42 s  pendulum1 passes 0.02 m from block plinth without touching it: nearest points (-2.02, 0.25, 0.21) m and (-2.02, 0.26, 0.20) m
 0.44 s  lever1.lever retaining lip first touches ball1
 0.44 s  ball1 passes 0.04 m from domino plinth without touching it: nearest points (-0.34, -0.15, 0.19) m and (-0.38, -0.15, 0.19) m
 0.44 s  door1 touches pendulum1 again
 0.51 s  lever1 touches ball1 again
 0.55 s  lever1 reaches its -45° stop (neither end sits lower) moving -219°/s
 0.57 s  lever1 is at its smallest, -46.6°
 0.62 s  lever1 reaches its -45° stop (neither end sits lower) again moving +17°/s
 0.63 s  ball1 comes to rest at (-0.25, -0.15, 0.09) m
 0.65 s  cart1 passes 0.04 m from ring1 (ring1_00) without touching it: nearest points (-0.18, -0.15, 0.51) m and (-0.18, -0.15, 0.55) m
 1.00 s  cart1 first touches domino1
 1.00 s  domino1 starts moving
 1.02 s  cart1 leaves domino1
 1.15 s  cart1 touches domino1 again
 1.15 s  cart1 leaves domino1
 1.24 s  ball2 leaves ramp1
 1.24 s  domino1 first touches ball2
 1.25 s  domino1 comes to rest at (-0.51, -0.15, 0.43) m
 1.27 s  cart1 touches domino1 again
 1.27 s  cart1 passes 0.13 m from ball2 without touching it: nearest points (-0.46, -0.15, 0.51) m and (-0.59, -0.15, 0.53) m
 1.27 s  cart1 passes 0.15 m from ramp1 without touching it: nearest points (-0.46, -0.09, 0.45) m and (-0.60, -0.09, 0.45) m
 1.27 s  cart1 passes 0.19 m from ramp ball retainer without touching it: nearest points (-0.46, -0.06, 0.48) m and (-0.65, -0.06, 0.48) m
 1.27 s  cart1 is at its smallest, -0.5 m
 1.29 s  cart1 leaves domino1
 1.35 s  ball2 touches ramp1 again
 1.36 s  domino1 leaves ball2
 1.36 s  cart1 passes 0.11 m from domino plinth without touching it: nearest points (-0.41, -0.08, 0.41) m and (-0.41, -0.08, 0.30) m
 1.46 s  domino1 touches ball2 again

State every 0.25 s:
0.00 s: lever1 at 0.0°, still; touching nothing | ball1 at (-0.27, -0.15, 0.86) m, at rest; touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (-0.46, -0.15, 0.42) m, at rest; touching nothing | ball2 at (-0.64, -0.15, 0.54) m, at rest; touching ramp ball retainer | door latch at 0.000 m, still; touching nothing | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.02, 0.38, 0.26) m, at rest; touching nothing
0.25 s: lever1 at 0.0°, still; touching nothing | ball1 at (-0.27, -0.15, 0.56) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (-0.46, -0.15, 0.42) m, at rest; touching domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -70.2°, turning -76°/s; touching nothing | pendulum1 at 36.2°, turning +194°/s; touching nothing | block1 at (-2.02, 0.38, 0.26) m, at rest; touching block plinth
0.50 s: lever1 at -34.9°, turning -177°/s; touching ball1 | ball1 at (-0.27, -0.15, 0.14) m, moving 1.02 m/s (vx +0.39, vy +0.00, vz -0.95); touching lever1.lever retaining lip | cart1 at -0.084 m, moving -0.74 m/s; touching nothing | domino1 at (-0.46, -0.15, 0.42) m, at rest; touching domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.7°, turning +28°/s; touching nothing | pendulum1 at 25.2°, turning -57°/s; touching nothing | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
0.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.260 m, moving -0.67 m/s; touching nothing | domino1 at (-0.46, -0.15, 0.42) m, at rest; touching domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -63.3°, turning -5°/s; touching pendulum1 | pendulum1 at 22.7°, turning +6°/s; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
1.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.419 m, moving -0.61 m/s; touching nothing | domino1 at (-0.46, -0.15, 0.42) m, at rest; touching domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.1°, still; touching pendulum1 | pendulum1 at 24.1°, turning +2°/s; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
1.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.462 m, moving -0.11 m/s; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.64, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer | door latch at 0.000 m, still; touching nothing | door1 at -64.2°, still; touching pendulum1 | pendulum1 at 24.3°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
1.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.461 m, moving +0.01 m/s; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.2°, still; touching pendulum1 | pendulum1 at 24.4°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
1.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.458 m, moving +0.01 m/s; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.3°, still; touching pendulum1 | pendulum1 at 24.5°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
2.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.455 m, moving +0.01 m/s; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.4°, still; touching pendulum1 | pendulum1 at 24.6°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
2.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.453 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.4°, still; touching pendulum1 | pendulum1 at 24.7°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
2.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.450 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.5°, still; touching pendulum1 | pendulum1 at 24.8°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
2.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.448 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.5°, still; touching pendulum1 | pendulum1 at 24.9°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
3.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.446 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.6°, still; touching pendulum1 | pendulum1 at 25.0°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
3.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.444 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.6°, still; touching pendulum1 | pendulum1 at 25.1°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
3.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.443 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.6°, still; touching pendulum1 | pendulum1 at 25.1°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
3.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.441 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.7°, still; touching pendulum1 | pendulum1 at 25.2°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
4.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.440 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.7°, still; touching pendulum1 | pendulum1 at 25.3°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
4.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.439 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.8°, still; touching pendulum1 | pendulum1 at 25.3°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
4.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.438 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.8°, still; touching pendulum1 | pendulum1 at 25.4°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
4.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.437 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.8°, still; touching pendulum1 | pendulum1 at 25.4°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
5.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.436 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.8°, still; touching pendulum1 | pendulum1 at 25.5°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
5.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.435 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.9°, still; touching pendulum1 | pendulum1 at 25.5°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
5.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.435 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.9°, still; touching pendulum1 | pendulum1 at 25.6°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
5.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.434 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.9°, still; touching pendulum1 | pendulum1 at 25.6°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
6.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.433 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -64.9°, still; touching pendulum1 | pendulum1 at 25.6°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
6.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.433 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.0°, still; touching pendulum1 | pendulum1 at 25.7°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
6.50 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.432 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.0°, still; touching pendulum1 | pendulum1 at 25.7°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 6.75 s)
7.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.432 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.0°, still; touching pendulum1 | pendulum1 at 25.8°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
7.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.431 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.0°, still; touching pendulum1 | pendulum1 at 25.8°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 7.50 s)
7.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.431 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.1°, still; touching pendulum1 | pendulum1 at 25.9°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
8.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.430 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.1°, still; touching pendulum1 | pendulum1 at 25.9°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 8.75 s)
9.00 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.430 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.1°, still; touching pendulum1 | pendulum1 at 26.0°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
9.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.429 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.1°, still; touching pendulum1 | pendulum1 at 26.0°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 10.00 s)
10.25 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.429 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.2°, still; touching pendulum1 | pendulum1 at 26.0°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 10.50 s)
10.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.429 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.2°, still; touching pendulum1 | pendulum1 at 26.1°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 11.50 s)
11.75 s: lever1 at -45.0°, still; touching ball1 | ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip | cart1 at -0.428 m, still; touching nothing | domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth | ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1 | door latch at 0.000 m, still; touching nothing | door1 at -65.2°, still; touching pendulum1 | pendulum1 at 26.1°, still; touching door1 | block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth
(the same through 12.00 s)

At the end (12.00 s):
- lever1 at -45.0°, still; touching ball1
- ball1 at (-0.25, -0.15, 0.09) m, at rest; touching lever1, lever1.lever retaining lip
- cart1 at -0.428 m, still; touching nothing
- domino1 at (-0.51, -0.15, 0.43) m, at rest, turned 21° from how it started; touching ball2, domino plinth
- ball2 at (-0.63, -0.15, 0.54) m, at rest; touching domino1, ramp ball retainer, ramp1
- door latch at 0.000 m, still; touching nothing
- door1 at -65.2°, still; touching pendulum1
- pendulum1 at 26.1°, still; touching door1
- block1 at (-2.02, 0.39, 0.26) m, at rest; touching block plinth

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.20 m across, centre (-0.27, -0.15, 0.56) m
- ball1 comes down through ring1's height at 0.25 s, 0.00 m from its centre: through it
</history>
