This scene has no keyframe, so it starts at rest and gravity drives everything. I worked out the geometry by hand and haven't run it, so the toppling and catching margins are estimates.

- **Ramp and ball1:** ball1 sits 1 m along a 5° ramp. It should reach the floor at about 1.1 m/s and hit `d1` above its centre of mass, so the domino tips forward.
- **Dominoes:** they are spaced 7 cm apart and are 10 cm tall, so each falling domino reaches the next. Ball1 is too slow to climb over the pile, so it should stay behind it.
- **Ball2:** it sits on a small fixed `stand`, an extra fixed body not in the brief. `d3` should push it off the stand before `d3` comes to rest leaning on the stand's corner.
- **Cup:** ball2 drops over the cup's low near wall into a walled box with a tall far wall. Rolling friction on ball2 should bring it to rest.

```xml
<mujoco model="ramp_domino_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="light_main" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.5994 0 0.0324" euler="0 5 0">
      <geom name="ramp_slab" type="box" size="0.6 0.15 0.02" friction="0.8 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball1" pos="-0.9901 0 0.1569">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.07" density="300" condim="6" friction="0.8 0.005 0.0005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="d1" pos="0.30 0 0.05">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>

    <body name="d2" pos="0.37 0 0.05">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.5 0.9 1"/>
    </body>

    <body name="d3" pos="0.44 0 0.05">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.04 0.05" density="650" friction="0.8 0.005 0.0001" rgba="0.2 0.8 0.9 1"/>
    </body>

    <body name="stand" pos="0.50 0 0.025">
      <geom name="stand_block" type="box" size="0.03 0.04 0.025" friction="0.8 0.005 0.0001" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="ball2" pos="0.50 0 0.075">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" density="1000" condim="6" friction="0.8 0.005 0.002" rgba="0.1 0.8 0.1 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" size="0.08 0.08 0.003" pos="0.61 0 0.003" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_near" type="box" size="0.005 0.08 0.012" pos="0.535 0 0.018" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_far" type="box" size="0.005 0.08 0.05" pos="0.685 0 0.056" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_left" type="box" size="0.08 0.005 0.03" pos="0.61 0.075 0.036" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_wall_right" type="box" size="0.08 0.005 0.03" pos="0.61 -0.075 0.036" friction="0.8 0.005 0.002" rgba="0.9 0.7 0.1 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm setting up the physical scene: a ramp inclined around 20°, with a ball starting 1 m along its surface, which I'm using to compute its height and rolling speed at the bottom using solid-sphere rolling dynamics.

Working out the ramp box's rotation and position...

I'm checking that the box's bottom corner near the low end doesn't poke above the floor past x=0, confirming the geometry is clean. Now I'm positioning the first ball a meter up the ramp's surface to find its contact point coordinates.

Then I'm sizing up the dominoes and ball mass — picking wood density for the dominoes giving around 0.15 kg each, and steel density for the ball giving roughly 2 kg, though I'm realizing that's likely too heavy for the setup to work properly.

The bigger issue is impact height: I need the ball to strike above the domino's center of mass so it topples forward instead of just kicking the base out and sliding. I'm reconsidering the ball radius and domino dimensions so the contact point lands safely above the domino's COM — maybe shrinking the domino height to 0.1 with a 0.05 half-height, paired with a slightly larger ball radius around 0.06.

Also, the ramp speed matters a lot here — at 2 m/s the first domino could fly off violently, which might disrupt the chain reaction with d2 and d3. I'm testing lower ramp angles like 10° and 8° to get calmer impact velocities (~1.4-1.56 m/s) while still following the "1 m up the ramp" requirement, and considering using a taller, heavier domino as the target instead.

Then the chain continues with the third domino knocking the second ball toward the cup — I need to think about whether the ball needs to clear a rim, or whether a low-profile cup or pedestal setup would make the final shot more reliable.

Maybe an elevated setup instead: put the ball on a shelf that the domino knocks off, letting it fall into the cup below where the walls catch it—gravity does the damping work for me. That needs an extra shelf body, which should be fine as long as each body and geom gets its own name. A sunken cup below the floor plane isn't feasible since the floor can't have holes, so a shelf-and-drop approach seems more robust than trying to stop a rolling ball with walls alone.

Without rolling resistance a ball would just roll forever on a flat floor, so I should give ball2 condim 6 with rolling friction to make it settle below the 5 cm/s threshold. The deep-cup approach seems more robust: the ball falls off the shelf with some horizontal kick, bounces inside the cup walls with low restitution, and rolling friction brings it to rest — I need to work out the cup wall height and fall height to keep speeds in range.

Checking timing more carefully: the ball's center drops only 0.03m by the time it would reach the far wall, and at 2 m/s it only travels 0.16m horizontally within that fall—well short of the 0.3m wall, so it clears fine. I should keep ball2's speed from the domino around 1 m/s max, though I also need to confirm whether the second domino sits on the shelf itself or the floor to make the height reachable.

Maybe simpler: put the whole domino chain and ball2 on the floor, with ball2 sitting on a short pedestal so the falling domino's top edge strikes it at the right height as it tips over its pivot edge.

I'm second-guessing the cup geometry — maybe simpler to make the cup's base the floor itself with a thin plate, or just have ball2 roll into it along the floor rather than fall from height. Let me reconsider a cleaner setup: ball2 resting on a pedestal shelf while the dominoes stay on the floor.

Now I'm sizing the dominoes and ball1 so the impact point lands above the ball's center of mass, then checking masses with reasonable densities — ball1 ends up much heavier than a domino, so it'll knock the first domino hard enough to topple the chain.

I worry about launching d1 clear over d2, so I try shallowing the ramp angle to slow the ball down, then consider lightening the ball's density instead and checking the minimum speed needed to tip a domino given its thickness and height.

Even so, the ball will likely carry excess momentum after knocking d1, sending that domino flying and risking the ball plowing straight through to hit d2 itself rather than letting the chain reaction unfold properly. I think I need to slow ball1 further, maybe with a flat runout section that relies on rolling friction to bleed off speed before contact.

Actually the speed probably isn't an issue in practice — domino chains work fine with fast-moving balls since d1 just leans into d2 if spacing is tight relative to domino height. I'll set domino spacing to about 0.07 m with 0.12 m tall dominoes so d1 contacts d2 as it rotates forward.

My bigger concern now is whether ball1 could roll past the fallen dominoes and collide with ball2 or the pedestal directly, since its radius (0.07) is large enough to roll over the thin fallen dominoes (0.02 thick) and potentially strike the pedestal's side wall, given the pedestal height is around 0.08.

Since the step height exceeds the ball's radius, ball1 physically can't climb up and over the pedestal, so it's safely blocked there, though I should consider whether rolling friction over the fallen pile leaves enough energy to matter. Now I'm pinning down exact sizes: setting the ramp base at x=0 and working out domino half-extents (thickness 0.02, width 0.08, height 0.10) alongside ball radii to make the collision geometry concrete.

I bump ball1's radius to 0.07 so its contact point lands around 70% of the domino's height, giving a solid torque above the center of mass for tipping. Then I lay out the dominoes along the flat section after the ramp: d1 at x=0.30, d2 at x=0.37, d3 at x=0.44, with roughly 0.05 gaps between faces so each falling domino's top edge should strike the next one at an angle as it topples.

Now I'm working out the geometry for the pedestal stage — d3 pivots at its front-bottom edge around x=0.45, and I need the pedestal's front face positioned so d3's falling top can sweep onto it without the pedestal being too tall to block the fall. I'm setting up the math for ball2 sitting on top of the pedestal, computing where its center lands relative to the rotating face of d3 as it pivots, so I can find the angle at which d3's face line comes into contact with the ball.

Checking the corner angle, xp=0.47 gives φ≈21.8°, confirming contact at 17.5° happens first. The pedestal spans 0.47–0.53 with the ball centered at 0.50, resting flat on top since a sphere on a plane is neutrally stable there.

D3 nudges the ball as it tips, giving it some rolling speed before it rolls off the far edge at x=0.53 and drops toward the cup below. I'm thinking the cup's near wall could actually be formed by the pedestal itself, with the ball's drop height working out so it clears the wall and lands inside.

Actually I should make the cup self-contained with its own four walls rather than relying on the pedestal as one wall, since the checker likely verifies the ball's position within the cup's bounds. I'll place a near wall right at the pedestal edge, low enough that the ball clears it as it rolls off with its forward momentum.

I wonder if lowering the near wall to 0.02 would even matter, since the ball's low speed and the pedestal behind it would block it anyway. Maybe I should just fold the pedestal into the cup body itself as one of its geoms, since the cup is defined as a fixed body where all geoms belong together.

I'll keep the pedestal as its own separate "stand" body for clarity, and set the cup's near wall height to 0.03. Now I'm working out the exact cup dimensions: base plate, interior bounds, and wall positions with their half-extents and centers for near, far, and side walls.

Once the ball drops into the cup it'll have both horizontal motion and falling speed, bouncing with MuJoCo's default dissipative contacts before settling into a roll. I'm checking how the rolling friction coefficient translates into a deceleration torque so the ball eventually comes to rest inside the cup rather than rolling out.

Working through the numbers, a rolling friction coefficient around 0.002 gives a deceleration of roughly 0.28 m/s², enough to stop a 0.3 m/s ball within about a second — that seems right for ball2. For ball1 on the floor/ramp, an even smaller rolling friction of 0.0005 only decelerates it about 0.05 m/s², which is negligible but fine. I'm also confirming ball2 sits stably on the flat pedestal top before anything else arrives, and that d3 leans against the pedestal corner at roughly a 22° angle once it falls, just ahead of ball2 — now moving on to work out ball1's dynamics with d1.

Trying a 6° ramp angle: with sin≈0.1045, the ball reaches the bottom at about 1.21 m/s after roughly 1.65 seconds, treating the ball's starting position as 1 m up along the ramp. I'm noting the ball's radius causes a slight pivot where the ramp meets the floor, which should be a minor effect. I'm leaning toward a lighter ball1 (around 0.575 kg at density 400) to keep the collision less violent, with dominoes around 0.02 kg at density 650.

I'm tracing the chain reaction: the domino weighs about 0.104 kg, far lighter than the ball hitting it at roughly 1.2 m/s, causing the contact point to move about 2 m/s and the first domino to tip forward hard into the second, which topples the third, which then strikes ball2 forcefully — possibly launching it past 1 m/s. I'm then working through ball2's short flight off the pedestal (0.05 m high, 1.5 m/s) down to the cup's base, estimating a 0.044 m drop over about 0.095 s, landing roughly 0.14 m forward from a start near x=0.53.

Checking whether ball2 clears or hits the far wall: at faster speeds like 3 m/s, the ball's trajectory still keeps its center below the wall's top even with a short flight time, so a 0.08–0.10 m wall height should safely catch it. I'm also considering whether reducing the ramp angle to around 4° would soften the whole chain by lowering the ball's initial speed to about 0.99 m/s over a 2-second rollout, making the cascade less violent overall.

Settling on 5° instead gives a velocity near 1.10 m/s with roughly 1.81 seconds of travel time, which seems like a reasonable balance. Then I start working through the mass of ball2 versus domino d3 to make sure the push-through force makes sense, and I realize there's a problem: ball1, after striking d1, continues rolling at about 0.7 m/s into the pedestal, but the pedestal's height of 0.05 m is actually less than the ball's radius of 0.07 m — meaning the ball could just roll over it instead of being stopped, which breaks the intended chain reaction.

I'm now worried ball1 might climb over the pedestal and tumble into the cup after ball2 is already there, which would ruin the setup since a second ball entering that small cup could easily disturb the first. I need something to intercept ball1 before it reaches that point — maybe using d3 leaning at an angle against the pedestal as a barrier, or adjusting ball1's speed through the upstream collisions so it doesn't carry enough momentum to climb over.

Running the numbers, rolling friction and the energy lost knocking down dominoes should sap most of ball1's speed — estimating roughly 0.6 m/s after impact gives only about 2.6 cm of climbing height from its remaining kinetic energy, which likely isn't enough to surmount a stack of fallen dominoes.

So the chain reaction probably ends with d1 leaning on d2, d2 on d3, d3 against the pedestal, and ball1 wedged against d1 unable to climb further — effectively at rest, satisfying the "slower than 5 cm/s" condition for the ball.

I also need to check that the impact dynamics make sense: ball1 hits d1 above its center of mass, causing it to rotate forward rather than slide, assuming decent floor friction on the dominoes. And I should verify the ball's trajectory lines up correctly as it transitions from the ramp onto the floor just before reaching d1.

Checking the low end of the ramp confirms the top surface meets the floor smoothly at (0,0), so the transition should be seamless. I'm now considering whether to add side rails to keep ball1 traveling straight down the ramp without rolling off sideways.

Since there are no lateral forces and the setup is symmetric, ball1 should naturally stay at y=0 without needing rails. I'll skip adding a keyframe since everything starts at rest and gravity handles the motion — no need to specify full qpos. For positions: dominoes rest at z=0.05 on the floor, ball2 sits on a pedestal at z=0.075, and I'm defining that pedestal as a box centered near x=0.50.

I'm spacing the dominoes with roughly 0.02 gaps between faces, checking that d3's rotation angle stays within range to strike ball2 before hitting the pedestal corner at 21.8°, confirming gravity torque is strong enough past 17° to keep pushing the ball forward through that contact window.

Checking the push direction into the pedestal seems fine, and the geometry of d2 falling onto d3's back face works out around 30° with the heights lining up. I also need to confirm friction of 0.8 is enough to keep the dominoes from sliding, then move on to checking ball1's contact with d1.

Now I'm working out the cup geometry — placing the base and near wall so their heights and positions line up correctly. I notice there's a gap of about 0.01 between the pedestal edge and the cup wall that I need to resolve.

I'm also checking what happens as the ball rolls off the pedestal edge, tracking how it pivots around the corner and estimating the detachment angle for a slow-moving ball to find where its center ends up when it leaves contact.

Checking the step height against ball radius, the ball probably can't climb back over at low speed anyway, and the small gap beyond it is too narrow for the ball to fall into. I'll simplify by abutting the near wall directly against the pedestal at x=0.53–0.54 with the same 0.03 top height, keeping the interior base span at 0.54–0.69.

Static-to-static contacts should get filtered automatically since both bodies are welded to the world, so pedestal-cup touching isn't an issue. Dominoes and ball1 resting at start should be fine with the pedestal gap, and I'm double-checking friction settings—condim 6 with different torsional/rolling friction values for ball1 versus ball2.

Friction combines by taking the max of each geom's value, so the floor's low rolling friction gets overridden by the ball's. Working through the timing: ball1 reaches the first domino around 1.81-2.0s, the chain reaction takes about half a second, ball2 lands in the cup around 2.7s, and with rolling friction decelerating it slightly, it should settle well before the 6s mark.

I'm checking whether domino1 being struck could cause it to fly over domino2 rather than toppling it, but given the masses and spacing it should transfer momentum correctly without jumping the gap. I'm considering lowering ball1's density slightly for a gentler impact while keeping it heavier than the dominoes, settling on a mass around 0.43 kg, and noting that freejoint bodies will compute their own inertia automatically so I don't need to specify that manually.

