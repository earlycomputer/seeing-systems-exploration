# Notes

## Parking lot

Ideas that came up while building experiment 1. Not in code; each needs a human before it becomes work.

- **Relational errors need a relational readback.** "Ball displaced" changes a distance between two objects.
  From a picture alone you cannot tell which one moved, and GPT-6.1 Sol blamed the hoop in 3 of the 5 runs
  where it saw the gap. A readback (or a verdict format) that can say "these two are 2.5 m apart, not 4"
  would score what the model actually saw.
- **A text-only control** (scene text, no image) would complete the picture: image only, text only, both.
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

## What the models did with the picture

From the 132 real runs (results/runs, results/failures.md):

- With the scene text, both models read the error straight from the text and never claimed to have found
  it in the picture alone. The with-text matrix measures reading, not seeing.
- GPT-6.1 Sol reads the picture like a person would: it estimates the rim at 2.4 to 2.5 m (true 2.55 m)
  and the ball at about twice regulation size. At 32 px it says nothing rather than guessing.
- Opus 5.5 reasons from the camera numbers: it back-projects pixel coordinates into metres ("at its
  back-projected depth of about 8.9 m, the ball appears about 11 px wide"). This works at 128 px for size
  and occasionally for height, but at 64 and 32 px the arithmetic goes wrong and produces false alarms
  (the support pole "ends mid-frame", the hoop is "2 m from the ball").
- At 32 px the ball is one or two gray pixels, and Opus twice reported it missing. One of those runs was
  scored correct because the error was in the ball, but for the wrong reason.
- Opus's scene added a floor plate, a bracket and a painted target square: a 1 mm box lying on the
  backboard's face. The renderer draws no colour, but the square's dots sit on top of the backboard's, so
  the patch is twice as dense and reads darker at 128 px (checked by eye). Opus described a "dark target
  square" there. Density changed because two surfaces overlap, which is true but was never designed as
  information: a law-3 question for experiment 2, where density is meant to carry confidence.
