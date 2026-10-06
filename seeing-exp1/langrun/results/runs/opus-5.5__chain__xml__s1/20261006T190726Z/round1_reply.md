In the run, `ball1` rolled into `ball2` as planned at 0.13 s, but the contact blew up. Both balls flew off at about 30 m/s in opposite directions, rising about 4 m into the air. They ended over 140 m away.

`ball2` passed above the cup without entering it. `ball3` was never touched and sat at x = 0.5 m for the whole run. Nothing reached the cup.

The cause is the ball-ball contact setting `solref="0.005 0.05"`. That makes the contact very stiff and nearly undamped, and at a 0.002 s timestep it became unstable and injected energy instead of giving a modest bounce.

In the corrected file I changed the ball contacts to `solref="0.015 0.3"`. That is a softer spring, about 7.5 timesteps, with real damping, which should give a stable bounce with roughly 0.35–0.4 restitution. Everything else is unchanged. Even if the collisions turn out nearly inelastic, the balls move forward as a train with `ball3` in front, so `ball3` should still be pushed up the lip ramp into the cup. I haven't rerun it, so this is a prediction.

```json
{"what_happens": "ball1 rolls into ball2 at 0.13 s, but the contact blows up: ball1 is flung backwards and ball2 forwards at about 30 m/s, both flying about 4 m high. ball2 passes over the cup and both end over 140 m away. ball3 is never touched and stays at rest at x = 0.5 m, and nothing enters the cup.", "works": false, "problem": "The very stiff, nearly undamped ball-ball contact (solref 0.005 0.05) went unstable at the 0.002 s timestep and launched ball1 and ball2 into the air, so ball3 was never hit and nothing reached the cup."}
```

```xml
<mujoco model="three_balls_into_cup">
  <option timestep="0.002"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -0.5 2" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.85 0.8 1" friction="0.8 0.005 0.0001" priority="1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" rgba="0.9 0.2 0.2 1" friction="0.05 0.005 0.0001" solref="0.015 0.3"/>
    </body>

    <body name="ball2" pos="0.25 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" rgba="0.2 0.4 0.9 1" friction="0.05 0.005 0.0001" solref="0.015 0.3"/>
    </body>

    <body name="ball3" pos="0.5 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" rgba="0.95 0.8 0.1 1" friction="0.05 0.005 0.0001" solref="0.015 0.3"/>
    </body>

    <!-- Cup lying on its side, mouth facing -x, axis at height 0.054, fixed to the world.
         Inner radius 0.05, wall thickness 0.004, interior spans x = 0.85 .. 0.97. -->
    <body name="cup" pos="0.91 0 0.054">
      <geom name="cup_wall_000" type="box" size="0.06 0.0145 0.002" pos="0 0 0.052" euler="0 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_030" type="box" size="0.06 0.0145 0.002" pos="0 -0.026 0.04503" euler="30 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_060" type="box" size="0.06 0.0145 0.002" pos="0 -0.04503 0.026" euler="60 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_090" type="box" size="0.06 0.0145 0.002" pos="0 -0.052 0" euler="90 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_120" type="box" size="0.06 0.0145 0.002" pos="0 -0.04503 -0.026" euler="120 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_150" type="box" size="0.06 0.0145 0.002" pos="0 -0.026 -0.04503" euler="150 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_180" type="box" size="0.06 0.0145 0.002" pos="0 0 -0.052" euler="180 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_210" type="box" size="0.06 0.0145 0.002" pos="0 0.026 -0.04503" euler="210 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_240" type="box" size="0.06 0.0145 0.002" pos="0 0.04503 -0.026" euler="240 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_270" type="box" size="0.06 0.0145 0.002" pos="0 0.052 0" euler="270 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_300" type="box" size="0.06 0.0145 0.002" pos="0 0.04503 0.026" euler="300 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_330" type="box" size="0.06 0.0145 0.002" pos="0 0.026 0.04503" euler="330 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_bottom" type="cylinder" size="0.054 0.003" pos="0.063 0 0" euler="0 90 0" rgba="0.5 0.25 0.6 1" priority="1"/>
      <!-- shallow lip ramp: top surface rises from z=0 at x=0.79 to z=0.004 at the mouth (x=0.85) -->
      <geom name="cup_lip_ramp" type="box" size="0.0301 0.025 0.002" pos="-0.0899 0 -0.054" euler="0 -3.81 0" rgba="0.5 0.25 0.6 1" priority="1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0  0.25 0 0.03 1 0 0 0  0.5 0 0.03 1 0 0 0" qvel="1.5 0 0 0 50 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

That collision contact used overly stiff solref values at a small timestep, which injected huge energy and sent the balls flying at unrealistic speeds — clearly an unstable constraint setup. I should fix this by using the default stable ball solref or a moderate damping ratio with a longer time constant instead.

