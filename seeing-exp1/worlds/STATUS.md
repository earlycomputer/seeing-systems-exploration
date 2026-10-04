# Status

**2026-10-04, built; waiting for 1b.** The five briefs, their tests, a hand-written world per brief, the
picture readback, the loop, the matrix and the report are built, and a dry run of all 40 worlds passes.
Jono approved the experiment to run after 1b's write-up. Before the first real run: merge the finished 1b
branch in (so the cap check sees 1b's whole ledger), set `settings.VIEW` from 1b's results, and run in a
session that has the Seeing Systems OpenAI key. Then the first runs (`python -m worlds.matrix --first`,
10 worlds) before the other 30.

**2026-10-04, finished.** All 40 worlds, 0 failed runs, $8.30 (the estimate was $33; most worlds stopped
after one round). With experiments 1 and 1b, $48.75 of the $100 cap. Jono approved the first 10 with the view
as built (drafting, framed to fit, 128 px), then asked for all 40 to run to completion. The finished 1b branch
was merged in first so the cap check saw its whole ledger. Working in the end: GPT-6.1 Sol 17 of 20, Opus 5.5
13 of 20; as first written 16 and 12. The picture fixed 2 of the 6 worlds that failed as first written, text
only 0. Results: `results/results.md`, the summary in `results/summary.md`, and `results/sensitivity.md` for
the catapult under a second reading of "3 m away". The branch waits on Jono to merge into `main`.
