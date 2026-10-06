## What happened

The relay itself works:
- At 0.12 s ball1 hits ball2, and ball2 rolls off at about 0.9 m/s.
- At 0.28 s ball2 hits ball3.
- Balls 1 and 2 then slow on the floor and settle around x = 0.34 m and x = 0.47 m.
- Ball3 rolls off at about 0.6 m/s.

The ending is too marginal. The stronger floor resistance slowed ball3 more than I expected. It reached the cup at only about 0.18 m/s at 2.07 s. It stopped at x = 1.11 m, only about 1 cm past the mouth at x = 1.10 m. That is barely inside the cup.

## Fix

I moved the cup closer: the mouth is now at x = 0.90 m and the back wall at x = 1.04 m. In this run ball3 passed x ≈ 0.9 at about 0.34 m/s, so it should now enter with that speed. It should roll several centimetres in, and the back wall catches it if it goes further. Balls 1 and 2 still stop more than 0.4 m short of the new mouth. Nothing else changes.

```json
{"what_happens": "ball1 rolls into ball2 at 0.12 s, ball2 rolls into ball3 at 0.28 s; balls 1 and 2 slow and stop near x=0.34 and 0.47, while ball3 rolls on, decelerating from 0.6 to ~0.18 m/s, and just barely enters the cup mouth, stopping at x=1.11 only 1 cm inside the cup (mouth at 1.10).", "works": false, "problem": "ball3 arrives too slowly and stops only 1 cm inside the cup mouth, which is not convincingly in the cup."}
```

```xml
<mujoco model="three_ball_relay_into_cup">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="0.6 -1 2" dir="0 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="side" pos="0.5 -1.6 0.6" xyaxes="1 0 0 0 0.35 1"/>

    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.75 1" condim="6" friction="1 0.001 0.002"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.85 0.2 0.2 1"/>
    </body>

    <body name="ball2" pos="0.2 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.2 0.6 0.2 1"/>
    </body>

    <body name="ball3" pos="0.4 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.2 0.3 0.85 1"/>
    </body>

    <!-- Cup lying on its side: octagonal shell around the x axis, mouth at x=0.90, closed back at x=1.04, inner bottom flush with floor -->
    <body name="cup" pos="0.97 0 0.06">
      <geom name="cup_bottom" type="box" size="0.07 0.027 0.003" pos="0 0 -0.063" euler="0 0 0" condim="6" friction="1 0.001 0.01" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_45" type="box" size="0.07 0.027 0.003" pos="0 0.04455 -0.04455" euler="45 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_90" type="box" size="0.07 0.027 0.003" pos="0 0.063 0" euler="90 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_135" type="box" size="0.07 0.027 0.003" pos="0 0.04455 0.04455" euler="135 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_180" type="box" size="0.07 0.027 0.003" pos="0 0 0.063" euler="180 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_225" type="box" size="0.07 0.027 0.003" pos="0 -0.04455 0.04455" euler="225 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_270" type="box" size="0.07 0.027 0.003" pos="0 -0.063 0" euler="270 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_315" type="box" size="0.07 0.027 0.003" pos="0 -0.04455 -0.04455" euler="315 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="cylinder" size="0.069 0.003" pos="0.073 0 0" euler="0 90 0" rgba="0.85 0.6 0.15 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <exclude name="ex13" body1="ball1" body2="ball3"/>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-50000 -1"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-50000 -1"/>
    <pair name="pair13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="-50000 -1"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0  0.2 0 0.03 1 0 0 0  0.4 0 0.03 1 0 0 0" qvel="1.2 0 0 0 40 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Ball3 ends up stopping right at the mouth, only about a centimeter inside, which feels too marginal to rely on—its deceleration was much higher than I expected. Balls 1 and 2 are still drifting slowly too. I should give ball3 more initial speed so it lands deeper, maybe by moving the cup closer.

Looking at the data, the deceleration seems roughly proportional to speed, like viscous damping from a soft constraint, which is consistent and manageable. The simplest fix is moving the cup mouth to x=0.90 so ball3 enters at about 0.34 m/s instead of its current slower speed—based on earlier runs at 0.67 m/s it traveled all the way to the back wall, so 0.34 should carry it several centimeters in, which is safer. Ball2 is essentially stopped far from this new position, so no conflict there. I could also lower the cup's rolling friction to help ball3 go deeper, but I'll just keep friction at 0.01 and reposition the cup instead.

