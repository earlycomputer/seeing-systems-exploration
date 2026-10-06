The ball is launched from the floor at (0, 0, 0.1195) with velocity (3.0085, 0, 8.7256) m/s. That gives it an apex of 4.0 m. It then falls through the center of a 0.457 m regulation rim at x = 4 m, z = 3.05 m, coming down at about 55°.

**Checks I worked out by hand (I did not run the simulation):**
- **Timing:** the ball reaches the rim plane 1.33 s after launch.
- **Rim clearance:** the ball's center stays about 0.19 m from both the front and back rim tubes along its path. That is more than the 0.13 m needed (ball radius plus tube radius).
- **Support:** the rim is held from the side, from a pole at y = 1 m. Nothing stands behind the hoop, so the ball's path is clear in the x–z plane.
- **Coming to rest:** the ball lands near x ≈ 5.35 m at about 1.8 s. Rolling friction on the ball (condim 6) should stop it, by my estimate near x ≈ 6 m by about 3 s. That is well inside the 6 s run and the 5 cm/s rest threshold.

**Simplifications:**
- **No backboard or net.** At this launch angle the ball would hit the bottom edge of a regulation backboard after passing through the rim, and a net would also touch it.
- **Barely any bounce.** MuJoCo's default contacts are close to inelastic, so the ball hardly bounces on landing. That keeps the settling predictable.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="12 12 0.1" rgba="0.75 0.6 0.4 1"/>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" fromto="0.237 0 0 0.2190 0.0907 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_01" type="capsule" fromto="0.2190 0.0907 0 0.1676 0.1676 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_02" type="capsule" fromto="0.1676 0.1676 0 0.0907 0.2190 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_03" type="capsule" fromto="0.0907 0.2190 0 0 0.237 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_04" type="capsule" fromto="0 0.237 0 -0.0907 0.2190 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_05" type="capsule" fromto="-0.0907 0.2190 0 -0.1676 0.1676 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_06" type="capsule" fromto="-0.1676 0.1676 0 -0.2190 0.0907 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_07" type="capsule" fromto="-0.2190 0.0907 0 -0.237 0 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_08" type="capsule" fromto="-0.237 0 0 -0.2190 -0.0907 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_09" type="capsule" fromto="-0.2190 -0.0907 0 -0.1676 -0.1676 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_10" type="capsule" fromto="-0.1676 -0.1676 0 -0.0907 -0.2190 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_11" type="capsule" fromto="-0.0907 -0.2190 0 0 -0.237 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_12" type="capsule" fromto="0 -0.237 0 0.0907 -0.2190 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_13" type="capsule" fromto="0.0907 -0.2190 0 0.1676 -0.1676 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_14" type="capsule" fromto="0.1676 -0.1676 0 0.2190 -0.0907 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="rim_15" type="capsule" fromto="0.2190 -0.0907 0 0.237 0 0" size="0.009" rgba="1 0.35 0 1"/>
      <geom name="hoop_arm" type="box" pos="0 0.625 0" size="0.015 0.38 0.015" rgba="0.3 0.3 0.3 1"/>
      <geom name="hoop_pole" type="cylinder" fromto="0 1.0 -3.05 0 1.0 0.05" size="0.05" rgba="0.3 0.3 0.3 1"/>
      <geom name="hoop_base" type="box" pos="0 1.0 -3.0" size="0.3 0.3 0.05" rgba="0.2 0.2 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.1195">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005903 0.005903 0.005903"/>
      <geom name="ball" type="sphere" size="0.1195" condim="6" friction="0.8 0.02 0.05" rgba="0.85 0.4 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.1195 1 0 0 0" qvel="3.008544 0 8.72556 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical parameters for a basketball shot trajectory—ball size and mass, hoop height and horizontal distance, rim diameter—so the ball arcs from the floor and descends through the hoop at the correct point.

Picking an apex height of 4.0 m, I compute the initial vertical velocity and timing by splitting the flight into rise and fall phases, then solving for horizontal velocity so the ball covers 4 m in that total time, giving a descent angle around 55° at the rim—a clean, makeable shot. I'm also checking clearance against the rim tube thickness to confirm the ball's center stays safely inside the rim's effective radius, and verifying the ball doesn't clip the front rim by checking its height at the point where it reaches that near-side edge.

Confirming via perpendicular distance that both the front and back rim points stay well clear of the ball's trajectory line, roughly 0.194 m away versus the 0.1275 m clearance needed, so the shot geometry checks out symmetrically.

Now I'm thinking about what happens after the ball passes through the hoop — it'll fall, hit the floor, and bounce, but with horizontal velocity around 3 m/s it would just keep rolling indefinitely unless I add damping. I should consider adding rolling friction via contact properties, or some other mechanism to bring it to rest within the simulation window rather than letting it roll forever.

Working through the rolling friction deceleration: with μr=0.05 and r=0.12, the ball decelerates around 2.92 m/s², so starting at roughly 2.14 m/s rolling speed it stops within about a second, which seems reasonable. I'm also considering vertical bounce behavior — MuJoCo's default contact solref is fairly inelastic so the ball would barely bounce, and I may need to tune solref to get realistic basketball-like bouncing instead.

Floor friction should convert sliding to rolling quickly. Computing the trajectory: the ball falls from z=3.05 with vz=-4.317, landing around t=0.449s after reaching peak, hitting the floor at roughly x=5.35 at t≈1.78s, then rolling to a stop near x≈6.5 about a second later with nothing in its path. I should check whether the backboard, positioned just behind the rim with about 0.15m clearance, could interfere with this trajectory.

Checking the backboard position at x≈4.38, I trace the ball's height as it passes that point shortly after clearing the hoop and find its top edge at z≈2.76 could actually clip the bottom of the backboard, which sits around z=2.745 — so there may be a collision there that I need to account for in the trajectory.

I'm reconsidering the hoop's support structure instead of worrying about that collision: rather than a backboard, I could mount the rim on a bracket arm extending from a pole, placing the pole off to the side or behind so it doesn't interfere with the ball's forward path after it passes through the net.

Now I'm working out the geometry for the rim itself, building it from a ring of small capsules positioned around a circle to form the hoop shape, skipping the net and backboard entirely to avoid unwanted collisions.

Finishing the remaining hoop rim points, then checking the inner edge clearance against the ball radius to confirm the trajectory passes cleanly through center. Now I'm positioning the support arm attachment at the rim, sizing its box dimensions and centering it between the hoop and backboard.

I'm placing the pole as a cylinder geom within the hoop body, spanning from ground to the rim height, and adding the base box. Then I'm computing the exact keyframe values for the ball's initial position and launch velocity, working out the fall time and height using gravity to get precise numbers for the simulation.

I'm also checking clearances so the ball doesn't collide with the support arm during flight, and deciding how to handle the ball's rotational inertia—considering whether to use a shell inertia attribute or explicitly specify the inertial properties for a hollow sphere using the standard moment of inertia formula.

Working through the physics after landing: computing the rolling deceleration from friction, the transition speed once the ball stops sliding and starts pure rolling, and roughly how long it takes to come to rest. I'm also setting the contact friction parameters (sliding, torsional, rolling) on the ball geom and checking how they combine with the floor's default friction values.

Estimating landing happens around 1.78s and the ball settles by roughly 3s, ending up around x≈6 on a large 10x10 floor plane. The solver timing constants look fine for the simulation timestep, and I'll add lights and give the ball an orange color for a nicer visual before writing out the file.

