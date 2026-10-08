The supplied language cannot express this brief exactly, so I can’t honestly provide a complete world that satisfies it.

Two required features are missing:

- **Horizontal slide joints and linear damping.** The language supports free bodies and hinges, but no slide joint or `0.20 N·s/m` slide-damping fact. Physical guide rails would not supply that damping.
- **Numeric restitution.** `bounce dead` and `bounce lively` do not specify a restitution coefficient of **0.05**.

MuJoCo’s default gravity is 9.81 m/s², and the stated masses, dimensions, friction, hinge damping, and zero starting velocities are expressible. Custom parts cannot add the missing joint or contact-setting features.

Please provide syntax for slide joints, linear damping, and numeric restitution—or permit approximations. Inventing those facts would produce unsupported syntax rather than the requested compiling world.

---
thinking (summarized):

**Addressing world simulation constraints**

The user prefers a transparent and concise response without unnecessary blocks, focusing on simulation fidelity. It’s clear I need to express the limitations of creating a world accurately based on the provided instructions. I should point out that delivering what’s requested may not be feasible and highlight specific constraints like gravity settings and restitution options. My honest assessment needs to effectively communicate these technical limitations without overstating capabilities.

**Clarifying simulation limitations**

It seems there's a need for complete transparency regarding what's possible without violating any requirements. Implementing certain features, like slides, seems quite impossible to define. I realize that numeric restitution functions only in specific contexts, and MuJoCo doesn't simplify it into a single numeric field. I need to explain these constraints clearly—emphasizing that while hinge damping is supported, extending beyond that isn't feasible. The user may expect actual artifacts, but creating the desired world may be intentionally tricky.

**Assessing restitution challenges**

I'm considering how restitution .05 might not be expressible exactly, but there could be approximations. I'm questioning whether it's truly impossible to achieve precise motions. Would returning an annotated partial world be acceptable? It feels better to prioritize honesty here. I wonder if I should mention that the provided language can't accurately express this brief without a specific syntax. Since the prompt might not demand full code, we should define concrete requirements instead of spending time on a flawed full world.

**Clarifying restitution terms**

It seems I'm discussing the numeric restitution parameters, particularly focusing on "bounce dead" or "lively" without explicitly specifying values like e=0.05. I should clarify that I can provide language extensions or allow for approximations. The user likely prefers straightforward responses without refusals, which I'm aiming to accomplish while maintaining accuracy. I’m considering how to finalize the response around 140 words, ensuring it's both clear and meets the user's needs.