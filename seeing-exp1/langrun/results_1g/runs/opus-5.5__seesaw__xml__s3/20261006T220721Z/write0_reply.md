The seesaw rests with the ball end on its stop, and a small lip at the end keeps the ball from rolling off. The 1 kg weight starts at rest 2 m up and falls about 1.4 m onto the raised end. The plank then swings to its other stop, which lifts the ball about 0.55 m. When the plank stops, the ball is thrown upward at roughly 3.5–4 m/s.

```xml
<mujoco model="seesaw_launch">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="fulcrum" type="box" pos="0 0 0.13" size="0.05 0.12 0.13" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="seesaw" pos="0 0 0.3" euler="0 0.27 0">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" range="-0.54 0" limited="true" damping="0.01"/>
      <geom name="seesaw_plank" type="box" size="1.0 0.1 0.02" mass="0.5" rgba="0.7 0.5 0.3 1"/>
      <geom name="seesaw_lip" type="box" pos="0.98 0 0.06" size="0.02 0.1 0.04" mass="0.02" rgba="0.5 0.3 0.2 1"/>
    </body>
    <body name="weight" pos="-0.86 0 2.0">
      <freejoint/>
      <geom name="weight" type="sphere" size="0.06" mass="1.0" rgba="0.2 0.2 0.2 1"/>
    </body>
    <body name="ball" pos="0.896 0 0.126">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

```expect
weight touches seesaw
ball rises at least 0.5 m above its start
```

---
thinking (summarized):

I'm working through the physics of a seesaw design: a 1 kg weight dropped from height onto one end needs to launch a 0.1 kg ball at least 0.5 m into the air from the other end, so I'm setting up the collision dynamics with arm lengths and moment of inertia to figure out the energy transfer.

Using a largely inelastic collision model, I calculate the common post-impact velocity shared by both ends, then require it exceed roughly 3.13 m/s (aiming for 4.5 m/s margin) so the ball reaches 0.5 m after the plank's impacting end hits the floor and releases the ball with its upward velocity, factoring in some horizontal motion from the arc of rotation.

Actually I realize the classic setup already gives free height: if the ball starts on the lowered end and the weight drops on the raised end, the plank's rotation alone lifts the ball by roughly 0.6 m before any ballistic flight, so the height requirement is easily met. I need a small lip or notch at that end so the ball doesn't roll off during the tilt before launch, releasing cleanly in a direction perpendicular to the plank once the opposite end strikes the ground.

I'm placing the pivot at x=0, z=0.3 with the hinge along y, using a 2 m plank (0.04 thick, 0.2 wide) with end B initially down and touching the floor and end A raised, then setting up the initial joint angle and range accordingly.

Rather than relying on floor contact, I'll use the hinge's joint limits as stops, computing that the tilt angle hits roughly 0.284 rad before the end would clip through the floor, so setting the range slightly tighter at ±0.27 keeps it safe with the default soft limit stiffness. That also naturally prevents the weighted end from ever reaching the floor.

For the dynamics, I estimate the plank's effective end mass from its moment of inertia (about 0.33 kg) plus the ball's 0.1 kg, then work through a 1 kg weight dropping from ~1.5 m onto end A, giving an impact speed of ~5.4 m/s that reduces to ~3.8 m/s after the inelastic collision. Continuing gravity acceleration afterward, I calculate the opposite end should launch high enough (over 1.2 m combined with the plank's own rise) to have plenty of margin for the task.

Now I'm thinking through the ball's precise placement on the tilted plank at end B, working out local coordinates based on the plank's thickness, tilt angle, and the ball's radius so it sits right at the lip, then converting that into world coordinates.

For the weight at end A, I'm similarly computing its world position by applying the rotation transform to its local plank coordinates.

I'm also thinking through whether to set initial positions via keyframe qpos ordering (hinge, free weight, free ball) or instead bake the seesaw's tilt into the body's initial orientation and adjust the joint range accordingly.

I'll skip the keyframe since gravity naturally settles the plank. For the fulcrum support, I'm making it a visual-only geom with contype and conaffinity set to zero so it doesn't interfere with the plank's tilting collision physics, positioning it just beneath the pivot point.

Once the ball launches, tracing its trajectory shows it moves inward and upward away from the lip, so no collision there. I'm now thinking about how to phrase success conditions for the checker—something like the ball rising a certain height above its start, or the weight touching the seesaw.

