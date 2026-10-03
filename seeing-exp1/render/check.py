"""Step 2 acceptance: the ball visibly moves between frames while its dots keep the same relative arrangement,
and a person can name every object in the 512 image.

    python -m render.check [--scene scene/authored.xml]

The ball is tossed (an initial velocity and spin set here, for this check only; the scene file is not
changed) so there is motion to look at. Writes frames, a contact sheet and the three tone fields to
results/step2/.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mujoco
import numpy as np
from PIL import Image

from config import AUTHORED_SCENE, FIXTURE_SCENE, RESOLUTIONS, RESULTS_DIR
from readback.tonefield import preview, tone_field
from render import dots
from scene import sim

TOSS = {"linear": [3.0, 0.0, 6.5], "angular": [0.0, -12.0, 0.0]}  # m/s toward the hoop and up; rad/s of backspin
FRAME_TIMES = [0.0, 0.25, 0.5, 0.75, 1.0]


def save(img: np.ndarray, path: Path) -> None:
    path.write_bytes(dots.to_png_bytes(img))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", type=Path, default=AUTHORED_SCENE if AUTHORED_SCENE.exists() else FIXTURE_SCENE)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    out = RESULTS_DIR / "step2"
    out.mkdir(parents=True, exist_ok=True)

    s = sim.load(args.scene.read_text())
    field = dots.DotField.sample(s.model, seed=args.seed)
    ball_geom = sim.ball_geom_id(s)
    on_ball = field.geom == ball_geom

    # t = 0, as written: this is the frame the readback uses.
    still = dots.draw(field, s.data)
    save(still, out / "frame_t0.png")
    for res in RESOLUTIONS:
        tone = tone_field(still, res)
        save(tone, out / f"tone_{res}.png")
        save(preview(tone), out / f"tone_{res}_preview.png")

    # Toss and record.
    jnt = s.model.body(sim.BALL).jntadr[0]
    qv = s.model.jnt_dofadr[jnt]
    s.data.qvel[qv:qv + 6] = TOSS["linear"] + TOSS["angular"]
    frames, ball_px, ball_dots = [], [], []
    for t in FRAME_TIMES:
        while s.data.time < t - 1e-9:
            mujoco.mj_step(s.model, s.data)
        frames.append(dots.draw(field, s.data))
        world, _ = field.world(s.data)
        ball_dots.append(world[on_ball])
        x, y, _ = dots.project(world[on_ball].mean(axis=0, keepdims=True))
        ball_px.append([float(x[0]), float(y[0])])
    sheet = np.concatenate([f[:, 64:448] for f in frames], axis=1)  # crop the sides so the sheet stays legible
    save(sheet, out / "contact_sheet.png")

    def pairwise(p):
        return np.linalg.norm(p[:, None] - p[None], axis=-1)

    drift = float(np.abs(pairwise(ball_dots[0][:200]) - pairwise(ball_dots[-1][:200])).max())
    moved_px = float(np.hypot(*(np.array(ball_px[-1]) - ball_px[0])))
    steps_px = [round(float(np.hypot(*(np.array(b) - a))), 1) for a, b in zip(ball_px, ball_px[1:])]
    report = {
        "scene": str(args.scene.relative_to(args.scene.parents[1])),
        "seed": args.seed,
        "dots": int(len(field.geom)),
        "dots_per_geom": {s.model.geom(int(g)).name: int((field.geom == g).sum()) for g in np.unique(field.geom)},
        "skipped_geoms": field.skipped,
        "toss": TOSS,
        "frame_times": FRAME_TIMES,
        "ball_centroid_px": [[round(v, 1) for v in b] for b in ball_px],
        "ball_moved_px_between_frames": steps_px,
        "ball_dots_max_pairwise_drift_m": drift,
        "acceptance": {
            "ball_visibly_moves": all(d > 5 for d in steps_px),
            "ball_dots_keep_arrangement": drift < 1e-9,
            "human_can_name_every_object": "look at results/step2/frame_t0.png",
        },
    }
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["acceptance"], indent=2), f"\nball moved {moved_px:.0f} px over {FRAME_TIMES[-1]} s")
    return 0 if report["acceptance"]["ball_visibly_moves"] and report["acceptance"]["ball_dots_keep_arrangement"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
