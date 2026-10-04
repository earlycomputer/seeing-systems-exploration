"""Experiment 1c, one world: a model writes it from a one-line brief, then sees and fixes it up to three times.

    python -m worlds.run --model opus-5.5 --brief catapult --arm picture --seed 0
    python -m worlds.run --model dry-run --brief door --arm picture        # plumbing test: the hand-written world

Write: the brief and the naming conventions go to the model; a file MuJoCo cannot load, or that lacks a name
the brief needs, goes back with the error (up to two times). Then up to three rounds: the picture arm is
shown its run as residue, the text arm is shown nothing and asked to check again. Each round the model says
whether the world works; if it says it does not, it sends a corrected file. The loop stops when the model is
satisfied or the rounds run out. MuJoCo's test of the brief (worlds/tests.py) judges every file; the model
never sees it. Everything goes to worlds/results/runs/<world>/<timestamp>/ (dry runs: .dryrun/worlds).
"""

from __future__ import annotations

import argparse
import json
import sys
import time

from config import RENDER_SIZE, ROOT
from loop.models import MODELS, extract_block, open_chat, png, text
from readback.tonefield import preview, tone_field
from render import dots
from worlds import budget, draw, tests
from worlds.settings import (ARMS, BRIEFS, DRYRUN_DIR, FIXTURES_DIR, MAX_LOAD_RETRIES, MAX_ROUNDS, RES, RUNS_DIR,
                             SIM_SECONDS, SPEND_LEDGER, VIEW, WORLDS_DIR)

SYSTEM = "You build MuJoCo scenes that do what their briefs say, and you check them honestly."
PROMPTS = WORLDS_DIR / "prompts"


def world_id(model: str, brief: str, arm: str, seed: int) -> str:
    return f"{model}__{brief}__{arm}__s{seed}"


def prompt(name: str, **kw) -> str:
    s = (PROMPTS / f"{name}.md").read_text()
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def parse_verdict(reply: str) -> dict:
    block = extract_block(reply, "json")
    if block is None:
        return {"parse_error": "no ```json block"}
    try:
        v = json.loads(block)
    except json.JSONDecodeError as e:
        return {"parse_error": f"bad json: {e}"}
    w = v.get("works")
    v["works_bool"] = w if isinstance(w, bool) else (str(w).strip().lower() in ("true", "yes") if w is not None else None)
    return v


def picture(xml_run: tests.Run, seed: int, out, tag: str) -> tuple[list[dict], dict]:
    field = dots.DotField.sample(xml_run.model, seed=seed)
    img, info = draw.render(VIEW, field, xml_run)
    tone = tone_field(img, RES)
    tone_png = dots.to_png_bytes(tone)
    (out / f"{tag}_render_512.png").write_bytes(dots.to_png_bytes(img))
    (out / f"{tag}_tone_{RES}.png").write_bytes(tone_png)
    (out / f"{tag}_tone_{RES}_preview.png").write_bytes(dots.to_png_bytes(preview(tone)))
    ts = info["times"]
    dt = ts[1] - ts[0] if len(ts) > 1 else 0.0
    if info["view"] == "drafting":
        view = prompt("view_drafting", scale=f"{info['scale_px_per_m'] * RES / RENDER_SIZE:.2f}",
                      x0=f"{info['x'][0]:g}", x1=f"{info['x'][1]:g}", z0=f"{info['z'][0]:g}", z1=f"{info['z'][1]:g}",
                      y0=f"{info['y'][0]:g}", y1=f"{info['y'][1]:g}")
    else:
        fmt = lambda v: ", ".join(f"{x:.2f}" for x in v)  # noqa: E731
        view = prompt("view_camera", eye=fmt(info["eye"]), target=fmt(info["target"]), fovy=f"{info['fovy']:g}")
    about = prompt("see_picture", seconds=f"{SIM_SECONDS:g}", dt=f"{dt:.2f}", end=f"{ts[-1]:.2f}", view=view.strip(),
                   res=RES, block=RENDER_SIZE // RES)
    return [text(about), png(tone_png)], {k: v for k, v in info.items()}


def judge_file(brief: str, xml: str | None, label: str, out) -> dict:
    if xml is None:
        return {"loaded": False, "problem": "I could not find a ```xml block in your reply.", "label": label}
    (out / f"{label}.xml").write_text(xml)
    j = tests.judge(brief, xml)
    j["label"] = label
    return j


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--brief", required=True, choices=list(BRIEFS))
    ap.add_argument("--arm", required=True, choices=ARMS)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--effort", default="high")
    args = ap.parse_args(argv)

    spec = MODELS[args.model]
    dry = spec.provider == "dry"
    wid = world_id(args.model, args.brief, args.arm, args.seed)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    out = (DRYRUN_DIR / "runs" if dry else RUNS_DIR) / wid / stamp
    out.mkdir(parents=True, exist_ok=True)
    B = BRIEFS[args.brief]
    first = prompt("author", brief=B["brief"], names=B["names"], seconds=f"{SIM_SECONDS:g}")
    (out / "author_prompt.md").write_text(first)

    script = None
    if dry:  # "dry-run" writes the hand-written world and says it works; "dry-run-echo" writes an empty floor
        fixture = (FIXTURES_DIR / f"{args.brief}.xml").read_text()
        empty = '<mujoco><option timestep="0.002"/><worldbody><geom name="floor" type="plane" size="5 5 0.1"/></worldbody></mujoco>\n'
        ok = '```json\n{"what_happens": "dry run", "works": true, "problem": ""}\n```'
        script = [f"```xml\n{fixture if args.model == 'dry-run' else empty}```"] + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)
    chat = open_chat(args.model, SYSTEM, args.effort, tag=f"1c/{wid}", script=script, ledger=SPEND_LEDGER)

    rec = {"world": wid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp, "experiment": "1c",
           "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
           "brief": args.brief, "brief_text": B["brief"], "arm": args.arm, "seed": args.seed, "view": VIEW,
           "res": RES, "dry_run": dry, "turns": [], "files": []}
    calls, t0 = [], time.monotonic()

    def send(parts, name):
        if not dry:
            budget.check()
        r = chat.send(parts)
        calls.append(r)
        (out / f"{name}_reply.md").write_text(r.text + ("\n\n---\nthinking (summarized):\n\n" + r.thinking
                                                        if r.thinking else ""))
        (out / f"{name}_raw.json").write_text(json.dumps(r.raw, indent=2, default=str) + "\n")
        return r

    # Write, with up to MAX_LOAD_RETRIES chances to fix a file that will not load or lacks a name.
    message, current = [text(first)], None
    for attempt in range(MAX_LOAD_RETRIES + 1):
        r = send(message, f"write{attempt}")
        j = judge_file(args.brief, extract_block(r.text, "xml"), f"written{attempt}", out)
        rec["files"].append(tests.public({**j, "turn": f"write{attempt}"}) | {"run": None})
        rec["turns"].append({"turn": f"write{attempt}", "usage": r.summary(), "problem": j.get("problem")})
        current = j
        if not j.get("problem"):
            break
        message = [text(prompt("load_problem", problem=j["problem"]))]
    rec["loads"] = not current.get("problem")
    rec["load_attempts"] = len([t for t in rec["turns"] if t["turn"].startswith("write")])
    rec["passes_first"] = bool(current.get("passed"))
    passed_at = 0 if rec["passes_first"] else None

    # See and fix.
    rounds = 0
    if rec["loads"]:
        for rnd in range(1, MAX_ROUNDS + 1):
            rounds = rnd
            if current.get("problem"):
                parts = [text(prompt("load_problem", problem=current["problem"]))]
                verb = None
            elif args.arm == "picture":
                parts, info = picture(current["run"], args.seed, out, f"round{rnd}")
                (out / f"round{rnd}_view.json").write_text(json.dumps(info, indent=2, default=str) + "\n")
                verb = "you see happen"
            else:
                parts, verb = [text(prompt("see_text"))], "you expect to happen"
            if verb:
                parts = parts + [text(prompt("see_task", verb=verb))]
            (out / f"round{rnd}_prompt.md").write_text(
                "\n\n".join(p["text"] if p["type"] == "text" else "[image]" for p in parts))
            r = send(parts, f"round{rnd}")
            v = parse_verdict(r.text) if verb else {}
            xml = extract_block(r.text, "xml")
            turn = {"turn": f"round{rnd}", "verdict": v, "usage": r.summary(),
                    "current_passed": bool(current.get("passed")), "sent_file": xml is not None}
            if xml is not None:
                current = judge_file(args.brief, xml, f"round{rnd}", out)
                rec["files"].append(tests.public({**current, "turn": f"round{rnd}"}) | {"run": None})
                turn["new_file_passed"] = bool(current.get("passed"))
                if current.get("passed") and passed_at is None:
                    passed_at = rnd
            rec["turns"].append(turn)
            if xml is None and v.get("works_bool") is True:
                break  # the model is satisfied
    last_verdict = next((t["verdict"] for t in reversed(rec["turns"]) if t.get("verdict")), {})
    rec["rounds"] = rounds
    rec["passes_final"] = bool(current.get("passed"))
    rec["passed_at_round"] = passed_at
    rec["claims_works"] = last_verdict.get("works_bool")
    rec["claim_correct"] = None if rec["claims_works"] is None else rec["claims_works"] == rec["passes_final"]
    rec["final_checks"] = current.get("checks")
    rec["seconds"] = round(time.monotonic() - t0, 1)
    rec["tokens"] = {"input": sum(c.input_tokens for c in calls), "output": sum(c.output_tokens for c in calls)}
    rec["tokens"]["total"] = rec["tokens"]["input"] + rec["tokens"]["output"]
    rec["cost_usd"] = round(sum(c.cost_usd for c in calls), 6)
    rec["served_models"] = sorted({c.served_model for c in calls})
    rec["finished_at"] = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (out / "world.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{wid}: loads={rec['loads']} first={rec['passes_first']} final={rec['passes_final']} "
          f"rounds={rounds} claims={rec['claims_works']} ${rec['cost_usd']:.4f} {rec['seconds']}s -> {rec['run_dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
