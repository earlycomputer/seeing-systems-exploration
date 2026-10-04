"""Experiment 1b, one cell: miss the shot on purpose, read back the outcome, let the model correct it.

    python -m outcome.run --model opus-5.5 --condition camera_64 --miss short --seed 0
    python -m outcome.run --model dry-run --condition drafting_64 --miss left     # plumbing test, no API calls

Turn 1: the readback (or the scene text alone); will it go in, and if not, short, long, left or right?
Turn 2: correct the keyframe. Turn 3, every condition but text only: the corrected shot's readback, made
the same way, and one more correction if the model says it still misses.

Judged by MuJoCo: direction named correctly; made after one correction; made after two. A correction
counts only if it changed nothing but the keyframe and the ball still starts where it rests. Every prompt,
reply, image and measurement goes to outcome/results/runs/<cell>/<timestamp>/ (dry runs: .dryrun/outcome).
"""

from __future__ import annotations

import argparse
import json
import sys
import time

import numpy as np

from config import RENDER_SIZE, ROOT
from loop.models import MODELS, extract_block, open_chat, png, text
from outcome import author, budget, draw, shot
from outcome.settings import (BASE_RECORD, BASE_SCENE, CONDITIONS, DRAFT_PLAN_Y, DRAFT_SIDE_Z, DRAFT_X,
                              DRYRUN_DIR, MISSES, NUMBERS_EVERY_S, OUTCOME_DIR, RESIDUE_EVERY_S, RUNS_DIR,
                              SPEND_LEDGER)
from readback.tonefield import preview, tone_field
from render import dots

SYSTEM = "You check physics scenes against their briefs. Be concrete, and say plainly when you cannot tell."
PROMPTS = OUTCOME_DIR / "prompts"
EVIDENCE = {"text": '"text" or "none"', "numbers": '"numbers", "text", "both" or "none"'}
LOOK_VERB = {"text": "predict", "numbers": "read in the numbers"}


def cell_id(model: str, condition: str, miss: str, seed: int) -> str:
    return f"{model}__{condition}__{miss}__s{seed}"


def view_of(condition: str) -> tuple[str, int | None]:
    if condition in ("text", "numbers"):
        return condition, None
    view, res = condition.split("_")
    return view, int(res)


def readback(condition: str, xml: str, seed: int, out, tag: str) -> tuple[list[dict], dict]:
    """The parts that show the model this shot's outcome, and what MuJoCo says the outcome is."""
    j = shot.judge(xml)
    flight = j["_real"]
    view, res = view_of(condition)
    fmt = lambda v: ", ".join(f"{x:.2f}" for x in v)  # noqa: E731
    if view == "text":
        parts = [text((PROMPTS / "view_text.md").read_text())]
    elif view == "numbers":
        rows = draw.numbers(flight)
        (out / f"{tag}_numbers.json").write_text(json.dumps(rows) + "\n")
        parts = [text((PROMPTS / "view_numbers.md").read_text().format(
            every=f"{NUMBERS_EVERY_S:g}", table=draw.numbers_table(rows)))]
    else:
        s = shot.load(xml)
        field = dots.DotField.sample(s.loaded.model, seed=seed)
        img = draw.render(view, field, s, flight)
        tone = tone_field(img, res)
        tone_png = dots.to_png_bytes(tone)
        (out / f"{tag}_render_512.png").write_bytes(dots.to_png_bytes(img))
        (out / f"{tag}_tone_{res}.png").write_bytes(tone_png)
        (out / f"{tag}_tone_{res}_preview.png").write_bytes(dots.to_png_bytes(preview(tone)))
        about = (PROMPTS / f"view_{view}.md").read_text().format(
            every=f"{RESIDUE_EVERY_S:g}", eye=fmt(dots.CAMERA_EYE), target=fmt(dots.CAMERA_TARGET),
            fovy=f"{dots.CAMERA_FOVY_DEG:g}", res=res, block=RENDER_SIZE // res,
            scale=f"{draw.DRAFT_SCALE * res / RENDER_SIZE:.2f}", x0=f"{DRAFT_X[0]:g}", x1=f"{DRAFT_X[1]:g}",
            z0=f"{DRAFT_SIDE_Z[0]:g}", z1=f"{DRAFT_SIDE_Z[1]:g}", y0=f"{DRAFT_PLAN_Y[0]:g}",
            y1=f"{DRAFT_PLAN_Y[1]:g}")
        parts = [text(about), png(tone_png)]
    return parts, shot.public(j)


def task_text(condition: str) -> str:
    view, _ = view_of(condition)
    return (PROMPTS / "task.md").read_text().replace("{look_verb}", LOOK_VERB.get(view, "see")).replace(
        "{evidence}", EVIDENCE.get(view, '"picture", "text", "both" or "none"'))


def parse_verdict(reply: str) -> dict:
    block = extract_block(reply, "json")
    if block is None:
        return {"parse_error": "no ```json block"}
    try:
        v = json.loads(block)
    except json.JSONDecodeError as e:
        return {"parse_error": f"bad json: {e}"}
    miss = v.get("miss")
    v["miss_named"] = miss.strip().lower() if isinstance(miss, str) else None
    return v


def judge_correction(miss_xml: str, fixed_xml: str | None) -> tuple[dict, str | None]:
    """MuJoCo's verdict on a corrected file, and the problem to send back if it cannot be run."""
    if fixed_xml is None:
        return {"loaded": False, "problem": "no ```xml block"}, "I could not find a ```xml block in your reply."
    try:
        j = shot.judge(fixed_xml)
    except Exception as e:  # a correction that does not load is a failed correction, and data
        return {"loaded": False, "problem": str(e)}, str(e)
    other = author.other_changes(miss_xml, fixed_xml)
    start = j["_real"].pos[0]
    rest = shot.judge(miss_xml)["_real"].pos[0]
    moved = float(np.linalg.norm(start - rest))
    out = {"loaded": True, "judged": shot.public(j), "other_changes": other, "start_moved_m": round(moved, 4),
           "qvel": shot.shot_qvel(fixed_xml)}
    out["made"] = j["made"]
    out["made_valid"] = j["made"] and not other and moved < 0.01
    return out, None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--condition", required=True, choices=CONDITIONS)
    ap.add_argument("--miss", required=True, choices=list(MISSES))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    scene_dir = DRYRUN_DIR / "scene" if dry else BASE_SCENE.parent
    base_path, record_path = scene_dir / BASE_SCENE.name, scene_dir / BASE_RECORD.name
    if not base_path.exists():
        print(f"{base_path} does not exist; run python -m outcome.author first", file=sys.stderr)
        return 1
    record = json.loads(record_path.read_text())
    step = record["misses"][args.miss]["step"]
    if step is None:
        print(f"the {args.miss} miss is not clear-cut on this base; a human decides next", file=sys.stderr)
        return 1

    cid = cell_id(args.model, args.condition, args.miss, args.seed)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / cid / stamp
    out.mkdir(parents=True, exist_ok=True)

    base_xml = base_path.read_text()
    brief = (OUTCOME_DIR / "scene" / "brief.txt").read_text().strip()
    miss_xml, edit = shot.inject(base_xml, args.miss, step)
    (out / "scene_miss.xml").write_text(miss_xml)
    parts, truth = readback(args.condition, miss_xml, args.seed, out, "t1")
    truth_label = "none" if truth["made"] else truth["direction"]
    intro = (PROMPTS / "intro.md").read_text().replace("{brief}", brief).replace("{scene}", miss_xml)
    turn1 = [text(intro)] + parts + [text(task_text(args.condition))]
    (out / "t1_prompt.md").write_text("\n\n".join(p["text"] if p["type"] == "text" else "[image]" for p in turn1))

    script = None
    if dry:  # "dry-run" names the truth and hands back the base; "dry-run-echo" says it goes in and changes nothing
        oracle = args.model == "dry-run"
        named = truth_label if oracle else "none"
        verdict = f'```json\n{{"description": "dry run", "goes_in": {str(named == "none").lower()}, "miss": "{named}", "evidence": "none"}}\n```'
        script = [verdict, f"```xml\n{base_xml if oracle else miss_xml}```",
                  '```json\n{"description": "dry run", "goes_in": true, "miss": "none", "evidence": "none"}\n```']
    chat = open_chat(args.model, SYSTEM, args.effort, tag=f"1b/{cid}", script=script, ledger=SPEND_LEDGER)

    run = {
        "cell": cid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp, "experiment": "1b",
        "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
        "condition": args.condition, "miss": args.miss, "seed": args.seed, "dry_run": dry,
        "base": base_path.name, "edit": edit, "truth": truth, "truth_label": truth_label, "turns": [],
    }
    calls = []

    def send(parts_, name):
        if not dry:
            budget.check()
        r = chat.send(parts_)
        calls.append(r)
        (out / f"{name}_reply.md").write_text(r.text + ("\n\n---\nthinking (summarized):\n\n" + r.thinking
                                                        if r.thinking else ""))
        (out / f"{name}_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
        return r

    # Turn 1: will it go in?
    r1 = send(turn1, "t1")
    v1 = parse_verdict(r1.text)
    run["turns"].append({"turn": 1, "verdict": v1, "usage": r1.summary()})
    run["named"] = v1.get("miss_named")
    run["named_correctly"] = v1.get("miss_named") == truth_label

    # Turn 2: correct it.
    r2 = send([text((PROMPTS / "correct.md").read_text())], "t2")
    fixed1 = extract_block(r2.text, "xml")
    if fixed1 is not None:
        (out / "scene_corrected_1.xml").write_text(fixed1)
    c1, problem = judge_correction(miss_xml, fixed1)
    run["turns"].append({"turn": 2, "correction": c1, "usage": r2.summary()})
    run["made_after_one"] = bool(c1.get("made_valid"))

    # Turn 3: see the corrected shot (not for text only), and correct once more if needed.
    run["made_after_two"] = None
    if args.condition != "text":
        if problem is None:
            parts3, truth3 = readback(args.condition, fixed1, args.seed, out, "t3")
            msg = [text((PROMPTS / "recheck.md").read_text())] + parts3 + [text((PROMPTS / "recheck_task.md").read_text())]
        else:
            truth3 = None
            msg = [text((PROMPTS / "reload.md").read_text().replace("{problem}", problem))]
        r3 = send(msg, "t3")
        v3 = parse_verdict(r3.text) if problem is None else {}
        fixed2 = extract_block(r3.text, "xml")
        if fixed2 is not None:
            (out / "scene_corrected_2.xml").write_text(fixed2)
            c2, _ = judge_correction(miss_xml, fixed2)
            made2 = bool(c2.get("made_valid"))
        else:
            c2, made2 = None, run["made_after_one"]  # no new file: the first correction stands
        run["turns"].append({"turn": 3, "shown": truth3, "verdict": v3, "correction": c2, "usage": r3.summary()})
        if truth3 is not None:
            run["recheck_correct"] = v3.get("goes_in") == truth3["made"]
        run["made_after_two"] = made2

    run["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    run["tokens"]["total"] = run["tokens"]["input"] + run["tokens"]["output"]
    run["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    run["served_models"] = sorted({c.served_model for c in calls})
    run["stop_reasons"] = [c.stop_reason for c in calls]
    run["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "run.json").write_text(json.dumps(run, indent=2) + "\n")
    print(f"{cid}: truth={truth_label} named={run['named']!r} made1={run['made_after_one']} "
          f"made2={run['made_after_two']} tokens={run['tokens']['total']} ${run['cost_usd']:.4f} "
          f"-> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
