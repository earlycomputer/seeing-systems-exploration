The ball starts near the top of a 10° ramp. It rolls off the ramp's lower end, which overhangs the near wall of a low open box (the cup). It lands inside, hits the far wall, and settles. Rolling friction on the cup floor helps it stop.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.2 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="ramp" type="box" size="0.25 0.06 0.01" pos="0.1371 0 0.1386" euler="0 10 0" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_post" type="box" size="0.01 0.04 0.0825" pos="-0.09 0 0.0825" rgba="0.5 0.35 0.2 1"/>
    <body name="cup" pos="0.5 0 0">
      <geom name="cup_floor" type="box" size="0.12 0.08 0.005" pos="0 0 0.005" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" size="0.005 0.08 0.04" pos="-0.115 0 0.04" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_far" type="box" size="0.005 0.08 0.04" pos="0.115 0 0.04" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" size="0.12 0.005 0.04" pos="0 0.075 0.04" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" size="0.12 0.005 0.04" pos="0 -0.075 0.04" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="ball" pos="-0.0637 0 0.211">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.025" condim="6" friction="1 0.005 0.0005" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="-0.0637 0 0.211 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches ramp
ball comes to rest in cup
```

---
thinking (summarized):

I'm sketching the physical setup: a tilted ramp with a small ball starting at the top, rolling down under gravity, with the goal of landing it securely inside a cup positioned at the ramp's base so it comes to rest there.

Running through the math, I find steeper angles or longer ramps give the ball too much speed, causing it to overshoot the cup opening—so I need to tune the ramp's length and incline to keep exit velocity low enough, and think about whether the ramp should overhang the cup so the ball drops directly in rather than rolling across the floor.

With a ball radius of 0.025 and cup dimensions of 0.2 x 0.12 with 0.08 high walls, I'm placing the ramp's lower end at the top of the near wall so the ball exits around 1 m/s, flies across, strikes the far wall, and falls to the cup floor—then settles there since it can't climb back over the tall vertical walls.

Since MuJoCo's default contacts only handle sliding friction, a rolling ball would just keep bouncing between walls indefinitely without losing much speed—though the inelastic default contact solver does dissipate some energy per bounce. To guarantee the ball eventually settles, I should add rolling friction by setting condim=6 with a small rolling friction coefficient, which will gradually decelerate the sphere's spin and translation over time.

Checking the math: a rolling friction coefficient around 0.001 gives a deceleration of roughly 0.28 m/s², which combined with the ramp's acceleration of about 1.22 m/s² still leaves a net positive acceleration near 0.94 m/s² down the slope, while being enough to stop a 0.5 m/s rolling ball in the cup within a couple seconds—that seems like a reasonable balance. I'm also considering lowering the ramp angle to around 8° to keep speeds more manageable overall.

Keeping it at 10° for now. I'm checking that the far wall height (0.08m) clears the ball's landing position and top height (0.06m) so it won't hop over, and estimating the vertical landing velocity to confirm MuJoCo's default contact won't produce excessive bounce. I also want to verify the ball doesn't clip the near-wall's top edge as it leaves the ramp, which depends on exactly where the ramp surface terminates.

I'll set the ramp end's x at the near wall's outer x, with ramp surface height at wall top plus 0.015 so the ball clears it comfortably. For the ramp geometry, I'm working out the rotation: tilting 10° about the y-axis so the +x end descends, with the top surface normal tilting accordingly to match the ball's rolling direction.

Now I'm laying out the cup dimensions — floor box, near and far walls, and side walls — positioning them at x=0.5 with the near wall spanning 0.38 to 0.39 and far wall at 0.61 to 0.62, giving an inner cup length around 0.39 for the ball to land in.

Then I'm working out the ramp's center and endpoint coordinates using the angle's sine and cosine, computing where the lower end's top surface meets near the cup wall and projecting the upper end's position from there, along with the bottom corner offset at the lower end.

Checking that corner's position against the wall — at x≈0.3816, z≈0.0754, the ramp bottom corner dips inside the wall top at z=0.08, which would overlap visually even though static geoms don't physically collide. I raise the ramp's lower end top surface to z=0.105, which lifts the bottom corner to about z=0.0854, clearing the wall at that x position, so I shift the ramp center z up by 0.01 accordingly.

I'm considering whether to add a support leg under the ramp's upper end for realism, deciding it's probably unnecessary but sketching out where such a post would sit based on the ramp's slope geometry.

Now I'm computing where to place the ball's starting position, picking a point partway down the ramp's top surface and offsetting it outward by the ball's radius along the surface normal to get the ball's center coordinates.

Then I work out the rolling physics down the ramp—adding rolling resistance to the gravity-driven acceleration—which gives an effective deceleration of about 0.94 m/s², and over the roughly 0.46 m rolling distance that yields an exit speed near 0.93 m/s as it leaves the ramp and begins falling.

From there I check the short airborne arc: dropping about 0.095 m with a small vertical launch velocity, the flight time works out to roughly 0.124 s, carrying the ball about 0.113 m horizontally before it lands safely before the far wall, with enough clearance to avoid collision there. After landing, it rolls toward the wall, bounces, and I estimate rolling friction will bring it to rest within a few seconds, factoring in energy lost at each wall impact, so the total time budget is roughly a second for the ramp phase plus the remaining rolling and bouncing afterward.

Since the cup's rolling friction alone might not stop the ball quickly enough within six seconds, especially if wall collisions don't dissipate much energy, I'm considering tuning the friction parameters separately for the ramp and the cup floor -- giving the cup floor geom a higher rolling friction coefficient so the ball decelerates faster once inside, while keeping the ramp's rolling friction lower so the ball still picks up speed on the way down. Working through the contact friction mixing rules (which take the max of the two contacting surfaces), I estimate a cup floor setting around 0.83 m/s² deceleration, stopping the ball in about a second, while the ramp's combined rolling friction stays low enough to maintain the acceleration needed for a good launch speed.

Now I'm checking the landing trajectory and torsional friction defaults, confirming the ball's vertical landing speed won't cause tunneling through the thin cup floor given the timestep, and thinking through exactly when the ball loses contact with the ramp's edge as it transitions into the air -- tracking the ball's position relative to the wall's inner face and top edge to make sure the geometry lines up correctly for a clean launch.

The cup itself is static with no joint, and the ball uses default sphere density giving it a reasonable mass. For the keyframe, I just need to set the freejoint qpos with zero velocity and let gravity handle the rest. Now I'm setting up the worldbody with the floor, ramp, ramp post, and lighting, naming all the bodies and geoms consistently.

