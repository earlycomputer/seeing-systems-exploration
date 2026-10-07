MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (0.55, 0.00, 3.95) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, -1.00, 0.00), range -51.5662° to 0° as MuJoCo applies it; its geoms: flap1_plate, flap1_side_a, flap1_side_b, flap1_crossbar; starts at 0.0°, still
- flap1_retainer: hinge joint flap1_retainer_hinge about axis (0.00, -1.00, 0.00), range -10.3132° to 0° as MuJoCo applies it; its geoms: flap1_retainer.flap1_cam_tip, flap1_retainer.flap1_cam_01, flap1_retainer.flap1_cam_02, flap1_retainer.flap1_cam_03, flap1_retainer.flap1_cam_04, flap1_retainer.flap1_cam_05, flap1_retainer.flap1_cam_06, flap1_retainer.flap1_cam_07, flap1_retainer.flap1_cam_08, flap1_retainer.flap1_cam_09; starts at 0.0°, still
- block: free body; its geoms: block_box; starts at (0.00, 0.00, 2.68) m, at rest
- flap2: hinge joint flap2_hinge about axis (0.00, -1.00, 0.00), range -51.5662° to 0° as MuJoCo applies it; its geoms: flap2_plate, flap2_side_a, flap2_side_b, flap2_crossbar; starts at 0.0°, still
- flap2_retainer: hinge joint flap2_retainer_hinge about axis (0.00, -1.00, 0.00), range -10.3132° to 0° as MuJoCo applies it; its geoms: flap2_retainer.flap2_cam_tip, flap2_retainer.flap2_cam_01, flap2_retainer.flap2_cam_02, flap2_retainer.flap2_cam_03, flap2_retainer.flap2_cam_04, flap2_retainer.flap2_cam_05, flap2_retainer.flap2_cam_06, flap2_retainer.flap2_cam_07, flap2_retainer.flap2_cam_08; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (-0.55, 0.00, 1.68) m, at rest

What happened, in order:
 0.00 s  flap1_retainer.flap1_cam_07 starts touching block_box
 0.00 s  flap2_retainer.flap2_cam_06 starts touching ball2_sphere
 0.00 s  flap1_retainer.flap1_cam_06 starts touching block_box
 0.00 s  flap1 starts at its upper stop (0°)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  flap1_retainer starts at its upper stop (0°)
 0.00 s  flap2 starts at its upper stop (0°)
 0.00 s  flap2 is at its largest at the start, 0.0°
 0.00 s  flap2_retainer starts at its upper stop (0°)
 0.00 s  flap2_retainer.flap2_cam_05 first touches ball2_sphere
 0.01 s  ball1 starts moving
 0.26 s  block_box first touches block_guides_xmm
 0.26 s  block_box first touches block_guides_xmp
 0.36 s  ball2_sphere first touches ball2_guides_mp
 0.36 s  ball2_sphere first touches ball2_guides_mm
 0.40 s  ball1 passes 0.06 m from hoop1 (hoop1_02) without touching it: nearest points (0.61, 0.06, 3.16) m and (0.65, 0.10, 3.15) m
 0.46 s  block_box first touches block_guides_xpm
 0.46 s  block_box first touches block_guides_xpp
 0.52 s  ball1 passes 0.41 m from block (block_box) without touching it: nearest points (0.47, 0.00, 2.62) m and (0.05, 0.00, 2.61) m
 0.53 s  ball1 passes 0.31 m from flap1_retainer (flap1_retainer.flap1_cam_09) without touching it: nearest points (0.47, 0.00, 2.57) m and (0.15, 0.00, 2.57) m
 0.58 s  flap1_retainer.flap1_cam_07 leaves block_box
 0.58 s  block_box leaves block_guides_xmm
 0.58 s  block_box leaves block_guides_xmp
 0.58 s  block_box leaves block_guides_xpm
 0.58 s  block_box leaves block_guides_xpp
 0.58 s  ball1_sphere first touches flap1_plate
 0.59 s  block starts moving
 0.59 s  flap1_retainer.flap1_cam_05 first touches block_box
 0.60 s  flap1_retainer.flap1_cam_06 leaves block_box
 0.60 s  flap1_retainer.flap1_cam_05 leaves block_box
 0.60 s  ball1 passes 0.46 m from support_frame (support_frame_bearing_1a) without touching it: nearest points (0.47, -0.02, 2.21) m and (0.02, -0.12, 2.20) m
 0.61 s  ball1_sphere leaves flap1_plate
 0.62 s  block_box touches block_guides_xpm again
 0.62 s  block_box touches block_guides_xpp again
 0.62 s  block_box touches block_guides_xmm again
 0.62 s  block_box touches block_guides_xmp again
 0.63 s  block_box leaves block_guides_xmm
 0.63 s  block_box leaves block_guides_xmp
 0.63 s  flap1_retainer.flap1_cam_03 first touches block_box
 0.63 s  flap1_retainer.flap1_cam_04 first touches block_box
 0.63 s  flap1_retainer.flap1_cam_04 leaves block_box
 0.64 s  flap1_retainer is at its largest, 0.0°
 0.64 s  flap2_retainer.flap2_cam_06 leaves ball2_sphere
 0.65 s  flap1_retainer.flap1_cam_03 leaves block_box
 0.65 s  flap1_retainer.flap1_cam_02 first touches block_box
 0.66 s  flap1_retainer.flap1_cam_02 leaves block_box
 0.66 s  flap1_retainer.flap1_cam_01 first touches block_box
 0.67 s  flap1_retainer.flap1_cam_01 leaves block_box
 0.67 s  flap1_retainer.flap1_cam_tip first touches block_box
 0.67 s  flap1_retainer.flap1_cam_tip leaves block_box
 0.68 s  block_box leaves block_guides_xpm
 0.68 s  block_box leaves block_guides_xpp
 0.69 s  flap1 reaches its lower stop (-51.5662°) moving -449°/s
 0.69 s  flap1 is at its smallest, -52.4°
 0.70 s  flap1 reaches its lower stop (-51.5662°) again moving +98°/s
 0.70 s  ball1_sphere first touches ball1_guides_mp
 0.70 s  ball1_sphere leaves ball1_guides_mp
 0.70 s  ball1_sphere first touches ball1_guides_mm
 0.70 s  ball1_sphere leaves ball1_guides_mm
 0.70 s  flap1 passes 0.14 m from flap2 (flap2_plate) without touching it: nearest points (0.66, 0.03, 1.34) m and (0.55, 0.03, 1.25) m
 0.71 s  ball1_sphere first touches ball1_guides_pp
 0.71 s  ball1_sphere first touches ball1_guides_pm
 0.72 s  ball1_sphere touches flap1_plate again
 0.72 s  block_box touches block_guides_xmm again
 0.72 s  block_box touches block_guides_xmp again
 0.72 s  flap1 reaches its lower stop (-51.5662°) again moving -180°/s
 0.73 s  flap1_retainer reaches its lower stop (-10.3132°) moving -115°/s
 0.73 s  flap1_retainer passes 0.09 m from ball1_guides (ball1_guides_mm) without touching it: nearest points (0.40, 0.00, 2.25) m and (0.47, -0.06, 2.25) m
 0.73 s  ball1 passes 0.31 m from flap2 (flap2_plate) without touching it: nearest points (0.56, 0.00, 1.56) m and (0.55, 0.00, 1.25) m
 0.73 s  block_box leaves block_guides_xmm
 0.73 s  block_box leaves block_guides_xmp
 0.73 s  flap1_retainer is at its smallest, -10.8°
 0.74 s  ball1_sphere leaves flap1_plate
 0.74 s  flap1_retainer reaches its lower stop (-10.3132°) again moving -16°/s
 0.76 s  ball1_sphere touches ball1_guides_mp again
 0.76 s  ball1_sphere touches ball1_guides_mm again
 0.76 s  ball1_sphere leaves ball1_guides_mp
 0.76 s  ball1_sphere leaves ball1_guides_mm
 0.78 s  ball1_sphere leaves ball1_guides_pp
 0.78 s  ball1_sphere leaves ball1_guides_pm
 0.83 s  ball1_sphere touches ball1_guides_mp again
 0.83 s  ball1_sphere leaves ball1_guides_mp
 0.83 s  ball1_sphere touches ball1_guides_mm again
 0.83 s  ball1_sphere leaves ball1_guides_mm
 0.85 s  ball1_sphere touches ball1_guides_pp again
 0.85 s  ball1_sphere touches ball1_guides_pm again
 0.86 s  block_box touches block_guides_xmm again
 0.86 s  block_box leaves block_guides_xmm
 0.86 s  block_box touches block_guides_xmp again
 0.86 s  block_box leaves block_guides_xmp
 0.86 s  ball1_sphere leaves ball1_guides_pp
 0.86 s  ball1_sphere leaves ball1_guides_pm
 0.88 s  block_box touches block_guides_xpm again
 0.88 s  block_box leaves block_guides_xpm
 0.88 s  block_box touches block_guides_xpp again
 0.88 s  block_box leaves block_guides_xpp
 0.91 s  ball1_sphere touches ball1_guides_mp again
 0.91 s  ball1_sphere touches ball1_guides_mm again
 0.91 s  ball1_sphere leaves ball1_guides_mp
 0.91 s  ball1_sphere leaves ball1_guides_mm
 0.93 s  block_box touches block_guides_xpm again
 0.93 s  block_box leaves block_guides_xpm
 0.93 s  block_box touches block_guides_xpp again
 0.93 s  block_box leaves block_guides_xpp
 0.94 s  ball1_sphere touches ball1_guides_pp again
 0.94 s  ball1_sphere leaves ball1_guides_pp
 0.94 s  ball1_sphere touches ball1_guides_pm again
 0.94 s  ball1_sphere leaves ball1_guides_pm
 0.99 s  ball1_sphere touches ball1_guides_mp 2 more times between 0.99 s and 1.13 s
 0.99 s  ball1_sphere touches ball1_guides_mm 2 more times between 0.99 s and 1.13 s
 1.01 s  flap1 passes 0.09 m from block (block_box) without touching it: nearest points (0.05, -0.14, 2.14) m and (0.05, -0.05, 2.14) m
 1.01 s  block passes 0.05 m from support_frame (support_frame_bearing_1b) without touching it: nearest points (0.00, 0.05, 2.20) m and (0.00, 0.10, 2.20) m
 1.02 s  block_box touches block_guides_xmm 4 more times between 1.02 s and 1.43 s
 1.02 s  block_box touches block_guides_xmp 4 more times between 1.02 s and 1.43 s
 1.07 s  block_box touches block_guides_xpm 6 more times between 1.07 s and 6.00 s, still touching at the end
 1.07 s  block_box touches block_guides_xpp 6 more times between 1.07 s and 6.00 s, still touching at the end
 1.08 s  ball1_sphere touches flap1_plate again
 1.08 s  ball1_sphere touches ball1_guides_pp again
 1.08 s  ball1_sphere touches ball1_guides_pm again
 1.09 s  ball1_sphere leaves flap1_plate
 1.10 s  ball1_sphere leaves ball1_guides_pp
 1.10 s  ball1_sphere leaves ball1_guides_pm
 1.13 s  ball1 passes 0.40 m from block_guides (block_guides_xpp) without touching it: nearest points (0.46, 0.01, 1.67) m and (0.06, 0.03, 1.67) m
 1.14 s  block passes 0.36 m from flap2_retainer (flap2_retainer.flap2_cam_08) without touching it: nearest points (-0.05, 0.00, 1.57) m and (-0.41, 0.00, 1.58) m
 1.19 s  ball1_sphere touches ball1_guides_pp 1 more times between 1.19 s and 6.00 s, still touching at the end
 1.19 s  ball1_sphere touches ball1_guides_pm 1 more times between 1.19 s and 6.00 s, still touching at the end
 1.20 s  ball1_sphere touches flap1_plate again
 1.21 s  ball2_sphere leaves ball2_guides_mp
 1.21 s  ball2_sphere leaves ball2_guides_mm
 1.21 s  block_box first touches flap2_plate
 1.21 s  ball2 starts moving
 1.22 s  flap2_retainer is at its largest, 0.3°
 1.23 s  flap2_retainer.flap2_cam_05 leaves ball2_sphere
 1.23 s  flap2_retainer.flap2_cam_04 first touches ball2_sphere
 1.23 s  flap2_retainer.flap2_cam_04 leaves ball2_sphere
 1.24 s  block_box leaves flap2_plate
 1.25 s  ball1 comes to rest at (0.55, 0.00, 1.66) m
 1.26 s  ball2_sphere first touches ball2_guides_pm
 1.26 s  ball2_sphere first touches ball2_guides_pp
 1.29 s  flap2_retainer.flap2_cam_tip first touches ball2_sphere
 1.29 s  flap2_retainer.flap2_cam_01 first touches ball2_sphere
 1.30 s  flap2_retainer.flap2_cam_tip leaves ball2_sphere
 1.30 s  flap2_retainer.flap2_cam_01 leaves ball2_sphere
 1.30 s  ball2_sphere leaves ball2_guides_pm
 1.30 s  ball2_sphere leaves ball2_guides_pp
 1.30 s  block passes 0.36 m from hoop2 (hoop2_01) without touching it: nearest points (-0.05, 0.00, 0.95) m and (-0.41, 0.00, 0.95) m
 1.33 s  flap2 reaches its lower stop (-51.5662°) moving -377°/s
 1.33 s  flap2 is at its smallest, -51.8°
 1.33 s  ball2_sphere touches ball2_guides_mp again
 1.33 s  ball2_sphere touches ball2_guides_mm again
 1.34 s  ball2_sphere leaves ball2_guides_mp
 1.34 s  ball2_sphere leaves ball2_guides_mm
 1.37 s  block_box touches flap2_plate again
 1.37 s  flap2 passes 0.06 m from hoop2 (hoop2_12) without touching it: nearest points (-0.36, 0.00, 0.99) m and (-0.41, 0.00, 0.96) m
 1.37 s  flap2 passes 0.46 m from cup (cup_wall_xp) without touching it: nearest points (-0.04, 0.03, 0.58) m and (-0.40, 0.03, 0.30) m
 1.37 s  block passes 0.48 m from cup (cup_wall_xp) without touching it: nearest points (-0.05, -0.05, 0.62) m and (-0.40, -0.05, 0.30) m
 1.39 s  block_box leaves flap2_plate
 1.39 s  flap2_retainer reaches its lower stop (-10.3132°) moving -112°/s
 1.40 s  ball2_sphere touches ball2_guides_pm again
 1.40 s  ball2_sphere touches ball2_guides_pp again
 1.40 s  flap2_retainer passes 0.14 m from block_guides (block_guides_xmp) without touching it: nearest points (-0.20, 0.00, 1.29) m and (-0.06, 0.03, 1.29) m
 1.40 s  flap2_retainer passes 0.39 m from hoop2 (hoop2_01) without touching it: nearest points (-0.21, 0.00, 1.29) m and (-0.41, 0.00, 0.96) m
 1.40 s  flap2_retainer is at its smallest, -10.5°
 1.41 s  ball2_sphere leaves ball2_guides_pm
 1.41 s  ball2_sphere leaves ball2_guides_pp
 1.41 s  block passes 0.43 m from ball2_guides (ball2_guides_pm) without touching it: nearest points (-0.05, -0.05, 0.79) m and (-0.48, -0.06, 0.79) m
 1.51 s  ball2_sphere touches ball2_guides_mp again
 1.51 s  ball2_sphere leaves ball2_guides_mp
 1.51 s  ball2_sphere touches ball2_guides_mm again
 1.51 s  ball2_sphere leaves ball2_guides_mm
 1.54 s  ball2_sphere touches ball2_guides_pm again
 1.54 s  ball2_sphere touches ball2_guides_pp again
 1.54 s  ball2_sphere leaves ball2_guides_pm
 1.54 s  ball2_sphere leaves ball2_guides_pp
 1.57 s  ball2_sphere touches ball2_guides_mp again
 1.57 s  ball2_sphere touches ball2_guides_mm again
 1.57 s  ball2_sphere leaves ball2_guides_mp
 1.57 s  ball2_sphere leaves ball2_guides_mm
 1.58 s  ball2_sphere touches ball2_guides_pm again
 1.58 s  ball2_sphere touches ball2_guides_pp again
 1.59 s  block_box touches flap2_plate again
 1.59 s  ball2_sphere leaves ball2_guides_pm
 1.59 s  ball2_sphere leaves ball2_guides_pp
 1.62 s  ball2_sphere touches ball2_guides_mp 10 more times between 1.62 s and 2.08 s
 1.62 s  ball2_sphere touches ball2_guides_mm 10 more times between 1.62 s and 2.08 s
 1.65 s  ball2_sphere touches ball2_guides_pm 8 more times between 1.65 s and 2.05 s
 1.65 s  ball2_sphere touches ball2_guides_pp 8 more times between 1.65 s and 2.05 s
 1.65 s  block comes to rest at (0.00, 0.00, 0.71) m
 1.68 s  flap2 passes 0.07 m from ball2 (ball2_sphere) without touching it: nearest points (-0.55, -0.14, 1.25) m and (-0.55, -0.07, 1.25) m
 1.68 s  ball2 passes 0.03 m from support_frame (support_frame_bearing_2a) without touching it: nearest points (-0.55, -0.07, 1.25) m and (-0.55, -0.10, 1.25) m
 1.80 s  ball2 passes 0.04 m from hoop2 (hoop2_06) without touching it: nearest points (-0.62, 0.02, 0.95) m and (-0.66, 0.03, 0.95) m
 1.91 s  block passes 0.42 m from ball2 (ball2_sphere) without touching it: nearest points (-0.05, 0.00, 0.68) m and (-0.47, 0.00, 0.68) m
 2.15 s  ball2_sphere first touches cup_base
 2.63 s  ball2_sphere first touches cup_wall_xp
 2.63 s  ball2 comes to rest at (-0.49, 0.00, 0.13) m
 2.67 s  ball2_sphere leaves cup_wall_xp

State every 0.25 s:
0.00 s: ball1 at (0.55, 0.00, 3.95) m, at rest; touching nothing | flap1 at 0.0°, still; touching nothing | flap1_retainer at 0.0°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest; touching flap1_retainer.flap1_cam_06, flap1_retainer.flap1_cam_07 | flap2 at 0.0°, still; touching nothing | flap2_retainer at 0.0°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_retainer.flap2_cam_06
0.25 s: ball1 at (0.55, 0.00, 3.65) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | flap1 at -0.2°, still; touching nothing | flap1_retainer at 0.0°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest, turned 1° from how it started; touching flap1_retainer.flap1_cam_06, flap1_retainer.flap1_cam_07 | flap2 at -0.2°, still; touching nothing | flap2_retainer at 0.0°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_retainer.flap2_cam_05, flap2_retainer.flap2_cam_06
0.50 s: ball1 at (0.55, 0.00, 2.73) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | flap1 at -0.3°, still; touching nothing | flap1_retainer at 0.0°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest, turned 2° from how it started; touching block_guides_xmm, block_guides_xmp, flap1_retainer.flap1_cam_06, flap1_retainer.flap1_cam_07 | flap2 at -0.4°, still; touching nothing | flap2_retainer at -0.0°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_retainer.flap2_cam_05, flap2_retainer.flap2_cam_06
0.75 s: ball1 at (0.55, 0.00, 1.68) m, moving 1.87 m/s (vx -0.48, vy +0.00, vz +1.81); touching nothing | flap1 at -51.6°, turning +5°/s; touching nothing | flap1_retainer at -10.5°, turning +17°/s; touching nothing | block at (0.00, 0.00, 2.66) m, moving 0.67 m/s (vx +0.01, vy -0.00, vz -0.67); touching nothing | flap2 at -0.6°, still; touching nothing | flap2_retainer at -0.1°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_retainer.flap2_cam_05
1.00 s: ball1 at (0.55, 0.00, 1.76) m, moving 0.88 m/s (vx +0.02, vy +0.00, vz -0.88); touching ball1_guides_mm, ball1_guides_mp | flap1 at -51.6°, still; touching nothing | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 2.18) m, moving 3.12 m/s (vx -0.03, vy -0.00, vz -3.12); touching nothing | flap2 at -0.8°, still; touching nothing | flap2_retainer at -0.1°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_retainer.flap2_cam_05
1.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 1.18) m, moving 3.45 m/s (vx -0.02, vy -0.00, vz -3.45), turned 1° from how it started; touching nothing | flap2 at -18.6°, turning -434°/s; touching nothing | flap2_retainer at 0.0°, turning -2°/s; touching nothing | ball2 at (-0.55, 0.00, 1.69) m, moving 0.16 m/s (vx +0.14, vy +0.00, vz +0.09); touching nothing
1.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.75) m, moving 0.11 m/s (vx +0.01, vy -0.00, vz -0.11); touching block_guides_xpm, block_guides_xpp | flap2 at -51.6°, still; touching nothing | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.55, 0.00, 1.58) m, moving 1.46 m/s (vx -0.05, vy -0.00, vz -1.46); touching nothing
1.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.55, 0.00, 1.08) m, moving 2.69 m/s (vx -0.10, vy +0.00, vz -2.69); touching nothing
2.00 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.55, 0.00, 0.49) m, moving 2.03 m/s (vx -0.34, vy +0.00, vz -2.00); touching nothing
2.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.53, 0.00, 0.13) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching cup_base
2.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.50, 0.00, 0.13) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching cup_base
2.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.50, 0.00, 0.13) m, at rest; touching cup_base
(the same through 3.25 s)
3.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.51, 0.00, 0.13) m, at rest; touching cup_base
(the same through 4.00 s)
4.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.52, 0.00, 0.13) m, at rest; touching cup_base
(the same through 4.50 s)
4.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.53, 0.00, 0.13) m, at rest; touching cup_base
(the same through 5.25 s)
5.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp | flap2 at -51.6°, still; touching nothing | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.54, 0.00, 0.13) m, at rest; touching cup_base
5.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at -51.6°, still; touching ball1_sphere | flap1_retainer at -10.3°, still; touching nothing | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at -51.6°, still; touching block_box | flap2_retainer at -10.3°, still; touching nothing | ball2 at (-0.54, 0.00, 0.13) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate
- flap1 at -51.6°, still; touching ball1_sphere
- flap1_retainer at -10.3°, still; touching nothing
- block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate
- flap2 at -51.6°, still; touching block_box
- flap2_retainer at -10.3°, still; touching nothing
- ball2 at (-0.54, 0.00, 0.13) m, at rest; touching cup_base
</history>
