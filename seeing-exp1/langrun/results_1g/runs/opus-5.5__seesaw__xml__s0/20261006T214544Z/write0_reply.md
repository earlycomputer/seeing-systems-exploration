A 1 kg ball falls about 2 m onto the raised end of a 2.1 m seesaw. A 100 g ball sits in a stop-block lip on the lowered end. A hinge limit halts the plank after 0.6 rad of rotation, and the small ball flies off.

Rough estimate:
- **Impact:** the weight hits at about 6 m/s. If it stays with the plank on impact, angular momentum gives about 4.8 rad/s.
- **Gravity during the swing:** the weight's torque raises this to about 5.6 rad/s.
- **Launch:** that throws the ball at about 5.4 m/s, aimed about 17° off vertical. This should take it roughly 1.3 m above its start, well over the 0.5 m target.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="pivot_post" type="box" pos="0 0 0.15" size="0.04 0.1 0.15" rgba="0.4 0.4 0.4 1"/>
    <body name="seesaw" pos="0 0 0.35" euler="0 0.3 0">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" limited="true" range="-0.6 0"/>
      <geom name="seesaw_plank" type="box" size="1.05 0.08 0.02" mass="0.5" rgba="0.6 0.4 0.2 1"/>
      <geom name="seesaw_stop" type="box" pos="1.03 0 0.05" size="0.02 0.08 0.05" mass="0.02" rgba="0.5 0.3 0.1 1"/>
    </body>
    <body name="weight" pos="-0.85 0 2.6">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.08" mass="1" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="0.9378 0 0.1332">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

```expect
weight touches seesaw
ball touches seesaw
seesaw reaches its lower stop
ball rises at least 0.5 m above its start
```

---
thinking (summarized):

I'm thinking through a seesaw design with equal arms: a heavy 1 kg ball drops onto one end while a lighter 0.1 kg ball sits on the other, and I need the collision physics—conserving angular momentum about the pivot with some coefficient of restitution—to launch the light ball at least 0.5 m upward.

Since MuJoCo contacts are soft rather than perfectly elastic, I'm estimating the drop height needed: the light ball needs roughly 3-5 m/s exit speed, which works out to a plank with modest inertia and a drop height around 2 m for the heavy ball. I'm also sketching the geometry—pivot height, arm length, and initial tilt angle—so the ball end starts touching the floor while the weight end is raised, giving the seesaw room to swing through on impact.

Rather than relying on the floor to stop the rotation, I'm considering using MuJoCo's joint range limits to cap the swing angle, since they behave similarly (soft but functional), and working out what tilt angle and pivot height keep the plank's low end just barely clear of the floor at the limit.

For the ball to rest properly on a tilted plank, I realize it would naturally roll downhill toward the low end, so I need a small stop or lip at the plank's edge to keep it in place -- and I should size the ball and weight (mass, radius) appropriately. Similarly, the weight dropped on the high end would roll back toward the pivot unless something holds it in position too.

Now I'm figuring out the rotation geometry: setting the pivot at the origin with the weight side at negative x and ball side at positive x, determining that a positive rotation about the y-axis lowers the +x end, so I need roughly a 17° tilt to start with the ball end down, and working out the quaternion for that rotation.

With the ball on the +x side, torque rotates the hinge positive toward the floor, so I'll set the range to roughly -0.62 to 0.02 so it rests near the limit before the weighted side drops and flings the ball off. I'm working out the tilted body frame geometry—placing the plank at height 0.35 with a 0.3 rad y-rotation and sizing the box geometry to figure out where the ball sits relative to center.

I'm applying the rotation transform to convert the ball's body-frame coordinates into world coordinates, computing the stop block's position and half-sizes to check where it collides with the plank's edge.

Checking the symmetric case confirms the same clearance at the other rotation limit. Now I'm computing where the weight's initial top corner lands in world coordinates to position it correctly relative to the slanted surface.

Estimating the drop height for the weight (roughly 1.9m fall, giving an impact speed near 6.1 m/s), then using angular momentum conservation to find the resulting swing: treating the collision as roughly inelastic since MuJoCo's default contact damping tends to make the weight stick on impact, I'm working out the lever arms and total moment of inertia needed to get the ball end's resulting speed.

With the vertical velocity component around 5.2 m/s, that gives a height of about 1.37 m, which is well within margin. I'm checking whether the ball's subsequent trajectory could bring it back to strike the weight or plank, estimating a landing point around x=-0.6 m, but this doesn't seem to be a real concern since the height clearance is what matters most.

The stop block is still necessary though—during acceleration the ball needs centripetal force (~30 m/s²) that gravity alone can't provide, so it would slide outward along the plank without the block holding it in place. I'm also considering whether the weight might briefly separate from the plank after impact and whether its contact with the slanted surface could cause it to bounce.

For the success conditions, I need to figure out how to phrase measurable outcomes like "ball rises at least 0.5 m above its start," "weight touches seesaw," or "seesaw reaches its lower stop"—trying to match the expected format from the examples while being specific about which end and which direction.

I'm placing a static pivot post geom under the plank's pivot point and checking clearances so it doesn't collide with the plank at various tilt angles, computing the plank's bottom height at tilt extremes to confirm it clears the post.

I'll skip defining a keyframe since initial body positions already work fine for the hinge, weight, and ball — default friction is okay, with the weight mass set to 1 and the ball mass set to 0.1 via the geom attribute.

