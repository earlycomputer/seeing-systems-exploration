## What happened

The ram reached block1 at 0.53 s and pushed it 0.25 m. The whole stack slid along with it as a single upright column and stopped at x = 0.25 m, still stacked, with every block's height unchanged. Nothing toppled.

The cause is the ram's speed. It lost speed sharing its momentum with the stack (from 0.40 to about 0.24 m/s), so it shoved the stack instead of striking it sharply. With friction 0.8 between the blocks, block1 dragged the blocks above along as one unit, and the base never accelerated hard enough to tip the column.

## The fix

The fix makes toppling a matter of geometry rather than impact strength:

- **Slippery joint under the stack.** Only the contact between block1 and block2 is made slippery (friction 0.03), using an explicit contact pair plus an exclude for the default contact.
- **Rest of the stack holds together.** The other contacts keep friction 0.8, so blocks 2–5 behave as one tall column.
- **Base slides out.** The ram slides block1 out about 0.15 m. Once block1 has moved more than 0.05 m relative to the blocks above, its trailing edge passes under their centre of mass, and the column must tip over that edge and fall.
- **Ram lowered.** The ram is now 2.5 cm tall at most (5 cm full height, top at 0.06 m) and stops at a joint limit, so it stays clear of the falling blocks.

I haven't run this version.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <camera name="side" pos="0 -1.6 0.5" xyaxes="1 0 0 0 0.3 1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>

    <!-- Ram: slides along +x, low (z 0.01..0.06) so it only hits the bottom block -->
    <body name="ram" pos="-0.30 0 0.035">
      <joint name="ram_slide" type="slide" axis="1 0 0" limited="true" range="0 0.36" damping="1"/>
      <geom name="ram_geom" type="box" size="0.04 0.15 0.025" mass="5" rgba="0.8 0.2 0.2 1" friction="0.8 0.005 0.0001"/>
    </body>

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

  <contact>
    <exclude name="no_default_b1_b2" body1="block1" body2="block2"/>
    <pair name="slippery_b1_b2" geom1="block1_geom" geom2="block2_geom" condim="3" friction="0.03 0.03 0.005 0.0001 0.0001"/>
  </contact>

  <actuator>
    <velocity name="ram_motor" joint="ram_slide" kv="500" ctrllimited="true" ctrlrange="-1 1" forcelimited="true" forcerange="-300 300"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.3  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.3"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The stack stands still until the ram reaches block1 at 0.53 s. The ram then pushes block1 0.25 m, and the entire five-block stack slides along with it as one upright column. It stops at x = 0.25 m, still fully stacked, and stays at rest through 6 s.", "works": false, "problem": "High friction between the blocks and a soft, decelerating push made the whole stack slide as one unit, so it never toppled."}
```

---
thinking (summarized):

The stack slid as one unit instead of toppling—the velocity actuator with its force limit couldn't make the ram impulsive enough, and the soft contact plus high friction kept everything moving together with only gentle acceleration. I need a more robust way to force toppling, maybe by hitting the bottom block harder and briefer.

A cleaner approach is to tip the stack using inertia: the base needs acceleration greater than g times half-width over COM height, roughly 2 m/s² for this geometry. Looking at the velocities again—block1 at 0.27, block5 at 0.41—the stack clearly got accelerated unevenly and then the ram itself slowed from momentum sharing between the 5 kg ram and 2.5 kg stack, landing around 0.27 m/s, while floor friction on the stack only amounts to about 20 N, which isn't enough to counter the force limit pattern I'm seeing.

I'm also considering a different toppling mechanism: rather than relying on whole-stack inertial tipping, I could have the pusher strike the bottom block so it slides out from under the stack above it. If block-block friction is low, block1 slides out while block2 remains supported only until its center of mass passes the shrinking contact edge, at which point blocks 2 through 5 topple forward as a unit even though block1 itself never tips.

I could use an explicit contact pair between block1 and block2 to set low friction specifically for that interface, while relying on the default (high) friction for all other dynamic contacts, since pairs supplement rather than replace the standard collision system. The exclude tag would only matter if I wanted to suppress dynamic contact entirely between those bodies, which isn't needed here since the pair handles it.

Tracing the physics further, the upper stack's small friction-driven acceleration means it keeps slipping relative to block1 since block1 moves faster — so the slip continues building until it exceeds some threshold, at which point the stack loses support and starts to tip.

But then I realize it would tip backward right onto the ram since the ram sits low behind block1's rear face. That's messy geometry-wise, so I'm considering repositioning the pusher so the falling stack doesn't land on it.

Actually, maybe the limited ram travel helps: it only pushes block1 a short distance then stops, while block1 keeps sliding slightly due to momentum before friction decelerates it. The toppled stack landing on the ram's low top surface is probably fine though -- it still achieves the topple, just lands on the ram rather than the floor, which doesn't break the outcome.

Once block1 stops moving, the stack keeps tipping backward since its COM sits behind the pivot edge—inherently unstable, so it falls regardless of edge friction, with block2 possibly sliding along the edge as it goes. The 2-5 block friction of 0.8 should keep them together through the fall, scattering mainly on impact, which matches what I saw in the earlier stability test.

I'm double-checking the ram's travel math against where block1 ends up, to make sure the ram reaches its limit right as block1 is pushed clear and the pivoting stack doesn't re-contact the ram afterward.

Solving for timing, the ram at 0.3 m/s closes the 0.05m gap in roughly 0.18s accounting for deceleration from the mass difference. I'll set friction and contact parameters, then write the keyframe with initial qvel 0.3 and matching ctrl 0.3.

