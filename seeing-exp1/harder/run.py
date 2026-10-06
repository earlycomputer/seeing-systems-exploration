"""Experiment 1d, one world: a broken world to check and fix, or a new brief to write; then see and fix it.

    python -m harder.run --model opus-5.5 --brief door --arm picture --seed 0       # a broken world
    python -m harder.run --model gpt-6.1 --brief dominoes --arm text --seed 2       # a new brief
    python -m harder.run --model dry-run --brief pendulum --arm picture             # plumbing test, no calls

1c's loop (worlds/run.py), with one change. A broken world skips the write: the model gets the brief, the
naming conventions and the broken file (harder/broken/), presented as a scene to check, not as a known
failure, and the first round's readback comes with it. A new brief is written from scratch, exactly as in
1c. Then up to three see-and-fix rounds, picture or text only; the loop stops when the model is satisfied or
the rounds run out. MuJoCo's test (harder/tests.py) judges every file; the model never sees it. Everything
goes to harder/results/runs/<world>/<timestamp>/ in 1c's layout (dry runs: .dryrun/harder).
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
from worlds import draw
from harder import budget, tests
from harder.breaks import broken
from harder.settings import (ARMS, BRIEFS, DRYRUN_DIR, FIXTURES_1C, FIXTURES_DIR, HARDER_DIR, MAX_LOAD_RETRIES,
                             MAX_ROUNDS, RES, RUNS_DIR, SIM_SECONDS, SPEND_LEDGER, VIEW)

SYSTEM = "You build MuJoCo scenes that do what their briefs say, and you check them honestly."
PROMPTS = HARDER_DIR / "prompts"


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


def picture(xml_run: tests.Run, seed: int, out, tag: str, whose: str) -> tuple[list[dict], dict]:
    field = dots.DotField.sample(xml_run.model, seed=seed)
    img, info = draw.render(VIEW, field, xml_run)
    tone = tone_field(img, RES)
    tone_png = dots.to_png_bytes(tone)
    (out / f"{tag}_render_512.png").write_bytes(dots.to_png_bytes(img))
    (out / f"{tag}_tone_{RES}.png").write_bytes(tone_png)
    (out / f"{tag}_tone_{RES}_preview.png").write_bytes(dots.to_png_bytes(preview(tone)))
    ts = info["times"]
    dt = ts[1] - ts[0] if len(ts) > 1 else 0.0
    view = prompt("view_drafting", scale=f"{info['scale_px_per_m'] * RES / RENDER_SIZE:.2f}",
                  x0=f"{info['x'][0]:g}", x1=f"{info['x'][1]:g}", z0=f"{info['z'][0]:g}", z1=f"{info['z'][1]:g}",
                  y0=f"{info['y'][0]:g}", y1=f"{info['y'][1]:g}")
    about = prompt("see_picture", whose=whose, seconds=f"{SIM_SECONDS:g}", dt=f"{dt:.2f}", end=f"{ts[-1]:.2f}",
                   view=view.strip(), res=RES, block=RENDER_SIZE // RES)
    return [text(about), png(tone_png)], dict(info)


def judge_file(test: str, xml: str | None, label: str, out) -> dict:
    if xml is None:
        return {"loaded": False, "problem": "I could not find a ```xml block in your reply.", "label": label}
    (out / f"{label}.xml").write_text(xml)
    j = tests.judge(test, xml)
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
    kind, test = B["kind"], B["test"]

    script = None
    if dry:  # "dry-run" sends the hand-written world and says it works; "dry-run-echo" sends nothing new and says it works
        fixture = ((FIXTURES_DIR if kind == "new" else FIXTURES_1C) / f"{args.brief}.xml").read_text()
        empty = '<mujoco><option timestep="0.002"/><worldbody><geom name="floor" type="plane" size="5 5 0.1"/></worldbody></mujoco>\n'
        ok = '```json\n{"what_happens": "dry run", "works": true, "problem": ""}\n```'
        fix = f'```json\n{{"what_happens": "dry run", "works": false, "problem": "dry run"}}\n```\n```xml\n{fixture}```'
        good = args.model == "dry-run"
        if kind == "new":
            script = [f"```xml\n{fixture if good else empty}```"] + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)
        else:
            script = ([fix] if good else []) + [ok] * (MAX_ROUNDS + MAX_LOAD_RETRIES)
    chat = open_chat(args.model, SYSTEM, args.effort, tag=f"1d/{wid}", script=script, ledger=SPEND_LEDGER)

    rec = {"world": wid, "run_dir": str(out.relative_to(ROOT)), "started_at": stamp, "experiment": "1d",
           "model": args.model, "model_label": spec.label, "model_id": spec.model_id, "effort": args.effort,
           "brief": args.brief, "brief_text": B["brief"], "kind": kind, "test": test, "arm": args.arm,
           "seed": args.seed, "view": VIEW, "res": RES, "dry_run": dry, "turns": [], "files": []}
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

    lead = []  # text that goes before the first round's readback (a broken world's brief and file)
    if kind == "new":
        first = prompt("author", brief=B["brief"], names=B["names"], seconds=f"{SIM_SECONDS:g}")
        (out / "author_prompt.md").write_text(first)
        message, current = [text(first)], None
        for attempt in range(MAX_LOAD_RETRIES + 1):
            r = send(message, f"write{attempt}")
            j = judge_file(test, extract_block(r.text, "xml"), f"written{attempt}", out)
            rec["files"].append(tests.public({**j, "turn": f"write{attempt}"}) | {"run": None})
            rec["turns"].append({"turn": f"write{attempt}", "usage": r.summary(), "problem": j.get("problem")})
            current = j
            if not j.get("problem"):
                break
            message = [text(prompt("load_problem", problem=j["problem"]))]
        rec["load_attempts"] = len([t for t in rec["turns"] if t["turn"].startswith("write")])
    else:
        given = broken(args.brief)
        current = judge_file(test, given, "given", out)
        rec["files"].append(tests.public({**current, "turn": "given"}) | {"run": None})
        lead = [text(prompt("given", brief=B["brief"], names=B["names"], seconds=f"{SIM_SECONDS:g}", scene=given.strip()))]
        rec["load_attempts"] = 0
    rec["loads"] = not current.get("problem")
    rec["passes_first"] = bool(current.get("passed"))
    passed_at = 0 if rec["passes_first"] else None

    rounds, edited = 0, kind == "new"
    if rec["loads"]:
        for rnd in range(1, MAX_ROUNDS + 1):
            rounds = rnd
            whose = "your" if edited else "the"
            if current.get("problem"):
                parts, verb = [text(prompt("load_problem", problem=current["problem"]))], None
            elif args.arm == "picture":
                parts, info = picture(current["run"], args.seed, out, f"round{rnd}", whose)
                (out / f"round{rnd}_view.json").write_text(json.dumps(info, indent=2, default=str) + "\n")
                verb = "you see happen"
            else:
                parts = [text(prompt("see_text", whose=whose, again=" once more" if edited else ""))]
                verb = "you expect to happen"
            if verb:
                parts = parts + [text(prompt("see_task", verb=verb))]
            parts = lead + parts
            lead = []
            (out / f"round{rnd}_prompt.md").write_text(
                "\n\n".join(p["text"] if p["type"] == "text" else "[image]" for p in parts))
            r = send(parts, f"round{rnd}")
            v = parse_verdict(r.text) if verb else {}
            xml = extract_block(r.text, "xml")
            turn = {"turn": f"round{rnd}", "verdict": v, "usage": r.summary(),
                    "current_passed": bool(current.get("passed")), "sent_file": xml is not None}
            if xml is not None:
                edited = True
                current = judge_file(test, xml, f"round{rnd}", out)
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
    rec["tried_fix"] = any(t.get("sent_file") for t in rec["turns"])
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
    print(f"{wid}: kind={kind} loads={rec['loads']} first={rec['passes_first']} final={rec['passes_final']} "
          f"rounds={rounds} claims={rec['claims_works']} ${rec['cost_usd']:.4f} {rec['seconds']}s -> {rec['run_dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
