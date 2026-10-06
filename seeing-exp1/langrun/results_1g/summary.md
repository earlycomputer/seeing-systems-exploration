Written after reading the tables above (2026-10-06).

1. **Checking expectations did not help.** With each world's own expectations checked against every run, 149 of 160
   worlds worked in the end; the control, with the same fixed language, history readback and "at rest under 5 cm/s"
   line but no expectations, got 156 of 160 (p = 0.11). Worlds that worked as first written fell from 134 to 115 of
   160 (p = 0.015): asking for expectations made first writes worse.
2. **The checker judged well; the models overrode it.** In 3 of 1g's 11 failures the readback said "DOES NOT HOLD:
   ball comes to rest in bucket (still moving, 0.06 m/s)" and the model answered that the brief only asks for the
   ball to land in the bucket, and called the world fine. In 5 failures every expectation held: the models did not
   write down the condition the test checks (a ball resting on the seesaw at the start, the stack standing before
   the push). 37 of 667 lines were outside the four forms ("ends tilted at least 15 degrees", "rises at least 0.5 m"):
   the vocabulary is too small for what the briefs ask.
3. **The free fixes did the work.** The control's language arm made all 80 worlds work (1f: 37 of 40); its XML arm 76
   of 80 (1f: 38 of 40). The four language fixes and the rest line together closed every language miss from 1f.
4. **Language against XML, both fixed (control).** Works in the end 80 of 80 against 76 of 80 (p = 0.12). Builds on
   first write 73 against 70. Per world the language used about half the output tokens (4,389 against 8,571), half
   the wall time (62 s against 128 s) and 24% less money ($0.146 against $0.191); getting a broken world working took
   9,131 output tokens against 17,202. Input tokens ran the other way (20,486 against 14,919): the language's guide
   and library ride along in every turn.
5. **Against Jono's 100x bar.** Nothing here is close: the largest effect is about 2x, in output tokens and time.
   Pass rates are at the ceiling for both formats on these briefs, so they cannot show a large effect either way.
6. **Misses that remain** are about what the brief means more than about the world: three "comes to rest" fails at
   0.05 to 0.07 m/s, and seesaw worlds (3 in the control, 4 in 1g, all Opus) where the ball is not touching the plank at the start.
