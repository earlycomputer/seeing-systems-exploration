"""Build outcome/results/viewer.html: every 1b shot animated, and every run's readback, words and corrections.

    python -m outcome.viewer

Generated from the run files, never edited by hand. MuJoCo re-flies each saved scene (the deliberate miss and
each correction) so the page draws the real flights; the images are the exact tone fields the models were sent.
"""

from __future__ import annotations

import base64
import json
import time

import mujoco
import numpy as np

from loop.models import MODELS
from outcome import budget, shot
from outcome.report import LABEL, load_runs
from outcome.settings import (BASE_RECORD, BASE_SCENE, CONDITIONS, DRAFT_PLAN_Y, DRAFT_SIDE_Z, DRAFT_X, MISSES,
                              OUTCOME_DIR, RESULTS_DIR, RUNS_DIR, SEEDS)
from scene import sim

SAMPLE_S = 0.02  # flight samples sent to the page


def flight(xml: str) -> dict:
    j = shot.judge(xml)
    f = j["_real"]
    stride = max(1, round(SAMPLE_S / (f.times[1] - f.times[0])))
    idx = list(range(0, len(f.times), stride))
    if idx[-1] != len(f.times) - 1:
        idx.append(len(f.times) - 1)
    return {"t": [round(float(f.times[i]), 3) for i in idx], "p": f.pos[idx].round(3).tolist(),
            "outcome": j["outcome"], "made": j["made"], "landed": j["landed_at_s"],
            "along": j["along"], "across": j["across"], "speed": j["launch_speed"],
            "elev": j["launch_elevation_deg"], "azim": j["launch_azimuth_deg"]}


def geometry(xml: str) -> dict:
    """Axis-aligned extents of every box, and every capsule as a segment, in world coordinates."""
    s = shot.load(xml).loaded
    m, d = s.model, s.data
    boxes, segs = [], []
    for g in range(m.ngeom):
        t, name = int(m.geom_type[g]), m.geom(g).name
        R, p, size = d.geom_xmat[g].reshape(3, 3), d.geom_xpos[g], m.geom_size[g]
        if t == mujoco.mjtGeom.mjGEOM_BOX:
            corners = np.array([[sx, sy, sz] for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)]) * size
            w = corners @ R.T + p
            boxes.append({"name": name, "lo": w.min(0).round(4).tolist(), "hi": w.max(0).round(4).tolist()})
        elif t == mujoco.mjtGeom.mjGEOM_CAPSULE:
            half = R[:, 2] * size[1]
            segs.append({"name": name, "a": (p - half).round(4).tolist(), "b": (p + half).round(4).tolist(),
                         "r": round(float(size[0]), 4)})
    return {"boxes": boxes, "segs": segs, "ball_r": float(m.geom_size[sim.ball_geom_id(s)][0]),
            "rim": shot.load(xml).rim.round(4).tolist()}


def png64(path) -> str | None:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode() if path.exists() else None


def run_entry(r: dict) -> dict:
    d = OUTCOME_DIR.parent / r["run_dir"]
    turns = {t["turn"]: t for t in r["turns"]}
    v1 = turns[1]["verdict"]
    e = {"cell": r["cell"], "model": r["model"], "condition": r["condition"], "miss": r["miss"], "seed": r["seed"],
         "truth": r["truth_label"], "named": r.get("named"), "named_ok": r.get("named_correctly"),
         "made1": r.get("made_after_one"), "made2": r.get("made_after_two"),
         "said": v1.get("description") or v1.get("parse_error"), "evidence": v1.get("evidence"),
         "cost": r["cost_usd"], "tokens": r["tokens"]["total"], "dir": r["run_dir"],
         "rescored": bool(r.get("superseded")), "corrections": []}
    res = r["condition"].split("_")[1] if "_" in r["condition"] else None
    if res:
        e["seen1"] = png64(d / f"t1_tone_{res}.png")
        e["seen3"] = png64(d / f"t3_tone_{res}.png")
    for n, turn in ((1, 2), (2, 3)):
        c = (turns.get(turn) or {}).get("correction")
        f = d / f"scene_corrected_{n}.xml"
        if c and c.get("loaded") and f.exists():
            e["corrections"].append({"n": n, "valid": c.get("made_valid"), "qvel": c.get("qvel", [])[:3],
                                     "flight": flight(f.read_text())})
        elif c is not None:
            e["corrections"].append({"n": n, "problem": c.get("problem") or "did not run"})
    if 3 in turns:
        v3 = turns[3].get("verdict") or {}
        e["said3"] = v3.get("description")
        e["goes_in3"] = v3.get("goes_in")
        e["shown3"] = (turns[3].get("shown") or {}).get("outcome")
    return e


def main() -> int:
    base = BASE_SCENE.read_text()
    rec = json.loads(BASE_RECORD.read_text())
    shots = {}
    for miss in MISSES:
        step = rec["misses"][miss]["step"]
        xml, _ = shot.inject(base, miss, step)
        shots[miss] = {"step": step, "kind": MISSES[miss]["kind"], "flight": flight(xml)}
    runs = sorted(load_runs(RUNS_DIR), key=lambda r: r["cell"])
    s = budget.spent()
    data = {
        "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "total_cells": len(CONDITIONS) * len(MISSES) * len(SEEDS) * 2, "spent_1b": round(s["exp1b"], 2),
        "models": {k: MODELS[k].label for k in ("opus-5.5", "gpt-6.1")},
        "conditions": {c: LABEL[c] for c in CONDITIONS}, "misses": list(MISSES), "seeds": list(SEEDS),
        "view": {"x": DRAFT_X, "z": DRAFT_SIDE_Z, "y": DRAFT_PLAN_Y},
        "geometry": geometry(base), "base_as_written": rec["as_written"]["outcome"], "shots": shots,
        "runs": [run_entry(r) for r in runs],
    }
    page = (OUTCOME_DIR / "viewer_template.html").read_text()
    blob = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    out = RESULTS_DIR / "viewer.html"
    out.write_text(page.replace("/*__DATA__*/null", blob))
    print(f"{len(runs)} runs -> {out} ({out.stat().st_size / 1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
