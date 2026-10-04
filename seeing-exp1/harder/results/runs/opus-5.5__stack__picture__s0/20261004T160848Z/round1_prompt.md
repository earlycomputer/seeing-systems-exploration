Here is a MuJoCo MJCF scene written for this brief:

<brief>
a stack of five blocks stands until the bottom block is pushed, then topples
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The blocks are bodies named `block1` (bottom) to `block5` (top), each with a `<freejoint/>` and one box geom. Whatever does the pushing is part of the scene.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-1.2 0 0.1">
      <freejoint/>
      <geom name="pusher" type="sphere" size="0.1" mass="4.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  -1.2 0 0.1 1 0 0 0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.5 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

If you send a corrected file, keep these conventions.


MuJoCo ran the scene for 6 s from its start. Here is a picture of what happened.

How the picture was made. A dot renderer drew the run: every surface is covered in small dark dots on a
white ground, shaded only by surface normal against one light from above; dots on surfaces facing away from
the viewer are hidden. Everything that moved is drawn as residue: a copy of it every 0.08 s from the start
to 1.91 s, older copies lighter, the last darkest. Everything that did not move is drawn once.

The picture is a drafting view: two orthographic views stacked, with no perspective, sharing one scale of
60.40 pixels per metre, so x lines up between them. A thin gray rule separates them.
- Top band, side elevation, looking along +y: x runs left to right from -1.62 to 0.5 m, z runs up from
  -0.26 to 1.22 m.
- Bottom band, plan, looking down: x runs left to right over the same range, y runs up the page from -0.32
  to 0.32 m.

The image is 128x128 pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of
its pixels averages 4x4 pixels of the original.


[image]

Does the world do what the brief says? First describe what you see happen. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what you see happen>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
