# Measuring for 100x

Jono, 2026-10-06: "I want to find 100x improvements in understanding, debugging, token cost, ease of
expression, shared understanding." This directory holds the measures and their baselines.

`baseline.py` reads the logged runs of 1d, 1e and 1f (no model calls) and writes `baseline.md`. Those runs live
on branch `claude/project-thread-p9qmg7`, read at commit ecf0447:

    git worktree add --detach /tmp/crit origin/claude/project-thread-p9qmg7
    python measure/baseline.py /tmp/crit/seeing-exp1 > measure/baseline.md

1d and 1e rows count only the 40 broken worlds; 1f counts all 80 worlds it wrote. "Tokens per working world" is
every token in and out divided by the worlds that passed their test, so failures cost the arm.

| Target | Measure | Where a 100x could show |
|---|---|---|
| Understanding | Questions about a run answered correctly, and tokens read to answer | Same accuracy from 1/100 of the tokens |
| Debugging | Tokens, seconds and runs from broken to working; "it works" said of a world that doesn't | Wrong claims 1 in 100, not 1 in 2 |
| Token cost | All tokens per working world | 250 tokens, not 25,000 |
| Ease of expression | Tokens the model writes per working world; worlds right on the first try | Right first time, written once |
| Shared understanding | Two readers predict what a world will do from its description; agreement with each other and the run | Predictions agree with the run 99 in 100 |

A success rate near the ceiling (38 of 40) cannot show 100x. Costs and error rates can, and an error rate of 1 in
100 needs hundreds of worlds to see.
