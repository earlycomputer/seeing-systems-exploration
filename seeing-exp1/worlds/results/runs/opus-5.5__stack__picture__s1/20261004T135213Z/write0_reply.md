The pusher is a heavy paddle on a slide rail. A velocity motor drives it at 1 m/s, and the keyframe sets that control. The paddle crosses an 0.85 m gap, so the stack stands untouched for about the first 0.9 s. A joint limit then stops it after it has shoved the bottom block about 9 cm, which is more than half a block width.

Block-to-block friction is low (0.4), so the bottom block slides out from under the stack faster than friction can drag the upper blocks along. The upper four blocks lose support under their centre of mass, and the friction at their base tips them backward, so they topple.

I have not run this, so the timing and the toppling are estimates.

```xml
<mujoco model="five_block_stack_push">
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.75 0.78 0.8 1"/>
    <material name="block_mat_a" rgba="0.85 0.35 0.25 1"/>
    <material name="block_mat_b" rgba="0.25 0.5 0.85 1"/>
    <material name="pusher_mat" rgba="0.2 0.2 0.2 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" material="floor_mat" friction="0.4 0.005 0.0001"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" material="block_mat_a" density="1000" friction="0.4 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" material="block_mat_b" density="1000" friction="0.4 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" material="block_mat_a" density="1000" friction="0.4 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" material="block_mat_b" density="1000" friction="0.4 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" material="block_mat_a" density="1000" friction="0.4 0.005 0.0001"/>
    </body>

    <body name="pusher" pos="-0.95 0 0.04">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 0.94" damping="0"/>
      <geom name="pusher_head" type="box" size="0.05 0.04 0.025" mass="5" material="pusher_mat" friction="0.4 0.005 0.0001"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="pusher_drive" joint="pusher_slide" kv="500" ctrllimited="true" ctrlrange="-2 2" forcelimited="true" forcerange="-150 150"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="1"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with a stack of five cube blocks that topples when the bottom block gets pushed, including a pusher object driven by velocity. I'm working out block dimensions and mass using a standard density so each 0.1m cube comes to about 1kg, stacking them to roughly half a meter tall.

For the pusher, I'm designing it as a sliding body with a velocity actuator (rather than relying on friction-slowed free motion) positioned above floor contact so it only strikes the bottom block, starting far enough away to delay impact by about a second before knocking the base out from under the stack and causing the upper blocks to topple.

Once block1 slides past half its width, the support region shifts enough that the upper stack's center of mass hangs over the edge, so it tips toward the -x side, falling back toward the pusher rather than staying balanced.

With friction coefficient 0.6 between block2 and block1, the upper stack could get dragged along if the push is too fast, so a slower push speed around 0.3 m/s seems safer to minimize that dragging effect while still letting the stack drop and topple once support is lost.

Checking torque condition: tipping requires mu*h_com > weight*half-width, giving mu>0.25, so the brief 0.05s acceleration window may or may not deliver enough rotational impulse—it's marginal. I'm thinking a more reliable approach is lowering friction so the pusher yanks block1 out from under the stack fast enough that the upper blocks essentially drop rather than tip cleanly.

But full removal risks the stack just landing flat and standing upright again, which defeats the goal. A better design limits the pusher's travel with a joint range—pushing block1 just past half-width (~0.07 m) then stopping, so the upper stack's center of mass ends up outside its remaining support base and topples.

The complication is friction between blocks: if block1 moves too slowly, it just drags the stack along with it instead of sliding free. I'd need either a fast impulsive push or lowered inter-block friction so block1 can slip out from under the stack while the stack stays roughly in place due to inertia.

Accounting for the stack's normal force, friction on block1 is substantial, so once the pusher stops after shifting it 0.08 m, block1 decelerates quickly (~44 m/s² from both floor and block-block friction) and settles almost immediately, needing to think through how the upper stack blocks respond as block1 accelerates during the push.

During the 0.08 s push, friction drags the upper stack along too, but it lags behind block1 (0.016 m vs 0.08 m moved), leaving the stack's center of mass outside block1's support region by about 0.014 m, and the friction-induced torque during acceleration tips it further backward.

The base accelerates forward under friction while the top lags, so the stack rotates toward -x, toward the pusher, confirming the COM shifts to the support's -x side as intended. When it topples it'll land partly on the pusher box and partly on the floor, which still counts as toppled, though I could shrink the pusher's height to avoid that overlap.

Now I'm sizing up the pusher mechanics: a slide joint along x keeps it from falling under gravity, its mass works out to about 0.8 kg, and with kv=100 the velocity actuator could exert up to 100 N if stalled, so I need to check the force needed to overcome friction when pushing against block1.

Running the numbers, friction against block1 needs roughly 35 N, giving about 0.65 m/s steady speed at kv=100, or near 1 m/s at kv=400. I'm worried the resulting time constant (mass/kv) gets too small for stable Euler integration, so I'll either switch to the implicitfast integrator, which handles actuator velocity derivatives properly, or just make the pusher heavier (around 5 kg) and bump kv to 500 for a more reasonable 0.01s time constant.

Now I'm working out the joint range: with the pusher centered at x=-0.95 and a 0.05 half-length, its front face sits at -0.9, while block1's left face is at -0.05, leaving a gap of 0.85. Adding the needed travel of 0.09 past contact gives a total range of about 0.94, so I'll set the joint range to "0 0.94". I also want to cap the actuator force using forcelimited with a forcerange like "-100 100" so it can push against the limit steadily without excessive force, while still comfortably exceeding the ~35 N needed plus acceleration.

With a 100 N cap on a 5 kg pusher, it reaches 1 m/s within about 0.05 s, which is plenty fast. On impact with the 1 kg block, the block should briefly pick up roughly 1.6 m/s depending on contact softness, and it'll keep sliding a bit after the pusher stops, which is fine. The stack itself should be stable since the blocks are placed exactly centered at z = 0.05, 0.15, ..., 0.45 with minimal settling penetration expected.

Now I need to think about qpos ordering — since freejoint qpos values follow body definition order, I should define the blocks before the pusher body to keep the indexing predictable.

Actually, I realize keyframes don't need explicit qpos at all if they default to qpos0, so I can simplify the keyframe to just specify the ctrl value and let positions default automatically. Then I'm double-checking the toppling dynamics — with friction at 0.4 and the push speed at 1 m/s, the block hits near-instantaneous velocity, and the upper stack experiences roughly 3.9 m/s² deceleration from friction, so I need to verify whether that's enough to cause tipping over the push duration.

I work through the displacement math and confirm the center of mass does end up outside the support base, so the stack should topple as blocks shift and pivot around the edge of the block below. I also note I need to make sure all block-floor friction coefficients are consistently set to 0.4 rather than letting the floor default to 1, since contact friction uses the maximum of the two geoms involved.

I set the pusher geometry so its vertical range only overlaps block1, not block2, and define its width before finalizing the setup.

