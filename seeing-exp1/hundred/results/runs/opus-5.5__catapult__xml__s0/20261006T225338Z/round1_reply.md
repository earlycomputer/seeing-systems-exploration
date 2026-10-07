## What happened in the run

- **Pendulum and cart worked.** The pendulum swung down and hit the cart at 0.46 s.
- **Cart and weight worked.** The cart pushed the weight off the shelf at about 0.4 m/s, and the weight landed in the seesaw's tray at 1.09 s.
- **The seesaw never reached its lower stop.** As the weight end swung down, the plank struck the shelf at 12.9°. My mistake was making the shelf a solid block down to the floor: the plank's weight end swings back under the shelf's edge.
- **The ball launch was too weak.** Because the seesaw stopped early, the ball rose only to 0.48 m. It clipped the cup's near wall and fell to the floor outside the cup.

## Fix

- **Shelf.** It is now a thin slab whose underside is at z ≈ 0.505 m. The plank, tray and stop all pass beneath it.
- **Seesaw position.** I moved the seesaw 3 cm closer to the shelf. This centres the tray under the weight's measured 0.4 m/s fall.
- **Everything downstream** moved by the same 3 cm: the lower stop, the seesaw stand, the ball and the cup.

```json
{"what_happens": "The pendulum hits the cart, which pushes the weight off the shelf into the seesaw tray. The seesaw's weight end then collides with the underside region of the shelf at 12.9° instead of reaching its lower stop. The ball is only weakly tossed, clips the cup's near wall, falls to the floor outside the cup and rests at x≈0.97 m.", "works": false, "problem": "The shelf is a solid block reaching the floor, so the seesaw plank hits it before reaching its lower stop, and the weak launch drops the ball outside the cup."}
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
      <geom name="seesaw_plank" type="box" pos="0.04 0 0" size="0.40 0.06 0.01" mass="0.2" rgba="0.2 0.7 0.3 1"/>
      <geom name="seesaw_tray_wall" type="box" pos="-0.185 0 0.03" size="0.005 0.06 0.02" mass="0.02" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_a" type="box" pos="-0.275 0.055 0.02" size="0.085 0.005 0.01" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_rail_b" type="box" pos="-0.275 -0.055 0.02" size="0.085 0.005 0.01" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_post" type="box" pos="0.40 0 0.03" size="0.008 0.008 0.02" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_pad" type="box" pos="0.40 0 0.055" size="0.033 0.03 0.005" mass="0.01" rgba="0.2 0.5 0.3 1"/>
      <geom name="seesaw_lip" type="box" pos="0.430 0 0.066" size="0.003 0.03 0.006" mass="0.002" rgba="0.2 0.5 0.3 1"/>
    </body>

    <body name="ball" pos="1.1311 0 0.2518">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.02" mass="0.02" condim="6" friction="0.8 0.01 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="cup" pos="1.395 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.19 0.15 0.01" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.18 0 0.16" size="0.005 0.15 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_far" type="box" pos="0.18 0 0.16" size="0.005 0.15 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.145 0.16" size="0.175 0.005 0.14" rgba="0.3 0.6 0.9 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.145 0.16" size="0.175 0.005 0.14" rgba="0.3 0.6 0.9 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5708 0 0.245 0 0.585 1 0 0 0 0.36 1.1311 0 0.2518 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm recalculating the collision geometry — tracking the plank's rotated end position as it swings to find where it actually contacts the shelf at 13°, since my earlier x-coordinate math was off.

Separately, I'm checking the ball launch: a weak rotation stop meant the ball barely rose and bounced off the wall, landing on the floor and rolling back; the weight also left the shelf slower than expected before settling near the tray.

To fix the overlap, I'm considering shortening the weight side of the plank so its end clears the shelf edge with margin, verifying the worst-case corner position at θ=0 gives enough clearance from 0.40.

I'm also re-solving the landing trajectory with the adjusted shelf edge (0.37) and plank end (−0.33), recomputing where the weight intersects the tray wall line given its exit speed of 0.42 m/s to confirm the geometry still works.

Trying to shift the seesaw pivot left to hit a target landing spot, but that creates a new collision between the plank end and the shelf edge at horizontal position — the geometry keeps conflicting no matter how I adjust the pivot. I'm now wondering if raising the shelf relative to the seesaw would let the plank pass beneath the shelf top instead of colliding with it.

So the tray needs to sit beyond the slab edge horizontally so the falling weight actually lands in it. Settling on slab dimensions (x center 0.235, half 0.165, z 0.505–0.545) with the cart bottom clearing fine, I check the plank end and stop block positions at θ=0 and confirm the contact geometry lines up — stop top matches plank bottom. Now I'm ready to verify the landing trajectory for v=0.4 with Xp=0.75.

For better centering I try shifting the pivot to Xp=0.72, which moves x_b to roughly −0.30 for v=0.4, −0.243 for v=0.7, and −0.316 for v=0.3 — all reasonable. Since shifting Xp by −0.03 moves everything seesaw-related (stop, stand, ball, cup) correspondingly, I recheck the plank end positions at both θ=0 and tilted states to confirm they stay clear of the slab edge.

I'm now checking the tray rails and falling weight clearance relative to the slab, confirming the weight lands within the tray rather than missing it, and placing the stop block under the plank's weight end at θ=0 to make sure the falling weight doesn't hit it prematurely. I also verify the pendulum and shelf positions don't collide, then shift focus to why the ball launch is weak — it looks like the seesaw stopped at only 13° due to a shelf collision.

With the fix allowing full rotation, I estimate the ball should launch with enough speed since the gravitational work over the full 20.6° swing is much greater than the partial 7.6° rotation that caused the earlier weak launch. I'm now adjusting positions by shifting everything -0.03 to fix clearance, updating the seesaw, stand, and stop block coordinates accordingly.

Checking v=0.9 and v=0.7 cases, both land within the wall bounds, confirming the trajectory holds across a reasonable speed range. The weight-plank-tray contact sequence and pivot height remain consistent, so I'm ready to write the file.

