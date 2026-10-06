**What happens in the run**

The weight falls and hits the plank at 0.59 s. The 100 g ball leaves the lowered end at about 3.3 m/s upward and peaks at z = 1.36 m at 1.09 s, 1.22 m above its 0.14 m start. It then lands on the floor and rolls away. The weight rolls along the plank and settles against the lip.

**Why this doesn't count as working**

The seesaw never actually swings. MuJoCo read my hinge range `0 0.6` as degrees, not radians, so the plank was locked to a 0.6° window. It only flexed to 3.5° by pushing into the joint limit. The throw came from the limit's soft-constraint impulse passing through an almost rigid plank, not from a seesaw rotating. The height target is met, but by a numerical artifact rather than the intended mechanism.

**Fix**

Give the range in degrees, `0 34`, so the plank can rotate its full ~34° from one tilt to the other. The end of the plank still clears the floor at both stops.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="fulcrum" type="box" pos="0 0 0.15" size="0.05 0.12 0.15" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="seesaw" pos="0 0 0.33" quat="0.98877 0 -0.14944 0">
      <joint name="pivot" type="hinge" axis="0 1 0" limited="true" range="0 34" damping="0.01"/>
      <geom name="plank" type="box" size="1.0 0.1 0.03" mass="0.3" solref="0.005 1" friction="1 0.01 0.001" rgba="0.6 0.4 0.2 1"/>
      <geom name="seesaw_lip" type="box" pos="-0.98 0 0.08" size="0.02 0.1 0.05" mass="0.02" solref="0.005 1" rgba="0.5 0.3 0.1 1"/>
    </body>
    <body name="weight" pos="0.80 0 2.4">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.08" mass="1.0" solref="0.005 1" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="-0.893 0 0.14">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" solref="0.005 1" friction="1 0.01 0.001" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

```expect
weight touches seesaw
seesaw reaches its upper stop
ball touches floor
```

```json
{"what_happens": "The weight falls and strikes the plank at 0.59 s, and the 100 g ball is flung up to z = 1.36 m (1.22 m above its start) before landing and rolling away, but the seesaw hinge was limited to 0.6 degrees so the plank barely moved (max 3.5 degrees) and the throw came from impact transmitted through the joint-limit constraint.", "works": false, "problem": "The hinge range was written as 0 to 0.6 (meant as radians) but applied in degrees, so the seesaw is effectively locked and the throw is a constraint artifact rather than a seesaw swing."}
```

---
thinking (summarized):

I'm puzzled by how the ball jumped from 0.14 to 1.36 m despite the seesaw barely tilting — it seems the weight hit the plank around 0.59 s and the joint limit snapped hard enough to fling the ball at 3.34 m/s vertically, even though the seesaw's own rotation stayed tiny.

This feels spurious, more like an artifact of limit penetration than a real throw. I should fix the range to "0 34" degrees instead and recheck clearance: at 34° the body tilt comes out to about 16.8°, giving a clearance of roughly 1.2 cm at the end, which should still be fine, and the weight rolling to the ball's end afterward shouldn't cause issues either.

