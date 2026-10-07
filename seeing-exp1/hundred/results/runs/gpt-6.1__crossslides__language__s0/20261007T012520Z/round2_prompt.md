1 problem in this world. Nothing was built.

-- PARTS START INSIDE EACH OTHER ----------- first forward stop / slider2

I was expecting parts that at most touch when the world starts, but I found:

    30 mm of overlap at t = 0

MuJoCo pushes overlapping parts apart in the first steps, so the world starts with a kick nobody wrote.

Hint: move one of them, or check the sizes


Reply with the complete corrected world in one ```world block (and a ```parts block if you define new parts).
