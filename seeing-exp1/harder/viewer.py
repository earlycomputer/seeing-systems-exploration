"""Build harder/results/viewer.html: every 1d world running in 3D, with what each model was shown and said.

    python -m harder.viewer
    python -m harder.viewer --runs .dryrun/harder/runs --out .dryrun/harder/viewer.html     # against dry runs

1c's viewer (worlds/viewer.py) with 1d's tests, briefs and breaks. Each saved world file is run again through
harder.tests, the same run its test judged, and the page plays that motion. A re-run whose verdict differs from
the saved one stops the build. A broken world's first file is the broken file as given; the page names its break.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from config import ROOT
from loop.models import MODELS
from worlds.viewer import FPS, geoms, motion, png64, prose, said
from harder import budget, tests
from harder.report import load
from harder.settings import ARMS, BREAKS, BRIEFS, HARDER_DIR, RES, RESULTS_DIR, RUNS_DIR, SEEDS, SIM_SECONDS


def world_entry(w: dict) -> dict:
    d = ROOT / w["run_dir"]
    versions = []
    for f in w["files"]:
        label = f["label"]
        xml_path = d / f"{label}.xml"
        xml = xml_path.read_text() if xml_path.exists() else None
        v = {"label": label, "turn": f["turn"], "loaded": f.get("loaded"), "problem": f.get("problem"),
             "passed": bool(f.get("passed")), "checks": f.get("checks") or {}, "values": f.get("values") or {},
             "xml": xml, "shown": None}
        if xml is not None and f.get("loaded"):
            j = tests.judge(w["test"], xml)
            if bool(j.get("passed")) != v["passed"] or (j.get("checks") or {}) != v["checks"]:
                raise SystemExit(f"{w['world']} {label}: the re-run's verdict differs from the saved one")
            if j.get("run") is not None:
                v["geoms"], v["skipped"] = geoms(j["run"].model)
                v["anim"] = motion(j["run"])
        versions.append(v)

    # Each see-and-fix round looked at the file current at that round: the given file, or the last one written.
    current = next((i for i, v in enumerate(versions) if v["turn"] == "given"), None)
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

    return {"id": w["world"], "model": w["model"], "brief": w["brief"], "kind": w["kind"], "arm": w["arm"],
            "seed": w["seed"], "passes_first": w["passes_first"], "passes_final": w["passes_final"],
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
        "spent_1d": round(sum(w["cost_usd"] for w in worlds), 2), "spent_all": round(sum(s.values()), 2),
        "models": {k: MODELS[k].label for k in ("opus-5.5", "gpt-6.1")},
        "briefs": {k: v["brief"] for k, v in BRIEFS.items()}, "kinds": {k: v["kind"] for k, v in BRIEFS.items()},
        "breaks": {k: v[2] for k, v in BREAKS.items()}, "arms": list(ARMS), "seeds": list(SEEDS),
        "worlds": entries,
    }
    page = (HARDER_DIR / "viewer_template.html").read_text()
    blob = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(page.replace("/*__DATA__*/null", blob))
    print(f"{len(entries)} worlds -> {args.out} ({args.out.stat().st_size / 1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
