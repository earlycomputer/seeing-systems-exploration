The ball is launched from the floor at (2.80, 0, 9.06) m/s. It peaks at about 4.3 m and drops through the rim center about 60° below horizontal, which leaves roughly 8 cm of clearance on each side of the 18-inch rim.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="2 -3 6" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.6 0.45 0.3 1"/>
    <body name="ball" pos="0 0 0.12">
      <freejoint/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.00585 0.00585 0.00585"/>
      <geom name="ball" type="sphere" size="0.119" rgba="0.9 0.45 0.1 1" solref="0.01 0.15" friction="0.8 0.01 0.001"/>
    </body>
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.009" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="1 0.3 0 1"/>
      <geom name="rim_01" type="capsule" size="0.009" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="1 0.3 0 1"/>
      <geom name="rim_02" type="capsule" size="0.009" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="1 0.3 0 1"/>
      <geom name="rim_03" type="capsule" size="0.009" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="1 0.3 0 1"/>
      <geom name="rim_04" type="capsule" size="0.009" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="1 0.3 0 1"/>
      <geom name="rim_05" type="capsule" size="0.009" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="1 0.3 0 1"/>
      <geom name="rim_06" type="capsule" size="0.009" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="1 0.3 0 1"/>
      <geom name="rim_07" type="capsule" size="0.009" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="1 0.3 0 1"/>
      <geom name="rim_08" type="capsule" size="0.009" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="1 0.3 0 1"/>
      <geom name="rim_09" type="capsule" size="0.009" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="1 0.3 0 1"/>
      <geom name="rim_10" type="capsule" size="0.009" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="1 0.3 0 1"/>
      <geom name="rim_11" type="capsule" size="0.009" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="1 0.3 0 1"/>
      <geom name="rim_12" type="capsule" size="0.009" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="1 0.3 0 1"/>
      <geom name="rim_13" type="capsule" size="0.009" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="1 0.3 0 1"/>
      <geom name="rim_14" type="capsule" size="0.009" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="1 0.3 0 1"/>
      <geom name="rim_15" type="capsule" size="0.009" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="1 0.3 0 1"/>
      <geom name="bracket" type="box" pos="0.309 0 -0.015" size="0.072 0.03 0.01" rgba="0.3 0.3 0.3 1"/>
      <geom name="backboard" type="box" pos="0.396 0 0.385" size="0.015 0.915 0.535" rgba="0.95 0.95 1 0.6"/>
    </body>
    <body name="stand" pos="5.6 0 0">
      <geom name="pole" type="cylinder" fromto="0 0 0 0 0 3.35" size="0.1" rgba="0.2 0.2 0.25 1"/>
      <geom name="arm" type="box" pos="-0.585 0 3.3" size="0.6 0.05 0.05" rgba="0.2 0.2 0.25 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="2.8012 0 9.056 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical dimensions needed: a regulation basketball with radius around 0.12 m, and a hoop rim with inner diameter 0.4572 m positioned at 3.05 m height, 4 m away from the launch point on the floor.

I need to figure out the right trajectory angle so the ball clears the rim without clipping it—since the ball is wide relative to the hoop opening, a steep descent angle (over roughly 32°) is necessary for the effective opening to be large enough, so I'm aiming for something closer to 55°. I'm also modeling the rim itself as a ring made of small capsule segments to approximate its physical shape.

Assuming no air drag since MuJoCo defaults to zero density, I compute a parabolic trajectory with an apex around 4.3m, giving a vertical velocity of about 9.06 m/s and total flight time of 1.43s, which works out to roughly 2.8 m/s horizontal speed and a 60.5° entry angle at the rim—steep enough to clear cleanly.

Checking clearance at the front rim: the ball's center passes well above the front rim point, with a perpendicular distance of about 0.206m from the rim edge, comfortably more than the rim tube's 0.128m radius, so it should swish through without hitting iron.

I then traced the ball's fall to the floor after passing through the net, computing it lands around x≈5.17 after a short additional drop, then considered whether to model a backboard near x=4.15-4.23 for completeness.

That's close enough to be fine. I'll keep it simple and skip a separate support pole, just attaching the backboard directly to the static hoop body rather than modeling realistic mounting hardware.

Computing geometry for the backboard bracket and rim capsule segments, checking that the ball's trajectory clears these attachments and working out the angular positions for each of the 16 rim segments.

Calculating remaining ring points, then checking capsule clearance against inner radius which comes out fine. Now working out the hoop and backboard positioning, using regulation distance of 15 inches from rim to backboard face.

Defining the bracket geometry connecting rim to backboard, naming all bodies and geoms as required, and setting up the stand body with its pole and arm placement.

I'm checking the ball's trajectory after it bounces off the floor and heads toward the pole, and adjusting the ball radius to match regulation size (~0.119m) and mass (0.62kg) with appropriate inertia handling.

Confirming vx=2.8012 matches, skipping any backspin addition, using default gravity. Now I'll write the final file.

