# Status

**2026-10-04, built; first real runs next.** The harness is built and passes a dry run of all 144 cells and
the report. Opus 5.5 wrote the shot on its first try ($0.18), and MuJoCo makes it as written, so it is the
base. The misses are settled on it (short −8%, long +12%, left 5°). Next: the first real runs, seed 0 of
eight cells per model (`python -m outcome.matrix --first`), shown to Jono before the full matrix. The
planning estimate for all 144 is about $47 at worst; the first runs will give the real cost per run.

**2026-10-04, first real runs done: waiting on Jono.** 16 runs, seed 0 of eight cells per model, $4.35.
GPT-6.1 Sol named the direction and made the shot after one correction in 8 of 8. Opus 5.5 named 6 of 8:
both misses came from a quick no-drag estimate ("1 m above the rim") that it trusted over the picture, on
the same shot it had designed by integrating the drag carefully. The runs found a harness bug (an XML
comment counted as a scene change), fixed and rescored. The full matrix's other 128 runs would cost about
$36 at the measured rates (1b about $40 in all, against the design's $25), which is Jono's call.
