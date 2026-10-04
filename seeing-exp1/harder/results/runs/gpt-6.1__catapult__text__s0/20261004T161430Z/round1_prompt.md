Here is a MuJoCo MJCF scene written for this brief:

<brief>
a catapult throws a ball into a bucket whose centre is 3 m from where the ball starts
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`; it starts at rest in the catapult. Every geom of the catapult is named with the prefix `catapult`. The bucket is a body named `bucket`; all its geoms belong to it.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.0" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.0 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

If you send a corrected file, keep these conventions.


Check the scene against the brief. You have no picture or measurement of the run.


Does the world do what the brief says? First describe what you expect to happen. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what you expect to happen>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
