1. 40 worlds, 0 failed runs, $4.58 (both models). All experiments together: $70.22 of the $100 cap.
2. With the run's history in words, models fixed 35 of 40 broken worlds, against 28 with a picture of the run and 17 with nothing (1d). Opus 5.5: 20 of 20 (picture 12, nothing 9). GPT-6.1 Sol: 15 of 20 (picture 16, nothing 8).
3. Contact failures, the ones text could not fix: history 15 of 16, picture 13 of 16, nothing 1 of 16. Calculable failures: 16 of 16 in every arm that saw the run or not.
4. The door, which nobody fixed in 1d (0 of 16): Opus fixed 4 of 4 with the history. GPT-6.1 Sol read the same line ("starts at 68.8°, outside its range of 0° to 2.1°"), described the slam correctly every time, and still judged that the door "does swing shut and stay shut", 0 of 4. Seeing the cause is not the same as calling it a failure.
5. Without feedback, every unfixed world was claimed to work (23 of 23). With the history, 5 of 5 unfixed worlds were also claimed to work, but only 5 were left: 4 GPT doors and 1 GPT stack.
6. Fixes came early: 33 of 35 in the first round. Opus's last claim was right 20 of 20.
7. Cheaper than the picture: $0.114 per world against $0.134, with histories of 300 to 2,200 tokens.
8. Caveat: the narrator (history/narrate.py) was written by a session that knew the five breaks. Its general events (touches, flights, rests, stops) carry no brief, but two features were added with these worlds in view: a joint's range read back from MuJoCo in degrees, with "starts outside its range", and close passes by things never touched. The door result leans on the first. Its rule is generic (any limited joint), but a narrator written blind might not have had it.
9. Caveat: 1d's picture and text arms ran on 2026-10-04 and were not rerun; same models, prompts, seeds and tests.
10. Embarrassment test passed: the history fixed 15 of 16 contact worlds, not text's 1 of 16.
11. So words about the run did what the picture did, and more, for these worlds. The 1d headline was about feedback from the run, not about pictures.
