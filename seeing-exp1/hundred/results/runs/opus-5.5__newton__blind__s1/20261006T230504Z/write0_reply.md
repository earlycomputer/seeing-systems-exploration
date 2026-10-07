A steel-ball pendulum swings down from 0.5 m above its lowest point and hits ball1. The impact then passes through four equal balls whose centres are 0.15 m apart on a level rail. Ball4 rolls off the end of the rail into a sunken box. I haven't run this file, so the behaviour below is what the design is meant to do, not a checked result.

How the design is meant to work:
- **Springy ball contacts.** Ball-to-ball and bob-to-ball contacts are set to be bouncy (low damping) so most of each ball's speed passes to the next.
- **Rail stops leftovers.** The rail is set to damp contacts and adds rolling friction. This should stop the slow leftover motion of balls 1–3 before they reach the rail's end, which extends 0.25 m past ball4.
- **Box catches ball4.** The box is heavily damped and also has rolling friction, so ball4 should settle inside it.
- **Pendulum and rail don't touch.** The pendulum only collides with the balls, never with the rail.

The settings most likely to need tuning are:
- the contact bounciness (`solref="0.006 0.05"` on the balls),
- the rail's rolling friction (0.005),
- the rail length past ball4.

```xml
<mujoco model="pendulum_ball_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.3 -1 2.5" dir="0 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1" solmix="100"/>

    <geom name="stand_post_left" type="cylinder" fromto="-0.05 0.08 0 -0.05 0.08 0.85" size="0.01" rgba="0.4 0.4 0.4 1" contype="0" conaffinity="0"/>
    <geom name="stand_post_right" type="cylinder" fromto="-0.05 -0.08 0 -0.05 -0.08 0.85" size="0.01" rgba="0.4 0.4 0.4 1" contype="0" conaffinity="0"/>
    <geom name="stand_axle" type="cylinder" fromto="-0.05 -0.08 0.825 -0.05 0.08 0.825" size="0.006" rgba="0.3 0.3 0.3 1" contype="0" conaffinity="0"/>

    <body name="pendulum" pos="-0.05 0 0.825">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.575" size="0.004" mass="0.001" rgba="0.3 0.3 0.3 1" contype="2" conaffinity="2"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.6" size="0.025" density="7800" friction="0.3 0.005 0.0001" solref="0.006 0.05" solmix="1" contype="2" conaffinity="2" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="ball1" pos="0 0 0.225">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.025" density="7800" friction="0.3 0.005 0.0001" solref="0.006 0.05" solmix="1" contype="3" conaffinity="3" rgba="0.7 0.7 0.75 1"/>
    </body>
    <body name="ball2" pos="0.15 0 0.225">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" density="7800" friction="0.3 0.005 0.0001" solref="0.006 0.05" solmix="1" contype="3" conaffinity="3" rgba="0.7 0.7 0.75 1"/>
    </body>
    <body name="ball3" pos="0.30 0 0.225">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.025" density="7800" friction="0.3 0.005 0.0001" solref="0.006 0.05" solmix="1" contype="3" conaffinity="3" rgba="0.7 0.7 0.75 1"/>
    </body>
    <body name="ball4" pos="0.45 0 0.225">
      <freejoint name="ball4_free"/>
      <geom name="ball4_geom" type="sphere" size="0.025" density="7800" friction="0.3 0.005 0.0001" solref="0.006 0.05" solmix="1" contype="3" conaffinity="3" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="rail" pos="0 0 0">
      <geom name="rail_plank" type="box" pos="0.345 0 0.19" size="0.355 0.03 0.01" condim="6" friction="1 0.005 0.005" solref="0.02 1" solmix="100" rgba="0.55 0.4 0.25 1"/>
      <geom name="rail_lip_left" type="box" pos="0.345 0.031 0.2075" size="0.355 0.003 0.0075" condim="6" friction="1 0.005 0.005" solref="0.02 1" solmix="100" rgba="0.55 0.4 0.25 1"/>
      <geom name="rail_lip_right" type="box" pos="0.345 -0.031 0.2075" size="0.355 0.003 0.0075" condim="6" friction="1 0.005 0.005" solref="0.02 1" solmix="100" rgba="0.55 0.4 0.25 1"/>
      <geom name="rail_post_a" type="box" pos="0.05 0 0.09" size="0.02 0.02 0.09" rgba="0.4 0.3 0.2 1"/>
      <geom name="rail_post_b" type="box" pos="0.64 0 0.09" size="0.02 0.02 0.09" rgba="0.4 0.3 0.2 1"/>
    </body>

    <body name="box" pos="0 0 0">
      <geom name="box_floor" type="box" pos="0.91 0 0.015" size="0.2 0.09 0.015" condim="6" friction="1 0.01 0.01" solref="0.02 1" solmix="100" rgba="0.3 0.6 0.3 1"/>
      <geom name="box_wall_near" type="box" pos="0.715 0 0.085" size="0.005 0.09 0.085" condim="6" friction="1 0.01 0.01" solref="0.02 1" solmix="100" rgba="0.3 0.6 0.3 1"/>
      <geom name="box_wall_far" type="box" pos="1.105 0 0.2" size="0.005 0.09 0.2" condim="6" friction="1 0.01 0.01" solref="0.02 1" solmix="100" rgba="0.3 0.6 0.3 1"/>
      <geom name="box_wall_left" type="box" pos="0.91 0.085 0.125" size="0.2 0.005 0.125" condim="6" friction="1 0.01 0.01" solref="0.02 1" solmix="100" rgba="0.3 0.6 0.3 0.6"/>
      <geom name="box_wall_right" type="box" pos="0.91 -0.085 0.125" size="0.2 0.005 0.125" condim="6" friction="1 0.01 0.01" solref="0.02 1" solmix="100" rgba="0.3 0.6 0.3 0.6"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.40335 0 0 0.225 1 0 0 0 0.15 0 0.225 1 0 0 0 0.30 0 0.225 1 0 0 0 0.45 0 0.225 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm setting up a scene where a pendulum bob swings down and strikes a line of balls spaced 0.15 m apart, like a loose Newton's cradle, with the final ball rolling into a box at rest. I'm considering how the chain reaction should propagate realistically between the gaps.

Default MuJoCo contact solref with critical damping tends to behave inelastically for equal masses, which would cause the balls to clump together rather than transfer momentum cleanly down the line, so I'm thinking I need to tune the contact solver parameters—using something like a lower damping ratio or explicit stiffness/damping values—to get a more elastic, billiard-like transfer of momentum between each ball.

For the final ball settling into the box, I'm considering whether to let friction and rolling resistance naturally dissipate its energy against the walls and floor, or whether to sink the box floor below the rail so the ball drops in and loses energy through an inelastic landing instead.

"Moves slower than 5 cm/s" probably just means linear velocity, so this should be fine. Freejoint doesn't seem to support a damping attribute directly, so I'll skip that. For balls resting on the flat rail, they'll stay still until struck, and since there's no rolling resistance with condim 3, a moving ball should just roll on at constant speed, which works for the setup.

I should check whether balls could drift sideways off the rail, though symmetry means y stays near zero — but to be safer, I could build the rail with two low side walls for lips, keeping balls centered. I'll set a ball radius of 0.025, derive mass from density, and figure out the rail's height relative to the pendulum setup.

Now I'm working out the actual geometry: placing the rail top at z=0.2, with ball centers at z=0.225, spaced 0.15 m apart along x. For the pendulum, I'm positioning the pivot and bob so the bob touches the first ball at the lowest point, setting rod length to 0.6 m, then solving for the release angle needed to drop the bob 0.5 m — giving roughly 80.4° from vertical, released from the negative x side.

I'm checking the rotation convention about the y-axis to confirm positive θ swings the bob toward negative x, giving a release angle of about 1.403 rad, and making sure the rail's starting x position leaves clearance for the bob's swing path.

After the elastic-ish collision I'm considering that the bob might not stop completely — with imperfect restitution it could creep forward and bump ball1 or the rail end again, so I need to check how far it can travel before ball1 blocks it.

Checking the geometry, the clearance between bob and the rail corner is marginal but just enough at 0.027 vs 0.025. I'm also calculating the physics for speed: dropping from 0.5m gives the bob about 3.13 m/s, which transfers into ball1 at roughly 3 m/s, then reduces to ~2.2 m/s rolling speed once friction takes over — fast enough that ball4 would fly off at over 2 m/s on impact.

I want the strike to happen at matching heights so the collision is purely horizontal. I'm placing the box to catch ball4 right at the rail's end, lowering its floor to around z=0.1 so the ball falls roughly 0.1m before landing, giving a short 0.143s fall time and about 0.29m horizontal travel at 2 m/s speed.

I'm now worried it'll smack the far wall too hard and bounce out, so I'm considering a sunken pit design instead, with tall walls (especially the far one) to contain the energy, floor near z=0.05, and enough inner length to absorb the impact without the ball escaping back out the entrance.

Working through the exact geometry: the rail ends around x=0.55, so I'm placing the box's near wall just beyond that so the ball clears it while rolling off the rail edge, with the near wall low enough (z=0.18) that the ball's falling trajectory passes over it, then sizing the box interior to about 0.4 long with the far wall positioned to actually catch the ball.

I'm estimating fall time from rail height to floor height (~0.175s) and checking whether the ball lands before or after hitting the far wall depending on speed — at 2 m/s it just barely stays inside, at 2.5 m/s it strikes the far wall mid-air, which is fine since that wall is tall enough to contain it either way. I'm also considering whether the ball could bounce back out over the near wall, but since the default contact damping gives little bounce, it should settle inside instead of escaping.

Now I'm thinking through how MuJoCo mixes solref parameters when two geoms with different contact properties touch — it averages them via solmix, so pairing an elastic ball with a damped box gives an intermediate bounce rather than a true elastic one. I'm weighing whether to use explicit contact pairs to assign elasticity precisely between ball-ball and ball-wall interactions, but that risks duplicate contacts unless the default collision is excluded via contype/conaffinity, so I'm leaning toward just tuning the solref values on the geoms directly to get the averaged result I want.

For elastic collisions, I'm thinking a solref of roughly "0.01 0.1" gives a timeconst of 5 timesteps and a damping ratio around 0.1, producing restitution near 0.73 via the standard soft-constraint approximation, though MuJoCo's actual impedance behavior only approximates this. I'm also considering that friction at the ball-ball contact point could impart slight spin transfer during impacts, since ball1's forward rotation creates a tangential velocity at contact that nudges ball2 with minor backspin.

The bigger concern is whether this collision chain actually delivers ball4 into the box, since with partial restitution ball1 won't fully stop—it retains some translational speed plus spin, which friction then converts into rolling motion at roughly 2/7 of its post-collision velocity, letting it creep forward at maybe 30-40% of its original speed. That means ball1 could keep advancing into the region where ball2 is also moving, though ball2 is still faster, so they likely won't re-collide immediately—but this raises the question of whether other balls might unintentionally end up entering the box when only ball4 is supposed to.

To actually stop balls 1-3 after their collisions, I need rolling friction on the rail, probably by adjusting contact parameters so that a rolling ball decelerates due to a rolling resistance torque. I'm working through the deceleration equations relating torque, moment of inertia, and radius to figure out how much rolling friction coefficient is needed to bring these balls to rest before they can roll into the box.

What if the rail is frictionless so balls don't spin, letting elastic collisions transfer momentum cleanly? But then leftover velocity from imperfect restitution would still drift balls toward the box too fast. I think near-perfect elasticity is the real fix — using soft contact parameters with low damping to push restitution close to 0.94 so leftover drift is negligible.

Maybe I should estimate with rolling friction and e≈0.85 instead, calculating the velocity ball1 gets from the bob's impact using the standard elastic collision formula with equal masses.

Factoring in spin's angular momentum contribution, ball1 likely settles around 0.3-0.5 m/s, then rolling friction decelerates it roughly 0.14 m before stopping. Ball2 follows the same slide-to-roll pattern, ending up near ball3's original spot and nudging it forward too, so ball3's leftover velocity carries it to roughly 0.54 m further.

This puts ball3 dangerously close to the rail's end at 0.55 — risking it falling off. I should extend the rail to around x=0.70 so ball3 settles safely before that point, while ball4 still has room to decelerate from its faster ~2 m/s speed across the remaining distance. There's some uncertainty since rolling friction also acts during the sliding phase and ball2's leftover motion might tap ball3 again as it moves away, plus ball1's leftover could gently graze ball2 — but the rough leftover distances should still work out.

Let me try bumping rolling friction to μ_r = 0.005, which gives a deceleration of about 1.4 m/s². Checking ball4's speed over its travel distance, it loses little and stays comfortably around 1.8 m/s, while its leftover momentum stops within a short distance — this seems like a solid choice. I need to make sure the contact model uses condim 6 so rolling and torsional friction are active, and set the ball friction parameters to include small rolling and torsional coefficients alongside the sliding friction value.

I'm thinking about how friction mixing works between ball-ball and ball-rail contacts: since MuJoCo takes the max of each friction component when solids mix, I can set condim 6 on the rail only and condim 3 on the balls, so ball-rail interactions get the higher-order friction while ball-ball stays simpler. I'll set rail friction with a high tangential value and low rolling/torsional coefficients, and keep the ball friction tangential coefficient moderate (around 0.3) to limit sliding friction in ball-ball collisions since the rail's friction values will dominate via the max-mixing rule anyway.

For the box, I'm reasoning through ball4's trajectory as it flies in at roughly 1.8 m/s, considering that the floor's condim-6 friction setup (with tangential coefficient 1 and rolling/torsional at 0.01) combined with solmix damping should let the ball settle within the simulation window — landing early around the 1-second mark and having about 5 seconds to decelerate and stop given the rolling friction coefficient, plus any wall impacts along the way. I'm also sizing the box's inner floor so it's not too large, keeping it compact, and confirming that MuJoCo's default pyramidal friction cone works fine with condim 6 for this rolling friction setup.

For the pendulum, I'm working out that after striking ball1 with a restitution of about 0.85, the bob retains a small residual velocity around 0.23 m/s, which causes it to swing with a small amplitude oscillation around the bottom of its arc. Calculating the natural frequency and resulting amplitude, I find the bob's front edge would swing forward enough to potentially strike ball1 again if ball1 remains positioned there, since the displacement from this residual swing is comparable to the gap between them.

I'm also checking whether the bob grazes the corner of the rail at this forward position, computing the distance between the bob's center and the rail corner at a few sample positions — it comes out just barely over the bob's radius, so it seems to just miss the rail at this swing amplitude.

Actually, simpler fix: use separate contype/conaffinity groups so the bob only collides with balls, not the rail — rail=1, bob=2, balls=3 bitmasks, so bob and rail never register contact while bob-ball collisions still work. The pendulum rod stays in the bob's group too, which is fine since it's positioned above and won't hit balls. Hinge damping isn't necessary since the pendulum doesn't need to settle, though residual swing is worth watching.

I'm giving the rod negligible mass so it doesn't distort the bob's momentum transfer, and setting bob and ball densities equal (steel, ~7800) with matching radii so the collision physics stays symmetric.

Checking the penetration depth for the fastest ball given its velocity and the contact timeconst—roughly a centimeter, which seems tolerable against the ball radius but worth watching since solimp parameters also factor in.

I'll bump timeconst up slightly to around 0.006 to stay safely above the minimum of twice the timestep, treating the restitution from dampratio 0.05 as approximate rather than precise. Now I'm working out the rail geometry: the rail body spans from x=-0.01 to 0.70, giving a center and half-width, with the plank's vertical extent and the side lips positioned to contain the ball at the rail's center.

Checking clearance, the ball's radius at the lip height stays comfortably within the lip's inner face, so I size the lip boxes accordingly and add a vertical post below the rail from the floor up to its base height for visual support, even though the rail body itself is a fixed object.

For the pendulum, I'm placing the bob at its release angle using the pivot position and swing length, giving coordinates for the starting point. I add a static support stand with posts and a crossbar beneath the pivot — these are decorative and won't interfere with collisions since the bob's lateral range stays narrow and pivot posts use default contact settings.

Now I'm checking where ball4 exits the rail edge and its exit speed after rolling friction, then considering how the box near the wall will receive it.

I'm mapping out the box's internal geometry — floor height, wall placements, and fall distance from the rail edge to the floor — to confirm the ball lands inside with time and horizontal travel calculated from its exit velocity, verifying it reaches the far wall rather than overshooting, and noting the side wall dimensions for containment with inelastic bounces.

Checking whether ball3's leftover momentum after colliding with ball4 leaves enough margin before the rail ends, and confirming the spacing between ball4 and the rail edge is sufficient. I'm also tracking whether residual spin could nudge ball1 into a stopped ball2, and estimating the final resting positions of balls 1 through 3 along the rail, allowing for the possibility they end up touching.

I'm reviewing the solver mixing parameters: the box and rail use high solmix with a softer solref so ball-rail contacts stay damped rather than bouncy, same with the floor, while each ball has its own tighter solref that gets blended using the solmix-weighted formula, and solimp mixes the same way. Then I'm checking the keyframe structure — the pendulum hinge contributes one qpos value, each of the four ball freejoints contributes seven, totaling 29 values, and I need to make sure each ball's keyframe entry correctly matches its intended position with an identity quaternion at height 0.225.

I settle on body ordering (pendulum, balls, rail, box) and lay out the full keyframe qpos string with the pendulum angle followed by each ball's position and orientation. Now I'm defining the pendulum body itself, with its hinge joint, a thin capsule rod, and a bob sphere at the end.

I'm now assigning contype/conaffinity groups so the rod doesn't collide with balls geometrically, while balls do collide with rail, floor, and box via their own groups, and setting friction and condim values for balls, rail, and box surfaces.

Checking that MuJoCo's friction constraints will bring a ball to full rest at low speed, and deciding to keep the default Euler integrator and pyramidal friction cone rather than switching to implicitfast. Now I'm finalizing the floor plane dimensions, adding lights, and writing out the final model.

