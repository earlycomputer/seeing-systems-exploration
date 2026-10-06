The 1 kg weight falls about 1.95 m onto the raised end of a 1 m plank. The 100 g ball sits against a small lip on the lowered end, so it can't roll off before launch. When the heavy end slams down onto the floor, the plank stops and the ball keeps going. By a hand estimate it leaves at roughly 4–5 m/s and rises well over 50 cm. I have not run this file in MuJoCo; the margin rests on that calculation.

```xml
<mujoco model="seesaw_launcher">
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- fulcrum support (visual only) -->
    <body name="fulcrum" pos="0 0 0">
      <geom name="fulcrum" type="box" size="0.04 0.06 0.07" pos="0 0 0.07" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    </body>

    <!-- seesaw: pivot at z=0.16, tilted so the +x end is up and the -x end rests on the floor -->
    <body name="seesaw" pos="0 0 0.16" euler="0 -17.5 0">
      <joint name="pivot" type="hinge" axis="0 1 0" pos="0 0 0" damping="0"/>
      <geom name="plank" type="box" size="0.5 0.05 0.01" mass="0.3" rgba="0.7 0.5 0.3 1"/>
      <geom name="lip" type="box" size="0.01 0.05 0.025" pos="-0.49 0 0.035" mass="0.01" rgba="0.5 0.3 0.2 1"/>
    </body>

    <!-- 1 kg weight dropped from rest above the raised end -->
    <body name="weight" pos="0.3785 0 2.3">
      <freejoint name="weight_free"/>
      <geom name="weight" type="sphere" size="0.06" mass="1" rgba="0.2 0.2 0.8 1"/>
    </body>

    <!-- 100 g ball resting on the lowered end against the lip -->
    <body name="ball" pos="-0.4299 0 0.0769">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0  0.3785 0 2.3 1 0 0 0  -0.4299 0 0.0769 1 0 0 0" qvel="0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

How the 50 cm target is met:

- **Impact speed.** The weight hits the plank at about 6.2 m/s.
- **Momentum transfer.** The ball end starts moving at about 5 m/s. This follows from angular momentum about the pivot, with a light plank and a nearly inelastic soft contact.
- **Launch.** The plank swings through about 35° until its heavy end strikes the floor and stops it. At that point the ball's velocity is about 95% vertical.
- **Height.** Ideally the ball would rise about 1 m. That is roughly double the required 50 cm, which leaves room for losses from the soft contact.

---
thinking (summarized):

I'm thinking through the physics of a seesaw launcher: a 1 kg ball dropped onto one end needs to fling a 0.1 kg ball at least 0.5 m into the air from the other end, via a pivot transferring momentum between the two sides.

I calculate needed launch velocity ≈3.13 m/s (aiming for ~5 m/s), then design plank dimensions, drop height, and use angular momentum conservation through an inelastic collision to estimate the resulting end speed (~5.25 m/s), accounting for plank inertia and rotation until the heavy end hits the floor and releases the light ball.

Checking the vertical component of ball velocity at launch gives a height gain of about 1.15 m, which clears the 0.5 m target with good margin, though I note MuJoCo's soft contact model could reduce this somewhat. A concern arises though: since the ball sits at the lower, tilted end of the plank, it might roll toward the pivot instead of staying put before launch.

So I need a physical stop — a small lip or cup at the ball's end of the plank, about 0.03m tall against a 0.04m radius ball, positioned outboard so it doesn't interfere with the ball's perpendicular launch trajectory once the plank snaps. Now I'm figuring out where to position the dropped weight above the raised end of the plank, based on the pivot location and plank angle.

For the seesaw geometry, I'm deciding the ball sits at the -x end on the floor while the weight end at +x is raised, with gravity holding the ball-end down naturally since that's where the ball mass is. To tilt the +x end upward, I'm working out that a rotation about the y-axis by -17.5 degrees achieves this, using Euler angles in degrees for the body orientation.

Now I'm working out the plank's box dimensions and pivot placement so that the bottom corner of the lowered end actually rests flush on the floor, computing the rotated coordinates of that corner to find the correct pivot height.

Allowing roughly ±17.5° of hinge rotation should be fine. For ball placement at x=-0.45 on the plank, I'm computing world coordinates and confirming height 0.072 clears the radius of 0.04. I'm also working out the lip box's local z-offset at 0.035 for the edge stop.

Checking the lip against the floor shows no penetration, but the ball at x=-0.45 actually overlaps the lip's inner face at -0.48, so I'm adjusting the ball to x=-0.435, leaving a small 5mm gap and letting it roll into place against the stop.

Now mapping the weight's drop target at local x=0.4 to world coordinates gives roughly (0.3785, 0.29), with a ~0.63s fall time over 1.95m. The weight's effective lever arm (0.4) is close to the ball's (0.435), and it may bounce or roll off the plank after impact, which is fine given the plank's tilt during contact.

The contact physics should behave like a brief inelastic spring interaction, during which the plank starts moving while the weight end drops toward the floor and the ball end swings upward, launching the ball with a horizontal component perpendicular to the tilted plank. This seems consistent enough to proceed without worrying about edge cases like the plank striking the floor or air resistance affecting the ball.

Checking the 50cm height requirement: the ball starts around 0.075-0.077 in z and needs to reach 0.58, giving roughly a meter of travel, which should leave plenty of margin even accounting for the soft contact transfer between plank and ball.

Now I'm laying out the keyframe structure — hinge position plus the weight's free joint (7 values) plus the ball's free joint (7 values), totaling 15 qpos entries, following body tree order of seesaw, weight, then ball. I'll set the ball's quaternion to identity and all velocities to zero since the weight starts at rest and doesn't need an initial push.

Making sure the ball body's position matches its keyframe qpos since it's a separate worldbody child with its own freejoint rather than nested inside the seesaw. Assigning masses — 0.1 for the ball, 1 for the weight, 0.3 for the plank, 0.01 for the lip — and sticking with default friction, condim 3, and the implicitfast integrator before writing the final file.

