# Seeing systems: exploration

Humans and machines working in the same space because both can see the same thing.

The program lives in these docs:

- [Seeing systems design journal](https://claude.ai/artifact/88e7a541-1b9c-49d6-85f3-d7ee56581363): decisions, experiments, results and next steps, kept as the work happens
- [Seeing systems for humans and machines](https://claude.ai/artifact/NTc95ve9kfXJjr9UvAjBrJ): thesis, laws, experiment ladder
- [Experiment 1 handoff: round trip](https://claude.ai/artifact/8bvbRyeu42bgKoB6V1AbxH): the spec this repo implements first

## Experiments

| # | Name | Directory | State |
|---|------|-----------|-------|
| 1 | Round trip | [`seeing-exp1/`](seeing-exp1/) | Matrix done; [results](seeing-exp1/results/results.md) |
| 1b | See the outcome | [`seeing-exp1/outcome/`](seeing-exp1/outcome/) | Done: text only was enough for a ballistic shot; GPT-6.1 Sol 72 of 72, Opus 5.5 60 of 72 and worse with pictures ([results](seeing-exp1/outcome/results/results.md), [status](seeing-exp1/outcome/STATUS.md)) |
| 1c | Five worlds | [`seeing-exp1/worlds/`](seeing-exp1/worlds/) | Done: most worlds work on the first write (GPT-6.1 Sol 17 of 20, Opus 5.5 13 of 20 in the end); the picture fixed 2 of 6 first-write failures, text only 0 ([results](seeing-exp1/worlds/results/results.md), [status](seeing-exp1/worlds/STATUS.md)) |
| 1d | Harder worlds | [`seeing-exp1/harder/`](seeing-exp1/harder/) | Built; first runs next ([status](seeing-exp1/harder/STATUS.md)) |
