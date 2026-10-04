The ball is launched from the floor with a keyframe velocity of (3.193, 0, 8.484) m/s. That arc is designed to peak near 3.79 m and drop through the rim center at about 1.25 s, falling at roughly 50° below horizontal. I checked these numbers by hand, not by running the simulation.

- **Ball:** regulation size 7, r = 0.12 m, m = 0.62 kg, hollow-shell inertia.
- **Rim:** 18″ inner diameter, made of 16 capsule segments.
- **Clearance:** along that path the ball's center passes at least about 0.17 m from the rim tube, which leaves about 0.045 m of margin.
- **Backboard:** placed to regulation. The ball passes under its 2.90 m bottom edge after going through the hoop.
- **Net:** visual only, with no collisions.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.75 0.6 0.4 1"/>

    <body name="ball" pos="0 0 0.12">
      <freejoint/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.00595 0.00595 0.00595"/>
      <geom name="ball" type="sphere" size="0.12" rgba="0.9 0.45 0.1 1" solref="0.01 0.15" friction="0.8 0.01 0.001"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.009" fromto="0.2286 0 0 0.2112 0.0875 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.009" fromto="0.2112 0.0875 0 0.1616 0.1616 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.009" fromto="0.1616 0.1616 0 0.0875 0.2112 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.009" fromto="0.0875 0.2112 0 0 0.2286 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.009" fromto="0 0.2286 0 -0.0875 0.2112 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.009" fromto="-0.0875 0.2112 0 -0.1616 0.1616 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.009" fromto="-0.1616 0.1616 0 -0.2112 0.0875 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.009" fromto="-0.2112 0.0875 0 -0.2286 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.009" fromto="-0.2286 0 0 -0.2112 -0.0875 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.009" fromto="-0.2112 -0.0875 0 -0.1616 -0.1616 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.009" fromto="-0.1616 -0.1616 0 -0.0875 -0.2112 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.009" fromto="-0.0875 -0.2112 0 0 -0.2286 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.009" fromto="0 -0.2286 0 0.0875 -0.2112 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.009" fromto="0.0875 -0.2112 0 0.1616 -0.1616 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.009" fromto="0.1616 -0.1616 0 0.2112 -0.0875 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.009" fromto="0.2112 -0.0875 0 0.2286 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="bracket" type="box" pos="0.305 0 0" size="0.076 0.05 0.008" rgba="0.9 0.3 0.05 1"/>
      <geom name="net_0" type="capsule" size="0.004" fromto="0.2286 0 0 0.12 0 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_1" type="capsule" size="0.004" fromto="-0.2286 0 0 -0.12 0 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_2" type="capsule" size="0.004" fromto="0 0.2286 0 0 0.12 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_3" type="capsule" size="0.004" fromto="0 -0.2286 0 0 -0.12 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_4" type="capsule" size="0.004" fromto="0.1616 0.1616 0 0.085 0.085 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_5" type="capsule" size="0.004" fromto="-0.1616 0.1616 0 -0.085 0.085 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_6" type="capsule" size="0.004" fromto="-0.1616 -0.1616 0 -0.085 -0.085 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
      <geom name="net_7" type="capsule" size="0.004" fromto="0.1616 -0.1616 0 0.085 -0.085 -0.4" contype="0" conaffinity="0" rgba="1 1 1 0.6"/>
    </body>

    <body name="backboard_support" pos="0 0 0">
      <geom name="backboard" type="box" pos="4.406 0 3.435" size="0.025 0.915 0.535" rgba="0.95 0.95 0.95 0.8"/>
      <geom name="support_arm" type="box" pos="5.455 0 3.6" size="1.025 0.06 0.06" rgba="0.3 0.3 0.35 1"/>
      <geom name="pole" type="cylinder" pos="6.5 0 1.83" size="0.1 1.83" rgba="0.3 0.3 0.35 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.193 0 8.484 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm setting up the physical parameters for a basketball shot scene: a regulation ball radius and mass, hoop height of 3.05 meters, horizontal distance of 4 meters, and the rim's inner radius so the trajectory can be computed to pass cleanly through the hoop opening starting from the ball resting on the floor.

Checking the clearance geometry, I realize the ball needs to enter the rim at a steep enough angle — above about 33 degrees from horizontal — so its effective width doesn't exceed the opening, so I'm aiming for a descent angle around 45-50 degrees. I'm now solving the parabolic trajectory equations to find launch velocity and angle that satisfy both the horizontal distance and this steep entry angle at the hoop.

That checks out, so the trajectory passes through the hoop correctly with no need for air drag modeling since MuJoCo defaults to zero density. I'm now checking whether the ball would clip the backboard afterward—regulation puts the rim 0.381 m from the backboard face, and tracing the ball's path past the rim shows it would reach the backboard plane shortly after, though by then it's already dropped well below backboard height, so it shouldn't interfere.

I need to check whether the ball clears the support bracket as it passes through the rim. Tracking the ball's trajectory after it crosses the hoop plane, I calculate where it would intersect the bracket's x-range and find its height there is too low, so I'll need to position the bracket thin and just above the rim plane, with its bottom around z=3.04, to keep it clear of the ball's path.

Checking both near and far rim points confirms clearance margin of about 0.045, so the ball should pass through safely without clipping the rim. Now I'm setting up the static hoop body at its position, building the rim out of 16 capsule segments arranged in a circle using fromto coordinates computed from the angle around the circle.

Continuing through the remaining points around the circle, I confirm the minimum perpendicular opening stays around 0.17 even with the inward chord offset. For the rim tube I'm setting radius to about 0.009, and now I'm sizing a bracket box within the hoop body spanning roughly x=0.2286 to 0.381, centered near 0.305.

Now I'm setting up the backboard as a thin box positioned behind the rim with appropriate width and height, plus a pole and arm structure to support it. I'm deciding to skip the net geometry or possibly leave it as a non-colliding visual, and moving on to defining the ball's mass and size properties.

For the ball, I'm using a regulation size-7 radius of about 0.119m and computing a hollow-sphere moment of inertia to use as explicit inertial data, so the physics engine doesn't fall back to solid-sphere assumptions. I'm setting the keyframe with an initial launch velocity and starting position matching the ball's radius above the ground.

I'll give the start a tiny 0.12 gap above the floor to avoid initial penetration contact, and I'm tuning solref values on the ball's contact to get a natural bounce rather than a dead stop. I'm also double-checking the trajectory against the rim geometry to confirm the ball clears or touches the hoop at the right point without clipping the near side on the way down.

Checking the backboard corners now — at various points along the path the ball's center stays far enough from the corner coordinates that it passes safely underneath without contact, so the shot trajectory looks clean through the hoop.

Now I need to figure out where the support pole lands relative to the ball's fall. Calculating the landing time after the bounce (about 0.477s), the ball would come down near x=5.52, so I should position the pole farther out, maybe around x=5.6-6.2, so it doesn't interfere even after the bounce — the connecting arm up near the backboard height should be fine too.

I'm settling on moving the pole to x=6.5 with the support arm running from the pole up to the backboard's back side, keeping it clear of the bounce path. Then I just need to size the floor plane, add lighting, and write everything out.

