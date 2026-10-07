MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever: hinge joint lever_hinge about axis (0.00, 1.00, 0.00), range -25° to 0° as MuJoCo applies it; its geoms: lever; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.65, 0.00, 1.12) m, at rest
- lift: free body; its geoms: lift, lift stem; starts at (0.68, 0.00, 1.11) m, at rest
- ball: free body; its geoms: ball; starts at (0.77, 0.00, 1.53) m, at rest

What happened, in order:
 0.00 s  ball starts touching bridge
 0.00 s  lever starts at its upper stop (0°)
 0.00 s  lever is at its largest at the start, 0.0°
 0.00 s  lift stem first touches right seat
 0.00 s  lift stem first touches left seat
 0.01 s  weight starts moving
 0.32 s  lever first touches weight
 0.35 s  lift stem leaves right seat
 0.35 s  lift stem leaves left seat
 0.35 s  lever first touches lift stem
 0.35 s  lift starts moving
 0.36 s  lift stem first touches rear guide
 0.38 s  lift stem first touches front guide
 0.38 s  lever leaves lift stem
 0.38 s  lever leaves weight
 0.39 s  lift stem leaves rear guide
 0.41 s  lever reaches its lower stop (-25°) moving -250°/s
 0.42 s  lever touches weight again
 0.43 s  ball leaves bridge
 0.43 s  lift first touches ball
 0.43 s  ball starts moving
 0.44 s  lever passes 0.06 m from left guide without touching it: nearest points (0.69, 0.03, 0.90) m and (0.69, 0.08, 0.90) m
 0.44 s  lever passes 0.06 m from right guide without touching it: nearest points (0.69, -0.03, 0.90) m and (0.69, -0.08, 0.90) m
 0.44 s  lift stem leaves front guide
 0.45 s  lever is at its smallest, -28.6°
 0.45 s  lift leaves ball
 0.45 s  lever passes 0.03 m from rear guide without touching it: nearest points (0.63, 0.00, 0.87) m and (0.61, 0.00, 0.90) m
 0.45 s  lift stem touches rear guide again
 0.47 s  lift stem leaves rear guide
 0.50 s  lever passes 0.05 m from front guide without touching it: nearest points (0.71, 0.03, 0.88) m and (0.74, 0.03, 0.90) m
 0.53 s  lever reaches its lower stop (-25°) again moving +28°/s
 0.58 s  ball is at the top of its flight, at (0.98, 0.00, 1.64) m
 0.73 s  ball touches bridge again
 0.81 s  lift is at the top of its flight, at (0.62, 0.00, 2.16) m
 0.88 s  ball leaves bridge
 0.89 s  ball first touches cup_base
 1.09 s  lift stem touches front guide again
 1.10 s  lift stem touches rear guide again
 1.11 s  lift stem leaves front guide
 1.12 s  lift stem leaves rear guide
 1.15 s  lift passes 0.08 m from bridge left rail without touching it: nearest points (0.75, 0.08, 1.49) m and (0.75, 0.16, 1.49) m
 1.15 s  lift stem touches front guide again
 1.15 s  lift stem first touches bridge
 1.16 s  lift stem leaves front guide
 1.16 s  lift stem touches rear guide again
 1.18 s  lift stem leaves bridge
 1.19 s  lift passes 0.08 m from bridge right rail without touching it: nearest points (0.75, -0.08, 1.50) m and (0.75, -0.16, 1.50) m
 1.19 s  lift stem leaves rear guide
 1.24 s  lift stem touches rear guide 2 more times between 1.24 s and 6.00 s, still touching at the end
 1.25 s  lift stem touches front guide again
 1.27 s  lift stem leaves front guide
 1.33 s  lift stem touches front guide 1 more times between 1.33 s and 1.33 s
 1.33 s  lever touches lift stem again
 1.35 s  weight comes to rest at (-0.70, 0.00, 0.31) m
 1.39 s  lift comes to rest at (0.67, 0.00, 1.33) m
 1.60 s  ball comes to rest at (1.83, 0.00, 1.53) m

State every 0.25 s:
0.00 s: lever at 0.0°, still; touching nothing | weight at (-0.65, 0.00, 1.12) m, at rest; touching nothing | lift at (0.68, 0.00, 1.11) m, at rest; touching nothing | ball at (0.77, 0.00, 1.53) m, at rest; touching bridge
0.25 s: lever at 0.0°, still; touching nothing | weight at (-0.65, 0.00, 0.82) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | lift at (0.68, 0.00, 1.11) m, at rest; touching left seat, right seat | ball at (0.77, 0.00, 1.53) m, at rest; touching bridge
0.50 s: lever at -26.3°, turning +42°/s; touching weight | weight at (-0.67, 0.00, 0.31) m, moving 0.52 m/s (vx -0.19, vy -0.00, vz +0.48), turned 26° from how it started; touching lever | lift at (0.66, 0.00, 1.67) m, moving 3.09 m/s (vx -0.13, vy -0.00, vz +3.08), turned 3° from how it started; touching nothing | ball at (0.86, 0.00, 1.61) m, moving 1.64 m/s (vx +1.43, vy +0.00, vz +0.81); touching nothing
0.75 s: lever at -25.4°, still; touching weight | weight at (-0.70, 0.00, 0.31) m, at rest, turned 25° from how it started; touching lever | lift at (0.63, 0.00, 2.14) m, moving 0.64 m/s (vx -0.13, vy -0.00, vz +0.63), turned 7° from how it started; touching nothing | ball at (1.22, 0.00, 1.53) m, moving 1.37 m/s (vx +1.36, vy +0.00, vz +0.18); touching bridge
1.00 s: lever at -25.4°, still; touching weight | weight at (-0.70, 0.00, 0.31) m, at rest, turned 25° from how it started; touching lever | lift at (0.60, 0.00, 1.99) m, moving 1.84 m/s (vx -0.13, vy -0.00, vz -1.83), turned 11° from how it started; touching nothing | ball at (1.53, 0.00, 1.53) m, moving 0.98 m/s (vx +0.98, vy +0.00, vz -0.01); touching nothing
1.25 s: lever at -25.4°, still; touching weight | weight at (-0.70, 0.00, 0.31) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.54) m, moving 2.15 m/s (vx +0.20, vy -0.00, vz -2.14), turned 2° from how it started; touching front guide, rear guide | ball at (1.72, 0.00, 1.53) m, moving 0.58 m/s (vx +0.58, vy +0.00, vz +0.02); touching cup_base
1.50 s: lever at -25.4°, still; touching lift stem, weight | weight at (-0.70, 0.00, 0.31) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest; touching lever, rear guide | ball at (1.82, 0.00, 1.53) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz -0.01); touching cup_base
1.75 s: lever at -25.3°, still; touching lift stem, weight | weight at (-0.70, 0.00, 0.31) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
(the same through 2.00 s)
2.25 s: lever at -25.3°, still; touching lift stem, weight | weight at (-0.70, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
2.50 s: lever at -25.4°, still; touching lift stem, weight | weight at (-0.70, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
2.75 s: lever at -25.4°, still; touching lift stem, weight | weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
3.00 s: lever at -25.3°, still; touching lift stem, weight | weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
3.25 s: lever at -25.4°, still; touching lift stem, weight | weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
(the same through 4.00 s)
4.25 s: lever at -25.3°, still; touching lift stem, weight | weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
4.50 s: lever at -25.4°, still; touching lift stem, weight | weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever | lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide | ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- lever at -25.4°, still; touching lift stem, weight
- weight at (-0.71, 0.00, 0.30) m, at rest, turned 25° from how it started; touching lever
- lift at (0.67, 0.00, 1.33) m, at rest, turned 1° from how it started; touching lever, rear guide
- ball at (1.84, 0.00, 1.53) m, at rest; touching cup_base
</history>
