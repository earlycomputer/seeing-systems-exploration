# Experiment 1h: measuring for 100x

Jono, 2026-10-06: "I want to find 100x improvements in understanding, debugging, token cost, ease of expression,
shared understanding". 1h measures those five plus foresight and trust (see `../measure/README.md` for all eleven
targets and the baselines from 1d to 1f). Jono chose "Pilot first": 5 briefs, 60 worlds, about $20.

## Design (decisions taken alone, by Claude)

- **Fresh briefs nobody tuned.** GPT-5.6, which writes no worlds, writes 24 briefs and their hidden tests in one call
  (`briefs.py`); the first 20 that pass mechanical validation are kept, committed before any world runs. The pilot
  uses the first 5. Briefs are harder than 1d's: 5 to 15 things, a chain of at least three causes.
- **Hidden tests in expectation forms** (`hidden.py`), stricter than an author's own: a touch must begin after the
  start, a thing must not start where it comes to rest, and the lines must happen in order.
- **Three arms** (`settings.py`): `blind` (MJCF, load errors only, no run information: today's tools), `xml` (MJCF,
  checks, the run in words, expectations checked: 1g's XML arm) and `language` (1g's language arm). Every arm
  writes expectations; only `xml` and `language` hear which hold. Opus 5.5 and GPT-6.1 Sol, 2 seeds.
- **Foresight and shared understanding** (`read.py`): both models read each final file, before seeing any run, and
  say which hidden-test statements will hold.
- **Understanding** (`quiz.py`): questions generated from each run (at rest at the end, ends inside what, first
  touch, when a touch begins), answered from raw MuJoCo state (positions every 0.1 s, contacts, geoms) or from the
  run in words. Pilot: 10 worlds. The picture is left out of the pilot.
- **Spend** (`budget.py`): the pilot stops at $25; every experiment together stays under `config.SPEND_CAP_USD`.

## Running

    python -m hundred.briefs                 # once; then commit briefs.json
    python -m hundred.matrix --pilot
    python -m hundred.read
    python -m hundred.quiz --worlds 10
    python -m hundred.report                 # writes results/results.md

Plumbing test with no calls: `python -m hundred.matrix --models dry-run dry-run-echo --dry-briefs`, then
`read --dry`, `quiz --dry`, `report --dry`.
