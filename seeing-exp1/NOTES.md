# Notes

## Parking lot

Ideas that came up while building experiment 1. Not in code; each needs a human before it becomes work.

- **The scene text may be doing all the work.** With the text included, every deliberate error can be read
  straight from the text: the hoop body says `pos="4 0 2.55"` against a brief that says 3.05 m. The
  with-text matrix may read near-perfect at every resolution, and that would say nothing about seeing.
  Control B covers one cell; `loop.matrix --image-only-arm` runs the full 27 cells per model without the
  text (a few dollars more per model). Off until a human decides, because it changes the design.
- **Readback as a body list or a latent** instead of an image (the handoff's optional extension). Only if the
  loop closes at 64 px or better inside the time box, and only after asking.
- **A plausibility critic** that scores the render before the LLM sees it (from the program doc). Out of scope.
- **Floor dot budget.** The floor gets a fixed quarter of the dots instead of the shared surface density,
  which would otherwise spend everything on it. That is a density difference that means "context, not
  object". Whether that is information or decoration is a question for law 3.

## What the dot render made easier or harder to read

From the hand-written fixture, before any model has looked (see results/step2/):

- The rim is the first thing to go. It is 2 cm thick and seen almost edge-on, so it reads as a thin
  ellipse at 512 px, is faint at 128, and is gone at 64 and 32.
- The backboard carries the hoop's position at low resolution. It is a large flat face with one normal,
  so it reads as a solid block of tone down to 32 px. Because the backboard belongs to the hoop body, the
  hoop-too-low error stays visible even after the rim is gone.
- The ball is about 20 px across at 512 and one or two gray pixels at 32. Even so, at 32 px each error
  still changes the picture: the backboard drops against the pole, the ball shifts, the oversized ball is
  a bigger blob (results/step2/errors_32_fixture.png, checked by eye on the fixture). Whether a model can
  tell without the unbroken picture beside it is what the matrix measures.
- The floor's dot window ends in a ragged far edge that reads like a horizon or the edge of a rug. It is
  an artifact of sampling a finite patch of an infinite plane.
- Back-face culling and the splatted depth test were in from the start, so this renderer has never been
  compared with one that lets the far side of an object show through.
