The ramp is a 10° tilted box whose lower end sits just above the near wall of an open box cup. The ball starts at rest near the top and gravity rolls it down. It leaves the ramp at about 0.8 m/s, drops roughly 13 cm and lands about 12 cm inside the cup. Rolling friction on the ball (`condim="6"`, rolling coefficient 0.002) and impacts with the cup walls should bring it under 5 cm/s well before 6 s. These figures are hand calculations; I haven't run the simulation.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp_body" pos="0 0 0">
      <geom name="ramp" type="box" pos="-0.2479 0 0.1736" euler="0 10 0" size="0.25 0.1 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="ramp_support_high" type="box" pos="-0.45 0 0.1" size="0.02 0.08 0.1" rgba="0.5 0.35 0.2 1"/>
      <geom name="ramp_support_low" type="box" pos="-0.12 0 0.075" size="0.02 0.08 0.075" rgba="0.5 0.35 0.2 1"/>
    </body>

    <body name="cup" pos="0.19 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.005" size="0.22 0.22 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.21 0 0.06" size="0.01 0.22 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_far" type="box" pos="0.21 0 0.06" size="0.01 0.22 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.21 0.06" size="0.2 0.01 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.21 0.06" size="0.2 0.01 0.06" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.438 0 0.249">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="2000" condim="6" friction="1 0.005 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.438 0 0.249 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through the physical setup: a ball starting atop a tilted ramp needs to roll down and land settled in a cup by t=6s. Since a cup's walls would block a ball rolling along the floor, it makes more sense to have the ramp end elevated above the cup so the ball rolls off and falls directly in.

I'll need to account for bouncing and residual rolling once inside the cup — contacts in MuJoCo are mostly inelastic, but without rolling friction the ball could oscillate back and forth off the walls. Adding rolling friction via condim and friction parameters on the ball should help it settle within the remaining time, rather than relying on artificial damping.

Now I'm working out the ramp geometry — a tilted box at roughly 15°, a meter long, positioned so its lower end sits just above the cup rim, with the ball launching off the end and dropping into the cup. I want to avoid recessing the cup below the floor, so instead I'm computing the fall height and resulting velocity from the ramp's drop to make sure the ball lands reliably inside rather than overshooting.

Fall time near 0.135s gives about 0.14m horizontal travel, so I need to check ball clearance over the near wall carefully — computing drop versus wall height to make sure the trajectory clears it before landing in the cup. I'll simplify by placing the near wall thin and positioned right at the ramp's end to avoid the clearance issue entirely.

MuJoCo should skip collisions between two static bodies anyway, so it's fine either way. After the ramp, the ball arcs into the cup, landing roughly 0.14 m in with modest horizontal speed, likely bouncing off a wall with the default soft contact damping before rolling friction decelerates it to a stop well within the 6-second window.

I'm worried the wall might not be tall enough to contain a bouncing or spinning ball — with wall height 0.07 barely above the ball's diameter of 0.06, topspin could let it climb over. I'll increase the wall height to 0.12 and raise the ramp end accordingly, recalculating the drop and flight time with the new geometry.

Now I'm checking the rolling friction on the ramp: with mu_roll near zero the deceleration is small, but I need to verify the torque balance so the ball actually rolls without slipping down the 10° slope rather than sliding.

Landing speed off the ramp near 0.84 m/s gives roughly 1.7 s to settle in the cup, plus about 1.1 s on the ramp, totaling roughly 3 s with good margin. I'm fairly confident MuJoCo's rolling friction via soft contacts will dissipate energy reasonably well, and whether the ball rolls or slides on landing shouldn't matter much since friction handles it either way. One lingering concern is making sure the ball doesn't roll off the ramp's edge where it meets the cup.

Now I'm working out the exact geometry: tilting the ramp by 10° about the y-axis so its lower end sits right at the cup's rim height of 0.14, computing the rotated surface normal and the position of the ramp's lower edge so everything lines up properly.

I'll add a static support box beneath the ramp's upper end, sized and positioned so its top stays just below the ramp surface, avoiding interference with the ball's path. Since the ball starts centered and the setup is symmetric, side rails shouldn't be necessary.

Now I'm computing the ball's starting position by offsetting slightly down the ramp slope and outward along its normal from the upper edge, then figuring the cup's placement and interior dimensions so its near wall sits just past the ramp's lower end.

Good, that's fine. Now checking the flight after exiting the ramp: with exit speed around 0.84 m/s at 10° below horizontal, I compute the fall time to reach the lower surface and get a horizontal travel of about 0.12 m, landing well within the interior before rolling further toward the far wall.

Now I'm working out the cup's geometry — bottom box dimensions and position, wall thicknesses and heights, placing near/far/side walls relative to a cup body centered around x=0.19 so everything lines up consistently.

Since it's just a box-shaped container rather than a curved bowl, that's fine for "resting in a cup." For the ball-cup interaction, I need to set appropriate friction and contact dimensionality so contacts resolve properly, defaulting to the stricter combination of the two geoms' properties.

Thinking through the rolling physics: after the ball hits the far wall at roughly 0.75 m/s, topspin keeps it pressed against the wall briefly before it rolls back, decelerating until it settles below the velocity threshold within about 1.7 seconds — consistent with rolling friction behavior in this engine. Now I'm setting up the initial keyframe position for the ball's starting pose.

