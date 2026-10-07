The pendulum is a 0.5 m arm released horizontally, so its bob starts exactly 0.5 m above its lowest point. At the bottom it hits ball1, and the impacts pass along the rail through ball2 and ball3 to ball4. Ball4 then rolls off the end of the rail and drops into the box. I have not run this file, so how the impacts and the landing play out is a design estimate.

- **Impacts:** the balls and the bob have lightly damped contacts so the hits are fairly elastic.
- **Box:** the box surfaces have strong rolling friction so ball4 comes to rest after landing.
- **Rail:** the rail has normal friction so the balls keep rolling along it between hits.

```xml
<mujoco model="pendulum_ball_chain_box">
  <option timestep="0.002"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="light_main" pos="0.6 -1.5 2.5" dir="0 0.5 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Pendulum: pivot 0.5 m above the bob's lowest point (bob center z = 0.325 at bottom) -->
    <body name="pendulum" pos="0 0 0.825">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.004" mass="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="0.2" friction="0.3 0.005 0.0001" solref="0.02 0.15" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- Four equal balls on the rail, centers 0.15 m apart -->
    <body name="ball1" pos="0.052 0 0.325">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.025" mass="0.2" friction="0.3 0.005 0.0001" solref="0.02 0.15" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="ball2" pos="0.202 0 0.325">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" mass="0.2" friction="0.3 0.005 0.0001" solref="0.02 0.15" rgba="0.2 0.6 0.8 1"/>
    </body>
    <body name="ball3" pos="0.352 0 0.325">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.025" mass="0.2" friction="0.3 0.005 0.0001" solref="0.02 0.15" rgba="0.2 0.8 0.6 1"/>
    </body>
    <body name="ball4" pos="0.502 0 0.325">
      <freejoint name="ball4_free"/>
      <geom name="ball4_geom" type="sphere" size="0.025" mass="0.2" friction="0.3 0.005 0.0001" solref="0.02 0.15" rgba="0.9 0.7 0.1 1"/>
    </body>

    <!-- Level rail: top surface at z = 0.3, from x = 0.03 to x = 0.6 -->
    <body name="rail" pos="0 0 0">
      <geom name="rail_beam" type="box" pos="0.315 0 0.29" size="0.285 0.04 0.01" rgba="0.5 0.4 0.3 1"/>
      <geom name="rail_leg1" type="box" pos="0.1 0 0.14" size="0.01 0.01 0.14" rgba="0.5 0.4 0.3 1"/>
      <geom name="rail_leg2" type="box" pos="0.55 0 0.14" size="0.01 0.01 0.14" rgba="0.5 0.4 0.3 1"/>
    </body>

    <!-- Catching box on the floor beyond the rail end: interior x 0.64..1.40, y -0.2..0.2 -->
    <body name="box" pos="0 0 0">
      <geom name="box_base" type="box" pos="1.02 0 0.005" size="0.39 0.21 0.005" condim="6" friction="1 0.02 0.02" rgba="0.3 0.6 0.3 1"/>
      <geom name="box_wall_near" type="box" pos="0.635 0 0.105" size="0.005 0.21 0.095" condim="6" friction="1 0.02 0.02" rgba="0.3 0.6 0.3 0.6"/>
      <geom name="box_wall_far" type="box" pos="1.405 0 0.205" size="0.005 0.21 0.195" condim="6" friction="1 0.02 0.02" rgba="0.3 0.6 0.3 0.6"/>
      <geom name="box_wall_left" type="box" pos="1.02 0.205 0.105" size="0.38 0.005 0.095" condim="6" friction="1 0.02 0.02" rgba="0.3 0.6 0.3 0.6"/>
      <geom name="box_wall_right" type="box" pos="1.02 -0.205 0.105" size="0.38 0.005 0.095" condim="6" friction="1 0.02 0.02" rgba="0.3 0.6 0.3 0.6"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="exclude_pendulum_rail" body1="pendulum" body2="rail"/>
  </contact>

  <keyframe>
    <key name="start" qpos="1.5708  0.052 0 0.325 1 0 0 0  0.202 0 0.325 1 0 0 0  0.352 0 0.325 1 0 0 0  0.502 0 0.325 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm designing a Newton's cradle chain where the last ball rolls into a box and rests. Working through the pendulum setup: with a 0.5 m length released horizontally, I calculate the speed at the bottom of the swing using energy conservation, getting roughly 3.13 m/s.

With balls spaced 0.15 m apart on a flat rail, the impacts happen sequentially rather than cradle-style since there are gaps between centers, and MuJoCo's contacts being somewhat soft/inelastic plus rolling spin effects will make the collision chain messy but workable. I just need to size the box so the final ball enters and comes to rest—other balls ending up wherever is probably acceptable as long as that condition holds.

For the pendulum, I'll make the bob a sphere matching the balls' radius and mass so momentum transfers cleanly, hinged along y so it swings in the x-z plane and strikes ball1 right at the bottom of its arc, with the bob center aligned to ball-center height. The rail itself will be a box surface with ball centers sitting at rail-top-plus-radius height, and the last ball rolls off the end and falls into a catch box positioned beyond the rail. Since default contacts have no rolling friction, I'm thinking about how speed losses occur only through collisions and impacts with the box walls, and whether restitution there is enough to let the ball settle rather than bounce around indefinitely.

At 0.05 rolling friction the decel is around 14 m/s², which would kill rolling quickly on impact while keeping the rail at default low rolling friction so balls still travel freely there. Since contacts take the max friction/condim between two geoms, applying this only to the box geoms should localize the extra damping to wall collisions without affecting rail motion.

I also need to make sure the pendulum bob doesn't graze the rail at the bottom of its swing. I'm positioning ball1's center just past the pivot by about two radii plus a small gap, and starting the rail a bit further out so the bob clears it, placing everything relative to the radius value.

There's a risk the bob corner grazes the rail edge, so I'll just add an explicit exclude between the pendulum and rail bodies to sidestep collision issues entirely, rather than fine-tuning geometry. I should also check whether the rod capsule could clip ball1 and add a similar exclusion if needed.

Now I'm figuring out the pendulum's starting orientation: with the hinge about the y-axis and bob offset along -z in the body frame, rotating by θ=π/2 places the bob at x=-L, level with the pivot, so it starts horizontal on the -x side and swings toward +x -- giving qpos=1.5708 as the initial keyframe value.

I'm checking whether this gives too much speed at the bottom (~3.13 m/s), considering whether a support structure is needed for the pivot, and thinking through friction losses as the struck ball transitions from sliding to rolling before reaching the box.

Tracing the collision chain through the balls: each impact transfers linear velocity while leaving spin behind, so successive balls slide before friction brings them to rolling, and with the 0.1 m gap between balls, they're likely still sliding when they strike the next one in line.

I'm also reconsidering the elasticity assumption — MuJoCo's default contact solver with critical damping (dampratio=1) produces very little bounce, so these collisions are closer to perfectly inelastic rather than elastic, meaning equal-mass impacts would leave both balls moving near v/2 instead of transferring velocity cleanly.

To get a proper Newton's-cradle-style transfer where impacts pass through cleanly, I need to lower the damping ratio (like dampratio~0.1, giving restitution around 0.7) and tune solref parameters so the contact timeconst stays above twice the timestep, which affects how long each collision event lasts.

Trying solref="0.02 0.15" gives ω≈333, half period ~9.4ms over 5 steps, restitution around 0.62 — reasonable since contacts mix via solmix and most geoms share the same values. I'm second-guessing whether elasticity even matters here; the test likely just checks that ball4 ends resting in the box and the contact ordering, so even fully inelastic collisions should satisfy that.

Now I'm working out the physical layout: rail positioned at z=0.3 with the pivot at (0, 0.825), balls spaced 0.15m apart along the rail starting at x=0.052, and computing the rail's box dimensions (half-size and center) so it supports the balls with enough length for the last one to roll before hitting the edge.

I'm considering adding thin side lips along the rail edges to keep the balls from drifting in y, though since the collision is purely along x and symmetric, this is mostly a safety margin. I'll keep the design simple — the lips barely interact with the balls unless there's slight drift — and now move to working out ball4's projectile motion once it leaves the rail edge at some launch speed.

Working through the fall from the rail's exit height to the box floor, I compute the drop time and resulting horizontal travel distance across the expected speed range, which spans roughly 0.19 to 0.73 meters. I need to size the box and its near wall carefully so it stays low enough to clear the ball's trajectory at launch without interfering.

I'm also wondering whether the pendulum keeps swinging after impact and could swing forward again to hit ball1 a second time if it hasn't moved far enough away — with restitution 0.6, the bob retains some forward speed, so I'm considering whether a bit of hinge damping is needed, though it's probably negligible enough to leave alone.

Now I'm working out masses: using steel density to estimate ball mass gives roughly 0.5 kg, but I'll just set explicit mass values like 0.2 for the balls and bob, and a small mass like 0.01 for the connecting rod so it doesn't meaningfully affect the pendulum's swing speed at the bottom.

For the floor and walls, I'm setting up box geoms with rolling friction around 0.02, which gives a reasonable deceleration rate for the rolling ball. I'm also checking that the contact solref settings between materials (ball-box, ball-ball) will blend to produce low-bounce, realistic collisions rather than excessive bouncing.

I considered adding a grooved rail with two parallel thin rods for lateral stability, but the geometry gets complicated, so I'll stick with a flat box rail instead. Now I'm working out the exact resting height for the pendulum bob so it aligns properly with the other ball.

Checking the clearances: ball1 sits a couple millimeters from the bob with no overlap, and the rail's starting edge is far enough from the bob's sphere that there's no collision at the corner. I'm placing the rail geometry at the right world position with its box dimensions set.

Now I'm working out the box interior dimensions and wall placements — near wall, far wall, and side walls — computing their centers and half-extents so they properly bound the x 0.64–1.40, y ±0.2 interior space, then verifying ball4's path clears the near wall's top edge.

Tracking the ball's trajectory at v=0.5: computing when its center passes the wall corner at x=0.64, checking the drop height against the corner position (0.64, 0.25), and confirming the clearance distance stays positive so the ball doesn't clip the corner.

Lowering the wall height near the edge to 0.2 for extra safety margin, with side walls matching that height. Now I need to construct the full keyframe qpos vector: one pendulum hinge angle plus four free joints (7 values each) for the balls, listed in body tree order — pendulum first, then the balls — with each ball resting at z=0.325 on top of the 0.3-height rail, and the pendulum hinge set to 1.5708 radians.

There's minor overlap from contact softness, which is acceptable. I'll skip adding a pivot post for the visualization and just write the file. Thinking through the dynamics: ball4 settles in the box, but ball3 could roll slowly forever on the frictionless rail and eventually fall in too, which is fine. The trickier question is whether the still-swinging pendulum could strike ball1 again if ball1 hasn't rolled far enough away after its collision with ball2.

Given the pendulum's swing period of about 1.4 seconds, it seems unlikely ball1 would end up back near the pivot. I don't think hinge damping is necessary to settle things down. I'll just confirm gravity defaults are fine and write the file.

