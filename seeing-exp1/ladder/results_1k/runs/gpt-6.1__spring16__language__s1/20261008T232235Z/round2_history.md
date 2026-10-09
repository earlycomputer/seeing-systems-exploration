Before the run, at the start:
- ball5 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 0.05 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-4.98, 0.00, 0.56) m, at rest
- cart1: free body; its geoms: cart1; starts at (-5.64, 0.00, 0.56) m, at rest
- cart1 spring pusher: hinge joint cart1_spring_hinge about axis (0.00, 1.00, 0.00), range 0° to 22.9183° as MuJoCo applies it; its geoms: cart1 spring pusher; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: pendulum1, pendulum1 rod; starts at 0.0°, still
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range 0° to 70° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (-3.19, 0.00, 0.06) m, at rest
- domino1: free body; its geoms: domino1; starts at (-2.79, 0.00, 0.12) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1 striker; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (-2.03, 0.00, 1.07) m, at rest
- cart2: free body; its geoms: cart2, cart2 rear foot, cart2 front foot, cart2 front bumper; starts at (-2.09, 0.00, 0.39) m, at rest
- domino2: free body; its geoms: domino2; starts at (-1.53, 0.00, 0.47) m, at rest
- ball3: free body; its geoms: ball3; starts at (-1.35, 0.00, 0.56) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 60.0001° as MuJoCo applies it; its geoms: flap1, flap1 striker; starts at 0.0°, still
- pendulum2: hinge joint pendulum2_hinge about axis (0.00, 1.00, 0.00), range -38° to 0° as MuJoCo applies it; its geoms: pendulum2, pendulum2 rod; starts at 0.0°, still
- ball4: free body; its geoms: ball4; starts at (0.08, 0.00, 0.90) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw1; starts at 0.0°, still
- ball5: free body; its geoms: ball5; starts at (1.06, 0.00, 0.35) m, at rest

What happened, in order:
 0.00 s  seesaw1 starts touching ball5
 0.00 s  cart2 front foot starts touching cart2 track
 0.00 s  cart1 starts touching cart1 right track
 0.00 s  ball1 starts touching ramp1_deck
 0.00 s  cart2 rear foot starts touching cart2 track
 0.00 s  ball3 starts touching ramp2_deck
 0.00 s  domino1 starts touching floor
 0.00 s  cart1 starts touching cart1 left track
 0.00 s  domino2 starts touching domino2 pedestal
 0.00 s  ball3 starts touching ball3 starting ledge
 0.00 s  block1 starts touching floor
 0.00 s  ball1 starts touching ball1 starting ledge
 0.00 s  cart1 spring pusher starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  pendulum2 starts at its 0° stop (the end where it sits lower)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +52°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +52°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +52°/s
 0.00 s  cart1 spring pusher reaches its lower stop 282 more times
 0.00 s  lever1 reaches its 0° stop (neither end sits lower) again moving -21886°/s
 0.00 s  lever1 reaches its 0° stop (neither end sits lower) again moving -21886°/s
 0.00 s  lever1 reaches its 0° stop (neither end sits lower) again moving -21886°/s
 0.00 s  lever1 reaches its upper stop 282 more times
 0.00 s  ball2 comes to rest at (-2.03, 0.00, 1.07) m
 0.00 s  ball4 first touches shelf1
 0.00 s  lever1 first touches ball2
 0.01 s  cart1 first touches cart1 spring pusher
 0.01 s  cart1 starts moving
 0.02 s  cart2 first touches cart2 track
 0.02 s  ball1 leaves ramp1_deck
 0.02 s  ball3 leaves ramp2_deck
 0.02 s  cart2 front foot leaves cart2 track
 0.02 s  cart2 front foot leaves cart2 track
 0.02 s  cart2 front foot leaves cart2 track
 0.02 s  cart2 front foot leaves cart2 track
 0.02 s  cart2 starts moving
 0.04 s  lever1 is at its largest, 0.0°
 0.05 s  cart1 is still moving at the end, 0.35 m/s
 0.05 s  cart2 is still moving at the end, 0.06 m/s
 0.05 s  seesaw1 is at its largest, 0.0°
 0.06 s  pendulum2 is at its largest, 0.0°
 0.06 s  cart2 front foot touches cart2 track again
 0.06 s  cart2 front foot touches cart2 track again
 0.06 s  cart2 front foot touches cart2 track again
 0.06 s  cart2 front foot touches cart2 track 282 more times between 0.06 s and 0.02 s
 0.06 s  lever1 first touches cart2 rear foot
 0.06 s  lever1 first touches cart2
 0.06 s  ball2 starts moving
 0.07 s  cart2 rear foot first touches floor
 0.07 s  cart2 first touches floor
 0.07 s  cart2 front bumper first touches floor
 0.07 s  cart2 front foot first touches floor
 0.07 s  cart1 spring pusher is at its largest, 2.1°
 0.07 s  lever1 is at its smallest, -264.1°
 0.07 s  flap1 is at its smallest, -0.0°
 0.07 s  lever1 passes 0.11 m from ring1 (ring1_07) without touching it: nearest points (-2.31, 0.00, 0.76) m and (-2.20, 0.00, 0.75) m
 0.07 s  lever1 passes 0.15 m from cart2 left guide without touching it: nearest points (-2.32, 0.05, 0.70) m and (-2.32, 0.09, 0.56) m
 0.07 s  lever1 passes 0.15 m from cart2 right guide without touching it: nearest points (-2.32, -0.05, 0.70) m and (-2.32, -0.09, 0.56) m

State every 0.25 s:
0.00 s: ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge, ramp1_deck | cart1 at (-5.64, 0.00, 0.56) m, at rest; touching cart1 left track, cart1 right track | cart1 spring pusher at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (-3.19, 0.00, 0.06) m, at rest; touching floor | domino1 at (-2.79, 0.00, 0.12) m, at rest; touching floor | lever1 at 0.0°, still; touching nothing | ball2 at (-2.03, 0.00, 1.07) m, at rest; touching nothing | cart2 at (-2.09, 0.00, 0.39) m, at rest; touching cart2 track | domino2 at (-1.53, 0.00, 0.47) m, at rest; touching domino2 pedestal | ball3 at (-1.35, 0.00, 0.56) m, at rest; touching ball3 starting ledge, ramp2_deck | flap1 at 0.0°, still; touching nothing | pendulum2 at 0.0°, still; touching nothing | ball4 at (0.08, 0.00, 0.90) m, at rest; touching nothing | seesaw1 at 0.0°, still; touching ball5 | ball5 at (1.06, 0.00, 0.35) m, at rest; touching seesaw1

At the end (0.05 s):
- ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge
- cart1 at (-5.63, 0.00, 0.56) m, moving 0.35 m/s (vx +0.35, vy -0.00, vz -0.01); touching cart1 left track, cart1 right track, cart1 spring pusher
- cart1 spring pusher at 1.2°, turning +37°/s; touching cart1
- pendulum1 at 0.0°, still; touching nothing
- door1 at 0.0°, still; touching nothing
- block1 at (-3.19, 0.00, 0.06) m, at rest; touching floor
- domino1 at (-2.79, 0.00, 0.12) m, at rest; touching floor
- lever1 at 0.0°, still; touching ball2
- ball2 at (-2.03, 0.00, 1.07) m, at rest; touching lever1
- cart2 at (-2.09, 0.00, 0.39) m, moving 0.06 m/s (vx -0.00, vy -0.00, vz -0.06); touching cart2 track
- domino2 at (-1.53, 0.00, 0.47) m, at rest; touching domino2 pedestal
- ball3 at (-1.35, 0.00, 0.56) m, at rest; touching ball3 starting ledge
- flap1 at -0.0°, still; touching nothing
- pendulum2 at 0.0°, still; touching nothing
- ball4 at (0.08, 0.00, 0.90) m, at rest; touching shelf1
- seesaw1 at 0.0°, still; touching ball5
- ball5 at (1.06, 0.00, 0.35) m, at rest; touching seesaw1

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.20 m across, centre (-2.10, 0.00, 0.75) m
- cart2 comes down through ring1's height at 0.06 s, 0.01 m from its centre: through it (down through that height 570 times; this is the closest)
ring2: an opening 0.20 m across, centre (0.40, 0.00, 0.60) m
- cart2 comes down through ring2's height at 0.06 s, 2.50 m from its centre: outside it, missing by 2.40 m (down through that height 570 times; this is the closest)
</history>
