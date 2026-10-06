The ball starts at rest on the floor, 4 m in front of the rim. Its keyframe velocity is about 3.18 m/s forward and 8.50 m/s up, plus some backspin. It peaks near 3.8 m, then comes down at about 50° and passes through the center of the rim. It never gets closer than about 5 cm to the rim tube.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="court" rgba="0.75 0.55 0.35 1"/>
    <material name="orange" rgba="0.9 0.4 0.1 1"/>
    <material name="steel" rgba="0.9 0.3 0.1 1"/>
    <material name="glass" rgba="0.85 0.9 1 0.5"/>
    <material name="grey" rgba="0.4 0.4 0.45 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="20 20 0.1" material="court" friction="0.8 0.01 0.001"/>

    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.00585 0.00585 0.00585"/>
      <geom name="ball" type="sphere" size="0.119" material="orange" friction="0.8 0.01 0.001" solref="0.01 0.3"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.01" fromto="0.2386 0 0 0.2066 0.1193 0" material="steel"/>
      <geom name="rim_01" type="capsule" size="0.01" fromto="0.2066 0.1193 0 0.1193 0.2066 0" material="steel"/>
      <geom name="rim_02" type="capsule" size="0.01" fromto="0.1193 0.2066 0 0 0.2386 0" material="steel"/>
      <geom name="rim_03" type="capsule" size="0.01" fromto="0 0.2386 0 -0.1193 0.2066 0" material="steel"/>
      <geom name="rim_04" type="capsule" size="0.01" fromto="-0.1193 0.2066 0 -0.2066 0.1193 0" material="steel"/>
      <geom name="rim_05" type="capsule" size="0.01" fromto="-0.2066 0.1193 0 -0.2386 0 0" material="steel"/>
      <geom name="rim_06" type="capsule" size="0.01" fromto="-0.2386 0 0 -0.2066 -0.1193 0" material="steel"/>
      <geom name="rim_07" type="capsule" size="0.01" fromto="-0.2066 -0.1193 0 -0.1193 -0.2066 0" material="steel"/>
      <geom name="rim_08" type="capsule" size="0.01" fromto="-0.1193 -0.2066 0 0 -0.2386 0" material="steel"/>
      <geom name="rim_09" type="capsule" size="0.01" fromto="0 -0.2386 0 0.1193 -0.2066 0" material="steel"/>
      <geom name="rim_10" type="capsule" size="0.01" fromto="0.1193 -0.2066 0 0.2066 -0.1193 0" material="steel"/>
      <geom name="rim_11" type="capsule" size="0.01" fromto="0.2066 -0.1193 0 0.2386 0 0" material="steel"/>
      <geom name="hoop_bracket" type="box" size="0.07 0.05 0.008" pos="0.31 0 0" material="steel"/>
    </body>

    <body name="backboard" pos="4.395 0 3.425">
      <geom name="backboard" type="box" size="0.015 0.915 0.525" material="glass"/>
    </body>

    <body name="support" pos="0 0 0">
      <geom name="support_arm" type="box" size="1.05 0.06 0.06" pos="5.46 0 3.6" material="grey"/>
      <geom name="support_pole" type="box" size="0.1 0.1 1.85" pos="6.6 0 1.85" material="grey"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.182 0 8.497 0 -6 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
ball touches floor
```

---
thinking (summarized):

I'm working out the regulation basketball dimensions and hoop geometry—ball radius around 0.119 m, hoop radius 0.2286 m—and setting up the launch so the ball starts resting on the floor before arcing to the hoop at 3.05 m height and 4 m distance.

Picking an apex height of 3.8 m, I calculate the launch velocity, timing, and horizontal speed needed so the ball descends steeply through the hoop at about 50°, confirming the ball's effective footprint still clears the rim comfortably. Now I'm planning to model the rim as a ring of small capsule segments to approximate the torus shape for collision purposes.

I also want to add a backboard positioned just behind the rim, and I'm figuring out the ball's trajectory as it continues past the hoop and falls toward the floor to make sure the geometry stays physically consistent.

I'm checking the distance between the ball's center and the back rim tube at several time steps to see if the ball clears it, since the gap needs to exceed the combined radii of about 0.129 m, and at each sampled point the distance looks like it's shrinking as the ball approaches.

I also check the front rim similarly for the approach path before the hoop, finding minimum distances around 0.18, which comfortably clears the required 0.129 threshold.

Good, so the ball passes through cleanly. Now I'm thinking about adding a backboard for realism, positioning it so its bottom edge sits well above the ball's trajectory with margin to spare, and placing its support pole further back out of the way.

I'm checking where the pole would need to sit so the ball's arc doesn't clip it on the way down—moving it further back to x=6.5 with a horizontal arm connecting to the backboard should clear the trajectory.

Then I'm positioning the static hoop body with rim capsules and a small bracket connecting the rim to the backboard, making sure the bracket sits low enough not to interfere with the ball's path near the rim.

I'll skip adding a net and focus on computing rim vertex coordinates around the 0.2386 radius circle at 30° intervals for the polygon approximation.

Still computing geometry...

The semi-implicit Euler integration introduces a tiny extra drop in height (about 1.2 cm at t=1.257s), which is negligible for this purpose. I'll skip adding bounce physics via solref since it's not essential, but I should consider whether rolling friction is needed so the ball doesn't roll forever once it hits the floor.

For the sphere's inertia, I'll explicitly set it using the hollow sphere formula (I = 2/3 m r²) rather than relying on default density-based calculation, giving mass 0.62 and the corresponding diagonal inertia. Now I'll finalize lighting and visual settings and write out the file.

