Three equal balls sit in a row along x. `ball1` starts rolling at 2 m/s, with matching spin so it rolls rather than slides. The ball-to-ball contacts are made fairly bouncy (explicit contact pairs with low damping), so each hit passes most of the momentum forward. `ball3` then rolls up a shallow ramp, over a small lip, and into a walled cup. Inside the cup the soft wall absorbs the impact, and the lip stops it from rolling back out.

These speeds are hand estimates and I haven't run the file. `ball3` should arrive at roughly 0.8–0.9 m/s, against about 0.5 m/s needed to clear the lip.

```xml
<mujoco model="three_ball_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.4 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.5 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.02">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.25 0 0.02">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.5 0 0.02">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="cup" pos="0.85 0 0">
      <geom name="cup_ramp" type="box" size="0.03 0.07 0.005" pos="-0.0742 0 -0.0009" euler="0 -9.09 0" friction="0.5 0.005 0.0001" rgba="0.7 0.5 0.3 1"/>
      <geom name="cup_floor" type="box" size="0.057 0.07 0.001" pos="0.013 0 0.001" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_back" type="box" size="0.005 0.08 0.03" pos="0.075 0 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_side_left" type="box" size="0.09 0.005 0.03" pos="-0.01 0.075 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_side_right" type="box" size="0.09 0.005 0.03" pos="-0.01 -0.075 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="pair_b1_b2" geom1="ball1_geom" geom2="ball2_geom" condim="3" friction="0.5 0.5 0.005 0.0001 0.0001" solref="0.005 0.05"/>
    <pair name="pair_b2_b3" geom1="ball2_geom" geom2="ball3_geom" condim="3" friction="0.5 0.5 0.005 0.0001 0.0001" solref="0.005 0.05"/>
    <pair name="pair_b1_b3" geom1="ball1_geom" geom2="ball3_geom" condim="3" friction="0.5 0.5 0.005 0.0001 0.0001" solref="0.005 0.05"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.02 1 0 0 0  0.25 0 0.02 1 0 0 0  0.5 0 0.02 1 0 0 0" qvel="2 0 0 0 100 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches cup_ramp
ball3 touches cup_back
ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning the scene with three balls in a row that collide and transfer momentum realistically, with spin and rolling physics after impact, plus a cup placed on the floor for a ball to roll into.

Since a flat floor can't have a hole, I'm thinking through how to build the cup: maybe walls on the back and sides with a low entry lip the ball can roll over, so it settles against the back wall without escaping.

Checking the physics: climbing a 5mm lip needs roughly 0.37 m/s, and MuJoCo's default contact damping gives near-zero restitution, so the ball should lose most normal velocity hitting the back wall. But spin matters too—working out that a forward-rolling ball contacting a vertical wall has its contact point moving downward relative to the wall, meaning wall friction pushes the ball upward, which could let it climb rather than just stop.

I'm also realizing ball-to-ball collisions face the same issue: default soft contacts would make them perfectly inelastic, so balls would just merge velocities instead of transferring momentum like billiard balls. I should tune solref values to get more elastic, bouncy collisions so spin and momentum transfer behave realistically between consecutive balls.

For setup, I'll keep radius at 0.02 with default density, and start working out the keyframe positions and velocities for each ball so rolling spin is consistent with initial sliding velocity.

Laying out ball1 at x=0, ball2 at 0.15, ball3 at 0.30, and cup at 0.5, giving ball1 an initial velocity of 1.0 m/s. Since MuJoCo's default friction doesn't impose rolling resistance, I'm calculating the chain of collision transfers: ball2 ends up around 0.71 m/s, ball3 around 0.5 m/s, which is above the 0.37 m/s threshold needed to clear a 5mm cup lip, though the margin is tight — I could reduce the lip to 3mm for more buffer, or bump ball1's initial speed to 1.5 m/s for a bigger safety margin, though that risks a harder impact at the back wall.

I'm thinking through what happens when the ball hits the cup wall with a soft, inelastic contact: the normal velocity gets killed but spin persists, so the ball keeps rubbing against the wall and floor, with floor friction pushing it into the wall and wall friction pushing it upward, gradually decaying the spin until it settles — this seems physically reasonable without needing to add extra rolling friction that could slow the balls prematurely.

Now I'm considering how to model the cup lip: rather than a rotated box ramp, a thin cylinder (4mm radius, centered at z=0.004mm) lying along the y-axis could work as a bump the ball rolls over. Working out the geometry, with a 0.02 ball radius and 0.004 bump radius, the contact occurs when centers are 0.024 apart, giving a vertical offset of 0.016 and horizontal offset of about 0.0179 — placing the contact normal at roughly 42° from horizontal, and in an inelastic collision the ball loses the velocity component along that normal direction.

That seems like too much energy loss though, so I'm weighing a gentler slope instead: a ramp at about 10° that only costs ~1.5% of velocity. But then I realize a plain ramp up to the cup floor doesn't actually trap the ball — without a lip at the top, it would just roll back down the ramp once inside. I need to rethink the cup's shape so there's an actual barrier holding the ball in after it enters.

I'm working out the fall trajectory: dropping 0.05m takes about 0.1s, giving roughly 0.05m horizontal travel, which fits inside the 0.12 cup width before hitting the back wall. But checking ball3's required speed against ball1's suggests the numbers are getting too fast with restitution factored in, so I'm trying a shallower rim instead — around 0.03m with a 0.02 radius ball, needing just over 0.91 m/s to clear it, and reconsidering the ramp-to-rim geometry as essentially rolling over a lip.

Once the ball rolls off the ramp at 0.03m above the floor onto the cup's front wall, it drops to floor level where the 0.03m walls exceed the 0.02m ball radius, meaning it's physically trapped since it can't roll up a vertical face that tall. I'm now considering a gentler approach — a wedge ramp down to a smaller 0.008m lip before dropping inside, with a tall back wall, so a returning ball would strike the lip's inner vertical face instead of escaping.

Since the lip is only 8mm, below the ball's radius, I'm checking whether a fast enough ball could climb it. Working out the geometry, the ball contacts the step edge at a steep angle, and since the collision is inelastic, it loses most of its energy, so it should stay trapped inside rather than climb back out.

Ball1 eventually catches up to ball2 around 0.21, and second collisions could ripple further, but ball3 stays fastest at 0.46 so it should clear into the cup even with trailing balls crowding behind. I'll pick v1=2.0 m/s giving ball3 roughly 0.92 m/s, then work out the sliding-friction transition distance for ball2 before it reaches pure rolling.

Checking ball3's climb over the 8mm bump — working out its speed loss there, then its drop onto the cup floor and collision with the back wall, where most of its normal velocity gets absorbed but its forward spin could translate into wall friction pushing it upward, so I need to bound that force by the available normal force from the floor.

I'm realizing the friction coefficients between ball, floor, and wall combine by taking the max, so setting a single surface to μ=1 dominates everywhere — I should lower the ball and floor friction to 0.5 so the wall-climbing friction stays safely below mg. That tradeoff means slower deceleration and longer sliding distances, so I'm adjusting the spacing between balls to roughly 0.25 m to compensate, and double-checking the back wall's height and bounce behavior won't fling the ball awkwardly. Now I'm setting up the ball-to-ball restitution parameters.

Working through the contact solver settings, since MuJoCo requires the timeconst to be at least twice the timestep or it gets silently clamped — with a 0.002s timestep that means timeconst ≥0.004, so I'm picking 0.005 with a damping ratio of 0.05 to get a restitution coefficient around 0.85, while also accounting for how solref parameters get averaged between two contacting geoms via solmix, which matters for the ball-floor contact too.

Since balls placed exactly at z=r will still have a tiny initial penetration under default solimp settings, there could be a small initial bounce, so I'm considering explicit contact pairs for ball-ball collisions while leaving geom defaults untouched, though I need to double check whether MuJoCo adds explicit pairs on top of the dynamic broadphase collisions for the same geoms or replaces them.

I'll set the pair friction values (sliding, torsional, rolling) and condim 3, along with a contact timeconst of 0.005 relative to a timestep of 0.002, giving roughly half a step for impact resolution.

Looking at the geometry, I'm placing balls of radius 0.02 along the x-axis at 0, 0.25, and 0.5, with the cup positioned around x=0.85. Ball2 slides about 0.18 m before reaching ball3's spacing, so the collision happens while it's still moving, just with reduced effectiveness.

For ball1's keyframe, I need to check whether the angular velocity in qvel for a free joint is expressed in the local body frame or the world frame, since that affects how I set the spin.

Working through the rolling condition, the contact point velocity calculation gives ω_y = v/r = 100 rad/s for pure rolling at 2 m/s with r=0.02, confirming the spin value.

Now I'm designing the cup body at x=0.85 with local coordinates, starting with an entry ramp built from a rotated box rising from the floor to a small height over a short horizontal span, giving it a gentle slope for the ball to climb into the cup.

Calculating the ramp box geometry: with half-thickness 0.005 and half-length 0.04, the slope angle works out to about 9.09°, letting me find the box's center position by offsetting the surface midpoint along the normal direction, then checking the surface's extent along the slope from the lower to upper edge.

Still computing cup geometry...

With the lip at about 6.7mm, that should be fine. The cup body being static without a joint keeps it welded to the world, and the ramp's side walls are positioned outside the ramp width, so everything checks out geometrically. Since all balls stay aligned on the same y-axis, the collisions should remain collinear and symmetric, and checking the timing, ball3 reaches the cup well within a second while the trailing balls carry different residual speeds after their collisions.

Working through the collision speeds, the threshold velocity to climb the 8.7mm lip comes out to roughly 0.49 m/s, so some balls will make it into the cup while slower ones roll back down the frictionless ramp indefinitely in the negative x direction, which shouldn't affect the outcome much. Even if multiple balls crowd into the cup alongside ball3, the inner length of about 0.11m should comfortably fit 2-3 balls.

For ball3's rest state inside the cup, I'm figuring it hits the back wall and its normal velocity gets absorbed while spin keeps pressing it against the wall, with floor friction gradually damping that spin until both velocity and angular velocity settle near zero—well under the 5cm/s rest threshold. I'm setting friction coefficients of 0.5 for the ball geoms, floor, and cup geoms, with default density for mass. Now I'm writing the keyframe definition, specifying qpos values for the three free-jointed balls (21 numbers total) and corresponding qvel entries (18 numbers), noting the cup itself has no joints so it doesn't need keyframe state.

