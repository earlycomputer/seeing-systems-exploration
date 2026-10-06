The scene releases the pendulum from horizontal. It strikes the ball at the ball's centre height, and the ball rolls 1 m to a cup centred at x = 1. The ball can't climb a cup wall from the floor, so the cup body has a short ramp leading up to a 5 cm entry rim. The ball goes over the rim and drops into the cup. The other three walls are 12 cm tall, and all four walls are higher than the 3 cm ball radius, so the ball stays trapped.

These numbers are design estimates, not results from a simulation run:

- **Strike speed:** the 1 kg bob on a 0.2 m arm reaches about 2 m/s at the bottom of its swing.
- **Rolling speed:** once sliding turns into rolling, the ball should keep somewhere between about 1.4 m/s (if the hit is nearly inelastic) and about 2.6 m/s (if it is elastic).
- **Clearing the rim:** the ball needs about 0.84 m/s to roll up and over the 5 cm rim.
- **Fast case:** at the high end of that range it should still hit the far wall below the wall's top.

```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- visual-only pivot marker -->
    <geom name="pivot_marker" type="cylinder" pos="-0.061 0 0.23" euler="90 0 0" size="0.012 0.03" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: pivot 0.2 m above the bob's lowest point; bob bottom position touches ball at centre height -->
    <body name="pendulum" pos="-0.061 0 0.23">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.175" size="0.008" mass="0.05" rgba="0.4 0.4 0.5 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.2" size="0.025" mass="1.0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball's start; interior is the floor between the walls -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.3184 0 0.0151" euler="0 -9.46 0" size="0.1521 0.1 0.01" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.16 0 0.025" size="0.01 0.17 0.025" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_far" type="box" pos="0.16 0 0.06" size="0.01 0.17 0.06" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.16 0.06" size="0.17 0.01 0.06" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.16 0.06" size="0.17 0.01 0.06" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- pendulum held horizontal (bob at x = -0.261), ball at rest -->
    <key name="start" qpos="1.5708 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to work out the physical layout: ball resting on the floor, a cup positioned a meter away, and a pendulum suspended above the ball that swings down from horizontal under gravity to strike it. The tricky part is making sure the ball actually rolls into the cup opening rather than bouncing off its walls.

Rolling friction tuning is fragile without testing. A more robust design: a horseshoe-shaped cup with an open front and a ramp leading up to the rim height, so the ball rolls up, drops inside, and is trapped by walls on the remaining sides—though rebound off the back wall from default contact damping could still kick it back out through the opening.

Doing the energy math: for a solid sphere's rolling kinetic energy (0.7mv²) to climb a ramp of height h against gravity, the entry speed must exceed sqrt(gh/0.7)—so for h=0.03m, roughly 0.65 m/s minimum. Once inside, the ball's remaining speed after the climb needs to stay below whatever it'd take to clear the far and side walls, which could be taller (like 0.08m) to keep it contained.

A vertical step equal to the ball's radius effectively blocks rolling escape since contact happens at mid-height and pushes horizontally rather than letting it climb — so making the near rim around 0.04m should trap the ball even if it exits the ramp ballistically rather than rolling. I need to work out the parabolic trajectory off the ramp top to make sure the cup interior is long enough to catch it, then consider just using a simple box shape for the interior floor to simplify the geometry.

I'll go with the ramp design: rim height 0.05m, ball radius 0.03m giving a volume of about 1.13e-4 m³ and mass around 0.113 kg at default density, placing the cup on the floor at roughly 1m horizontal distance from the ball's start.

For the dynamics, since the sphere rolls freely on the plane without rolling resistance, I need to account for energy loss when the ball transitions from sliding to rolling after impact — a ball struck at center height loses energy such that its final rolling speed becomes 5/7 of the initial sliding velocity. So requiring enough energy to climb the 0.05m rim means v0 must exceed about 0.84 m/s before friction losses, and I'm targeting a rolling velocity near 1.5 m/s to ensure it clears the rim comfortably.

Working through the energy balance: with rolling KE coefficient 0.7, a 1.5 m/s roll gives 1.575 energy per mass, and subtracting the potential energy to climb 0.05m leaves enough to reach the top at about 1.24 m/s. Using the ramp's shallow angle (~11° from height 0.05 over horizontal 0.25), the ball then becomes a projectile off the top, falling 0.05m to the floor in about 0.1s and landing roughly 0.12m horizontally before continuing to roll across the cup floor.

I'm thinking through what happens when the ball reaches the far wall -- it'll bounce back with low restitution (MuJoCo's soft contact with damping ratio 1 gives maybe 0.1-0.2), and since the ball is still spinning forward even after translational reversal, floor friction will eventually reverse that spin too, letting the ball settle into a back-and-forth bouncing motion between the walls while staying inside the cup. I'm considering whether to add rolling friction to the ball's contact properties to help it settle faster, perhaps using condim=6 with a friction vector like "0.8 0.005 0.0001".

Now I'm second-guessing the rolling friction approach since the torque coefficient units and behavior can be unpredictable in MuJoCo, so I'll likely skip it and rely on the cup walls naturally containing the ball regardless. I'm also checking whether the ball could climb the wall on impact -- working through the geometry of the spinning ball hitting the vertical wall, computing the surface velocity at the contact point based on the angular velocity about the y-axis to see if friction there would cause any upward creep.

Using the effective tangential mass for a sphere (2/7 m), the slip-stopping impulse gives only about 0.35 m/s upward velocity, so the climb height is negligible (~6mm) — I'll keep the far wall at 0.1 to be safe. I also need to make sure the ramp's top edge aligns with the near wall's top so the ball rolls smoothly onto the wall and over the inner edge into the cup.

Now I'm working out the cup geometry centered at x=1, with an interior half-width around 0.12–0.15, and tracing the ball's trajectory as it leaves the wall edge, arcs over, and lands inside before potentially hitting the far wall. I'm also computing the ramp's rise angle (about 9.46°) based on a 0.05 height gain over a 0.3 run, and starting to define the ramp's box geometry.

Computing ramp rotation and position...

I'm checking that the box corner dipping below the floor isn't an issue since the cup is a static body with no joint, meaning static-static contacts with the floor are excluded anyway. Now I'm working out exactly where the box's end faces land relative to the ramp's bottom corner.

Confirming the lower corner lines up at (0.53, 0), so the ball crossing the small 9.5° kink there should be fine at its rolling speed. I'm also checking the near-wall section at the top — a short flat box segment from 0.83 to 0.85 at height 0.05 — and figuring the ball might hop slightly over that kink but it shouldn't cause real issues.

Now I'm narrowing the ramp to half-width 0.1 in y so the ball travels straight and hits the pendulum squarely. I'm laying out the cup geometry: interior walls from x 0.85 to 1.15, y ±0.15, with a far wall and side walls at height 0.1, and a shorter 0.05 near wall. I'm deciding the floor itself can serve as the cup's base rather than adding a separate plate, since that would just introduce an unwanted step.

Now I'm setting up the pendulum assembly — placing the ball at its rest position, defining the hinge pivot above it, and working out the bob's radius, rod length, and position at the bottom of its swing so it strikes the ball at the right contact point.

But I notice at the bottom of the swing the bob's z-height nearly equals its radius, meaning it would graze the floor — I need to shrink the bob or shift the contact point to avoid that collision.

With bob radius reduced to 0.025 at height 0.03, I get a safe 0.005 clearance from the floor, and the impact with the ball stays purely horizontal. I'm also considering how MuJoCo's contact damping will handle the collision — with critical damping the restitution is near zero, so the transfer behaves more like an inelastic collision rather than a bouncy elastic one.

Working through the momentum transfer, the ball should end up with velocity somewhere between the fully inelastic case (M/(M+m))V and the elastic case 2(M/(M+m))V, depending on how much the pendulum continues pushing after initial contact. Since the ball is struck at its center, it'll initially slide before friction converts it to rolling at 5/7 of that initial speed — I could tune this further with solref but I'll stick with the default contact parameters for now.

Checking the exit angle at the ramp top: the ball launches nearly horizontal, so its centre stays near 0.08 height, safely below a wall raised to 0.12. I should bump the far/side wall height for margin, and verify the ballistic rise at various exit speeds stays small enough not to clear the wall — this suggests a workable rolling-speed window somewhere around 1.0 and up.

I also need to check the sliding-to-rolling transition distance with default friction, which comes out around 0.1 m — short enough not to matter. For target rolling speed near 1.4–1.6 m/s, I'm back-calculating the needed initial launch speed under both inelastic and elastic assumptions, since an elastic bounce could roughly double the rolling speed and push it toward the upper limit of what's safe.

I'm also second-guessing whether MuJoCo's default critically-damped contact model behaves more like an inelastic or elastic collision — with critical damping, the penetration returns to zero without overshoot, so the ball doesn't get a true elastic bounce, but it's not purely inelastic either since the contact force keeps acting on the mass as it separates.

So I'll treat the collision as roughly inelastic with a small restitution factor near 1.1x. For the pendulum-ball setup, I want the bob (say 1 kg) hitting a lighter ball (0.1 kg) so the ball exits at close to the bob's impact velocity, targeting an initial ball speed around 2.1 to get roughly 1.5 m of rolling distance — working out what release height gives that bob velocity at the bottom of its swing.

Let me try different pendulum lengths and release angles: a length of 0.3 m released from 60° off vertical gives a bottom velocity of about 1.72 m/s, which translates to rolling distances roughly between 1.2 and 2.4 m depending on restitution, so I need to check this against the threshold condition more carefully.

I'm also considering whether the pendulum could swing back and hit the ball a second time after separation — since the ball leaves quickly, it should already be out of range by the time the pendulum returns. Without damping, the pendulum would oscillate indefinitely, so I might add a tiny bit of hinge damping or just leave it undamped since it doesn't affect the single collision event.

Actually, let me simplify the setup: releasing the pendulum from horizontal with L=0.2 gives a clean impact velocity of about 1.98 m/s, producing a reasonable post-collision rolling speed either way (inelastic ~1.41, elastic upper bound ~2.57), so I'll go with horizontal release and work out the pivot position, rod geometry, and bob placement accordingly.

Rotating about the y-axis by θ=π/2 puts the bob initially at (-L,0,0) relative to the pivot, so it swings toward +x and strikes moving in the desired direction — giving initial hinge qpos of 1.5708 and a bob position around x=-0.261, z=0.23. I'm setting a light rod mass (~0.05) with a heavier bob (1.0) so the effective swing speed stays close to the simple sqrt(2gL) point-mass estimate.

I'll skip adding a physical pivot support since the pendulum can hang without one, but I could add a purely visual cylinder at the pivot with no collision properties if needed. For the ball, I'm letting it rest slightly into the surface at z=0.03 for a stable settle, and I'm building the keyframe qpos string with the hinge angle first (1.5708), followed by the ball's 7-value freejoint state (position and quaternion), since the cup itself has no joints to include.

Working through the timing: a quarter-period swing for the pendulum from horizontal to vertical takes roughly 0.27s given the amplitude correction, and the ball at ~1.4 m/s should cross the gap to the ramp in about 0.4s, landing in the cup around the 1s mark — well within the 6s simulation window. I'm also checking that the resting ball doesn't actually penetrate the floor given the small gap, and confirming the ramp-ball contact uses the default condim 3 setting, which should be sufficient.

Checking that the ball hits the ramp exactly on centerline alignment, then thinking through how it behaves once inside the cup — bouncing between walls with some energy loss until it settles, without climbing the inner wall faces since the ball radius keeps its center below the wall top edge. I confirm the ball should clear the near wall's inner top edge properly and land correctly without skidding issues, then start checking that the ramp's width lines up with the cup's wall span.

Setting the ball's mass explicitly and letting the sphere inertia derive from that, then moving to writing the XML — placing the floor plane, considering optional lights, and positioning the cup geoms (ramp box with its tilt angle, cup body location) so everything lines up relative to the cup's body frame at a chosen offset.

Working out wall positions and dimensions...

Double-checking the Euler angle sign for the ramp's rotation about y — confirming that the up-vector and normal vector directions both come out correct at θ=-9.46°. The ramp's top corner meets the near wall's top edge at x=0.83, which lines up consistently.

I'll skip adding a visual base for the cup bottom, leave keyframe controls at none, and leave hinge damping at its default.

