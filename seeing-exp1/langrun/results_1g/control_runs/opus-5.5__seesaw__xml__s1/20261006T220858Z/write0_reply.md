The weight falls from 3 m onto the raised end of a light 2 m plank. The hinge limit then stops the plank abruptly, and the 100 g ball is flung upward from a lipped cup at the far end. By rough hand estimates, the ball leaves at about 4.5 m/s and rises well over a metre. I haven't run this file in MuJoCo, so these numbers have not been checked in simulation.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 5" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1" friction="1 0.005 0.005"/>

    <!-- visual-only fulcrum -->
    <geom name="fulcrum" type="box" pos="0 0 0.19" size="0.05 0.12 0.19" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>

    <!-- seesaw: pivot at z=0.4, ball end at +x, weight lands on -x end -->
    <body name="seesaw" pos="0 0 0.4">
      <joint name="pivot" type="hinge" axis="0 1 0" limited="true" range="-0.3 0.3" damping="0.02"/>
      <geom name="plank" type="box" size="1.0 0.1 0.01" mass="0.5" rgba="0.6 0.4 0.2 1"/>
      <geom name="lip" type="box" pos="0.99 0 0.04" size="0.01 0.1 0.03" mass="0.02" rgba="0.5 0.3 0.1 1"/>
    </body>

    <!-- 1 kg dropped weight -->
    <body name="weight" pos="-0.85 0 3.0">
      <freejoint name="weight_free"/>
      <geom name="weight_geom" type="sphere" size="0.06" mass="1" condim="6" friction="1 0.005 0.005" rgba="0.2 0.2 0.8 1"/>
    </body>

    <!-- 100 g thrown ball, resting on the low end against the lip -->
    <body name="ball" pos="0.9128 0 0.16998">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="1 0.005 0.005" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.3  -0.85 0 3.0 1 0 0 0  0.9128 0 0.16998 1 0 0 0" qvel="0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the seesaw catapult setup: a 1 kg weight drops on one end to launch a 100 g ball from the other end at least 50 cm above its starting height. I need to figure out what "at rest" means for the ball — whether it refers to its initial resting state before launch or some final settling condition, since the threshold is moving slower than 5 cm/s.

I'm also thinking about damping so everything settles within the 6-second simulation window, since a ball on a flat plane could roll indefinitely without rolling friction — so I'll need contact properties that introduce rolling resistance. Now I'm working through the physics: plank length 2 m with a pivot at center, calculating moment of inertia for a lightweight plank plus the ball's contribution, then using conservation of angular momentum from an inelastic collision to estimate the ball's launch velocity from the weight's drop height.

Raising the drop height to 2 m gives roughly 6.26 m/s impact velocity, translating to about 4.95 m/s for the ball and a launch height near 1.25 m — comfortably within range. I'm also working out the seesaw's rotation limits given a 0.3 m pivot height and 1 m half-length, giving about ±17° of travel, and tracing through the sequence: ball-end starts low, weight drops on the raised end, the plank swings until the weight-end hits the floor and stops, launching the ball upward at roughly the moment the plank's motion is arrested.

Now I realize the ball would simply roll off a plank tilted at -17° unless something holds it in place, so I need a stopper or lip at the ball's end to keep it resting against the slope until launch. I'm figuring out the lip's dimensions relative to the ball's radius and how to position everything so the ball starts in a stable resting state at t=0 rather than relying on the simulation to settle it.

Actually, using a hinge joint with range limits seems cleaner than floor contact for the plank — limiting rotation to roughly ±0.3 rad means gravity on the heavier ball side naturally holds the plank at its limit, and I'm checking that the plank's far end still clears the floor given the pivot height and half-length.

I'm working out the body ordering and rotation math: with the hinge axis along y, choosing the ball end at +x means it needs a positive tilt angle to rest low, while the weight dropping on the opposite end flips the rotation to raise the ball side. I'm also sketching out the qpos ordering across the seesaw, weight, and ball bodies, and defining the plank geometry as a thin box.

Now I'm adding a small lip geometry at the +x end of the plank to keep the ball from rolling off, and figuring out the ball's mass and radius so it sits properly on top of the plank against that lip, resting at the right height in the body frame.

Then I'm converting those body-frame coordinates to world coordinates by applying the hinge rotation about the y-axis at θ=0.3 radians, computing the cosine and sine values and plugging them into the rotation transform to get the ball's actual world x and z position, while double-checking the sign convention for MuJoCo's y-axis rotation matrix.

I note the ball may slightly penetrate the surface at this position, but that's fine since contact dynamics will resolve it quickly, and the keyframe sets velocity to zero so it starts at rest. Then I'm working out where the weight should be dropped above the opposite end of the plank—placing it near x=-0.9 in body frame, converting that to world coordinates (around x=-0.86, z=0.675), and figuring the weight should fall from z=2.5, giving roughly a 1.76 drop height.

Working through the impact: drop speed around 5.9 m/s hits the tilted plank, with the normal direction giving an effective velocity component of about 5.6, which drives the angular impulse on the plank. After impact the plank rotates back toward negative tilt, reversing the slope so the weight slides off toward the far end—I'm deciding to keep the drop position at -0.85 despite the tradeoff between contact reliability and lever arm length.

The plank rotates roughly 0.6 rad over about 0.12s, and as it swings the ball stays pressed against the lip due to centrifugal effect while being pushed outward. At the limit stop, the plank halts abruptly and the ball launches at about 4.7 m/s, with its velocity direction set by the plank's final angle—giving a vertical component near 4.5 m/s and an estimated rise of roughly 1.03 m.

I'm checking margins: starting from a drop height around 0.17-3.0 m gives a range of fall velocities (4.5 to 6.7 m/s), and even with 50% energy loss from soft contact there's plenty of margin for the ball to clear whatever height is needed. I don't think the exact drop height matters much as long as it's in this range, and I'm not worried about the ball ejecting slightly early since it'll still get launched upward regardless. The horizontal velocity component works out to about -1.4 m/s given the plank's launch angle.

Projecting the trajectory, the ball should land roughly 0.5 m from the pivot after about a second of flight, possibly striking the plank or weight on the way down, but that's acceptable since I mainly need it to settle at rest by around 6 seconds. To stop the ball from rolling indefinitely after landing, I'm considering adding rolling friction to its geom -- something like a small rolling friction coefficient (around 0.005) that would produce a gentle deceleration proportional to gravity and inversely related to the ball's radius.

Working through the math, a rolling friction coefficient of 0.005 gives roughly 0.87 m/s² deceleration, so a ball moving at 1.4 m/s would stop in about 1.6 seconds -- good enough. I'll apply condim 6 and matching rolling friction to both the ball and the weight body, add a little hinge damping on the seesaw to help it settle, and set up the floor plane with a light source, naming the relevant bodies and geoms for the ball, weight, and seesaw plank.

Now I'm checking whether a fulcrum box under the pivot would clip through the plank as it tilts -- computing the plank's lowest point near the pivot at a small rotation angle and comparing it to the fulcrum's top height, finding they overlap slightly, so I need to lower the fulcrum's top surface to avoid collision.

I'll just disable collision on the fulcrum entirely by setting contype and conaffinity to 0, which is simpler than tuning geometry. Then I'm working out a keyframe for the initial scene: positioning the plank at its rotational limit and placing the weight so it sits exactly touching the lip's inner face, checking the ball-to-lip distance equals the ball radius for a tangent contact, and confirming the plank starts right at the joint limit so gravity will begin acting on it immediately.

The weight's position at the positive-x end creates a torque that rotates the plank further into its limit, which is the direction I want. I'm also checking timing details like how long the weight takes to fall and settle, making sure the contact solver's reference timestep won't let the plank overshoot its limit excessively before the ball launches off.

Now I'm writing out the final XML, naming the hinge joint, setting sizes, and skipping unnecessary attributes like armature.

