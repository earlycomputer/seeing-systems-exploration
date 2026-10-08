Before the run, at the start:
- ball retainer already touches ball1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 8 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 8.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.02, 0.00, 0.54) m, at rest
- ball retainer: hinge joint ball_retainer_hinge about axis (0.00, 1.00, 0.00), range 0° to 29° as MuJoCo applies it; its geoms: ball retainer; starts at 0.0°, still
- cart1: free body; its geoms: cart1; starts at (-0.12, 0.00, 1.12) m, at rest
- cart pusher arm: hinge joint cart_spring_hinge about axis (0.00, 1.00, 0.00), range -26.5651° to 0° as MuJoCo applies it; its geoms: cart pusher arm, cart pusher arm.cart pusher tip; starts at -26.6°, still
- pendulum1: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: pendulum1; starts at 0.0°, still
- door1: hinge joint door_hinge about axis (0.00, 0.00, 1.00), range -70° to 0° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (1.94, -0.09, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching ball retainer
 0.00 s  block1 starts touching floor
 0.00 s  ball retainer starts at its 0° stop (the end where it sits higher)
 0.00 s  cart pusher arm starts at its -26.5651° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  ball1 first touches ramp1
 0.00 s  cart1 first touches cart pusher arm.cart pusher tip
 0.00 s  cart1 starts moving
 0.01 s  ball retainer is at its smallest, -0.0°
 0.08 s  ball retainer is at its largest, 0.0°
 0.09 s  cart1 first touches cart far guide
 0.10 s  cart1 leaves cart far guide
 0.16 s  cart1 leaves cart pusher arm.cart pusher tip
 0.17 s  cart pusher arm reaches its 0° stop (the end where it sits lower) moving +248°/s
 0.18 s  cart1 touches cart far guide again
 0.18 s  cart1 leaves cart far guide
 0.19 s  cart pusher arm is at its largest, 1.6°
 0.20 s  ball1 passes 0.38 m from cart pusher arm (cart pusher arm.cart pusher tip) without touching it: nearest points (0.01, 0.00, 0.59) m and (-0.08, 0.00, 0.96) m
 0.20 s  ball retainer passes 0.44 m from cart pusher arm (cart pusher arm.cart pusher tip) without touching it: nearest points (0.08, 0.00, 0.55) m and (-0.07, 0.00, 0.96) m
 0.20 s  cart pusher arm passes 0.48 m from ramp1 without touching it: nearest points (-0.08, 0.00, 0.96) m and (0.00, 0.00, 0.49) m
 0.24 s  cart pusher arm reaches its 0° stop (the end where it sits lower) again moving -18°/s
 0.25 s  cart1 first touches cart near guide
 0.25 s  cart1 leaves cart near guide
 0.36 s  ball1 passes 0.01 m from cart1 without touching it: nearest points (-0.03, 0.00, 0.54) m and (-0.04, 0.00, 0.54) m
 0.36 s  ball retainer passes 0.11 m from cart1 without touching it: nearest points (0.07, 0.00, 0.54) m and (-0.04, 0.00, 0.54) m
 0.38 s  cart1 passes 0.04 m from ramp1 without touching it: nearest points (-0.04, 0.09, 0.48) m and (0.00, 0.09, 0.47) m
 0.45 s  cart1 first touches floor
 0.65 s  cart1 comes to rest at (-0.10, 0.00, 0.11) m

State every 0.25 s:
0.00 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer | ball retainer at 0.0°, still; touching ball1 | cart1 at (-0.12, 0.00, 1.12) m, at rest; touching nothing | cart pusher arm at -26.6°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.25 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer, ramp1 | ball retainer at 0.0°, still; touching ball1 | cart1 at (-0.14, 0.00, 0.76) m, moving 2.61 m/s (vx -0.41, vy +0.00, vz -2.58), turned 43° from how it started; touching nothing | cart pusher arm at 0.4°, turning -13°/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.50 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer, ramp1 | ball retainer at 0.0°, still; touching ball1 | cart1 at (-0.10, 0.00, 0.10) m, moving 0.29 m/s (vx +0.08, vy +0.00, vz +0.28), turned 90° from how it started; touching floor | cart pusher arm at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
0.75 s: ball1 at (0.02, 0.00, 0.54) m, at rest; touching ball retainer, ramp1 | ball retainer at -0.0°, still; touching ball1 | cart1 at (-0.10, 0.00, 0.11) m, at rest, turned 90° from how it started; touching floor | cart pusher arm at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
(the same through 7.75 s)
8.00 s: ball1 at (0.02, 0.01, 0.54) m, at rest; touching ball retainer, ramp1 | ball retainer at -0.0°, still; touching ball1 | cart1 at (-0.10, 0.00, 0.11) m, at rest, turned 90° from how it started; touching floor | cart pusher arm at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (1.94, -0.09, 0.06) m, at rest; touching floor

At the end (8.00 s):
- ball1 at (0.02, 0.01, 0.54) m, at rest; touching ball retainer, ramp1
- ball retainer at -0.0°, still; touching ball1
- cart1 at (-0.10, 0.00, 0.11) m, at rest, turned 90° from how it started; touching floor
- cart pusher arm at 0.0°, still; touching nothing
- pendulum1 at 0.0°, still; touching nothing
- door1 at 0.0°, still; touching nothing
- block1 at (1.94, -0.09, 0.06) m, at rest; touching floor
</history>
