## What happened in the run

- **Front of the chain worked.** The pendulum hit the cart, the cart knocked the weight off the shelf, and the weight landed on the seesaw. The seesaw reached its lower stop at 1.17 s.
- **The ball was thrown backwards.** It left at vx ≈ −0.55 m/s, away from the cup.
  - Cause: my sign reasoning was wrong. The ball sat above the line through the hinge, so its velocity tilted back over the pivot.
- **The weight did not stay on the seesaw.**
  - It bounced off the tray's inner wall and rolled toward −x.
  - That end of the tray had no wall, so it rolled off and onto the floor. It was still moving at 6 s.
  - Without the weight, the seesaw tipped back to its upper stop. The ball fell back onto it and ended there at rest, not in the cup.

## Fixes

- **Ball holder.** The holder now hangs just beyond the plank's end, with the ball about 9 cm below the hinge line. A ball below that line is thrown up and outward, toward +x and the cup.
- **Seesaw balance.** The tray parts are now lighter. This keeps the empty seesaw resting firmly on its upper stop despite the lowered holder.
- **Tray outer wall.** I added a wall at the outer end of the tray. It sits low enough for the falling weight to clear it, so the weight is held between the two walls.
- **Cup.** I moved and widened the cup to cover launch speeds of about 2.2 to 3.6 m/s from the new, lower launch point. Its rim is now 0.20 m high.

```json
{"what_happens": "The pendulum strikes the cart, which pushes the weight off the shelf onto the seesaw tray. The seesaw reaches its lower stop at 1.17 s, but the ball is launched toward -x, away from the cup, because it sits above the hinge line. The weight bounces off the tray wall, rolls off the open outer end of the plank and leaves the seesaw. The seesaw then tips back to its upper stop and the ball falls back onto the plank and rests there.", "works": false, "problem": "The ball is thrown backwards because its holder is above the hinge line, and the weight rolls off the seesaw's open tray end so the seesaw tips back."}
```

```xml
<mujoco model="pendulum_cart_seesaw_cup">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0.6 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="frame_post" type="box" pos="0 -0.2 0.6" size="0.02 0.02 0.6" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="frame_beam" type="box" pos="0 -0.1 1.2" size="0.015 0.1 0.015" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="shelf" type="box" pos="0.235 0 0.525" size="0.165 0.1 0.02" rgba="0.6 0.45 0.3 1"/>
    <geom name="shelf_leg" type="box" pos="0.12 0 0.2525" size="0.02 0.05 0.2525" contype="0" conaffinity="0" rgba="0.5 0.4 0.3 1"/>
    <geom name="lower_stop" type="box" pos="0.40 0 0.155" size="0.02 0.05 0.155" rgba="0.7 0.2 0.2 1"/>
    <geom name="seesaw_stand" type="box" pos="0.72 0 0.15" size="0.02 0.08 0.15" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>

    <body name="pendulum" pos="0 0 1.2">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.55" size="0.01" mass="0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.6" size="0.05" mass="1" rgba="0.2 0.2 0.8 1"/>
    </body>

    <body name="cart" pos="0.115 0 0.6">
      <joint name="cart_slide" type="slide" axis="1 0 0" limited="true" range="-0.01 0.10"/>
      <geom name="cart_body" type="box" size="0.06 0.06 0.05" mass="3" rgba="0.9 0.6 0.1 1"/>
    </body>

    <body name="weight" pos="0.245 0 0.585">
      <freejoint name="weight_free"/>
      <geom name="weight_geom" type="sphere" size="0.04" mass="1" rgba="0.2 0.2 0.2 1"/>
    </body>

    <body name="seesaw" pos="0.72 0 0.32">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-0.1 0.361"/>
      <geom name="seesaw_axle" type="cylinder" pos="0 0 0" size="0.015 0.07" euler="1.5708 0 0" contype="0" conaffinity="0" mass="0.01" rgba="0.3 0.3 0.3 1"/>
      <geom name="seesaw_plank" type="box" pos="0.01 0 0" size="0.37 0.06 0.01" mass="0.2" rgba="0.2 0.7 0.3 1"/>
      <geom name="seesaw_tray_wall" type="box" pos="-0.185 0 0.03" size="0.005 0.06 0.02" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_end_wall" type="box" pos="-0.355 0 0.025" size="0.005 0.06 0.015" mass="0.005" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_a" type="box" pos="-0.275 0.055 0.02" size="0.085 0.005 0.01" mass="0.005" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_b" type="box" pos="-0.275 -0.055 0.02" size="0.085 0.005 0.01" mass="0.005" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_bracket" type="box" pos="0.385 0 -0.055" size="0.005 0.03 0.065" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_pad" type="box" pos="0.425 0 -0.115" size="0.035 0.03 0.005" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_lip" type="box" pos="0.457 0 -0.104" size="0.003 0.03 0.006" mass="0.002" rgba="0.2 0.5 0.3 1"/>
    </body>

    <body name="ball" pos="1.0965 0 0.0832">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.02" mass="0.02" condim="6" friction="0.8 0.01 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="cup" pos="1.545 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.225 0.15 0.01" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.22 0 0.11" size="0.005 0.15 0.09" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_far" type="box" pos="0.22 0 0.11" size="0.005 0.15 0.09" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.145 0.11" size="0.215 0.005 0.09" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.145 0.11" size="0.215 0.005 0.09" rgba="0.3 0.6 0.9 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5708 0 0.245 0 0.585 1 0 0 0 0.36 1.0965 0 0.0832 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm puzzled why the ball launched backward with negative x-velocity once the seesaw hit its stop—working through the rotational position equations to find the velocity direction as a function of the tilt angle θ.

Now it clicks: since the radius vector at the stop leans toward +x, the perpendicular velocity actually leans toward −x, confirming the backward launch is correct physics, not a bug. But I'm also realizing the weight itself wasn't retained in the tray—it rolled off the back end after the bounce, lightening the seesaw and flipping it back up, which knocked the ball off the plank. So there are really two separate issues to fix: the launch direction logic, and adding some kind of retaining wall to the tray so the weight stays put after landing.

Since rolling over a 0.02 wall likely won't happen at that speed, I'll bump the wall to 0.03 tall and recheck clearance — still fine with about 0.06 margin. With the end wall added, the bouncing weight stays contained now.

Next I need to settle the launch direction: throw the ball toward +x toward the cup, since putting the cup on the −x side would conflict with the seesaw/shelf area.

The rotation range is too limited for the elevation to flip sign properly, so I'm reconsidering the geometry entirely — maybe placing the pivot above the plank instead, with the ball holder positioned below the hinge axis so that as the plank rotates, the ball end can swing fully from below to above the pivot line.

Actually, rather than raising the whole body and recomputing everything, it's simpler to just shift all the geoms down by 0.19 in the body frame while keeping body position the same — plank, tray wall, rails, post/pad/lip, and ball center all move by that offset. I need to double check that the horizontal θ=0 configuration still makes sense as the "stop" position after this shift.

With the pivot now above the plank, tilting the plank at θ causes a horizontal shift as well as vertical, since rotating a point below the pivot mixes x and z components — so the tilted plank's x-position moves slightly, meaning I'll need to retune the landing spot for the ball. I'm also considering whether this pivot-above-CoM setup creates stability: like a pendulum, gravity would tend to pull the mass back toward hanging below the pivot, so I need to work out the torque balance using the body-frame coordinates and rotation to see if the rest angle θ0 is still an equilibrium.

Working through the torque sum, I find the net torque actually pulls the seesaw toward the weight side even before the ball lands — which is bad, since I want it balanced until the ball arrives. So I'm reconsidering the design: instead of keeping the ball on the plank surface, maybe I should hang the ball holder below the plank's end via a downward bracket, placing it lower in z to fix the torque balance.

Checking the geometry though, the ball needs to launch upward and outward, and if it's positioned beneath the plank it would collide with the plank itself on its way up. I'm repositioning the pad and ball so they sit just beyond the plank's physical end, with the ball's outward trajectory (moving away from the plank in +x) clearing the obstruction.

I'm defining exact coordinates now: the plank spans roughly −0.36 to 0.38 in x, with a vertical bracket positioned just past the plank's end, and a pad mounted at the bracket's base around x 0.39–0.46. This placement keeps the ball clear of the plank as it rolls outward to the lip and launches.

I'm computing where the lip's edge sits (around x 0.454–0.46) and where the ball rests against it, finding a ball center roughly at x 0.4357 tilted about 11.7° outward from vertical, with the resting radius about 0.445. I'm double-checking clearances so the ball doesn't collide with the bracket during launch, since it's moving outward and away from the inner face at x 0.39.

Now I'm verifying launch velocity direction against the lip's contact normal—roughly 78° apart, confirming separation happens correctly—then estimating the ball's actual speed and height at launch by working backward from its observed position and velocity at t=1.25s.

Computing vz0 gives a higher value than my initial estimate, closer to 2.9-3.1 given the larger radius, and I realize I need to recheck the cup's rim height relative to this lower launch point. The uncertainty in speed is fairly wide (2.6-3.4), which matters since range scales with v², so I'm breaking the velocity into components using the 11.7° launch angle to carry this forward.

I could lower the tilt to 8° to tighten the landing spread to 0.19–0.33, but I'll keep 11.7° with a 0.4 cup width since the near wall clears the seesaw end comfortably. The ball rises about 0.44m before dropping steeply into the 0.20-rim cup, and the seesaw stays stable at its stop holding the weight — checking the weight's trajectory now, it lands on the plank at 1.09 and touches the tray wall at 1.15.

I'm recomputing the seesaw's resting balance by summing the moment contributions from each component — plank, tray wall, rails, end wall, bracket, pad, lip, and ball — along with their tilt-adjusted z-offset effects to confirm it stays stable at rest.

That margin works, so I'll keep the weight at 1 kg despite the mass changes. Now I'm computing the launch geometry in world coordinates, finding the ball's resting position at the stop and its initial tilted position by rotating the body-frame coordinates through θ0=0.36, then I still need to add clearance along the pad normal.

Checking the pad's lowest corner clears the floor by a healthy margin, and the plank's bottom at the stop position fits within the stop's range without hitting the end wall. Now I'm starting to work out the cup position based on the launch x-coordinate and its offset range.

Checking ball trajectories at various speeds against the cup walls — at low speed the ball's crossing point stays just clear of the near inner wall, at nominal speed clearance looks fine, and I'm tracing through the high-speed case to see where the trajectory lands relative to the cup opening.

Now I'm defining the cup geometry — center position, inner wall offsets, base and wall heights, and half-widths — to figure out where the ball will fall into it and whether it needs to bounce or roll before settling. I confirm the ball's path from the launch point clears the seesaw pad since it's moving away from it, then double back to recheck the launch velocity estimate for accuracy.

I'm recalculating the launch parameters with r=0.445 giving ω≈3.15, deriving vz and vx components, solving the quadratic for flight time (~0.631s), and getting a landing offset that puts the ball right at the cup center (x≈1.56) — confirming the trajectory works. I note that adding an end wall could shift where the weight first lands on the plank, though the exact landing point there isn't critical. I'm now finalizing the file, setting masses and dimensions for the tray walls, rails, and end wall box.

