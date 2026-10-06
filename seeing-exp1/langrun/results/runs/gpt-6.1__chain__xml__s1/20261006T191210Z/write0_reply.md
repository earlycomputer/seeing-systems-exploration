```xml
<mujoco model="three_balls_into_a_cup">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" cone="elliptic"/>
  <size njmax="1000" nconmax="200"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
    <headlight ambient="0.3 0.3 0.3" diffuse="0.6 0.6 0.6" specular="0.2 0.2 0.2"/>
    <rgba haze="0.85 0.9 0.95 1"/>
  </visual>

  <worldbody>
    <light name="key_light" pos="-1 -2 3" dir="0.3 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <light name="fill_light" pos="1 1 2" dir="-0.3 -0.3 -1" diffuse="0.4 0.4 0.4"/>
    <camera name="overview" pos="0.1 -2.4 1.7" xyaxes="1 0 0 0 0.57 0.82" fovy="42"/>

    <geom name="floor" type="plane" pos="0 0 0" size="3 2 0.1" rgba="0.82 0.84 0.86 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" solimp="0.95 0.99 0.001" priority="1"/>

    <body name="ball1" pos="-0.65 0 0.05">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.1" rgba="0.85 0.16 0.12 1" condim="6" friction="0.65 0.003 0.002" solref="0.006 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="-0.25 0 0.05">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.1" rgba="0.95 0.65 0.08 1" condim="6" friction="0.65 0.003 0.002" solref="0.006 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball3" pos="0.15 0 0.05">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.1" rgba="0.12 0.35 0.9 1" condim="6" friction="0.65 0.003 0.002" solref="0.006 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- A fixed cup lying on its side, with its open mouth facing the balls.
         Sixteen wall panels form a hollow tube; the cylinder closes its far end.
         The inside bottom is only 8 mm above the floor. -->
    <body name="cup" pos="0.68 0 0.124">
      <geom name="cup_wall_00" type="box" pos="0 0 0.12" euler="0 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_01" type="box" pos="0 -0.045922 0.110866" euler="22.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_02" type="box" pos="0 -0.084853 0.084853" euler="45 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_03" type="box" pos="0 -0.110866 0.045922" euler="67.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_04" type="box" pos="0 -0.12 0" euler="90 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_05" type="box" pos="0 -0.110866 -0.045922" euler="112.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_06" type="box" pos="0 -0.084853 -0.084853" euler="135 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_07" type="box" pos="0 -0.045922 -0.110866" euler="157.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_08" type="box" pos="0 0 -0.12" euler="180 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_09" type="box" pos="0 0.045922 -0.110866" euler="202.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_10" type="box" pos="0 0.084853 -0.084853" euler="225 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_11" type="box" pos="0 0.110866 -0.045922" euler="247.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_12" type="box" pos="0 0.12 0" euler="270 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_13" type="box" pos="0 0.110866 0.045922" euler="292.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_14" type="box" pos="0 0.084853 0.084853" euler="315 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_wall_15" type="box" pos="0 0.045922 0.110866" euler="337.5 0 0" size="0.16 0.0243 0.004" rgba="0.22 0.48 0.52 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
      <geom name="cup_base" type="cylinder" pos="0.164 0 0" euler="0 90 0" size="0.124 0.004" rgba="0.18 0.39 0.43 1" condim="6" friction="0.65 0.003 0.002" solref="0.008 1" priority="1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Ball 1 begins in pure rolling motion: vx = radius * omega_y. -->
    <key name="start" time="0" qpos="-0.65 0 0.05 1 0 0 0 -0.25 0 0.05 1 0 0 0 0.15 0 0.05 1 0 0 0" qvel="2.1 0 0 0 42 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Analyzing ball collision dynamics**

I'm considering how restitution affects the bouncing of three balls in a sequence. The first ball transfers translational velocity while maintaining its spin, then rolls and accelerates. The second ball receives this velocity but without spin, decelerating. I need to ensure they are spaced correctly to fit in a cup after six seconds. I’m also evaluating their speeds and how they might interact, ensuring the first and second balls don’t just chase the third but manage to roll together effectively.

**Examining ball dynamics with friction**

I'm considering how friction affects three balls rolling into a cup. The third ball needs to settle in the cup first before the others can follow. I'm evaluating different rolling frictions and how they decelerate each ball. Initial speeds and spins will change based on mass, but I prefer equal weights for consistency. If the cup is positioned close enough, all three balls could land inside. I think about how to design a ramp on the cup's side to help the third ball rise and drop into the cup effectively.

**Designing the cup with ramps**

I'm exploring the design of a cup that has a wall cut halfway to create a ramp for balls. The ramp should allow a smooth climb of .025, similar to a tipped drinking cup. I need to ensure that the horizontal bottom lip of the cup is only .008 to permit the right velocities for the balls. The interior radius will be .116 while the outer radius is .124. The ball's radius is .05, so a smooth surface is essential for proper movement.