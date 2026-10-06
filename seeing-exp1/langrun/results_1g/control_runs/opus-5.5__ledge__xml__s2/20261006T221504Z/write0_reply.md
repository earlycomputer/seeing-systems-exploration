The ball starts rolling (spin matched to speed) at 1.65 m/s along a 75 cm table, leaves the edge at x = 0, and lands near x ≈ 0.64 m on the floor of a 15 cm-radius bucket centred at x = 0.6 m. The bucket floor has rolling friction (condim 6), so the ball stops there. The table has none, so the ball keeps its speed on the way to the edge.

```xml
<mujoco model="ball_off_table_into_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Table: top surface at z = 0.75, edge at x = 0 -->
    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" size="0.5 0.3 0.02" pos="-0.5 0 0.73" rgba="0.6 0.4 0.2 1" friction="1 0.005 0.0001" condim="3"/>
      <geom name="table_leg1" type="box" size="0.025 0.025 0.355" pos="-0.05 0.25 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" size="0.025 0.025 0.355" pos="-0.05 -0.25 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" size="0.025 0.025 0.355" pos="-0.95 0.25 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" size="0.025 0.025 0.355" pos="-0.95 -0.25 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <!-- Bucket: centre 0.6 m beyond the table edge, inner radius ~0.15 m, rim at 0.25 m -->
    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.16 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall0" type="box" size="0.005 0.044 0.125" pos="0.155 0 0.125" euler="0 0 0" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall1" type="box" size="0.005 0.044 0.125" pos="0.13423 0.0775 0.125" euler="0 0 30" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall2" type="box" size="0.005 0.044 0.125" pos="0.0775 0.13423 0.125" euler="0 0 60" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall3" type="box" size="0.005 0.044 0.125" pos="0 0.155 0.125" euler="0 0 90" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall4" type="box" size="0.005 0.044 0.125" pos="-0.0775 0.13423 0.125" euler="0 0 120" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall5" type="box" size="0.005 0.044 0.125" pos="-0.13423 0.0775 0.125" euler="0 0 150" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall6" type="box" size="0.005 0.044 0.125" pos="-0.155 0 0.125" euler="0 0 180" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall7" type="box" size="0.005 0.044 0.125" pos="-0.13423 -0.0775 0.125" euler="0 0 210" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall8" type="box" size="0.005 0.044 0.125" pos="-0.0775 -0.13423 0.125" euler="0 0 240" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall9" type="box" size="0.005 0.044 0.125" pos="0 -0.155 0.125" euler="0 0 270" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall10" type="box" size="0.005 0.044 0.125" pos="0.0775 -0.13423 0.125" euler="0 0 300" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
      <geom name="bucket_wall11" type="box" size="0.005 0.044 0.125" pos="0.13423 -0.0775 0.125" euler="0 0 330" rgba="0.2 0.4 0.8 1" condim="6" friction="1 0.02 0.02"/>
    </body>

    <!-- Ball: radius 3 cm, resting on the table top -->
    <body name="ball" pos="-0.4 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" rgba="0.9 0.1 0.1 1" friction="1 0.001 0.001" condim="3"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Rolling without slipping: omega_y = v / r = 1.65 / 0.03 = 55 rad/s -->
    <key name="start" qpos="-0.4 0 0.78 1 0 0 0" qvel="1.65 0 0 0 55 0"/>
  </keyframe>
</mujoco>
```

These are hand calculations, not results from running the file:

- **Leaving the edge:** v²/(g r) ≈ 9, which is well above 1. So the ball leaves the edge immediately instead of curling around it.
- **Clearing the near rim:** when the ball's centre is at rim-clearing height (0.28 m), it is at x ≈ 0.53 m. Its near side is then about 5 cm past the inner wall at x = 0.45 m.
- **Landing:** the ball hits the bucket floor (centre at z = 0.05 m) at x ≈ 0.64 m. That is inside the far wall at 0.75 m.
- **Coming to rest:** rolling friction on the bucket floor slows the ball at about 2 m/s². It should be still within about 1–2 s, well inside the 6 s run.

---
thinking (summarized):

I'm setting up the physical scene: a table at 0.75m height, a bucket positioned 0.6m from the edge, and a ball of radius 0.03m that needs to roll off and fall into the bucket, clearing the rim height of around 0.25m.

Working out the launch speed with projectile motion, I get roughly 1.75 m/s. Since the ball leaves the table edge almost immediately given its speed, I don't need to worry about it clinging to the edge. Now I'm figuring out the initial angular velocity so the ball rolls naturally rather than slides, using the relationship between linear and angular velocity for rolling contact, and accounting for how MuJoCo's free joint represents angular velocity in the body's local frame.

Now I'm sizing the bucket itself — inner radius around 0.15 m so the ball center needs to land within a specific range near the rim, and planning the bucket geometry as a ring of boxes approximating a cylinder with walls about 0.25 m tall and 0.01 m thick. I'm tracing the ball's descent trajectory to check it clears the near wall and lands inside rather than hitting the rim.

So landing near the far side then bouncing isn't ideal; aiming for the bottom center around x=0.6 gives better clearance. Testing v=1.65: at rim height the ball clears the near wall by about 4.7cm and lands around x=0.64, leaving reasonable margin before the far wall.

I'm also checking the ball doesn't clip the wall top earlier in flight—at x=0.45 the ball's height still clears the rim fine. For rolling physics, with standard friction the ball should maintain speed across the table without much loss, so v=1.65 corresponds to an angular velocity of about 55. I'm now setting the initial ball height accounting for slight contact penetration from the solver.

Now I need the ball to settle in the bucket within the time limit—given landing speeds (~1.65 horizontal, ~3.8 vertical) and MuJoCo's damped contact response, bouncing should be minimal, but a flat bucket bottom with no rolling friction could let the ball oscillate between walls indefinitely since wall collisions alone won't dissipate enough energy. I'm considering adding rolling friction via a higher condim on the ball or bucket bottom, though that would also slow it unintentionally while crossing the table, so I need to balance where that friction gets applied.

I'll settle on explicit ball friction values so only the bucket's rolling friction matters once it lands inside, and keep the bucket as a static body positioned on the floor rather than free, since tipping isn't needed here.

For the bucket walls, I'm computing the twelve box segments around the cylinder's circumference, getting their size, radial offset, and rotation angle so each one forms a wall segment, then placing them at the right height with the inner faces lining up near the target radius.

Now I'm designing the table: a tabletop box offset to one side plus four leg boxes positioned at the corners so the ball's trajectory stays clear, and I'm setting up the ball's starting position and mass based on its density and radius.

Checking the physics: since v²/(gr) exceeds 1, the ball leaves the edge immediately without rolling further, and the timing works out to roughly 0.24s rolling, 0.4s flight, and under 2s to settle. I'm also double-checking the impact velocity against the floor thickness and timestep to make sure the ball doesn't tunnel through on collision.

Given floor overlap below the bucket bottom, thickening the bottom to 0.02 with its half-height at 0.01 should prevent any penetration issues, and recalculating the landing point gives roughly 0.64m horizontal travel after a 0.73m fall. I'm also verifying the ball doesn't bounce out when it reaches the far wall, checking clearances against wall thickness and per-step displacement, and considering whether critical damping is needed to keep it contained.

Now I'm setting the freejoint keyframe for the ball with its initial position, orientation, and velocity (linear x-velocity plus angular spin), while keeping the bucket fixed and static. I'm also double-checking the ball doesn't clip the rim during its trajectory, then finishing the scene file with lighting, visual polish, and a 3x3x0.1 floor.

