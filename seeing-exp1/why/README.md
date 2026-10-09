# Errors with the why in them

Jono, 2026-10-07: "I want the why trace to show up in errors. The debugger is UI for a human to process information
that would be overwhelming to read. An agent can read much more, much faster."

The spacetime debugger (`typed/spacetime.py`, PR #6) finds why a run went wrong for a person to click through.
`errors.py` writes the same why into the error an agent reads when an expectation fails, for worlds in the world
language and in raw MuJoCo XML alike. `python -m why.bench` checks it at $0.

## What an error says

For each expectation that fails:

1. **What was expected and what happened**, pointing at the expect line.
2. **When it was lost.** Each form has its own losing moment: the last landing before rest, the nearest pass for a
   touch, the crossing for a drop, the nearest approach for a stop, or, under 1h's hidden forms, the moment a line
   happened out of order. The weak-spring catapult fails at 1.88 s but was lost at 1.14 s.
3. **How it got there**: the events in the light cone of that moment, oldest first. The walk is spacetime.py's: back
   through touch alone, stopping at things that never move.
4. **The lines that set those things up**: every thing in the cone, what it touched on the way, and the target, as
   the author wrote them. For XML, a body's whole element, plus the keyframe, which sets where everything starts.
5. **Which numbers move it**: each number on those lines is run again at 1.1, 0.9, 1.5 and 0.5 times itself, one at
   a time, in parallel. The numbers that make the expectation hold come first, then those that move the miss most.

The error describes and points; it never edits the world.

## Decisions taken alone (Claude)

- **New directory, nothing else changed.** `typed/`, `langrun/` and `hundred/` are read, not edited. The cone walk is
  spacetime.py's, re-run over history/narrate.py's touch intervals so it works on any MJCF; the forms are
  langrun/expect.py's, and 1h's stricter hidden forms (hundred/hidden.py) with `strict=True`.
- **Forks inside the error.** Running a world takes about a third of a second, so the error tries up to 240 forks
  (four cores) rather than leaving the agent to guess which number matters. Numbers on moving things are forked
  first when there are too many.
- **Four multiples, not one.** A 10% fork alone found the broken line in fewer worlds: 1d's breaks halve or double a
  number, and toppling a stack is a threshold a small change never crosses.
- **The miss is measured at the losing moment** (where the ball came down), not at the end (where it rolled to),
  because the rest position is a poor signal: the catapult's spring sweep is non-monotonic at the rest position.

## Running

    python -m why.bench      # 1d's five breaks in both formats and 1h's twelve failures; ~8 minutes on 4 cores

    from why.errors import explain
    text, info = explain(source, "world", ["ball comes to rest in bucket"])   # or "xml"; strict=True for 1h's forms
