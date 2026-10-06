The ball starts at rest near the top of a 10° ramp and rolls down under gravity. The ramp's low end overhangs the inside of a walled cup. The ball drops in, loses most of its speed hitting the far wall, and rolling friction (condim 6) brings it to rest.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Ramp: 0.5 m long, tilted 10 deg, descending toward +x; low end overhangs the cup interior -->
    <geom name="ramp_board" type="box" size="0.25 0.08 0.01" pos="0.15206 0 0.15356" euler="0 10 0" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_support" type="box" size="0.03 0.06 0.09" pos="-0.06 0 0.09" rgba="0.5 0.35 0.2 1"/>

    <!-- Cup: open box, inner 0.24 x 0.24 m, interior floor at z = 0.02, rim at z = 0.10 -->
    <body name="cup" pos="0.5 0 0">
      <geom name="cup_base" type="box" size="0.14 0.14 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" size="0.01 0.14 0.04" pos="-0.13 0 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_far" type="box" size="0.01 0.14 0.04" pos="0.13 0 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" size="0.12 0.01 0.04" pos="0 0.13 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" size="0.12 0.01 0.04" pos="0 -0.13 0.06" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- Ball: radius 3 cm, with rolling friction so it settles -->
    <body name="ball" pos="-0.0381 0 0.2286">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" condim="6" friction="1 0.005 0.002" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.0381 0 0.2286 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

I haven't run this file. These numbers are estimates. The ball should leave the ramp at about 0.8–1.0 m/s and land near the middle of the cup, about 0.1 m past the ramp's end. It should then stop well within the 6 s, comfortably under the 5 cm/s rest threshold. Simulating it and checking the ball's final speed would confirm this.

---
thinking (summarized):

I'm planning the scene layout: a tilted ramp box with a ball starting at the top, rolling down and off the end, dropping into a cup positioned so it settles inside by the 6-second mark with low speed.

The cup itself could be a flat-bottomed container formed from box walls, but a ball there might roll back and forth indefinitely without rolling friction. I'm considering using condim 6 with rolling friction parameters to damp the motion so it actually comes to rest, and now I'm working out the ball's mass and radius to make sure the physics checks out.

With a 1 m ramp at 20°, the exit velocity is too fast and the ball would overshoot the cup, so I'm recalculating with a shorter 0.6 m ramp at 15°, giving a slower rolling velocity and a more manageable horizontal speed as it leaves the ramp and drops into the cup.

Then I'm working out how far the ball travels before hitting the far wall, and estimating how rolling friction decelerates it afterward — using a rolling resistance coefficient to get a deceleration rate, which suggests the ball would coast to a stop within a few seconds after bouncing inside the cup.

Actually, since wall collisions in MuJoCo are near-critically-damped with low restitution, the ball should lose most of its normal velocity on impact and settle quickly. To make this more robust, I'm considering shallowing the ramp angle to around 10° so the ball arrives at the bottom moving more slowly, around 1.1 m/s instead of 1.4 m/s.

I'm also working out the precise cup geometry — positioning the ramp so the ball rolls over the near wall and drops inside, with the cup's inner half-width, wall thickness, and wall height all sized so the ball comfortably fits and the walls sit flush on the base.

Since both ramp and cup are static bodies, overlapping geoms between them won't generate contact forces, so I don't need to worry about precise clearance there. I'm now tracing the ball's trajectory after it rolls off the ramp edge — leaving at roughly 10° with some speed, falling from about z=0.15 down to landing near z=0.05 inside the cup, a drop of about 0.1m.

Working through the projectile math, the fall takes roughly 0.125 s and the ball travels about 0.135m horizontally, landing safely inside the cup's walls with margin to spare. It'll then hit the far wall at around 1 m/s and likely bounce back slightly, possibly toward the near wall, though the ramp overhang above should keep it contained.

Straight rolling is fine without rails, so I'll skip them and just let gravity start the ball from rest at the top. For the ramp placement, I'm working out the rotation math: a 10° tilt about the y-axis sends the +x end downward, so euler="0 10 0" achieves the descending slope, and I'm computing the resulting top surface normal to confirm the geometry lines up.

Picking the ramp's top end position at x=0.40, z=0.12, I solve backward using the half-length offset along the tilted x-axis and the half-thickness offset along the tilted z-axis to get the box center, landing on roughly (0.152, 0, 0.154).

I'm then computing the opposite (low) end of the ramp, which comes out near x=-0.093, z=0.207, and considering whether the ramp needs a supporting pillar underneath since it would otherwise float. I'm sketching a small vertical box under the low end, checking where the ramp's bottom surface would intersect that pillar's x-position so the support actually touches the ramp.

I decide a slight overlap is fine since the pillar is static and won't interfere with the ball's motion above the ramp. Then I work out a specific starting point for the ball a short distance down the slope from the top, calculating its coordinates along the inclined surface so I can offset the ball center above that point.

I then estimate the ball's physics down the ramp: over a 0.45 m roll with a drop of 0.078 m, I calculate gravity's effective acceleration along the incline reduced by rolling friction losses, arriving at a velocity around 0.8 m/s at the bottom, while double-checking how rolling resistance interacts with MuJoCo's contact model.

Finishing the flight calc gives landing at x≈0.505, close to cup center, with safe margin even at higher speeds up to v=1.1 landing at 0.535. I also need to check the ramp edge geometry — the ball's clearance over the near wall seems fine since the ramp overhang sits above it with enough gap for the ball's radius.

Now I'm setting rolling friction on the ball geom with condim 6 and anisotropic friction values, letting contact combine use the max friction and condim, plus a small torsional component. Default timestep of 0.002 and standard impedance should work fine. I'm adding the keyframe for the ball's starting position and orientation, plus the floor plane, lighting, and finalizing the XML.

