## What happens when the scene runs

1. **Ramp, 0–1.2 s.** The ball starts at rest 1 m along the 20° ramp and rolls down. It leaves the ramp at about 2 m/s and rolls along the floor in +x.
2. **Paddle, about 1.2 s.** The 0.5 kg ball hits the hanging paddle near its bottom. It keeps pushing the paddle until the paddle's lower edge rises above the ball's top, at roughly 30°. The ball then rolls on under it.
3. **Slider.** While the paddle turns, its face pushes the frictionless slider along +x. The slider closes its 3 cm gap to the block and keeps pushing it.
4. **Block and hoop.** The block's centre passes the ledge edge at x = 0.92 and it tips and falls. The slider stops at its 0.14 m limit with the block well past the edge. The block drops about 0.15 m and passes through the octagonal hoop. The hoop's inner span is about 0.89–1.19 m, and the block is expected to cross near x ≈ 1.0.
5. **Box.** The block lands in the box and settles well before 6 s.
6. **Ball.** The ball rolls under the slider, ledge and hoop and stops against the box's outer left wall. Floor and wall friction kill its spin within a fraction of a second, so it comes to rest.

## Problem found

The paddle hinge has no damping, so it keeps swinging back and forth. Each swing sweeps over the spot where the ball rests against the box wall. At x ≈ 0.805 the paddle's bottom corner passes only about 2–7 mm above the ball's top. That is too tight. Any tap would keep the ball moving, and the ball might not be at rest at 6 s.

## Fix

- Shorten the paddle slightly so its bottom sits at z = 0.035 instead of z = 0.02. The ball's contact point at z = 0.05 still lands on the plate face.
- This gives about 2.4 cm of clearance over the resting ball.
- Add a little hinge damping so the paddle's swing dies out over the run.

```json
{"what_happens": "The ball rolls 1 m down the ramp and hits and pushes the paddle, which shoves the slider; the slider pushes the block off the ledge, and the block falls through the hoop into the box and settles. The ball rolls under everything and comes to rest against the box's outer wall. However, the undamped paddle keeps swinging and its tip passes only millimetres above the resting ball, so it could keep tapping it.", "works": false, "problem": "The undamped paddle's swing clears the ball resting at the box wall by only a few millimetres, so it may keep nudging the ball and stop it from being at rest at the end."}
```

```xml
<mujoco model="ball_ramp_paddle_slider_block">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.5706 0 0.1864" euler="0 20 0">
      <geom name="ramp_deck" type="box" size="0.6 0.1 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball" pos="-0.9226 0 0.3890">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.05" mass="0.5" friction="0.5 0.005 0.002" condim="6" rgba="0.8 0.1 0.1 1"/>
    </body>

    <body name="paddle" pos="0.5 0 0.6">
      <joint name="paddle_hinge" type="hinge" axis="0 1 0" pos="0 0 0" damping="0.005"/>
      <geom name="paddle_plate" type="box" size="0.01 0.08 0.2825" pos="0 0 -0.2825" mass="0.2" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="slider" pos="0.68 0 0.40">
      <joint name="slider_slide" type="slide" axis="1 0 0" limited="true" range="0 0.14"/>
      <geom name="slider_bar" type="box" size="0.15 0.03 0.03" mass="0.1" friction="0.1" rgba="0.2 0.7 0.3 1"/>
    </body>

    <body name="ledge" pos="0.86 0 0.35">
      <geom name="ledge_shelf" type="box" size="0.06 0.08 0.01" friction="0.15" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="block" pos="0.90 0 0.40">
      <freejoint name="block_free"/>
      <geom name="block_geom" type="box" size="0.04 0.04 0.04" mass="0.1" friction="0.15" rgba="0.9 0.7 0.1 1"/>
    </body>

    <body name="hoop" pos="1.04 0 0.25">
      <geom name="hoop_s0" type="capsule" size="0.01" fromto="0.1571 0.0651 0 0.0651 0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s1" type="capsule" size="0.01" fromto="0.0651 0.1571 0 -0.0651 0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s2" type="capsule" size="0.01" fromto="-0.0651 0.1571 0 -0.1571 0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s3" type="capsule" size="0.01" fromto="-0.1571 0.0651 0 -0.1571 -0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s4" type="capsule" size="0.01" fromto="-0.1571 -0.0651 0 -0.0651 -0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s5" type="capsule" size="0.01" fromto="-0.0651 -0.1571 0 0.0651 -0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s6" type="capsule" size="0.01" fromto="0.0651 -0.1571 0 0.1571 -0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s7" type="capsule" size="0.01" fromto="0.1571 -0.0651 0 0.1571 0.0651 0" rgba="0.7 0.2 0.7 1"/>
    </body>

    <body name="box" pos="1.06 0 0">
      <geom name="box_bottom" type="box" size="0.21 0.21 0.005" pos="0 0 0.005" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_left" type="box" size="0.005 0.21 0.055" pos="-0.205 0 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_right" type="box" size="0.005 0.21 0.055" pos="0.205 0 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_front" type="box" size="0.21 0.005 0.055" pos="0 -0.205 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_back" type="box" size="0.21 0.005 0.055" pos="0 0.205 0.065" rgba="0.4 0.3 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.9226 0 0.3890 1 0 0 0  0  0  0.90 0 0.40 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Let me double-check the geometry again, particularly whether the paddle gets blocked by the slider near its limit—checking the contact point between the paddle face and the slider's end position to make sure they don't collide prematurely.

Since the ball is round, it actually passes under the paddle's bottom edge once that edge clears the ball's height, which happens around φ≈31° rather than when the edge geometrically overlaps. I'm also tracking how far the slider travels as the paddle pushes it during this rotation, comparing that against its travel limit to confirm there's enough room before contact resistance becomes an issue.

Working through the slider-block interaction further: the slider contacts the block after some travel, pushes it until hitting its own limit at 0.14, and I need to verify the block's resulting position relative to the ledge edge to confirm it clears safely rather than getting stuck. Once the block is pushed past the ledge, I'm now considering when it starts to fall and how that interacts with the hoop's position along its path.

Slider contact is lost once the block drops about 0.07, taking the block's top below the slider face. I'm checking where the hoop sits relative to the block at that height—inner x range roughly 0.893–1.187—and the block's likely center range of 0.95–1.12 seems to clear it fine. I also need to check whether the paddle's rotation is limited by the slider acting as a stop around 44°, which would prevent it from actually reaching the hoop.

Checking the geometry at 44° rotation: the paddle tip lands around x=0.903, z=0.183, while the hoop ring sits at z 0.24–0.26 with its outer left edge near 0.873—giving roughly 3 cm of clearance, which looks fine. I also want to confirm the block falling through the hoop (centered around 1.0, spanning 0.94–1.06) stays clear of the paddle tip at x=0.90, and that checks out too.

Tracing the ball's path to the box, it rolls under the paddle and hits the left wall around x=0.855, settling near x=0.805. There's a tight moment where the swinging paddle's tip (at roughly φ=31°, z=0.103) comes very close to the ball's top surface (z=0.1)—close enough that the corner might just graze it, though it shouldn't be catastrophic. The ball ends up resting against the wall, still spinning forward.

Working through the spin dynamics: the ball hits the wall at about 1.3 m/s with ω≈26 rad/s, and once translational motion stops, the spin persists. Floor friction drives the ball into the wall while wall friction acts upward, but since the upward friction force is less than the ball's weight, the ball just spins in place, gradually decelerating from combined torque at both contact points.

I'm checking the ball stops within about 0.07 s and settles to rest, then verifying it clears the slider and ramp geometry properly, confirming the ramp's bottom edge meets the floor exactly at the origin, and checking the ball stays centered symmetrically. I'm also confirming the paddle's bottom edge maintains its 2 cm gap above the floor so there's no unintended contact.

Now I'm working through the ball-paddle collision: the 0.5 kg ball transfers momentum to the paddle, pushing the slider as the paddle rotates toward 31°. The block gets pushed about 0.05 m, moving its center past the 0.92 edge threshold so it's already tipping by that point, and the slider retains enough velocity (~0.45 m/s) to keep going despite friction from the partially-tipped block, reaching its travel limit—so the mechanism seems robust since the ball does most of the work. I'm now wondering whether the tipping block could interfere with the ball's path since the ball is down at floor level.

Checking the geometry: the ball travels under the hoop toward the box wall at 0.855 without obstruction, and the slider's bottom at 0.37 clears the ledge top at 0.36 so there's no unwanted contact there, with the slider face pushing the block at mid-height as it rotates around the ledge edge. For the block's fall from 0.4 down to the box floor at 0.01, it should land around x = 1.0–1.15, comfortably within the box's inner boundary of 1.26, so the landing looks fine too.

I'm verifying the keyframe qpos count totals 16 (7 for ball, 1 paddle, 1 slider, 7 block) and that the written values match this structure correctly. The ball's initial contact with the ramp is exactly tangent, masses are set via geom attributes, and static bodies like the ramp, hoop, and ledge have no joints as expected. Now I'm double-checking whether the paddle might collide with the ledge — the slider stops the paddle at 44°, and I need to compare that position against the ledge's footprint at x 0.80–0.92, z 0.34–0.36.

Confirming paddle clearance at z=0.35 gives x≈0.742, well under the ledge's 0.80 threshold, so that's fine. I'm now considering whether the paddle's free oscillation after the ball passes could swing back and strike the resting ball near x=0.805 — checking the swing amplitude and whether the slider's range actually prevents that contact.

Accounting for the plate's thickness and corner offsets, the paddle's lower corner near that angle lands around 0.102–0.112 while the ball's top sits at 0.1 — a gap of only a few millimeters, so contact is marginal and depends on exact ball resting position. If the paddle keeps tapping the ball at this margin, it may not land a clean hit.

Worse, the paddle swings through this zone while the ball is actually passing underneath, and the backswing could clip the ball if it reaches 0.805 at just the wrong moment. I should add hinge damping so the paddle settles instead of oscillating indefinitely — with inertia 0.0224, a damping coefficient around 0.02 N·m·s/rad gives a decay rate that would calm the motion fairly quickly.

Checking the slider travel and block position with the adjusted paddle geometry, it still clears - block pushed to 0.94 past the 0.92 edge. Then verifying the tip clearance at the sweep point: about 3cm margin above the ball, which works with the added damping. I'm now double-checking where the plate's face actually contacts the ball relative to its bottom edge as it rotates through the swing.

Trying a tweak: paddle length 0.565, bottom z 0.035, damping reduced to 0.005. Recomputing the tip position gives about 2.4cm clearance, and the ball still contacts the plate face cleanly within its bounds. Now I need to reconsider the paddle's mass and moment of inertia to match this adjustment.

Checking the clearance more carefully though, the gap between the paddle tip and the ball at the critical moment comes out to only about 2mm when accounting for the corner geometry — that's too marginal since MuJoCo only triggers contact on actual overlap. That's worth fixing before presenting this as a working solution.

I'll correct the paddle geometry dimensions, adjust its position offset accordingly, and add some joint damping to make the motion more stable.

