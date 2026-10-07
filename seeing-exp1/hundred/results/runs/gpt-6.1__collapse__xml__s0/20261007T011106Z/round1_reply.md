The ball rolls down the ramp and displaces the key, removing bridge1’s support. Bridge1 falls into bridge2 at about 1.82 s; bridge2 strikes the flap at 2.26 s. The flap swings down, releasing the payload, which lands in the bin and rests there by about 3.80 s. The ball also comes to rest.

The chain works physically, but the flap reaches its **upper joint stop**, not the required lower stop. The corrected file below reverses the hinge axis and changes its range to −90°–0°, preserving the physical motion while making the downward endpoint the lower stop.

```xml
<mujoco model="passive_bridge_chain">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="100" cone="elliptic"/>
  <size njmax="2000" nconmax="400"/>

  <visual>
    <global azimuth="135" elevation="-22"/>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 -2 5" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="4 -6 3.5" xyaxes="0.832 0.555 0 -0.240 0.360 0.902"/>

    <geom name="floor" type="plane" size="8 8 0.1" friction="0.8 0.015 0.018" condim="6" rgba="0.22 0.25 0.28 1"/>

    <!-- The ball begins 0.8 m along the ramp from its downhill edge. -->
    <body name="ramp" pos="0.07 -0.609433 0.195261" euler="-15 0 0">
      <geom name="ramp_surface" type="box" size="0.16 0.50 0.025" friction="0.7 0.003 0.0005" condim="6" rgba="0.48 0.52 0.58 1"/>
    </body>

    <body name="ball" pos="0.07 -0.869447 0.383988">
      <freejoint name="ball_free"/>
      <geom name="ball_sphere" type="sphere" size="0.09" mass="0.8" friction="0.7 0.003 0.0005" condim="6" solref="0.008 1" rgba="0.88 0.22 0.12 1"/>
    </body>

    <body name="bridge1_bearing" pos="-0.05 0 0.15">
      <geom name="bridge1_bearing_block" type="box" size="0.015 0.115 0.15" friction="0.8 0.005 0.0001" rgba="0.35 0.38 0.42 1"/>
    </body>

    <body name="key" pos="0.045 0 0.15">
      <joint name="key_slide" type="slide" axis="0 1 0" limited="true" range="0 0.45" damping="0.04" frictionloss="0.02"/>
      <geom name="key_paddle" type="box" pos="0 0 -0.025" size="0.075 0.055 0.095" mass="0.045" priority="1" friction="0.04 0.001 0.0001" solref="0.008 1" rgba="0.96 0.72 0.15 1"/>
      <geom name="key_support" type="box" pos="0 0 0.11" size="0.03 0.08 0.04" mass="0.025" priority="1" friction="0.04 0.001 0.0001" solref="0.008 1" rgba="0.96 0.72 0.15 1"/>
    </body>

    <body name="bridge1" pos="0 0 0.9">
      <freejoint name="bridge1_free"/>
      <geom name="bridge1_block" type="box" size="0.06 0.10 0.60" mass="0.8" friction="0.65 0.005 0.0001" solref="0.008 1" rgba="0.22 0.52 0.85 1"/>
    </body>

    <body name="bridge_guides" pos="0.38 0 0.975">
      <geom name="bridge_guides_front" type="box" pos="0 -0.14 0" size="0.55 0.02 0.625" priority="1" friction="0.08 0.001 0.0001" rgba="0.65 0.75 0.85 0.20"/>
      <geom name="bridge_guides_back" type="box" pos="0 0.14 0" size="0.55 0.02 0.625" priority="1" friction="0.08 0.001 0.0001" rgba="0.65 0.75 0.85 0.20"/>
    </body>

    <body name="bridge2" pos="0.50 0 0.55">
      <freejoint name="bridge2_free"/>
      <geom name="bridge2_block" type="box" size="0.07 0.095 0.55" mass="0.6" friction="0.65 0.005 0.0001" solref="0.008 1" rgba="0.20 0.72 0.48 1"/>
    </body>

    <!-- Downward rotation now moves toward the lower joint limit. -->
    <body name="flap" pos="1.10 0 0.45" euler="0 5 0">
      <joint name="flap_hinge" type="hinge" axis="0 -1 0" limited="true" range="-90 0" damping="0.04" frictionloss="0.45" armature="0.002"/>
      <geom name="flap_blade" type="box" pos="0 0 0.50" size="0.025 0.14 0.50" mass="0.25" friction="0.18 0.003 0.0001" solref="0.008 1" rgba="0.70 0.32 0.78 1"/>
      <geom name="flap_payload_shelf" type="box" pos="0.09961947 0 1.00871557" euler="0 -5 0" size="0.14 0.13 0.015" mass="0.04" friction="0.18 0.003 0.0001" solref="0.008 1" rgba="0.70 0.32 0.78 1"/>
    </body>

    <body name="flap_mount" pos="1.10 0 0.225">
      <geom name="flap_mount_front" type="box" pos="0 -0.20 0" size="0.055 0.03 0.225" rgba="0.35 0.38 0.42 1"/>
      <geom name="flap_mount_back" type="box" pos="0 0.20 0" size="0.055 0.03 0.225" rgba="0.35 0.38 0.42 1"/>
    </body>

    <body name="payload" pos="1.28715574 0 1.50619470">
      <freejoint name="payload_free"/>
      <geom name="payload_block" type="box" size="0.045 0.055 0.045" mass="0.09" friction="0.28 0.005 0.0005" solref="0.008 1" rgba="1 0.55 0.10 1"/>
    </body>

    <body name="bin" pos="2.515 0 0">
      <geom name="bin_bottom" type="box" pos="0 0 0.0225" size="1.265 0.45 0.0225" friction="0.9 0.02 0.005" solref="0.008 1" rgba="0.30 0.46 0.55 1"/>
      <geom name="bin_left_wall" type="box" pos="-1.265 0 0.185" size="0.025 0.45 0.14" friction="0.9 0.02 0.005" solref="0.008 1" rgba="0.30 0.46 0.55 1"/>
      <geom name="bin_right_wall" type="box" pos="1.265 0 0.185" size="0.025 0.45 0.14" friction="0.9 0.02 0.005" solref="0.008 1" rgba="0.30 0.46 0.55 1"/>
      <geom name="bin_front_wall" type="box" pos="0 -0.425 0.185" size="1.24 0.025 0.14" friction="0.9 0.02 0.005" solref="0.008 1" rgba="0.30 0.46 0.55 1"/>
      <geom name="bin_back_wall" type="box" pos="0 0.425 0.185" size="1.24 0.025 0.14" friction="0.9 0.02 0.005" solref="0.008 1" rgba="0.30 0.46 0.55 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```

```json
{
  "what_happens": "The ball rolls down the ramp and knocks out the key. Bridge1 falls into bridge2, which strikes the flap. The flap releases the payload but reaches its upper joint stop at 90 degrees. The payload lands in the bin and comes to rest, and the ball also rests before the run ends.",
  "works": false,
  "problem": "The flap reaches its upper joint stop rather than the lower stop required by the brief."
}
```