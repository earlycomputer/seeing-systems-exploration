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
