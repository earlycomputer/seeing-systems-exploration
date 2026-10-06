The seesaw is a light 1.5 m plank on a hinge 0.25 m up, limited to ±0.3 rad and starting with the ball end down. A small lip keeps the 100 g ball (start height z ≈ 0.11 m) from rolling off the low end. The 1 kg weight falls about 1.1 m onto the raised end.

By hand estimate (not a simulation run), the plank's end tip should reach about 4 m/s, so the ball rises roughly 0.8 m or more above its start.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="fulcrum" type="box" pos="0 0 0.1" size="0.03 0.08 0.1" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="seesaw" pos="0 0 0.25">
      <joint name="pivot" type="hinge" axis="0 1 0" limited="true" range="-0.3 0.3"/>
      <geom name="plank" type="box" size="0.75 0.06 0.02" mass="0.3" rgba="0.7 0.5 0.3 1"/>
      <geom name="lip" type="box" pos="0.73 0 0.05" size="0.02 0.06 0.03" mass="0.01" rgba="0.5 0.3 0.2 1"/>
    </body>
    <body name="weight" pos="-0.615 0 1.6">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.06" mass="1.0" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="0.6578 0 0.110">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.3 -0.615 0 1.6 1 0 0 0 0.6578 0 0.110 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm designing a seesaw catapult mechanism: a pivoted plank with a 1 kg ball dropped on one end to launch a 100 g ball at least 0.5 m high from the other end, working out pivot height, arm lengths, and initial tilt geometry.

Estimating drop height and impact speed, I'm considering asymmetric arm lengths (longer ball-side arm) to amplify the launch velocity beyond what a symmetric seesaw would give, since a symmetric design only yields about 0.8 m of rise — enough but with little margin.

Rather than modeling floor contact for each end, I think it's simpler to just constrain the hinge with a joint angle limit instead. I'll set pivot height at 0.25, with symmetric 0.75 arms and 0.04 thickness, weight end at -x and ball end at +x, then work out the rotation math to confirm initial ball-down orientation.

I'll just rely on the joint limit rather than floor contact to stop the plank's motion. But I realize the tilted plank would actually let the ball roll off the low end, so I need to add a small lip or stop at the end of the plank to keep the ball in place, positioning it near that lip.

Now I'm working out the launch dynamics: when the plank rotates upward, the ball at the end gets thrown in a direction perpendicular to the arm, which I need to compute based on the arm's tilt angle and rotation direction.

I also need to figure out where the dropped weight should land on the plank's opposite end, and compute the surface height there based on the plank's geometry so the collision triggers correctly.

Working out the plank's moment of inertia, estimating its mass around 0.3 kg and the drop height around 1 meter for a reasonable impact speed.

Using inelastic collision physics, the weight hitting at ~4.6 m/s imparts an angular velocity of about 5.6 rad/s to the plank, giving the ball at the far end a vertical launch speed near 4 m/s, which would send it up roughly 0.8-0.9 meters.

Now I'm checking feasibility details: MuJoCo's default soft contact should handle the weight-plank collision fine given the light plank, but I need to watch for ball slippage at the lip and make sure the ball's initial position aligns precisely with the plank surface to avoid jitter, accounting for the lip's dimensions and the ball's 0.04 radius.

I'm computing the ball's world-space starting coordinates by rotating its local position through the seesaw's 0.3 rad tilt, landing on roughly z=0.110 with a tiny offset for clearance, then setting the seesaw body position and using a keyframe to initialize the joint angle to 0.3.

For qpos ordering, I'll list the seesaw hinge first, then the weight's free joint, then the ball's free joint, matching body declaration order in the XML, with the ball given an identity quaternion. I also need a static fulcrum support under the pivot that won't collide with the tilted plank—sizing it as a thin box reaching up to about z=0.2 and disabling its contype/conaffinity so it doesn't interfere physically.

I'm checking that the hinge joint limit (-0.3 to 0.3 rad) keeps both the weight and ball ends clear of the floor at max tilt, with the weight's spherical cap resting on the plank and the ball constrained to roll only along the tilt axis since the plank width (0.06) barely exceeds the ball radius (0.04). I'm also verifying the weight's position at the far end of the plank doesn't clip through the plank surface during tilting.

Now I'm drafting the keyframe qpos values for the seesaw's hinge angle and the ball/weight positions, making sure the ball's lip geometry (part of the seesaw body) doesn't collide with the fulcrum itself, then finalizing the weight sphere's mass and radius before writing everything out.

