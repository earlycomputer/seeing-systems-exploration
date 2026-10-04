Here is a MuJoCo MJCF scene written for this brief:

<brief>
a door swings shut and stays shut
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The door is a body named `door` on a hinge joint named `hinge`. The door is shut when `hinge` is at 0.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

```xml
<mujoco model="door_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="5 5 0.1"/>
    <geom name="frame_post" type="box" pos="0 -0.12 1.05" size="0.04 0.04 1.05"/>
    <body name="door" pos="0 0 1.0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" stiffness="40" springref="0" damping="25" range="0 2.1" limited="true"/>
      <geom name="door_panel" type="box" pos="0 0.45 0" size="0.02 0.45 0.98" mass="20"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.2"/>
  </keyframe>
</mujoco>
```

If you send a corrected file, keep these conventions.


MuJoCo ran the scene for 6 s from its start. Here is a picture of what happened.

How the picture was made. A dot renderer drew the run: every surface is covered in small dark dots on a
white ground, shaded only by surface normal against one light from above; dots on surfaces facing away from
the viewer are hidden. Everything that moved is drawn as residue: a copy of it every 0.03 s from the start
to 0.74 s, older copies lighter, the last darkest. Everything that did not move is drawn once.

The picture is a drafting view: two orthographic views stacked, with no perspective, sharing one scale of
30.24 pixels per metre, so x lines up between them. A thin gray rule separates them.
- Top band, side elevation, looking along +y: x runs left to right from -2.48 to 1.75 m, z runs up from
  -0.27 to 2.37 m.
- Bottom band, plan, looking down: x runs left to right over the same range, y runs up the page from -0.43
  to 1.17 m.

The image is 128x128 pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of
its pixels averages 4x4 pixels of the original.


[image]

Does the world do what the brief says? First describe what you see happen. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what you see happen>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
