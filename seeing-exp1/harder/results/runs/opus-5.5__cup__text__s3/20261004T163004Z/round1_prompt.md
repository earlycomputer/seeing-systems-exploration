Here is a MuJoCo MJCF scene written for this brief:

<brief>
a ball rolls down a ramp and comes to rest in a cup
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. Every geom of the ramp is named with the prefix `ramp`. The cup is a body named `cup`; all its geoms belong to it.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

```xml
<mujoco model="cup_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.8 0.005 0.002"/>
    <geom name="ramp_deck" type="box" pos="0.8000 0 0.7250" euler="0 18.9704 0" size="0.8459 0.2 0.02"/>
    <geom name="ramp_leg" type="box" pos="0.0000 0 0.5000" size="0.03 0.03 0.5000"/>
    <body name="ball" pos="0.1398 0 1.0376">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.2" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="cup" pos="2.6500 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.450 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.450 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.450 0.01 0.150"/>
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
