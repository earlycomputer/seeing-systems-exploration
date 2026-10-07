2 problems in this file. Nothing was run.

-- PARTS START INSIDE EACH OTHER --------- ball2_perch_block / cup_bottom

I was expecting parts that at most touch when the world starts, but I found:

    10 mm of overlap at t = 0

MuJoCo pushes overlapping parts apart in the first steps, so the world starts with a kick nobody wrote.

Hint: move one of them, or check the sizes

-- PARTS START INSIDE EACH OTHER ------ ball2_perch_block / cup_rear_wall

I was expecting parts that at most touch when the world starts, but I found:

    10 mm of overlap at t = 0

MuJoCo pushes overlapping parts apart in the first steps, so the world starts with a kick nobody wrote.

Hint: move one of them, or check the sizes


Reply with the complete corrected file in one ```xml block.
