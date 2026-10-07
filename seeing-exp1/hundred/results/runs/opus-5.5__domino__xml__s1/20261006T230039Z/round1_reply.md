In the run, ball1 rolled 1 m down the ramp, reached about 1.08 m/s and struck d1 at 2.02 s. d1 toppled d2, d2 toppled d3, and d3 hit ball2 at 2.15 s. d3 then came to rest leaning on the stand's corner. Ball2 was only nudged about 2 cm, from x = 0.50 to 0.52 m. Its rolling friction stopped it on the stand within about 0.1 s, still 1 cm short of the stand's far edge at 0.53 m, so it never reached the cup.

The fix makes the push easier to succeed:
- The stand is narrower, so its far edge is at x = 0.505 m.
- Ball2 sits 7 mm from that edge, so the nudge from d3 tips it over.
- Ball2's rolling friction is lower.
- The cup is shifted to sit against the new stand edge.

```json
{"what_happens": "ball1 rolls down the ramp and hits d1 at 2.02 s; d1 topples d2, d2 topples d3, and d3 strikes ball2 at 2.15 s, then rests leaning on the stand. Ball2 is pushed only ~2 cm and stops on the stand at x=0.52 m, short of the edge, so it never enters the cup.", "works": false, "problem": "d3's nudge was too weak against ball2's rolling friction to carry it off the stand, so ball2 stayed on the stand instead of falling into the cup."}
```

```xml
<mujoco model="ramp_domino_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="light_main" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.5994 0 0.0324" euler="0 5 0">
      <geom name="ramp_slab" type="box" size="0.6 0.15 0.02" friction="0.8 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball1" pos="-0.9901 0 0.1569">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.07" density="300" condim="6" friction="0.8 0.005 0.0005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="d1" pos="0.30 0 0.05">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>

    <body name="d2" pos="0.37 0 0.05">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.5 0.9 1"/>
    </body>

    <body name="d3" pos="0.44 0 0.05">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.8 0.9 1"/>
    </body>

    <body name="stand" pos="0.4875 0 0.025">
      <geom name="stand_block" type="box" size="0.0175 0.04 0.025" friction="0.8 0.005 0.0001" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="ball2" pos="0.498 0 0.075">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" density="1000" condim="6" friction="0.8 0.005 0.0008" rgba="0.1 0.8 0.1 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" size="0.08 0.08 0.003" pos="0.585 0 0.003" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_near" type="box" size="0.005 0.08 0.012" pos="0.51 0 0.018" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_far" type="box" size="0.005 0.08 0.05" pos="0.66 0 0.056" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_left" type="box" size="0.08 0.005 0.03" pos="0.585 0.075 0.036" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_right" type="box" size="0.08 0.005 0.03" pos="0.585 -0.075 0.036" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

The chain did work, but ball2 only got a weak nudge and stalled against the stand's corner instead of continuing. I need to lower ball2's rolling friction, position it closer to the stand's far edge, and shrink the stand's width so it doesn't block the path.

Settling on rolling friction 0.001 for decel ~0.28, with ball entering the cup around 2.3s and stopping by 4.5s. I'm rechecking the geometry — shifting the stand's far edge to 0.505 and repositioning the cup base to span 0.505–0.665, with walls centered accordingly so the interior pocket is about 0.14 wide.

Double-checking the ball's fall off the edge clears the near wall corner with margin (0.036 vs 0.025 needed), and confirming the stand-d3 collision angle stays the same at 21.8°. For ball2's resting position, I'm considering nudging it slightly from 0.500 to 0.497 to give a bit more safety margin from the edge at 0.505.

