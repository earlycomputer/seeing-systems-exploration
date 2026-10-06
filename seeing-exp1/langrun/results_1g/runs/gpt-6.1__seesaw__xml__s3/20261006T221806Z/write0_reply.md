The seesaw is passive: gravity drops the 1 kg weight onto its left end, launching the 100 g ball from the right. The lightweight beam and limited hinge travel are designed to produce a rise exceeding 50 cm.

```xml
<mujoco model="gravity_seesaw_launcher">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
  <size njmax="1000" nconmax="200"/>

  <worldbody>
    <light name="overhead_light" pos="0 -3 5" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.25 0.28 0.32 1" friction="0.8 0.005 0.0001" solref="0.006 1" solimp="0.98 0.99 0.001"/>

    <body name="support" pos="0 0 0">
      <geom name="support_base" type="box" pos="0 0 0.05" size="0.25 0.3 0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>
      <geom name="support_column" type="box" pos="0 0 0.3" size="0.055 0.12 0.25" contype="0" conaffinity="0" rgba="0.4 0.4 0.45 1"/>
      <geom name="support_axle" type="cylinder" pos="0 0 0.6" quat="0.70710678 0.70710678 0 0" size="0.045 0.22" contype="0" conaffinity="0" rgba="0.15 0.15 0.18 1"/>
    </body>

    <body name="seesaw" pos="0 0 0.6">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" limited="true" range="-28 0" damping="0.02" armature="0.001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.001"/>
      <geom name="seesaw_beam" type="box" size="1 0.16 0.025" mass="0.12" rgba="0.85 0.55 0.18 1" friction="0.35 0.002 0.0001" condim="3" solref="0.004 1" solimp="0.98 0.99 0.001"/>
    </body>

    <body name="weight" pos="-0.8 0 2.2">
      <freejoint name="weight_free"/>
      <geom name="weight_sphere" type="sphere" size="0.14" mass="1" rgba="0.25 0.3 0.8 1" friction="0.35 0.002 0.0001" condim="3" solref="0.004 1" solimp="0.98 0.99 0.001"/>
    </body>

    <body name="ball" pos="0.8 0 0.705">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.08" mass="0.1" rgba="0.9 0.15 0.12 1" friction="0.25 0.002 0.0001" condim="3" solref="0.004 1" solimp="0.98 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 -0.8 0 2.2 1 0 0 0 0.8 0 0.705 1 0 0 0" qvel="0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
weight touches seesaw
ball touches seesaw
seesaw reaches its lower stop
ball touches floor
```

---
thinking (summarized):

**Designing the seesaw dynamics**

I need to design a physical seesaw that launches a 0.1 kg weight at least 0.5 meters high when dropping a 1 kg weight. Unfortunately, the necessary tools aren’t available, so I’ll calculate the dynamics manually. The seesaw will have a flat lever hinge, with one side heavy and the other light for upward launch. I’m estimating the impact velocity and considering the beam mass and moment for effective results. It's crucial that the light weight gets an initial upward velocity upon impact.

**Analyzing seesaw motion**

The seesaw's right end goes up at approximately 4.5 m/s before decelerating. The heavy weight accelerates downwards while increasing upward speeds until separating from contact. When the heavy weight stops, its angle is around -25 degrees, and the light weight launches at about 4 m/s at a significant angle. I need to manage the negative angle direction as heavy torque negatively affects the seesaw's movement. The heavy weight drops from a height of 1.335 meters, leading to possible sliding at the left end.

**Evaluating seesaw dynamics**

I’m considering the seesaw's height and mass configurations to achieve optimal launch conditions. With a lever arm mass of 0.1, I estimate a moment of around 0.05. The box dimensions and mass suggest an effective setup, aiming for an ideal ball launch height of at least 0.99m. The hinge's stop position can increase launch height, leading to a robust design overall. However, I realize finite contacts can impact the beam's rotation and leftward acceleration, especially with the heavy weight's energy dynamics.

**Clarifying expectations for height checks**

I need to clarify the expectations for height checks. It seems unclear, but I can express it as “the ball rises at least 0.5 m above its starting height.” The examples mention various forms, like “the ball touches the ramp” or “the ball drops through,” which suggests limitations on what can be stated. I wonder if I could build a target hoop 0.5 m above the starting height and design simple lever systems without extra complexity.

**Ensuring ball mechanics and setup**

I need to ensure that the thrown ball starts at rest. The initial frame might involve gravity affecting the ball on the left. The ball's load on the right tends to rotate positively at the upper limit, while a heavy drop under contact triggers a negative effect. The initial ball position is at x=0.8, just above the floor. I’m considering naming the bodies and geometric shapes used, like calling the stand “support.” I need to account for counterweights to maintain balance, and the hinge settings need adjustments to ensure smooth operation.

**Adjusting contact and friction settings**

I need to ensure a stiff and sufficient time step is allowed with the contact settings. I should set the solver's reflectivity to 0.004 for smooth interactions. It seems that default global classes might need to be avoided entirely. For each geometric shape, I can set the friction values as "0.5, 0.005, 0.0001." I must be cautious with the beam properties to avoid overly bouncy reactions; a small contact softness should be safe for handling larger impacts, around 5.

**Evaluating ball dynamics**

I'm analyzing a scenario where a ball touches the floor and the expectations around its motion. It might peak at about 1.8 seconds and hit the floor heavily. The goal here isn't just for the ball to come to rest on the floor, but it could keep rolling due to friction. I need to clarify that the ball should rise at least 0.5 meters above its starting height, but I can’t create additional markers since the existing expectations are sufficient.