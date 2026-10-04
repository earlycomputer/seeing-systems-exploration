The pendulum starts held back 40° and swings down under gravity. Its heavy bob hits the 3 cm ball at the bottom of the swing, at the ball's centre height, so the ball rolls along +x. The cup is a walled box centred at x = 1 m. A shallow ramp leads up and over its 4 cm front lip. The side and back walls are 10 cm tall. All walls are taller than the ball's radius, so once the ball drops in it can't roll back out.

These figures are hand estimates; I haven't run the simulation:

- **Ball speed after the hit:** about 1.1–2.1 m/s.
- **Minimum speed to clear the lip:** about 0.75 m/s.
- **Back wall:** even at the fast end, the ball reaches it with its centre around 6 cm up. That is below the 10 cm wall top, so the ball stays in.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.056 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.005" mass="0.02" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="1.0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_ramp" type="box" pos="0.798 0 0.0102" euler="0 -12 0" size="0.0962 0.1 0.01" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_front" type="box" pos="0.895 0 0.02" size="0.005 0.11 0.02" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="box" pos="1.105 0 0.05" size="0.005 0.11 0.05" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_left" type="box" pos="1.0 0.105 0.05" size="0.11 0.005 0.05" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_right" type="box" pos="1.0 -0.105 0.05" size="0.11 0.005 0.05" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.698 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out scene geometry: placing the ball at the origin resting on the floor and the cup centered a meter away, and considering whether a rolling ball could actually enter a walled cup without a ramp or opening.

So I'm leaning toward a U-shaped cup with an entrance gap facing the ball, a back wall to stop it, and relying on inelastic contact settings so it doesn't bounce back out, though a low-lip step the ball rolls over is another option worth weighing against physical realism.

With rolling friction the ball will lose energy on each bounce and eventually settle, so I can tune speed so it stops near the target even without the wall as backup. Alternatively I could shape the entrance as an external ramp leading up to the cup's lip: the ball needs enough speed to climb the ramp height (using rolling kinetic energy 7/10 m v² vs g h), and once past the lip it drops into the cup where the vertical interior wall prevents it from climbing back out.

Even a fast ball should stay trapped since it hits the back wall at low speed after the short drop. I'm also checking ramp-to-box collisions: since the cup is a static body with no joint, static-static collisions get skipped automatically, so the rotated ramp intersecting the floor isn't an issue. The remaining concern is the transition where the ramp meets the top of the front wall — making sure the ball transitions smoothly from slope to edge without getting stuck.

Now I'm working out exact dimensions: I'll flush the ramp top against the wall's outer face, computing the ramp length from a 15° incline rising 0.04m. I'm also reconsidering whether a square cup built from boxes is simpler than a cylindrical ring, settling on inner half-width 0.08, wall thickness 0.01, and wall height 0.04 against a 0.03 ball radius.

I'm bumping wall height to 0.05 for safety, recalculating the minimum launch speed needed (~0.837 m/s) and settling on an aim speed near 1.3 m/s. I'm placing the front wall's outer face at x=0.91 and defining the ramp as a plane rising from the launch point up to that wall's top edge, now working out the ramp's angle.

Computing ramp box geometry...

Checking the rotation sign: for a y-axis rotation of -12°, x maps toward +z as needed, so euler="0 -12 0" works. I'm verifying the ramp's edges align with floor level at both ends so the ball transitions smoothly onto and off the slope without catching on exposed corners.

Now I'm computing the ball's speed at the top of the ramp, accounting for rolling energy loss and the climb height: starting at v0=1.3, it slows to about v'≈0.995 at the edge, with an upward velocity component of roughly 0.2 from the 12° incline. I'm figuring out the launch point—the ball's center sits slightly offset from the ramp surface by its radius, giving a position around (0.904, 0.079) as it leaves the edge and becomes a projectile.

Working through the projectile motion, I'm solving for the time to drop the 0.05 in height to the next surface, getting t≈0.1235 s. Using that time with the horizontal velocity component, the ball's center lands at roughly x≈1.024, and now I'm comparing that landing spot to the position of the inner back wall at x=1.08 to check whether it clears or hits it.

I'm verifying the ball clears the top edge en route and confirming it lands before reaching the back wall, with max height around 0.082 staying below the 0.05 wall blocking threshold. Then I check that inside the 0.16×0.16 box, with wall height 0.05 exceeding the ball radius 0.03, the ball stays contained after bouncing, before considering a higher initial velocity scenario of v0=1.6.

Front wall outer face moves to 0.89, so I'll redo the ramp with its top there. I'll make back and side walls taller (0.1) while keeping the front wall at 0.05 for robustness against overshoot, and confirm the ball stays within bounds when bouncing back since friction on the floor won't slow its roll.

Since contacts are fairly dissipative, the ball bouncing inside the cup should settle without escaping. Now I need to work out the pendulum setup — hinge height, rod length, and bob position so it strikes the ball at its center height with the target speed at the bottom of the swing.

At the lowest point, the bob's velocity is horizontal, so I'm placing the pivot so the bob just touches the ball at that bottom position — bob center at z equal to the ball radius, with the pivot x-offset set to the sum of bob and ball radii so contact happens exactly there, keeping the ball's start position a meter from the cup. I also need to check the bob clears the floor given its radius.

Now I'm thinking through the collision physics: MuJoCo's default contact solver is mostly inelastic with little bounce, so the pendulum bob's effective mass at the contact point matters more than its total mass. If I make the pendulum heavy relative to the ball, the two move together briefly then the pendulum keeps pushing as it swings upward, decelerating while the ball rolls ahead and separates.

I'm also accounting for the ball's initial slide-to-roll transition via floor friction, which settles it at roughly 5/7 of its initial sliding speed — so I'm estimating a target rolling speed around 1.35, checking that it clears the ramp (needs more than about 0.84) while staying under whatever upper bound avoids overshooting the back wall, testing scenarios like an initial speed of 2.5 to see where the ball would land relative to the wall.

With that window of roughly 0.9 to 2.5 established, I'm aiming for about 1.5 as the target rolling speed. Now I'm working out the pendulum-to-ball collision: giving the bob a mass much greater than the ball (say a 20:1 ratio) so the inelastic collision transfers close to 95% of the bob's speed to the ball, while considering how MuJoCo's contact damping might introduce some restitution effects.

Accounting for the slide-then-roll transition using 5/7 scaling, I land on swinging the pendulum with initial speed around 1.6, which translates to roughly 1.14–2.24 once rolling — comfortably inside the window.

For the pendulum release itself, u=1.69 works out from a drop height around 0.146 m with length 0.5 m, giving θ0=45°, with rod and bob inertia negligible since the rod mass is small. I'm placing the pivot at z=0.53, x=-0.055 to account for the combined bob and ball radii.

Since contact engages right at the lowest point where velocity is horizontal, I'll settle on pivot x=-0.056, slightly inside -0.055, so penetration grows naturally just past bottom rather than before. Now I'm setting up the pendulum body at (-0.056, 0, 0.53) with a hinge along the y-axis.

I'm working out the rod and bob geometry, then reasoning through the rotation: setting the hinge angle to about +0.785 radians (45°) swings the bob back toward -x initially, so that its downswing carries it toward +x and gives it positive velocity at the bottom when it contacts the ball.

For the keyframe, I'm specifying the hinge angle plus the ball's free-joint state (position on the floor with identity orientation), noting the cup is static and needs no qpos entry. I'm also checking that the pendulum, lacking damping, will keep swinging back and forth after the hit but shouldn't cause issues since the ball will already be gone and the bob clears the floor.

Now I'm working through whether the pendulum could re-strike the ball: since the ball slides with friction decelerating it at roughly μg while the bob near the bottom decelerates more slowly, I'm calculating the short sliding-to-rolling transition time (about 0.047s) to see if the pendulum catches up to the ball again during that window.

Working through the contact geometry, the upward-moving point creates friction with the bob that resists the ball's rotation, making the exact rolling speed hard to pin down analytically—likely somewhere between 1.2 and 2.4 in these units. Rather than solve this precisely, I'm considering just lowering the friction coefficient on the pendulum's geoms to reduce this interaction effect.

Trying θ0 = 40° instead: that gives h=0.117 and u=1.515, putting the range at roughly 1.06–2.1, which comfortably clears the ramp's 0.84 requirement even accounting for the lip. My lower-bound estimate was likely too pessimistic since the heavy pendulum keeps pushing the ball during spin-up, pulling the actual speed closer to u. I'll go with 40°, and maybe shave the front lip down to 0.04 to give a bit more margin on the minimum velocity.

Checking that a 0.03 ball radius still gets trapped by a 0.04 lip, confirming yes. I'm now working out wall placements and dimensions for the ramp housing -- computing center positions and half-sizes for front, back, and side walls based on the updated lip height.

Now I'm computing the ramp geometry itself: using the 12° incline angle to find the horizontal run, slope length, top-surface midpoint, and the box center offset accounting for the surface normal, then setting the half-dimensions and rotation for the ramp box.

Checking the ball's flight off the ramp into the cup at 2.1 rolling speed: after the drop, velocity reduces to about 1.96, and by the time it reaches the back wall its height is around 0.06, comfortably below the 0.1 wall height, so it clears fine.

After bouncing off the back wall, the ball heads back toward the front wall whose inner face is 0.04 tall. Since its center height is lower than that, it should stay contained unless it's still airborne high enough to hop the edge, which seems unlikely given the low restitution. For the slower 1.06 case, the velocity squared works out to about 0.56 after the drop, confirming the ball stays well-behaved in both scenarios.

I also want to double check the pendulum-ball collision timing and masses: the ball at 0.05 mass versus a 1.0 bob, with MuJoCo deriving the sphere's inertia automatically from the geom, floor friction left at default so the ball rolls cleanly without extra rolling resistance, and small masses assigned to the rod versus the heavier bob to keep the physics sensible.

Setting the keyframe with the pendulum at 40° (0.698 rad) and ball resting at z=0.03. Now I need to add lighting for the scene to be visible.

