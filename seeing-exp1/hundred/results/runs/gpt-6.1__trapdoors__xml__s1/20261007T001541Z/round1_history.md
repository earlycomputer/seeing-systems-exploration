MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (0.55, 0.00, 3.95) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 51.5662° as MuJoCo applies it; its geoms: flap1_plate, flap1_side_a, flap1_side_b, flap1_crossbar, flap1_cam_01, flap1_cam_02, flap1_cam_03, flap1_cam_04, flap1_cam_05, flap1_cam_06, flap1_cam_07, flap1_cam_08, flap1_cam_09; starts at 0.0°, still
- block: free body; its geoms: block_box; starts at (0.00, 0.00, 2.68) m, at rest
- flap2: hinge joint flap2_hinge about axis (0.00, 1.00, 0.00), range 0° to 51.5662° as MuJoCo applies it; its geoms: flap2_plate, flap2_side_a, flap2_side_b, flap2_crossbar, flap2_cam_01, flap2_cam_02, flap2_cam_03, flap2_cam_04, flap2_cam_05, flap2_cam_06, flap2_cam_07, flap2_cam_08; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (-0.55, 0.00, 1.68) m, at rest

What happened, in order:
 0.00 s  flap1_cam_06 starts touching block_box
 0.00 s  flap1_cam_07 starts touching block_box
 0.00 s  flap2_cam_06 starts touching ball2_sphere
 0.00 s  flap1 starts at its lower stop (0°)
 0.00 s  flap2 starts at its lower stop (0°)
 0.00 s  flap2_cam_05 first touches ball2_sphere
 0.01 s  ball1 starts moving
 0.27 s  block_box first touches block_guides_xmm
 0.27 s  block_box first touches block_guides_xmp
 0.36 s  ball2_sphere first touches ball2_guides_mp
 0.36 s  ball2_sphere first touches ball2_guides_mm
 0.40 s  ball1 passes 0.06 m from hoop1 (hoop1_02) without touching it: nearest points (0.61, 0.06, 3.16) m and (0.65, 0.10, 3.15) m
 0.48 s  block_box first touches block_guides_xpp
 0.48 s  block_box first touches block_guides_xpm
 0.52 s  ball1 passes 0.41 m from block (block_box) without touching it: nearest points (0.47, 0.00, 2.62) m and (0.05, 0.00, 2.61) m
 0.58 s  flap1_cam_07 leaves block_box
 0.58 s  ball1_sphere first touches flap1_plate
 0.59 s  block_box leaves block_guides_xmm
 0.59 s  block_box leaves block_guides_xmp
 0.59 s  block_box leaves block_guides_xpp
 0.59 s  block_box leaves block_guides_xpm
 0.59 s  flap1_cam_06 leaves block_box
 0.59 s  flap1_cam_05 first touches block_box
 0.59 s  block starts moving
 0.60 s  ball1 passes 0.46 m from support_frame (support_frame_bearing_1a) without touching it: nearest points (0.47, -0.02, 2.21) m and (0.02, -0.12, 2.20) m
 0.61 s  ball1_sphere leaves flap1_plate
 0.62 s  flap1_cam_05 leaves block_box
 0.62 s  flap1_cam_04 first touches block_box
 0.63 s  flap1_cam_04 leaves block_box
 0.63 s  flap1_cam_03 first touches block_box
 0.63 s  flap1_cam_03 leaves block_box
 0.63 s  block_box touches block_guides_xpp again
 0.63 s  block_box touches block_guides_xpm again
 0.66 s  flap1_cam_01 first touches block_box
 0.66 s  flap1_cam_02 first touches block_box
 0.66 s  flap1_cam_02 leaves block_box
 0.67 s  flap1_cam_01 leaves block_box
 0.69 s  flap1 reaches its upper stop (51.5662°) moving +449°/s
 0.69 s  flap1 is at its largest, 52.4°
 0.70 s  flap2_cam_06 leaves ball2_sphere
 0.70 s  ball1_sphere first touches ball1_guides_mp
 0.70 s  ball1_sphere first touches ball1_guides_mm
 0.70 s  flap1 reaches its upper stop (51.5662°) again moving -107°/s
 0.70 s  ball1_sphere first touches ball1_guides_pm
 0.70 s  ball1_sphere first touches ball1_guides_pp
 0.72 s  ball1_sphere leaves ball1_guides_mp
 0.72 s  ball1_sphere leaves ball1_guides_mm
 0.72 s  block_box touches block_guides_xmm again
 0.72 s  block_box touches block_guides_xmp again
 0.72 s  ball1_sphere touches flap1_plate again
 0.72 s  flap1_cam_01 touches block_box again
 0.72 s  flap1_cam_01 leaves block_box
 0.73 s  flap1 reaches its upper stop (51.5662°) again moving +221°/s
 0.73 s  block_box leaves block_guides_xmm
 0.73 s  block_box leaves block_guides_xmp
 0.73 s  flap1 passes 0.14 m from flap2 (flap2_plate) without touching it: nearest points (0.66, 0.02, 1.34) m and (0.55, 0.02, 1.25) m
 0.73 s  ball1 passes 0.30 m from flap2 (flap2_plate) without touching it: nearest points (0.55, 0.00, 1.56) m and (0.55, 0.00, 1.25) m
 0.73 s  block_box leaves block_guides_xpp
 0.73 s  block_box leaves block_guides_xpm
 0.74 s  ball1_sphere leaves flap1_plate
 0.76 s  ball1_sphere touches ball1_guides_mp again
 0.76 s  ball1_sphere touches ball1_guides_mm again
 0.76 s  ball1_sphere leaves ball1_guides_mp
 0.76 s  ball1_sphere leaves ball1_guides_mm
 0.78 s  ball1_sphere leaves ball1_guides_pm
 0.78 s  ball1_sphere leaves ball1_guides_pp
 0.81 s  ball1_sphere touches ball1_guides_mp again
 0.81 s  ball1_sphere leaves ball1_guides_mp
 0.81 s  ball1_sphere touches ball1_guides_mm again
 0.81 s  ball1_sphere leaves ball1_guides_mm
 0.83 s  ball1_sphere touches ball1_guides_pm again
 0.83 s  ball1_sphere touches ball1_guides_pp again
 0.85 s  ball1_sphere leaves ball1_guides_pm
 0.85 s  ball1_sphere leaves ball1_guides_pp
 0.87 s  block_box touches block_guides_xpp again
 0.87 s  block_box leaves block_guides_xpp
 0.87 s  block_box touches block_guides_xpm again
 0.87 s  block_box leaves block_guides_xpm
 0.95 s  ball1_sphere touches ball1_guides_mp again
 0.95 s  ball1_sphere leaves ball1_guides_mp
 0.95 s  ball1_sphere touches ball1_guides_mm again
 0.95 s  ball1_sphere leaves ball1_guides_mm
 0.99 s  block passes 0.05 m from support_frame (support_frame_bearing_1b) without touching it: nearest points (0.00, 0.05, 2.20) m and (0.00, 0.10, 2.20) m
 1.00 s  block_box touches block_guides_xmm again
 1.00 s  block_box leaves block_guides_xmm
 1.00 s  block_box touches block_guides_xmp again
 1.00 s  block_box leaves block_guides_xmp
 1.02 s  ball1_sphere touches ball1_guides_pm again
 1.02 s  ball1_sphere leaves ball1_guides_pm
 1.02 s  ball1_sphere touches ball1_guides_pp again
 1.02 s  ball1_sphere leaves ball1_guides_pp
 1.03 s  block_box touches block_guides_xmm again
 1.03 s  block_box leaves block_guides_xmm
 1.03 s  block_box touches block_guides_xmp again
 1.03 s  block_box leaves block_guides_xmp
 1.04 s  ball1_sphere touches ball1_guides_mp 3 more times between 1.04 s and 1.27 s
 1.04 s  ball1_sphere touches ball1_guides_mm 3 more times between 1.04 s and 1.27 s
 1.04 s  ball1 passes 0.40 m from block_guides (block_guides_xpm) without touching it: nearest points (0.46, -0.01, 1.77) m and (0.06, -0.03, 1.77) m
 1.09 s  block_box touches block_guides_xpp again
 1.09 s  block_box touches block_guides_xpm again
 1.09 s  block_box leaves block_guides_xpp
 1.09 s  block_box leaves block_guides_xpm
 1.11 s  ball1_sphere touches ball1_guides_pm again
 1.11 s  ball1_sphere touches ball1_guides_pp again
 1.12 s  ball1_sphere touches flap1_plate again
 1.13 s  ball1_sphere leaves flap1_plate
 1.14 s  ball1_sphere leaves ball1_guides_pm
 1.14 s  ball1_sphere leaves ball1_guides_pp
 1.15 s  block_box touches block_guides_xmm 5 more times between 1.15 s and 1.44 s
 1.15 s  block_box touches block_guides_xmp 5 more times between 1.15 s and 1.44 s
 1.20 s  ball1_sphere touches ball1_guides_pm 2 more times between 1.20 s and 6.00 s, still touching at the end
 1.20 s  ball1_sphere touches ball1_guides_pp 2 more times between 1.20 s and 6.00 s, still touching at the end
 1.22 s  ball2_sphere leaves ball2_guides_mp
 1.22 s  ball2_sphere leaves ball2_guides_mm
 1.22 s  flap2_cam_05 leaves ball2_sphere
 1.22 s  block_box touches block_guides_xpp 5 more times between 1.22 s and 6.00 s, still touching at the end
 1.22 s  block_box touches block_guides_xpm 5 more times between 1.22 s and 6.00 s, still touching at the end
 1.22 s  block_box first touches flap2_plate
 1.22 s  ball2 starts moving
 1.25 s  block_box leaves flap2_plate
 1.26 s  flap2_cam_03 first touches ball2_sphere
 1.26 s  flap2_cam_03 leaves ball2_sphere
 1.29 s  flap2_cam_02 first touches ball2_sphere
 1.29 s  flap2_cam_02 leaves ball2_sphere
 1.29 s  ball1_sphere touches flap1_plate again
 1.29 s  ball2_sphere first touches ball2_guides_pp
 1.29 s  ball2_sphere first touches ball2_guides_pm
 1.30 s  ball2_sphere leaves ball2_guides_pp
 1.30 s  ball2_sphere leaves ball2_guides_pm
 1.30 s  block passes 0.36 m from hoop2 (hoop2_01) without touching it: nearest points (-0.05, 0.00, 0.97) m and (-0.41, 0.00, 0.95) m
 1.31 s  flap2_cam_01 first touches ball2_sphere
 1.31 s  flap2_cam_01 leaves ball2_sphere
 1.33 s  ball2_sphere touches ball2_guides_pp again
 1.33 s  ball2_sphere leaves ball2_guides_pp
 1.33 s  ball2_sphere touches ball2_guides_pm again
 1.33 s  ball2_sphere leaves ball2_guides_pm
 1.34 s  ball2 is at the top of its flight, at (-0.55, 0.00, 1.69) m
 1.35 s  flap2 reaches its upper stop (51.5662°) moving +356°/s
 1.35 s  flap2 is at its largest, 51.9°
 1.35 s  ball1 comes to rest at (0.55, 0.00, 1.66) m
 1.38 s  block_box touches flap2_plate again
 1.39 s  flap2 passes 0.06 m from hoop2 (hoop2_01) without touching it: nearest points (-0.36, 0.00, 0.99) m and (-0.41, 0.00, 0.96) m
 1.39 s  flap2 passes 0.46 m from cup (cup_wall_xp) without touching it: nearest points (-0.04, 0.03, 0.58) m and (-0.40, 0.03, 0.30) m
 1.39 s  block passes 0.48 m from cup (cup_wall_xp) without touching it: nearest points (-0.04, 0.05, 0.62) m and (-0.40, 0.05, 0.30) m
 1.40 s  block_box leaves flap2_plate
 1.42 s  block passes 0.43 m from ball2_guides (ball2_guides_pp) without touching it: nearest points (-0.05, 0.05, 0.65) m and (-0.48, 0.06, 0.65) m
 1.48 s  ball2_sphere touches ball2_guides_mp again
 1.48 s  ball2_sphere leaves ball2_guides_mp
 1.48 s  ball2_sphere touches ball2_guides_mm again
 1.48 s  ball2_sphere leaves ball2_guides_mm
 1.51 s  ball2_sphere touches ball2_guides_pp again
 1.51 s  ball2_sphere touches ball2_guides_pm again
 1.51 s  ball2_sphere leaves ball2_guides_pp
 1.51 s  ball2_sphere leaves ball2_guides_pm
 1.54 s  ball2_sphere touches ball2_guides_mp again
 1.54 s  ball2_sphere leaves ball2_guides_mp
 1.54 s  ball2_sphere touches ball2_guides_mm again
 1.54 s  ball2_sphere leaves ball2_guides_mm
 1.58 s  ball2_sphere touches ball2_guides_pp again
 1.58 s  ball2_sphere touches ball2_guides_pm again
 1.58 s  ball2_sphere leaves ball2_guides_pp
 1.58 s  ball2_sphere leaves ball2_guides_pm
 1.60 s  ball2_sphere touches ball2_guides_mp again
 1.60 s  ball2_sphere touches ball2_guides_mm again
 1.60 s  ball2_sphere leaves ball2_guides_mp
 1.60 s  ball2_sphere leaves ball2_guides_mm
 1.62 s  block_box touches flap2_plate again
 1.62 s  ball2_sphere touches ball2_guides_pp 8 more times between 1.62 s and 2.01 s
 1.62 s  ball2_sphere touches ball2_guides_pm 8 more times between 1.62 s and 2.01 s
 1.65 s  ball2_sphere touches ball2_guides_mp 9 more times between 1.65 s and 2.05 s
 1.65 s  ball2_sphere touches ball2_guides_mm 9 more times between 1.65 s and 2.05 s
 1.67 s  ball2 passes 0.03 m from support_frame (support_frame_bearing_2b) without touching it: nearest points (-0.55, 0.07, 1.25) m and (-0.55, 0.10, 1.25) m
 1.67 s  block comes to rest at (0.00, 0.00, 0.71) m
 1.80 s  ball2 passes 0.04 m from hoop2 (hoop2_06) without touching it: nearest points (-0.62, 0.02, 0.95) m and (-0.66, 0.03, 0.95) m
 1.88 s  block passes 0.42 m from ball2 (ball2_sphere) without touching it: nearest points (-0.05, 0.00, 0.75) m and (-0.47, 0.00, 0.75) m
 2.12 s  ball2_sphere first touches cup_base
 2.41 s  ball2_sphere first touches cup_wall_xp
 2.41 s  ball2 comes to rest at (-0.49, 0.00, 0.13) m
 2.45 s  ball2_sphere leaves cup_wall_xp

State every 0.25 s:
0.00 s: ball1 at (0.55, 0.00, 3.95) m, at rest; touching nothing | flap1 at 0.0°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest; touching flap1_cam_06, flap1_cam_07 | flap2 at 0.0°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_cam_06
0.25 s: ball1 at (0.55, 0.00, 3.65) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | flap1 at 0.1°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest, turned 1° from how it started; touching flap1_cam_06, flap1_cam_07 | flap2 at 0.2°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_cam_05, flap2_cam_06
0.50 s: ball1 at (0.55, 0.00, 2.73) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | flap1 at 0.3°, still; touching block_box | block at (0.00, 0.00, 2.68) m, at rest, turned 2° from how it started; touching block_guides_xpm, block_guides_xpp, flap1_cam_06, flap1_cam_07 | flap2 at 0.4°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching flap2_cam_05, flap2_cam_06
0.75 s: ball1 at (0.55, 0.00, 1.67) m, moving 2.09 m/s (vx -0.47, vy +0.00, vz +2.04); touching nothing | flap1 at 51.5°, turning -15°/s; touching nothing | block at (0.00, 0.00, 2.66) m, moving 0.54 m/s (vx +0.00, vy -0.00, vz -0.54), turned 1° from how it started; touching nothing | flap2 at 0.5°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching ball2_guides_mm, ball2_guides_mp, flap2_cam_05
1.00 s: ball1 at (0.55, 0.00, 1.81) m, moving 0.75 m/s (vx +0.05, vy -0.00, vz -0.75); touching nothing | flap1 at 51.5°, still; touching nothing | block at (0.00, 0.00, 2.22) m, moving 2.99 m/s (vx +0.01, vy +0.00, vz -2.99); touching nothing | flap2 at 0.7°, still; touching ball2_sphere | ball2 at (-0.55, 0.00, 1.68) m, at rest; touching ball2_guides_mm, ball2_guides_mp, flap2_cam_05
1.25 s: ball1 at (0.55, 0.00, 1.69) m, moving 0.33 m/s (vx -0.06, vy -0.00, vz -0.32); touching nothing | flap1 at 51.6°, still; touching nothing | block at (0.00, 0.00, 1.23) m, moving 3.34 m/s (vx +0.05, vy +0.00, vz -3.34); touching nothing | flap2 at 12.7°, turning +418°/s; touching nothing | ball2 at (-0.55, 0.00, 1.68) m, moving 0.10 m/s (vx +0.04, vy +0.00, vz -0.09); touching nothing
1.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.76) m, moving 0.10 m/s (vx +0.04, vy +0.00, vz +0.09); touching block_guides_xpm, block_guides_xpp | flap2 at 51.6°, still; touching nothing | ball2 at (-0.55, 0.00, 1.56) m, moving 1.53 m/s (vx +0.22, vy +0.00, vz -1.52); touching nothing
1.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.55, 0.00, 1.06) m, moving 2.44 m/s (vx -0.33, vy -0.00, vz -2.41); touching nothing
2.00 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.55, 0.00, 0.46) m, moving 2.44 m/s (vx +0.22, vy +0.00, vz -2.43); touching nothing
2.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.51, 0.00, 0.13) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz +0.00); touching cup_base
2.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.50, 0.00, 0.13) m, at rest; touching cup_base
(the same through 2.75 s)
3.00 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp | flap2 at 51.6°, still; touching nothing | ball2 at (-0.51, 0.00, 0.13) m, at rest; touching cup_base
3.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.51, 0.00, 0.13) m, at rest; touching cup_base
3.50 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.52, 0.00, 0.13) m, at rest; touching cup_base
(the same through 3.75 s)
4.00 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.53, 0.00, 0.13) m, at rest; touching cup_base
4.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.54, 0.00, 0.13) m, at rest; touching cup_base
(the same through 4.50 s)
4.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.55, 0.00, 0.13) m, at rest; touching cup_base
(the same through 5.00 s)
5.25 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.56, 0.00, 0.13) m, at rest; touching cup_base
(the same through 5.50 s)
5.75 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.57, 0.00, 0.13) m, at rest; touching cup_base
6.00 s: ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate | flap1 at 51.6°, still; touching ball1_sphere | block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate | flap2 at 51.6°, still; touching block_box | ball2 at (-0.58, 0.00, 0.13) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (0.55, 0.00, 1.66) m, at rest; touching ball1_guides_pm, ball1_guides_pp, flap1_plate
- flap1 at 51.6°, still; touching ball1_sphere
- block at (0.00, 0.00, 0.71) m, at rest; touching block_guides_xpm, block_guides_xpp, flap2_plate
- flap2 at 51.6°, still; touching block_box
- ball2 at (-0.58, 0.00, 0.13) m, at rest; touching cup_base
</history>
