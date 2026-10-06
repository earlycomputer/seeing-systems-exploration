The ball starts near the top of a tilted ramp and rolls about 0.7 m down it. It leaves the low end at about 1.5 m/s, clears the cup's low near wall and lands inside the cup. The tall far wall stops it, and rolling friction on the ball lets it settle on the cup floor well within the 6 s run.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="ramp" type="box" size="0.4 0.08 0.01" pos="0 0 0.213" euler="0 15 0" friction="0.8 0.005 0.005" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_leg" type="box" size="0.02 0.05 0.145" pos="-0.36 0 0.145" rgba="0.5 0.35 0.2 1"/>

    <body name="cup" pos="0.62 0 0">
      <geom name="cup_bottom" type="box" size="0.2 0.13 0.005" pos="0 0 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_near_wall" type="box" size="0.01 0.13 0.03" pos="-0.19 0 0.04" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_far_wall" type="box" size="0.01 0.13 0.095" pos="0.19 0 0.105" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_side_left" type="box" size="0.2 0.01 0.04" pos="0 0.12 0.05" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_side_right" type="box" size="0.2 0.01 0.04" pos="0 -0.12 0.05" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.282 0 0.332">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" condim="6" friction="0.8 0.005 0.005" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.282 0 0.332 1 0 0 0" qvel="0 0 0 0 0 0"/>
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

I'm thinking through the physical setup—a tilted ramp with a ball rolling down into a cup at the bottom, and need to account for the ball's horizontal momentum so it doesn't bounce over the cup's wall instead of settling inside.

I'm sizing the cup interior close to the ball diameter to limit rolling, then calculating ramp drop height and exit velocity using rolling-ball physics—a 0.3m drop gives ~2m/s, too fast, so I'm testing smaller drops like 0.15m. I'm also considering having the ramp feed directly over a low near wall into the cup, balancing ramp height, wall heights, and cup length so the ball's trajectory lands inside rather than overshooting.

For the trajectory, I'm working out fall time and horizontal distance with an exit angle of about 15°, finding the ball should land well within a 0.3m cup, then considering what happens as it rolls into the far wall—losing forward momentum but retaining spin, likely settling with some friction-driven oscillation rather than bouncing out.

I'm estimating rolling friction deceleration using MuJoCo's torque-based model: with a rolling friction coefficient around 0.005, the ball decelerates at roughly 1.17 m/s², which combined with wall collisions should bring it to rest within about 6 seconds, while the steeper slope deceleration from gravity dominates on the ramp itself.

Default contact settings with solref giving damping ratio 1 should mean minimal bounce off the walls, which helps. I'm now working out the ramp geometry — tilting the box 15° about the y-axis, with a half-length of 0.4 m and half-thickness of 0.01 m, positioning its center along the x-axis so the ball descends properly before entering the flat cup region.

I'll skip the low-end leg and just add one support leg near the high end to keep things simple, since static geoms won't cause contact issues anyway. For the ball's starting position, I'm computing its placement along the ramp surface at s=-0.3, converting that to x and z coordinates using the 15-degree incline.

Then I work out the ball center by offsetting from the surface along the normal direction, giving roughly (-0.282, 0, 0.330), and estimate its speed at the bottom using energy conservation over the 0.7m roll distance and corresponding height drop — about 1.59 m/s before accounting for friction losses.

Now I'm tracking the projectile path as the ball leaves the ramp edge, checking its trajectory against the near wall of the cup at x≈0.42-0.44 and confirming it clears the 0.06 wall height comfortably, then setting up the cup geometry itself: a bottom plate from x=0.42 to 0.82, a near wall around x=0.42-0.44, and a far wall near x=0.80-0.82.

Solving for when the ball's center drops to resting height inside the cup, I get t≈0.113s and a landing x≈0.568, which falls nicely within the cup's interior bounds. The vertical speed on impact is around 1.52 m/s, soft enough to avoid a significant bounce, and after landing the ball should roll toward the far wall at roughly 1.4 m/s before friction (deceleration ~1.17 m/s²) brings it to rest in time. I'm also setting the side walls at y≈±0.12 to keep the ball contained laterally.

Now I'm defining the cup geometry: a static body placed at x=0.62, with a bottom box and near/far walls sized so the walls clear the ball's resting height with a few centimeters of margin, making sure the near wall doesn't collide with the ball mid-flight.

I'm also setting up side rails at y=±0.12 to contain the ball since it rolls straight with no lateral perturbation needed. For the keyframe, I'm computing the initial qpos by placing the ball's center at the correct normal distance above the ramp surface plane, using the surface center point to derive the exact offset.

Working through the geometry: with the box center at (0,0,0.213) and normal vector (0.2588,0,0.9659), I calculate the surface plane equation and verify the ball center at (-0.282,0,0.332) sits at a normal distance of 0.032 from the surface — giving a 2mm gap above the 0.03 radius, which looks correct. Now I'm checking the ramp's low end by computing where the top edge lands using the along-axis direction (0.9659,0,-0.2588) from the box center.

For the high-end support leg, I'm sizing it to reach up to where the ramp bottom sits near x=-0.38 (roughly z=0.30), using a leg box of size "0.02 0.05 0.145" positioned at "-0.36 0 0.145" — a small gap there is acceptable since the ramp geometry doesn't carry physical density. I'm also setting the ball's mass from its radius and density (about 0.113 kg) and defining its friction properties, considering whether to add torsional friction via a higher condim.

For success conditions, I'll keep it simple: the ball touches the ramp first, then ends up at rest in the cup.

