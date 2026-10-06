```xml
<mujoco model="ten_domino_chain">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <global azimuth="110" elevation="-25"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.15 0.15 0.15"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.5 -0.5 2" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="0.50 -1.65 0.95" xyaxes="1 0 0 0 0.447214 0.894427"/>
    <geom name="floor" type="plane" pos="0 0 0" size="2 1.5 0.1" rgba="0.22 0.25 0.29 1" condim="3" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <!-- Each domino measures 0.03 by 0.10 by 0.30 m.
         The first starts tilted 15 degrees toward the row, beyond its
         tipping point, with its lower forward edge resting on the floor. -->
    <body name="domino1" pos="0.0393339694 0 0.1487711596" quat="0.9914448614 0 0.1305261922 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.9 0.25 0.15 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino2" pos="0.11 0 0.15">
      <freejoint name="domino2_free"/>
      <geom name="domino2_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.95 0.45 0.15 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino3" pos="0.22 0 0.15">
      <freejoint name="domino3_free"/>
      <geom name="domino3_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.95 0.65 0.15 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino4" pos="0.33 0 0.15">
      <freejoint name="domino4_free"/>
      <geom name="domino4_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.75 0.8 0.2 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino5" pos="0.44 0 0.15">
      <freejoint name="domino5_free"/>
      <geom name="domino5_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.3 0.75 0.35 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino6" pos="0.55 0 0.15">
      <freejoint name="domino6_free"/>
      <geom name="domino6_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.2 0.75 0.65 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino7" pos="0.66 0 0.15">
      <freejoint name="domino7_free"/>
      <geom name="domino7_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.2 0.6 0.9 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino8" pos="0.77 0 0.15">
      <freejoint name="domino8_free"/>
      <geom name="domino8_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.3 0.4 0.9 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino9" pos="0.88 0 0.15">
      <freejoint name="domino9_free"/>
      <geom name="domino9_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.55 0.3 0.85 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="domino10" pos="0.99 0 0.15">
      <freejoint name="domino10_free"/>
      <geom name="domino10_geom" type="box" size="0.015 0.05 0.15" density="600" rgba="0.8 0.3 0.65 1" condim="3" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

**Designing domino simulation**

I'm figuring out how to design a robust falling domino simulation without any available tools. I need to create an analytically valid scene where the first domino tips and causes a cascade in about 6 seconds. I want to set up boxes of varying height, width, and thickness while ensuring they don't intersect or penetrate the floor. The initial domino should be tilted at 15-25 degrees and have proper support positions. I'll need to determine the dimensions and spacing carefully.

**Calculating rotation dynamics**

I'm working through the equations for a rotation involving angles and offsets, focusing on how the components transform into a position. I need to find the new x and z coordinates after applying a 20-degree rotation. The minimum and maximum z values require careful calculations for height and tilt, especially since there's a bit of overlap when checking the dimensions. I'll also adjust the height and width parameters and ensure everything fits, keeping an eye on how everything interacts in 3D space.

**Exploring domino collision dynamics**

I'm analyzing the ideal conditions for a domino collision. It seems like I want the top domino to fall within two seconds, with angles around 15 degrees. The first domino should have an initial tilt of about 21.5 degrees, and I need to ensure they are aligned in a row for optimal performance. I'm considering different pitches and initial angles to ensure a successful chain reaction, focusing on adjustments around 17.5 to 18 degrees. It’s all about getting those angles just right!