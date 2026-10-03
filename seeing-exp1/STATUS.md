# Status

**2026-10-03, first session.** The whole harness is built and committed step by step: environment and smoke
test, authoring, the dot renderer, readback, correction, the matrix runner and the report script. Step 2
passes its acceptance on a hand-written fixture: the ball moves about 65 px per quarter second while its
dots keep their pairwise distances to under 1e-9 m, and every object can be named in the 512 image. Steps
1, 3, 4 and 5 run end to end in dry-run mode (a scripted oracle and a scripted failure, 62 cells in 3
seconds) but have not run against a real model, because the cloud environment has no API keys. The second
model is Gemini 3.1 Pro rather than GPT-5.6, because the environment's network policy blocks
api.openai.com. Nothing in results/ comes from a model yet. Next: add ANTHROPIC_API_KEY and GOOGLE_API_KEY,
run step 1, rerun step 2 on the authored scene, check step 3's control, then run the matrix (rough
estimate about $10 for 62 runs, against the $100 cap).

**2026-10-03, later the same day: matrix done.** Keys arrived (the Anthropic key as SEEING_ANTHROPIC_API_KEY,
because cloud environments reserve ANTHROPIC_API_KEY), and a human switched the second model to GPT-6.1 Sol.
Steps 1 to 4 passed on the first real runs, and those runs showed both models finding the error in the
scene text, so with the human's go-ahead the matrix also ran image-only, with a false-alarm control. All 132
runs completed for $7.52 (plus $0.10 authoring). With text, the loop closes at 32 px for both models. With
the picture alone, GPT-6.1 Sol closes it at 64 px for hoop height and ball size with no false alarms;
Opus 5.5 does not close it at any resolution. The ten-line summary is in results/summary.md. Open: the
handoff's optional extension (readback as a body list or latent), which needs a human's yes.
