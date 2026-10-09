# Notes

- First dry run on spring8 XML s1 round3 (1j): `forks 4` finds 9 single-number changes that make "door1 swings to a
  stop" hold, all tuning (the hinge range -70 to -63, the door's position). `watch door1` shows the real cause: the
  door stops at -69°, 1° short of its stop, because it hits block1 at 1.78 s. The watch tool, not the forks, found it.
  Forks alone would hand a builder tuning; the debugger has to be told (and is) that tuning a brief's number is not a fix.
- `why` gives little for "swings to a stop" (no losing moment or light cone for the stop forms); worth adding.
- The free check first ran every file for 6 s, not the ladder's 12 s and 20 s; rerun with each world's own run length.
