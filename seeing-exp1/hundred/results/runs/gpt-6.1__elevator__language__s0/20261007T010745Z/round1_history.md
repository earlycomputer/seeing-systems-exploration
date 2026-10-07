MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 0.02 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever: hinge joint lever_hinge about axis (0.00, 1.00, 0.00), range -12° to 0° as MuJoCo applies it; its geoms: lever; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.45, 0.00, 0.98) m, at rest
- lift: free body; its geoms: lift, lift shank; starts at (0.45, 0.00, 0.90) m, at rest
- ball: free body; its geoms: ball; starts at (0.51, 0.00, 1.12) m, at rest

What happened, in order:
 0.00 s  lever starts at its upper stop (0°)
 0.00 s  lever is at its largest at the start, 0.0°
 0.00 s  lift shank first touches right lift shoulder
 0.00 s  lift shank first touches left lift shoulder
 0.00 s  ball first touches bridge
 0.01 s  weight starts moving
 0.02 s  lift shank leaves right lift shoulder
 0.02 s  lift shank leaves left lift shoulder
 0.02 s  lift starts moving
 0.02 s  lift shank first touches left lift guide
 0.02 s  weight is still moving at the end, 0.20 m/s
 0.02 s  lift is still moving at the end, 0.39 m/s
 0.02 s  lift shank first touches right lift guide
 0.04 s  lift shank first touches far lift guide
 0.04 s  lift shank first touches near lift guide
 0.05 s  weight passes 0.10 m from lift (lift shank) without touching it: nearest points (-0.39, -0.01, 0.91) m and (-0.30, -0.01, 0.88) m
 0.05 s  lift first touches floor
 0.05 s  lift shank first touches floor

State every 0.25 s:
0.00 s: lever at 0.0°, still; touching nothing | weight at (-0.45, 0.00, 0.98) m, at rest; touching nothing | lift at (0.45, 0.00, 0.90) m, at rest; touching nothing | ball at (0.51, 0.00, 1.12) m, at rest; touching nothing

At the end (0.02 s):
- lever at 0.0°, still; touching nothing
- weight at (-0.45, 0.00, 0.98) m, moving 0.20 m/s (vx +0.00, vy +0.00, vz -0.20); touching nothing
- lift at (0.45, 0.00, 0.90) m, moving 0.39 m/s (vx +0.06, vy +0.21, vz +0.32); touching left lift guide
- ball at (0.51, 0.00, 1.12) m, at rest; touching bridge
</history>
