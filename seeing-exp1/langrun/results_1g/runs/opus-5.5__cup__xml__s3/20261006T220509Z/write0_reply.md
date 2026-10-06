The ball starts at rest on a 15° ramp and rolls about 0.3 m. It leaves the low end at roughly 1 m/s and drops over the near wall into an octagonal cup. The cup's geoms have rolling friction, so the ball stops rolling around inside.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="ramp" type="box" size="0.18 0.06 0.01" pos="0 0 0.1669" euler="0 15 0" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_leg" type="box" size="0.01 0.04 0.0915" pos="-0.10 0 0.0915" rgba="0.5 0.3 0.15 1"/>

    <body name="ball" pos="-0.1081 0 0.2269">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.02" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="cup" pos="0.30 0 0">
      <geom name="cup_bottom" type="cylinder" size="0.09 0.005" pos="0 0 0.005" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall0" type="box" size="0.005 0.037 0.04" pos="0.085 0 0.04" euler="0 0 0" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall1" type="box" size="0.005 0.037 0.04" pos="0.0601 0.0601 0.04" euler="0 0 45" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall2" type="box" size="0.005 0.037 0.04" pos="0 0.085 0.04" euler="0 0 90" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall3" type="box" size="0.005 0.037 0.04" pos="-0.0601 0.0601 0.04" euler="0 0 135" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall4" type="box" size="0.005 0.037 0.04" pos="-0.085 0 0.04" euler="0 0 180" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall5" type="box" size="0.005 0.037 0.04" pos="-0.0601 -0.0601 0.04" euler="0 0 225" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall6" type="box" size="0.005 0.037 0.04" pos="0 -0.085 0.04" euler="0 0 270" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
      <geom name="cup_wall7" type="box" size="0.005 0.037 0.04" pos="0.0601 -0.0601 0.04" euler="0 0 315" condim="6" friction="1 0.005 0.005" rgba="0.2 0.4 0.9 1"/>
    </body>
  </worldbody>
</mujoco>
```

```expect
ball touches ramp
ball touches cup
ball comes to rest in cup
```

---
thinking (summarized):

I'm planning the scene layout: a tilted ramp leading down into a cup built from a base and surrounding wall pieces, designed so the ball rolls off the ramp, falls into the cup, and settles to rest by the 6 second mark.

I'm working through the physics—calculating acceleration from gravity and ramp angle, rolling distance, resulting exit velocity, and the trajectory as the ball leaves the ramp edge and falls toward the cup's interior, tuning the angle and ramp length so the ball doesn't fly out past the cup walls.

Then I realize an issue: without rolling friction specified, a sphere resting on a flat surface inside the cup would just keep rolling forever rather than settling, so contacts and damping need some consideration to make the ball actually stop realistically.

That would also slow the ball on the ramp, but applying rolling friction only to the cup geoms (condim 6, higher rolling coefficient) while keeping ball/ramp/floor at default condim 3 solves this nicely—contacts combine by max, so the cup gets strong rolling resistance to stop the ball quickly while ramp motion stays fast.

For the ramp geometry, I need to orient the box so it slopes downward in +x: rotating about the y-axis by +15° maps the x-axis toward (cos15, 0, -sin15), so euler="0 15 0" gives the correct descending direction. With friction coefficient 1 the ball won't slide on the 15° incline—it'll roll properly from rest.

Now I'm solving for the ramp's center height so the low end of the top surface sits at z=0.13, working out zc from the box's half-dimensions and rotation trig, then computing the x-coordinates of both the low and high ends of the top surface.

Then I place the ball 0.2m back from the top along the slope, offset perpendicular to the surface by its radius plus clearance, giving a ball center around (−0.185, 0, 0.266). With 0.45m of travel distance remaining and gravity component 1.81, I compute the final velocity as roughly 1.28 m/s.

So ball position becomes roughly (−0.108, 0, 0.227), and I'm tracking the velocity components as the ball exits the ramp at the low end, computing where its center sits relative to the edge using the surface normal offset, and confirming the ramp geometry can stay static in the worldbody.

I also need a support leg under the ramp so it doesn't float—placing it near the high end around x=−0.10 without blocking the ball's path, and computing the ramp's bottom surface height there using the slope's tangent and normal offset so the leg's top aligns correctly.

Now I'm sizing the cup: a thin bottom cylinder (radius 0.09, half-height 0.005) sitting on the floor with its top at z=0.01, so the ball needs to land at center z≈0.03. I'm computing the fall time from release height to that landing point using the drop equation with initial downward velocity, solving the quadratic for t.

I'm checking the trajectory to make sure the ball clears the near wall of the cup — placing the cup center around x=0.30, computing the ball's position and height when it passes over the near wall at x≈0.24, and verifying the wall height stays below the ball's path at that point.

I'm also confirming the far wall geometry: wall thickness, heights (0 to 0.07), and whether the ball, after landing around x=0.313 with some residual forward velocity, might roll into the far wall at inner radius 0.38 and whether it could climb the vertical wall surface given the contact normal is horizontal.

Given critically-damped contact (solref with dampratio 1), the bounce on landing is minimal despite a vertical velocity of about -1.55 m/s, so the ball settles quickly via rolling friction. I'm considering bumping wall height up to 0.09 for extra safety margin, and double-checking the ball's clearance over the near wall as its center passes through x≈0.21-0.22.

I'm computing the octagonal wall box arrangement around the circle, sizing each segment's thickness and height to form a ring, then positioning the cup body separately at its own static location.

For the cup geoms I'm adding rolling friction parameters (condim 6, custom friction values) so the ball doesn't slide unrealistically when it lands, and confirming the ball's mass from its density and radius works out fine with a freejoint and initial body position, skipping a keyframe since it's not needed.

Checking the floor plane size and making sure the ball doesn't penetrate the ramp at the start, plus confirming the contact sequence should produce "ball touches ramp" followed by the ball settling in the cup within the 6 second simulation.

