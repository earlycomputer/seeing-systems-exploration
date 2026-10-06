The ball is a size-7 basketball: radius 0.119 m, mass 0.62 kg, and the hollow-shell inertia I = ⅔mr² is set explicitly. It starts resting on the floor at x = 0. The keyframe launches it at (vx, vz) = (2.865, 8.948) m/s. In vacuum that path peaks at about 4.2 m. It then crosses the rim plane (z = 3.05 m) at x ≈ 4.00 m, t ≈ 1.40 s, coming down at about 59°.

The rim has a regulation 0.457 m inner diameter and is built from 16 capsules. I checked the parabola by hand: the ball centre stays at least ~0.20 m from the rim tube centreline, and contact would need 0.129 m. It also passes under the backboard, which has a regulation 0.15 m offset. After that it bounces on the floor toward the support pole.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="court" rgba="0.75 0.55 0.35 1"/>
    <material name="orange" rgba="0.9 0.4 0.1 1"/>
    <material name="rimred" rgba="0.85 0.15 0.05 1"/>
    <material name="glass" rgba="0.9 0.95 1 0.5"/>
    <material name="steel" rgba="0.3 0.3 0.35 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="2.5 -9 2.5" xyaxes="1 0 0 0 0.2 1"/>
    <geom name="floor" type="plane" pos="3 0 0" size="10 10 0.1" material="court"/>

    <body name="ball" pos="0 0 0.12">
      <freejoint/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005853 0.005853 0.005853"/>
      <geom name="ball" type="sphere" size="0.119" material="orange" solref="0.004 0.15" friction="0.8 0.01 0.001"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim0" type="capsule" size="0.01" fromto="0.2386 0 0 0.22044 0.09131 0" material="rimred"/>
      <geom name="rim1" type="capsule" size="0.01" fromto="0.22044 0.09131 0 0.16872 0.16872 0" material="rimred"/>
      <geom name="rim2" type="capsule" size="0.01" fromto="0.16872 0.16872 0 0.09131 0.22044 0" material="rimred"/>
      <geom name="rim3" type="capsule" size="0.01" fromto="0.09131 0.22044 0 0 0.2386 0" material="rimred"/>
      <geom name="rim4" type="capsule" size="0.01" fromto="0 0.2386 0 -0.09131 0.22044 0" material="rimred"/>
      <geom name="rim5" type="capsule" size="0.01" fromto="-0.09131 0.22044 0 -0.16872 0.16872 0" material="rimred"/>
      <geom name="rim6" type="capsule" size="0.01" fromto="-0.16872 0.16872 0 -0.22044 0.09131 0" material="rimred"/>
      <geom name="rim7" type="capsule" size="0.01" fromto="-0.22044 0.09131 0 -0.2386 0 0" material="rimred"/>
      <geom name="rim8" type="capsule" size="0.01" fromto="-0.2386 0 0 -0.22044 -0.09131 0" material="rimred"/>
      <geom name="rim9" type="capsule" size="0.01" fromto="-0.22044 -0.09131 0 -0.16872 -0.16872 0" material="rimred"/>
      <geom name="rim10" type="capsule" size="0.01" fromto="-0.16872 -0.16872 0 -0.09131 -0.22044 0" material="rimred"/>
      <geom name="rim11" type="capsule" size="0.01" fromto="-0.09131 -0.22044 0 0 -0.2386 0" material="rimred"/>
      <geom name="rim12" type="capsule" size="0.01" fromto="0 -0.2386 0 0.09131 -0.22044 0" material="rimred"/>
      <geom name="rim13" type="capsule" size="0.01" fromto="0.09131 -0.22044 0 0.16872 -0.16872 0" material="rimred"/>
      <geom name="rim14" type="capsule" size="0.01" fromto="0.16872 -0.16872 0 0.22044 -0.09131 0" material="rimred"/>
      <geom name="rim15" type="capsule" size="0.01" fromto="0.22044 -0.09131 0 0.2386 0 0" material="rimred"/>
      <geom name="bracket" type="box" pos="0.3093 0 -0.01" size="0.0707 0.06 0.015" material="steel"/>
      <geom name="backboard" type="box" pos="0.395 0 0.385" size="0.015 0.915 0.535" material="glass"/>
    </body>

    <body name="support" pos="0 0 0">
      <geom name="arm" type="box" pos="5.305 0 3.4" size="0.895 0.05 0.05" material="steel"/>
      <geom name="pole" type="cylinder" fromto="6.2 0 0 6.2 0 3.45" size="0.08" material="steel"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="2.865 0 8.948 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out realistic basketball specs—size 7 ball with ~0.119 m radius and ~0.62 kg mass, and a regulation rim with 0.2286 m inner radius—so I can set up a launch from the floor that arcs through the hoop 4 m away and 3.05 m high.

Picking an apex around 4.2 m lets me calculate the launch and descent velocities: vz0 ≈ 8.95 m/s, giving a descent angle at the rim of about 58.9°, which makes the effective opening (~0.39 m) comfortably wider than the ball's 0.24 m diameter. I'm placing the rim torus with its tube radius added to the inner radius for a realistic ring thickness.

Now I'm checking the tighter clearance case at the front and back rim points, computing the perpendicular distance from the trajectory line to each rim edge to confirm the ball passes without clipping the tube.

Checking the far rim clearance too, finding the closest approach stays around 0.2, comfortably clearing the rim without hitting it.

Now I'm considering whether the ball could hit the backboard on its way in—using regulation spacing where the rim's near edge sits about 0.152 m from the board, placing the rim center roughly 0.38 m from the backboard face.

Checking the corner distance confirms the ball clears the board's bottom edge safely, so it passes underneath without hitting. I'll move the stanchion pole further back to x=5.5 to avoid interference, then figure out when the ball falls to the floor from its height of 3.05 m.

Hitting the pole afterward isn't a problem for the brief, which just cares about the drop through the hoop, so I'll keep it simple. I'll make the hoop a static body positioned at the rim center with rim capsules and a separate backboard geom as children, and skip the net or just add a thin non-colliding visual for it.

Calculating rim points around the circle...

Still placing geometry...

I should also check whether the ball's arc ever crosses near the arm or board before reaching the rim, and it looks clear since the trajectory stays well below and in front. For the ball's physics, I'm considering whether to use a solid sphere inertia default or specify a hollow-shell inertia (2/3 m r²) to better match a real basketball.

Recomputing with a standard size-7 ball: radius ~0.119 m, mass ~0.62 kg, giving diagonal inertia around 0.00595. I'm redoing the launch velocity calculation with this starting height, getting vz0≈8.948 m/s paired with vx=2.865, then checking when the ball's height crosses the rim plane at z=3.05.

I also want to avoid starting the ball in contact with the floor at t=0, so I'm nudging the initial z slightly to 0.12 to prevent an unwanted collision impulse, then re-solving the crossing time with this tiny adjustment — the shift in the result is negligible.

Air density is zero by default so no drag to worry about, and no spin is needed. For the bounce behavior I'll pick a mild solref setting to give a touch of restitution without it being critical to the outcome, then finalize the keyframe with the ball's starting position and launch velocity.

The hoop stays static with no joint, so no inertia needed there — I'll skip adding net visuals and just keep things simple with a floor plane and light. Checking the trajectory, the ball should land around x≈5.23 and bounce toward the pole near x=6.2, hitting it cleanly given the pole's radius. I'm naming the rim segments and bracket, then writing out the full single-line attribute definitions for the scene.

