A tilted box ramp runs down toward +x, and its low end overhangs the inside of a square cup. The ball rolls about 0.6 m down the ramp and drops off the end. It hits the cup's far wall, then stops on the cup floor, which has rolling friction.

```xml
<mujoco model="ramp_ball_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="ramp" type="box" pos="0.0793 0 0.2209" euler="0 15 0" size="0.35 0.08 0.01" friction="1 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_post" type="box" pos="-0.22 0 0.145" size="0.01 0.03 0.145" rgba="0.5 0.3 0.15 1"/>
    <body name="cup" pos="0.5 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.005" size="0.17 0.17 0.005" friction="1 0.01 0.01" condim="6" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.16 0 0.065" size="0.01 0.17 0.055" friction="1 0.01 0.01" condim="6" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_far" type="box" pos="0.16 0 0.065" size="0.01 0.17 0.055" friction="1 0.01 0.01" condim="6" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_left" type="box" pos="0 0.16 0.065" size="0.15 0.01 0.055" friction="1 0.01 0.01" condim="6" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.16 0.065" size="0.15 0.01 0.055" friction="1 0.01 0.01" condim="6" rgba="0.2 0.4 0.8 0.6"/>
    </body>
    <body name="ball" pos="-0.1518 0 0.3253">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" friction="1 0.005 0.0001" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="-0.1518 0 0.3253 1 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches ramp
ball touches cup
ball comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the physical setup: a tilted ramp with a ball rolling down, positioned so it falls off the end directly into a cup placed below, letting gravity carry it to rest within the time limit.

Running the rolling-ball physics, I calculate acceleration and exit velocity for a 20° incline, then check the projectile path to ensure the ball clears the ramp edge and lands inside the cup rather than bouncing out. Since the speed feels a bit high for a clean catch, I consider a shallower 15° angle with shorter travel distance to reduce velocity and improve the odds of the ball landing safely in the cup.

I'm now placing the cup geometry relative to the ramp's exit point, setting wall height and inner radius so the ball clears the near wall but still drops into the bottom, then solving the drop-time equation to get the horizontal distance traveled during the fall and checking it against the wall clearance.

Actually the ramp can overhang the cup wall entirely, so there's no near-wall collision to worry about — I just need the ramp's underside at its end to clear the wall's top height, which works out fine with the ramp thickness and tilt. Then the ball leaves the ramp end, travels a bit further before landing in the cup, hitting the bottom with some horizontal velocity that could carry it into the far wall, so I need to size the cup and its center position accordingly.

I should make the wall taller, maybe 0.10, and raise the cup's inner radius to 0.15 to fit the geometry properly, checking that the ramp's underside clears the wall height. I also realize that with a flat cup bottom and no rolling friction by default in MuJoCo, the ball would just roll forever once it settles there, so I need condim 6 with rolling friction to actually bring it to rest.

I'm estimating that rolling friction (mu_r ≈ 0.002) gives a deceleration around 0.45 m/s², which also slows the ball on the ramp itself, bringing acceleration down from 1.81 to about 1.35 m/s². I'm weighing whether to apply high rolling friction only to the cup bottom while keeping the ramp low-friction, since MuJoCo combines contact friction by taking the max between contacting geoms.

That computes to about 2.3 m/s² deceleration, so the ball stops within roughly 0.6 seconds from 1.3 m/s — reasonable. I'll make the cup a simple square with a bottom box plus four wall boxes, inner half-width 0.15. For the ramp, I'm setting the tilt at 15°, with half-sizes 0.35 length, 0.08 width, 0.01 thickness, rotated about the y-axis.

Positive pitch around y makes the +x end descend, so I'll use euler="0 15 0" to have the ramp slope downward toward +x. I'm working out where the ball sits at the ramp's lower end by placing its center offset from the top surface by the ball radius along the surface normal, then finding the ramp's center position so the +x edge lines up correctly with the cup.

Now I'm sizing the catching cup: setting its center at x=0.5 with inner half-width 0.15, giving inner walls spanning x=0.35 to 0.65, a thin bottom box around z=0.005-0.01, and side walls rising from z=0.01 to about 0.12 with their inner faces at x=±0.15 so the ramp feeds the ball into the cup's opening.

I need to make sure the ramp clears the cup wall top of 0.12 as it passes over x=0.33-0.35 — working out the vertical offset between the ramp's top and bottom surfaces along its 15° tilt, I find the bottom surface clears the wall only if the ramp's end height z_end is at least about 0.125, so I'm checking the end face corner position accordingly.

Setting z_end to 0.14 places the ball's center at roughly (0.428, 0.169) when it leaves the ramp — far enough past the wall. I still need to verify the ball clears the far wall (needs center height above 0.15) during flight, so I'm computing the launch speed from the ramp travel distance (0.6 m along a 0.7 m ramp with energy from gravity along the slope, giving about 1.47 m/s), then breaking that into horizontal and vertical velocity components to trace the trajectory.

Solving the fall equation for when the ball reaches resting height gives a time around 0.128s, translating to a horizontal travel of about 0.18m, landing near x=0.61 — just inside the far wall at 0.65 with the contact point at 0.62. Checking the ball's height as it crosses the wall position confirms it's well below the wall top, so the trajectory clears safely, though I note the speed is close enough to the edge that slowing it slightly would add safety margin.

Friction on the ramp is low enough that the tangent of the slope angle stays small, so the ball rolls without slipping. After hitting the far wall at roughly 1.42 m/s, the soft contact absorbs the impact and the ball bounces back slightly before rolling friction brings it to rest — I check whether it could then strike the underside of the ramp on the rebound, but the clearance there is sufficient since the ball's top sits well below the ramp's underside height at that point.

Now I'm computing the ramp's center point P using the endpoint position plus offsets along the normal and surface direction vectors, working through the normal component (0.01n) and surface component (0.35u) to find the resulting coordinates.

I'm also computing the top end of the ramp similarly, then thinking about whether the ramp needs support posts since it's just a static body floating in the worldbody — I'm sketching out a post geometry under the top end, calculating the ramp's bottom surface height at that x-position using the slope angle to size the post correctly.

Now I'm placing the ball's starting position 0.1 units along the ramp surface from the top, computing the contact point and offsetting by the ball radius along the normal to avoid penetration, with a small extra clearance. I'm reasoning that since the ball only travels in the x-direction down the slope, lateral rails aren't necessary, though I note the ball's radius for mass calculation.

I'm setting up the ball's free joint keyframe with its starting position and identity orientation, with no actuators needed. Then I'm defining the cup body at a fixed position with wall and bottom geoms sized to contain the ball, applying friction and condim settings for rolling contact, and confirming the cup itself needs no joint since it's stationary.

Checking timing: the ball should roll down the ramp in about 0.8 seconds, briefly go airborne for 0.13 seconds, then settle in the cup within a second, coming to rest with speed under 5cm/s. I'll set expectations around the ball touching the ramp and ultimately resting in the cup.

