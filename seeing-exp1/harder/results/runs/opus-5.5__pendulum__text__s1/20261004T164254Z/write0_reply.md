The ball is struck at x = 0 and rolls toward a cup centred at x = 1. The cup is a box of walls standing on the floor. A shallow ramp leads up over its low front lip, so the ball rolls up, drops inside and is trapped by taller back and side walls. I have reasoned this through by hand but have not run the simulation.

**Launch.** The pendulum is a 0.5 kg bob on a 0.5 m light rod. The keyframe releases it from 45°, so it reaches about 1.7 m/s at the bottom of its swing. There it strikes the 0.05 kg ball. Taking the collision restitution as anywhere between 0 and 1, the ball should leave at roughly 1.5–3 m/s. Once it stops slipping, its rolling speed should be roughly 1.1–2.2 m/s.

**Capture.** To climb the 4 cm ramp, the ball needs a rolling speed of about 0.75 m/s or more, which this range covers. The back wall is 14 cm tall, so even the fastest case should not clear it. The front wall is 4 cm tall, higher than the ball's 3 cm radius, so the ball cannot roll back out.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="light" pos="0.5 0 2" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>
    <body name="pendulum" pos="-0.06 0 0.535">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.47" size="0.006" mass="0.02" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.03" mass="0.5" rgba="0.8 0.2 0.2 1"/>
    </body>
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.2042 0 0.0141" euler="0 -9.09 0" size="0.1266 0.06 0.005" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_front" type="box" pos="-0.08 0 0.02" size="0.01 0.09 0.02" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="box" pos="0.08 0 0.07" size="0.01 0.09 0.07" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_left" type="box" pos="0 0.08 0.07" size="0.07 0.01 0.07" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_right" type="box" pos="0 -0.08 0.07" size="0.07 0.01 0.07" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.785 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics: ball starting near the origin with radius 0.03, cup positioned around x=1.0. I need the cup to actually be reachable by a rolling ball on the floor, so I'm thinking through whether it needs a sunken opening rather than raised walls, since a rolling ball can't climb over a rim.

I'll build the cup as walls forming a U-shape open on the approach side, with a back wall to stop and contain the ball, since contacts should have enough restitution for the ball to settle without bouncing back out through the opening.

That bump idea seems unreliable without testing. I'm thinking it might be more robust to tune rolling friction so the ball settles at the cup center, though that's hard to get right analytically given MuJoCo's contact model. Maybe the cleanest fix is to control impact speed and make the back wall highly damped so it absorbs energy without bouncing, using a soft solref tuned for a high damping ratio to kill any rebound.

Maybe instead design the cup as a funnel leading to a raised interior well: a ramp climbs to a lip, then drops into the cup floor surrounded by walls tall enough to trap the ball, calculating the minimum launch velocity needed to clear the lip height against rolling resistance.

Computing fall dynamics after leaving the ramp top: with v_top≈0.94, the ball drops 0.04 m in about 0.09 s, traveling roughly 0.085 m horizontally, landing comfortably within a cup of inner diameter ~0.16 m and back wall height 0.10 m. I'm also settling on placing the cup body at x=1.0 with the ramp as an offset geom belonging to that same body.

Since rolling friction isn't modeled by default in MuJoCo (condim=3 gives no rolling resistance), the ball should preserve speed across the floor roll and ramp, needing to arrive around 0.8–1.5 m/s. For the pendulum strike, I'm unsure how much restitution the contact model effectively provides—likely somewhere in the 0.3–0.5 range given soft, critically damped contacts rather than a truly elastic collision.

Front wall is low enough and restitution weak enough that the ball likely stays in rather than bouncing back out. More concerning: checking the pendulum geometry, the bob striking the ball at its center height means the bob's bottom edge dips below the floor level—that's a clearance problem I need to fix.

I can resize the bob slightly smaller and raise its center so it still contacts the ball near mid-height while keeping its bottom comfortably above the floor, or alternatively rely on contype/conaffinity bitmasks to exclude pendulum-floor collisions entirely. Keeping physical clearance is simpler and more robust than masking, so I'll go with adjusting the bob's radius and height.

For the swing, I'll set the pivot height to L + 0.045 with L=0.5, placing it at x=-0.075 so the bob's resting position aligns horizontally with the ball for contact at the bottom of the arc. I'm computing that releasing from a 60° raised angle gives the bob roughly 2.2 m/s at impact via energy conservation, which should transfer into a reasonable rolling speed for the ball without being excessive.

Testing smaller release angles instead to tune impact speed: at 35° the bob hits at 1.33 m/s, and with bob mass 0.5 kg vs ball mass 0.05 kg, the resulting ball speed range (depending on restitution) comes out to 0.86–1.73 m/s rolling, which is a bit too close to the ramp's minimum requirement of 0.75 m/s at height 0.04. Bumping the angle up to 45° gives a bob speed of 1.70 m/s, yielding a safer rolling speed range of 1.1–2.2 m/s, so I'm leaning toward that configuration with a slightly lower ramp height of 0.03.

Now working out the pendulum's swing direction: with the pivot at x=-0.075 and rotation about the y-axis, I confirm that a positive initial angle θ=0.785 displaces the bob toward -x, and as gravity pulls it down toward θ=0, it swings toward +x — which is the direction I want it moving to strike the ball. With that geometry settled, I'm moving on to defining the ball's starting keyframe.

I'm figuring out qpos ordering across bodies -- pendulum joint values first, then the ball's freejoint position and quaternion -- and sanity-checking that at θ=0.785 the bob sits clear of the ball's resting position. I'm also sizing both spheres (ball radius ~0.03, bob radius ~0.03) and setting resting heights so each sits just above the floor with a small clearance.

Now I'm placing the pivot and rod geometry so the bob swings from (-0.06, 0, 0.535) with length 0.5, timing contact to occur right at the bottom of the swing where velocity peaks. I'm also assigning masses (ball ~0.05, rod ~0.02) and checking the thin rod capsule doesn't collide with the ball given their x-offsets, confirming the pendulum continues forward after impact.

After impact the pendulum swings up to roughly x ≈ -0.06+0.35, well short of the cup, oscillating indefinitely without damping since none is needed. I'm deciding to just specify a mass on the bob sphere directly rather than relying on density, and confirming the hinge needs no joint limits. Now I'm working out where to place the cup body and the ball's starting position.

Placing the cup center at x=1.0 with the ball starting at x=0 gives a 1-meter gap, and I'm designing the cup as a square-walled box structure: front wall shorter (top at 0.03) with back and sides taller (0.12), inner half-size 0.07, wall thickness 0.01. I'm working out the ramp geometry so its top edge aligns with the front wall's top surface at roughly x≈0.92, z=0.03, giving a ramp run of 0.25 starting at x=0.67 and computing the resulting incline angle.

Still computing ramp geometry...

So I set euler to "0 -6.84 0" for the tilt. I'm also noting that the box's bottom corner may dip slightly below the floor plane, but since the cup is a static body welded to world with no joint, MuJoCo should skip contacts between static-static geom pairs anyway, so that penetration shouldn't cause collision issues.

For the ramp, I made the top surface meet the floor exactly at z=0 where the ball transitions on, but I'm wondering if the leading edge creates numerical contact issues right at that corner, so I might nudge the ramp down by a millimeter to make the leading edge slightly buried rather than exactly flush.

The wall top edge at x 0.91-0.93 then drops inside; I decide to skip adding a cup base since the floor plane works fine for the ball to rest on. I'm checking that the ramp-to-floor kink is small enough not to disrupt the ball's motion, then tracing the ball's path as it falls off the wall edge into the cup toward the back wall.

Hitting the back wall inner face, the ball rebounds toward the front wall, but I realize the front wall's height exactly equals the ball's radius, meaning contact happens right at the corner with a purely horizontal normal — the ball physically can't climb that step since its center is level with the edge, so it would just bounce back rather than escape over the wall.

So I'm reconsidering with the front wall taller, say h=0.04, checking whether the rolling speed estimate (~1.1) clears the required threshold (~0.75) for mounting that step. Recomputing the restitution bounds, taking e≥0 gives ball speed around 1.55, and after accounting for rolling friction losses (5/7 factor), I get roughly 1.1 for the post-slip rolling speed, which should be enough to climb the taller step.

I'm also checking contact geometry details—ball hitting at height 0.035 versus the pendulum's center at 0.03 means the contact normal is slightly downward, which seems fine, and the pendulum hinge shouldn't interfere with collision dynamics. For the ramp with h=0.04 and run 0.25, I compute the incline angle as about 9.09°, with the ramp spanning from x=0.67 to the wall at x=0.92, giving a top surface length of about 0.253 and half-length 0.1266, with sinα≈0.158 and cosα≈0.987.

Computing the ramp's position in the cup's local frame after shifting it down by 1mm, converting to the cup body coordinates, and setting the orientation angle—since the ball travels straight along x with no lateral offset, it should stay centered at y=0 and fit within the cup's inner width of 0.14 without issue.

Now I'm laying out the four cup walls using the inner half-width of 0.07 plus wall thickness, placing front, back, left, and right walls at their respective positions and sizes, then tracing the ball's path as it clears the front wall's top edge, falls into the interior, and eventually strikes the back wall across the 0.14 interior length.

The ball will likely oscillate between front and back walls, bleeding energy through bounces until it settles near the cup's center, well within the ±0.04 tolerance. I'm confirming that the ramp's overlap with the box wall at the landing zone is harmless since they're static geoms, and default friction values should suffice without needing rolling friction. Now I'm setting up the pendulum hinge, placing the pivot body so the bob's bottom center sits at z=0.035 given a rod length of 0.5, meaning the pivot itself sits at z=0.535.

I'm defining the rod as a thin capsule and the bob as a sphere sized to overlap slightly with the rod's end so they connect properly. I'm considering whether to add a visual support post for the pivot but deciding it's unnecessary extra geometry that could risk unwanted collisions, so I'll skip it and keep things minimal.

Checking the restitution bounds for the collision: with low e the pendulum just swings gently through its arc without ever re-engaging the ball, which confirms the hinge and initial angle setup (θ=0.785 giving bob height ~0.181) are consistent. I'm also verifying the energy math for the ball's speed at the top of the ramp under different restitution values, confirming the rolling versus sliding velocity estimates look reasonable.

I'm checking the full trajectory — the time to clear the ramp, the airborne arc, and the back wall rebound — all comfortably fit within the 6-second simulation window. I'm now moving to write the actual MuJoCo XML file, setting up the floor plane, lighting, pendulum hinge with proper clearance from the floor, and the ball's geom properties including contact dimension settings.

