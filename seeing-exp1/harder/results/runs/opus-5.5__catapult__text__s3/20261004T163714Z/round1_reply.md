**What I expect to happen.** With no keyframe, the run starts at the arm's zero pose with the arm horizontal. The spring torque is 2.0 × 2.62 ≈ 5.2 N·m. The load torque from the arm, cup and ball is about 3.1 N·m, so the arm swings up until it hits its 55° stop.

Over that swing the spring does about 4.1 J of work. Lifting the arm, cup and ball takes about 2.5 J, and damping takes about 0.1 J. The arm's inertia about the hinge is about 0.27 kg·m², so it reaches only about 3.4 rad/s. The ball leaves the cup at about 3.1 m/s, roughly 29° above horizontal, from about (−0.45, 1.2) m.

On that path it reaches the floor near x ≈ 1.4 m. That is short of the bucket's near wall at x ≈ 1.6 m.

There is a second problem. The bucket centre is at x = 2.0 m and the ball starts at x = −0.92 m, so the gap is 2.92 m, not the 3 m the brief asks for. The ball also starts about 0.5 mm into the cup floor.

**The fix**
- Move the bucket to x = 2.08 so its centre is exactly 3 m from the ball's start.
- Raise the spring stiffness to 2.6 N·m/rad. That gives about 5.3 J of spring work, an arm speed of about 4.5 rad/s and a release speed of about 4.2 m/s.
- On that path the ball clears the near wall at a height of about 0.7 m. It drops through the rim near x ≈ 2.08 at a height of about 0.25 m and lands on the bucket floor, which is kept closed by the walls.
- Seat the ball exactly on the cup floor.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.6" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.490">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The spring swings the arm up to its 55 degree stop. The ball leaves at only about 3.1 m/s at about 29 degrees and hits the floor near x = 1.4 m, short of the bucket's near wall at 1.6 m. The bucket centre is also 2.92 m from the ball's start instead of 3 m.", "works": false, "problem": "The spring is too weak, so the ball lands short of the bucket, and the bucket centre is 2.92 m from the ball's start rather than 3 m."}
```

---
thinking (summarized):

Measuring the distance from the ball's starting position to the bucket, I get about 2.92 m against the briefed 3 m — close but slightly off. I'm also reviewing the arm's hinge setup: axis along y at z=0.4, extending toward -x, with a range of 0 to 55 degrees, spring reference at 150 degrees, and stiffness of 2.0 N·m/rad.

Working through the torque balance, positive rotation about y lifts the arm end upward, and spring torque (around 5.24 N·m at q=0) clearly exceeds gravity torque (around 3.1 N·m from the beam, cup, and ball weights), so the arm will launch. I'm checking that this holds across the whole range up to the 55-degree hard stop, where the spring still outpaces gravity, confirming the ball gets thrown. Now I'm computing the energy balance — integrating spring work over the rotation and comparing it to the gravitational potential energy gained by the beam's center of mass as it rises.

Adding up the gravity work for the beam, cup, and ball gives roughly 2.53 J, leaving about 1.57 J of net kinetic energy once damping is accounted for. I'm estimating the total rotational inertia from the beam, cup, ball, and armature contributions to get around 0.262, which gives an angular velocity near 3.46 rad/s and a ball tip speed around 3.2 m/s — now I'm considering whether the ball might separate from the cup before reaching the hard stop.

At the 55° stop, I'm computing the ball's release velocity direction as perpendicular to the arm, splitting it into components (~2.62, 1.84 m/s) to get a launch angle near 35°, then working out the ball's release height and horizontal position using the arm geometry at that angle.

Using the flight equation, I'm solving for when the ball reaches bucket-rim height (z=0.4) versus floor height, checking whether the resulting horizontal distance falls within the bucket's opening at x=1.61 to 2.39 — finding the first case lands short at x≈1.21.

Checking the floor-contact case gives x≈1.39, still short of the bucket's near wall at 1.6, confirming a miss. I'm also verifying the ball stays seated in the cup throughout the swing since the arm accelerates continuously (positive torque), and checking the arm/base geometry clears at q=0. Noticing the bucket center is off from the intended 3.0 distance (currently ~2.92), I'm planning to reposition the bucket to x=2.08 and increase the launch parameters to compensate.

Now I'm working out the energy balance needed: spring work minus damping losses should set a velocity that carries the ball from its launch point at (-0.455, 1.205) at a 35° angle to land around x=2.08, z≈0.3, solving the projectile equations for time of flight and the resulting height at that horizontal distance.

Since this is sensitive to my approximations, I want to redo the moment of inertia calculation more carefully, starting with the beam's contribution about the hinge axis using its mass and half-dimensions.

I'm working through the parallel axis theorem for each component now: the cup floor, cup back wall, and the ball, adding up their individual inertias plus mass times distance-squared terms to get the total rotational inertia about the hinge.

Summing everything, I get total I ≈ 0.2656. Now I'm computing the gravitational work by finding how much each mass rises as the arm swings through 55 degrees, using the rotated coordinate transform to get the height change for each component, starting with the beam (giving about 1.2055 J) and moving into the cup floor's contribution.

For the cup back and ball, I similarly compute the rise terms and multiply by mass times gravity, arriving at a total gravitational work of about 2.482 J. I'm then setting up the spring's potential energy expression using its reference angle and current deflection, getting roughly 2.0524k, and starting to estimate the damping loss by integrating the damping coefficient over angular velocity across the swing.

Checking whether the ball separates cleanly before the arm hits its stop — since net torque stays positive throughout, the arm keeps accelerating and the cup's back wall provides the inward centripetal force needed to hold the ball until the joint limit, at which point the arm halts but the ball continues tangentially and releases upward-forward off the outer wall.

I'm computing the ball's release velocity at the stop angle. Working out the radius and position offset gives a launch direction around 29.4° rather than exactly 55°, since the ball's slight lateral offset shifts the effective tangent angle.

Now I'm aiming for the bucket centered near x=2.08, solving for the angular speed ω needed so the projectile's trajectory lands inside the bucket opening between the rim and floor height, setting up the equation 0=1.205+1.4305-48.61/ω² to solve for ω.

Solving gives ω²≈20.38 so ω≈4.51, with kinetic energy of roughly 2.7 J, which combined with the spring's potential energy requirement and damping losses suggests a spring constant around k=2.6. I'm now checking sensitivity, estimating how much the landing position shifts within the bucket's acceptable range, and considering what happens physically when the arm hits its joint limit stop and whether the ball separates cleanly at that point.

Checking that the ball doesn't clip the back wall of the cup — since the ball exits moving in the local +z direction away from the cup floor, while the wall only extends to z=0.12, it looks like the ball's trajectory clears that wall given its radius and release height.

Projecting gravity onto the arm's local axes at the moment of release, I find gravity's local-x component actually pushes the ball toward the hinge, away from the back wall — good, that confirms no collision there.

Now I need to check whether the arm and base geoms could collide near the hinge region, since the beam's bottom edge sits close to the base top at q=0. This raises the question of whether MuJoCo's parent-child contact filtering even applies when one of the bodies is the worldbody — I need to verify whether that exclusion still holds for world-attached geoms.

I'm also checking the ball-cup contact geometry: the ball's initial position overlaps slightly with the cup floor by half a millimeter, so I should nudge the ball's starting height up a bit to avoid initial penetration. The beam and cup floor don't conflict since the ball sits above both. I'm also considering whether the ball's trajectory clears the bucket wall near x=1.69 as it flies over.

Running the numbers, the ball's height at x=1.69 comes out to about 0.707, well above the wall, and it continues on its arc to land around x=2.15 on the bucket floor where it will bounce slightly before settling, since the contact solver parameters are set for near-critical damping. I'm settling on k=2.6 for the energy calculation, which gives a reasonable angular velocity of about 4.54 for the launch mechanism.

The bucket itself is just a static world-body child with no joint, so its mass doesn't matter. I'll finalize the corrected file with bucket position at 2.08, stiffness 2.6, and ball z at 0.490.

