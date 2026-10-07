MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.34, -0.27, 1.32) m, at rest
- rotor: hinge joint rotor_hinge about axis (0.00, 0.00, 1.00), range 0° to 100° as MuJoCo applies it; its geoms: rotor_hub, rotor_trigger_arm, rotor_striker_arm; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (0.30, 0.15, 1.03) m, at rest
- latch: slide joint latch_slide about axis (0.00, 1.00, 0.00), range 0 m to 0.43 m as MuJoCo applies it; its geoms: latch_striker_face, latch_longitudinal_link, latch_cross_link, latch_payload_shelf; starts at 0.000 m, still
- block: free body; its geoms: block_payload; starts at (0.80, 0.68, 1.23) m, at rest

What happened, in order:
 0.00 s  ball2_sphere starts touching ramp_ball2_runway
 0.00 s  ball1_sphere starts touching ramp_incline
 0.00 s  rotor starts at its lower stop (0°)
 0.00 s  latch starts at its lower stop (0 m)
 0.00 s  latch_payload_shelf first touches block_payload
 0.00 s  latch_cross_link first touches block_payload
 0.01 s  latch is at its smallest, -0.0 m
 0.03 s  ball1 starts moving
 1.09 s  ball1_sphere leaves ramp_incline
 1.09 s  ball1_sphere first touches ramp_ball1_runout
 1.25 s  ball1_sphere leaves ramp_ball1_runout
 1.25 s  ball1_sphere first touches rotor_trigger_arm
 1.27 s  rotor_striker_arm first touches ball2_sphere
 1.27 s  ball2 starts moving
 1.28 s  ball1 passes 0.41 m from ball2 (ball2_sphere) without touching it: nearest points (-0.02, -0.21, 1.04) m and (0.25, 0.10, 1.04) m
 1.30 s  rotor_striker_arm leaves ball2_sphere
 1.31 s  ball1_sphere leaves rotor_trigger_arm
 1.35 s  ball1_sphere touches ramp_ball1_runout again
 1.58 s  rotor passes 0.18 m from latch (latch_striker_face) without touching it: nearest points (0.32, 0.24, 1.03) m and (0.32, 0.43, 1.03) m
 1.58 s  ball2_sphere first touches latch_striker_face
 1.59 s  latch_cross_link leaves block_payload
 1.59 s  ball2_sphere leaves latch_striker_face
 1.75 s  block starts moving
 1.83 s  latch_payload_shelf leaves block_payload
 1.95 s  ball2 passes 0.46 m from block (block_payload) without touching it: nearest points (0.30, 0.48, 1.04) m and (0.74, 0.59, 1.05) m
 2.10 s  ball1 comes to rest at (0.10, -0.31, 1.03) m
 2.11 s  block passes 0.06 m from ring (ring_segment_08) without touching it: nearest points (0.75, 0.59, 0.69) m and (0.71, 0.55, 0.70) m
 2.23 s  block_payload first touches box_bottom
 2.26 s  block_payload leaves box_bottom
 2.27 s  latch reaches its upper stop (0.43 m) moving +0.64 m/s
 2.30 s  latch is at its largest, 0.4 m
 2.34 s  block_payload touches box_bottom again
 2.45 s  ball2 comes to rest at (0.21, 0.53, 1.03) m
 2.47 s  block comes to rest at (0.80, 0.63, 0.16) m
 5.04 s  ball2 passes 0.41 m from ring (ring_left_post) without touching it: nearest points (0.26, 0.55, 0.98) m and (0.54, 0.66, 0.70) m
 6.00 s  rotor is at its largest, 51.7°

State every 0.25 s:
0.00 s: ball1 at (-1.34, -0.27, 1.32) m, at rest; touching ramp_incline | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching nothing | block at (0.80, 0.68, 1.23) m, at rest; touching nothing
0.25 s: ball1 at (-1.29, -0.27, 1.30) m, moving 0.42 m/s (vx +0.40, vy +0.00, vz -0.11); touching ramp_incline | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
0.50 s: ball1 at (-1.14, -0.27, 1.26) m, moving 0.84 m/s (vx +0.80, vy +0.00, vz -0.25); touching ramp_incline | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
0.75 s: ball1 at (-0.88, -0.27, 1.18) m, moving 1.26 m/s (vx +1.21, vy +0.00, vz -0.35); touching ramp_incline | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
1.00 s: ball1 at (-0.53, -0.27, 1.08) m, moving 1.68 m/s (vx +1.61, vy +0.00, vz -0.48); touching ramp_incline | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
1.25 s: ball1 at (-0.11, -0.27, 1.04) m, moving 1.67 m/s (vx +1.67, vy +0.00, vz +0.01); touching nothing | rotor at 0.0°, still; touching nothing | ball2 at (0.30, 0.15, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
1.50 s: ball1 at (0.01, -0.29, 1.03) m, moving 0.27 m/s (vx +0.27, vy -0.06, vz +0.00); touching ramp_ball1_runout | rotor at 27.9°, turning +68°/s; touching nothing | ball2 at (0.27, 0.30, 1.04) m, moving 0.62 m/s (vx -0.12, vy +0.61, vz -0.00); touching nothing | latch at 0.000 m, still; touching block_payload | block at (0.80, 0.68, 1.22) m, at rest; touching latch_cross_link, latch_payload_shelf
1.75 s: ball1 at (0.06, -0.30, 1.03) m, moving 0.18 m/s (vx +0.17, vy -0.04, vz -0.00); touching ramp_ball1_runout | rotor at 40.7°, turning +37°/s; touching nothing | ball2 at (0.24, 0.41, 1.03) m, moving 0.31 m/s (vx -0.09, vy +0.30, vz +0.00); touching ramp_ball2_runway | latch at 0.090 m, moving +0.53 m/s; touching block_payload | block at (0.80, 0.68, 1.22) m, moving 0.06 m/s (vx -0.00, vy +0.00, vz -0.06), turned 2° from how it started; touching latch_payload_shelf
2.00 s: ball1 at (0.09, -0.31, 1.03) m, moving 0.08 m/s (vx +0.08, vy -0.02, vz -0.00); touching ramp_ball1_runout | rotor at 47.5°, turning +19°/s; touching nothing | ball2 at (0.23, 0.47, 1.03) m, moving 0.22 m/s (vx -0.06, vy +0.21, vz +0.00); touching ramp_ball2_runway | latch at 0.250 m, moving +0.66 m/s; touching nothing | block at (0.80, 0.68, 0.97) m, moving 2.23 m/s (vx -0.00, vy -0.03, vz -2.23), turned 74° from how it started; touching nothing
2.25 s: ball1 at (0.10, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 50.7°, turning +8°/s; touching nothing | ball2 at (0.21, 0.51, 1.03) m, moving 0.12 m/s (vx -0.03, vy +0.12, vz -0.00); touching ramp_ball2_runway | latch at 0.412 m, moving +0.64 m/s; touching nothing | block at (0.80, 0.66, 0.18) m, moving 0.57 m/s (vx -0.00, vy -0.48, vz +0.30), turned 154° from how it started; touching box_bottom
2.50 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.419 m, moving -0.07 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
2.75 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.401 m, moving -0.07 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
3.00 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.384 m, moving -0.07 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
3.25 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.368 m, moving -0.06 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
3.50 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.352 m, moving -0.06 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
3.75 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.337 m, moving -0.06 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
4.00 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.324 m, moving -0.05 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
4.25 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.311 m, moving -0.05 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
4.50 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.298 m, moving -0.05 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
4.75 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.287 m, moving -0.04 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
5.00 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.276 m, moving -0.04 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
5.25 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.267 m, moving -0.04 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
5.50 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.257 m, moving -0.04 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
5.75 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.249 m, moving -0.03 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
6.00 s: ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout | rotor at 51.7°, still; touching nothing | ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway | latch at 0.241 m, moving -0.03 m/s; touching nothing | block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom

At the end (6.00 s):
- ball1 at (0.11, -0.31, 1.03) m, at rest; touching ramp_ball1_runout
- rotor at 51.7°, still; touching nothing
- ball2 at (0.21, 0.53, 1.03) m, at rest; touching ramp_ball2_runway
- latch at 0.241 m, moving -0.03 m/s; touching nothing
- block at (0.80, 0.63, 0.16) m, at rest, turned 180° from how it started; touching box_bottom
</history>
