"""One cell of the matrix: break the scene, render it, read it back, let the model correct it, measure.

    python -m loop.run --model opus-5.5 --res 64 --error hoop_low --seed 0
    python -m loop.run --model opus-5.5 --res 128 --error none --seed 0            # control: unmodified
    python -m loop.run --model opus-5.5 --res 128 --error hoop_low --image-only    # control: no scene text
    python -m loop.run --model dry-run --res 64 --error hoop_low                   # plumbing test, no API calls

Every prompt, reply, image and measurement goes to results/runs/<cell>/<timestamp>/ (dry runs go to
.dryrun/ instead and never reach results.md). Judged by MuJoCo state, never by eye.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import sys
import time
from pathlib import Path

import mujoco

from config import (AUTHORED_SCENE, BRIEF_FILE, DRYRUN_DIR, FIXTURE_SCENE, RENDER_SIZE, RESOLUTIONS, ROOT,
                    RUNS_DIR, TARGETS)
from loop.models import MODELS, extract_block, open_chat, png, text
from readback.tonefield import preview, tone_field
from render import dots
from scene import sim

SYSTEM = "You check physics scenes against their briefs. Be concrete, and say plainly when you cannot tell."


def cell_id(model: str, res: int, error: str, seed: int, image_only: bool) -> str:
    return f"{model}__{res}__{error}__s{seed}" + ("__image-only" if image_only else "")


def top_level_objects(model: mujoco.MjModel) -> list[str]:
    names = [model.body(b).name for b in range(1, model.nbody) if model.body_parentid[b] == 0]
    return [n for n in names if n] + ["floor", "none"]


def readback_parts(brief: str, scene_xml: str | None, tone_png: bytes, res: int, objects: list[str]) -> list[dict]:
    here = ROOT / "readback"
    scene_section = (
        "The scene text, as currently loaded:\n\n```xml\n" + scene_xml + "```" if scene_xml is not None
        else "The scene text is withheld for this check; you have only the picture.")
    fmt = lambda v: ", ".join(f"{x:.2f}" for x in v)  # noqa: E731
    intro = (here / "prompt.md").read_text().format(
        brief=brief, scene_section=scene_section, eye=fmt(dots.CAMERA_EYE), target=fmt(dots.CAMERA_TARGET),
        fovy=f"{dots.CAMERA_FOVY_DEG:g}", res=res, block=RENDER_SIZE // res)
    task = (here / "task.md").read_text().replace("{objects}", " | ".join(f'"{o}"' for o in objects))
    return [text(intro), png(tone_png), text(task)]


def parse_readback(reply: str) -> tuple[dict | None, str | None]:
    block = extract_block(reply, "json")
    if block is None:
        return None, "no ```json block"
    try:
        return json.loads(block), None
    except json.JSONDecodeError as e:
        return None, f"bad json: {e}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--res", type=int, required=True, choices=RESOLUTIONS)
    ap.add_argument("--error", required=True, choices=["none", *sim.ERRORS])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--image-only", action="store_true", help="withhold the scene text (control); no correction turn")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--scene", type=Path, default=None, help="defaults to scene/authored.xml (dry runs: the fixture)")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    scene_path = args.scene or (FIXTURE_SCENE if dry else AUTHORED_SCENE)
    if not dry and scene_path.resolve() != AUTHORED_SCENE.resolve():
        print("real runs use scene/authored.xml only; run python -m scene.author first", file=sys.stderr)
        return 1
    if not scene_path.exists():
        print(f"{scene_path} does not exist; run python -m scene.author first", file=sys.stderr)
        return 1

    cid = cell_id(args.model, args.res, args.error, args.seed, args.image_only)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / cid / stamp
    out.mkdir(parents=True, exist_ok=True)
    error = sim.ERRORS.get(args.error, sim.NONE)

    base_xml = scene_path.read_text()
    brief = BRIEF_FILE.read_text().strip()
    base = sim.load(base_xml)
    bad_xml, edit = sim.inject(base_xml, args.error)
    bad = sim.load(bad_xml)
    (out / "scene_injected.xml").write_text(bad_xml)

    field = dots.DotField.sample(bad.model, seed=args.seed)
    img = dots.draw(field, bad.data)
    tone = tone_field(img, args.res)
    tone_png = dots.to_png_bytes(tone)
    (out / "render_512.png").write_bytes(dots.to_png_bytes(img))
    (out / f"tone_{args.res}.png").write_bytes(tone_png)
    (out / f"tone_{args.res}_preview.png").write_bytes(dots.to_png_bytes(preview(tone)))

    objects = top_level_objects(bad.model)
    parts = readback_parts(brief, None if args.image_only else bad_xml, tone_png, args.res, objects)
    (out / "readback_prompt.md").write_text(
        "\n\n".join(p["text"] if p["type"] == "text" else f"[image: tone_{args.res}.png]" for p in parts))

    script = None
    if dry:  # dry-run: an oracle that names the right object and hands back the unbroken scene.
        oracle = args.model == "dry-run"  # dry-run-echo: names nothing and hands back the broken scene.
        script = [f'```json\n{{"description": "dry run", "mismatch": "{error.target_object if oracle else "none"}", '
                  f'"what_is_wrong": "dry run", "evidence": "none"}}\n```',
                  f"```xml\n{base_xml if oracle else bad_xml}```"]
    chat = open_chat(args.model, SYSTEM, args.effort, tag=cid, script=script)

    run = {
        "cell": cid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp,
        "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
        "resolution": args.res, "error": args.error, "error_label": error.label, "seed": args.seed,
        "condition": "image_only" if args.image_only else "with_text", "dry_run": dry,
        "scene": str(scene_path.relative_to(ROOT)),
        "scene_sha256": hashlib.sha256(base_xml.encode()).hexdigest(),
        "edit": edit, "load_log": base.log + bad.log, "dots": int(len(field.geom)), "skipped_geoms": field.skipped,
        "targets": TARGETS, "objects_offered": objects, "expected_mismatch": error.target_object,
        "measurements": {"baseline": sim.measure(base), "injected": sim.measure(bad)},
    }

    # Turn 1: readback.
    r1 = chat.send(parts)
    (out / "readback_reply.md").write_text(r1.text + ("\n\n---\nthinking (summarized):\n\n" + r1.thinking
                                                      if r1.thinking else ""))
    (out / "readback_raw.json").write_text(json.dumps(r1.raw, indent=2, default=str) + "\n")
    parsed, parse_error = parse_readback(r1.text)
    named = (parsed or {}).get("mismatch")
    named = named.strip().lower() if isinstance(named, str) else None
    run["readback"] = {"parsed": parsed, "parse_error": parse_error, "named": named,
                       "named_correctly": named == error.target_object, "usage": r1.summary()}
    calls = [r1]

    # Turn 2: correction (only when the model has the text to correct).
    if args.image_only:
        run["correction"] = None
        run["fixed_within_tolerance"] = None
    else:
        r2 = chat.send([text((ROOT / "readback" / "correction.md").read_text())])
        calls.append(r2)
        (out / "correction_reply.md").write_text(r2.text + ("\n\n---\nthinking (summarized):\n\n" + r2.thinking
                                                            if r2.thinking else ""))
        (out / "correction_raw.json").write_text(json.dumps(r2.raw, indent=2, default=str) + "\n")
        fixed_xml = extract_block(r2.text, "xml")
        corr = {"usage": r2.summary(), "loaded": False, "load_error": None, "diff_vs_injected": None}
        fixed = False
        if fixed_xml is None:
            corr["load_error"] = "no ```xml block"
        else:
            (out / "scene_corrected.xml").write_text(fixed_xml)
            corr["diff_vs_injected"] = "".join(difflib.unified_diff(
                bad_xml.splitlines(True), fixed_xml.splitlines(True), "injected", "corrected", n=0))
            try:
                fixed_scene = sim.load(fixed_xml)
                m = sim.measure(fixed_scene)
                run["measurements"]["corrected"] = m
                corr["loaded"] = True
                corr["load_log"] = fixed_scene.log
                corr["within"] = {k: sim.within(m, k) for k in TARGETS}
                fixed = all(corr["within"].values()) if error.key == "none" else corr["within"][error.measured]
                corr["collateral"] = [k for k, ok in corr["within"].items() if not ok and k != error.measured]
            except Exception as e:  # a correction that does not load is a failed correction, and data
                corr["load_error"] = str(e)
        run["correction"] = corr
        run["fixed_within_tolerance"] = fixed

    run["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    run["tokens"]["total"] = run["tokens"]["input"] + run["tokens"]["output"]
    run["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    run["served_models"] = sorted({c.served_model for c in calls})
    run["stop_reasons"] = [c.stop_reason for c in calls]
    run["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "run.json").write_text(json.dumps(run, indent=2) + "\n")

    fixed_s = "n/a" if run["fixed_within_tolerance"] is None else run["fixed_within_tolerance"]
    print(f"{cid}: named={named!r} correct={run['readback']['named_correctly']} fixed={fixed_s} "
          f"tokens={run['tokens']['total']} ${run['cost_usd']:.4f} -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
