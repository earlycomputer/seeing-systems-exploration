# Notes

- Door (1d's radians-in-degrees break) can't be caught by any expectation form: the door snaps shut at once, so
  "door reaches its lower stop" holds. The world language refuses to build it (the door starts open 69°, outside
  0° to 2.1°). The run-time error has nothing to say about a world that does the right thing for the wrong reason.
- The shot's plain form `ball drops through hoop` holds in the language world even with backspin: the hoop's box
  includes its backboard and pole, so "through" is 0.9 m wide. `hoop.rim` (language) and `rim` (XML) are the honest
  lines. Worth fixing in langrun/expect.py (owned elsewhere): use the ring's inner radius, not the bounding box.
- Forks are local. Two numbers wrong together, or a wrong structure (a missing wall), won't show as one number.
- 1h's trapdoors XML worlds start the flap at its lower stop; under the hidden forms that is "not something that
  happens". The error says so in words now.
- Errors run 2,000 to 8,000 characters; the run in words that 1e to 1h sent runs 2,000 to 15,000. On the small 1d
  worlds the error is about as long as the whole history; on 1h's bigger worlds it is about half.
- In 1h's table, "error chars" covers every failing line of that world: gpt-6.1 trapdoors blind s0 has four errors
  (37,134 chars), the rest one or two. Per error, 4,000 to 9,000 chars on 1h's worlds.
- Shot (language) ranks the spin line 7th: the miss at the rim moves more with launch speed than with spin, and
  no single forked number fixes it. The error still points at the line.
