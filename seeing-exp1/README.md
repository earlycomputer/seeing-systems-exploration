# Experiment 1: round trip

A model writes a physical scene as text, a dot renderer draws it, a low-resolution readback of the drawing
goes back to the model, and the model has to find and fix a deliberate error using what it can see.
Spec: [Experiment 1 handoff](https://claude.ai/artifact/8bvbRyeu42bgKoB6V1AbxH).

## Run it

```bash
cd seeing-exp1
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
source .venv/bin/activate
python smoke_test.py                                   # MuJoCo works

# Keys come from the environment, never from files:
#   SEEING_ANTHROPIC_API_KEY  (primary, Opus 5.5; cloud environments strip ANTHROPIC_API_KEY,
#                              which is reserved for Claude Code's own login)
#   OPENAI_API_KEY     (second, GPT-5.6)
python -m scene.author --model opus-5.5                # step 1: writes scene/authored.xml
python -m render.check                                 # step 2: frames + tone fields in results/step2/
python -m loop.run --model opus-5.5 --res 128 --error none            # step 3: should report nothing wrong
python -m loop.run --model opus-5.5 --res 64 --error hoop_low --seed 0  # step 4: one cell
python -m loop.matrix --plan                           # step 5: what would run, rough cost
python -m loop.matrix                                  # step 5: every cell, 4 at a time, skips done cells
python -m loop.report                                  # results/results.md and results/failures.md
```

Every step has a dry-run mode that needs no keys: `--model dry-run` always gets it right and
`--model dry-run-echo` never does. Dry output goes to `.dryrun/` (gitignored) and never reaches results.

## Where things are

```
scene/      brief.txt, author_prompt.md, author.py (step 1), sim.py (load, measure, inject errors),
            fixture_handwritten.xml (agent-written, for development only; real runs refuse it)
render/     dots.py (body state -> dot field -> 512 image), check.py (step 2 acceptance)
readback/   tonefield.py (box-filter downsample), prompt.md + task.md (turn 1), correction.md (turn 2)
loop/       models.py (vendor adapters, spend ledger, $100 cap), run.py (one cell), matrix.py, report.py
results/    runs/<cell>/<timestamp>/ (every prompt, reply, raw response, image, measurement), spend.jsonl,
            results.md and failures.md (generated), summary.md (the ten lines, written after reading)
NOTES.md    parking lot and observations
STATUS.md   end-of-day status
```

## State of each step

| Step | Acceptance | State |
|---|---|---|
| 0 Environment | Smoke test passes | Passed |
| 1 Authoring | Model's file loads without hand edits; hoop rim z = 3.05 m | Built, dry-run passes; **needs ANTHROPIC_API_KEY** |
| 2 Dot renderer | Ball moves between frames, its dots keep their arrangement; a person can name every object | Passed on the hand-written fixture; rerun on the authored scene |
| 3 Readback | Unmodified scene at 128 px: model reports no discrepancy | Built, dry-run passes; **needs keys** |
| 4 Correction | Measured quantity within 5% after one correction turn, by MuJoCo state | Built, dry-run passes both ways; **needs keys** |
| 5 Matrix | results.md filled by script | Built, 62-cell dry run fills it; **needs keys** |

## Decisions made without a human

The handoff leaves these to the agent; each is logged here so it shows its origin.

- **Second model: GPT-5.6** (`gpt-5.6-sol`, the flagship tier). The handoff allows GPT-5.6 or Gemini 3.1 Pro.
  The first session used Gemini because the network policy blocked `api.openai.com`; once the host was
  allowed on 2026-10-03, GPT-5.6 replaced it. The Gemini adapter stays as the alternative.
  Model ids and prices came from third-party listings on 2026-10-03 because the vendors' doc sites are
  blocked from the cloud box; the first real call checks each id (`loop/models.py`).
- **Model settings.** Effort `high` for both models. Opus 5.5 uses adaptive thinking with summarized thinking
  logged; GPT-5.6 uses reasoning effort high with reasoning summaries logged. Anthropic refusal fallbacks are off, so a
  row labelled Opus 5.5 is always served by Opus 5.5 and a refusal is recorded as data.
- **Authoring conventions** (`scene/author_prompt.md`): names (`ball`, `hoop`, `rim*`, `floor`), axes
  (z up, floor at z = 0, ball at the origin, hoop along +x), primitives only, one element per line.
  They fix names and axes, not what the model builds. The one-element-per-line rule keeps every
  deliberate error to exactly one changed line.
- **Camera.** Fixed pinhole at (-0.80, -8.50, 4.25) m looking at (2.6, 0, 1.7) m, 40° vertical field of view: a
  raised three-quarter view so the rim reads as an ellipse and the backboard's face shows. The first,
  side-on pose showed the rim as a line and cut off the pole. The readback prompt tells the model the pose.
- **Dots.** About 20,000: a quarter on the floor over the visible window (x -3 to 7 m, y -4 to 4 m), the rest at
  one density over every solid surface, with small bodies lifted to 400 dots as a whole (the ball). 2 px
  opaque marks, back faces dropped, a splatted depth test for occlusion, shading by normal only.
- **Frame shown.** The readback renders t = 0, the scene as written, before simulation.
- **Encoding.** Grayscale PNG at the readback resolution itself (128, 64 or 32 px), not upscaled.
- **Conversation.** Two turns: readback (describe, then a JSON verdict), then correction (the full file,
  with an XML comment on each changed line). The image-only control gets no correction turn.
- **What "fixed" measures.** Hoop too low: mean z of the `rim*` geoms vs 3.05 m. Ball displaced: horizontal
  distance from ball center to rim center at t = 0 vs 4.0 m. Ball wrong size: sphere radius vs 0.12 m.
  Each within 5%.
- **"Ball x shifted 1.5 m sideways"** is read literally as +1.5 m along x. In this frame that moves the ball
  toward the hoop, 4.0 m to 2.5 m. If "sideways" meant across the court (y), the brief's "4 m away" would
  barely change (4.27 m, inside 7%), and the error would hardly be an error.
- **Controls.** A: the unmodified scene at 128, 64 and 32 px. B: the embarrassment cell exactly as the handoff
  states it, hoop 0.5 m low at 64 px, with the scene text withheld. Both run at seed 0, once per model.
- **Seeds.** The seed sets dot sampling, so each seed is a slightly different picture and an independent
  model sample. Neither API takes a sampling seed.
- **Timestep** is forced to 0.002 s on every load, and the override is logged when it applies.
