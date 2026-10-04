Ten dominoes stand 0.1 m tall and 6 cm apart. The keyframe gives the first one a 2 rad/s forward roll about its front bottom edge, and gravity then carries the chain. If upright, a domino leaning on its neighbour rests at about 27°. Each one leans on a neighbour that is itself tilted, so it rests at a larger angle than that. The last one falls flat. I have not simulated this, so the 15° minimum is an estimate, not a measured result.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="800" offheight="600"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>
    <body name="domino1" pos="0 0 0.05">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.0075 0.025 0.05" rgba="0.9 0.2 0.2 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.0075 0.025 0.05" rgba="0.2 0.9 0.3 1" friction="0.5 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0 0.06 0 0.05 1 0 0 0 0.12 0 0.05 1 0 0 0 0.18 0 0.05 1 0 0 0 0.24 0 0.05 1 0 0 0 0.30 0 0.05 1 0 0 0 0.36 0 0.05 1 0 0 0 0.42 0 0.05 1 0 0 0 0.48 0 0.05 1 0 0 0 0.54 0 0.05 1 0 0 0" qvel="0.1 0 0.015 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sizing up standard domino dimensions and spacing for the layout, then thinking through how MuJoCo's free joint represents position, orientation, and velocity state for each body so I can set initial conditions correctly.

To tip the first domino forward, I work out the angular velocity needed about the y-axis and convert it into the corresponding linear velocity of its center of mass, treating the motion as a pivot about the bottom front edge. I settle on roughly 5 rad/s as a reasonable starting push, enough to carry the domino past its tipping point given its height and thickness.

Now I'm sizing the dominoes more generously for stability at this timestep — around 0.1m tall, 0.015m thick, 0.05m wide, spaced 0.06m apart so each one can topple into the next, with the final domino falling flat against the floor while earlier ones end up leaning at fairly steep angles against their neighbors.

I'll bump spacing to 0.06, keep default friction and density settings so mass works out to about 0.075kg per domino, and use a 0.002 timestep which should handle contacts fine at this thickness. For the initial keyframe, I'm positioning the ten domino bodies in a line and giving the first one an angular and linear velocity to kick off the toppling sequence.

Checking the physics: with w=5 rad/s, the kinetic energy vastly exceeds the energy needed to tip the domino past its pivot point, so that velocity is overkill and could cause unwanted sliding or bouncing. I'll dial it back to something like w=2 instead.

Now I'm setting up the keyframe data - positioning ten dominoes spaced 0.06m apart along x, with matching qpos and qvel arrays where only the first domino gets initial velocity (translational and angular) while the rest start at rest. I'll make sure body positions align with the keyframe and include the floor and lighting in the scene file.

