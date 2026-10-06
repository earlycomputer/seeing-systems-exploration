The 1 kg weight drops about 2.4 m onto the raised end of a 2 m seesaw, which is tilted 15° and pivots 0.3 m above the floor. The 100 g ball sits in a lipped pocket at the lowered end. The impact should spin the plank at roughly 5 rad/s. When the plank hits its joint stop, the ball should leave at about 4–5 m/s, which I estimate gives a rise of roughly 0.9 m. That estimate is a hand calculation and has not been checked in simulation.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="plank_mat" rgba="0.6 0.4 0.2 1"/>
    <material name="weight_mat" rgba="0.2 0.2 0.25 1"/>
    <material name="ball_mat" rgba="0.9 0.2 0.1 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 5" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" material="floor_mat" friction="1 0.005 0.005"/>

    <!-- visual-only fulcrum under the pivot -->
    <geom name="fulcrum" type="box" pos="0 0 0.14" size="0.05 0.12 0.14" rgba="0.4 0.4 0.4 1" contype="0" conaffinity="0"/>

    <!-- seesaw: tilted 15 deg so the +x (ball) end is down, -x (weight) end is up -->
    <body name="seesaw" pos="0 0 0.3" euler="0 15 0">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" pos="0 0 0" limited="true" range="-30 0" damping="0.5"/>
      <geom name="plank" type="box" size="1.0 0.1 0.02" mass="1.0" material="plank_mat"/>
      <geom name="lip_ball" type="box" pos="0.96 0 0.06" size="0.02 0.1 0.04" mass="0.05" material="plank_mat"/>
      <geom name="lip_weight" type="box" pos="-0.96 0 0.06" size="0.02 0.1 0.04" mass="0.05" material="plank_mat"/>
    </body>

    <!-- 1 kg weight dropped from rest above the raised end -->
    <body name="weight" pos="-0.82 0 3.0">
      <freejoint name="weight_free"/>
      <geom name="weight" type="sphere" size="0.08" mass="1.0" condim="6" friction="1 0.01 0.01" material="weight_mat"/>
    </body>

    <!-- 100 g ball resting in the pocket at the lowered end -->
    <body name="ball" pos="0.9141 0 0.1183">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.01 0.01" material="ball_mat"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm designing a seesaw mechanism with a pivot at the center: a weight dropped onto one end should launch a lighter ball on the other end at least 0.5 m into the air. I'm working out the physics—impact velocity from drop height, plank length of 2 m, and how plank mass affects the energy transfer to the ball.

I'm thinking about how to keep the ball from bouncing or rolling away indefinitely after landing, so I'll add rolling friction via condim 6 contacts between ball and floor. For the seesaw geometry, I'm planning a classic tilted start with the ball end down touching the ground and the weight end raised, so the weight's drop onto the raised end flings the ball upward.

Rather than computing the tilt trigonometry by hand, I'm considering just defining the hinge angle directly through a keyframe, setting the plank's initial rotation and working out the ball's starting position to match.

Using θ=15° gives concrete sine/cosine values, so I'm computing the pivot height so the +x end just clears the floor, settling around h=0.30 with a tiny gap. Then I set a hinge range so the joint naturally rests with the ball end down and rotating further positive is blocked, while negative rotation lifts that end back up.

I need to figure out the full swing range so the weighted end stops at the floor, roughly symmetric around -30°, and set a limited hinge range like "-29 0.5". For the fulcrum support, I'm considering using a world-attached box geom, and checking whether MuJoCo's default parent-filtering will automatically exclude contacts between the plank and its supporting world geom.

The floor should act as a backup stop, not the main limit, so that's consistent with the joint range already hitting first. For the ball, I'm computing its mass and realizing it will roll down the tilted plank and fall off the lower end unless I add a stopper lip — so I'll place a small box lip near the end to create a cup effect holding the ball in place.

Applying the rotation gives ball world position roughly (0.914, 0, 0.117), confirming it sits just at the plank's edge near the lip. Now I'm working out where the dropped weight (radius 0.08) should land on the opposite end of the plank, targeting local x=-0.85 and converting that into world coordinates through the same rotation to position the surface correctly.

I'm estimating the drop height and impact velocity for the weight falling about 2.4 m, then thinking through the physics of the collision: lever arm distance from the pivot, moment of inertia of the plank and ball, and how the impulse from the weight's impact translates into angular momentum about the pivot point.

Working through the numbers, I get roughly 4.85 rad/s angular velocity after impact, giving the ball a tangential speed near 4.5 m/s, which then builds further as the plank swings through its 30° range before hitting the limit. After the plank stops, the ball should launch upward with enough speed to rise close to a meter, giving decent margin—though I note the real contact dynamics in MuJoCo will be softer than this idealized perfectly inelastic collision model.

I should also consider whether the weight rolls off after landing: with the plank tilted down at the far end, the weight might slide or roll toward the negative-x edge and fall off entirely instead of resting. I'm adding a lip near that end, sized against the weight's radius and the plank's tilt, to catch it and keep it from rolling away.

Now I'm working out where the ball actually lands after release — computing its velocity from the angular rate and plank geometry at the moment of launch, since at roughly -15° tilt the rotation imparts both a backward and vertical velocity component relative to the pivot.

Estimating about 1.2 m/s horizontal and 4.5 m/s vertical speed gives roughly 0.9s of flight, so the ball travels about 1.1m backward and likely lands near x=-0.2, back on the plank, then rolls down the tilt toward the weight and settles against it within about 6 seconds thanks to rolling friction. I'm adding slight damping to the seesaw hinge to help it settle, and finalizing the plank as a lightweight box with small lip masses and a non-colliding fulcrum visual under the pivot.

I'm deciding to skip defining an explicit keyframe and just rely on default initial positions from body placements, since the hinge angle and tilt are already baked into the setup — simpler and less error-prone. I just need to double check the ball's starting height clears the plank surface with a tiny margin so it doesn't interpenetrate at spawn.

With the hinge limited to -30 to 0 degrees, the weight's mass naturally rotates the plank to rest against the limit, and I'm checking that both ends stay just clear of the floor at the extremes. The impact against the joint limit when the weight drops should be softened by the default solref damping, so there might be a slight bounce but nothing unstable.

Now I'm naming all the geoms and finalizing the file: a floor plane with friction set for decent grip, condim 6 on the ball and weight for full contact dimensionality, plus basic lighting and visuals.

