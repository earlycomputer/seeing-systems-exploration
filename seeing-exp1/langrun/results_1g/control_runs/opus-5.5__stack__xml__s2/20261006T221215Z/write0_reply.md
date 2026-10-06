The stack stands on its own for about half a second. Then a motor-driven ram slides in at 0.4 m/s and shoves only the bottom block. The ram is low enough that it cannot touch the upper blocks, and a joint limit stops it after it has pushed 0.25 m. I have not simulated this file. I expect the collapse from the geometry and the forces involved, but I haven't checked it.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <camera name="side" pos="0 -1.6 0.5" xyaxes="1 0 0 0 0.3 1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>

    <!-- Ram: slides along +x, low enough to hit only the bottom block (z 0.015..0.085) -->
    <body name="ram" pos="-0.30 0 0.05">
      <joint name="ram_slide" type="slide" axis="1 0 0" limited="true" range="0 0.46" damping="1"/>
      <geom name="ram_geom" type="box" size="0.04 0.15 0.035" mass="5" rgba="0.8 0.2 0.2 1" friction="0.8 0.005 0.0001"/>
    </body>

    <!-- Stack of five 10 cm cubes, resting exactly in contact -->
    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" rgba="0.2 0.4 0.8 1" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" rgba="0.2 0.7 0.4 1" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" rgba="0.9 0.7 0.2 1" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" rgba="0.6 0.3 0.8 1" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" rgba="0.9 0.4 0.2 1" friction="0.8 0.005 0.0001"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="ram_motor" joint="ram_slide" kv="200" ctrllimited="true" ctrlrange="-1 1" forcelimited="true" forcerange="-150 150"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.4  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.4"/>
  </keyframe>
</mujoco>
```

What I expect to happen:
- **Before contact:** the blocks start exactly touching, so the stack should stay still. The ram's front face starts 0.21 m from the bottom block, so at 0.4 m/s it arrives at about t ≈ 0.5 s.
- **On contact:** the bottom block jumps to 0.4 m/s almost at once, which is far more than the roughly 2 m/s² that would be enough to tip a 0.5 m-tall, 0.1 m-wide tower. Friction between the blocks (μ = 0.8) can only pass on part of that. So I expect the upper blocks to lag, lose support as the bottom block moves 0.25 m (more than its own 0.1 m width), and topple.
- **Afterwards:** the ram stops at the end of its travel and keeps pressing against the limit, which is harmless. I haven't checked whether every block has come to rest by t = 6 s. The brief doesn't ask for that.

---
thinking (summarized):

I'm designing a scene with a stack of five small cube blocks that stands stable initially, then gets toppled by something striking the bottom block—maybe a sliding ram given an initial velocity or a rolling ball—so the stack falls after the push.

I'm weighing how fast to push the bottom block: too fast and it could shoot out "tablecloth-style" leaving the upper blocks drop straight down without toppling, while a moderate push lets friction drag the second block along and the upper blocks' inertia makes the stack lean and fall over. I'm considering a motor-driven slide actuator moving at a constant moderate speed to push the bottom block steadily, relying on friction to transmit the push upward and cause toppling.

Analyzing the physics further, I figure the rigid tower would rotate backward around its rear-bottom edge when the base is kicked forward, tipping once the acceleration exceeds roughly 0.2g — easily surpassed by an impulsive push, so the stack should topple or scatter either way once the ram continues forward.

Now I'm deciding on actuator specifics: rather than a sharp impulsive hit (which risks ejecting the bottom block like a Jenga trick), a moderate constant-velocity push feels more controlled — a velocity actuator with kv=50, ctrl around 0.4 m/s, ram mass near 5 kg, and a travel limit so it stops after a set distance of contact.

I'm placing the ram 0.2 m away so the stack stands steady for about half a second before contact, with blocks stacked at exact contact heights (0.05, 0.15, etc.) to avoid wobble. For the ram geometry, I'm sizing it so its top sits below the second block's base, ensuring it only strikes the bottom block without touching the ones above.

Working out the slide joint range (0 to 0.46 m) and velocity actuator parameters (kv=200, force limits ±100) so the ram travels 0.21 m to first contact at 0.4 m/s, then pushes another 0.25 m before stopping at the limit — setting the initial keyframe velocity to match and ordering the qpos entries by body sequence in the XML.

Now I'm checking whether the impact at 0.4 m/s could topple the stack: with a stiff velocity servo the ram accelerates block1 almost instantly (~100 m/s²), but friction between block1 and block2 only transmits about 0.8g given the normal force from four blocks stacked above, so block1 should slide out while block2 stays mostly in place rather than getting dragged along.

Movement after collapse isn't critical since it's past the time limit, and the ram pushing against its joint limit is acceptable. I'm setting up collision defaults and finalizing body placements—block positions at origin with identity quaternions, the ram's slide joint range, geometry size, and mass computed from density times volume. Writing the MuJoCo XML file now...

