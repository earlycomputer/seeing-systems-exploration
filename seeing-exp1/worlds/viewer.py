"""Build worlds/results/viewer.html: every 1c world running in 3D, with what each model was shown and said.

    python -m worlds.viewer
    python -m worlds.viewer --runs .dryrun/worlds/runs --out .dryrun/worlds/viewer.html     # against dry runs

Generated from the run files, never edited by hand. Each saved world file is run again through worlds.tests, the
same run its test judged, and the page plays that motion: every body's pose at 50 frames a second, with the
geoms as MuJoCo compiled them. A re-run whose verdict differs from the saved one stops the build. The pictures
are the exact tone fields the models were sent; the trail copies are taken at the same moments as their residue.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import time
from pathlib import Path

import mujoco
import numpy as np

from config import ROOT
from loop.models import MODELS
from worlds import budget, draw, tests
from worlds.report import load
from worlds.settings import ARMS, BRIEFS, RES, RESULTS_DIR, RUNS_DIR, SEEDS, SIM_SECONDS, WORLDS_DIR

FPS = 50  # frames sent to the page; it interpolates between them
GEOM_TYPES = {mujoco.mjtGeom.mjGEOM_PLANE: "plane", mujoco.mjtGeom.mjGEOM_SPHERE: "sphere",
              mujoco.mjtGeom.mjGEOM_CAPSULE: "capsule", mujoco.mjtGeom.mjGEOM_ELLIPSOID: "ellipsoid",
              mujoco.mjtGeom.mjGEOM_CYLINDER: "cylinder", mujoco.mjtGeom.mjGEOM_BOX: "box"}
HIDDEN_GROUP = 3  # MuJoCo's viewer hides geom groups 3 and up by default
CODE = re.compile(r"```.*?```", re.S)


def r(a, n: int) -> list:
    return np.round(np.asarray(a, dtype=float), n).tolist()


def geoms(m) -> tuple[list[dict], list[str]]:
    out, skipped = [], []
    for g in range(m.ngeom):
        kind = GEOM_TYPES.get(mujoco.mjtGeom(m.geom_type[g]))
        rgba = m.mat_rgba[m.geom_matid[g]] if m.geom_matid[g] >= 0 else m.geom_rgba[g]
        if kind is None or m.geom_group[g] >= HIDDEN_GROUP or rgba[3] == 0:
            skipped.append(m.geom(g).name or f"geom {g}")
            continue
        out.append({"name": m.geom(g).name, "b": int(m.geom_bodyid[g]), "t": kind, "s": r(m.geom_size[g], 4),
                    "p": r(m.geom_pos[g], 4), "q": r(m.geom_quat[g], 5), "c": r(rgba, 3)})
    return out, skipped


def bounds(run: tests.Run, idx: list[int]) -> tuple[list, list]:
    """Box around every non-plane geom over the run, kept near the opening scene so a body that falls away
    for good does not shrink everything else."""
    m = run.model
    gs = [g for g in range(m.ngeom) if m.geom_type[g] != mujoco.mjtGeom.mjGEOM_PLANE]
    if not gs:
        return [-1, -1, 0], [1, 1, 1]

    def centers(i):
        b = m.geom_bodyid[gs]
        R = np.stack([tests.quat_mat(run.xquat[i, k]) for k in b])
        return run.xpos[i, b] + np.einsum("gij,gj->gi", R, m.geom_pos[gs])

    rb = m.geom_rbound[gs][:, None]
    c0 = centers(0)
    lo0, hi0 = (c0 - rb).min(0), (c0 + rb).max(0)
    pad = np.maximum(2.0, hi0 - lo0)
    lo, hi = lo0.copy(), hi0.copy()
    for i in idx:
        c = centers(i)
        lo, hi = np.minimum(lo, (c - rb).min(0)), np.maximum(hi, (c + rb).max(0))
    lo, hi = np.maximum(lo, lo0 - pad), np.minimum(hi, hi0 + pad)
    lo[2] = min(lo[2], 0.0)
    return r(lo, 3), r(hi, 3)


def motion(run: tests.Run) -> dict:
    m = run.model
    stride = max(1, round(1 / FPS / m.opt.timestep))
    idx = list(range(0, len(run.times), stride))
    if idx[-1] != len(run.times) - 1:
        idx.append(len(run.times) - 1)
    moving = draw.moving_bodies(run)
    bodies = []
    for b in range(1, m.nbody):
        if b in moving:
            bodies.append({"b": b, "name": m.body(b).name, "p": r(run.xpos[idx, b].ravel(), 4),
                           "q": r(run.xquat[idx, b].ravel(), 5)})
        else:
            bodies.append({"b": b, "name": m.body(b).name, "p": r(run.xpos[0, b], 4), "q": r(run.xquat[0, b], 5)})
    lo, hi = bounds(run, idx)
    return {"t": r(run.times[idx], 3), "bodies": bodies, "moving": moving, "trail": draw.copy_times(run, moving),
            "lo": lo, "hi": hi, "diverged": run.diverged}


def png64(path: Path) -> str | None:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode() if path.exists() else None


def said(v: dict | None) -> dict | None:
    if not v:
        return None
    return {"what": v.get("what_happens"), "works": v.get("works_bool"), "problem": v.get("problem") or None,
            "error": v.get("parse_error")}


def prose(reply: Path) -> str:
    """What the model said around its file on the first write, without the file or its thinking."""
    if not reply.exists():
        return ""
    s = reply.read_text().split("\n\n---\nthinking (summarized):")[0]
    return CODE.sub("", s).strip()


def world_entry(w: dict) -> dict:
    d = ROOT / w["run_dir"]
    turns = {t["turn"]: t for t in w["turns"]}
    versions = []
    for f in w["files"]:
        label = f["label"]
        xml_path = d / f"{label}.xml"
        xml = xml_path.read_text() if xml_path.exists() else None
        v = {"label": label, "turn": f["turn"], "loaded": f.get("loaded"), "problem": f.get("problem"),
             "passed": bool(f.get("passed")), "checks": f.get("checks") or {}, "values": f.get("values") or {},
             "xml": xml, "shown": None}
        if xml is not None and f.get("loaded"):
            j = tests.judge(w["brief"], xml)
            if bool(j.get("passed")) != v["passed"] or (j.get("checks") or {}) != v["checks"]:
                raise SystemExit(f"{w['world']} {label}: the re-run's verdict differs from the saved one")
            if j.get("run") is not None:
                m = j["run"].model
                v["geoms"], v["skipped"] = geoms(m)
                v["anim"] = motion(j["run"])
        versions.append(v)

    # Each see-and-fix round looked at the file current at that round: the last file written before it.
    current = None
    for t in w["turns"]:
        if t["turn"].startswith("write"):
            current = next(i for i, v in enumerate(versions) if v["turn"] == t["turn"])
            continue
        n = int(t["turn"].removeprefix("round"))
        if current is not None and versions[current]["shown"] is None:
            versions[current]["shown"] = {"round": n, "said": said(t.get("verdict")),
                                          "image": png64(d / f"round{n}_tone_{RES}.png") if w["arm"] == "picture" else None,
                                          "sent_file": t.get("sent_file")}
        if t.get("sent_file"):
            current = next(i for i, v in enumerate(versions) if v["turn"] == t["turn"])

    return {"id": w["world"], "model": w["model"], "brief": w["brief"], "arm": w["arm"], "seed": w["seed"],
            "passes_first": w["passes_first"], "passes_final": w["passes_final"],
            "passed_at_round": w["passed_at_round"], "claims_works": w["claims_works"],
            "claim_correct": w["claim_correct"], "rounds": w["rounds"], "cost": w["cost_usd"],
            "seconds": w["seconds"], "intro": prose(d / "write0_reply.md"), "dir": w["run_dir"],
            "versions": versions}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=RUNS_DIR)
    ap.add_argument("--out", type=Path, default=RESULTS_DIR / "viewer.html")
    args = ap.parse_args(argv)

    worlds = sorted(load(args.runs), key=lambda w: w["world"])
    entries = []
    for w in worlds:
        t0 = time.monotonic()
        entries.append(world_entry(w))
        print(f"{w['world']}: {len(entries[-1]['versions'])} file(s), {time.monotonic() - t0:.1f}s")
    s = budget.spent()
    data = {
        "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "seconds": SIM_SECONDS, "res": RES, "fps": FPS,
        "spent_1c": round(sum(w["cost_usd"] for w in worlds), 2), "spent_all": round(sum(s.values()), 2),
        "models": {k: MODELS[k].label for k in ("opus-5.5", "gpt-6.1")},
        "briefs": {k: v["brief"] for k, v in BRIEFS.items()}, "arms": list(ARMS), "seeds": list(SEEDS),
        "worlds": entries,
    }
    page = (WORLDS_DIR / "viewer_template.html").read_text()
    blob = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(page.replace("/*__DATA__*/null", blob))
    print(f"{len(entries)} worlds -> {args.out} ({args.out.stat().st_size / 1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
