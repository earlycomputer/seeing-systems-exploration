**Prediction: the ball drops through the hoop, near the centre of the rim.**

**Setup**
- The `shot` keyframe sets only `qvel`. The ball therefore starts at its body position (0, 0, 0.1194), resting on the floor.
- Launch velocity is vx = 3.21 m/s and vz = 9.3 m/s, about 71° above horizontal. There is no sideways component and no spin, so the Magnus term is zero and the ball stays at y = 0. A left or right miss is not possible.

**Air drag**
- Air drag decides whether this goes in or long. Without air the ball would reach the rim height (3.05 m) at x ≈ 4.8 m, about 0.8 m long, and hit the backboard.
- With `density="1.2"` and `fluidshape="ellipsoid"`, I assumed the sphere gets quadratic drag of F = C_blunt · ρ · A · |v| · v, with C_blunt = 0.25 and A = πr² ≈ 0.0448 m². I am working from memory of MuJoCo's ellipsoid fluid model here, not from the source. This is roughly a textbook Cd of 0.5.
- Added mass is tiny, about 0.004 kg, and I treated it as negligible.
- That gives k = ρ · C · A / m ≈ 0.0215 per metre.

**Hand integration** (midpoint method, 0.1 s steps)

| Point | Time | Height z | Distance x | Velocity |
|---|---|---|---|---|
| Apex | ≈ 0.89 s | ≈ 4.12 m | ≈ 2.65 m | – |
| Rim plane (z = 3.05 m) | ≈ 1.36 s | 3.05 m | **≈ 4.00 m** | vx ≈ 2.79, vz ≈ −4.2 m/s |

At the rim plane the ball's centre is essentially at the rim centre, and it is descending about 33° from vertical. The closest approach of its path to the front and back rim tubes is about 0.20 m. The ball needs 0.127 m (ball radius 0.1194 plus tube radius 0.008), so it clears both. It passes cleanly through and then falls to the floor just beyond the hoop, around x ≈ 4.2–4.3 m.

**How sure I am**
- The result depends on the drag strength. If MuJoCo's blunt-drag term carried an extra factor of ½, the ball would reach rim height near x ≈ 4.4 m and miss long, into the back rim or backboard.
- The coefficient chosen (0.25) and the near-perfect centring my integration gives both suggest the shot was tuned for the formula I assumed. I predict a make.

```json
{"description": "Ball launches from rest on the floor at (0,0,0.12) with v=(3.21,0,9.3). With MuJoCo ellipsoid quadratic drag (C_blunt=0.25, rho=1.2), it peaks near z≈4.12 m around x≈2.65 m. It descends through the rim plane z=3.05 at x≈4.00 m, centred on the rim, at about 33° from vertical with ample clearance from both rim edges. It drops through and lands on the floor just past the hoop (x≈4.2-4.3 m). No lateral velocity or spin, so no left/right error. Without drag, or with half the drag, it would go long.", "goes_in": true, "miss": "none", "evidence": "text"}
```

---
thinking (summarized):

I'm figuring out the starting position of the ball at z=0.1194 since no explicit qpos keyframe is given, then calculating the trajectory using vx=3.21 and vz=9.3, finding the apex height rises about 4.41 m above the start, reaching roughly z=4.53.

Without drag, time to apex is about 0.948 s, and descending to the hoop height of 3.05 adds another 0.549 s, giving total flight time of 1.497 s and horizontal distance of 4.81 m — overshooting by 0.81 m, so the ball would hit the backboard around x=4.38. I'm now working through MuJoCo's ellipsoid fluid drag model, estimating the drag force relative to gravity (roughly 22% of weight at 10 m/s) and trying to recall the exact blunt drag coefficient formula MuJoCo uses to adjust this estimate.

Working through the drag-reduced apex height calculation, I get roughly 4.03 m instead of 4.41 m without drag, and I'm now computing the time to reach that apex using the arctangent formula for velocity-squared drag.

For the descent and horizontal motion, I estimate fall time around 0.46 s for the remaining drop, giving a total flight time near 1.36 s, and factoring in horizontal velocity decay I get a landing distance close to 3.98 m — remarkably near the target of 4 m, which is encouraging for this drag coefficient estimate.

Trying another k value, I recompute apex height and descent time, landing around 4.38 m, which would overshoot and hit the backboard. This tells me I need MuJoCo's precise drag formula rather than my approximation — recalling that MuJoCo distinguishes between an inertia-based drag model and an ellipsoid-based model, with the latter using a projected-area drag force formula I need to pin down exactly.

I'm working out the linear drag coefficient combining the Stokes viscous term with the quadratic blunt/slender drag terms, noting that for a sphere the projected area equals the max cross-sectional area so the slender term vanishes.

With no initial spin, Magnus force is zero, and checking added mass for the sphere gives a negligible contribution around 0.7% of the total. I'm also considering whether MuJoCo's fluid model includes buoyancy, which seems minor either way.

I'm computing the drag coefficient k using cross-sectional area and effective mass that accounts for added mass, working toward a more precise numeric integration of the trajectory.

Now I'm running an RK2 midpoint integration step from t=0 to 0.1, starting with initial velocity components, computing drag acceleration from the speed magnitude, then propagating position and velocity forward using the midpoint estimate.

Continuing the midpoint integration into step 3, I'm updating position to x=0.6293, z=1.7483 with velocities settling around vx=3.09, vz=7.03, then computing new drag coefficients for the next iteration.

Continuing the step-by-step integration, I update velocities and positions for step 5, recalculating drag coefficients with each midpoint estimate to refine vx, vz, x, and z values.

Continuing the numerical integration, I compute drag and gravity forces at step 7, updating velocity to vx=2.9179, vz=1.8521 and position to x=2.1249, z=3.9461, then start step 8 by finding the new speed and drag coefficient.

Continuing the integration, I find the trajectory peaks near z≈4.119 at about t=0.89s, then starts descending as vz goes negative. I keep iterating the drag-adjusted velocity and position updates for the next step past the apex.

Continuing the step-by-step velocity and position integration, drag deceleration keeps reducing horizontal speed while gravity dominates the vertical component, pushing the projectile's z-position down toward 3.6 as I move into step 12.

Running the next RK2 iteration for step 13: recomputing speed magnitude, drag coefficient, and accelerations at midpoint then full step, getting new velocities around vx=2.79, vz=-3.98 and position x=3.84, z=3.29. I'm now setting up step 14, noting I need z to reach 3.05, meaning roughly 0.24 more drop with vz heading further negative.

Checking clearance against both rim edges confirms the ball's path clears the back and front rim by a comfortable margin, so it should swish through cleanly under this drag model — though I note that if my drag coefficient is off by a factor of two, the shot could land too long and clip the backboard instead.

My numerical integration gives a dead-center make, which strongly suggests this trajectory was deliberately designed. With default viscosity at zero there's no Stokes drag term, and buoyancy doesn't seem included either—the ball starts resting on the floor, gets launched upward, and lands right in.

