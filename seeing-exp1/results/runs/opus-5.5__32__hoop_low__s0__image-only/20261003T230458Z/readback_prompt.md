You are checking a physics scene against the brief it was written from, by looking at a picture of it.

<brief>
a regulation basketball on a floor, a hoop at 3.05 m, 4 m away, lit from above
</brief>

The scene text is withheld for this check; you have only the picture.

How the picture was made. A dot renderer drew the scene at t = 0, as written, before any simulation. Every
object's surface is covered in small dark dots on a white ground, shaded only by surface normal against
one light from above; dots on surfaces facing away from the camera are hidden. The camera is fixed: it
stands at (-0.80, -8.50, 4.25) m and looks at (2.60, 0.00, 1.70) m, with a 40 degree vertical field of view, so +x runs
left to right and slightly away from you, z is up, and you look down a little. The image below is
32x32 pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of its pixels
averages 16x16 pixels of the original.


[image: tone_32.png]

First, describe what you see in the image: which objects are there, roughly where, and roughly how big.
Then compare the scene with the brief and name the single object that does not match it, if any.

End your reply with a ```json block holding one object:

{"description": "<what you see>", "mismatch": <one of "ball" | "hoop" | "hoop_support" | "floor" | "none">, "what_is_wrong": "<one sentence, or empty>", "evidence": <"image", "text", "both" or "none">}

`evidence` says where you found the mismatch: in the picture, in the scene text, or both.
