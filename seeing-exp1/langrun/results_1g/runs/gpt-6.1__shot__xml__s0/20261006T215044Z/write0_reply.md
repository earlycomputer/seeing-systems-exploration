The `start` keyframe launches the basketball from floor level toward a regulation-size rim centered 4 m away and 3.05 m high.

```xml
<mujoco model="basketball_shot">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="RK4"/>

  <visual>
    <global azimuth="135" elevation="-20"/>
    <rgba haze="0.85 0.9 0.95 1"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="2 -3 8" dir="0 0 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="shot_view" pos="2 -9 4" xyaxes="1 0 0 0 0.1644 0.9864"/>

    <geom name="floor" type="plane" pos="0 0 0" size="12 8 0.1" rgba="0.65 0.48 0.3 1" friction="0.7 0.005 0.0001" solref="0.012 1"/>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" fromto="0.237600 0 0 0.233035 0.046353 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_01" type="capsule" fromto="0.233035 0.046353 0 0.219514 0.090926 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_02" type="capsule" fromto="0.219514 0.090926 0 0.197558 0.132003 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_03" type="capsule" fromto="0.197558 0.132003 0 0.168009 0.168009 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_04" type="capsule" fromto="0.168009 0.168009 0 0.132003 0.197558 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_05" type="capsule" fromto="0.132003 0.197558 0 0.090926 0.219514 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_06" type="capsule" fromto="0.090926 0.219514 0 0.046353 0.233035 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_07" type="capsule" fromto="0.046353 0.233035 0 0 0.237600 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_08" type="capsule" fromto="0 0.237600 0 -0.046353 0.233035 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_09" type="capsule" fromto="-0.046353 0.233035 0 -0.090926 0.219514 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_10" type="capsule" fromto="-0.090926 0.219514 0 -0.132003 0.197558 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_11" type="capsule" fromto="-0.132003 0.197558 0 -0.168009 0.168009 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_12" type="capsule" fromto="-0.168009 0.168009 0 -0.197558 0.132003 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_13" type="capsule" fromto="-0.197558 0.132003 0 -0.219514 0.090926 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_14" type="capsule" fromto="-0.219514 0.090926 0 -0.233035 0.046353 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_15" type="capsule" fromto="-0.233035 0.046353 0 -0.237600 0 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_16" type="capsule" fromto="-0.237600 0 0 -0.233035 -0.046353 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_17" type="capsule" fromto="-0.233035 -0.046353 0 -0.219514 -0.090926 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_18" type="capsule" fromto="-0.219514 -0.090926 0 -0.197558 -0.132003 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_19" type="capsule" fromto="-0.197558 -0.132003 0 -0.168009 -0.168009 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_20" type="capsule" fromto="-0.168009 -0.168009 0 -0.132003 -0.197558 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_21" type="capsule" fromto="-0.132003 -0.197558 0 -0.090926 -0.219514 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_22" type="capsule" fromto="-0.090926 -0.219514 0 -0.046353 -0.233035 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_23" type="capsule" fromto="-0.046353 -0.233035 0 0 -0.237600 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_24" type="capsule" fromto="0 -0.237600 0 0.046353 -0.233035 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_25" type="capsule" fromto="0.046353 -0.233035 0 0.090926 -0.219514 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_26" type="capsule" fromto="0.090926 -0.219514 0 0.132003 -0.197558 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_27" type="capsule" fromto="0.132003 -0.197558 0 0.168009 -0.168009 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_28" type="capsule" fromto="0.168009 -0.168009 0 0.197558 -0.132003 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_29" type="capsule" fromto="0.197558 -0.132003 0 0.219514 -0.090926 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_30" type="capsule" fromto="0.219514 -0.090926 0 0.233035 -0.046353 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="rim_31" type="capsule" fromto="0.233035 -0.046353 0 0.237600 0 0" size="0.009" rgba="0.9 0.16 0.04 1"/>
      <geom name="hoop_mount" type="box" pos="0.309 0 0" size="0.072 0.045 0.012" rgba="0.9 0.16 0.04 1"/>
    </body>

    <body name="backboard" pos="4.411 0 3.425">
      <geom name="backboard" type="box" size="0.03 0.9 0.525" rgba="0.85 0.92 1 0.45"/>
    </body>

    <body name="ball" pos="0 0 0.12">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.12" mass="0.624" rgba="0.95 0.34 0.055 1" friction="0.7 0.005 0.0001" solref="0.012 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" time="0" qpos="0 0 0.12 1 0 0 0" qvel="3 0 8.7375 0 -12 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
```

---
thinking (summarized):

**Analyzing backboard dimensions**

I'm considering the dimensions of the regulation backboard, noting that the rim center is 0.381 from the plane, with specific measurements for thickness and height. The lower edge is 2.9, and the upper edge is 3.95, with a center height of 3.425. Then, I analyze the ball's trajectory and its interaction with the backboard. It looks like the ball could hit the support but will drop before making it to the hoop. It’s all about calculating the right angles and impacts!

**Evaluating polygon measurements**

I'm working with 24 straight polygons, calculating an inner radius of about 0.2376. I see that the diameter is 0.4531, which is within the regulation of 450 to 459 mm, so that’s good! Using 32 increments makes for easier coordinates at 15-degree angles with a radius of 0.2381. I find the minimum radius works well, and the conventional ring radius choice fits too. I can also simplify the design by omitting basketball stripes for a smooth sphere.

**Analyzing hoop specifications**

I'm looking at the hoop's components, like the hoop_mount and the backboard geometry. It seems the ring geometry is designed to exclude the backboard to avoid confusion. I wonder if the expectation detector considers all the hoop's body geometries as a union around the center. The hoop body is static with no joints, and the ball should drop through without touching the floor. I also want to ensure that the specifications for launching the ball are correct.