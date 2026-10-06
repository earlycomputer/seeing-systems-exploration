The pendulum starts 45° from vertical and swings down. Its 0.5 kg bob hits the 0.1 kg ball near the bottom of the arc. The ball then rolls about 1 m in +x, hops a 9 mm lip and stops against the back wall of the cup.

I haven't run this file. The numbers below are hand estimates:

- **Bob speed:** about 1.7 m/s at the strike.
- **Ball speed:** roughly 0.85–1.5 m/s after the hit. Clearing the lip needs only about 0.45 m/s.
- **Timing:** the ball should reach the cup at about t ≈ 1–2 s, well inside the 6 s run.
- **Settling:** MuJoCo's default contacts are close to inelastic, so the ball should stay in the cup.
- **Stand:** the stand is visual only (`contype`/`conaffinity` = 0).

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- visual-only stand holding the pendulum axle -->
    <geom name="stand_post_left" type="cylinder" fromto="-0.059 -0.12 0 -0.059 -0.12 0.545" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="stand_post_right" type="cylinder" fromto="-0.059 0.12 0 -0.059 0.12 0.545" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="stand_axle" type="cylinder" fromto="-0.059 -0.12 0.535 -0.059 0.12 0.535" size="0.008" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: pivot at z=0.535, bob centre hangs at z=0.035 just behind the ball -->
    <body name="pendulum" pos="-0.059 0 0.535">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.47" size="0.006" mass="0.05" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.03" mass="0.5" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- cup centred at x = 1 m: thin base, low front lip, tall side and back walls -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.0015" size="0.07 0.07 0.0015" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_lip" type="box" pos="-0.075 0 0.0045" size="0.005 0.08 0.0045" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_back" type="box" pos="0.075 0 0.06" size="0.005 0.08 0.06" rgba="0.9 0.6 0.1 0.8"/>
      <geom name="cup_side_left" type="box" pos="0 -0.075 0.06" size="0.08 0.005 0.06" rgba="0.9 0.6 0.1 0.8"/>
      <geom name="cup_side_right" type="box" pos="0 0.075 0.06" size="0.08 0.005 0.06" rgba="0.9 0.6 0.1 0.8"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.785 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working through the physics of the scene—a ball resting on the floor needs to roll into a cup positioned across the way, so I need to figure out whether the cup should have low walls, an opening, or a ramp so the ball can actually enter rather than getting blocked.

Default MuJoCo contacts are nearly inelastic, so the ball hitting the back wall should just stop rather than bouncing back over the low front step — that solves the energy issue. With condim=3 there's no rolling resistance, so the ball maintains constant speed, meaning I can just pick something like 1 m/s for it to roll steadily. Now I'm thinking through the pendulum setup: hinge height, rod length, bob mass, and starting angle released from rest.

Since collisions are roughly perfectly inelastic, I need to estimate the ball's post-impact speed as a momentum-sharing calculation between the swinging bob and the ball, then account for friction converting initial sliding into rolling at 5/7 of that speed — and the strike height relative to the bob's center matters for this.

Since the sphere-sphere (or sphere-capsule) contact normal always passes through the ball's center regardless of bob shape, the ball inevitably starts sliding before transitioning to rolling at 5/7 speed, so I don't need to worry about precise contact geometry for pure rolling. I also need to check whether the pendulum bob swings back and strikes the ball a second time after it's already rolled away.

Since the pendulum barely slows down while the ball decelerates with friction, it could catch up and strike again, so multiple contacts seem likely and hard to predict without simulation — I should just design with extra margin instead of relying on exact numbers. Maybe lowering floor friction or making the pendulum bob much lighter than the ball could simplify the collision dynamics.

For the cup entrance, I'm leaning toward a small lip rather than a strict velocity threshold — using the physics of a rolling sphere pivoting over a step edge, where the post-impact velocity scales with the ratio of lip height to ball radius, roughly v' = v(1 - 5h/7r), to pick a lip height that still lets the ball hop in reliably.

Checking the ball's flight after leaving the lip — falling roughly 5cm before landing shouldn't cause it to bounce over the back wall, since the wall height of 0.1 is enough margin. I'm weighing whether to drop the front lip entirely and use a three-walled cup instead, but the lip makes it more recognizably cup-shaped, and a sphere-box corner collision in MuJoCo should still behave physically correctly.

I'm also considering using box geoms to form the cup walls rather than cylinders, just treating "cup" as a label regardless of shape. More importantly, I'm worried about the ball's forward spin interacting with the back wall's friction — a rolling ball striking a vertical wall could have its spin cause it to climb up the wall rather than simply stopping, since the contact point velocity from the angular momentum could translate into an upward force against the wall.

I'm roughly estimating how high the ball could climb given typical velocities (maybe a centimeter or so), concluding the back wall should be reasonably tall to contain this effect before the ball falls back in. I also need to make sure that once it falls back with reduced spin, it doesn't gain enough backward velocity to roll back out over the front lip, so I'm thinking about how to shape the lip to prevent that escape path.

Now thinking about the pendulum geometry: setting the bob's height so it clears the floor at the bottom of the swing, since the ball's radius and position determine whether the contact normal pushes it harmlessly into the floor or causes unwanted collision. I'm working through the exact height and radius values to keep the bob clear while still making good contact with the ball.

For timing, I want the pendulum to just graze the ball right near the bottom of its arc where velocity is highest, so I'm adjusting the pivot's horizontal offset slightly so contact triggers just before dead-bottom rather than exactly at it, avoiding a zero-margin resting-contact issue.

For the rod length, I'll set L=0.5 giving a pivot height of 0.535, then add static support posts in the worldbody positioned off to the sides (y=±0.15) so they don't interfere with the ball's path along y=0 or the pendulum's swing in the xz-plane.

Good, since world is the exception to parent filtering, I'll just set contype=0 conaffinity=0 on the stand to be safe. For the pendulum physics, I'll compute the bob's speed at the bottom using energy conservation from the release angle, and assign explicit masses — a heavier bob (~0.5 kg) and a much lighter rod (~0.05 kg) with a small bob radius.

Working through the collision, I calculate the pendulum's effective mass at the impact point using its moment of inertia, then estimate the ball's post-impact speed assuming momentum transfer like a common velocity. But I realize the ball will also be decelerating from floor friction while the pendulum continues to push through contact, so I need to account for that coupling during the impact.

Actually, since the pendulum's gravitational deceleration starts at zero at the bottom of the swing while the ball's slip friction gives a roughly constant deceleration, the ball should separate from the pendulum fairly early once it starts rolling without slipping.

For the target, I want a ball speed around 1.2 m/s after separation, which means I need the pendulum bob's initial speed near 1.6-1.7 m/s. Working backward, a release angle around 45° gives v_bob ≈ 1.70 m/s, and the ball likely comes out around 1.0-1.4 m/s. The timing works out too: roughly 1 second to reach the cup, a quarter-period swing of about 0.355 s, keeping the whole sequence under 2 seconds with room to settle.

Checking the lip requirement: this speed range exceeds the 0.42 threshold, so the ball should clear it fine. I also need to watch for the opposite failure mode, overshooting and hitting the back wall with too much speed, but since the walls have low friction it should be manageable. At 1.4 m/s, after the lip interaction the ball speed drops to about 1.1 m/s before launching into a short flight, which seems fine.

Now I'm working out the hinge geometry -- the pendulum swings from the negative-x side toward positive-x, with the body pivoting at a fixed point and the rod hanging straight down. I'm setting up the rotation equations about the y-axis to track how the bob's position shifts as the angle increases.

With the bob starting at θ=+0.785 rad, it sits raised on the -x side and swings toward +x, confirming the starting configuration is correct. I calculate the bob position at θ=45° to double check it lands at a reasonable spot. Then I'm figuring out the qpos layout for the keyframe -- the hinge takes one value, the ball's freejoint takes seven (position plus quaternion), and I need to set the ball's resting z-position to match its body offset, allowing for slight penetration from the soft contact model.

Now I'm designing the cup geometry: a centered pocket with inner half-width 0.07 to fit the 0.06-diameter ball, thin walls of 0.01, a front lip low enough for the ball to climb over, and a taller back wall and side walls to contain it after it drops in.

I'm debating whether to give the cup a solid floor or leave it open to the ground plane. Adding a base plate complicates the lip height relationships, so I'll skip it and just let the floor serve as the cup's bottom, treating the walls as a simple containing ring.

Working out the geometry of the edge contact, I compute the normal direction from contact point to ball center as roughly (-0.8, 0.6), then project out the velocity component along that normal for the inelastic collision, leaving a reduced tangential speed around 0.6v for the ball to continue with afterward.

Checking whether that remaining speed is enough for the ball to climb over the lip, I find the center needs to rise 0.012m, requiring v' ≥ 0.485 and thus v ≥ 0.81 — a tighter constraint that pushes me toward a lower lip height and differentiated friction settings per geometry (low friction on back/side walls, default elsewhere) to make the shot more forgiving.

Since the contact force is unilateral and gets clamped by MuJoCo once it would go attractive, the effective restitution ends up small, maybe 0.1-0.2 in practice, giving a rebound speed around 0.15 m/s, well below the 0.34 m/s escape threshold. Factoring in spin from the ball rolling into the wall should further reduce the chance of escape after impact.

Working through the friction math, the bounce height ends up only about 8mm, which is negligible given the 0.12 wall height, so low friction isn't actually necessary there — I'll keep things simple and move on. Now I'm sketching the front lip and base geometry, figuring out the box dimensions and positions for the lip and the base section connecting it to the back wall.

I'm also sizing the side walls and back wall boxes, then checking whether the ball could fly over the lip after a fast impact — it looks like the ball could briefly leave the surface at the pivot point given its speed, so I'm working out the launch angle and velocity components at the moment of separation.

Running the numbers, the ball launches close to 45° with modest height gain and roughly 8 cm of horizontal travel during the brief flight, which lands it well within the box before the back wall at 1.07 m, so the geometry should hold up even accounting for this bounce.

As for the pendulum, after the strike it retains enough residual speed to swing forward and rise to roughly 37°, but checking the timing shows the ball is already clear across the box by the time the pendulum reaches that peak, so there's no risk of a second collision.

Checking the floor clearance, the bob at the bottom of its swing sits with its lowest point at 0.005 above the floor, so no contact there, and the rod capsule geometry keeps clear too. Looking at bob-ball contact at the bottom of the swing, the distance between centers is about 0.0592 against a combined radius of 0.06, so they overlap by less than a millimeter — meaning contact actually starts just before the bob reaches the very bottom, which is consistent with the intended strike. With no hinge damping, the pendulum will keep swinging freely afterward.

Setting the ball's mass to 0.1 directly rather than relying on density, and giving the bob 0.5 mass and the rod 0.05, with the floor plane sized generously and basic lighting added. The default Euler integrator should be fine here. Checking the ball's trajectory confirms it stays on a straight line with y=0, and working through the timing — impact around 0.36s, then roughly 0.75s more for the ball to reach x≈0.9 at its rolling speed, landing in the cup around 1.2s total.

Even at a slower ball speed of 0.6 m/s this still works out to about 1.8s total. I'm bounding the worst-case ball speeds: the low end around 0.85 m/s and the high end around 1.43 m/s from momentum transfer, checking whether a fast hit at 1.7 m/s bob speed risks the ball flying over the cup's back wall — working through the projectile arc, rise height, flight time, and horizontal distance, I find it still lands inside since the wall is tall enough. Now I'm defining the rod as a capsule geometry positioned at the pivot in the body frame.

Placing the bob sphere, adding the stand posts and crossbeam as non-colliding worldbody elements positioned around the pivot, double-checking the lip height clears the ball radius, then writing the complete file.

