1. With the scene text, the loop closed at every resolution down to 32 px: both models named the error 3 of 3 and fixed it within 5% in all 18 cells, and reported nothing wrong on the unmodified scene.
2. The text did that work. Across 54 error runs with text, neither model said it found the error in the picture alone (Opus 5.5: "text" 19, "both" 8; GPT-6.1 Sol: "text" 25, "both" 2).
3. With the picture alone (the image-only arm, added with a human's go-ahead after the first runs), the answer splits by model.
4. GPT-6.1 Sol closes the loop at 64 px for hoop height and ball size: 3 of 3 for each at 128 and 64 px, no false alarms in 9 unmodified runs, and where it gave a number it put the rim at 2.4 to 2.5 m (true: 2.55 m).
5. At 32 px it goes quiet rather than wrong: 0 of 3 on the hoop, 1 of 3 on size, still no false alarms.
6. Ball displaced scores low (2 of 9) partly by construction: at 128 and 64 px GPT-6.1 Sol saw the ball and hoop 2.5 to 3 m apart in 5 of 6 runs but blamed the hoop in 3. From a picture alone you cannot tell which of two objects moved.
7. Opus 5.5 does not close the loop from the picture at any resolution: hoop 1 of 9, ball size 3 of 9, displacement 2 of 9 (one of those for the wrong reason), and 4 false alarms in 9 unmodified runs, all at 64 or 32 px.
8. Embarrassment test (64 px, hoop 0.5 m low, picture only): GPT-6.1 Sol passed 3 of 3. Opus 5.5 failed 3 of 3, reporting nothing wrong each time.
9. Cost of the round trip: about 11k tokens per run for Opus and 9k for GPT-6.1 Sol with the text, about 3k with the picture only. The 132 runs cost $7.52, authoring $0.10.
10. So the central claim is not wrong as framed: a 64 px picture can carry a 0.5 m error to at least one model. But it is model-dependent, and errors about relations (how far apart) need a readback that can say which object moved.
