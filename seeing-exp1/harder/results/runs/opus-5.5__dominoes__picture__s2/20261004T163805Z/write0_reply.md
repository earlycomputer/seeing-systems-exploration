The row runs along +x with 6 cm spacing. Each domino is 10 cm tall, 5 cm wide and 1.6 cm thick. The keyframe gives `domino1` a forward rotation about its bottom-front edge. That kick carries about 2.5 times the energy needed to tip it past its balance point. I haven't run this file. By geometry alone, each domino left leaning on its neighbour would sit near 26° from upright, and the last one lies flat on the floor, so every domino should finish tilted well past 15°.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1" friction="1 0.005 0.0001"/>
    <body name="domino1" pos="0 0 0.05">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.95 0.95 0.9 1"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.008 0.025 0.05" density="700" friction="0.5 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0.06 0 0.05 1 0 0 0  0.12 0 0.05 1 0 0 0  0.18 0 0.05 1 0 0 0  0.24 0 0.05 1 0 0 0  0.30 0 0.05 1 0 0 0  0.36 0 0.05 1 0 0 0  0.42 0 0.05 1 0 0 0  0.48 0 0.05 1 0 0 0  0.54 0 0.05 1 0 0 0" qvel="0.15 0 0.024 0 3 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sketching out domino dimensions and spacing for the chain, then thinking through the free joint structure for each domino body—position and quaternion for pose, plus linear and angular velocity for the initial tip.

Checking the leaning geometry: with spacing 0.03 and height 0.048, each fallen domino should lean against the next at roughly 27°, well past the 15° threshold, with the last one falling flat against the floor. For the initial push, I'm calculating the toppling angle (~9.5°) and settling on an angular velocity around 4 rad/s applied about the y-axis to kick the first domino toward +x.

I'm also checking that the pivot should be the bottom edge rather than the center, computing the velocity components there and comparing the rise in center-of-mass height against the rotational kinetic energy needed to ensure the push is strong enough to topple the domino.

With w=4 the energy comfortably clears the threshold, so bumping it to 5 for extra margin seems safe without risking the piece flying off. I'm also weighing friction defaults and whether to scale up domino dimensions a bit (closer to real 48mm) for more robust collisions at the given timestep.

I'm redoing the sizing with halved dimensions (h=0.1, half-thickness 0.008, half-width 0.025) and 0.06 spacing, checking the lean angle comes out around 26°, then recalculating the pivot inertia and center-of-mass rise to see that with w=3 the kinetic energy per mass comes out to about 0.0154, well above the needed threshold.

Now I'm computing the initial linear velocity from the angular velocity at the contact point, getting roughly (0.15, 0, 0.024), and reasoning that this impulse should be enough to propagate the toppling through the chain of dominoes placed 0.06 apart along x. I'm now assembling the full qpos and qvel keyframe arrays for all the dominoes, setting the first domino's velocity values and zeroing the rest, along with finalizing physics defaults like condim and solref before writing the complete file.

I'm also tuning friction coefficients: keeping domino-floor friction high (around 1, from the max combination rule) to prevent bottom sliding, while lowering domino-domino friction to about 0.5 so they can slide against each other as they topple.

