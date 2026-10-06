Ten box dominoes are spaced 10 cm apart along +x. The first one starts with a keyframe velocity that rotates it about its front bottom edge, so it tips forward instead of sliding, and the falling dominoes knock down the rest in turn. I haven't run this in MuJoCo, so I haven't checked that all ten fall or that each ends up tilted at least 15°.

```xml
<mujoco model="domino_row">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>
    <body name="domino1" pos="0.0 0 0.1">
      <freejoint name="j1"/>
      <geom name="d1" type="box" size="0.015 0.05 0.1" rgba="0.9 0.2 0.2 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino2" pos="0.1 0 0.1">
      <freejoint name="j2"/>
      <geom name="d2" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino3" pos="0.2 0 0.1">
      <freejoint name="j3"/>
      <geom name="d3" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino4" pos="0.3 0 0.1">
      <freejoint name="j4"/>
      <geom name="d4" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino5" pos="0.4 0 0.1">
      <freejoint name="j5"/>
      <geom name="d5" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino6" pos="0.5 0 0.1">
      <freejoint name="j6"/>
      <geom name="d6" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino7" pos="0.6 0 0.1">
      <freejoint name="j7"/>
      <geom name="d7" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino8" pos="0.7 0 0.1">
      <freejoint name="j8"/>
      <geom name="d8" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino9" pos="0.8 0 0.1">
      <freejoint name="j9"/>
      <geom name="d9" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="domino10" pos="0.9 0 0.1">
      <freejoint name="j10"/>
      <geom name="d10" type="box" size="0.015 0.05 0.1" rgba="0.2 0.4 0.9 1" friction="0.6 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.1 1 0 0 0 0.1 0 0.1 1 0 0 0 0.2 0 0.1 1 0 0 0 0.3 0 0.1 1 0 0 0 0.4 0 0.1 1 0 0 0 0.5 0 0.1 1 0 0 0 0.6 0 0.1 1 0 0 0 0.7 0 0.1 1 0 0 0 0.8 0 0.1 1 0 0 0 0.9 0 0.1 1 0 0 0" qvel="0.3 0 0.045 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sizing the dominoes at roughly 0.2 height, 0.03 thickness, 0.1 width, spaced about 0.1 apart in a row along the x-axis, and planning to give the first one an initial angular velocity to kick off the chain reaction.

Working out the keyframe details: since qpos defaults to qpos0 when unspecified but qvel needs the full length, I'm setting the first domino's y-angular velocity to around 3 rad/s, which should rotate it forward toward +x and start the cascade, with the last domino expected to tip nearly 90 degrees onto the floor.

Checking that the spacing and physics work out: with domino centers 0.1 apart, a tilt of roughly 20° is enough for one to strike the next, and with default friction and a mass of about 0.6 kg per domino, an initial angular velocity of 3 rad/s should carry enough energy to topple the first piece and propagate the fall down the line.

Setting angular velocity to 3 gives a reasonable kinetic energy of about 0.036 J, easily enough to overcome the tiny potential barrier from the center rising as it tips. The dominoes are positioned flush with the floor spaced along x from 0 to 0.9, with the chain reaction ending as the last domino falls flat and the second-to-last rests leaning against it.

