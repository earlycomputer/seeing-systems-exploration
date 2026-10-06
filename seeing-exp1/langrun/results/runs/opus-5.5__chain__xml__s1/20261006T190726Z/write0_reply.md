The balls sit in a line along +x. `ball1` starts already rolling at 1.5 m/s. The cup lies on its side, fixed to the floor, with its mouth facing the balls and a shallow ramp up to the 4 mm lip so `ball3` can roll inside and come to rest against the back wall.

To keep the knock-ons distinct, ball-ball contacts are springy and low-friction. The floor and the cup have higher contact priority, so they keep normal friction and damping. Even if the collisions turn out less elastic than intended, `ball3` stays at the front of the group and still gets pushed into the cup. I haven't run this, so the speeds and outcome are estimates.

```xml
<mujoco model="three_balls_into_cup">
  <option timestep="0.002"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -0.5 2" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.85 0.8 1" friction="0.8 0.005 0.0001" priority="1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" rgba="0.9 0.2 0.2 1" friction="0.05 0.005 0.0001" solref="0.005 0.05"/>
    </body>

    <body name="ball2" pos="0.25 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" rgba="0.2 0.4 0.9 1" friction="0.05 0.005 0.0001" solref="0.005 0.05"/>
    </body>

    <body name="ball3" pos="0.5 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" rgba="0.95 0.8 0.1 1" friction="0.05 0.005 0.0001" solref="0.005 0.05"/>
    </body>

    <!-- Cup lying on its side, mouth facing -x, axis at height 0.054, fixed to the world.
         Inner radius 0.05, wall thickness 0.004, interior spans x = 0.85 .. 0.97. -->
    <body name="cup" pos="0.91 0 0.054">
      <geom name="cup_wall_000" type="box" size="0.06 0.0145 0.002" pos="0 0 0.052" euler="0 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_030" type="box" size="0.06 0.0145 0.002" pos="0 -0.026 0.04503" euler="30 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_060" type="box" size="0.06 0.0145 0.002" pos="0 -0.04503 0.026" euler="60 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_090" type="box" size="0.06 0.0145 0.002" pos="0 -0.052 0" euler="90 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_120" type="box" size="0.06 0.0145 0.002" pos="0 -0.04503 -0.026" euler="120 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_150" type="box" size="0.06 0.0145 0.002" pos="0 -0.026 -0.04503" euler="150 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_180" type="box" size="0.06 0.0145 0.002" pos="0 0 -0.052" euler="180 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_210" type="box" size="0.06 0.0145 0.002" pos="0 0.026 -0.04503" euler="210 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_240" type="box" size="0.06 0.0145 0.002" pos="0 0.04503 -0.026" euler="240 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_270" type="box" size="0.06 0.0145 0.002" pos="0 0.052 0" euler="270 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_300" type="box" size="0.06 0.0145 0.002" pos="0 0.04503 0.026" euler="300 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_wall_330" type="box" size="0.06 0.0145 0.002" pos="0 0.026 0.04503" euler="330 0 0" rgba="0.6 0.3 0.7 1" priority="1"/>
      <geom name="cup_bottom" type="cylinder" size="0.054 0.003" pos="0.063 0 0" euler="0 90 0" rgba="0.5 0.25 0.6 1" priority="1"/>
      <!-- shallow lip ramp: top surface rises from z=0 at x=0.79 to z=0.004 at the mouth (x=0.85) -->
      <geom name="cup_lip_ramp" type="box" size="0.0301 0.025 0.002" pos="-0.0899 0 -0.054" euler="0 -3.81 0" rgba="0.5 0.25 0.6 1" priority="1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0  0.25 0 0.03 1 0 0 0  0.5 0 0.03 1 0 0 0" qvel="1.5 0 0 0 50 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with three balls in a row, where the first rolls into the second, which knocks into the third, which finally rolls into a cup, while thinking through how MuJoCo's default soft-contact physics will handle the sequential collisions and momentum transfer realistically.

Spin complicates things too—after collision ball1 would regain some forward velocity due to friction converting spin to rolling, potentially chasing ball2 again, which is messy but probably acceptable since only ball3 needs to land in the cup. I'm weighing whether to set ball1's initial keyframe velocity as pure sliding (no spin) versus rolling, and now turning to how the cup geometry needs to be shaped so a ball rolling along the floor can actually enter it.

Since the floor is flat and can't have a hole, I need the cup itself to provide the entry point—maybe tipped on its side with the opening facing the oncoming ball, or with a ramp leading up to the rim. A side-lying cup means the inside surface is curved, so I'm thinking through how that curvature affects the ball's path into it.

Sinking the cup below the floor won't work since the floor plane is solid everywhere. So instead I'll design the cup as an open-front receptacle: a thin low floor plate the ball can roll onto, with tall back and side walls to catch it, and no front lip so the ball enters easily but might risk rolling back out if damping isn't enough.

For collisions, I'm weighing whether bounciness even matters here — maybe default inelastic contact is simpler. With an inelastic collision, ball1 transfers momentum to ball2, but ball1 keeps its spin while ball2 doesn't, so ball1 keeps pushing ball2 forward via friction until they reach ball3 and the chain continues.

But the phrase "first rolled into second, second rolls into third" implies sequential bumps rather than a single merged group, so I should space the balls out and give contacts some restitution. I'm considering solref parameters that produce a damping ratio around 0.05–0.1, giving a restitution coefficient of roughly 0.73–0.85, while being careful that this doesn't cause jitter on the resting floor contacts.

I think using contact priority solves this cleanly: give the floor and cup higher priority with default damped solref, so only ball-ball contacts use the bouncier parameters. For timeconst, I'll keep it near twice the timestep (0.004–0.005s with dt=0.002s) to stay within MuJoCo's recommended range, accepting that the implicit integrator will numerically damp some of the restitution anyway.

I'm also considering friction: since spinning balls create tangential surface velocity at contact, I could lower ball-ball friction to something like 0.05 while keeping floor/cup friction at 1, using priority so floor-ball contacts use the floor's higher friction. Rolling friction stays at zero by default, so balls will keep rolling unless something stops them.

Now I'm working out positions and masses: with radius 0.03 and default density, each ball comes out to about 0.113 kg, placed along the x-axis at intervals of 0.3 toward a cup near x=1.0, each sitting at z=0.03 on the floor. I'm setting the initial velocity for the first ball to roll forward at 1 m/s, which means computing the matching angular velocity (v/r ≈ 33.33 rad/s) so the contact point has zero slip, working through the cross product to get the sign right for rolling in the +x direction.

Then I'm figuring out the collision dynamics: ball1 hitting ball2 with a restitution around 0.8 leaves ball1 at roughly 0.1 m/s and ball2 at 0.9 m/s sliding without spin, after which friction brings ball2 to a rolling speed of about 0.64 m/s, and I'm computing the slide time using the deceleration from friction to find when pure rolling kicks in.

Ball1 ends up rolling at about 0.36 m/s after transitioning from its initial sliding speed. Then ball2 catches up to ball3 across the gap and transfers momentum again, leaving ball3 sliding at roughly 0.58 m/s before settling into rolling around 0.41 m/s, while I track ball2's remaining velocity afterward.

I'm now considering whether multiple balls might end up entering the cup together, or whether the setup should be simplified so only the third ball clearly enters it, which might mean giving ball1 no initial spin to keep things cleaner.

Checking the numbers: over that short gap, ball1 only picks up minor spin before contact, so it's not a perfectly clean stun but close enough. Really the actual requirement is just that ball3 lands in the cup, so minor residual motion from the followers is fine as long as they don't knock ball3 back out—I should focus there instead of over-engineering the stun shot.

For the cup, I'm rethinking the geometry: rather than an open-front receptacle, I want something that reads as an actual cup lying on its side, built from a back disc plus a ring of boxes forming the walls, with a small lip height for the ball to roll over. I need to make sure the cup itself stays fixed and doesn't roll away on contact.

I'll just weld the cup to the world as a static body rather than giving it a joint, which keeps things simple and avoids it tumbling around. Then for the walls, I'm constructing a ring of around 12 boxes arranged radially around the cup's axis to approximate a cylindrical interior, sizing each segment's length, width, and radial thickness so they fit together into a believable cup shape.

Placing each segment...

With θ=180 ensuring the bottom is flat, I'm working out the ring dimensions: inner radius 0.05, wall thickness 0.006, axis height so the bottom outer face sits at z=0, and tangential half-widths sized to overlap slightly at the outer edge with an axial half-length of 0.07.

Now I'm placing the back disk by rotating a cylinder so its axis points along x, sizing it to match the tube radius, and positioning it at the back end. Then I'm checking whether a rolling ball with r=0.03 moving at 0.4 m/s has enough kinetic energy to climb a 6mm lip, comparing the rolling energy term against the potential energy needed and noting that a real step impact also dissipates energy on collision with the edge.

Accounting for the inelastic edge impact (angular momentum conserved about the edge), the ball's velocity drops to about 0.857 of its original value, which still leaves it marginally above the threshold to climb the lip. To make this more reliable, I'm considering adding a small tilted ramp in front of the lip as part of the cup geometry, rising from floor level to the lip height over a short run, and I'm working out the box dimensions needed for that ramp.

Since the cup is a child of the world body with no joint, it's effectively welded and excluded from collision with the floor, so the ramp's geometry extending slightly below floor level isn't a problem. I'm also considering thinning the wall to around 3-4mm combined with the ramp, and bumping up the ball launch speeds to ensure they clear the lip reliably.

I'll keep the cup's axial length at 0.12 since ball3 stays in regardless. With the 12-gon interior, the flat bottom strip is narrow enough that a centered ball rests on it cleanly, and since all balls stay aligned at y=0 there's no lateral drift to worry about—just straight-line collisions along x.

For followers, ball2 will eventually catch up to ball3 pinned against the cup's back wall and bounce back from the ball-ball restitution. I should confirm MuJoCo's geom priority attribute exists so the higher-priority geom's friction and solver parameters dominate contacts, and think through reasonable solref/solimp/dampratio values for a softish ball contact.

Checking positions: ball1 at x=0, ball2 at x=0.25, ball3 at x=0.5, with the cup's front lip at x=0.85, ramp spanning 0.79-0.85, interior from 0.85-0.97, and back disk at 0.97-0.976. I'm also noting that friction during ball-ball collisions stays low enough not to meaningfully interfere with spin, and starting to work out timing with ball1 launched at 1.5 m/s.

I'm estimating travel times for each ball to reach the cup given their gaps and rolling/sliding transitions, finding everything should settle within roughly 1 second well inside a 6 second window. I'm also sanity-checking with a lower restitution value (e=0.5) to confirm the balls would still arrive in reasonable order even in that worse case.

Now I'm working out the ramp geometry for lip climbing at the cup's edge, calculating the small wall thickness, ramp angle (around 3.8°), and placement of a box to bridge the floor to the cup's inner lip height.

Checking continuity: the ramp's top edge meets the cup bottom segment's inner face properly at x=0.85, z=0.004, and the ramp width/half-width of 0.025 looks right. Now verifying the ball's position at the front opening and lower-side wall segments—on the flat bottom the ball center sits at z=0.034 while the axis is at 0.054, about 0.02 below axis, which seems consistent with the geometry.

Calculating the distance from the ball center to the θ=150 wall plane: after projecting the ball's offset onto the wall normal, the distance comes out to roughly 0.0327, which is greater than the ball radius of 0.03, so there's no contact there and the ball rests cleanly on the bottom. Now I'm working out the box segment dimensions—axial half-size 0.06, tangential half-width about 0.0145 based on the outer radius and 15-degree angle, and radial half-thickness 0.002.

Next I'm computing the absolute positions of each of the twelve segments around the cup by rotating the relative offset (0, -0.052 sinθ, 0.052 cosθ) through each 30-degree increment, listing out coordinates for θ=0 through 330, then starting to work out the position of the back disk relative to the axis center.

Setting contact priorities and friction for cup, ball, and floor geoms, then defining the keyframe with three freejoint balls positioned at x=0, 0.25, 0.5 and giving the first ball some rolling velocity and spin to start the simulation moving.

Thinking through the physics: the ball starting right at floor contact height will settle naturally, rolling without extra friction until it eventually collides with later balls or the cup and comes to rest. Checking that soft-contact damping handles the collisions stably, including a ball hitting the back wall of the cup, then moving on to lighting and visual details with default densities for the balls.

