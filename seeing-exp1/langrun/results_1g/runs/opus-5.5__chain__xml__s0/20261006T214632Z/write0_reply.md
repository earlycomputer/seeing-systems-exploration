The balls sit 0.3 m apart along x and the cup stands at the far end. Ball1 starts rolling at 3.5 m/s, and ball-to-ball contacts use bouncy explicit pairs so each impact passes most of its speed down the row. All other contacts use the default, almost non-bouncy settings, so ball3 loses energy against the cup walls and settles. A shallow 8° ramp lifts ball3 to the 4 cm front wall of the cup. It drops over that wall into the cup and cannot roll back out, because the inner face of the wall rises above the ball's centre.

```xml
<mujoco model="three_ball_chain_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.8 -1 2" dir="0 0.5 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" contype="0" conaffinity="2" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" contype="2" conaffinity="0" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.3 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" contype="2" conaffinity="0" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.6 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" contype="2" conaffinity="0" rgba="0.2 0.2 0.9 1"/>
    </body>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp_geom" type="box" size="0.18 0.06 0.01" pos="1.1081 0 0.00505" euler="0 -8 0" contype="0" conaffinity="2" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_front" type="box" size="0.006 0.072 0.02" pos="1.291 0 0.02" contype="0" conaffinity="2" rgba="0.3 0.3 0.6 1"/>
      <geom name="cup_base" type="box" size="0.15 0.06 0.002" pos="1.447 0 0.002" contype="0" conaffinity="2" rgba="0.3 0.3 0.6 1"/>
      <geom name="cup_back" type="box" size="0.006 0.072 0.05" pos="1.603 0 0.05" contype="0" conaffinity="2" rgba="0.3 0.3 0.6 1"/>
      <geom name="cup_left" type="box" size="0.162 0.006 0.05" pos="1.447 0.066 0.05" contype="0" conaffinity="2" rgba="0.3 0.3 0.6 0.5"/>
      <geom name="cup_right" type="box" size="0.162 0.006 0.05" pos="1.447 -0.066 0.05" contype="0" conaffinity="2" rgba="0.3 0.3 0.6 0.5"/>
    </body>
  </worldbody>

  <contact>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" solref="0.05 0.05" friction="0.5 0.5 0.005 0.0001 0.0001"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" solref="0.05 0.05" friction="0.5 0.5 0.005 0.0001 0.0001"/>
    <pair name="pair13" geom1="ball1_geom" geom2="ball3_geom" solref="0.05 0.05" friction="0.5 0.5 0.005 0.0001 0.0001"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0  0.3 0 0.03 1 0 0 0  0.6 0 0.03 1 0 0 0" qvel="3.5 0 0 0 116.67 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches ramp
ball3 touches cup
ball3 comes to rest in cup
```

---
thinking (summarized):

I'm thinking through how the ball could actually land in a cup since a flat floor can't have a sunken pocket—maybe I need a ramp or wedge leading up to the cup's rim so the ball rolls up and drops in.

I need to figure out the velocity threshold for the ball to clear the ramp height using rolling-ball energy equations, and also plan how equal-mass balls will transfer momentum down the chain before the final ball makes its climb into the cup.

I'll set up each ball's radius, position spacing, and initial velocity/spin so ball1 slides and rolls realistically into the chain, accounting for friction converting slide velocity to roll velocity at each collision.

Given MuJoCo's default damping, the collision looks closer to perfectly inelastic — both balls end up with roughly v/2 afterward, then friction converts that into rolling speed via the 5/7 and 2/7 split for ball2 and ball1 respectively.

I realize ball1 ends up catching up with ball2 again, which gets messy. To fix this I should tune the contact solref to make the balls bouncier — lowering dampratio or adjusting solref values like "0.005 0.05" so there's actual restitution instead of balls merging velocities, while keeping the timeconstant reasonable relative to the timestep.

I'm working through the chain reaction math: each ball keeps 2/7 of incoming velocity as spin-driven acceleration while passing most forward momentum along, so spacing them roughly 0.3m apart based on slide-to-roll transition distances should keep the collisions sequential and realistic.

Now I'm sizing the cup geometry — thin floor, 0.05 wall height — and checking that launch velocity (v>0.84 m/s accounting for rolling energy loss) is enough to crest the rim, while also considering energy loss at the ramp-to-ground transition angle.

I check that the front wall height exceeds the ball's center height so it can't roll over, but bouncy contacts would make it oscillate forever unless I apply the bouncy solref only on ball-ball pair contacts, leaving ball-wall contacts critically damped so the ball settles naturally against the cup wall.

I'm also considering whether explicit contact pairs override MuJoCo's default dynamically generated geom pairs, since I need the explicit bouncy pairs between balls to take precedence over any default collision handling.

Given the uncertainty, a safer approach is to use contype/conaffinity bitmasks to disable ball-ball dynamic collision entirely, letting only the explicit pair definitions govern ball-ball contact while balls still collide normally with the floor and cup.

Working through the damping ratio to restitution relationship: ζ=0.1 gives e≈0.73, ζ=0.05 gives e≈0.85. I'm figuring out how MuJoCo's solref parameters (timeconst and dampratio) translate into effective stiffness and damping coefficients, since the oscillation frequency scales roughly as 1/(timeconst·dampratio) — so with tc=0.01 and ζ=0.05 I need to check this stays compatible with the simulation timestep.

Realizing ω comes out way too high (period shorter than dt), so I need to pick timeconst and dampratio so the half-period is comfortably larger than dt — working out that tc≈0.06 with dampratio 0.1 gives a reasonable solref of "0.06 0.1", then checking how penetration depth relates to the ball's kinetic energy and effective contact stiffness.

With ζ=0.1, time constant comes out to 0.025s, giving penetration around 7.5mm at v=3, which seems acceptable. I'm checking whether lowering velocity to 2.5 still clears the energy threshold needed to escape the cup's front wall trap—computing the minimum velocity using the lip height versus ball radius suggests v=3 with ramping is the safer choice, so I'll keep that and think about whether the cup floor needs its own geometry or can just rely on the ground plane.

Now I'm working out how to place the ramp as its own tilted body: a box rotated about the y-axis at roughly 8°, sized so its top surface starts flush with the floor at one end and rises to meet the cup's front wall height at the other end. I'm figuring out the exact position and rotation needed so the ramp's surface line connects smoothly from z=0 up to the rim height without worrying about the lower edge dipping below the floor, since that part won't collide anyway.

I'm defining the cup geometry with interior dimensions and wall heights, then working out the ball's flight trajectory after it exits over the front wall—computing exit velocity components and solving for landing time using the height drop and gravity.

After landing, I'm reasoning through the ball's subsequent motion: it rolls back against the rear wall with some inelastic bounce, keeps spinning, and friction gradually redirects and decelerates it until it presses against the back wall at rest. I'm also checking a higher exit speed case (v3=2.5) to see how the trajectory scales.

Then I shift to considering the other balls on the ramp — ball1 and ball2 moving slower, likely rolling back down the ramp toward negative x indefinitely since there's no friction loss, possibly colliding with each other, and I'm checking whether ball2's speed is below the threshold needed to disturb ball3 in the cup while ball1 retains enough energy to matter.

Ball1 at 0.86 m/s is actually above the 0.75 threshold, so it could follow into the cup and strike ball3 after a secondary bounce with ball2. I'm weighing whether to add rolling friction to damp this out, or instead give ball1 a purely sliding initial velocity with no spin so the first collision kills its motion entirely — though that risks it picking up spin before impact unless the ball spacing is small enough that it's still sliding when it hits ball2. For now I'll just accept the imperfection and move forward with the simpler setup.

Tracing out the rest of the collision chain: ball1 reaches the cup around 1.5s and knocks into ball3 sitting at the back wall, pinning it there, while ball2 rolls up the ramp (not quite high enough to crest) and rolls back down, possibly meeting ball1 along the way — not a big concern either way. For contact properties, I'll stick with default friction 1 and specify the five-value pair friction with condim 3.

Now I'm working out the initial keyframe values: 21 qpos entries for three free joints, with ball1 positioned at (0,0,0.03) with identity quaternion, and computing the angular velocity needed for rolling-without-slipping motion in the +x direction (ωy = v/r), making sure I account for whether free-joint angular velocities are expressed in the local or world frame.

I'm also computing the ramp geometry — figuring out the slope direction and normal vectors from the 8° incline angle, extending the slope length to cover the floor transition, and calculating the box center position by offsetting from the top surface along the normal to account for the ramp's half-thickness.

Working out cup geometry: base plate, back wall, and side walls, checking that interior width fits the ball and lines up with the ramp's width so everything fits together without gaps.

I'm setting all balls to the same y-coordinate so collisions stay perfectly aligned. I also need to check expected contact outcomes—ball1 hitting ball2, ball2 hitting ball3, and ball3 settling in the cup—and estimate post-collision velocities using an imperfect restitution coefficient to track how much speed carries through each impact.

But I'm noticing a problem: with higher initial speed, ball1's residual rolling velocity after collision could actually exceed ball3's, meaning ball1 might catch up to ball2 again later. That changes the whole sequence and I need to rework the velocity estimates to account for it.

Let me try increasing the collision damping ratio to around 0.05, which gives a restitution near 0.85 and corresponds to a solref time constant of 0.05 seconds—that should push the balls along more effectively. Using an initial velocity of 3.5 m/s with the corresponding spin should work.

