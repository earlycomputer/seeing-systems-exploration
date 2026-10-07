The ball falls onto wall1 at 0.43 s, ricochets into wall2 at 0.76 s, and hits the target at 0.89 s. The target turns, withdrawing the cam support; the block falls into the bin and settles. Both the ball and block are at rest by the end.

The sequence mostly works, but the target reaches its **upper joint stop**, not its lower stop. The correction below reverses the hinge axis and limits without changing the physical trajectory, making the downward endpoint the lower joint stop.

```xml
<mujoco model="gravity_ricochet_release">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" cone="elliptic"/>
  <visual>
    <global azimuth="90" elevation="-18"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 -3 6" dir="0 0 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="overview" pos="4 -7 3.4" xyaxes="0.868 0.496 0 -0.093 0.163 0.982"/>

    <geom name="floor" type="plane" size="8 8 0.1" rgba="0.25 0.28 0.31 1" condim="6" friction="0.9 0.08 0.04" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <body name="ball" pos="0 0 4">
      <freejoint name="ball_free"/>
      <geom name="ball_sphere" type="sphere" size="0.06" mass="0.20" rgba="0.95 0.25 0.08 1" condim="6" friction="0.8 0.06 0.04" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="wall1" pos="0 0 3" quat="0.923879533 0 0.382683432 0">
      <geom name="wall1_reflector" type="box" pos="0 0 -0.035" size="0.70 0.30 0.035" rgba="0.20 0.55 0.85 1" friction="0 0 0" solref="0.008 1"/>
    </body>

    <body name="wall2" pos="1.4 0 2.6" quat="0.642787610 0 -0.766044443 0">
      <geom name="wall2_reflector" type="box" pos="0 0 -0.035" size="0.75 0.30 0.035" rgba="0.20 0.55 0.85 1" friction="0 0 0" solref="0.008 1"/>
    </body>

    <!-- Negative hinge rotation lowers the plate to the lower stop at -75 degrees. -->
    <body name="target" pos="-0.35 0 1.8">
      <inertial pos="0 0 0" mass="0.8" diaginertia="0.025 0.14 0.14"/>
      <joint name="target_hinge" type="hinge" axis="0 -1 0" range="-75 0" damping="0.01" frictionloss="0.025" solreflimit="0.004 1" solimplimit="0.95 0.99 0.001"/>

      <geom name="target_plate" type="box" pos="1.125 0 0" size="0.675 0.20 0.025" mass="0" rgba="0.85 0.20 0.22 1" friction="0.15 0.005 0.002" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="target_side_rail" type="capsule" fromto="0.027835 0.17 0.198054 0.65 0.17 0" size="0.017" mass="0" rgba="0.60 0.12 0.14 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_connector" type="capsule" fromto="0.027835 0 0.198054 0.027835 0.17 0.198054" size="0.006" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>

      <geom name="target_cam_01" type="capsule" fromto="-0.182709 0 0.081347 -0.165808 0 0.111839" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_02" type="capsule" fromto="-0.165808 0 0.111839 -0.148629 0 0.133826" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_03" type="capsule" fromto="-0.148629 0 0.133826 -0.128558 0 0.153209" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_04" type="capsule" fromto="-0.128558 0 0.153209 -0.105984 0 0.169610" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_05" type="capsule" fromto="-0.105984 0 0.169610 -0.081347 0 0.182709" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_06" type="capsule" fromto="-0.081347 0 0.182709 -0.055128 0 0.192252" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_07" type="capsule" fromto="-0.055128 0 0.192252 -0.027835 0 0.198054" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_08" type="capsule" fromto="-0.027835 0 0.198054 0 0 0.2" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
      <geom name="target_cam_09" type="capsule" fromto="0 0 0.2 0.027835 0 0.198054" size="0.010" mass="0" rgba="0.65 0.65 0.68 1" friction="0.02 0 0" solref="0.008 1"/>
    </body>

    <body name="block" pos="-0.35 0 2.065">
      <freejoint name="block_free"/>
      <geom name="block_payload" type="box" size="0.018 0.045 0.055" mass="0.08" rgba="0.95 0.75 0.12 1" condim="6" friction="0.4 0.01 0.005" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="bin" pos="-0.35 0 0">
      <geom name="bin_bottom" type="box" pos="0 0 0.035" size="0.325 0.275 0.035" rgba="0.15 0.55 0.38 1" condim="6" friction="0.8 0.05 0.02" solref="0.008 1"/>
      <geom name="bin_left" type="box" pos="-0.30 0 0.20" size="0.025 0.275 0.13" rgba="0.15 0.55 0.38 1" friction="0.5 0.01 0.005" solref="0.008 1"/>
      <geom name="bin_right" type="box" pos="0.30 0 0.20" size="0.025 0.275 0.13" rgba="0.15 0.55 0.38 1" friction="0.5 0.01 0.005" solref="0.008 1"/>
      <geom name="bin_front" type="box" pos="0 -0.25 0.20" size="0.275 0.025 0.13" rgba="0.15 0.55 0.38 1" friction="0.5 0.01 0.005" solref="0.008 1"/>
      <geom name="bin_back" type="box" pos="0 0.25 0.20" size="0.275 0.025 0.13" rgba="0.15 0.55 0.38 1" friction="0.5 0.01 0.005" solref="0.008 1"/>

      <geom name="bin_guide_left" type="box" pos="-0.0295 0 1.60" size="0.010 0.0665 0.70" rgba="0.35 0.55 0.45 0.55" friction="0.025 0 0" solref="0.008 1"/>
      <geom name="bin_guide_right" type="box" pos="0.0295 0 1.60" size="0.010 0.0665 0.70" rgba="0.35 0.55 0.45 0.55" friction="0.025 0 0" solref="0.008 1"/>
      <geom name="bin_guide_front" type="box" pos="0 -0.0565 1.60" size="0.0195 0.010 0.70" rgba="0.35 0.55 0.45 0.35" friction="0.025 0 0" solref="0.008 1"/>
      <geom name="bin_guide_back" type="box" pos="0 0.0565 1.60" size="0.0195 0.010 0.70" rgba="0.35 0.55 0.45 0.55" friction="0.025 0 0" solref="0.008 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="ricochet_wall1" geom1="ball_sphere" geom2="wall1_reflector" condim="1" friction="0 0 0 0 0" solref="-100000 -10" solimp="0.99 0.99 0.001"/>
    <pair name="ricochet_wall2" geom1="ball_sphere" geom2="wall2_reflector" condim="1" friction="0 0 0 0 0" solref="-100000 -10" solimp="0.99 0.99 0.001"/>
    <exclude name="cam_guide_clearance" body1="target" body2="bin"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 4 1 0 0 0 0 -0.35 0 2.065 1 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{
  "what_happens": "The ball falls, ricochets from wall1 into wall2, and strikes the target. The target rotates to its upper joint stop at 75 degrees, withdrawing the cam support. The block falls into the bin and rests on its bottom; the ball rests on the floor before the run ends.",
  "works": false,
  "problem": "The target reaches its upper joint stop rather than the lower stop required by the brief."
}
```