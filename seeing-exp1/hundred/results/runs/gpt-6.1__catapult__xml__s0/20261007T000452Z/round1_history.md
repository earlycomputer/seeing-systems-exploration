MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -17.1887° to 60.1606° as MuJoCo applies it; its geoms: pendulum_rod, pendulum_striker; starts at 53.1°, still
- cart: slide joint cart_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.24 m as MuJoCo applies it; its geoms: cart_block; starts at 0.000 m, still
- weight: free body; its geoms: weight_block; starts at (-1.03, 0.00, 2.04) m, at rest
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range 20.0535° to 42.9718° as MuJoCo applies it; its geoms: seesaw_beam, seesaw_weight_pad, seesaw_weight_inner_wall, seesaw_weight_front_wall, seesaw_weight_back_wall, seesaw_ball_outer_lip, seesaw_ball_inner_lip, seesaw_ball_front_lip, seesaw_ball_back_lip; starts at 43.0°, still
- ball: free body; its geoms: ball_sphere; starts at (0.77, 0.00, 0.48) m, at rest

What happened, in order:
 0.00 s  weight_block starts touching weight_shelf_top
 0.00 s  pendulum is at its largest at the start, 53.1°
 0.00 s  cart starts at its lower stop (0 m)
 0.00 s  seesaw starts at its upper stop (42.9718°)
 0.00 s  seesaw_ball_outer_lip first touches ball_sphere
 0.00 s  seesaw is at its largest, 43.0°
 0.01 s  ball starts moving
 0.02 s  seesaw_beam first touches ball_sphere
 0.02 s  ball comes to rest at (0.77, 0.00, 0.48) m
 0.66 s  pendulum_striker first touches cart_block
 0.67 s  cart_block first touches weight_block
 0.67 s  weight starts moving
 0.67 s  pendulum passes 0.39 m from weight (weight_block) without touching it: nearest points (-1.51, 0.00, 2.09) m and (-1.12, 0.00, 2.09) m
 0.69 s  weight_block leaves weight_shelf_top
 0.69 s  cart_block leaves weight_block
 0.70 s  pendulum_striker leaves cart_block
 0.72 s  weight_block touches weight_shelf_top again
 0.78 s  cart_block touches weight_block again
 0.80 s  pendulum_striker touches cart_block again
 0.84 s  cart is at its largest, 0.1 m
 0.84 s  pendulum passes 0.04 m from weight_shelf (weight_shelf_top) without touching it: nearest points (-1.54, 0.00, 1.98) m and (-1.52, 0.00, 1.95) m
 0.84 s  pendulum is at its smallest, -3.6°
 0.90 s  cart_block leaves weight_block
 0.91 s  pendulum_striker leaves cart_block
 0.94 s  weight comes to rest at (-0.99, 0.00, 2.04) m
 1.56 s  cart reaches its lower stop (0 m) again moving -0.06 m/s
 1.64 s  cart is at its smallest, -0.0 m
 2.76 s  pendulum_striker touches cart_block again
 2.78 s  pendulum_striker leaves cart_block
 3.03 s  cart_block touches weight_block again
 3.05 s  cart_block leaves weight_block

State every 0.25 s:
0.00 s: pendulum at 53.1°, still; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-1.03, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching nothing | ball at (0.77, 0.00, 0.48) m, at rest; touching nothing
0.25 s: pendulum at 43.9°, turning -72°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-1.03, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
0.50 s: pendulum at 18.9°, turning -122°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-1.03, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
0.75 s: pendulum at -3.1°, turning -9°/s; touching nothing | cart at 0.044 m, moving +0.29 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, moving 0.20 m/s (vx +0.17, vy -0.00, vz +0.11), turned 3° from how it started; touching nothing | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
1.00 s: pendulum at -3.0°, turning +6°/s; touching nothing | cart at 0.043 m, moving -0.08 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
1.25 s: pendulum at -1.1°, turning +9°/s; touching nothing | cart at 0.025 m, moving -0.07 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
1.50 s: pendulum at 1.3°, turning +9°/s; touching nothing | cart at 0.008 m, moving -0.06 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
1.75 s: pendulum at 3.1°, turning +5°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
2.00 s: pendulum at 3.7°, still; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
2.25 s: pendulum at 2.9°, turning -6°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
2.50 s: pendulum at 0.9°, turning -9°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
2.75 s: pendulum at -1.5°, turning -9°/s; touching nothing | cart at 0.000 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
3.00 s: pendulum at -2.6°, turning -3°/s; touching nothing | cart at 0.046 m, moving +0.19 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
3.25 s: pendulum at -2.7°, turning +2°/s; touching nothing | cart at 0.049 m, moving -0.01 m/s; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
3.50 s: pendulum at -1.8°, turning +6°/s; touching nothing | cart at 0.047 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
3.75 s: pendulum at -0.1°, turning +7°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
4.00 s: pendulum at 1.6°, turning +6°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
4.25 s: pendulum at 2.7°, turning +2°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
4.50 s: pendulum at 2.7°, turning -2°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
4.75 s: pendulum at 1.6°, turning -6°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
5.00 s: pendulum at -0.1°, turning -7°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
5.25 s: pendulum at -1.7°, turning -6°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
5.50 s: pendulum at -2.7°, turning -2°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
5.75 s: pendulum at -2.6°, turning +3°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
6.00 s: pendulum at -1.5°, turning +6°/s; touching nothing | cart at 0.046 m, still; touching nothing | weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top | seesaw at 43.0°, still; touching ball_sphere | ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam

At the end (6.00 s):
- pendulum at -1.5°, turning +6°/s; touching nothing
- cart at 0.046 m, still; touching nothing
- weight at (-0.99, 0.00, 2.04) m, at rest; touching weight_shelf_top
- seesaw at 43.0°, still; touching ball_sphere
- ball at (0.77, 0.00, 0.48) m, at rest; touching seesaw_ball_outer_lip, seesaw_beam
</history>
