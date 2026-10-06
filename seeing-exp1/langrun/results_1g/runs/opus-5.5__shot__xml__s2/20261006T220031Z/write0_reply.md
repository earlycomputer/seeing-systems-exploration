The ball starts resting on the floor with its center at z = 0.119 m. It is launched at (3.008, 0, 8.726) m/s, which gives it a 4.0 m apex. It comes down through the rim center at 4 m, entering at about 55°. At that angle the ball passes about 19 cm from the rim tube centers on both the front and back of the rim. The ball would collide if it came within 12.7 cm, so the path is clear. The ball then passes under the backboard and lands at about x = 5.35 m.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="2 -3 6" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 5 0.1" rgba="0.75 0.6 0.4 1"/>
    <body name="ball" pos="0 0 0.119">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.119" mass="0.62" rgba="0.9 0.45 0.1 1"/>
    </body>
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.21859 0.09054 0" rgba="1 0.3 0 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.21859 0.09054 0 0.16730 0.16730 0" rgba="1 0.3 0 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.16730 0.16730 0 0.09054 0.21859 0" rgba="1 0.3 0 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.09054 0.21859 0 0 0.2366 0" rgba="1 0.3 0 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.09054 0.21859 0" rgba="1 0.3 0 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.09054 0.21859 0 -0.16730 0.16730 0" rgba="1 0.3 0 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.16730 0.16730 0 -0.21859 0.09054 0" rgba="1 0.3 0 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.21859 0.09054 0 -0.2366 0 0" rgba="1 0.3 0 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.21859 -0.09054 0" rgba="1 0.3 0 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.21859 -0.09054 0 -0.16730 -0.16730 0" rgba="1 0.3 0 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.16730 -0.16730 0 -0.09054 -0.21859 0" rgba="1 0.3 0 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.09054 -0.21859 0 0 -0.2366 0" rgba="1 0.3 0 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.09054 -0.21859 0" rgba="1 0.3 0 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.09054 -0.21859 0 0.16730 -0.16730 0" rgba="1 0.3 0 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.16730 -0.16730 0 0.21859 -0.09054 0" rgba="1 0.3 0 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.21859 -0.09054 0 0.2366 0 0" rgba="1 0.3 0 1"/>
      <geom name="bracket" type="box" size="0.07 0.04 0.01" pos="0.305 0 0" rgba="0.4 0.4 0.4 1"/>
      <geom name="backboard" type="box" size="0.015 0.915 0.535" pos="0.38 0 0.385" rgba="0.95 0.95 0.95 0.6"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.119 1 0 0 0" qvel="3.008 0 8.726 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
ball touches floor
```

---
thinking (summarized):

I'm working out regulation basketball dimensions—circumference, radius, mass—and rim specs like inner diameter and tube thickness, so I can set up the physics of a shot arcing from the floor into the hoop at 3.05 m height and 4 m away.

Computing a steep trajectory with an apex around 4.0 m gives launch and entry velocities that yield roughly a 55° entry angle, which clears the rim comfortably given the ball's diameter relative to the rim opening. Now I'm planning the rim geometry itself, building it as a ring of small capsule segments at the correct centerline radius and tube thickness to approximate the hoop realistically in MuJoCo.

Computing remaining points...

Now I'm checking if a backboard is needed, sizing it based on regulation rim-to-board distance and positioning it near x=4.38 with proper height and width.

After passing the rim, I'm computing the ball's remaining fall to the floor given its downward velocity, finding it lands around x=5.35. Then I'm checking whether the ball's path would actually intersect the backboard at x≈4.246, verifying its height there to see if a collision occurs before it reaches the floor.

I decide the ball clears under the board since its top stays below the board's bottom edge, so no collision with the backboard occurs. I also weigh whether to add a support pole or bracket for the backboard, deciding it's simpler to just include the backboard without extra structural supports since it's static and the ball clears it anyway.

Then I check the rim clearance more precisely: computing the perpendicular distance from the trajectory line to the front rim's tube center, confirming it's safely larger than the combined radius needed to avoid clipping.

I'm not too worried about bounce dynamics or rolling friction since the task doesn't require precise post-bounce behavior, just that the ball passes through the hoop. For inertia, I'll keep things simple with a default solid sphere approximation rather than hollow-shell inertia, using mass 0.62. Then I set up the keyframe with the initial position and orientation for the freejoint.

Setting velocities so the ball launches toward the hoop at x=4, starting from x=0 at floor contact height. The hoop itself stays static with no joint, positioned at (4, 0, 3.05), and I add a backboard geom offset behind the rim plus a bracket connecting them, checking that the ball's trajectory passes well below the bracket so there's no unwanted collision.

