The pendulum swings down from horizontal and hits ball1 at 3.1 m/s. The impact passes along the four balls on the guided rail, and ball4 rolls off the rail end into the box on the floor. I haven't run this in MuJoCo, so the transfer and the final rest are estimates from hand calculations:

- **Ball contacts:** these use low damping so they bounce, but not fully elastically. Balls 1–3 will probably keep some forward speed and may also roll off into the box after ball4.
- **Stopping ball4:** the box has rolling friction and more strongly damped contacts so ball4 should settle well within 6 s. That margin hasn't been confirmed.
- **Pendulum:** it only collides with the balls, not with the rail or the floor.

```xml
<mujoco model="pendulum_ball_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.4 -1 2" dir="0 0.5 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.05 0 0.725">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.004" mass="0.001" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="0.1" contype="2" conaffinity="2" solref="0.01 0.1" friction="0.5 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="rail" pos="0 0 0">
      <geom name="rail_base" type="box" pos="0.235 0 0.1" size="0.265 0.04 0.1" contype="1" conaffinity="1" condim="3" friction="0.5 0.005 0.0001" rgba="0.5 0.5 0.6 1"/>
      <geom name="rail_guide_left" type="box" pos="0.235 0.0325 0.21" size="0.265 0.0025 0.01" contype="1" conaffinity="1" rgba="0.4 0.4 0.5 1"/>
      <geom name="rail_guide_right" type="box" pos="0.235 -0.0325 0.21" size="0.265 0.0025 0.01" contype="1" conaffinity="1" rgba="0.4 0.4 0.5 1"/>
    </body>

    <body name="ball1" pos="0 0 0.225">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.025" mass="0.1" contype="1" conaffinity="3" condim="3" solref="0.01 0.1" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball2" pos="0.15 0 0.225">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" mass="0.1" contype="1" conaffinity="3" condim="3" solref="0.01 0.1" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball3" pos="0.30 0 0.225">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.025" mass="0.1" contype="1" conaffinity="3" condim="3" solref="0.01 0.1" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball4" pos="0.45 0 0.225">
      <freejoint name="ball4_free"/>
      <geom name="ball4_geom" type="sphere" size="0.025" mass="0.1" contype="1" conaffinity="3" condim="3" solref="0.01 0.1" friction="0.5 0.005 0.0001" rgba="0.9 0.7 0.1 1"/>
    </body>

    <body name="box" pos="0 0 0">
      <geom name="box_floor" type="box" pos="0.9 0 0.005" size="0.38 0.13 0.005" condim="6" friction="0.8 0.01 0.01" solref="0.02 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_near" type="box" pos="0.525 0 0.07" size="0.005 0.13 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.02 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_far" type="box" pos="1.275 0 0.07" size="0.005 0.13 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.02 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_left" type="box" pos="0.9 0.125 0.07" size="0.38 0.005 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.02 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="box_wall_right" type="box" pos="0.9 -0.125 0.07" size="0.38 0.005 0.06" condim="6" friction="0.8 0.01 0.01" solref="0.02 1" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5708  0 0 0.225 1 0 0 0  0.15 0 0.225 1 0 0 0  0.30 0 0.225 1 0 0 0  0.45 0 0.225 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sketching out a Newton's cradle-style chain reaction: a pendulum bob drops from 0.5 m to strike a line of balls, with momentum propagating through to the last ball, which rolls into a box and settles. I'm working through the pendulum geometry, choosing an arm length of 0.5 m released from horizontal, and calculating the impact speed at the bottom using energy conservation.

I'm reasoning about ball spacing along the rail and how collisions will transfer momentum given MuJoCo's imperfect elasticity between equal masses, accepting that balls may bunch together as they move forward, as long as ball4 ends up resting in the box per the chain order requirement. Now I'm thinking through how to physically constrain the balls to the rail, likely with side guides or a channel geometry to keep them moving in a straight line.

The box just needs to catch ball4 without worrying about others drifting in. I'll tune solref toward a more elastic, less damped contact (something like "0.01 0.1") so impacts transfer momentum more distinctly rather than everything clumping together, while keeping timeconst safely above twice the timestep. With condim 3 the spheres should roll naturally on the plane, sliding briefly right after impact since they're struck at center height.

For the box floor, I'm considering condim 6 with rolling friction so the ball actually comes to rest instead of rolling forever, estimating a small rolling friction coefficient against the ball radius to get a reasonable deceleration.

Simpler plan: let the rail end and drop the ball into a separate box sitting lower on the ground, with walls to catch it and let rolling friction plus damping bring it to rest — rail elevated, box below catching the fall.

Now I'm working out the pendulum geometry: ball radius 0.025, rail top at z=0.2 so ball centers sit at z=0.225, with the pendulum pivot placed above the first ball at (-0.05, 0, 0.725) and a 0.5-length arm. Released horizontally, the bob starts at (-0.55, 0, 0.725), hinged about the y-axis so it swings down to strike the first ball in the Newton's cradle line.

I'm checking whether after a collision an inelastic pendulum would keep moving and strike the ball again, or whether it swings forward past the contact point into the rail region where the balls sit -- need to make sure the geometry doesn't cause unwanted overlap.

Actually, the edge-of-rail contact seems negligible since the gap is sub-millimeter, so I shouldn't worry about it — ball1 would get struck first anyway. Instead of fine-tuning geometry, I could just assign different contype/conaffinity values to the pendulum bob so it simply doesn't collide with the rail at all.

I'm estimating the restitution from the damping ratio and deciding to keep the arm mass small so the bob behaves like the effective mass in the chain, then setting ball mass to match a steel sphere's density rather than worrying too much about exact elasticity.

Working through the impact sequence: pendulum hits ball1 at 3.13 m/s, transferring most velocity forward while the pendulum retains a small residual and swings back. I'm tracing how balls 1-3 drift forward incrementally after each collision and considering whether they'd eventually roll off the rail into the box, which could complicate the later "ball4 enters box" event.

I'm reasoning that without rolling friction a ball on the rail never naturally stops, so I may need to add slight friction or shorten the rail so ball4 reaches the end quickly. I'm also accounting for how sliding friction converts ball1's velocity to 5/7 of its initial speed once it starts pure rolling, and how its retained spin lets it keep moving forward even after striking ball2.

They'll likely roll off the end into the box eventually, which is fine as long as the box is sized to catch them without disrupting ball4 — there's enough time before that matters. Working through the rolling friction deceleration formula for a sphere, I get roughly 0.56 m/s² with μ_r=0.002, and I'm estimating that ball1 slides off the pendulum at ~2.8 m/s before settling into a rolling speed around 2.0 m/s.

Since the gap between balls is small, ball1 is still sliding (not fully rolling) when it hits ball2, so the momentum transfer is a bit messy to model exactly, but the forward push should carry through the chain so ball4 ends up with at least ~1 m/s as it leaves the rail. From there I'm figuring the fall time into the box based on the drop height from the rail to the box floor.

I'm positioning the box so it spans the likely landing zone (roughly x=0.5 to 1.2), with walls tall enough to catch the ball but lower than the rail height, and making sure the near wall can sit flush against the end of the rail block without overlap.

For damping, I'm checking that the box floor uses rolling friction and condim 6 so balls settle rather than skid, and that the mixed solref values between ball/box/rail contacts stay reasonably soft so collisions look natural rather than overly elastic or bouncy.

I'm also thinking through the pendulum's residual swing after impact — it should just oscillate harmlessly since nothing else is in its path — and confirming the rail's side guides are spaced to let balls sit snugly without the bob catching on them, since the bob uses different collision groups.

Now placing the four balls along the rail at even spacing, checking ball4 clears the rail edge before the next ball strikes it. I'm sketching a collection box at the end with a floor plate and surrounding walls, verifying the near wall doesn't intersect the rail's trajectory.

Then I'm working out the keyframe qpos ordering, matching the pendulum hinge and each ball's free joint in body declaration order, with absolute positions for each ball since this is an initial keyframe rather than relative offsets.

For the pendulum, I'm setting it up released from horizontal rest: a thin massless-ish capsule arm with contype/conaffinity disabled so it doesn't collide, pivoted at the top, with a small bob sphere at the end. I decide to skip adding a visual pivot support geom since it risks interfering with the mechanism.

Checking the drop height, the bob sits 0.5m above its lowest resting point, confirming the setup is correct. I'm reasoning through the impact physics — momentum transfer should be sufficient even with inelastic collision, and I'm checking that friction coefficients (sliding, rolling, torsional) across the ball, rail, and box floor are set so the ball eventually settles rather than sliding or rolling indefinitely once it lands in the box.

Tracing the ball's motion after bouncing off the far wall, I estimate a moderate restitution from the soft contact damping, then rolling friction deceleration should bring it to rest quickly, with the vertical bounce on landing also settling due to the solver's damping ratio. I'm also considering that balls 1-3 will fall in later and strike ball4, but should arrive slower and everything should settle by 6 seconds. I'm double-checking the floor plane dimensions and collision groups (contype/conaffinity) to make sure all objects interact correctly without unintended overlaps.

Checking that the pendulum bob's collision group properly interacts with the balls' collision group confirms they'll collide as intended. I'll add the timestep option and finalize the file.

