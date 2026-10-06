The design is a light 2 m plank on a hinge. Its joint range is 0° to 34°, starting tilted 17° with the ball end resting low against a small end stop. The 1 kg weight falls 1 m onto the raised end. That swings the plank until it hits the opposite joint limit, and the abrupt stop flings the 100 g ball upward.

I haven't run this. By a hand estimate, the plank's swing alone lifts the ball about 0.42 m, and the throw should add roughly another 0.8 m, giving a peak around 1.2 m above the start against the 0.5 m needed. Rolling friction (`condim="6"`) is there so both balls should settle once they land.

```xml
<mujoco model="seesaw_catapult">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="stand" type="box" pos="0 0 0.16" size="0.03 0.15 0.16" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>

    <body name="seesaw" pos="0 0 0.35" euler="0 -17 0">
      <joint name="pivot" type="hinge" axis="0 1 0" pos="0 0 0" range="0 34" limited="true" damping="0"/>
      <geom name="plank" type="box" pos="0 0 0" size="1.0 0.1 0.02" mass="0.5" rgba="0.7 0.5 0.3 1"/>
      <geom name="ball_stop" type="box" pos="-0.98 0 0.06" size="0.02 0.1 0.04" mass="0.05" rgba="0.5 0.3 0.2 1"/>
      <geom name="weight_stop" type="box" pos="0.98 0 0.08" size="0.02 0.1 0.06" mass="0.05" rgba="0.5 0.3 0.2 1"/>
    </body>

    <body name="ball" pos="-0.893 0 0.141">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" condim="6" friction="0.8 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="weight" pos="0.807 0 1.67">
      <freejoint name="weight_free"/>
      <geom name="weight" type="sphere" size="0.05" mass="1" condim="6" friction="0.8 0.005 0.005" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm thinking through a seesaw catapult design: a 2 m plank pivoting at the center, with the ball resting on the lowered end and the 1 kg weight dropped onto the raised end, causing it to flip and launch the ball upward.

Working through the physics, I'm estimating the weight's impact velocity from drop height, computing the plank's moment of inertia along with the ball and weight contributions, and using angular momentum conservation to find the resulting rotation speed. I'm trying to figure out whether the ball's resulting launch velocity, combined with the rise from the plank's tilt, gets it at least 50 cm above its starting height.

I'm also considering that the ball could roll off the tilted plank before it gets launched, so I'll add a stopper block at the low end to keep it in place until impact.

With a 6-second sim, I want the ball to actually settle rather than roll indefinitely on the floor, so I'll add rolling friction to the ball and floor contacts, maybe friction values like "1 0.005 0.01" with condim 6, even though the brief doesn't strictly require "at rest" behavior.

I should also check that the weight doesn't just roll off the plank after impact — it lands on the raised end and should settle there too, so giving it similar rolling friction makes sense for stability.

Now I'm working out the plank's initial orientation: it's hinged at the pivot along the y-axis, and I need the ball end tilted down to the floor while the weight end stays up. Rotating about y by a negative angle achieves that, so I'll set the body's initial pose accordingly rather than fiddling with keyframe qpos directly.

I'm also figuring out the plank dimensions (thickness 0.04, half-length 1.0) and deciding to use the hinge's range limits instead of relying on messy floor contact to stop the low end from sinking further.

Good, that confirms no floor contact at the limit angle. Now I need to work out the sign convention for the hinge rotation so the ball's end starts down—since positive rotation about y lowers the +x side, I want the initial angle to be -17° (about -0.297 rad) to put the ball side at -x down.

Maybe simpler to tilt the body itself using euler angles so the plank starts at the proper angle without needing explicit keyframe qpos, letting the hinge range just go from 0 to 34 degrees. The ball, being a separate freejoint body in world coordinates, doesn't need a keyframe either since gravity will naturally drop it from rest.

Good, gravity pulls the ball toward negative qpos, against the lower limit, so the setup is stable. Now I'm working out the plank's local geometry: the box top surface sits at z=0.02, with a stopper block near the -x end to cradle the ball, and I'm placing the ball's center so it rests against the stopper's inner face while sitting just above the plank surface, accounting for the ball's radius.

I'm deciding against adding an inner lip stopper, since that would turn the cradle into a cup and could deflect the ball's launch trajectory — better to keep it simple so the ball is flung cleanly at the moment the plank's rotation halts at its extreme angle, with the launch direction determined by the velocity of the -x end point at that instant.

The ball might just land back on the plank and roll off, which is messy but acceptable. I should check the stopper doesn't block this perpendicular launch, and now I'm converting the ball's body-frame position into world coordinates using the -17° rotation about y to find where it actually lands.

Now I'm sizing the weight to drop onto the +x end of the plank — using a 1 kg steel ball of radius 0.05, computing the top surface point in world coordinates (around x=0.807, z=0.618), and setting its drop height so it starts about 1m above that point, landing around z≈1.67.

Working through the impact dynamics: the weight hits at ~4.43 m/s, giving angular momentum about the pivot of roughly 3.58 kg·m²/s. I'm estimating the moment of inertia contributions from the plank (~0.167), the weight (~0.76), and the ball (~0.085), totaling about 1.01, which gives an initial angular velocity near 3.5 rad/s. Then factoring in gravity torques (weight ~7.8 N·m vs ball ~0.9 N·m), I'm getting a net angular acceleration around 6.9 N·m of imbalance divided by the inertia.

Continuing through the rotation over 0.59 rad, angular velocity climbs to about 4.5 rad/s, so the ball at 0.92 m radius reaches roughly 4.1 m/s, with a vertical component near 3.95 m/s giving extra rise of about 0.79 m. Adding the plank's own lift, the ball rises roughly 0.42 m from the plank geometry, totaling about 1.2 m above its start — plenty of margin. Now I'm checking whether the ball stays in contact with the plank during this accelerated swing by comparing the centripetal requirement (~18 m/s² inward) against gravity's component along the plank.

The ball would tend to slide outward, but the stopper at the far end holds it in place, so contact is maintained as the plank pushes it through the angular acceleration. I'm also considering the joint limit behavior — since it's a soft constraint with a short timescale (~20ms), the plank should decelerate abruptly enough that the ball separates cleanly once the limit is reached, which is the desired behavior.

Estimating flight time around 1 second, the ball should land roughly 0.45m along the tilted plank, roll down toward the stopper and weight, and settle there even if it bounces slightly since rolling friction will stop it. I'll also set condim="6" on the ball geom to ensure proper rolling friction at the contact.

Checking the rolling friction math: with coefficient 0.005, deceleration works out to about 0.88 m/s², enough to stop the ball within a couple seconds on flat ground. On the 17° plank though, 0.005/0.04 gives a ratio below tan(17°), meaning the ball won't be held stationary purely by rolling resistance on that slope—it'll keep moving until it hits the stopper or weight.

I'm now fixing mass values since defaults make the plank way too heavy (16 kg from default box density), so I need explicit mass settings: plank around 0.5 kg, stoppers 0.05 kg each, ball 0.1 kg, weight 1 kg. Also adding a visual support structure under the pivot point, non-colliding, extending up to the pivot height.

I'm checking that the weight drops cleanly onto the inclined plank without interfering with the ball's position, and verifying the floor plane, lighting, timestep (0.002), and that the ball's launch height (~0.64m) matches the energy available from the weight drop.

The impact rotates the plank away from its lower limit correctly, and the ball interacts fine with the plank and stopper box geometry. I'll make sure every body, geom, and joint gets a unique name on its own line, skip the keyframe since it's optional, and finish defining the stand geometry with proper contype/conaffinity settings to avoid unwanted collisions.

Now I'm checking the pivot hinge range and axis, making sure the compiler angle unit is set explicitly to degrees, and confirming the plank's mass and inertia near the hinge are reasonable before writing out the full XML.

