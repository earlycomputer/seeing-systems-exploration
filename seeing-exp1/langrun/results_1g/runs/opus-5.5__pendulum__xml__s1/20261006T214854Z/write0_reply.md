The pendulum starts 60° back and swings down to strike the ball at the bottom of its arc. The ball rolls along the floor, up a short ramp, and drops into a walled cup. The cup's near wall is lower than its other walls and level with the top of the ramp. A little rolling friction on the ball lets it settle inside the cup.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.055 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.006" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="0.5" rgba="0.7 0.2 0.2 1"/>
    </body>

    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" condim="6" friction="0.8 0.005 0.001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp" type="box" pos="0.73227 0 0.02526" euler="0 -13.134 0" size="0.15403 0.08 0.01" rgba="0.6 0.5 0.3 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_near" type="box" pos="0.89 0 0.035" size="0.01 0.12 0.035" rgba="0.3 0.7 0.3 1"/>
      <geom name="cup_far" type="box" pos="1.11 0 0.07" size="0.01 0.12 0.07" rgba="0.3 0.7 0.3 1"/>
      <geom name="cup_left" type="box" pos="1.0 0.11 0.07" size="0.12 0.01 0.07" rgba="0.3 0.7 0.3 1"/>
      <geom name="cup_right" type="box" pos="1.0 -0.11 0.07" size="0.12 0.01 0.07" rgba="0.3 0.7 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.047 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches ramp
ball touches cup
ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the scene geometry and physics setup: placing the ball near the origin, the cup target at x=1.0, and a pendulum pivoting from the negative-x side to strike the ball forward, while considering how MuJoCo's default friction model will let the ball roll and gradually settle.

For the cup design, since the floor can't have a hole, I'm considering a shallow dish with a low near wall and taller far/side walls, or a short ramp leading up into the cup opening -- so the ball can roll over the entry edge but then gets contained once inside, rather than bouncing back out.

Checking flight time off the edge gives roughly 0.11s, so about 0.13m horizontal travel — the ball should land inside the cup against the taller far wall and bounce back without escaping, since MuJoCo's contacts are fairly inelastic anyway. I'm treating the ramp edge itself as the near wall, short enough that the ball can't climb back out once it settles.

I'll keep the ramp as a separate static body rather than folding it into the cup geometry, with the cup made of base and wall geoms — the goal being that the ball visibly comes to rest inside. Rather than relying on a sharp step edge (which risks the sphere bouncing unpredictably on contact), I'll shape the ramp as a tilted box whose top surface smoothly meets the near wall's top edge, going from the base up to height H at the wall.

Working out the specifics: the near wall spans a small thickness at the top, flat at height H, over which the ball rolls before falling into the cup. For the ramp itself, I'm picking a thickness, horizontal run, and height rise to compute the slope angle so the geometry lines up correctly with the wall's position.

Calculating the ramp's length and tilt angle, then positioning the box's center by offsetting from the surface midpoint along the normal direction, and working out the correct rotation sign about the y-axis so the ramp tilts the right way.

The end face of the box dips below the floor but the top corner meets the slope exactly at z=0, so the ball transitions smoothly with just a slight 11° kink. The ramp's top end at 0.90 aligns with the wall's base, so I could even treat the wall as part of the cup structure, with the cup interior starting around x=0.92.

I'm sketching the cup walls: near wall spans x[0.90,0.92] at 0.06 height, far wall at x[1.08,1.10] at 0.12 height, with side walls running the length at y≈±0.08-0.10 and 0.12 height. I'm checking whether the ball clears the near wall edge as it launches off the ramp — it falls about 0.06m over roughly 0.11s before landing, so I need to verify the horizontal distance it covers matches up with the cup's interior.

I'll skip adding a base plate since it'd just complicate collisions—the walls alone define the cup, and it stays static with no joint.

Now for the pendulum: pivot at the top, with a spherical bob at the end that swings down to strike the ball. I'm positioning the bob so its bottom clears the floor by a small margin while still making contact with the ball at the bottom of the arc.

For clean horizontal contact, I'm offsetting the pendulum's resting position horizontally so the bob meets the ball exactly at the swing's lowest point, with the pivot placed high enough to give sufficient arc length. Then I need to figure out the right velocity so the ball ends up rolling at roughly 1.6 m/s after the collision, accounting for the slide-then-roll transition.

I'm uncertain how MuJoCo's contact model will split momentum between bob and ball — it's somewhere between elastic and inelastic depending on damping, so I'm considering making the bob significantly heavier than the ball (say 0.5 kg vs 0.05 kg) to push the ball's post-impact speed closer to the pendulum's full velocity, while also worrying about whether the pendulum swings back and re-hits the ball after it's already moving away.

The harder constraint is that the ball needs enough speed to roll up the ramp (around 1.29 m/s initial) but not so much that it overshoots the far wall (0.12 m tall) when it launches off the ramp's 11° upward slope — since the ramp angle gives the ball some vertical velocity on exit, I need to check whether its resulting arc stays low enough to be blocked rather than flying over.

I'm also worried about the near wall being only equal to the ball's diameter (0.06 m) — the ball can't climb back over a wall exactly its own height without help from spin or bounce, so I might need to raise that wall slightly, say to 0.07, and recompute the required speed accordingly.

Then I'm checking pendulum release conditions to get a bottom speed near 2.0 m/s, propagating that through rolling friction to see the range of speeds at the top of the ramp, and making sure it settles within 6 seconds. The tricky part is that if the ball just rolls back and forth between the cup's walls without losing energy, it could bounce indefinitely — so I need each wall collision to bleed off enough energy that the motion damps out in time.

I'm also considering adding rolling friction to the ball itself, since surface friction alone won't slow a rolling sphere. Estimating the effective linear deceleration from a small rolling friction coefficient to see if it's enough to bring the ball to rest below the 5 cm/s threshold within the time limit.

With a coefficient around 0.001, the extra deceleration is small but sufficient over the typical travel distance, so I'll give the ball condim 6 with friction values covering sliding, torsional, and rolling. I'll also keep MuJoCo's default contact solver settings since they're already fairly inelastic with some bounce. Now I'm working out the release velocity needed from the pendulum swing using energy conservation.

For the geometry, I need to figure out how rotating the pendulum by angle φ about the y-axis moves its hanging direction, computing the rotated position components to determine the correct release orientation.

Swinging down from φ=60° to 0 moves the bob in the +x direction, hitting at the bottom of the arc at roughly quarter-period timing (~0.4s). I'll set the hinge qpos keyframe to 1.047 radians with zero damping, and give the bob sphere an explicit mass of 0.5 (using steel-like density) since the default density makes it too light at only ~0.065 kg.

I set the ball mass to 0.05 kg at radius 0.03, roughly wood-like density, which seems fine. Checking clearances: the bob sits 5mm above the floor plane with no penetration issues given default margins, and after the pendulum strikes the ball and swings through to the other side (~60° reduced amplitude), it rises to about x=0.38, z=0.28, well clear of the ramp starting at x=0.58. Now I'm working out the rod capsule geometry connecting the pivot to the bob.

Good, the ball stays far from the rod so collision isn't an issue, and hitting it along x shouldn't disturb y-motion. Checking the keyframe setup — pendulum hinge angle then ball's free joint position, resting at height 0.03 on the floor, which should settle fine with contact softness. The bob at 60° is far from the ball at rest, so no initial contact there, and now I'm checking the cup wall interior dimensions.

Now I'm working out the ramp geometry: a 30cm run with 7cm rise gives about a 13.1° incline, so I'm computing the surface length, normal vector, and center position/orientation for the ramp box, plus its width to match the near wall. I'm also considering whether the ball might hop slightly at the kink where the ramp meets the flat section given its speed.

Checking the end-face geometry where the ramp meets the near wall, the box slightly pokes into the wall but overlap stays within tolerance. Then I'm estimating the ball's velocity after energy losses from sliding friction and rolling friction over the 0.58 m stretch, tracking how speed decays from roughly 2 m/s down through successive loss terms.

Comparing that remaining speed against what's needed to climb the 0.3 m ramp section (including ramp friction), the margin looks adequate but not huge. I also want a more rigorous worst-case pendulum speed estimate accounting for the rod's mass distribution, so I'm computing the rod's mass from its cylindrical dimensions, then working out the combined moment of inertia of rod and bob and the potential energy drop for a 60-degree swing to pin down the actual speed at the bottom.

Checking the upper-bound elastic case too: even at 4.0 m/s the ball's vertical rise after leaving the slope keeps its center below the far wall's top edge, so it still strikes the wall face rather than clearing it. After bouncing around in the cup the ball should settle from rolling friction, though I should double check whether a rebound off the far wall could send it back into the near wall.

Timing-wise the hit happens near 0.4s, the ramp contact around 0.7s, and the ball lands in the cup by about 1.0s, leaving plenty of margin within the 5s window for it to settle. The pendulum keeps swinging afterward but doesn't interact with anything else, so that's fine.

For the final expectations I'll phrase them simply: the pendulum touches the ball, the ball touches the ramp, and the ball comes to rest in the cup, keeping consistent "X touches Y" and "X comes to rest in Y" phrasing throughout.

Now I'm writing the actual MJCF XML — floor plane, lighting, ball geom with friction and condim settings tuned for rolling contact, and a keyframe defining the starting qpos with zero velocities.

