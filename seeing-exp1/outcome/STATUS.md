# Status

**2026-10-04, built; first real runs next.** The harness is built and passes a dry run of all 144 cells and
the report. Opus 5.5 wrote the shot on its first try ($0.18), and MuJoCo makes it as written, so it is the
base. The misses are settled on it (short −8%, long +12%, left 5°). Next: the first real runs, seed 0 of
eight cells per model (`python -m outcome.matrix --first`), shown to Jono before the full matrix. The
planning estimate for all 144 is about $47 at worst; the first runs will give the real cost per run.
