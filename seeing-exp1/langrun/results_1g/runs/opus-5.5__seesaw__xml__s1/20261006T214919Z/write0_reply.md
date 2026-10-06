The seesaw starts tilted, with the ball's end down against its hinge stop. A small lip holds the 100 g ball in place. The 1 kg weight falls about 1.4 m onto the raised end, about 0.4 m from the pivot, and drives the plank to its opposite stop. That flings the ball upward.

My hand estimate for the ball's launch speed is about 4 m/s, which would carry it roughly 0.8 m up, comfortably over 50 cm. This is a calculation only; I have not run the scene.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>
    <body name="base" pos="0 0 0">
      <geom name="base_post" type="box" size="0.03 0.08 0.1" pos="0 0 0.1" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    </body>
    <body name="seesaw" pos="0 0 0.25">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" limited="true" range="-0.3 0.3" damping="0"/>
      <geom name="seesaw_plank" type="box" size="0.5 0.06 0.01" mass="0.2" rgba="0.6 0.4 0.2 1"/>
      <geom name="seesaw_lip" type="box" size="0.01 0.06 0.03" pos="-0.49 0 0.04" mass="0.01" rgba="0.5 0.3 0.1 1"/>
    </body>
    <body name="weight" pos="0.38 0 1.8">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.05" mass="1.0" rgba="0.2 0.2 0.2 1"/>
    </body>
    <body name="ball" pos="-0.4417 0 0.156">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="-0.3  0.38 0 1.8 1 0 0 0  -0.4417 0 0.156 1 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
weight touches seesaw
seesaw reaches its upper stop
ball rises at least 0.5 m above its start
```

---
thinking (summarized):

I'm thinking through a seesaw catapult design: a hinged plank with arms about 0.5 m long, lightweight at 0.2 kg, where a 1 kg ball dropped on one end launches a 100 g ball on the other end at least 50 cm high, with the heavier ball's end starting near the ground.

Running through the collision physics with moments of inertia and angular momentum conservation, I estimate a drop height around 0.68 m gives roughly the needed launch velocity, but then I reconsider since the plank keeps rotating with the weight attached until it slams into the ground, abruptly stopping and flinging the light ball free. Trying a larger drop height of 2 m instead to make sure there's enough margin for the ball to actually clear 50 cm.

I realize there's still a practical issue though: with the plank tilted ball-end-down, the ball would just roll off the low end before impact, so I need a small lip or stop at that end to hold it in place until the weight drops. I'm also considering whether starting the plank level instead would be simpler, though that raises its own balance questions with the mismatched masses.

Working through the geometry now: pivot height, plank half-length, and tilt angle all interact, so I'm computing the angle needed for the ball end to touch the floor and checking whether a shallower pivot height gives a gentler, more usable tilt instead of resting the plank directly on the floor via contact physics.

I need to work out the ball's resting position against a lip at the plank's lower end, computing its local coordinates relative to the plank's tilt so it sits just inside the lip box at the correct height above the plank surface.

Rotating that local point by the plank's -0.3 radian tilt about y, I get the ball's world coordinates relative to the pivot, placing it at roughly (-0.44, 0, 0.155). I'm also checking that gravity will pull the ball downhill against the lip as intended.

Now computing the weight's placement at the other end: a 1 kg sphere of radius 0.05 (density ~1910) dropped near x=+0.4 in plank coordinates, applying the same rotation transform to find its world position.

Then I calculate the drop and impact: falling about 1.37 m gives ~5.2 m/s, and treating the collision as inelastic yields roughly ω=10.3 rad/s, pushing the ball end up at ~4.6 m/s — though the plank will actually hit its rotational limit at 0.3 rad before completing full travel, so I need to account for that constraint on the ball's rise.

As the plank rotates, the ball slides outward toward the lip and launches upward at an angle, roughly perpendicular to the plank's surface and tilted toward the pivot side — I'm working out that launch velocity vector using ω×r with the ball positioned near the -x end.

Now I'm thinking about the hinge limit stiffness and plank mass properties, plus adding a static support base under the pivot — I need to make sure the base doesn't intersect the plank as it rotates, so I'm keeping the base top just below the plank's lowest swept point.

For success conditions, I'm settling on phrases like "weight touches seesaw", "seesaw reaches its upper stop", and "ball rises at least 50 cm above its start" to match the expected outcome formats.

For the keyframe, I need to order qpos correctly: hinge first, then weight's freejoint (7 values), then ball's freejoint (7 values), setting positions and orientations so the scene starts correctly rather than defaulting to horizontal. Friction, condim, and solver settings should be fine with defaults.

