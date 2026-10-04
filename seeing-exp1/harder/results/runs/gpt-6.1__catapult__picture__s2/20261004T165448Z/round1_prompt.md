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


MuJoCo ran the scene for 6 s from its start. Here is a picture of what happened.

How the picture was made. A dot renderer drew the run: every surface is covered in small dark dots on a
white ground, shaded only by surface normal against one light from above; dots on surfaces facing away from
the viewer are hidden. Everything that moved is drawn as residue: a copy of it every 0.10 s from the start
to 2.38 s, older copies lighter, the last darkest. Everything that did not move is drawn once.

The picture is a drafting view: two orthographic views stacked, with no perspective, sharing one scale of
30.72 pixels per metre, so x lines up between them. A thin gray rule separates them.
- Top band, side elevation, looking along +y: x runs left to right from -1.38 to 2.78 m, z runs up from
  -0.4 to 1.72 m.
- Bottom band, plan, looking down: x runs left to right over the same range, y runs up the page from -1.02
  to 1.02 m.

The image is 128x128 pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of
its pixels averages 4x4 pixels of the original.


[image]

Does the world do what the brief says? First describe what you see happen. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what you see happen>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
