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


MuJoCo ran the scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- door: hinge joint hinge about axis (0.00, 0.00, 1.00), range 0° to 2.1° as MuJoCo applies it; its geoms: door_panel; starts at 68.8°, still

What happened, in order:
 0.00 s  door starts at 68.8°, outside its range of 0° to 2.1°
 0.00 s  door is at its largest at the start, 68.8°
 0.06 s  door reaches its upper stop (2.1°) moving -1041°/s
 0.06 s  door reaches its lower stop (0°) moving -1032°/s
 0.08 s  door is at its smallest, -6.5°
 0.14 s  door reaches its lower stop (0°) again moving +103°/s
 0.16 s  door reaches its upper stop (2.1°) again moving +93°/s
 0.20 s  door reaches its upper stop (2.1°) again moving -11°/s
 0.48 s  door reaches its lower stop (0°) again moving -5°/s

State every 0.25 s:
0.00 s: door at 68.8°, still; touching nothing
0.25 s: door at 2.1°, turning -10°/s; touching nothing
0.50 s: door at 0.4°, turning -4°/s; touching nothing
0.75 s: door at 0.0°, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- door at 0.0°, still; touching nothing
</history>


Does the world do what the brief says? First describe what happens in the run. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what happens in the run>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
