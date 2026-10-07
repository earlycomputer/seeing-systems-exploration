MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- trigger: free body; its geoms: trigger_ball; starts at (-0.65, 0.00, 2.72) m, at rest
- wedge: slide joint wedge_slide about axis (0.00, 0.00, -1.00), range 0 m to 0.32 m as MuJoCo applies it; its geoms: wedge_ramp, wedge_cap, wedge_post_left, wedge_post_right; starts at 0.000 m, still
- cart: slide joint cart_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.38 m as MuJoCo applies it; its geoms: cart_follower, cart_beam, cart_striker; starts at 0.000 m, still
- block: free body; its geoms: block_ball; starts at (0.17, 0.00, 1.24) m, at rest

What happened, in order:
 0.00 s  wedge starts at its lower stop (0 m)
 0.00 s  cart starts at its lower stop (0 m)
 0.00 s  block_ball first touches ledge_deck
 0.01 s  trigger starts moving
 0.32 s  trigger_ball first touches wedge_cap
 0.33 s  wedge_ramp first touches cart_follower
 0.35 s  block_ball leaves ledge_deck
 0.35 s  cart_striker first touches block_ball
 0.35 s  block starts moving
 0.36 s  wedge_ramp leaves cart_follower
 0.36 s  cart_striker leaves block_ball
 0.39 s  block is at the top of its flight, at (0.24, 0.00, 1.24) m
 0.40 s  wedge_ramp touches cart_follower again
 0.64 s  wedge_ramp leaves cart_follower
 0.65 s  wedge reaches its upper stop (0.32 m) moving +0.45 m/s
 0.66 s  wedge passes 0.27 m from ledge (ledge_deck) without touching it: nearest points (-0.13, 0.12, 1.35) m and (0.06, 0.12, 1.16) m
 0.66 s  wedge is at its largest, 0.3 m
 0.67 s  trigger comes to rest at (-0.65, 0.00, 1.90) m
 0.86 s  block_ball first touches box_bottom
 0.88 s  block_ball leaves box_bottom
 0.94 s  block is at the top of its flight, at (1.13, 0.00, 0.19) m
 1.01 s  block_ball touches box_bottom again
 1.45 s  block_ball leaves box_bottom
 1.46 s  block_ball first touches box_wall_right
 1.47 s  block_ball leaves box_wall_right
 1.51 s  block_ball touches box_bottom again
 1.51 s  block comes to rest at (1.63, 0.00, 0.16) m
 6.00 s  cart is at its largest, 0.3 m

State every 0.25 s:
0.00 s: trigger at (-0.65, 0.00, 2.72) m, at rest; touching nothing | wedge at 0.000 m, still; touching nothing | cart at 0.000 m, still; touching nothing | block at (0.17, 0.00, 1.24) m, at rest; touching nothing
0.25 s: trigger at (-0.65, 0.00, 2.42) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | wedge at 0.000 m, still; touching nothing | cart at 0.000 m, still; touching nothing | block at (0.17, 0.00, 1.23) m, at rest; touching ledge_deck
0.50 s: trigger at (-0.65, 0.00, 2.00) m, moving 0.81 m/s (vx -0.00, vy -0.00, vz -0.81); touching wedge_cap | wedge at 0.226 m, moving +0.81 m/s; touching trigger_ball | cart at 0.201 m, moving +0.82 m/s; touching nothing | block at (0.43, 0.00, 1.19) m, moving 2.01 m/s (vx +1.69, vy +0.00, vz -1.08); touching nothing
0.75 s: trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap | wedge at 0.320 m, still; touching trigger_ball | cart at 0.322 m, moving +0.20 m/s; touching nothing | block at (0.85, 0.00, 0.61) m, moving 3.92 m/s (vx +1.69, vy +0.00, vz -3.53); touching nothing
1.00 s: trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap | wedge at 0.320 m, still; touching trigger_ball | cart at 0.341 m, still; touching nothing | block at (1.18, 0.00, 0.17) m, moving 1.18 m/s (vx +1.05, vy +0.00, vz -0.55); touching nothing
1.25 s: trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap | wedge at 0.320 m, still; touching trigger_ball | cart at 0.341 m, still; touching nothing | block at (1.44, 0.00, 0.17) m, moving 0.99 m/s (vx +0.99, vy +0.00, vz -0.01); touching nothing
1.50 s: trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap | wedge at 0.320 m, still; touching trigger_ball | cart at 0.341 m, still; touching nothing | block at (1.63, 0.00, 0.17) m, moving 0.21 m/s (vx -0.13, vy +0.00, vz -0.17); touching nothing
1.75 s: trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap | wedge at 0.320 m, still; touching trigger_ball | cart at 0.341 m, still; touching nothing | block at (1.62, 0.00, 0.16) m, at rest; touching box_bottom
(the same through 6.00 s)

At the end (6.00 s):
- trigger at (-0.65, 0.00, 1.90) m, at rest; touching wedge_cap
- wedge at 0.320 m, still; touching trigger_ball
- cart at 0.341 m, still; touching nothing
- block at (1.62, 0.00, 0.16) m, at rest; touching box_bottom
</history>
