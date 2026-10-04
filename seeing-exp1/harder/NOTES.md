# Notes

## Parking lot

- **Breaks a careful reader could catch.** The door's "0 2.1" and the shot's backspin are visible in the XML to
  someone who knows MuJoCo's conventions; the cup's distance, the stack's push and the catapult's spring need
  the run. A result split along that line would say which failures text can catch.

## Building it

- Backspin of 30 rad/s on the 1b shot made it come down short (crossing rim height at x = 3.42 m), with a
  higher apex. 10 rad/s still went in. 20 missed.
- The hand-written pendulum works for release angles 0.9 to 1.5 rad; below 0.9 the ball stops short or bounces
  off the cup's low lip. It is released at 1.1.
- The first domino needs a tip of about 4 rad/s; at 2.5 it rocks back upright.
- The broken door's residue ends at 0.74 s, correctly: the limit slams it shut within the first copy, then
  nothing moves.

## What the 112 worlds showed (2026-10-04)

- **Calculable against dynamic.** The shot's backspin and the cup's distance were fixed by text as well as by
  the picture: models removed the air or recomputed the flight off the ramp. The stack's push and the
  catapult's spring needed the run: text fixed 1 of 16, the picture 13.
- **Blind fixes that miss, then claim success.** All 8 text-only catapults diagnosed "falls short" by
  calculation and changed the file, and all 8 still missed and then said it works. Text only gets one guess.
- **GPT-6.1 Sol's text-only stacks never tried a fix** (0 of 4): it predicted the push would topple the stack.
  With the picture it saw the stack stand and fixed all 4.
- **The door's break is a wrong cause with a right-looking outcome.** The door does shut and stay shut; it
  slams through its limit in 0.03 s. Every model in both arms described a door swinging shut and called it
  working. In 1c, Opus caught the same trap once, from a residue with no swing; here the given door's first
  copy is open and the next shut, which reads as a swing at 128 px.
- **Test flaws the runs found.** A first domino that starts tipped is a fair reading of the brief; a cup body
  that includes its entry ramp is what the naming convention asks for. Both were the test's fault, not the
  models'. Writing tests before runs catches loopholes in worlds, but not every loophole in the test.
- **Dominoes were too easy** (16 of 16 first write). A longer chain, a turn, or a gap to bridge would make it
  a test.
- **The viewer** (`viewer.py`, from 1c's on `exp1c-viewer`, merged into this branch) re-runs all 189 saved files
  and checks each verdict before drawing it; all agree.
