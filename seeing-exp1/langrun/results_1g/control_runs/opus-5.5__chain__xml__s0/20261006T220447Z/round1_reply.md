## What happened

The relay itself worked as the brief describes:
- At 0.12 s ball1 hit ball2 and handed over most of its speed.
- At 0.27 s ball2 hit ball3.
- Ball3 rolled at about 0.73 m/s, entered the cup at 1.22 s, touched the back wall, and came to rest inside at x = 1.21 m.

The leftover motion did not die out. Ball1 and ball2 kept rolling forward at 0.1–0.2 m/s, slowing by only about 0.04 m/s². Ball2 drifted all the way to the cup mouth and stopped there at 5.03 s. Ball1 was still rolling at 0.08 m/s at 6 s, so it never came to rest.

## Why

The floor's rolling resistance gave roughly a third of the slowing I had estimated. Balls 1 and 2 needed that slowing to stop well before the cup.

## Fix

I raised the floor's rolling-friction coefficient from 0.0006 to 0.002, about 3.3 times stronger. Scaling from the 0.04–0.06 m/s² seen in this run gives about 0.15–0.2 m/s²; that scaling is my assumption, not a measurement.
- Ball1, leaving the first collision at about 0.25 m/s, should then stop within about 0.2 m.
- Ball2, at about 0.16 m/s, should stop within about 0.1 m.
- Ball3, at about 0.75 m/s, has a stopping range of roughly 1.4 m from x ≈ 0.5. That should still carry it the remaining 0.6 m into the cup at a reduced speed.

Nothing else changes.

```json
{"what_happens": "ball1 strikes ball2 at 0.12 s, ball2 strikes ball3 at 0.27 s, and ball3 rolls at ~0.73 m/s into the cup at 1.22 s, touches the back wall and rests inside at x=1.21. However ball1 and ball2 keep rolling forward at 0.1-0.2 m/s because floor rolling resistance is weak: ball2 creeps all the way into the cup mouth at 5 s and ball1 is still rolling at 0.08 m/s at 6 s.", "works": false, "problem": "Floor rolling resistance is too weak, so ball2 drifts into the cup and ball1 is still moving at 0.08 m/s at the end."}
```

```xml
<mujoco model="three_ball_relay_into_cup">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="0.6 -1 2" dir="0 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="side" pos="0.6 -1.6 0.6" xyaxes="1 0 0 0 0.35 1"/>

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

    <!-- Cup lying on its side: octagonal shell around the x axis, mouth at x=1.1, closed back at x=1.24, inner bottom flush with floor -->
    <body name="cup" pos="1.17 0 0.06">
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

The relay results show ball3 did settle in the cup, but the floor friction turned out much weaker than modeled—decel of only about 0.04 m/s² instead of the expected 0.14. That means ball1 still has residual motion at 0.08 m/s at the end, and ball2 overshoots into the cup's mouth instead of stopping short. So the trial fails on two counts: ball1 isn't at rest and ball2's final position is wrong. I need to figure out why the friction estimate was so far off, looking at ball3's deceleration from 0.75 toward zero.

I'm recalculating: ball3 went from 0.75 to 0.72 over 0.5 s, giving about 0.06 m/s² observed, while the cup's own rolling friction behaved as expected. The discrepancy might stem from the pyramidal cone shape or from forces being split across contacts. My fix is to roughly quadruple the floor rolling friction coefficient to 0.0025, which should yield about 0.24 m/s² based on scaling the observed 0.06 by 4x. Checking whether ball3 can still reach the cup under this higher friction: starting near x≈0.5 at 0.75 m/s with 0.6 m remaining, the math gives a final speed of about 0.52 m/s, assuming linear scaling holds.

For ball1 and ball2, I'm checking their stopping distances under the new friction value — ball1 at 0.25 m/s should stop within about 0.13 m, keeping both comfortably clear of the cup. I'm also weighing whether the pyramidal cone itself is the real culprit, considering switching to an elliptic cone, but that risks unpredictable side effects, so raising mu_r directly seems like the safer, simpler fix. There's still some risk the friction doesn't scale linearly, so I'm considering whether to also nudge up the initial launch speed proportionally, since that would scale ball1 and ball2's speeds in tandem with ball3's.

Running through a sensitivity check: with a=0.24, ball3 travels about 1.17 m from x≈0.5, reaching roughly 1.67, while ball1 only moves 0.13 m — a comfortable margin. If actual deceleration is instead 0.4 m/s², ball3's range drops to about 0.70 m, reaching 1.2, which is more marginal. Testing mu_r=0.002 (a≈0.19) instead gives ball1 a 0.16 m range and ball3 1.47 m, which feels like a better balance, so I'll settle on mu_r=0.002. I'm also confirming ball3 should still rest near the back of the cup, and that ball1 and ball2 will gently collide and settle to rest under the stronger friction rather than causing any disruptive re-hit. The only change needed is the floor friction value.

