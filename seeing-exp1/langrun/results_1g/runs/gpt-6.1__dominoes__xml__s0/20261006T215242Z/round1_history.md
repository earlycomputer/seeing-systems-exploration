Your expectations, checked against the run (9 of 19 hold):

- holds: domino1 touches domino2 (first touch at 0.05 s)
- holds: domino2 touches domino3 (first touch at 0.23 s)
- holds: domino3 touches domino4 (first touch at 0.39 s)
- holds: domino4 touches domino5 (first touch at 0.52 s)
- holds: domino5 touches domino6 (first touch at 0.63 s)
- holds: domino6 touches domino7 (first touch at 0.73 s)
- holds: domino7 touches domino8 (first touch at 0.82 s)
- holds: domino8 touches domino9 (first touch at 0.91 s)
- holds: domino9 touches domino10 (first touch at 1.00 s)
- DOES NOT HOLD: domino1 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino2 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino3 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino4 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino5 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino6 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino7 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino8 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino9 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- DOES NOT HOLD: domino10 ends tilted at least 15 degrees from upright (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- domino1: free body; its geoms: domino1_geom; starts at (0.00, 0.00, 0.15) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.07)
- domino2: free body; its geoms: domino2_geom; starts at (0.12, 0.00, 0.15) m, at rest
- domino3: free body; its geoms: domino3_geom; starts at (0.24, 0.00, 0.15) m, at rest
- domino4: free body; its geoms: domino4_geom; starts at (0.36, 0.00, 0.15) m, at rest
- domino5: free body; its geoms: domino5_geom; starts at (0.48, 0.00, 0.15) m, at rest
- domino6: free body; its geoms: domino6_geom; starts at (0.60, 0.00, 0.15) m, at rest
- domino7: free body; its geoms: domino7_geom; starts at (0.72, 0.00, 0.15) m, at rest
- domino8: free body; its geoms: domino8_geom; starts at (0.84, 0.00, 0.15) m, at rest
- domino9: free body; its geoms: domino9_geom; starts at (0.96, 0.00, 0.15) m, at rest
- domino10: free body; its geoms: domino10_geom; starts at (1.08, 0.00, 0.15) m, at rest

What happened, in order:
 0.00 s  domino7_geom starts touching floor
 0.00 s  domino4_geom starts touching floor
 0.00 s  domino10_geom starts touching floor
 0.00 s  domino3_geom starts touching floor
 0.00 s  domino9_geom starts touching floor
 0.00 s  domino6_geom starts touching floor
 0.00 s  domino2_geom starts touching floor
 0.00 s  domino5_geom starts touching floor
 0.00 s  domino8_geom starts touching floor
 0.00 s  domino1_geom first touches floor
 0.05 s  domino1_geom first touches domino2_geom
 0.05 s  domino2 starts moving
 0.06 s  domino1_geom leaves domino2_geom
 0.10 s  domino1_geom touches domino2_geom again
 0.17 s  domino1_geom leaves domino2_geom
 0.21 s  domino1_geom touches domino2_geom again
 0.23 s  domino2_geom first touches domino3_geom
 0.23 s  domino3 starts moving
 0.24 s  domino2_geom leaves domino3_geom
 0.24 s  domino1_geom leaves domino2_geom
 0.28 s  domino1_geom touches domino2_geom again
 0.29 s  domino2_geom touches domino3_geom again
 0.35 s  domino1_geom leaves domino2_geom
 0.39 s  domino1_geom touches domino2_geom 2 more times between 0.39 s and 6.00 s, still touching at the end
 0.39 s  domino3_geom first touches domino4_geom
 0.39 s  domino4 starts moving
 0.40 s  domino2_geom leaves domino3_geom
 0.41 s  domino3_geom leaves domino4_geom
 0.44 s  domino2_geom touches domino3_geom again
 0.45 s  domino3_geom touches domino4_geom again
 0.46 s  domino3_geom leaves domino4_geom
 0.50 s  domino3_geom touches domino4_geom again
 0.52 s  domino4_geom first touches domino5_geom
 0.52 s  domino5 starts moving
 0.53 s  domino3_geom leaves domino4_geom
 0.53 s  domino4_geom leaves domino5_geom
 0.58 s  domino3_geom touches domino4_geom again
 0.61 s  domino4_geom touches domino5_geom again
 0.62 s  domino1 passes 0.34 m from domino6 (domino6_geom) without touching it: nearest points (0.24, -0.06, 0.13) m and (0.58, -0.06, 0.13) m
 0.63 s  domino5_geom first touches domino6_geom
 0.63 s  domino6 starts moving
 0.64 s  domino5_geom leaves domino6_geom
 0.71 s  domino5_geom touches domino6_geom again
 0.72 s  domino1 passes 0.45 m from domino7 (domino7_geom) without touching it: nearest points (0.25, -0.06, 0.11) m and (0.70, -0.06, 0.11) m
 0.73 s  domino6_geom first touches domino7_geom
 0.73 s  domino7 starts moving
 0.73 s  domino2 passes 0.30 m from domino7 (domino7_geom) without touching it: nearest points (0.40, -0.06, 0.16) m and (0.70, -0.06, 0.16) m
 0.74 s  domino6_geom leaves domino7_geom
 0.74 s  domino5_geom leaves domino6_geom
 0.74 s  domino4_geom leaves domino5_geom
 0.79 s  domino4_geom touches domino5_geom again
 0.81 s  domino5_geom touches domino6_geom again
 0.82 s  domino7_geom first touches domino8_geom
 0.82 s  domino8 starts moving
 0.82 s  domino3 passes 0.30 m from domino8 (domino8_geom) without touching it: nearest points (0.52, -0.06, 0.16) m and (0.82, -0.06, 0.16) m
 0.82 s  domino2 passes 0.41 m from domino8 (domino8_geom) without touching it: nearest points (0.41, -0.06, 0.14) m and (0.82, -0.06, 0.14) m
 0.82 s  domino6_geom touches domino7_geom again
 0.83 s  domino7_geom leaves domino8_geom
 0.83 s  domino6_geom leaves domino7_geom
 0.83 s  domino5_geom leaves domino6_geom
 0.87 s  domino5_geom touches domino6_geom again
 0.90 s  domino6_geom touches domino7_geom again
 0.91 s  domino8_geom first touches domino9_geom
 0.91 s  domino9 starts moving
 0.91 s  domino1 passes 0.23 m from domino5 (domino5_geom) without touching it: nearest points (0.26, -0.06, 0.10) m and (0.48, -0.06, 0.03) m
 0.91 s  domino4 passes 0.30 m from domino9 (domino9_geom) without touching it: nearest points (0.64, -0.06, 0.16) m and (0.94, -0.06, 0.16) m
 0.91 s  domino3 passes 0.41 m from domino9 (domino9_geom) without touching it: nearest points (0.53, -0.06, 0.14) m and (0.94, -0.06, 0.14) m
 0.91 s  domino7_geom touches domino8_geom again
 0.92 s  domino7_geom leaves domino8_geom
 0.93 s  domino6_geom leaves domino7_geom
 0.93 s  domino8_geom leaves domino9_geom
 0.93 s  domino5_geom leaves domino6_geom
 0.96 s  domino5_geom touches domino6_geom 1 more times between 0.96 s and 6.00 s, still touching at the end
 0.98 s  domino8_geom touches domino9_geom again
 0.98 s  domino6_geom touches domino7_geom again
 0.98 s  domino7_geom touches domino8_geom again
 0.99 s  domino4 passes 0.41 m from domino10 (domino10_geom) without touching it: nearest points (0.65, -0.06, 0.14) m and (1.06, -0.06, 0.14) m
 1.00 s  domino9_geom first touches domino10_geom
 1.00 s  domino10 starts moving
 1.01 s  domino9_geom leaves domino10_geom
 1.08 s  domino9_geom touches domino10_geom again
 1.10 s  domino1 comes to rest at (0.11, 0.00, 0.06) m
 1.14 s  domino1 passes 0.12 m from domino4 (domino4_geom) without touching it: nearest points (0.26, -0.06, 0.09) m and (0.37, -0.06, 0.04) m
 1.17 s  domino5 passes 0.30 m from domino10 (domino10_geom) without touching it: nearest points (0.79, 0.06, 0.12) m and (1.07, 0.06, 0.03) m
 1.18 s  domino9_geom leaves domino10_geom
 1.19 s  domino3 passes 0.19 m from domino7 (domino7_geom) without touching it: nearest points (0.55, -0.06, 0.10) m and (0.73, -0.06, 0.04) m
 1.20 s  domino4 passes 0.19 m from domino8 (domino8_geom) without touching it: nearest points (0.67, 0.06, 0.10) m and (0.85, 0.06, 0.04) m
 1.21 s  domino2 passes 0.19 m from domino6 (domino6_geom) without touching it: nearest points (0.43, -0.06, 0.10) m and (0.61, -0.06, 0.04) m
 1.21 s  domino5 passes 0.19 m from domino9 (domino9_geom) without touching it: nearest points (0.79, 0.06, 0.10) m and (0.97, 0.06, 0.04) m
 1.21 s  domino6 passes 0.19 m from domino10 (domino10_geom) without touching it: nearest points (0.91, 0.06, 0.11) m and (1.09, 0.06, 0.04) m
 1.21 s  domino9_geom touches domino10_geom again
 1.21 s  domino2 comes to rest at (0.28, 0.00, 0.07) m
 1.22 s  domino3 passes 0.04 m from domino5 (domino5_geom) without touching it: nearest points (0.55, -0.06, 0.10) m and (0.57, -0.06, 0.06) m
 1.22 s  domino4 passes 0.09 m from domino7 (domino7_geom) without touching it: nearest points (0.67, -0.06, 0.10) m and (0.73, -0.06, 0.04) m
 1.22 s  domino5 passes 0.04 m from domino7 (domino7_geom) without touching it: nearest points (0.79, 0.06, 0.10) m and (0.80, 0.06, 0.06) m
 1.22 s  domino3 comes to rest at (0.40, 0.00, 0.07) m
 1.23 s  domino8_geom leaves floor
 1.23 s  domino9_geom leaves floor
 1.23 s  domino4 comes to rest at (0.52, 0.00, 0.07) m
 1.23 s  domino2 passes 0.04 m from domino4 (domino4_geom) without touching it: nearest points (0.43, -0.06, 0.10) m and (0.44, -0.06, 0.06) m
 1.23 s  domino2 passes 0.09 m from domino5 (domino5_geom) without touching it: nearest points (0.43, -0.06, 0.10) m and (0.50, -0.06, 0.04) m
 1.23 s  domino3 passes 0.09 m from domino6 (domino6_geom) without touching it: nearest points (0.55, -0.06, 0.10) m and (0.62, -0.06, 0.04) m
 1.23 s  domino4 passes 0.04 m from domino6 (domino6_geom) without touching it: nearest points (0.60, -0.06, 0.08) m and (0.62, -0.06, 0.04) m
 1.23 s  domino5 passes 0.09 m from domino8 (domino8_geom) without touching it: nearest points (0.79, 0.06, 0.10) m and (0.86, 0.06, 0.04) m
 1.23 s  domino6 passes 0.04 m from domino8 (domino8_geom) without touching it: nearest points (0.84, 0.06, 0.08) m and (0.86, 0.06, 0.04) m
 1.23 s  domino6 passes 0.09 m from domino9 (domino9_geom) without touching it: nearest points (0.91, 0.06, 0.10) m and (0.97, 0.06, 0.04) m
 1.23 s  domino7 passes 0.04 m from domino9 (domino9_geom) without touching it: nearest points (0.96, 0.06, 0.07) m and (0.97, 0.06, 0.04) m
 1.23 s  domino7 passes 0.09 m from domino10 (domino10_geom) without touching it: nearest points (1.03, 0.06, 0.10) m and (1.10, 0.06, 0.04) m
 1.24 s  domino3_geom leaves floor
 1.24 s  domino9_geom leaves domino10_geom
 1.25 s  domino5 comes to rest at (0.64, 0.00, 0.07) m
 1.26 s  domino8_geom touches floor again
 1.27 s  domino9_geom touches floor again
 1.28 s  domino9_geom leaves floor
 1.28 s  domino9_geom touches domino10_geom again
 1.28 s  domino6 comes to rest at (0.77, 0.00, 0.07) m
 1.28 s  domino8_geom leaves floor
 1.29 s  domino7 comes to rest at (0.89, 0.00, 0.07) m
 1.29 s  domino9 comes to rest at (1.14, 0.00, 0.07) m
 1.29 s  domino10 comes to rest at (1.26, 0.00, 0.02) m
 1.29 s  domino8 passes 0.04 m from domino10 (domino10_geom) without touching it: nearest points (1.10, 0.06, 0.08) m and (1.11, 0.06, 0.04) m
 1.31 s  domino6_geom leaves floor
 1.33 s  domino8_geom touches floor again
 1.33 s  domino8 comes to rest at (1.01, 0.00, 0.07) m
 3.25 s  domino6_geom touches floor again
 5.11 s  domino3_geom touches floor again
 6.00 s  domino1 passes 0.04 m from domino3 (domino3_geom) without touching it: nearest points (0.26, 0.06, 0.08) m and (0.28, 0.06, 0.04) m

State every 0.25 s:
0.00 s: domino1 at (0.00, 0.00, 0.15) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.07); touching nothing | domino2 at (0.12, 0.00, 0.15) m, at rest; touching floor | domino3 at (0.24, 0.00, 0.15) m, at rest; touching floor | domino4 at (0.36, 0.00, 0.15) m, at rest; touching floor | domino5 at (0.48, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.60, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.72, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.84, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.96, 0.00, 0.15) m, at rest; touching floor | domino10 at (1.08, 0.00, 0.15) m, at rest; touching floor
0.25 s: domino1 at (0.05, 0.00, 0.13) m, moving 0.12 m/s (vx +0.10, vy -0.00, vz -0.06), turned 21° from how it started; touching floor | domino2 at (0.16, 0.00, 0.15) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.02), turned 16° from how it started; touching floor | domino3 at (0.24, 0.00, 0.15) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz +0.02), turned 1° from how it started; touching floor | domino4 at (0.36, 0.00, 0.15) m, at rest; touching floor | domino5 at (0.48, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.60, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.72, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.84, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.96, 0.00, 0.15) m, at rest; touching floor | domino10 at (1.08, 0.00, 0.15) m, at rest; touching floor
0.50 s: domino1 at (0.09, 0.00, 0.10) m, moving 0.18 m/s (vx +0.12, vy -0.00, vz -0.13), turned 38° from how it started; touching floor | domino2 at (0.22, 0.00, 0.13) m, moving 0.28 m/s (vx +0.25, vy -0.00, vz -0.13), turned 40° from how it started; touching domino3_geom, floor | domino3 at (0.31, 0.00, 0.14) m, moving 0.38 m/s (vx +0.36, vy -0.00, vz -0.12), turned 27° from how it started; touching domino2_geom, floor | domino4 at (0.39, 0.00, 0.15) m, moving 0.45 m/s (vx +0.44, vy -0.00, vz -0.04), turned 13° from how it started; touching floor | domino5 at (0.48, 0.00, 0.15) m, at rest; touching floor | domino6 at (0.60, 0.00, 0.15) m, at rest; touching floor | domino7 at (0.72, 0.00, 0.15) m, at rest; touching floor | domino8 at (0.84, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.96, 0.00, 0.15) m, at rest; touching floor | domino10 at (1.08, 0.00, 0.15) m, at rest; touching floor
0.75 s: domino1 at (0.11, 0.00, 0.07) m, at rest, turned 48° from how it started; touching domino2_geom, floor | domino2 at (0.26, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.37, 0.00, 0.11) m, moving 0.09 m/s (vx +0.07, vy -0.00, vz -0.05), turned 52° from how it started; touching domino2_geom, floor | domino4 at (0.47, 0.00, 0.12) m, moving 0.16 m/s (vx +0.13, vy +0.00, vz -0.09), turned 43° from how it started; touching floor | domino5 at (0.57, 0.00, 0.14) m, moving 0.25 m/s (vx +0.23, vy +0.00, vz -0.10), turned 32° from how it started; touching floor | domino6 at (0.65, 0.00, 0.15) m, moving 0.37 m/s (vx +0.36, vy -0.00, vz -0.06), turned 18° from how it started; touching floor | domino7 at (0.73, 0.00, 0.15) m, moving 0.46 m/s (vx +0.46, vy -0.00, vz +0.03), turned 4° from how it started; touching floor | domino8 at (0.84, 0.00, 0.15) m, at rest; touching floor | domino9 at (0.96, 0.00, 0.15) m, at rest; touching floor | domino10 at (1.08, 0.00, 0.15) m, at rest; touching floor
1.00 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 52° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.08) m, at rest, turned 67° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.08) m, moving 0.08 m/s (vx +0.05, vy -0.00, vz -0.06), turned 65° from how it started; touching domino2_geom, floor | domino4 at (0.51, 0.00, 0.09) m, moving 0.15 m/s (vx +0.09, vy +0.00, vz -0.12), turned 62° from how it started; touching floor | domino5 at (0.62, 0.00, 0.10) m, moving 0.21 m/s (vx +0.14, vy +0.00, vz -0.16), turned 58° from how it started; touching floor | domino6 at (0.73, 0.00, 0.11) m, moving 0.35 m/s (vx +0.26, vy -0.00, vz -0.24), turned 51° from how it started; touching floor | domino7 at (0.83, 0.00, 0.12) m, moving 0.28 m/s (vx +0.27, vy -0.00, vz -0.08), turned 43° from how it started; touching domino8_geom, floor | domino8 at (0.92, 0.00, 0.14) m, moving 0.36 m/s (vx +0.35, vy -0.00, vz -0.09), turned 30° from how it started; touching domino7_geom, domino9_geom | domino9 at (1.00, 0.00, 0.15) m, moving 0.41 m/s (vx +0.40, vy -0.00, vz -0.07), turned 16° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.08, 0.00, 0.15) m, moving 0.40 m/s (vx +0.40, vy -0.00, vz +0.05); touching domino9_geom, floor
1.25 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.64, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, floor | domino6 at (0.77, 0.00, 0.07) m, moving 0.07 m/s (vx +0.06, vy -0.00, vz -0.04), turned 70° from how it started; touching floor | domino7 at (0.89, 0.00, 0.07) m, moving 0.16 m/s (vx +0.15, vy -0.00, vz -0.03), turned 70° from how it started; touching domino8_geom | domino8 at (1.01, 0.00, 0.07) m, moving 0.26 m/s (vx +0.26, vy +0.00, vz +0.02), turned 70° from how it started; touching domino7_geom | domino9 at (1.13, 0.00, 0.07) m, moving 0.37 m/s (vx +0.33, vy -0.00, vz +0.17), turned 70° from how it started; touching nothing | domino10 at (1.25, 0.00, 0.03) m, moving 1.56 m/s (vx +0.52, vy +0.00, vz -1.47), turned 85° from how it started; touching nothing
1.50 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.64, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom | domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
1.75 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.64, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom | domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 3.25 s)
3.50 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.64, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.00 s)
5.25 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.64, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 5.50 s)
5.75 s: domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor | domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor | domino3 at (0.40, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor | domino4 at (0.52, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor | domino5 at (0.65, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor | domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor | domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor | domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor | domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom | domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
(the same through 6.00 s)

At the end (6.00 s):
- domino1 at (0.11, 0.00, 0.06) m, at rest, turned 54° from how it started; touching domino2_geom, floor
- domino2 at (0.28, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino1_geom, domino3_geom, floor
- domino3 at (0.40, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino2_geom, domino4_geom, floor
- domino4 at (0.52, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino3_geom, domino5_geom, floor
- domino5 at (0.65, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino4_geom, domino6_geom, floor
- domino6 at (0.77, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino5_geom, domino7_geom, floor
- domino7 at (0.89, 0.00, 0.07) m, at rest, turned 71° from how it started; touching domino6_geom, domino8_geom, floor
- domino8 at (1.01, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino7_geom, domino9_geom, floor
- domino9 at (1.14, 0.00, 0.07) m, at rest, turned 70° from how it started; touching domino10_geom, domino8_geom
- domino10 at (1.26, 0.00, 0.02) m, at rest, turned 90° from how it started; touching domino9_geom, floor
</history>
