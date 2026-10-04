The ramp is a 12° tilted box whose low end overhangs a walled cup. The ball starts at rest near the top, rolls about 0.45 m, and leaves the ramp at roughly 1 m/s. It drops into the cup and lands well short of the far wall. Rolling friction, together with the wall collisions, brings it to rest inside the cup within the 6 s. These figures are hand estimates; I haven't run the scene.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <geom name="ramp_deck" type="box" size="0.25 0.06 0.01" pos="-0.3466 0 0.2422" euler="0 12 0" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_support" type="box" size="0.02 0.04 0.14" pos="-0.56 0 0.14" rgba="0.5 0.3 0.15 1"/>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" size="0.18 0.18 0.005" pos="0 0 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_px" type="box" size="0.005 0.18 0.075" pos="0.175 0 0.085" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_nx" type="box" size="0.005 0.18 0.075" pos="-0.175 0 0.085" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_py" type="box" size="0.17 0.005 0.075" pos="0 0.175 0.085" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_ny" type="box" size="0.17 0.005 0.075" pos="0 -0.175 0.085" rgba="0.2 0.4 0.8 0.6"/>
    </body>

    <body name="ball" pos="-0.5339 0 0.324">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" condim="6" friction="0.8 0.005 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="-0.5339 0 0.324 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the physics setup: a tilted ramp feeding a ball onto the floor and into a cup, needing the ball to settle within 6 seconds. I'm weighing designs so the ball doesn't just roll over the cup's wall, considering whether the ramp should end right at the rim or the cup needs to be positioned so gravity naturally funnels the ball in.

I'm working out the rolling-sphere velocity along the incline, the projectile drop off the ramp's edge, and whether a wide low-walled cup or a tall back wall would better catch the ball given its horizontal speed and fall height.

I'm also thinking about how to get the ball to settle rather than bounce indefinitely—using rolling friction coefficients on the ball geom to add a small decelerating torque, or shaping the cup bottom (flat vs V-shaped) so it naturally comes to rest in the middle.

Now I'm laying out concrete dimensions: the cup as a base box plus four wall boxes sized to form an interior of roughly 0.23m square, and a ramp positioned so its lower end overhangs the cup interior at an angle of about 15°, letting the ball roll down and drop in.

I'm checking that the ramp's geometry clears the cup wall at that overhang point, keeping its underside above the wall's rim height so the two static geoms don't improperly intersect.

Working out the ramp's actual tilted box placement: computing the top and bottom edge points along the 20° incline, then finding the surface normal to offset the box center inward by half its thickness so the top face sits exactly on the intended slope.

I'm setting the rotation using a y-axis euler angle of 20° so the box's local x-axis aligns with the downslope direction, with half-extents of 0.25 x 0.06 x 0.01. I'm considering whether side rails are needed to prevent the ball drifting off the track, but since the ball should roll straight with no y-drift, I'll likely skip them for simplicity.

Now I'm computing the ball's starting position by placing it near the upper end of the ramp, offset 0.05m along the slope direction plus the radius along the normal to sit just above the surface, landing around (-0.49, 0, 0.32) with a slight z-bump to avoid overlap. I'm then calculating the rolling dynamics down the 0.45m incline using energy conservation for a rolling sphere, getting an exit speed of about 1.47 m/s, and breaking that into its horizontal and vertical velocity components along the slope direction.

I'm then tracking where the ball leaves the ramp edge and solving the projectile motion equations for its fall into the cup, finding it drops about 0.128m over roughly 0.118 seconds, landing close to the far wall of the cup. Since the landing point nearly collides with the inner wall face, I'm reconsidering the cup dimensions and planning to widen it so the ball actually lands safely inside rather than clipping the edge.

Now recalculating the ramp's high point, midpoint, and ball start position with the new coordinates. The ball lands within the wall bounds, moving horizontally around 1.38 m/s before hitting the far wall. Since MuJoCo's default contact solver is nearly inelastic, the bounce should be minimal, so the ball should continue rolling at roughly that speed afterward.

I'm checking whether the ball's radius keeps it below the wall's height—ball top sits at 0.07 versus wall top at 0.10, so it shouldn't clear the wall under normal rolling. Now I'm considering whether topspin from rolling could cause the ball to climb the wall on impact, since the friction at the contact point with the wall could push the ball upward depending on the direction of its angular velocity.

This could push the jump height to 0.14, close to the wall's 0.10 top, so I'm reconsidering raising the walls and ramp together, but recalculating landing trajectories shows the ball might overshoot a taller 0.16-0.18 wall too. I'm working through the drop and travel distances numerically to see if the landing point clears or hits the wall edge, and it seems I need to reduce the ball's speed or shorten the ramp to keep the landing within bounds.

Testing a shallower 12° angle with a shorter rolling distance, I'm recalculating velocity and trajectory components, then choosing new ramp and wall heights to see if the drop-and-travel math now lands the ball safely past the 0.16 wall top.

I'll widen the cup walls slightly to ±0.175 for extra margin, then check whether the ball's rolling speed is low enough that it won't clear the far wall when it climbs — the math checks out around 1.1 m/s. Now I'm working out the rolling friction decay rate using a condim 6 contact model to estimate how quickly the ball loses speed as it bounces around the cup.

Contact condim resolves to 6 since the ball dominates. I'm also confirming the wall positions at y=±0.175, then working out the ramp geometry — computing the low/high endpoints, midpoint, and center offset along the normal, with euler rotation 0 12 0 and size 0.25 0.06 0.01. From there I'm placing the ball's starting position 0.05 up the ramp from the top edge, offset along the normal by 0.03.

I'm checking clearance near the wall at x=-0.175 against the ramp's top and bottom z-values, confirming it clears the wall height of 0.16 and that the ball's outward flight path isn't obstructed. Then I'm adding a visual support leg under the ramp's upper end, sizing and positioning the box so its top aligns with the ramp's underside at that location.

With geometry settled, the sphere's default density gives the ball a mass of about 0.113 kg, which is fine. For the keyframe, I just need the ball's position and identity quaternion with zero velocities, since it's the only body with degrees of freedom.

