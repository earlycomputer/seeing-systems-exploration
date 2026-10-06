Your expectations, checked against the run (0 of 10 hold):

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
- domino1: free body; its geoms: domino1_box; starts at (0.01, 0.00, 0.06) m, moving 0.24 m/s (vx +0.24, vy +0.00, vz -0.01)
- domino2: free body; its geoms: domino2_box; starts at (0.04, 0.00, 0.06) m, at rest
- domino3: free body; its geoms: domino3_box; starts at (0.09, 0.00, 0.06) m, at rest
- domino4: free body; its geoms: domino4_box; starts at (0.14, 0.00, 0.06) m, at rest
- domino5: free body; its geoms: domino5_box; starts at (0.18, 0.00, 0.06) m, at rest
- domino6: free body; its geoms: domino6_box; starts at (0.23, 0.00, 0.06) m, at rest
- domino7: free body; its geoms: domino7_box; starts at (0.27, 0.00, 0.06) m, at rest
- domino8: free body; its geoms: domino8_box; starts at (0.32, 0.00, 0.06) m, at rest
- domino9: free body; its geoms: domino9_box; starts at (0.36, 0.00, 0.06) m, at rest
- domino10: free body; its geoms: domino10_box; starts at (0.41, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  domino1_box first touches domino2_box
 0.00 s  domino2 starts moving
 0.01 s  domino7_box first touches floor
 0.01 s  domino4_box first touches floor
 0.01 s  domino10_box first touches floor
 0.01 s  domino3_box first touches floor
 0.01 s  domino9_box first touches floor
 0.01 s  domino6_box first touches floor
 0.01 s  domino2_box first touches floor
 0.01 s  domino5_box first touches floor
 0.01 s  domino8_box first touches floor
 0.01 s  domino1_box first touches floor
 0.02 s  domino1_box leaves domino2_box
 0.08 s  domino1_box touches domino2_box again
 0.12 s  domino2_box first touches domino3_box
 0.13 s  domino3 starts moving
 0.26 s  domino3_box first touches domino4_box
 0.26 s  domino4 starts moving
 0.27 s  domino3_box leaves domino4_box
 0.27 s  domino2_box leaves domino3_box
 0.30 s  domino2_box touches domino3_box again
 0.31 s  domino3_box touches domino4_box again
 0.35 s  domino4_box first touches domino5_box
 0.35 s  domino5 starts moving
 0.36 s  domino3_box leaves domino4_box
 0.36 s  domino4_box leaves domino5_box
 0.39 s  domino3_box touches domino4_box again
 0.41 s  domino4_box touches domino5_box again
 0.43 s  domino5_box first touches domino6_box
 0.43 s  domino6 starts moving
 0.43 s  domino5_box leaves domino6_box
 0.47 s  domino5_box touches domino6_box again
 0.49 s  domino6_box first touches domino7_box
 0.49 s  domino7 starts moving
 0.50 s  domino6_box leaves domino7_box
 0.54 s  domino6_box touches domino7_box again
 0.55 s  domino7_box first touches domino8_box
 0.55 s  domino8 starts moving
 0.56 s  domino7_box leaves domino8_box
 0.57 s  domino6_box leaves domino7_box
 0.60 s  domino7_box touches domino8_box again
 0.61 s  domino6_box touches domino7_box again
 0.61 s  domino2 passes 0.19 m from domino9 (domino9_box) without touching it: nearest points (0.16, 0.03, 0.07) m and (0.35, 0.03, 0.07) m
 0.61 s  domino8_box first touches domino9_box
 0.61 s  domino9 starts moving
 0.62 s  domino8_box leaves domino9_box
 0.62 s  domino7_box leaves domino8_box
 0.66 s  domino2 passes 0.24 m from domino10 (domino10_box) without touching it: nearest points (0.16, 0.03, 0.06) m and (0.39, 0.03, 0.06) m
 0.66 s  domino3 passes 0.19 m from domino10 (domino10_box) without touching it: nearest points (0.20, 0.03, 0.07) m and (0.39, 0.03, 0.07) m
 0.66 s  domino9_box first touches domino10_box
 0.66 s  domino10 starts moving
 0.67 s  domino8_box touches domino9_box again
 0.67 s  domino7_box touches domino8_box again
 0.75 s  domino1 comes to rest at (0.06, 0.00, 0.04) m
 0.78 s  domino1_box leaves floor
 0.80 s  domino2 comes to rest at (0.11, 0.00, 0.04) m
 0.82 s  domino4_box leaves floor
 0.82 s  domino3 comes to rest at (0.15, 0.00, 0.04) m
 0.82 s  domino9_box leaves floor
 0.82 s  domino4 comes to rest at (0.20, 0.00, 0.04) m
 0.82 s  domino5 comes to rest at (0.24, 0.00, 0.04) m
 0.85 s  domino9_box touches floor again
 0.87 s  domino9_box leaves floor
 0.87 s  domino8_box leaves floor
 0.87 s  domino6 comes to rest at (0.29, 0.00, 0.03) m
 0.87 s  domino7 comes to rest at (0.34, 0.00, 0.04) m
 0.87 s  domino9 comes to rest at (0.43, 0.00, 0.04) m
 0.87 s  domino10 comes to rest at (0.48, 0.00, 0.01) m
 0.88 s  domino8 comes to rest at (0.38, 0.00, 0.04) m
 0.97 s  domino8_box touches floor again
 1.56 s  domino4_box touches floor again
 1.60 s  domino3_box leaves floor
 2.98 s  domino3_box touches floor again
 5.36 s  domino1_box touches floor again

State every 0.25 s:
0.00 s: domino1 at (0.01, 0.00, 0.06) m, moving 0.24 m/s (vx +0.24, vy +0.00, vz -0.01); touching nothing | domino2 at (0.04, 0.00, 0.06) m, at rest; touching nothing | domino3 at (0.09, 0.00, 0.06) m, at rest; touching nothing | domino4 at (0.14, 0.00, 0.06) m, at rest; touching nothing | domino5 at (0.18, 0.00, 0.06) m, at rest; touching nothing | domino6 at (0.23, 0.00, 0.06) m, at rest; touching nothing | domino7 at (0.27, 0.00, 0.06) m, at rest; touching nothing | domino8 at (0.32, 0.00, 0.06) m, at rest; touching nothing | domino9 at (0.36, 0.00, 0.06) m, at rest; touching nothing | domino10 at (0.41, 0.00, 0.06) m, at rest; touching nothing
0.25 s: domino1 at (0.04, 0.00, 0.06) m, moving 0.10 m/s (vx +0.09, vy +0.00, vz -0.03), turned 21° from how it started; touching domino2_box, floor | domino2 at (0.07, 0.00, 0.06) m, moving 0.13 m/s (vx +0.12, vy +0.00, vz -0.03), turned 23° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.10, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00), turned 11° from how it started; touching domino2_box, floor | domino4 at (0.14, 0.00, 0.06) m, at rest; touching floor | domino5 at (0.18, 0.00, 0.06) m, at rest; touching floor | domino6 at (0.23, 0.00, 0.06) m, at rest; touching floor | domino7 at (0.27, 0.00, 0.06) m, at rest; touching floor | domino8 at (0.32, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.36, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.41, 0.00, 0.06) m, at rest; touching floor
0.50 s: domino1 at (0.05, 0.00, 0.04) m, moving 0.07 m/s (vx +0.06, vy +0.00, vz -0.03), turned 41° from how it started; touching domino2_box | domino2 at (0.09, 0.00, 0.05) m, moving 0.06 m/s (vx +0.05, vy +0.00, vz -0.02), turned 49° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.14, 0.00, 0.05) m, moving 0.07 m/s (vx +0.06, vy -0.00, vz -0.03), turned 42° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.17, 0.00, 0.06) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.02), turned 34° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.21, 0.00, 0.06) m, moving 0.13 m/s (vx +0.12, vy -0.00, vz -0.03), turned 24° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.24, 0.00, 0.06) m, moving 0.19 m/s (vx +0.18, vy +0.00, vz -0.02), turned 13° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.27, 0.00, 0.06) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz +0.03), turned 1° from how it started; touching domino6_box, floor | domino8 at (0.32, 0.00, 0.06) m, at rest; touching floor | domino9 at (0.36, 0.00, 0.06) m, at rest; touching floor | domino10 at (0.41, 0.00, 0.06) m, at rest; touching floor
0.75 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 50° from how it started; touching domino2_box, floor | domino2 at (0.11, 0.00, 0.04) m, moving 0.06 m/s (vx +0.04, vy +0.00, vz -0.05), turned 62° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, moving 0.11 m/s (vx +0.06, vy -0.00, vz -0.09), turned 60° from how it started; touching domino2_box, floor | domino4 at (0.19, 0.00, 0.04) m, moving 0.12 m/s (vx +0.08, vy -0.00, vz -0.09), turned 58° from how it started; touching floor | domino5 at (0.24, 0.00, 0.04) m, moving 0.12 m/s (vx +0.10, vy -0.00, vz -0.07), turned 56° from how it started; touching domino6_box, floor | domino6 at (0.28, 0.00, 0.04) m, moving 0.15 m/s (vx +0.12, vy -0.00, vz -0.10), turned 52° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.32, 0.00, 0.05) m, moving 0.26 m/s (vx +0.21, vy -0.00, vz -0.16), turned 47° from how it started; touching domino6_box, floor | domino8 at (0.36, 0.00, 0.05) m, moving 0.31 m/s (vx +0.27, vy -0.00, vz -0.15), turned 41° from how it started; touching domino9_box | domino9 at (0.40, 0.00, 0.06) m, moving 0.37 m/s (vx +0.34, vy +0.00, vz -0.14), turned 32° from how it started; touching domino8_box, floor | domino10 at (0.43, 0.00, 0.06) m, moving 0.42 m/s (vx +0.41, vy +0.00, vz -0.09), turned 23° from how it started; touching floor
1.00 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box | domino5 at (0.24, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 1.25 s)
1.50 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box | domino5 at (0.24, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
1.75 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.24, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 63° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 2.75 s)
3.00 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.24, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
(the same through 5.25 s)
5.50 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box, floor | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.24, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
5.75 s: domino1 at (0.06, 0.00, 0.04) m, at rest, turned 52° from how it started; touching domino2_box, floor | domino2 at (0.11, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.20, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.24, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
6.00 s: domino1 at (0.06, 0.00, 0.03) m, at rest, turned 52° from how it started; touching domino2_box, floor | domino2 at (0.11, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor | domino3 at (0.15, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor | domino4 at (0.20, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor | domino5 at (0.24, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor | domino6 at (0.29, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor | domino7 at (0.34, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor | domino8 at (0.38, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino7_box, domino9_box, floor | domino9 at (0.43, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino10_box, domino8_box | domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor

At the end (6.00 s):
- domino1 at (0.06, 0.00, 0.03) m, at rest, turned 52° from how it started; touching domino2_box, floor
- domino2 at (0.11, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino1_box, domino3_box, floor
- domino3 at (0.15, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino2_box, domino4_box, floor
- domino4 at (0.20, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino3_box, domino5_box, floor
- domino5 at (0.24, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino4_box, domino6_box, floor
- domino6 at (0.29, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino5_box, domino7_box, floor
- domino7 at (0.34, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino6_box, domino8_box, floor
- domino8 at (0.38, 0.00, 0.03) m, at rest, turned 64° from how it started; touching domino7_box, domino9_box, floor
- domino9 at (0.43, 0.00, 0.04) m, at rest, turned 64° from how it started; touching domino10_box, domino8_box
- domino10 at (0.48, 0.00, 0.01) m, at rest, turned 90° from how it started; touching domino9_box, floor
</history>
