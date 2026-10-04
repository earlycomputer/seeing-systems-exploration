The pendulum is released from 0.6 rad and strikes the ball at the bottom of its arc. The ball rolls 1 m along +x into a walled cup centred at (1, 0). The floor is an unbroken plane, so the cup's mouth faces the incoming ball. The ball should stop against the back wall: its forward spin keeps it pressed there. I haven't run this, so the timings and speeds below are estimates.

- **Release:** The pendulum is 0.4 m long and starts at 0.6 rad. That should give a bob speed of about 1.2 m/s at the bottom.
- **Strike:** At the bottom of the swing, the bob centre is level with the ball centre (z = 0.03) and just touching it. The push should be horizontal.
- **Ball speed:** The bob is 0.2 kg and the ball 0.05 kg. The ball should leave at roughly 1.2–1.6 m/s, then settle to about 0.9–1.1 m/s once it is rolling.
- **Arrival:** It should reach the cup in about a second, well within the 6 s run.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- cosmetic support frame for the pendulum (non-colliding) -->
    <geom name="support_post" type="cylinder" fromto="-0.055 0.2 0 -0.055 0.2 0.45" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="support_beam" type="cylinder" fromto="-0.055 0.2 0.45 -0.055 -0.03 0.45" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>

    <!-- pendulum: pivot 0.4 m above the ball centre, bob just touching the ball when vertical -->
    <body name="pendulum" pos="-0.055 0 0.43">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.002"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.375" size="0.008" mass="0.02" rgba="0.3 0.3 0.7 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.4" size="0.025" mass="0.2" rgba="0.2 0.2 0.8 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" rgba="0.9 0.2 0.2 1"/>
    </body>

    <!-- cup centred 1 m from the ball start, mouth facing the ball (-x side) -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_back" type="box" pos="0.09 0 0.05" size="0.01 0.1 0.05" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_side_left" type="box" pos="0 0.09 0.05" size="0.08 0.01 0.05" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_side_right" type="box" pos="0 -0.09 0.05" size="0.08 0.01 0.05" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_front_left" type="box" pos="-0.09 0.0725 0.05" size="0.01 0.0275 0.05" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_front_right" type="box" pos="-0.09 -0.0725 0.05" size="0.01 0.0275 0.05" rgba="0.2 0.7 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- pendulum raised 0.6 rad back (bob toward -x); ball at rest -->
    <key name="start" qpos="0.6 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics of the scene: a ball resting on the floor needs to roll a meter into a cup, but I'm realizing a cup with raised walls would block the ball from entering unless the walls are low enough or there's some opening for it to roll in.

So maybe the cup should be shaped like a U open toward the ball, with a back wall to stop its motion—but then I need to worry about it bouncing back out, since MuJoCo contacts have some restitution even if small. The ball's arriving speed and the wall's damping properties will determine whether it settles inside or rebounds out.

I'm thinking through how a rolling ball interacts with a wall: the linear velocity halts on impact but angular momentum keeps spinning it, and floor friction will convert that spin into continued pressure against the back wall, so it should stay put. I'm now considering whether an open-front cup design is sufficient, or whether I need a more enclosed shape—possibly a raised ring with a ramp leading the ball up and over into a shallow basin—to make it feel more like an actual cup rather than just a three-walled pocket.

Weighing the ramp idea against energy requirements, I calculate the ball needs enough speed to roll up the incline accounting for rotational kinetic energy, but this introduces too much uncertainty without being able to simulate it directly. I'll stick with the simpler U-shaped wall design since it's more robust and predictable, just framing it as a cup with its mouth oriented toward the pendulum's swing.

Now I'm working out the pendulum mechanics: hinge axis placement, bob position so it strikes the ball at the right height, and ensuring the ball travels straight along the line toward the cup's center once struck.

For the collision itself, I'm thinking the ball is lighter (0.05 kg) than the bob (0.2 kg), and with MuJoCo's default soft contact giving low restitution, the heavier pendulum effectively pushes the ball forward rather than bouncing back — so the ball launches roughly at the bob's bottom speed while the pendulum continues swinging past vertical and upward.

After launch, the ball initially slides before friction brings it to rolling speed (5/7 of initial), but since condim=3 gives no rolling resistance, it'll roll indefinitely at that speed until hitting the far wall — so I want to pick an initial speed that nets a modest final speed around 0.7 m/s for a reasonable bounce there.

Thinking through the wall collision more carefully: since the ball has forward spin about y, the contact point at the ball's leading edge is actually moving downward relative to the wall, so wall friction would push upward and could cause the ball to climb slightly on impact — I need to account for that interaction with the spin after the linear velocity is absorbed.

Rolling resistance would cause negligible deceleration over the time scale, so I'll just keep default condim 3 for predictability—the friction will dissipate any residual spin fine. For the pendulum, I'm calculating the bob speed needed at the bottom to transfer roughly 1.0 m/s to the ball given the height and inelastic collision assumption.

Now I need to position the pendulum rod as a capsule running from the pivot to the bob, making sure it clears the floor and ball, and set up the hinge rotation about the y-axis so the bob starts pulled back and raised.

Checking rod-versus-ball clearance: the rod's edge stays around x≈−0.047 at its lowest point while the ball spans [−0.03, 0.03], so no overlap there, and since the ball is already ahead after being struck, they shouldn't collide. I'm also checking whether the pendulum's swing afterward could bring it back around to clip the cup, given the max horizontal reach is roughly 0.17 at that angle.

For masses, I'll just assign mass attributes directly: bob 0.2, rod 0.02, ball 0.05, rather than deriving densities. Then I'm verifying the contact geometry — at θ=0 the bob and ball centers are exactly 0.055 apart, equal to the sum of their radii, confirming they touch; I'm working out the exact angle where contact first occurs as the bob swings down.

I'm also considering whether the bob could strike the ball a second time while it's still slipping before reaching pure rolling, since the ball decelerates due to floor friction while the bob swings back. Even with possible re-contacts, the ball should still end up rolling forward, with an estimated final speed around 0.8-1.2 m/s given the 5/7 rolling factor.

Now I'm designing the cup geometry: sizing the walls and gaps so the opening is wide enough (about 0.09 wide) to admit the 0.06-diameter ball, positioning a back wall and two side walls plus front stub pieces to form a mouth, and checking that the ball traveling along y=0 will fit through without clipping the stubs.

The cup body itself should be static—fixed at position (1,0,0) with no joint, since it's meant to just catch the ball, not move. I'm also tracing the ball's trajectory: it reaches the back wall roughly 1 second in, hits with forward spin, and I'm reasoning through whether it might bounce back out the mouth. Given soft contact and spin-driven rolling friction pushing it forward again, it should stay trapped rather than escape.

I'm now working out the keyframe setup: qpos needs to account for the pendulum hinge plus the ball's freejoint, ordered by body tree position. I also need to decide whether to add a static support post or crossbar for the pendulum pivot, making sure it doesn't interfere with the ball's path.

Writing MJCF structure...

