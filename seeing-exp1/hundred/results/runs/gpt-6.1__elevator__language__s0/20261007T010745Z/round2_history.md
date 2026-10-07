MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 0.06 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever: hinge joint lever_hinge about axis (0.00, 1.00, 0.00), range -12° to 0° as MuJoCo applies it; its geoms: lever; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.45, 0.00, 0.98) m, at rest
- lift: free body; its geoms: lift, lift crown; starts at (0.40, 0.00, 0.67) m, at rest
- ball: free body; its geoms: ball; starts at (0.51, 0.00, 1.13) m, at rest

What happened, in order:
 0.00 s  ball starts touching bridge
 0.00 s  lever starts at its upper stop (0°)
 0.00 s  lever is at its largest at the start, 0.0°
 0.00 s  ball comes to rest at (0.51, 0.00, 1.13) m
 0.00 s  lift first touches right lift shoulder
 0.00 s  lift first touches left lift shoulder
 0.01 s  weight starts moving
 0.01 s  lift starts moving
 0.05 s  lift comes to rest at (0.40, 0.00, 0.67) m
 0.06 s  weight is still moving at the end, 0.59 m/s
 0.18 s  lift touches right lift shoulder again
 0.18 s  lift touches right lift shoulder again
 0.18 s  lift touches right lift shoulder again
 0.18 s  lift touches right lift shoulder 27 more times between 0.18 s and 0.05 s
 0.19 s  lift first touches ball
 0.19 s  lift crown first touches bridge
 0.19 s  ball starts moving
 0.20 s  lift first touches floor
 0.20 s  lift crown first touches floor
 0.20 s  lever passes 0.31 m from weight without touching it: nearest points (-0.41, 0.05, 0.42) m and (-0.41, 0.05, 0.73) m

State every 0.25 s:
0.00 s: lever at 0.0°, still; touching nothing | weight at (-0.45, 0.00, 0.98) m, at rest; touching nothing | lift at (0.40, 0.00, 0.67) m, at rest; touching nothing | ball at (0.51, 0.00, 1.13) m, at rest; touching bridge

At the end (0.06 s):
- lever at 0.0°, still; touching nothing
- weight at (-0.45, 0.00, 0.96) m, moving 0.59 m/s (vx +0.00, vy +0.00, vz -0.59); touching nothing
- lift at (0.40, 0.00, 0.67) m, at rest; touching left lift shoulder
- ball at (0.51, 0.00, 1.13) m, at rest; touching bridge
</history>
