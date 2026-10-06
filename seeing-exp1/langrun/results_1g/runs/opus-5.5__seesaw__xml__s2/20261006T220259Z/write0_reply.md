A 1 kg ball falls 1.8 m onto the raised end of a light 2 m seesaw. A 100 g ball rests against a small lip on the lowered end. The impact swings the plank about 34° until the hinge stop catches it. The 100 g ball then leaves at roughly 5 m/s, which by my estimate should carry it about 1 m above its start of z ≈ 0.14 m. That is only an estimate and hasn't been simulated.

```xml
<mujoco model="seesaw_catapult">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="fulcrum" type="box" pos="0 0 0.15" size="0.05 0.12 0.15" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="seesaw" pos="0 0 0.33" quat="0.98877 0 -0.14944 0">
      <joint name="pivot" type="hinge" axis="0 1 0" limited="true" range="0 0.6" damping="0.01"/>
      <geom name="plank" type="box" size="1.0 0.1 0.03" mass="0.3" solref="0.005 1" friction="1 0.01 0.001" rgba="0.6 0.4 0.2 1"/>
      <geom name="seesaw_lip" type="box" pos="-0.98 0 0.08" size="0.02 0.1 0.05" mass="0.02" solref="0.005 1" rgba="0.5 0.3 0.1 1"/>
    </body>
    <body name="weight" pos="0.80 0 2.4">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.08" mass="1.0" solref="0.005 1" rgba="0.2 0.2 0.8 1"/>
    </body>
    <body name="ball" pos="-0.893 0 0.14">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" solref="0.005 1" friction="1 0.01 0.001" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

```expect
weight touches seesaw
ball touches seesaw
```

---
thinking (summarized):

I'm working through the physics of a seesaw catapult—a pivoting plank with the ball resting on one end, where a dropped weight on the other end needs to launch the ball at least 0.5 m high. I'm considering a lightweight plank design where the falling weight's collision transfers angular momentum to fling the ball upward.

I estimate that dropping the weight from about 1.8 m gives the plank end enough velocity to launch the ball roughly 1.35 m high, giving plenty of margin over the 0.5 m target, and I'm now thinking about how to orient the plank initially so the ball's end starts down.

Since a ball resting on a tilted plank would just roll off, I'm planning to add a small lip or stop at the ball end so it stays put, with the plank pivoted at 0.3 m height and tilted about 17.5° so that end touches the floor. I'll constrain the hinge joint's rotation range to match this angle so the plank naturally stops near floor contact without relying purely on collision.

I'm working out the rotation math: about the y-axis, positive theta tilts the +x end down, so I'll put the ball at the -x end and have the weight land on the +x end, then verify the -x endpoint's z-height when theta is -0.3.

Instead of computing explicit keyframe qpos values for every joint, it's simpler to set the seesaw body's orientation directly with a quaternion tilted -0.3 radians about y, and give the hinge joint a range from 0 to 0.6 radians so it only rotates toward level. That way I don't need an initial keyframe at all—the weight can just drop from height naturally.

Now I'm working out where the ball should rest on the tilted plank, transforming its position from the plank's local frame (accounting for the lip geometry and ball radius) into world coordinates using the rotation matrix for the -0.3 radian tilt.

I also realize there's a geometry concern: when the plank seesaws to launch the ball, the lip near the resting end might actually cause the ball to roll toward center rather than catapult over it, since the tilt direction reverses at launch and the ball gets horizontal velocity from the rotating plank surface.

For the weight, I'm computing where it lands on the plank's opposite end by transforming the local coordinates into world space, giving roughly x=0.854, z=0.605. Dropping from height 2.4 means it falls about 1.71m, hitting at around 5.8 m/s, which seems like a reasonable impact speed for triggering the seesaw given the plank's low mass.

I'm worried about tunneling though—at that impact speed, the default contact softness could let the weight penetrate deeper than the plank's 4cm thickness. I'll thicken the plank slightly and stiffen the solref parameters on the weight and ball geoms to keep the timeconstant above twice the timestep, which should limit penetration to about a centimeter.

Now I'm reworking the geometry with a thinner 0.03 half-thickness plank, recalculating the pivot height and the ball's position in both plank-local and world coordinates to make sure everything lines up with the lip and the weight's target position.

Checking the hinge mechanics: the weight will slam the plank down, with the joint limits (0 to 0.6) stopping rotation appropriately since positive rotation tips the +x end downward toward the floor. I estimate the ball should clear more than a meter of rise, well above the 0.5m threshold needed from its 0.14 starting height.

Given the limited event vocabulary available, I'm settling on simpler descriptions like "weight touches seesaw" and tracking whether the ball eventually touches the floor or plank after being launched, since expressing exact height thresholds isn't straightforward with these event types. The launch trajectory depends on the plank's tilt angle at the moment of contact, which complicates predicting the exact horizontal/vertical velocity split.

I'm also setting up masses for the components—assigning the plank box a moderate mass and the lip a much smaller one—while accounting for friction on the ball as it rolls down the tilted surface.

Setting masses and quaternion rotation for the plank's tilt, and deciding to skip a keyframe to avoid qpos mismatches. Now I'm adding contact solver reference parameters between the weight and the plank.

