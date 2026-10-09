# 1m: a debugger agent, and building one link at a time

Jono, 2026-10-09: "A talking debugger is great! It might as well be an agent too." Then: "I think agents deserve great
ergonomics, like Elm gives developers, and that's a place we get compounding gains." And on the plan below: "Go for it!"

**Why.** The free check (`ladder/breaks.py`, `ladder/results_breaks/breaks.md`) re-ran every file the 1j to 1l long
worlds wrote. Builders see the break (their verdicts name the broken link about three times in four), but about half
their revisions leave the first break where it was, and some break links that already held. Fixing, not seeing, is
the bottleneck. On a chain, per-link gains multiply, so this is where gains could compound.

**What is here.**
- `tools.py`: the debugger's tools over one run, all answered in words: `status` (which links hold), `why` (1i's
  light-cone error for a link), `forks` (each number behind a link changed alone, every fork judged on the whole chain,
  so a change that loses an earlier link shows), `try` (a proposed edit, run and judged), `watch` (a thing over a window).
- `agent.py`: the debugger agent. A second model asks questions in ```ask blocks, the harness answers from the run,
  and it ends with a ```report for the builder. It never edits the file or picks the number to set.
- `run.py`: 1j's XML-with-words loop plus `--debugger` (the report goes to the builder with the run in words) and
  `--staged` (2 links a stage at 8 steps, 4 at 16; a file that breaks an earlier stage's link is refused and the last
  good file kept).
- `bench.py`: $0. For every failing file a 1j to 1l builder revised, could a single-number fork have moved the first
  break forward without losing a link, and was that a number the brief doesn't state?

**Decisions taken alone.**
- Control is 1j's XML-with-words arm, already run with the same briefs, model, seeds, prompts and three rounds.
- The debugger is GPT-6.1, like the builder, with up to 3 question turns of up to 4 questions each.
- Frozen links are enforced by outcome (the earlier stage's links must still hold), not by forbidding edits to lines.
- The number to beat: the share of revisions that move the first break forward without losing a link (1j XML with
  words: 26 of 48). Also worlds that work, steps held, tokens and cost.
- 1m's ceiling is $0 in `run.py` until Jono approves a paid run.
