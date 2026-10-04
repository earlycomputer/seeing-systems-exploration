Here is a MuJoCo scene for this brief:

<brief>
{brief}
</brief>

```xml
{scene}```

The scene does not yet launch the ball. Add a keyframe named `shot` that launches the ball from where it
rests so that it drops through the hoop. MuJoCo will reset to this keyframe and simulate from there.

- Write one `<keyframe>` element after `</worldbody>`, holding one `<key name="shot" .../>` on a single line.
- Set its `qvel`. The ball's free joint is the scene's only joint, so `qvel` is six numbers: linear velocity
  x y z in m/s, then angular velocity x y z in rad/s. Leave out `qpos` so the ball starts where it rests.
- Change nothing else in the file. Note the scene has air: `density` on `<option>`, and the ball's geom
  uses MuJoCo's ellipsoid fluid model.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.
