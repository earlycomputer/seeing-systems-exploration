The seesaw rests tilted at 15°, with its low end on the floor. The 100 g ball sits on that low end against a small lip. The 1 kg weight is released from rest 3 m up, above the raised end.

Rough check: the weight falls about 2.4 m and hits the plank at about 6.8 m/s. Treating that hit as nearly inelastic gives the plank about 6 rad/s. That throws the ball at about 5 m/s, which would carry it well over a metre above its start against the 0.5 m target. I have not run this in MuJoCo, so these numbers are estimates only.

```xml
<mujoco model="seesaw_launch">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 5" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <!-- visual fulcrum stand (non-colliding) -->
    <geom name="fulcrum" type="box" size="0.04 0.12 0.12" pos="0 0 0.12" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>

    <!-- seesaw: pivot at z=0.278, tilted 15 deg so the +x end rests on the floor -->
    <body name="seesaw" pos="0 0 0.278" euler="0 15 0">
      <joint name="pivot" type="hinge" axis="0 1 0" pos="0 0 0" damping="0.01"/>
      <geom name="plank" type="box" size="1.0 0.15 0.02" mass="0.5" rgba="0.7 0.5 0.3 1"/>
      <geom name="lip" type="box" size="0.02 0.15 0.03" pos="0.98 0 0.05" mass="0.02" rgba="0.5 0.3 0.2 1"/>
    </body>

    <!-- 100 g ball resting on the low end against the lip -->
    <body name="ball" pos="0.9042 0 0.0985">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- 1 kg weight dropped from rest above the high end -->
    <body name="weight" pos="-0.86 0 3.0">
      <freejoint name="weight_free"/>
      <geom name="weight" type="sphere" size="0.08" mass="1.0" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm sketching a seesaw design: a 1 kg weight dropped onto one end launches a 0.1 kg ball resting on the other end at least 0.5 m high, with a 2 m plank pivoting at its center, and I'm considering how plank mass and inertia affect the energy transfer.

Working through the impulsive-collision physics: the weight sticking to the plank transfers angular momentum, giving the ball end a tangential speed, so I estimate the ball needs roughly 3.13 m/s to clear 0.5 m, meaning the weight's impact velocity should be around 6.3 m/s—achievable by dropping from about 2 m. To build in margin for energy losses from soft contacts and gravity during rotation, I'll go with a drop height of about 3 m.

I'm reconsidering the setup: a seesaw configuration where one end rests on the ground is cleaner — the ball sits on the low end, the weight drops onto the high end, and the plank rotates to launch the ball. This gives a naturally stable resting state since the ball's weight balances the plank's symmetry. But I realize the ball would simply roll off the tilted low end before any collision happens, so I need to add some kind of stop or lip at that end of the plank to keep the ball in place beforehand.

Working through the geometry now: pivot height at 0.3 m, plank half-length 1.0 m, giving a tilt angle around 17.5 degrees so the low end just touches the floor, with the plank thickness set to 0.04 and a lip added at the low end to hold the ball steady until launch.

I'll put qpos=0 as resting with no keyframe needed, using hinge rotation about y where positive θ tilts the +x end down—so I'll place the ball on the +x low end and the dropped weight on the -x high end, since impact there rotates the plank to raise the +x end. Then I work out the pivot height so the plank's bottom corner just touches the floor at a 15° tilt, computing with sinθ=0.2588 and cosθ=0.966.

Now I'm sizing the lip geometry and ball placement—figuring the lip as a small box above the plank's top surface, sizing the ball radius and mass, and solving for where the ball center sits locally against the lip's inner face, before transforming those local coordinates into world space using the plank's rotation about y.

Plugging in numbers, I get ball center world coordinates around (0.904, 0.098), confirming the ball rests just above the floor with sufficient clearance. I'm now checking whether the lip's far corner dips below the floor to make sure nothing clips.

I'm also thinking about how to support the pivot visually — adding a fulcrum stand beneath it, but worrying it could collide with the plank as it rotates. I decide to make the stand non-colliding (contype/conaffinity set to 0) to avoid interference, since even a narrow stand would cause a slight overlap at small rotation angles.

Now I'm computing the high end's position after rotation, then figuring the drop height and resulting velocity of a weight dropped onto that end, along with the torque arm from the impact point to the pivot. I'm also estimating how far the plank needs to rotate (around 30°) before the high end contacts the floor.

With that, I'm calculating the angular momentum delivered by the falling weight, then working out the plank's effective moment of inertia by combining its own inertia, the weight's contribution, and the ball's contribution at its distance from the pivot, settling on a plank mass of 0.5 kg to get a reasonable angular velocity (~5.9 rad/s) and resulting ball speed (~5.4 m/s), while noting the weight might bounce rather than stick.

Over the roughly 30° rotation, gravity assists the torque from the weight. At the moment of launch, the ball leaves with velocity perpendicular to the plank's angle (~15° from horizontal), giving a vertical component around 5.2 m/s—enough to reach roughly 1.4 m height with margin for losses—while I'm now checking the horizontal component's direction relative to the pivot.

Working through the geometry, since the plank end is rising, the ball's velocity actually points slightly toward -x (toward the pivot side) rather than purely outward, around 1.4 m/s horizontally, meaning over a ~2 s flight it'd drift about 2.8 m inward, potentially near the weight or plank itself—though that's not a major issue since the lip is further out and doesn't constrain the ball's path here.

I'm also considering whether the plank slams hard into the floor on the high side given the weight's momentum, and whether the ball might just roll after landing rather than coming to rest—neither of which seems critical for success. I'm leaning toward skipping an explicit keyframe for the weight's initial position, since default qpos from body placement should work fine and avoids extra complexity.

Now I'm settling on the body euler rotation for the plank tilt, confirming that a +15° rotation about y correctly tips the far end downward, and assigning masses: plank at 0.5, lip at 0.02, with the stand as a static non-colliding support attached to worldbody.

I'm placing the weight body at (-0.86, 0, 3.0) above the plank so it drops onto the surface, widening the plank's half-width to 0.15 to make sure the 0.08-radius ball lands safely within bounds given the tilt. I estimate the fall takes about 0.7s, well within the 6s simulation window, then I add a light source to finish the scene.

