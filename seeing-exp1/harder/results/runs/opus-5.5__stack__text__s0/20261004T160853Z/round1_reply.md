**What I expect to happen**

- **Before the push (0 to about 1 s).** The five blocks start exactly touching, so the stack settles slightly and stands still. The 4 kg pusher sphere starts sliding at 1.5 m/s. Floor friction quickly turns this into pure rolling at about 5/7 of the starting speed, roughly 1.07 m/s. The default contact dimension of 3 adds no rolling resistance, so it keeps that speed.
- **The push (about 1 s).** The sphere covers the 1.0 m gap in about a second and hits `block1` squarely at its centre height. Because the sphere is much heavier, it shoves `block1` forward at roughly 0.9–1 m/s.
- **Why the stack tips.** Friction between `block1` and `block2` drags the base of the upper four blocks forward at up to 0.6 g. Tipping starts at about 0.25 g, the half-width of 0.1 m divided by the centre-of-mass height of 0.4 m. So the upper stack pivots back onto the rear edge of `block1`.
- **Rough numbers.** By my estimate, the brief slip phase gives the upper stack about 1.9 rad/s of backward spin. That is about 0.8 J of rotational energy, against about 0.1 J needed to carry the centre of mass past the tipping angle. The upper blocks therefore rotate past balance and topple, separating as they fall onto the floor and the pusher.
- **Afterwards.** Everything comes to rest well within the 6 s window.

The scene stands, the bottom block gets pushed, and the stack topples, which matches the brief. This rests on hand estimates, since I have no run to check against.

```json
{"what_happens": "The stack settles and stands while the 4 kg sphere rolls in at about 1.07 m/s. At about 1 s it hits block1 and shoves it forward. Friction drags the base of the upper four blocks forward faster than they can stay upright (about 0.6 g against a 0.25 g tipping threshold), so they pivot backward off block1's rear edge and topple onto the floor, settling before 6 s.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm working out the pusher sphere's dynamics: radius 0.1, mass 4, starting at x=-1.2, z=0.1, sliding at 1.5 m/s with no initial spin. The effective friction with the floor is the max of the two surface coefficients, 0.6, and I'm using that to figure out how quickly friction converts the sliding into rolling motion for a solid sphere.

Once rolling (around 1.07 m/s), it travels about 1 m to reach block1, taking roughly a second. I'm estimating the impact: the 4 kg sphere striking a 0.5 kg block supporting a stack, with floor and inter-block friction around 0.6, likely knocks block1 out at a speed that settles near 0.95 m/s due to MuJoCo's fairly inelastic contacts, while friction drags on the blocks above start to accelerate block2 under the reduced load.

This resembles the "tablecloth trick" scenario — the key question is whether yanking block1 out leaves the upper three blocks standing (dropping down slightly) or toppling, which depends on how the base friction torque interacts with the stack's center of mass as it's dragged forward.

Working through the relative velocity more carefully: block1's velocity relative to the stack hits zero around t=0.17s, giving a relative displacement of only about 0.085 m — not enough for block1 to fully slide out unless the sphere keeps pushing it. This is getting complicated with the sphere's momentum and floor friction interacting, so I'm stepping back to consider whether the upper stack actually topples given the torque from base-dragging versus its height and width.

My best guess is the blocks likely topple given the momentum mismatch, though it's genuinely hard to predict precisely—I'll just note the stack starts stable, the pusher arrives around 1 second in, and with default contact settings the sphere should roll without losing momentum beforehand.

Adding floor friction on the sphere too, the combined deceleration comes out around 5.9 m/s² for the lower mass with the upper stack accelerating oppositely, closing the relative velocity gap in roughly 0.08 s with about 0.04 m relative displacement. That acceleration exceeds the 0.25g tipping threshold, so the upper stack would actually begin tipping backward during this brief contact window rather than just sliding.

Working out the tipping dynamics, I compute the moment of inertia of the four-block stack about its center of mass, then estimate the net torque from the friction force acting below the COM against the normal force's offset to the back edge, giving roughly 2.76 Nm of tipping torque. That translates to an angular acceleration around 24 rad/s², which over the 0.08 s contact window produces a small rotation of about 0.08 rad before everything starts moving and decelerating together.

Now I'm checking whether the system's deceleration (around 0.6g from floor friction, moderated by the sphere's mass sharing the load) is enough to actually topple the stack — comparing the already-tilted 0.08 rad angle against the critical toppling angle of about 0.245 rad, and computing the rotational kinetic energy at the pivot (~0.81 J) to see if it's sufficient to overcome the potential energy barrier needed to tip over.

Working through the energy comparison, the potential energy required to rise over the critical angle is only about 0.11 J, far less than the 0.81 J available, so the stack does topple backward toward the pusher. There's a chance individual blocks slide apart rather than toppling rigidly, and the stack may land on the sphere, but overall it works as intended.

